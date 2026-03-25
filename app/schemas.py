from typing import Any

from pydantic import BaseModel, Field


class APIResponse(BaseModel):
    success: bool = True
    message: str
    data: Any | None = None


class LoginRequest(BaseModel):
    username: str = Field(min_length=3)
    password: str = Field(min_length=8)


class RefreshTokenRequest(BaseModel):
    refresh_token: str = Field(min_length=10)


class ForgotPasswordRequest(BaseModel):
    email_or_registration_no: str = Field(min_length=3)


class ResetPasswordRequest(BaseModel):
    otp: str = Field(min_length=4, max_length=6)
    new_password: str = Field(min_length=8)


class AttendanceGenerateQRIn(BaseModel):
    block: str
    year: int = Field(ge=1, le=4)
    duration_minutes: int = Field(ge=1, le=180)


class AttendanceScanIn(BaseModel):
    qr_token: str
    latitude: float
    longitude: float


class LeaveRequestIn(BaseModel):
    leave_type: str
    from_date: str
    to_date: str
    place_of_visit: str | None = None
    extra_details: str | None = None


class GrievanceIn(BaseModel):
    category: str
    sub_category: str | None = None
    priority: str
    description: str


class StudentIn(BaseModel):
    registration_no: str
    name: str
    phone: str
    parent_phone: str
    year: int = Field(ge=1, le=4)
    semester: int = Field(ge=1, le=8)


class StudentDocumentIn(BaseModel):
    doc_type: str
    file_url: str


class RoomIn(BaseModel):
    room_no: str
    block: str
    floor: int
    capacity: int = Field(ge=1, le=10)


class MessageIn(BaseModel):
    thread_id: str
    content: str = Field(min_length=1, max_length=2000)


class PaymentIn(BaseModel):
    student_id: str
    amount: float
    payment_for: str
