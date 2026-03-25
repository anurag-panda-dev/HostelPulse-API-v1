from fastapi import APIRouter, Depends

from app.dependencies import Role, get_current_role
from app.schemas import APIResponse, ForgotPasswordRequest, LoginRequest, RefreshTokenRequest, ResetPasswordRequest

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])


@router.post("/login", response_model=APIResponse)
def login(payload: LoginRequest) -> APIResponse:
    return APIResponse(
        message="Login successful",
        data={
            "user": payload.username,
            "access_token": "sample-access-token",
            "refresh_token": "sample-refresh-token",
        },
    )


@router.post("/logout", response_model=APIResponse)
def logout(current_role: Role = Depends(get_current_role)) -> APIResponse:
    return APIResponse(message="Logout successful", data={"role": current_role})


@router.post("/refresh", response_model=APIResponse)
def refresh_token(payload: RefreshTokenRequest) -> APIResponse:
    return APIResponse(
        message="Token refreshed",
        data={"access_token": "sample-new-access-token", "refresh_token": payload.refresh_token},
    )


@router.post("/forgot-password", response_model=APIResponse)
def forgot_password(payload: ForgotPasswordRequest) -> APIResponse:
    return APIResponse(message="OTP sent", data={"identifier": payload.email_or_registration_no})


@router.post("/reset-password", response_model=APIResponse)
def reset_password(payload: ResetPasswordRequest) -> APIResponse:
    return APIResponse(message="Password reset successful", data={"otp_used": payload.otp})


@router.get("/me", response_model=APIResponse)
def me(current_role: Role = Depends(get_current_role)) -> APIResponse:
    return APIResponse(message="Fetched current user", data={"role": current_role})
