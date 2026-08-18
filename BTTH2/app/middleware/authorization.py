from fastapi import Request
from fastapi.responses import JSONResponse


ROLE_PERMISSIONS = {
    ("POST", "/api/v1/orders/assign"): [
        "DISPATCHER"
    ],

    ("PATCH", "/api/v1/orders/status"): [
        "DISPATCHER",
        "DRIVER"
    ],

    ("GET", "/api/v1/orders/track"): [
        "DISPATCHER",
        "DRIVER",
        "CUSTOMER_SUPPORT"
    ]
}


async def authorization_middleware(
    request: Request,
    call_next
):

    method = request.method
    path = request.url.path

    permission_key = (method, path)

    if permission_key not in ROLE_PERMISSIONS:
        return await call_next(request)

    user_role = request.headers.get(
        "X-Role-Identity"
    )

    if user_role is None:
        return JSONResponse(
            status_code=403,
            content={
                "status": "Rejected",
                "reason": "Unauthorized action for this role"
            }
        )

    allowed_roles = ROLE_PERMISSIONS[
        permission_key
    ]

    
    if user_role not in allowed_roles:
        return JSONResponse(
            status_code=403,
            content={
                "status": "Rejected",
                "reason": "Unauthorized action for this role"
            }
        )

    # Được phép
    return await call_next(request)