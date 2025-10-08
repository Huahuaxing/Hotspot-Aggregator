from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import News
from app.schemas import NewsCreate

async def create_news(db: AsyncSession, news: NewsCreate):
    db_news = News(**news.dict())
    db.add(db_news)
    await db.commit()
    await db.refresh(db_news)
    return db_news

async def get_news_list(db: AsyncSession, limit: int = 20):
    result = await db.execute(select(News).order_by(News.created_at.desc()).limit(limit))
    return result.scalars().all()
