from fastapi import APIRouter, Request
from .handlers import handle_webhook

router = APIRouter()

@router.post("/webhooks")
async def webhook(request: Request):
    return await handle_webhook(request)
