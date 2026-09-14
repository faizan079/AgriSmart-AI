"""
AgriSmart AI - Crop Disease Detection - Training Script
Transfer learning on ResNet18 (torchvision), fine-tuned on PlantVillage-style data.

Expected folder structure for --data_dir:
    data_dir/
        train/<class_name>/*.jpg
        val/<class_name>/*.jpg
        test/<class_name>/*.jpg   (optional local test - NEVER the organizer held-out set)

Run:
    python model/training/train.py --data_dir ./data --epochs 10
"""
import argparse
import json
import os
from copy import deepcopy

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, models, transforms


def build_model(num_classes: int) -> nn.Module:
    model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
    for param in model.parameters():
        param.requires_grad = False
    model.fc = nn.Linear(model.fc.in_features, num_classes)
    return model


def get_transforms():
    train_tf = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomRotation(15),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
        transforms.RandomAffine(degrees=0, translate=(0.1, 0.1)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    eval_tf = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    return train_tf, eval_tf


def train(data_dir: str, epochs: int, batch_size: int, lr: float, out_path: str, 
          patience: int = 5, unfreeze_epoch: int = 5):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    train_tf, eval_tf = get_transforms()

    train_ds = datasets.ImageFolder(os.path.join(data_dir, "train"), transform=train_tf)
    val_ds = datasets.ImageFolder(os.path.join(data_dir, "val"), transform=eval_tf)

    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True, num_workers=0)
    val_loader = DataLoader(val_ds, batch_size=batch_size, shuffle=False, num_workers=0)

    class_names = train_ds.classes
    num_classes = len(class_names)
    print(f"Classes ({num_classes}): {class_names}")
    print(f"Train samples: {len(train_ds)}, Val samples: {len(val_ds)}")
    
    model = build_model(num_classes=num_classes).to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.fc.parameters(), lr=lr)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='max', factor=0.5, patience=3)

    best_val_acc = 0.0
    best_model_state = None
    epochs_no_improve = 0
    training_history = {
        "train_loss": [],
        "val_acc": [],
        "learning_rate": []
    }
    
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item() * images.size(0)

        train_loss = running_loss / len(train_ds)

        model.eval()
        correct, total = 0, 0
        val_loss = 0.0
        with torch.no_grad():
            for images, labels in val_loader:
                images, labels = images.to(device), labels.to(device)
                outputs = model(images)
                loss = criterion(outputs, labels)
                val_loss += loss.item() * images.size(0)
                _, preds = torch.max(outputs, 1)
                correct += (preds == labels).sum().item()
                total += labels.size(0)
        
        val_loss = val_loss / len(val_ds)
        val_acc = correct / total if total else 0.0
        current_lr = optimizer.param_groups[0]['lr']
        
        training_history["train_loss"].append(train_loss)
        training_history["val_acc"].append(val_acc)
        training_history["learning_rate"].append(current_lr)

        print(f"Epoch {epoch+1}/{epochs} - train_loss: {train_loss:.4f} - val_loss: {val_loss:.4f} - val_acc: {val_acc:.4f} - lr: {current_lr:.6f}")

        # Learning rate scheduling
        scheduler.step(val_acc)

        # Save best model
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            best_model_state = deepcopy(model.state_dict())
            epochs_no_improve = 0
            print(f"  -> New best model saved! val_acc: {best_val_acc:.4f}")
        else:
            epochs_no_improve += 1

        # Early stopping
        if epochs_no_improve >= patience:
            print(f"Early stopping triggered after {epoch+1} epochs (patience: {patience})")
            break

        # Unfreeze backbone for fine-tuning
        if epoch + 1 == unfreeze_epoch:
            print(f"Unfreezing backbone for fine-tuning at epoch {epoch+1}")
            for param in model.parameters():
                param.requires_grad = True
            optimizer = torch.optim.Adam(model.parameters(), lr=lr * 0.1)

    # Load best model and save
    if best_model_state is not None:
        model.load_state_dict(best_model_state)
    
    torch.save({
        "model_state_dict": model.state_dict(),
        "class_names": class_names,
        "training_history": training_history,
        "best_val_acc": best_val_acc,
    }, out_path)

    # Save training history
    history_path = os.path.join(os.path.dirname(out_path), "training_history.json")
    with open(history_path, "w") as f:
        json.dump(training_history, f, indent=2)

    # Save class names
    with open(os.path.join(os.path.dirname(out_path), "classes.json"), "w") as f:
        json.dump(class_names, f, indent=2)

    print(f"\nTraining complete!")
    print(f"Best val_acc: {best_val_acc:.4f}")
    print(f"Weights saved to: {out_path}")
    print(f"Training history saved to: {history_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train AgriSmart AI Disease Detection Model")
    parser.add_argument("--data_dir", type=str, required=True, help="Path to data directory with train/val folders")
    parser.add_argument("--epochs", type=int, default=20, help="Maximum number of training epochs")
    parser.add_argument("--batch_size", type=int, default=32, help="Batch size for training")
    parser.add_argument("--lr", type=float, default=1e-3, help="Initial learning rate")
    parser.add_argument("--out", type=str, default="./model/weights/model.pt", help="Path to save model weights")
    parser.add_argument("--patience", type=int, default=5, help="Early stopping patience (epochs without improvement)")
    parser.add_argument("--unfreeze_epoch", type=int, default=5, help="Epoch to unfreeze backbone for fine-tuning")
    args = parser.parse_args()

    train(args.data_dir, args.epochs, args.batch_size, args.lr, args.out, args.patience, args.unfreeze_epoch)
