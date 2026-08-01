<!-- 
This file was automatically translated from English to Japanese.
Source: local_ai_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# ローカル AI アーキテクチャ

大規模言語モデルを完全にオンデバイスで動かすための実践的ガイドです。ハードウェア要件、推論エンジン、メモリ最適化、エッジデプロイ向けシステム設計を扱います。

---

## なぜ AI をローカルで動かすのか

- **Privacy**: データが端末の外に出ない
- **Cost**: token ごとの API 料金がかからない
- **Latency**: ネットワークに依存しない、安定した低遅延推論ができる
- **Offline availability**: インターネットがなくても動く
- **Control**: モデルのバージョン、カスタマイズ、fine-tuning を自分で管理できる

---

## ハードウェア要件

### GPU メモリ（VRAM）
もっとも重要な資源です。メモリ上のモデルサイズはおおむね **パラメータ数 × 1 パラメータ当たりのバイト数** で見積もれます。

| Precision | Bytes per parameter | 3.8B model | 7B model | 13B model | 70B model |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32      | 4                   | ~15 GB     | ~28 GB   | ~52 GB    | ~280 GB   |
| FP16      | 2                   | ~7.6 GB    | ~14 GB   | ~26 GB    | ~140 GB   |
| INT8 (8-bit) | 1              | ~3.8 GB    | ~7 GB    | ~13 GB    | ~70 GB    |
| INT4 (4-bit) | 0.5            | ~1.9 GB    | ~3.5 GB  | ~6.5 GB   | ~35 GB    |

**実用上の目安:**
- 8GB VRAM → 4-bit なら 7B モデル程度まで
- 12GB VRAM → 4-bit なら 13B モデル程度まで
- 24GB VRAM → 4-bit なら 70B モデル、8-bit なら 13B モデル程度まで
- Apple Silicon（unified memory）は 64GB 以上あれば 70B モデルも動かせることがある

### RAM（システムメモリ）
- CPU 推論では、モデル全体を読み込めるだけの RAM が必要です（概ね VRAM と同程度の目安）。
- GPU 推論でも、VRAM にオフロードする前にモデルを読み込むためのシステム RAM が重要です。

### ストレージ
- 量子化済みモデルの重みでも数 GB を使います（例: 4-bit の 7B でディスク上約 4 GB）。複数モデルを扱うなら、少なくとも 20〜50 GB 程度の空きがあると安心です。

### CPU
- prompt 処理（prefill）や CPU offloading では、現代的なマルチコア CPU が役立ちます。
- Apple M シリーズは unified memory と Neural Engine により、LLM 実行に非常に相性が良いです。

---

## 量子化（Quantisation）

量子化は重みの数値精度を下げることで、精度低下を小さく抑えつつ、メモリ使用量を大幅に減らし、速度を高める手法です。

### よく使われる形式

| Format | Bits | 説明 | 主な用途 |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | llama.cpp 形式。CPU / GPU ハイブリッドに最適化 | ローカル推論向けの定番 |
| **GPTQ** | 4–8 | GPU 専用で CUDA 上で効率的 | NVIDIA GPU 向け |
| **AWQ** | 4 | activation-aware な量子化。GPU 専用 | GPU での batch inference 向け |
| **ONNX** | variable | 標準化され、クロスプラットフォーム | 本番サービング向け |

### 量子化レベルの選び方
- **Q8_0**（8-bit）: 品質低下が最小で、サイズは大きい
- **Q6_K**（6-bit）: 品質と圧縮率のバランスが良い
- **Q5_K_M**（5-bit）: 実用上の定番バランス
- **Q4_K_M**（4-bit）: もっとも軽く、多くの用途で十分な品質
- **IQ4_XS** / **IQ3_XS**: 4 / 3 bit 帯で perplexity 改善を狙った量子化

**経験則:** 品質とサイズのバランスを取るなら Q4_K_M が無難です。VRAM に余裕があるなら Q5 や Q6 を選ぶとよいでしょう。

---

## ローカル推論エンジン

### llama.cpp
- C++ で書かれている
- GGUF 形式に対応している
- CUDA、Metal、OpenCL を通じて CPU / GPU の両方を活用できる
- 特に CPU 上で高速
- コマンドライン、server mode、Python binding がある

**例:**
```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
```

`-ngl 32` は 32 層を GPU にオフロードする指定です。

### Ollama
- llama.cpp を、使いやすい CLI と REST API で包んだツール
- モデルの自動ダウンロードや管理を行う
- プロトタイピングやデスクトップアプリに向く
- system prompt を定義する custom Modelfile に対応

**使い方:**
```bash
ollama run phi3:3.8b
ollama run llama3:8b
```

### LM Studio
- Windows、macOS、Linux 向けの GUI デスクトップアプリ
- ワンクリックのダウンロードとチャット UI を備える
- OpenAI 互換 API を持つローカルサーバーを内蔵
- 非技術者や素早い試用に向いている

### Hugging Face Transformers + bitsandbytes
- Hugging Face モデル向けの標準的な Python ライブラリ群
- `load_in_4bit=True` などで bitsandbytes による 4-bit 量子化を使える
- fine-tuning の自由度は高いが、推論は llama.cpp より遅いことが多い

### ExLlamaV2
- GPTQ と AWQ 向けの非常に高速な GPU 推論エンジン
- NVIDIA GPU で特に高性能
- batched generation に対応

### mlx（Apple）
- Apple が M シリーズ向けに提供するフレームワーク
- Apple Silicon 上で高度に最適化されている
- Python API を利用できる

---

## メモリ管理

### Context Window と KV Cache
KV cache は、各層・各 token の key-value pair を保存する領域で、context length に比例して増えます。

メモリコストのおおまかな式:

`2 × layers × (KV heads × head dim) × tokens × bytes per value`

たとえば 32 層、KV heads が 8、head dim が 128 のモデルでは、1 token 当たり約 65 KB が必要です。128k tokens になると、cache だけで約 8 GB になります。

### オフロード戦略
- **Layer offloading**: 一部の層を GPU、残りを CPU に置く。純 CPU より速く、必要 VRAM を抑えられる
- **Token streaming**: まとめてではなく token を逐次処理する

### Prompt Caching
類似した prompt 間で KV cache を再利用し、prefill を再計算しないようにする方法です。vLLM や `llama.cpp --prompt-cache` などで利用できます。

### Memory-Mapped Files
巨大モデルで RAM が限られる環境では、重み全体を RAM に載せず、ディスクから直接 memory-map して扱う方法が有効です。llama.cpp はデフォルトでこれを使います。

---

## デプロイアーキテクチャ

### Single-Device Mode
1 台のマシン（ノート PC、スマートフォン、エッジデバイス）で 1 つのモデルを動かす方式です。個人アシスタント、ノートアプリ、コード補完などに向きます。

### Hybrid Edge-Cloud
一般的な問い合わせはローカルモデルで処理し、複雑な質問だけクラウドモデルへフォールバックする方式です。速度とプライバシーを確保しつつ、難問への対応力も得られます。

### Distributed Inference（Multi-GPU）
大きなモデルでは、層を複数 GPU に分散したり（tensor parallelism）、context を機器間で分けたり（pipeline parallelism）します。llama.cpp の `-ngl` や ExLlamaV2 の `--num-gpu-layers` などが使われます。

### モバイルデプロイ
- **Android**: JNI binding や ML Kit 経由で llama.cpp を使う
- **iOS**: Swift binding や mlx 経由で llama.cpp を使う
- **Web**: WebLLM（WebGPU + ONNX runtime）や transformers.js を使う

---

## パフォーマンス最適化

### Flash Attention
attention 計算を高速化し、メモリ使用量も減らす手法です。llama.cpp、ExLlamaV2、近年の transformers library で利用できます。

### Batch Inference
複数の prompt を 1 回の forward pass で処理する方法です。throughput を大きく高められます。llama-batch や vLLM が代表的です。

### Early Stopping / Token Budgeting
生成が際限なく続かないよう、最大 token 数の上限を設けます。

### Speculative Decoding
小型高速モデル（draft model）で token を先読みし、大型モデルで並列に検証する方法です。2〜3 倍の高速化が得られることがあります。

---

## 実践セットアップガイド

1. **Ollama をインストールする**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

2. **モデルを取得する**
```bash
ollama pull phi3:3.8b-q4_K_M
```

3. **API として起動する**
```bash
ollama serve
```

その後、`http://localhost:11434/api/generate` にリクエストを送ります。

4. **Python から連携する**
```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
```

5. **別案: llama.cpp を直接使う**
```bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
```

---

## 監視と可観測性

- GPU 使用率を追跡する（Linux では `nvidia-smi`、macOS では Activity Monitor など）
- メモリ使用量（RAM と VRAM）を確認する
- 1 秒当たりの token 数（throughput）を測る
- 最初の token が返るまでの時間（latency）を測る
- llama.cpp や Ollama の組み込みログを活用する

---

## 制約とトレードオフ

- **品質差**: 小型ローカルモデル（3.8B〜7B）は、複雑な推論では GPT-4 や Claude 3.5 などの大型クラウドモデルに及ばないことが多い
- **Knowledge cutoff**: モデルの知識は学習時点で固定されるため、最新情報には RAG などで補う必要がある
- **多言語性能**: 小型モデルは多言語能力が弱い場合がある
- **Tool use**: function calling を含む agentic workflow は、小型モデルでは信頼性が低いことがある

それでも、要約、Q&A、コード補完、分類といった日常的な多くのタスクでは、ローカルモデルはすでに十分実用的であり、今も急速に改善しています。
