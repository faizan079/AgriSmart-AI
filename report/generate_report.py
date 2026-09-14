"""
AgriSmart AI - Model Report Generator (Section 4 / Section 7.3 requirements)

Run:
    python report/generate_report.py --eval_json report/model_report.json --baseline_f1 0.55
"""
import argparse
import json


def generate_report(eval_json_path: str, baseline_f1: float, out_path: str = "report/model_report.md"):
    with open(eval_json_path) as f:
        data = json.load(f)

    macro_f1 = data["macro_f1"]
    class_names = data["class_names"]
    cm = data["confusion_matrix"]

    diff = macro_f1 - baseline_f1
    if diff < 0:
        comparison = f"Below baseline by {abs(diff):.4f}"
    elif diff < 0.10:
        comparison = f"Mid-range: {diff:.4f} above baseline"
    else:
        comparison = f"Well above baseline: +{diff:.4f}"

    cm_lines = "\n".join(
        f"| {class_names[i]} | " + " | ".join(str(v) for v in row) + " |"
        for i, row in enumerate(cm)
    )
    header_row = "| Actual \\ Predicted | " + " | ".join(class_names) + " |"
    sep_row = "|---" * (len(class_names) + 1) + "|"

    report = f"""# AgriSmart AI - Core Model Report

## Task
Crop-disease image classification across {len(class_names)} classes (including "healthy"),
trained on lab-condition images and evaluated on field-condition images (domain shift).

## Dataset & Split
- Training/validation: PlantVillage-style lab images.
- Held-out test: organizer-provided field-condition set (natural lighting, clutter, occlusion).
- The held-out test set was NEVER used for training or hyperparameter tuning.

## Model / Approach
- Backbone: ResNet18 (ImageNet-pretrained), transfer learning with fine-tuned final layer.
- Input: 224x224 RGB, normalized with ImageNet mean/std.
- Augmentation: horizontal flip + rotation (to improve generalisation to field conditions).

## Metric & Result
- **Macro-F1 (primary metric): {macro_f1:.4f}**
- Baseline Macro-F1: {baseline_f1:.4f}
- Comparison: {comparison}

### Confusion Matrix
{header_row}
{sep_row}
{cm_lines}

## Baseline Comparison
Reported baseline Macro-F1 was {baseline_f1:.4f}. This model scored {macro_f1:.4f} ({comparison}).

## Limitations (honest, required)
- Model is trained on clean lab images; performance on field images with occlusion,
  poor lighting, or multiple leaves in-frame is expected to be lower than validation accuracy.
- Class imbalance in the training set may bias predictions toward majority classes -
  this is why Macro-F1 (not accuracy) is the primary metric.
- Confidence scores are softmax outputs, not calibrated probabilities.
- Only classes present in the shared class list are supported; out-of-distribution
  crops/diseases will be misclassified into the nearest known class.
"""

    import os
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        f.write(report)

    print(f"Report written to {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--eval_json", type=str, default="report/model_report.json")
    parser.add_argument("--baseline_f1", type=float, required=True,
                        help="Baseline macro-F1 provided by organizers")
    parser.add_argument("--out", type=str, default="report/model_report.md")
    args = parser.parse_args()
    generate_report(args.eval_json, args.baseline_f1, args.out)
