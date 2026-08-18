from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.middleware.authorization import (
    authorization_middleware
)

from app.routers.orders import router as order_router


app = FastAPI()

allowed_origins = [
    "https://driver.flashmove.io",
    "https://hub.flashmove.io"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=[
        "GET",
        "POST",
        "PATCH"
    ],
    allow_headers=[
        "Content-Type",
        "X-Role-Identity"
    ]
)


app.middleware("http")(
    authorization_middleware
)


app.include_router(order_router)