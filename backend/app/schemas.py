from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any

class HotspotBase(BaseModel):
    title: str
    url: str
    source: Optional[str] = "zhihu"
    summary: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[Dict[str, Any]] = None
    published_at: Optional[datetime] = None

class HotspotCreate(HotspotBase):
    pass

class HotspotUpdate(BaseModel):
    title: Optional[str] = None
    summary: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[Dict[str, Any]] = None
    published_at: Optional[datetime] = None

class HotspotRead(HotspotBase):
    id: int
    fetched_at: datetime
    is_processed: bool

    class Config:
        from_attributes = True