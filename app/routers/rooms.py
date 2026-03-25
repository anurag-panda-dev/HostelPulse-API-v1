from fastapi import APIRouter, Depends

from app.dependencies import Role, role_guard
from app.schemas import APIResponse, RoomIn

router = APIRouter(prefix="/api/v1/rooms", tags=["rooms"])


@router.get("", response_model=APIResponse)
def list_rooms(_role: Role = Depends(role_guard(Role.warden))) -> APIResponse:
    return APIResponse(message="Rooms fetched", data=[{"id": "room-101", "block": "A"}])


@router.post("", response_model=APIResponse)
def create_room(payload: RoomIn, _role: Role = Depends(role_guard(Role.warden))) -> APIResponse:
    return APIResponse(message="Room created", data={"id": "room-102", "room_no": payload.room_no})


@router.get("/{room_id}", response_model=APIResponse)
def get_room(room_id: str, _role: Role = Depends(role_guard(Role.warden))) -> APIResponse:
    return APIResponse(message="Room fetched", data={"id": room_id})


@router.put("/{room_id}", response_model=APIResponse)
def update_room(room_id: str, payload: RoomIn, _role: Role = Depends(role_guard(Role.warden))) -> APIResponse:
    return APIResponse(message="Room updated", data={"id": room_id, "room_no": payload.room_no})
