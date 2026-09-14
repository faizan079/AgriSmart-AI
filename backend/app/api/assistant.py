"""
Farmer Assistant API
"""
from fastapi import APIRouter

from backend.app.schemas.common import APIResponse
from backend.app.schemas.assistant import AssistantRequest, AssistantResponse
from backend.app.services.assistant_service import get_assistant_response

router = APIRouter()


@router.post("/chat", response_model=APIResponse[AssistantResponse])
async def assistant_chat(request: AssistantRequest):
    """Get farming assistance and recommendations"""
    try:
        request_data = {
            "question": request.question,
            "context": request.context
        }

        result = get_assistant_response(request_data)

        return APIResponse(
            data=AssistantResponse(**result),
            message="Assistant response generated successfully."
        )
    except Exception as exc:
        raise Exception(f"Assistant response failed: {exc}") from exc