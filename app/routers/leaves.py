from fastapi import APIRouter, Depends

from app.dependencies import Role, role_guard
from app.schemas import APIResponse, LeaveRequestIn

router = APIRouter(prefix="/api/v1/leaves", tags=["leaves"])


@router.post("", response_model=APIResponse)
def request_leave(payload: LeaveRequestIn, _role: Role = Depends(role_guard(Role.student))) -> APIResponse:
    return APIResponse(message="Leave request submitted", data={"id": "leave-1", "leave_type": payload.leave_type})


@router.get("", response_model=APIResponse)
def list_leaves(_role: Role = Depends(role_guard(Role.student, Role.warden, Role.guard, Role.staff))) -> APIResponse:
    return APIResponse(message="Leaves fetched", data=[{"id": "leave-1", "status": "pending"}])


@router.get("/active", response_model=APIResponse)
def active_leaves(_role: Role = Depends(role_guard(Role.guard))) -> APIResponse:
    return APIResponse(message="Active leaves fetched", data=[{"id": "leave-1", "status": "approved"}])


@router.get("/{leave_id}", response_model=APIResponse)
def get_leave(leave_id: str, _role: Role = Depends(role_guard(Role.student, Role.warden, Role.guard))) -> APIResponse:
    return APIResponse(message="Leave fetched", data={"id": leave_id})


@router.put("/{leave_id}/approve", response_model=APIResponse)
def approve_leave(leave_id: str, _role: Role = Depends(role_guard(Role.warden))) -> APIResponse:
    return APIResponse(message="Leave approved", data={"leave_id": leave_id, "status": "approved"})


@router.put("/{leave_id}/reject", response_model=APIResponse)
def reject_leave(leave_id: str, _role: Role = Depends(role_guard(Role.warden))) -> APIResponse:
    return APIResponse(message="Leave rejected", data={"leave_id": leave_id, "status": "rejected"})


@router.delete("/{leave_id}", response_model=APIResponse)
def cancel_leave(leave_id: str, _role: Role = Depends(role_guard(Role.student))) -> APIResponse:
    return APIResponse(message="Leave request cancelled", data={"leave_id": leave_id})
