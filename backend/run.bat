@echo off
REM 启动 FastAPI 服务
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000