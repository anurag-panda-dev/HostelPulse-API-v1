from fastapi import APIRouter, Depends

from app.dependencies import Role, role_guard
from app.schemas import APIResponse

router = APIRouter(prefix="/api/v1/notifications", tags=["notifications"])


@router.get("", response_model=APIResponse)
def list_notifications(_role: Role = Depends(role_guard(Role.student, Role.warden, Role.guard, Role.staff))) -> APIResponse:
    return APIResponse(message="Notifications fetched", data=[{"id": "n-1", "is_read": False}])


@router.put("/{notification_id}/read", response_model=APIResponse)
def mark_read(notification_id: str, _role: Role = Depends(role_guard(Role.student, Role.warden, Role.guard, Role.staff))) -> APIResponse:
    return APIResponse(message="Notification marked as read", data={"notification_id": notification_id})


@router.post("/read-all", response_model=APIResponse)
def mark_all_read(_role: Role = Depends(role_guard(Role.student, Role.warden, Role.guard, Role.staff))) -> APIResponse:
    return APIResponse(message="All notifications marked as read")
