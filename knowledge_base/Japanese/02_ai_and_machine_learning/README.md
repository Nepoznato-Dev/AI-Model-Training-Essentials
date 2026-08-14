# AI と機械学習
人工知能の基礎、モデル アーキテクチャ、ML エンジニアリング、言語および視覚処理、AI 倫理を中心的な概念から運用展開までカバーする、構造化された参考ドキュメントのコレクション。
＃＃ 構造
```
02_ai_and_machine_learning/
├── README.md                          ← You are here
├── foundations/                       ← Core AI/ML concepts and workflows
│   ├── artificial_intelligence.md        AI overview, ML, deep learning, LLMs
│   └── ml_evaluation_and_workflow.md     ML pipelines, metrics, best practices
├── architectures/                     ← Advanced model types
│   ├── generative_ai_deep_dive.md        GANs, VAEs, diffusion models, LLMs
│   ├── graph_neural_networks.md          GCNs, GATs, knowledge graphs
│   ├── reinforcement_learning.md         MDPs, Q-learning, RLHF, multi-agent
│   ├── recommendation_systems.md         Collaborative filtering, matrix factorisation
│   └── federated_learning_and_privacy.md Decentralised training, differential privacy
├── engineering/                       ← Deployment and infrastructure
│   ├── model_optimization_and_deployment.md  Quantisation, pruning, ONNX, serving
│   ├── ml_engineering_and_mlops.md           Model serving, registries, drift monitoring
│   ├── data_engineering_and_pipelines.md     ETL/ELT, data lakes, Kafka, feature stores
│   ├── local_ai_architecture.md              Local AI deployment architectures
│   └── phi3_and_local_models.md              Running models locally
├── nlp_and_speech/                    ← Language, vision, audio, and sequence models
│   ├── nlp_fundamentals.md               Text processing, embeddings, Transformers
│   ├── speech_and_audio_processing.md    ASR, TTS, Whisper, audio features
│   ├── time_series_and_forecasting.md    ARIMA, Prophet, LSTMs, seasonality
│   ├── computer_vision_fundamentals.md   CNNs, object detection, segmentation
│   └── multimodal_ai.md                  Vision-language models, CLIP, DALL-E
└── ethics_and_safety/                 ← Responsible AI
    ├── ai_ethics_and_governance.md       Bias, fairness, accountability, regulation
    └── ai_safety_and_alignment.md        Alignment problem, RLHF, interpretability
```

## サブカテゴリ別のファイル
### 基礎
|ファイル |説明 |
|------|---------------|
| [artificial_intelligence.md](foundations/artificial_intelligence.md)| AI の概要、ML、深層学習、LLM、倫理 |
| [ml_evaluation_and_workflow.md](foundations/ml_evaluation_and_workflow.md)| ML パイプライン、メトリクス、ベスト プラクティス |
### モデルのアーキテクチャ
|ファイル |説明 |
|------|---------------|
| [generative_ai_deep_dive.md](architectures/generative_ai_deep_dive.md)| GAN、VAE、拡散モデル、LLM、生成 AI アプリケーション |
| [graph_neural_networks.md](architectures/graph_neural_networks.md)| GCN、GAT、メッセージ パッシング、ナレッジ グラフ |
| [reinforcement_learning.md](architectures/reinforcement_learning.md)| MDP、Q ラーニング、ポリシー勾配、RLHF、マルチエージェント システム |
| [recommendation_systems.md](architectures/recommendation_systems.md)|協調フィルタリング、コンテンツベース、ハイブリッド、行列分解 |
| [federated_learning_and_privacy.md](architectures/federated_learning_and_privacy.md)|分散型トレーニング、差分プライバシー、安全な集約 |
### ML エンジニアリング
|ファイル |説明 |
|------|---------------|
| [model_optimization_and_deployment.md](engineering/model_optimization_and_deployment.md)|量子化、プルーニング、蒸留、ONNX、サービング |
| [ml_engineering_and_mlops.md](engineering/ml_engineering_and_mlops.md)|モデル提供、レジストリ、展開戦略、ドリフト監視 |
| [data_engineering_and_pipelines.md](engineering/data_engineering_and_pipelines.md)| ETL/ELT、データレイク、オーケストレーション、Kafka、機能ストア |
| [local_ai_architecture.md](engineering/local_ai_architecture.md)|ローカル AI 導入アーキテクチャ |
| [phi3_and_local_models.md](engineering/phi3_and_local_models.md)|モデルをローカルで実行する |
### NLP とスピーチ
|ファイル |説明 |
|------|---------------|
| [nlp_fundamentals.md](nlp_and_speech/nlp_fundamentals.md)|テキスト処理、埋め込み、トランスフォーマー、BERT、GPT |
| [speech_and_audio_processing.md](nlp_and_speech/speech_and_audio_processing.md)| ASR、TTS、オーディオ機能、ウィスパー |
| [time_series_and_forecasting.md](nlp_and_speech/time_series_and_forecasting.md)| ARIMA、Prophet、LSTM、季節性、異常検出 |
| [computer_vision_fundamentals.md](nlp_and_speech/computer_vision_fundamentals.md)| CNN、オブジェクト検出、セグメンテーション、転移学習 |
| [multimodal_ai.md](nlp_and_speech/multimodal_ai.md)|視覚言語モデル、CLIP、DALL-E、クロスモーダル学習 |
### 倫理と安全
|ファイル |説明 |
|------|---------------|
| [ai_ethics_and_governance.md](ethics_and_safety/ai_ethics_and_governance.md)| AI バイアス、公平性、説明責任、規制、ガバナンス |
| [ai_safety_and_alignment.md](ethics_and_safety/ai_safety_and_alignment.md)|アライメント問題、RLHF、解釈可能性、AI の安全性研究 |
## 推奨される読書パス
### **AI 初心者向けパス**
1.`foundations/artificial_intelligence.md`— AI とは何ですか?
2.`foundations/ml_evaluation_and_workflow.md`— ML がエンドツーエンドでどのように機能するか
3.`nlp_and_speech/nlp_fundamentals.md`— テキストと言語の処理
4.`nlp_and_speech/computer_vision_fundamentals.md`— 画像および視覚処理
### **ML エンジニア パス**
1.`foundations/ml_evaluation_and_workflow.md`— ML パイプライン
2.`engineering/data_engineering_and_pipelines.md`— データインフラストラクチャ
3.`engineering/model_optimization_and_deployment.md`— モデルの最適化
4.`engineering/ml_engineering_and_mlops.md`— MLOps とサービング
5.`engineering/local_ai_architecture.md`— 導入アーキテクチャ
### **研究パス**
1.`foundations/artificial_intelligence.md`— 中心となる概念
2.`architectures/generative_ai_deep_dive.md`— 生成モデル
3.`architectures/graph_neural_networks.md`— グラフベースのモデル
4.`architectures/reinforcement_learning.md`— RL と意思決定
5.`ethics_and_safety/ai_safety_and_alignment.md`— 安全上の考慮事項