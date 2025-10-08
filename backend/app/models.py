from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, func
from sqlalchemy.dialects.postgresql import JSONB
from .db import Base

class Zhihu_hot(Base):
    __tablename__ = "zhihu_hot"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(512), nullable=False)
    url = Column(String(2048), unique=True, nullable=False, index=True)
    source = Column(String(128), default="zhihu")
    summary = Column(Text)
    content = Column(Text)
    tags = Column(JSONB)
    published_at = Column(DateTime)
    fetched_at = Column(DateTime, server_default=func.now())
    is_processed = Column(Boolean, default=False)