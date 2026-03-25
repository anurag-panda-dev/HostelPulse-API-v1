from fastapi import APIRouter, Depends, WebSocket

from app.dependencies import Role, role_guard
from app.schemas import APIResponse, MessageIn

router = APIRouter(prefix="/api/v1/messages", tags=["messages"])


@router.post("", response_model=APIResponse)
def send_message(payload: MessageIn, _role: Role = Depends(role_guard(Role.student, Role.warden))) -> APIResponse:
    return APIResponse(message="Message sent", data={"thread_id": payload.thread_id})


@router.get("/threads", response_model=APIResponse)
def list_threads(_role: Role = Depends(role_guard(Role.student, Role.warden))) -> APIResponse:
    return APIResponse(message="Threads fetched", data=[{"thread_id": "thread-1"}])


@router.get("/threads/{thread_id}", response_model=APIResponse)
def get_thread(thread_id: str, _role: Role = Depends(role_guard(Role.student, Role.warden))) -> APIResponse:
    return APIResponse(message="Thread fetched", data={"thread_id": thread_id})


@router.put("/{message_id}/read", response_model=APIResponse)
def mark_message_read(message_id: str, _role: Role = Depends(role_guard(Role.student, Role.warden))) -> APIResponse:
    return APIResponse(message="Message marked read", data={"message_id": message_id})


@router.websocket("/ws/messages")
async def messages_ws(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"event": "connected", "channel": "messages"})
    await websocket.close()
