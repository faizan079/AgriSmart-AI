import sys
from pathlib import Path

from backend.app.config.settings import INFERENCE_DIR


def _ensure_inference_path():
    path = str(INFERENCE_DIR)
    if path not in sys.path:
        sys.path.insert(0, path)


def predict_disease(image_path: str) -> dict:
    """Run ML inference on a saved image file."""
    _ensure_inference_path()
    from predict import predict  # noqa: WPS433

    return predict(image_path)
