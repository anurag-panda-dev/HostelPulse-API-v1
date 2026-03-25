from enum import Enum

from fastapi import Depends, Header, HTTPException, status


class Role(str, Enum):
    student = "student"
    warden = "warden"
    guard = "guard"
    staff = "staff"


def get_current_role(x_role: Role | None = Header(default=None, alias="X-Role")) -> Role:
    if x_role is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing X-Role header",
        )
    return x_role


def role_guard(*allowed_roles: Role):
    def dependency(current_role: Role = Depends(get_current_role)) -> Role:
        if current_role not in allowed_roles:
            allowed = ", ".join(role.value for role in allowed_roles)
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access denied for role '{current_role.value}'. Allowed roles: {allowed}",
            )
        return current_role

    return dependency
