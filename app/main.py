from fastapi import FastAPI

from app.routers import (
    attendance,
    auth,
    grievances,
    leaves,
    messages,
    notifications,
    payments,
    rooms,
    students,
)

app = FastAPI(
    title="HostelPulse API",
    version="1.0.0",
    description="Basic FastAPI starter aligned to TRD endpoints with role-based access per route.",
)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "HostelPulse API is running"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(auth.router)
app.include_router(students.router)
app.include_router(attendance.router)
app.include_router(leaves.router)
app.include_router(grievances.router)
app.include_router(messages.router)
app.include_router(payments.router)
app.include_router(notifications.router)
app.include_router(rooms.router)
