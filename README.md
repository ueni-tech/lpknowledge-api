# lpknowledge-api
# LPナレッジ検索API（フェーズ2）

FastAPI + LangChain + RAGを活用したコーディング規約Q&Aシステム
（フェーズ1のStreamlit版から API化への移行）

## フェーズ1からの主な変更点

- **UI**: Streamlit → FastAPI（Swagger UI）
- **ポート**: 8501 → 8000  
- **アクセス方法**: ブラウザUI → REST API
- **用途**: 単体アプリ → 他システムから利用可能なAPI

## クイックスタート

### 1. プロジェクト構造を作成
```bash
mkdir lpknowledge-api && cd lpknowledge-api

# フェーズ1と同様の基本構造 + FastAPI用構造
mkdir -p app/{core,models,api}
touch app/__init__.py app/core/__init__.py app/models/__init__.py app/api/__init__.py
```

### 2. 各ファイルを配置
- フェーズ1の設定を引き継ぎつつ、FastAPI向けに最適化済み
- 依存関係やボリューム設定はフェーズ1と互換

### 3. 環境設定
```bash
# .envファイルでOpenAI APIキーを設定（フェーズ1と同様）
OPENAI_API_KEY=your_actual_api_key_here
```

### 4. サーバー起動（フェーズ1の手順と類似）
```bash
# フェーズ1と同様のDocker Compose起動
docker-compose up --build
```

### 5. 動作確認
- **Swagger UI**: http://localhost:8000/docs（フェーズ1の8501から8000に変更）
- **ヘルスチェック**: http://localhost:8000/health
- **システム情報**: http://localhost:8000/api/v1/system/info

## 使用方法（フェーズ1からAPI化）

### フェーズ1（Streamlit UI）
```bash
# ブラウザでUI操作
# http://localhost:8501
```

### フェーズ2（REST API）
```bash
# 1. PDFアップロード
curl -X POST "http://localhost:8000/api/v1/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@coding_rules.pdf"

# 2. 質問・回答
curl -X POST "http://localhost:8000/api/v1/ask" \
  -H "Content-Type: application/json" \
  -d '{"question": "クラスの命名規則は？", "top_k": 3}'

# 3. 文書検索のみ
curl -X POST "http://localhost:8000/api/v1/search" \
  -H "Content-Type: application/json" \
  -d '{"question": "関数について", "top_k": 5}'
```

## フェーズ1との互換性

### 継承される機能
- ✅ PDF処理（PyPDF2）
- ✅ RAG処理（LangChain + OpenAI）
- ✅ ベクトルストア（ChromaDB永続化）
- ✅ Docker環境（ホットリロード対応）
- ✅ 環境変数設定

### API化による新機能
- 🆕 REST API提供
- 🆕 Swagger UI自動生成
- 🆕 他アプリからの利用可能
- 🆕 型安全なリクエスト/レスポンス

## 開発者向け情報

### ログ確認（フェーズ1と同様）
```bash
docker-compose logs -f api
```

### デバッグ（フェーズ1と同様）
```bash
docker-compose exec api bash
```

### ホットリロード（フェーズ1と同様）
- ファイル保存で自動反映
- bind-mountによるリアルタイム更新