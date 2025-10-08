from fastapi import FastAPI
from app.routes import news
from app.db import engine, Base
import asyncio

app = FastAPI(title="Hotspot Aggregator Backend")

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(news.router)

@app.get("/")
async def root():
    return {"message": "Backend running successfully!"}
