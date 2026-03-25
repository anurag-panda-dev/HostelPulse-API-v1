from fastapi import APIRouter, Depends

from app.dependencies import Role, role_guard
from app.schemas import APIResponse, GrievanceIn

router = APIRouter(prefix="/api/v1/grievances", tags=["grievances"])


@router.post("", response_model=APIResponse)
def create_grievance(payload: GrievanceIn, _role: Role = Depends(role_guard(Role.student))) -> APIResponse:
    return APIResponse(message="Grievance created", data={"ticket_id": "GRV-2026-00001", "category": payload.category})


@router.get("", response_model=APIResponse)
def list_grievances(_role: Role = Depends(role_guard(Role.student, Role.warden, Role.staff))) -> APIResponse:
    return APIResponse(message="Grievances fetched", data=[{"id": "grv-1", "status": "open"}])


@router.get("/{grievance_id}", response_model=APIResponse)
def get_grievance(grievance_id: str, _role: Role = Depends(role_guard(Role.student, Role.warden, Role.staff))) -> APIResponse:
    return APIResponse(message="Grievance fetched", data={"id": grievance_id})


@router.put("/{grievance_id}/resolve", response_model=APIResponse)
def resolve_grievance(grievance_id: str, _role: Role = Depends(role_guard(Role.warden))) -> APIResponse:
    return APIResponse(message="Grievance resolved", data={"grievance_id": grievance_id})


@router.post("/{grievance_id}/images", response_model=APIResponse)
def upload_grievance_image(grievance_id: str, _role: Role = Depends(role_guard(Role.student))) -> APIResponse:
    return APIResponse(message="Grievance image uploaded", data={"grievance_id": grievance_id})
