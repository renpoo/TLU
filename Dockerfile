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
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    fonts-noto-cjk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN rm -rf /root/.cache/matplotlib

# コンテナ内の作業ディレクトリ（Immutable Zone）
WORKDIR /app

# 依存パッケージのインストール（requirements.txtが存在する場合）
# TDDの高速化のため、依存解決レイヤーを先にキャッシュさせる
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    if [ -s requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# PYTHONPATHのパスを通し、srcディレクトリ内のモジュール解決を容易にする
ENV PYTHONPATH=/app/src

# 実行時のデフォルトエントリポイント（インタラクティブシェルを想定）
CMD ["/bin/bash"]
