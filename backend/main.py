"""
Entry point for running FastAPI backend server directly from the backend directory.

Run from repository root:
    uvicorn backend.app.main:app --reload

Run from backend directory:
    uvicorn backend.main:app --reload
"""
from backend.app.main import app

__all__ = ["app"]
