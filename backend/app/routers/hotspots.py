from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app import crud, schemas

router = APIRouter(prefix="/hotspots", tags=["Hotspots"])

@router.get("/", response_model=list[schemas.HotspotRead])
async def list_hotspots(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await crud.get_hotspots(db, skip, limit)
