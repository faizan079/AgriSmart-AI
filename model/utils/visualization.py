"""
AgriSmart AI - Visualization Utilities
Provides functions for plotting training curves, confusion matrices, and other metrics.
"""
import json
import os
from typing import Dict, List

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix


def plot_training_history(history_path: str, save_dir: str = None):
    """
    Plot training curves from training history JSON file.
    
    Args:
        history_path: Path to training_history.json
        save_dir: Directory to save plots (default: same directory as history_path)
    """
    if not os.path.exists(history_path):
        raise FileNotFoundError(f"Training history not found at {history_path}")
    
    with open(history_path, 'r') as f:
        history = json.load(f)
    
    if save_dir is None:
        save_dir = os.path.dirname(history_path)
    
    os.makedirs(save_dir, exist_ok=True)
    
    # Plot training loss and validation accuracy
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    epochs = range(1, len(history['train_loss']) + 1)
    
    # Training loss
    ax1.plot(epochs, history['train_loss'], 'b-', label='Training Loss', linewidth=2)
    ax1.set_xlabel('Epoch', fontsize=12)
    ax1.set_ylabel('Loss', fontsize=12)
    ax1.set_title('Training Loss Over Epochs', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # Validation accuracy
    ax2.plot(epochs, history['val_acc'], 'g-', label='Validation Accuracy', linewidth=2)
    ax2.set_xlabel('Epoch', fontsize=12)
    ax2.set_ylabel('Accuracy', fontsize=12)
    ax2.set_title('Validation Accuracy Over Epochs', fontsize=14, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plot_path = os.path.join(save_dir, 'training_curves.png')
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Training curves saved to: {plot_path}")
    
    # Plot learning rate schedule
    if 'learning_rate' in history and history['learning_rate']:
        plt.figure(figsize=(10, 5))
        plt.plot(epochs, history['learning_rate'], 'r-', label='Learning Rate', linewidth=2)
        plt.xlabel('Epoch', fontsize=12)
        plt.ylabel('Learning Rate', fontsize=12)
        plt.title('Learning Rate Schedule', fontsize=14, fontweight='bold')
        plt.legend(fontsize=10)
        plt.yscale('log')
        plt.grid(True, alpha=0.3)
        
        lr_plot_path = os.path.join(save_dir, 'learning_rate_schedule.png')
        plt.savefig(lr_plot_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"Learning rate schedule saved to: {lr_plot_path}")


def plot_confusion_matrix(cm: np.ndarray, class_names: List[str], 
                          save_path: str = None, normalize: bool = False):
    """
    Plot confusion matrix with labels.
    
    Args:
        cm: Confusion matrix array
        class_names: List of class names
        save_path: Path to save the plot
        normalize: Whether to normalize the confusion matrix
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        title = 'Normalized Confusion Matrix'
        fmt = '.2f'
    else:
        title = 'Confusion Matrix'
        fmt = 'd'
    
    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    ax.figure.colorbar(im, ax=ax)
    
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           xticklabels=class_names, yticklabels=class_names,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')
    
    # Rotate the tick labels and set their alignment
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    
    # Add text annotations
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                   ha="center", va="center",
                   color="white" if cm[i, j] > thresh else "black",
                   fontsize=10)
    
    fig.tight_layout()
    
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Confusion matrix saved to: {save_path}")
    else:
        plt.show()


def plot_per_class_metrics(report: Dict, save_path: str = None):
    """
    Plot per-class precision, recall, and F1-score.
    
    Args:
        report: Classification report dictionary
        save_path: Path to save the plot
    """
    class_names = []
    precision = []
    recall = []
    f1_score = []
    
    for class_name in report.keys():
        if class_name not in ['accuracy', 'macro avg', 'weighted avg']:
            class_names.append(class_name)
            precision.append(report[class_name]['precision'])
            recall.append(report[class_name]['recall'])
            f1_score.append(report[class_name]['f1-score'])
    
    x = np.arange(len(class_names))
    width = 0.25
    
    fig, ax = plt.subplots(figsize=(14, 6))
    
    rects1 = ax.bar(x - width, precision, width, label='Precision', alpha=0.8)
    rects2 = ax.bar(x, recall, width, label='Recall', alpha=0.8)
    rects3 = ax.bar(x + width, f1_score, width, label='F1-Score', alpha=0.8)
    
    ax.set_xlabel('Class', fontsize=12)
    ax.set_ylabel('Score', fontsize=12)
    ax.set_title('Per-Class Metrics', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(class_names, rotation=45, ha='right')
    ax.legend(fontsize=10)
    ax.set_ylim([0, 1])
    ax.grid(True, alpha=0.3, axis='y')
    
    fig.tight_layout()
    
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Per-class metrics plot saved to: {save_path}")
    else:
        plt.show()


if __name__ == "__main__":
    # Example usage
    print("Visualization utilities loaded successfully.")
    print("Use plot_training_history(), plot_confusion_matrix(), and plot_per_class_metrics() functions.")
