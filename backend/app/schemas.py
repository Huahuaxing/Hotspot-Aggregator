from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

class UserRead(BaseModel):
    id: int
    username: str
    
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# 现有的新闻相关模型...
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
        from_attributes = True