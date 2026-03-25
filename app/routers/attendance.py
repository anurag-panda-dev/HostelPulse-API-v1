from fastapi import APIRouter, Depends, WebSocket

from app.dependencies import Role, role_guard
from app.schemas import APIResponse, AttendanceGenerateQRIn, AttendanceScanIn

router = APIRouter(prefix="/api/v1/attendance", tags=["attendance"])


@router.post("/generate-qr", response_model=APIResponse)
def generate_qr(payload: AttendanceGenerateQRIn, _role: Role = Depends(role_guard(Role.guard))) -> APIResponse:
    return APIResponse(
        message="QR generated",
        data={"session_id": "sess-1", "qr_token": "signed-token", "block": payload.block, "year": payload.year},
    )


@router.post("/scan", response_model=APIResponse)
def scan_qr(payload: AttendanceScanIn, _role: Role = Depends(role_guard(Role.student))) -> APIResponse:
    return APIResponse(message="Attendance marked", data={"qr_token": payload.qr_token, "distance_meters": 1.4})


@router.get("/sessions", response_model=APIResponse)
def list_sessions(_role: Role = Depends(role_guard(Role.guard, Role.warden))) -> APIResponse:
    return APIResponse(message="Attendance sessions fetched", data=[{"id": "sess-1", "status": "active"}])


@router.get("/sessions/{session_id}", response_model=APIResponse)
def get_session(session_id: str, _role: Role = Depends(role_guard(Role.guard, Role.warden))) -> APIResponse:
    return APIResponse(message="Attendance session fetched", data={"id": session_id})


@router.put("/sessions/{session_id}/close", response_model=APIResponse)
def close_session(session_id: str, _role: Role = Depends(role_guard(Role.guard))) -> APIResponse:
    return APIResponse(message="Attendance session closed", data={"id": session_id, "status": "closed"})


@router.get("/reports", response_model=APIResponse)
def attendance_report(_role: Role = Depends(role_guard(Role.warden))) -> APIResponse:
    return APIResponse(message="Attendance report fetched", data={"present": 120, "absent": 8})


@router.post("/manual-mark", response_model=APIResponse)
def manual_mark(_role: Role = Depends(role_guard(Role.warden))) -> APIResponse:
    return APIResponse(message="Attendance manually marked", data={"is_manual": True})


@router.websocket("/ws/attendance/{session_id}")
async def attendance_live(websocket: WebSocket, session_id: str):
    await websocket.accept()
    await websocket.send_json({"session_id": session_id, "event": "connected"})
    await websocket.close()
