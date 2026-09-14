# AgriSmart AI

**Intelligent Agriculture for a Sustainable Future** — SIH 2026 Internal Hackathon

AI-powered smart agriculture platform: crop disease detection, crop recommendation, irrigation, weather intelligence, sustainability scoring, Gemini farmer assistant, and agentic advisor.

## Project Structure

```
AgriSmart-AI/
├── backend/app/          # FastAPI backend (modular APIs + services)
├── frontend/             # React responsive UI
├── model/
│   ├── training/         # train.py
│   ├── inference/        # predict.py (required interface)
│   ├── evaluation/       # evaluate.py
│   └── weights/          # model.pt (after training)
├── report/               # model report generator + metrics
├── requirements.txt
└── README.md
```

## Quick Start (Part 1 — Foundation)

### 1. Backend

```bash
cd "D:\Hackathon's\AgriSmart-AI"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn backend.app.main:app --reload
```

Open: http://127.0.0.1:8000 → `{"status": "ok", ...}`

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

Open: http://127.0.0.1:5173

## Development Phases

| Part | Focus | Status |
|------|-------|--------|
| 1 | Foundation & architecture | ✅ Current |
| 2 | Core disease ML model | Pending |
| 3 | Disease API (complete) | Pending |
| 4 | Disease frontend polish | Pending |
| 5–10 | Bonus modules + Gemini + Agent | Pending |

## Core ML (Part 2)

```bash
# Train (requires dataset in ./data/train and ./data/val)
python model/training/train.py --data_dir ./data --epochs 10

# Evaluate
python model/evaluation/evaluate.py --data_dir ./data/test --weights ./model/weights/model.pt

# Predict (required interface)
python model/inference/predict.py --image path/to/leaf.jpg
```

**Important:** Never train on the organizer's held-out field test set.

## API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/api/disease/predict` | POST | Upload image → disease prediction |

## Environment

Copy `.env.example` to `.env` and add API keys (Gemini in Phase 9).

## License

Academic / Hackathon project — L.J. Institute of Engineering and Technology.
