from fastapi import APIRouter

from backend.app.api.disease import router as disease_router
from backend.app.api.crop import router as crop_router
from backend.app.api.irrigation import router as irrigation_router
from backend.app.api.sustainability import router as sustainability_router
from backend.app.api.innovation import router as innovation_router
from backend.app.api.assistant import router as assistant_router
from backend.app.api.advisor import router as advisor_router

api_router = APIRouter(prefix="/api")
api_router.include_router(disease_router, prefix="/disease", tags=["disease"])
api_router.include_router(crop_router, prefix="/crop", tags=["crop"])
api_router.include_router(irrigation_router, prefix="/irrigation", tags=["irrigation"])
api_router.include_router(sustainability_router, prefix="/sustainability", tags=["sustainability"])
api_router.include_router(innovation_router, prefix="/innovation", tags=["innovation"])
api_router.include_router(assistant_router, prefix="/assistant", tags=["assistant"])
api_router.include_router(advisor_router, prefix="/advisor", tags=["advisor"])
