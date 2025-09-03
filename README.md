# openai-api-sample

## 概要
OpenAI 互換エンドポイントに接続し、コマンドライン上で対話できるサンプルを含みます。

## 動作要件
- Python 3.9 以上
- `pip` と（推奨）仮想環境ツール

## セットアップ
```bash
# 依存パッケージのインストール（任意で仮想環境を使用）
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 環境変数ファイルを作成
cp .env.example .env
# .env を編集して OPENAI_API_KEY を設定（このファイルはコミットしない）
```

主要な環境変数（.env で定義）
- `OPENAI_API_KEY`: API キー（必須）
- `OPENAI_BASE_URL`: ベース URL（既定: `http://ip-61-206-39-8.aits-tyo-02.v4.digital-dynamic.co.jp:8000/v1/`）
- `OPENAI_MODEL`: モデル名（既定: `openai/gpt-oss-120b`）

## 使い方（CLI チャット）
```bash
python examples/chat_cli.py
```
- プロンプトにメッセージを入力して Enter。
- `Ctrl+C` で終了、`/reset` で会話履歴をリセット。
- 応答はストリーミングで逐次表示されます。

## ファイル構成（抜粋）
- `examples/chat_cli.py`: 対話用 CLI スクリプト
- `.env.example`: 環境変数のテンプレート（`.env` にコピーして編集）
- `requirements.txt`: Python 依存関係

## 注意事項
- API キー等の秘密情報は `.env` にのみ記載し、決してコミットしないでください。
