from fastapi import FastAPI
from app.routes import news
from app.db import engine, Base
from contextlib import asynccontextmanager

# 使用 lifespan 替代 on_event
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 应用启动前执行（类似 startup）
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # 应用关闭时执行（类似 shutdown）
    await engine.dispose()

app = FastAPI(
    title="Hotspot Aggregator Backend",
    lifespan=lifespan
)

# 注册路由
app.include_router(news.router)

@app.get("/")
async def root():
    return {"message": "Backend running successfully!"}