#!/usr/bin/env python3
"""服装AI售后助手 - 后端主程序"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title="服装AI售后助手API",
    description="专注服装品类的AI客服助手后端服务",
    version="1.0.0"
)

# 跨域配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "服装AI售后助手API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "clothing-customer-service"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)