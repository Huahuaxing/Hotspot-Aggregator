from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, schemas

async def get_hotspots(db: AsyncSession, skip=0, limit=10):
    """获取知乎热点列表"""
    result = await db.execute(select(models.Zhihu_hot).offset(skip).limit(limit))
    return result.scalars().all()

async def create_hotspot(db: AsyncSession, hotspot: schemas.HotspotCreate):
    """创建知乎热点"""
    db_item = models.Zhihu_hot(**hotspot.dict())
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item

async def get_hotspot_by_id(db: AsyncSession, hotspot_id: int):
    """根据ID获取热点"""
    result = await db.execute(select(models.Zhihu_hot).where(models.Zhihu_hot.id == hotspot_id))
    return result.scalar_one_or_none()

async def get_hotspot_by_url(db: AsyncSession, url: str):
    """根据URL获取热点"""
    result = await db.execute(select(models.Zhihu_hot).where(models.Zhihu_hot.url == url))
    return result.scalar_one_or_none()

async def update_hotspot(db: AsyncSession, hotspot_id: int, hotspot_update: schemas.HotspotCreate):
    """更新热点信息"""
    result = await db.execute(select(models.Zhihu_hot).where(models.Zhihu_hot.id == hotspot_id))
    db_item = result.scalar_one_or_none()
    if db_item:
        for key, value in hotspot_update.dict().items():
            setattr(db_item, key, value)
        await db.commit()
        await db.refresh(db_item)
    return db_item

async def delete_hotspot(db: AsyncSession, hotspot_id: int):
    """删除热点"""
    result = await db.execute(select(models.Zhihu_hot).where(models.Zhihu_hot.id == hotspot_id))
    db_item = result.scalar_one_or_none()
    if db_item:
        await db.delete(db_item)
        await db.commit()
    return db_item