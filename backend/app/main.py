"""
AgriSmart AI - FastAPI Backend

Run from project root:
    uvicorn backend.app.main:app --reload
"""
import sys
from pathlib import Path

# Ensure project root is on PYTHONPATH
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api import api_router
from backend.app.config.settings import CORS_ORIGINS

app = FastAPI(
    title="AgriSmart AI",
    description="Intelligent Agriculture for a Sustainable Future",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.get("/")
def health():
    return {
        "status": "ok",
        "service": "AgriSmart AI",
        "version": "0.2.0",
        "phase": "4 - Disease Detection Complete",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
