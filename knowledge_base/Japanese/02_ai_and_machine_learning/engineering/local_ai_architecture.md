<!--
---
# Metadata
title: "Local AI Architecture"
description: "Local AI deployment architectures"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to engineering/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [local, ai, architecture, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# ローカル AI アーキテクチャ
大規模な言語モデルを完全にデバイス上で実行するための実践的なガイド。ハードウェアの考慮事項、推論エンジン、メモリの最適化、エッジ展開のためのシステム設計について説明します。
---

## AI をローカルで実行する理由
- **プライバシー**: デバイスからデータが流出することはありません。
- **コスト**: トークンごとの API 料金はかかりません。
- **レイテンシ**: 予測可能なネットワークフリーの推論。
- **オフライン可用性**: インターネットなしで動作します。
- **コントロール**: モデルのバージョン、カスタマイズ、微調整を完全にコントロールします。
---

## ハードウェア要件
### GPU メモリ (VRAM)
最も重要なリソース。メモリ内のモデル サイズ ≈ **パラメータ × パラメータあたりのバイト数**。
|精度 |パラメータごとのバイト数 | 3.8Bモデル | 7Bモデル | 13Bモデル | 70Bモデル |
|----------|----------|---------------|----------|-----------|-----------|
| FP32 | 4 | ～15 GB | ～28 GB | ～52 GB | ～280 GB |
| FP16 | 2 | ～7.6GB | ～14 GB | ～26 GB | ～140 GB |
| INT8 (8 ビット) | 1 | ～3.8 GB | ～7 GB | ～13 GB | ～70 GB |
| INT4 (4 ビット) | 0.5 | ～1.9 GB | ～3.5 GB | ～6.5GB | ～35 GB |
**実践的なガイドライン:**
- 8GB VRAM → 4 ビットで最大 7B モデル。
- 12GB VRAM → 4 ビットで最大 13B モデル。
- 24GB VRAM → 4 ビットで最大 70B モデル (または 8 ビットで 13B)。
- Apple Silicon (統合メモリ) は、64GB 以上のシステムで 70B モデルを実行できます。
### RAM (システムメモリ)
- CPU 推論の場合、モデルをロードするのに十分なシステム RAM (VRAM 数と同様) が必要です。
- GPU 推論の場合、VRAM にオフロードする前にモデルをメモリにロードするためにシステム RAM が重要になります。
### ストレージ
- 量子化されたモデルの重みは数 GB を占めます (例: ディスク上の 4 ビット 7B ≈ 4 GB)。複数のモデルで少なくとも 20 ～ 50 GB の空き容量を確保してください。
### CPU
- プロンプト処理 (プレフィル) と CPU オフロードには、最新のマルチコア CPU が役立ちます。
- Apple M シリーズ チップは、統合メモリとニューラル エンジンにより、LLM に対して優れたパフォーマンスを発揮します。
---

## 量子化
量子化により重みの数値精度が低下し、メモリが大幅に削減され、わずかな精度コストで速度が向上します。
### 一般的な形式
|フォーマット |ビット |説明 |一般的な使用法 |
|----------|------|---------------|---------------|
| **GGUF** | 4–8 | llama.cpp 形式、CPU/GPU ハイブリッド用に最適化 |ローカル推論に最適 |
| **GPTQ** | 4–8 | GPU のみ、CUDA で効率的 | NVIDIA GPU に最適 |
| **AWQ** | 4 |アクティベーション対応、GPU のみ | GPU でのバッチ推論に適しています |
| **ONNX** |変数 |標準化されたクロスプラットフォーム |生産サービス |
### 量子化レベルの選択
- **Q8_0** (8 ビット): 品質の低下は最小限、サイズは最大。
- **Q6_K** (6 ビット): 高品質、適切な圧縮。
- **Q5_K_M** (5 ビット): 一般的なスイート スポット。
- **Q4_K_M** (4 ビット): ほとんどのタスクで許容できる最小の品質。
- **IQ4_XS** / **IQ3_XS**: 4/3 ビットでのパープレキシティが向上し、量子化が改善されました。
**経験則:** 品質とサイズのバランスを良くするには、Q4_K_M を使用します。余分な VRAM がある場合は、Q5 または Q6 を使用してください。
---

## 推論エンジン (ローカル)
### ラマ.cpp
- C++ で書かれています。
- GGUF形式をサポートします。
- CPU および GPU 用に最適化 (CUDA、Metal、OpenCL 経由)。
- 特に CPU 上で非常に高速です。
- コマンドライン、サーバーモード、および Python バインディング。
**コマンドの例:**```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
# -ngl 32 offloads 32 layers to GPU
```

### オラマ
- シンプルな CLI と REST API で llama.cpp をラップします。
- モデルを自動ダウンロードし、管理します。
- プロトタイピングやデスクトップ アプリに最適です。
- システム プロンプトのカスタム モデルファイルをサポートします。
```bash
ollama run phi3:3.8b
ollama run llama3:8b
```

### LMスタジオ
- Windows、macOS、Linux 用のグラフィカル デスクトップ アプリ。
- ワンクリックのダウンロードとチャットインターフェイス。
- OpenAI互換APIを備えた内蔵ローカルサーバー。
- 技術者以外のユーザーや簡単なテストに適しています。
### ハグフェイストランスフォーマー + bitsandbytes
- HF モデル用の標準 Python ライブラリ。
- 4 ビット量子化には`bitsandbytes`を使用します (`load_in_4bit=True`)。
- 微調整には柔軟性がありますが、推論には llama.cpp よりも時間がかかります。
### ExLlamaV2
- GPTQ および AWQ の非常に高速な GPU 推論。
- NVIDIA GPU で最高のパフォーマンス。
- バッチ生成をサポートします。
### mlx (アップル)
- Apple の M シリーズ チップ用フレームワーク。
- Apple Silicon向けに高度に最適化されています。
- Python API。
---

## メモリ管理
### コンテキスト ウィンドウと KV キャッシュ
KV キャッシュには、コンテキスト内のすべてのレイヤーとすべてのトークンのキーと値のペアが保存されます。コンテキストの長さに応じて直線的に増加します。
メモリコスト ≈ 2 × レイヤー × (KV ヘッド × ヘッドディム) × トークン × 値ごとのバイト数
8 KV ヘッドと 128 ヘッドディムを備えた 32 層モデルの場合、各トークンのコストはトークンあたり約 32 × 8 × 128 × 2 バイト = 65 KB になります。 128,000 トークンの場合、キャッシュだけで約 8 GB になります。
### オフロード戦略
- **レイヤーのオフロード**: 一部のレイヤーを GPU に配置し、他のレイヤーを CPU に配置します。純粋な CPU よりも高速で、VRAM 要件が低くなります。
- **トークン ストリーミング**: トークンを一度に処理するのではなく、段階的に処理します。
### プロンプトキャッシュ
同様のプロンプト間で KV キャッシュを再利用して、事前入力フェーズの再計算を回避します。一部のフレームワークはこれをサポートしています (例: vLLM、`--prompt-cache` を備えた llama.cpp)。
### メモリマップされたファイル
モデルの重みを完全に RAM にロードせずに、ディスクから直接ロードします (メモリが制限されたシステム上の巨大なモデルに役立ちます)。 llama.cpp はデフォルトでメモリマッピングを使用します。
---

## 導入アーキテクチャ
### シングルデバイスモード
1 つのモデルは 1 つのマシン (ラップトップ、スマートフォン、エッジ デバイス) 上で実行されます。パーソナル アシスタント、メモを取るアプリ、コード補完に使用されます。
### ハイブリッド エッジ クラウド
ローカル モデルは一般的なクエリを処理します。複雑な質問にはクラウド モデルにフォールバックします。これにより、ほとんどの場合は速度/プライベート、エッジケースでは機能という両方の長所が得られます。
### 分散推論 (マルチ GPU)
より大きなモデルの場合は、複数の GPU にレイヤーを分割するか (テンソル並列処理)、デバイス間でコンテキストを分割します (パイプライン並列処理)。`-ngl`で llama.cpp を使用するか、`--num-gpu-layers`で ExLlamaV2 を使用します。
### モバイル展開
- **Android**: JNI バインディングまたは ML Kit 経由で llama.cpp を使用します。
- **iOS**: Swift バインディングまたは mlx 経由で llama.cpp を使用します。
- **Web**: WebLLM (ONNX ランタイム経由で WebGPU 上で実行) またはtransformers.js を使用します。
---

## パフォーマンスの最適化
### フラッシュアテンション
アテンションの計算を高速化し、メモリ使用量を削減します。 llama.cpp、ExLlamaV2、および最新のトランスフォーマー ライブラリで利用できます。
### バッチ推論
単一の転送パスで複数のプロンプトを処理します。スループットが大幅に向上します。`llama-batch`または vLLM を使用します。
### 早期停止/トークンの予算設定
無制限の生成を防ぐために、最大トークン予算を設定します。
### 投機的デコード
小規模な高速モデル (ドラフト) を使用してトークンを予測し、その後、大規模なモデルを並行して検証します。 2 ～ 3 倍の速度向上が得られます。
---

## 実践的なセットアップ ガイド
### 1. Ollama をインストールする
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. モデルをプルする
```bash
ollama pull phi3:3.8b-q4_K_M
```

### 3. API を使用して実行する
```bash
ollama serve
```

次に、リクエストを`http://localhost:11434/api/generate`に送信します。
### 4. Python の統合
```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
```

### 5. (代替案) llama.cpp を直接使用する
```bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
```

---

## 監視と可観測性
- GPU 使用率を追跡します (Linux では `nvidia-smi`、macOS ではアクティビティ モニター)。
- メモリ使用量 (RAM および VRAM) を追跡します。
- 1 秒あたりのトークンを追跡します (スループット)。
- 最初のトークンまでの時間を追跡します (待ち時間)。
- llama.cpp または Ollama の組み込みログを使用します。
---

## 制限とトレードオフ
- **品質ギャップ**: 小規模なローカル モデル (3.8B ～ 7B) は、一般に、複雑な推論において大規模なクラウド モデル (GPT-4、Claude 3.5) よりもパフォーマンスが劣ります。
- **知識のカットオフ**: モデルの知識はトレーニング時に凍結されます。 RAG を使用して現在の情報を注入します。
- **多言語**: 小型モデルでは多言語機能が低い場合があります。
- **ツールの使用**: 小規模なモデルでは、エージェント ワークフロー (関数呼び出し) の信頼性が低くなる可能性があります。
多くの日常的なタスク (要約、Q&A、コード補完、分類) については、ローカル モデルですでに十分であり、急速に改善されています。