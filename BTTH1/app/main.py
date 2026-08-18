from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.middleware import authorization_middleware
from app.routers.test_api import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://internal.megamart.com"],

    allow_methods=["GET","POST"],
    allow_headers=["Content-Type","X-User-Role"]
)


app.middleware("http")(authorization_middleware)
app.include_router(router)