from fastapi import APIRouter, Depends

from app.dependencies import Role, role_guard
from app.schemas import APIResponse, StudentDocumentIn, StudentIn

router = APIRouter(prefix="/api/v1/students", tags=["students"])


@router.get("/me", response_model=APIResponse)
def student_profile(current_role: Role = Depends(role_guard(Role.student))) -> APIResponse:
    return APIResponse(message="Student profile fetched", data={"id": "stu-self", "role": current_role})


@router.get("", response_model=APIResponse)
def list_students(_role: Role = Depends(role_guard(Role.warden))) -> APIResponse:
    return APIResponse(message="Students fetched", data=[{"id": "stu-1", "name": "Alice"}])


@router.post("", response_model=APIResponse)
def create_student(payload: StudentIn, _role: Role = Depends(role_guard(Role.warden))) -> APIResponse:
    return APIResponse(message="Student created", data={"id": "stu-2", "name": payload.name})


@router.get("/{student_id}", response_model=APIResponse)
def get_student(student_id: str, _role: Role = Depends(role_guard(Role.warden, Role.student))) -> APIResponse:
    return APIResponse(message="Student fetched", data={"id": student_id})


@router.put("/{student_id}", response_model=APIResponse)
def update_student(student_id: str, payload: StudentIn, _role: Role = Depends(role_guard(Role.warden))) -> APIResponse:
    return APIResponse(message="Student updated", data={"id": student_id, "name": payload.name})


@router.delete("/{student_id}", response_model=APIResponse)
def delete_student(student_id: str, _role: Role = Depends(role_guard(Role.warden))) -> APIResponse:
    return APIResponse(message="Student deleted", data={"id": student_id})


@router.post("/{student_id}/documents", response_model=APIResponse)
def add_student_document(
    student_id: str,
    payload: StudentDocumentIn,
    _role: Role = Depends(role_guard(Role.warden)),
) -> APIResponse:
    return APIResponse(
        message="Student document uploaded",
        data={"student_id": student_id, "doc_type": payload.doc_type, "file_url": payload.file_url},
    )


@router.get("/{student_id}/documents", response_model=APIResponse)
def list_student_documents(student_id: str, _role: Role = Depends(role_guard(Role.warden, Role.student))) -> APIResponse:
    return APIResponse(message="Student documents fetched", data=[{"student_id": student_id, "doc_type": "aadhaar"}])
