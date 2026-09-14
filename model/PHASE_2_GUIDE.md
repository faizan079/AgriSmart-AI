# AgriSmart AI - Phase 2: Core Disease ML Model

## Overview

Phase 2 implements the mandatory core feature: **AI Crop Disease Detection** using a transfer learning approach with ResNet18 on PlantVillage-style crop disease images.

## Key Improvements in Phase 2

### 1. Enhanced Training Script (`model/training/train.py`)

**New Features:**
- **Advanced Data Augmentation**: RandomResizedCrop, ColorJitter, RandomAffine for better generalization
- **Learning Rate Scheduling**: ReduceLROnPlateau for adaptive learning rate adjustment
- **Early Stopping**: Prevents overfitting by stopping when validation accuracy doesn't improve
- **Progressive Unfreezing**: Backbone unfreezing at specified epoch for fine-tuning
- **Comprehensive Logging**: Training history saved with loss, accuracy, and learning rate tracking
- **Best Model Saving**: Only saves the best performing model based on validation accuracy

**Parameters:**
- `--data_dir`: Path to data directory with train/val folders (required)
- `--epochs`: Maximum training epochs (default: 20)
- `--batch_size`: Batch size (default: 32)
- `--lr`: Initial learning rate (default: 1e-3)
- `--out`: Model weights output path (default: ./model/weights/model.pt)
- `--patience`: Early stopping patience (default: 5)
- `--unfreeze_epoch`: Epoch to unfreeze backbone (default: 5)

### 2. Enhanced Evaluation Script (`model/evaluation/evaluate.py`)

**New Features:**
- **Detailed Metrics**: Accuracy, Macro-F1, Weighted-F1, per-class precision/recall/F1
- **Confusion Matrix**: Both raw and normalized versions
- **Visualization**: Automatic generation of confusion matrix plots and per-class metrics
- **Comprehensive Reports**: JSON reports with all metrics for reproducibility

**Parameters:**
- `--data_dir`: Path to test data directory (required)
- `--weights`: Path to model weights (required)
- `--report`: Evaluation report output path (default: report/model_report.json)
- `--plot_dir`: Visualization plots directory (default: report/plots)

### 3. Visualization Utilities (`model/utils/visualization.py`)

**Functions:**
- `plot_training_history()`: Plots training curves (loss, accuracy, learning rate)
- `plot_confusion_matrix()`: Creates confusion matrix visualizations
- `plot_per_class_metrics()`: Bar charts for per-class precision, recall, F1

### 4. Data Setup Utility (`model/utils/setup_data.py`)

**Functions:**
- `create_data_structure()`: Creates required directory structure
- `validate_data_structure()`: Validates data directory format
- `print_data_summary()`: Prints dataset statistics

## Data Directory Structure

**Current Dataset:** PlantVillage-style dataset with 26 classes covering various crop diseases across Apple, Blueberry, Corn, Grape, Orange, Peach, Pepper, Raspberry, Soybean, Squash, Strawberry, and Tomato.

**Dataset Statistics:**
- Total Classes: 26
- Total Images: 38,008
- Train: 30,404 images
- Val: 7,604 images
- Test: 0 images (empty - will need to create from train/val if needed)

**Classes (26):**
1. Apple___Apple_scab
2. Apple___Black_rot
3. Apple___healthy
4. Blueberry___healthy
5. Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot
6. Corn_(maize)___Common_rust_
7. Corn_(maize)___Northern_Leaf_Blight
8. Corn_(maize)___healthy
9. Grape___Black_rot
10. Grape___Leaf_blight_(Isariopsis_Leaf_Spot)
11. Grape___healthy
12. Orange___Haunglongbing_(Citrus_greening)
13. Peach___Bacterial_spot
14. Peach___healthy
15. Pepper,_bell___Bacterial_spot
16. Pepper,_bell___healthy
17. Raspberry___healthy
18. Soybean___healthy
19. Squash___Powdery_mildew
20. Strawberry___Leaf_scorch
21. Strawberry___healthy
22. Tomato___Bacterial_spot
23. Tomato___Early_blight
24. Tomato___Late_blight
25. Tomato___Leaf_Mold
26. Tomato___healthy

```
data/
├── train/
│   ├── Apple___Apple_scab/
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── ...
│   ├── Apple___Black_rot/
│   ├── Apple___healthy/
│   ├── Blueberry___healthy/
│   ├── Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot/
│   ├── Corn_(maize)___Common_rust_/
│   ├── Corn_(maize)___Northern_Leaf_Blight/
│   ├── Corn_(maize)___healthy/
│   ├── Grape___Black_rot/
│   ├── Grape___Leaf_blight_(Isariopsis_Leaf_Spot)/
│   ├── Grape___healthy/
│   ├── Orange___Haunglongbing_(Citrus_greening)/
│   ├── Peach___Bacterial_spot/
│   ├── Peach___healthy/
│   ├── Pepper,_bell___Bacterial_spot/
│   ├── Pepper,_bell___healthy/
│   ├── Raspberry___healthy/
│   ├── Soybean___healthy/
│   ├── Squash___Powdery_mildew/
│   ├── Strawberry___Leaf_scorch/
│   ├── Strawberry___healthy/
│   ├── Tomato___Bacterial_spot/
│   ├── Tomato___Early_blight/
│   ├── Tomato___Late_blight/
│   ├── Tomato___Leaf_Mold/
│   └── Tomato___healthy/
├── val/
│   └── ... (same 26 classes as train)
└── test/
    └── ... (same 26 classes as train, if available)
```

## Step-by-Step Usage Guide

### Step 1: Setup Data Directory

```bash
# Create directory structure
python model/utils/setup_data.py --action create --data_dir ./data

# Validate structure
python model/utils/setup_data.py --action validate --data_dir ./data

# View dataset summary
python model/utils/setup_data.py --action summary --data_dir ./data
```

### Step 2: Train the Model

```bash
# Basic training with default parameters
python model/training/train.py --data_dir ./data

# Training with custom parameters
python model/training/train.py \
    --data_dir ./data \
    --epochs 30 \
    --batch_size 64 \
    --lr 0.001 \
    --patience 7 \
    --unfreeze_epoch 8 \
    --out ./model/weights/model.pt
```

**Training Output:**
- Model weights: `./model/weights/model.pt`
- Class names: `./model/weights/classes.json`
- Training history: `./model/weights/training_history.json`

### Step 3: Visualize Training Progress

```bash
# Plot training curves (after training)
python -c "
from model.utils.visualization import plot_training_history
plot_training_history('./model/weights/training_history.json')
"
```

### Step 4: Evaluate the Model

```bash
# Basic evaluation
python model/evaluation/evaluate.py \
    --data_dir ./data/test \
    --weights ./model/weights/model.pt

# Evaluation with custom output paths
python model/evaluation/evaluate.py \
    --data_dir ./data/test \
    --weights ./model/weights/model.pt \
    --report ./report/final_report.json \
    --plot_dir ./report/final_plots
```

**Evaluation Output:**
- Detailed report: `report/model_report.json`
- Confusion matrix plot: `report/plots/confusion_matrix.png`
- Normalized confusion matrix: `report/plots/confusion_matrix_normalized.png`
- Per-class metrics: `report/plots/per_class_metrics.png`

### Step 5: Test Inference

```bash
# Test single image prediction
python model/inference/predict.py --image path/to/leaf.jpg

# Or use as a function
python -c "
from model.inference.predict import predict
result = predict('path/to/leaf.jpg')
print(result)
"
```

## Model Architecture

**Base Model:** ResNet18 (pretrained on ImageNet)

**Modifications:**
- Freeze all backbone layers initially
- Replace final fully connected layer for custom number of classes
- Progressive unfreezing for fine-tuning

**Input:** 224x224 RGB images

**Output:** Class probabilities for each disease class

## Training Strategy

### Phase 1: Feature Extraction (Epochs 1-4)
- Backbone frozen
- Only train the final classification layer
- High learning rate (1e-3)

### Phase 2: Fine-Tuning (Epochs 5+)
- Unfreeze entire backbone
- Lower learning rate (1e-4)
- Fine-tune all layers

### Regularization
- Data augmentation for robustness
- Early stopping to prevent overfitting
- Learning rate scheduling for convergence

## Evaluation Metrics

**Primary Metric:** Macro-F1 Score (as per SIH requirements)

**Additional Metrics:**
- Accuracy
- Weighted F1-Score
- Per-class Precision, Recall, F1
- Confusion Matrix

## Best Practices

### Data Preparation
1. **Dataset Split**: Use 70-15-15 split for train-val-test
2. **Class Balance**: Ensure balanced classes or use weighted loss
3. **Image Quality**: Use high-quality, diverse images
4. **Field Images**: Include field conditions for better generalization

### Training
1. **Start Small**: Test with small dataset first
2. **Monitor Metrics**: Watch for overfitting (train loss << val loss)
3. **GPU Usage**: Use GPU for faster training if available
4. **Save Checkpoints**: Always save best model

### Evaluation
1. **Never Use Test Set for Training**: Keep test set completely separate
2. **Held-Out Set**: Never use organizer's held-out set for tuning
3. **Reproducibility**: Document all hyperparameters and random seeds
4. **Baseline Comparison**: Compare with simple baseline

## Troubleshooting

### Common Issues

**Issue: CUDA out of memory**
- Solution: Reduce batch_size or use CPU

**Issue: Poor validation accuracy**
- Solution: 
  - Check data quality and class balance
  - Increase training epochs
  - Try different learning rates
  - Add more data augmentation

**Issue: Overfitting**
- Solution:
  - Add more data augmentation
  - Reduce model complexity
  - Increase early stopping patience
  - Use dropout or weight decay

**Issue: Slow training**
- Solution:
  - Use GPU if available
  - Increase batch_size
  - Reduce num_workers in DataLoader
  - Use mixed precision training

## File Dependencies

**Required Python Packages:**
- torch>=2.2.0
- torchvision>=0.17.0
- scikit-learn>=1.5.0
- Pillow>=10.4.0
- matplotlib (for visualization)

**Install:**
```bash
pip install -r requirements.txt
pip install matplotlib
```

## Next Steps (Phase 3)

After completing Phase 2:
1. Integrate the trained model into the FastAPI backend
2. Create `/api/disease/predict` endpoint
3. Test the API with sample images
4. Move to Phase 4: Frontend integration

## Important Notes

⚠️ **CRITICAL**: Never train on the organizer's held-out test set. This is grounds for disqualification.

⚠️ **REPRODUCIBILITY**: The final submission must be reproducible. Document all steps, hyperparameters, and data sources.

⚠️ **MACRO-F1**: This is the primary evaluation metric. Optimize for macro-F1 rather than simple accuracy.

⚠️ **GENERALIZATION**: The real challenge is generalizing from lab images to field images. Focus on robust training strategies.

## Contact & Support

For issues or questions about Phase 2 implementation, refer to:
- Project Overview document
- SIH 2026 problem statement
- Team documentation
