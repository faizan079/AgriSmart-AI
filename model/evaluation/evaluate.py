"""
AgriSmart AI - Evaluation Script
Computes macro-F1, confusion matrix, per-class precision/recall on a labeled test set.
NEVER point --data_dir at the organizer's held-out set for tuning - only for final reporting.

Run:
    python model/evaluation/evaluate.py --data_dir ./data/test --weights ./model/weights/model.pt
"""
import argparse
import json
import os
import sys

import torch
import torch.nn as nn
from sklearn.metrics import classification_report, confusion_matrix, f1_score
from torch.utils.data import DataLoader
from torchvision import datasets, models, transforms

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.visualization import plot_confusion_matrix, plot_per_class_metrics


def load_model(weights_path: str, device):
    checkpoint = torch.load(weights_path, map_location=device)
    class_names = checkpoint["class_names"]
    model = models.resnet18(weights=None)
    model.fc = nn.Linear(model.fc.in_features, len(class_names))
    model.load_state_dict(checkpoint["model_state_dict"])
    model.to(device).eval()
    return model, class_names


def evaluate(data_dir: str, weights_path: str, report_path: str = "report/model_report.json", 
              plot_dir: str = "report/plots"):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    model, class_names = load_model(weights_path, device)
    print(f"Loaded model with {len(class_names)} classes: {class_names}")

    eval_tf = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    test_ds = datasets.ImageFolder(data_dir, transform=eval_tf)
    test_loader = DataLoader(test_ds, batch_size=32, shuffle=False, num_workers=0)
    
    print(f"Test samples: {len(test_ds)}")

    all_preds, all_labels = [], []
    all_probs = []
    
    with torch.no_grad():
        for images, labels in test_loader:
            images = images.to(device)
            outputs = model(images)
            probs = torch.softmax(outputs, dim=1)
            _, preds = torch.max(outputs, 1)
            all_preds.extend(preds.cpu().tolist())
            all_labels.extend(labels.tolist())
            all_probs.extend(probs.cpu().tolist())

    # Calculate metrics
    macro_f1 = f1_score(all_labels, all_preds, average="macro")
    weighted_f1 = f1_score(all_labels, all_preds, average="weighted")
    accuracy = sum(1 for x, y in zip(all_preds, all_labels) if x == y) / len(all_labels)
    cm = confusion_matrix(all_labels, all_preds)
    
    # Detailed classification report
    report_dict = classification_report(all_labels, all_preds, target_names=class_names, 
                                        output_dict=True)
    report_str = classification_report(all_labels, all_preds, target_names=class_names)

    print(f"\n{'='*60}")
    print(f"EVALUATION RESULTS")
    print(f"{'='*60}")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Macro F1-Score: {macro_f1:.4f}")
    print(f"Weighted F1-Score: {weighted_f1:.4f}")
    print(f"\nConfusion Matrix:")
    print(cm)
    print(f"\nPer-class precision/recall:")
    print(report_str)
    print(f"{'='*60}\n")

    # Create output directories
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    os.makedirs(plot_dir, exist_ok=True)

    # Save detailed report
    full_report = {
        "accuracy": accuracy,
        "macro_f1": macro_f1,
        "weighted_f1": weighted_f1,
        "confusion_matrix": cm.tolist(),
        "class_names": class_names,
        "classification_report": report_dict,
        "num_samples": len(test_ds)
    }
    
    with open(report_path, "w") as f:
        json.dump(full_report, f, indent=2)
    
    print(f"Detailed report saved to: {report_path}")

    # Generate visualizations
    try:
        # Plot confusion matrix
        cm_plot_path = os.path.join(plot_dir, "confusion_matrix.png")
        plot_confusion_matrix(cm, class_names, cm_plot_path, normalize=False)
        
        # Plot normalized confusion matrix
        cm_norm_plot_path = os.path.join(plot_dir, "confusion_matrix_normalized.png")
        plot_confusion_matrix(cm, class_names, cm_norm_plot_path, normalize=True)
        
        # Plot per-class metrics
        per_class_plot_path = os.path.join(plot_dir, "per_class_metrics.png")
        plot_per_class_metrics(report_dict, per_class_plot_path)
        
        print(f"Visualizations saved to: {plot_dir}")
    except Exception as e:
        print(f"Warning: Could not generate visualizations: {e}")

    return full_report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate AgriSmart AI Disease Detection Model")
    parser.add_argument("--data_dir", type=str, required=True, help="Path to test data directory")
    parser.add_argument("--weights", type=str, required=True, help="Path to model weights")
    parser.add_argument("--report", type=str, default="report/model_report.json", help="Path to save evaluation report")
    parser.add_argument("--plot_dir", type=str, default="report/plots", help="Directory to save visualization plots")
    args = parser.parse_args()
    evaluate(args.data_dir, args.weights, args.report, args.plot_dir)
