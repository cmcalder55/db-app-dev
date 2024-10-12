
from bs4 import BeautifulSoup
from fastapi import FastAPI
import requests
import uvicorn
from pydantic import BaseModel
from typing import Set, Union
from router import router
from motor.motor_asyncio import AsyncIOMotorClient
from config import settings

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(settings.DB_URL)
    app.mongodb = app.mongodb_client[settings.DB_NAME]


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(router, tags=["items"], prefix="/item")

if __name__ == "__main__":

    # uvicorn.run(
    #     "main:app",
    #     host=settings.HOST,
    #     reload=settings.DEBUG_MODE,
    #     port=settings.PORT,
    # )

    uvicorn.run(
        "main:app", 
        host="127.0.0.1", 
        port=5000, 
        reload=True,
        log_level="info")