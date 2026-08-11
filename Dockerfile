# ==========================================
# Dockerfile
# TLU System: Hybrid Execution Environment
# ==========================================
FROM python:3.12-slim

# Unix哲学に基づく事前フィルタリング・結合層のための標準ツール群をインストール
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gawk \
    grep \
    bc \
    coreutils \
    jq \
    fonts-noto-cjk \
    && rm -rf /var/lib/apt/lists/*

# コンテナ内の作業ディレクトリ（Immutable Zone）
WORKDIR /app

# 非rootユーザーの作成 (TLU Security Hardening)
RUN useradd -m -u 1000 tluuser && \
    chown -R tluuser:tluuser /app

# 依存パッケージのインストール（requirements.txtが存在する場合）
# TDDの高速化のため、依存解決レイヤーを先にキャッシュさせる
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    if [ -s requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# ソースコードと成果物権限の設定
COPY --chown=tluuser:tluuser . /app

# 非rootユーザーへ切り替え
USER tluuser

# PYTHONPATHのパスを通し、srcディレクトリ内のモジュール解決を容易にする
ENV PYTHONPATH=/app/src

# 実行時のデフォルトエントリポイント（インタラクティブシェルを想定）
CMD ["/bin/bash"]
