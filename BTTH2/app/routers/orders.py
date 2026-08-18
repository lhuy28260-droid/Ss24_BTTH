from fastapi import APIRouter


router = APIRouter(
    prefix="/api/v1/orders",
    tags=["Orders"]
)


@router.post("/assign")
async def assign_order():

    return {
        "status": "Success",
        "message": "Order assigned successfully"
    }


@router.patch("/status")
async def update_order_status():

    return {
        "status": "Success",
        "message": "Order status updated successfully"
    }


@router.get("/track")
async def track_order():

    return {
        "status": "Success",
        "message": "Order tracking information"
    }