"""
AgriSmart AI - Required predict interface (Section 4.1 of problem statement).

Usage as CLI:
    python model/inference/predict.py --image path/to/leaf.jpg

Usage as function:
    from predict import predict
    result = predict("path/to/leaf.jpg")
"""
import argparse
import json
import os

import torch
import torch.nn as nn
from PIL import Image
from torchvision import models, transforms

WEIGHTS_PATH = os.path.join(os.path.dirname(__file__), "..", "weights", "model.pt")

PRECAUTIONS = {
    "Apple___Apple_scab": "Remove affected leaves and fruit, apply fungicide in early spring, improve air circulation.",
    "Apple___Black_rot": "Remove mummified fruit, prune infected canes, apply fungicide during wet periods.",
    "Apple___healthy": "No action needed. Continue regular monitoring and maintain good orchard hygiene.",
    "Blueberry___healthy": "No action needed. Continue regular monitoring and proper irrigation.",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": "Rotate crops, apply fungicide, avoid overhead irrigation, remove crop residue.",
    "Corn_(maize)___Common_rust_": "Apply resistant varieties, rotate crops, apply fungicide early in infection.",
    "Corn_(maize)___Northern_Leaf_Blight": "Use resistant hybrids, rotate crops, apply foliar fungicides, remove infected debris.",
    "Corn_(maize)___healthy": "No action needed. Continue regular monitoring and proper fertilization.",
    "Grape___Black_rot": "Remove infected clusters, improve air circulation, apply fungicide during bloom and fruit set.",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": "Remove infected leaves, improve air circulation, apply fungicide, avoid overhead irrigation.",
    "Grape___healthy": "No action needed. Continue regular monitoring and proper canopy management.",
    "Orange___Haunglongbing_(Citrus_greening)": "Remove infected trees, control Asian citrus psyllid, use certified disease-free nursery stock.",
    "Peach___Bacterial_spot": "Apply copper-based fungicides, avoid overhead irrigation, remove infected plant material.",
    "Peach___healthy": "No action needed. Continue regular monitoring and proper orchard maintenance.",
    "Pepper,_bell___Bacterial_spot": "Use disease-free seeds, crop rotation, copper sprays, avoid working with wet plants.",
    "Pepper,_bell___healthy": "No action needed. Continue regular monitoring and proper watering practices.",
    "Raspberry___healthy": "No action needed. Continue regular monitoring and proper trellising.",
    "Soybean___healthy": "No action needed. Continue regular monitoring and proper crop rotation.",
    "Squash___Powdery_mildew": "Improve air circulation, apply fungicide, remove severely infected leaves, resistant varieties.",
    "Strawberry___Leaf_scorch": "Remove infected leaves, improve air circulation, avoid overhead irrigation, apply fungicide.",
    "Strawberry___healthy": "No action needed. Continue regular monitoring and proper bed management.",
    "Tomato___Bacterial_spot": "Use disease-free seeds, crop rotation, copper sprays, avoid working with wet plants.",
    "Tomato___Early_blight": "Remove affected leaves, avoid overhead watering, apply approved fungicide, crop rotation.",
    "Tomato___Late_blight": "Remove and destroy infected plants, improve air circulation, avoid wet foliage, apply fungicide.",
    "Tomato___Leaf_Mold": "Improve air circulation, reduce humidity, apply fungicide, remove infected leaves.",
    "Tomato___healthy": "No action needed. Continue regular monitoring and proper plant care.",
}

_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

_model = None
_class_names = None


def _load_model():
    global _model, _class_names
    if _model is not None:
        return
    if not os.path.exists(WEIGHTS_PATH):
        raise FileNotFoundError(
            f"Model weights not found at {WEIGHTS_PATH}. "
            "Train the model first: python model/training/train.py --data_dir ./data"
        )
    checkpoint = torch.load(WEIGHTS_PATH, map_location="cpu")
    _class_names = checkpoint["class_names"]
    model = models.resnet18(weights=None)
    model.fc = nn.Linear(model.fc.in_features, len(_class_names))
    model.load_state_dict(checkpoint["model_state_dict"])
    model.eval()
    _model = model


def _format_label(raw_label: str) -> str:
    """Convert class label to a human-readable display name.

    Example: 'Tomato___Early_blight' -> 'Tomato - Early Blight'
    """
    parts = raw_label.split("___")
    crop = parts[0].replace("_", " ").replace(",", ",")
    if len(parts) > 1:
        disease = parts[1].replace("_", " ").strip()
        return f"{crop} - {disease.title()}"
    return crop


def predict(image_path: str) -> dict:
    """Required interface: predict(image_path) -> class_label (+ extra fields)."""
    _load_model()
    image = Image.open(image_path).convert("RGB")
    tensor = _transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = _model(tensor)
        probs = torch.softmax(outputs, dim=1)[0]
        conf, idx = torch.max(probs, dim=0)

    label = _class_names[idx.item()]
    is_healthy = "healthy" in label.lower()

    # Top 3 predictions
    top3_vals, top3_idxs = torch.topk(probs, k=min(3, len(_class_names)))
    top_predictions = []
    for val, i in zip(top3_vals, top3_idxs):
        top_predictions.append({
            "class_label": _format_label(_class_names[i.item()]),
            "confidence": round(val.item(), 4),
        })

    return {
        "class_label": _format_label(label),
        "confidence": round(conf.item(), 4),
        "is_healthy": is_healthy,
        "precaution": PRECAUTIONS.get(label, "Consult a local agricultural expert."),
        "top_predictions": top_predictions,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=str, required=True)
    args = parser.parse_args()
    result = predict(args.image)
    print(json.dumps(result, indent=2))
