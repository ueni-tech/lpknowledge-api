"""
依存関係管理モジュール
FastAPIの依存性注入で使用する関数を集約
"""

from .rag_engine import RAGEngine

# グローバルRAGエンジンインスタンス
_rag_engine: RAGEngine | None = None


async def initialize_rag_engine() -> None:
    """RAGエンジンを初期化"""
    global _rag_engine
    _rag_engine = RAGEngine()
    await _rag_engine.initialize()


def get_rag_engine() -> RAGEngine:
    """RAGエンジンインスタンスを取得
    FastAPIの依存性注入で使用
    """
    if _rag_engine is None:
        raise RuntimeError("RAGエンジンが初期化されていません")
    return _rag_engine


def get_rag_engine_instance() -> RAGEngine | None:
    """RAGエンジンインスタンスを直接取得（内部使用）"""
    return _rag_engine
