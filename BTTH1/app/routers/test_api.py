from fastapi import APIRouter

router = APIRouter(prefix="/api/v1",tags=["Test API"])

@router.get("/salary/modify")
def modify_salary():
    return {
        "message": "Salary modified successfully"
    }

@router.get("/system/settings")
def system_settings():
    return {
        "message": "System settings"
    }

@router.get("/profile")
def get_profile():
    return {
        "message": "User profile"
    }