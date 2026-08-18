from fastapi import Request
from fastapi.responses import JSONResponse
from app.security import Role

ROLE_PERMISSIONS = {
    "/api/v1/salary/modify": [Role.ADMIN,Role.HR],
    "/api/v1/system/settings": [Role.ADMIN],
    "/api/v1/profile": [Role.ADMIN,Role.HR,Role.STAFF]
}

async def authorization_middleware(request: Request, call_next):

    path = request.url.path
    # API không nằm trong danh sách bảo vệ
    # thì cho Request đi tiếp
    if path not in ROLE_PERMISSIONS:
        return await call_next(request)
    # Lấy Role từ Header
    user_role = request.headers.get("X-User-Role")

    # Không có Role
    if user_role is None:
        return JSONResponse(
            status_code=403,
            content={
                "error": "Permission Denied"
            }
        )

    
    try:
        user_role = Role(user_role)
    except ValueError:
        return JSONResponse(
            status_code=403,
            content={
                "error": "Permission Denied"
            }
        )

    
    allowed_roles = ROLE_PERMISSIONS[path]

    if user_role not in allowed_roles:
        return JSONResponse(
            status_code=403,
            content={
                "error": "Permission Denied"
            }
        )

    # Có quyền
    return await call_next(request)