# AgriSmart AI Backend Service

FastAPI-powered Intelligent Agriculture API engine.

## Quick Start

Run the backend server from the repository root:

```bash
uvicorn backend.app.main:app --reload
```

Or from inside the `backend` directory:

```bash
uvicorn backend.main:app --reload
```

## API Modules & Endpoints

- **Disease Detection**: `POST /api/disease/predict`
- **Crop Recommendation**: `POST /api/crop/recommend`
- **Smart Irrigation**: `POST /api/irrigation/analyze`
- **Weather Intelligence**: `POST /api/irrigation/weather`
- **Sustainability Score**: `POST /api/sustainability/score`
- **Crop Stress Warning**: `POST /api/innovation/stress`
- **Crop Rotation**: `POST /api/innovation/rotation`
- **Water & Yield Prediction**: `POST /api/innovation/prediction`
- **Farmer Assistant**: `POST /api/assistant/chat`
- **AI Advisor**: `POST /api/advisor/analyze`
