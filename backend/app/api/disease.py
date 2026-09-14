import shutil
import tempfile
from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from backend.app.schemas.common import APIResponse
from backend.app.schemas.disease import DiseasePrediction
from backend.app.services.disease_service import predict_disease

router = APIRouter()

ALLOWED_TYPES = ("image/jpeg", "image/png", "image/jpg")


@router.post("/predict", response_model=APIResponse[DiseasePrediction])
async def disease_predict(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Upload a JPEG or PNG image.")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name

    try:
        result = predict_disease(tmp_path)
    except FileNotFoundError as exc:
        raise HTTPException(
            status_code=503,
            detail=str(exc),
        ) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Inference failed: {exc}") from exc
    finally:
        Path(tmp_path).unlink(missing_ok=True)

    return APIResponse(
        data=DiseasePrediction(**result),
        message="Disease prediction completed.",
    )
