from fastapi import FastAPI
from app.api.routes import api_router
from app.webhooks import webhook_router
from app.core.config import settings
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router, prefix="/api")
app.include_router(webhook_router, prefix="/webhook")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
