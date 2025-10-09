from fastapi import APIRouter, Depends, HTTPException
from app.schemas import UserCreate, UserLogin
from app import crud

router = APIRouter()

@router.post('/register')
async def register(user: UserCreate):
    pass

@router.post('/login')
async def login(user: UserLogin):
    pass