from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db import engine, Base
from app.routers import hotspots

# 定义 lifespan 异步上下文管理器
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动事件
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # 关闭事件（可选，如果有清理逻辑可以写在这里）
    # await engine.dispose()  # 示例

# 创建 FastAPI 实例，并传入 lifespan
app = FastAPI(title="Hotspot Aggregator API", lifespan=lifespan)

# 注册路由
app.include_router(hotspots.router)

# 根路由
@app.get("/")
def root():
    return {"msg": "Hotspot Aggregator API is running 🚀"}

