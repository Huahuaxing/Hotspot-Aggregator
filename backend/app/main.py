from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routes import user, news
from app.db import engine, Base
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(
    title="Hotspot Aggregator Backend",
    lifespan=lifespan
)

app.mount("/", StaticFiles(directory="../frontend/dist", html=True), name="static")

# 添加CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],  # Vite默认端口
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 修复路由注册
app.include_router(user.router, prefix="/api/users", tags=["users"])
app.include_router(news.router, prefix="/api/news", tags=["news"])

@app.get("/")
async def root():
    return {"message": "Backend running successfully!"}