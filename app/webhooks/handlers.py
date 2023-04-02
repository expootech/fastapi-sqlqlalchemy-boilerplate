from fastapi import Request

async def handle_webhook(request: Request):
    # Handle the webhook request here
    return {"message": "Webhook received successfully"}
