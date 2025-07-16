"""
最小限のFastAPIアプリケーション - 段階的テスト用

まずは基本的な動作確認から始めます
"""

from fastapi import FastAPI
from datetime import datetime

# 最小限のFastAPIアプリケーション
app = FastAPI(title="LPナレッジ検索API", version="0.1.0", description="段階的テスト版")


@app.get("/")
async def root():
    """ルートエンドポイント"""
    return {
        "message": "LPナレッジ検索API - 動作中",
        "timestamp": datetime.now().isoformat(),
        "status": "OK",
    }


@app.get("/health")
async def health_check():
    """ヘルスチェック"""
    return {
        "status": "healthy",
        "service": "lpknowledge-api",
        "version": "0.1.0",
        "timestamp": datetime.now().isoformat(),
    }


@app.get("/test")
async def test_endpoint():
    """テスト用エンドポイント"""
    return {
        "message": "テストエンドポイントが正常に動作しています",
        "docker_environment": "正常",
        "fastapi_version": "動作中",
    }
