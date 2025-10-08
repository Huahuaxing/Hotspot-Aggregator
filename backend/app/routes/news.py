from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app import crud, schemas

router = APIRouter(prefix="/news", tags=["News"])

@router.get("/", response_model=list[schemas.NewsOut])
async def list_news(db: AsyncSession = Depends(get_db)):
    return await crud.get_news_list(db)

@router.post("/", response_model=schemas.NewsOut)
async def add_news(news: schemas.NewsCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_news(db, news)
