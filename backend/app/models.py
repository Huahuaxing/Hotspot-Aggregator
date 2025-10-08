from sqlalchemy import Column, Integer, String, DateTime, func
from app.db import Base

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256), nullable=False)
    url = Column(String(512), nullable=False, unique=True)
    source = Column(String(128))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
