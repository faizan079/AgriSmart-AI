"""
AgriSmart AI - Data Directory Setup Utility
Creates the required directory structure for training the disease detection model.

Expected structure:
    data/
        train/
            <class_name>/
                *.jpg
                *.png
        val/
            <class_name>/
                *.jpg
                *.png
        test/
            <class_name>/
                *.jpg
                *.png
"""
import os
import shutil
from pathlib import Path


def create_data_structure(base_dir: str = "data", classes: list = None):
    """
    Create the required directory structure for training.
    
    Args:
        base_dir: Base directory for data (default: "data")
        classes: List of class names (default: common crop disease classes)
    """
    if classes is None:
        classes = [
            "Apple___Apple_scab",
            "Apple___Black_rot",
            "Apple___healthy",
            "Blueberry___healthy",
            "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
            "Corn_(maize)___Common_rust_",
            "Corn_(maize)___Northern_Leaf_Blight",
            "Corn_(maize)___healthy",
            "Grape___Black_rot",
            "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
            "Grape___healthy",
            "Orange___Haunglongbing_(Citrus_greening)",
            "Peach___Bacterial_spot",
            "Peach___healthy",
            "Pepper,_bell___Bacterial_spot",
            "Pepper,_bell___healthy",
            "Raspberry___healthy",
            "Soybean___healthy",
            "Squash___Powdery_mildew",
            "Strawberry___Leaf_scorch",
            "Strawberry___healthy",
            "Tomato___Bacterial_spot",
            "Tomato___Early_blight",
            "Tomato___Late_blight",
            "Tomato___Leaf_Mold",
            "Tomato___healthy"
        ]
    
    splits = ["train", "val", "test"]
    
    for split in splits:
        for class_name in classes:
            class_dir = os.path.join(base_dir, split, class_name)
            os.makedirs(class_dir, exist_ok=True)
    
    print(f"Created data directory structure at: {base_dir}")
    print(f"Splits: {splits}")
    print(f"Classes ({len(classes)}): {classes}")
    print("\nDirectory structure:")
    for split in splits:
        print(f"  {split}/")
        for class_name in classes:
            print(f"    {class_name}/")


def validate_data_structure(data_dir: str) -> bool:
    """
    Validate that the data directory structure is correct.
    
    Args:
        data_dir: Path to data directory
        
    Returns:
        True if structure is valid, False otherwise
    """
    required_splits = ["train", "val"]
    
    for split in required_splits:
        split_path = os.path.join(data_dir, split)
        if not os.path.exists(split_path):
            print(f"Error: Missing required split directory: {split_path}")
            return False
        
        class_dirs = [d for d in os.listdir(split_path) 
                     if os.path.isdir(os.path.join(split_path, d))]
        
        if not class_dirs:
            print(f"Error: No class directories found in {split_path}")
            return False
        
        for class_dir in class_dirs:
            class_path = os.path.join(split_path, class_dir)
            images = [f for f in os.listdir(class_path) 
                     if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
            
            if not images:
                print(f"Warning: No images found in {class_path}")
    
    print("Data directory structure is valid!")
    return True


def print_data_summary(data_dir: str):
    """
    Print a summary of the dataset.
    
    Args:
        data_dir: Path to data directory
    """
    splits = ["train", "val", "test"]
    
    print(f"\n{'='*60}")
    print(f"DATASET SUMMARY: {data_dir}")
    print(f"{'='*60}")
    
    total_images = 0
    class_counts = {}
    
    for split in splits:
        split_path = os.path.join(data_dir, split)
        if not os.path.exists(split_path):
            continue
        
        print(f"\n{split.upper()}:")
        split_total = 0
        
        class_dirs = sorted([d for d in os.listdir(split_path) 
                            if os.path.isdir(os.path.join(split_path, d))])
        
        for class_dir in class_dirs:
            class_path = os.path.join(split_path, class_dir)
            images = [f for f in os.listdir(class_path) 
                     if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
            count = len(images)
            split_total += count
            total_images += count
            
            if class_dir not in class_counts:
                class_counts[class_dir] = 0
            class_counts[class_dir] += count
            
            print(f"  {class_dir}: {count} images")
        
        print(f"  Total: {split_total} images")
    
    print(f"\n{'='*60}")
    print(f"TOTAL IMAGES: {total_images}")
    print(f"{'='*60}")
    print(f"\nClasses ({len(class_counts)}):")
    for class_name, count in sorted(class_counts.items()):
        print(f"  {class_name}: {count} images")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Setup and validate data directory structure")
    parser.add_argument("--action", type=str, choices=["create", "validate", "summary"], 
                       default="create", help="Action to perform")
    parser.add_argument("--data_dir", type=str, default="data", help="Data directory path")
    parser.add_argument("--classes", type=str, nargs="+", 
                       help="List of class names (for create action)")
    
    args = parser.parse_args()
    
    if args.action == "create":
        create_data_structure(args.data_dir, args.classes)
    elif args.action == "validate":
        validate_data_structure(args.data_dir)
    elif args.action == "summary":
        print_data_summary(args.data_dir)
