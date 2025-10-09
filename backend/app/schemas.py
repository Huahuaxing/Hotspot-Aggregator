from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class UserRead(BaseModel):
    id: int
    username: str
    
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str

class NewsBase(BaseModel):
    title: str
    url: str
    source: str | None = None

class NewsCreate(NewsBase):
    pass

class NewsOut(NewsBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
