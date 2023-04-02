from fastapi import APIRouter
from app.webhooks.routes import router

webhook_router = APIRouter()
webhook_router.include_router(router)
