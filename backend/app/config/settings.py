from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
MODEL_WEIGHTS = PROJECT_ROOT / "model" / "weights" / "model.pt"
INFERENCE_DIR = PROJECT_ROOT / "model" / "inference"

# CORS - frontend dev server
CORS_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000",
]

# Gemini (Phase 9)
GEMINI_API_KEY = ""
