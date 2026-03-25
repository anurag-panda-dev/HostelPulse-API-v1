from fastapi import APIRouter, Depends

from app.dependencies import Role, role_guard
from app.schemas import APIResponse, PaymentIn

router = APIRouter(prefix="/api/v1/payments", tags=["payments"])


@router.post("", response_model=APIResponse)
def create_payment(payload: PaymentIn, _role: Role = Depends(role_guard(Role.warden))) -> APIResponse:
    return APIResponse(message="Payment record created", data={"student_id": payload.student_id, "amount": payload.amount})


@router.put("/{payment_id}/verify", response_model=APIResponse)
def verify_payment(payment_id: str, _role: Role = Depends(role_guard(Role.warden))) -> APIResponse:
    return APIResponse(message="Payment verified", data={"payment_id": payment_id, "status": "paid"})


@router.get("", response_model=APIResponse)
def list_payments(_role: Role = Depends(role_guard(Role.warden))) -> APIResponse:
    return APIResponse(message="Payments fetched", data=[{"id": "pay-1", "status": "pending"}])


@router.get("/student/{student_id}", response_model=APIResponse)
def payment_history(student_id: str, _role: Role = Depends(role_guard(Role.student, Role.warden))) -> APIResponse:
    return APIResponse(message="Payment history fetched", data={"student_id": student_id, "items": []})
