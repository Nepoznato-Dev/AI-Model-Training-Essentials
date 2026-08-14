# 人工智慧和機器學習
結構化的參考文件集合，涵蓋人工智慧基礎知識、模型架構、機器學習工程、語言和視覺處理以及人工智慧倫理——從核心概念到生產部署。
＃＃ 結構
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

## 檔案（按子類別）
### 基礎
|文件|描述 |
|------|-------------|
|[artificial_intelligence.md](foundations/artificial_intelligence.md)|人工智慧概述、機器學習、深度學習、法學碩士、倫理 |
|[ml_evaluation_and_workflow.md](foundations/ml_evaluation_and_workflow.md)|機器學習管道、指標、最佳實踐 |
### 模型架構
|文件|描述 |
|------|-------------|
|[generative_ai_deep_dive.md](architectures/generative_ai_deep_dive.md)| GAN、VAE、擴散模型、法學碩士、生成式人工智慧應用 |
|[graph_neural_networks.md](architectures/graph_neural_networks.md)| GCN、GAT、訊息傳遞、知識圖 |
|[reinforcement_learning.md](architectures/reinforcement_learning.md)| MDP、Q-learning、策略梯度、RLHF、多智能體系統 |
|[recommendation_systems.md](architectures/recommendation_systems.md)|協作過濾、基於內容、混合、矩陣分解 |
|[federated_learning_and_privacy.md](architectures/federated_learning_and_privacy.md)|去中心化訓練、差異隱私、安全聚合 |
### 機器學習工程
|文件|描述 |
|------|-------------|
|[model_optimization_and_deployment.md](engineering/model_optimization_and_deployment.md)|量化、剪枝、蒸餾、ONNX、服務 |
|[ml_engineering_and_mlops.md](engineering/ml_engineering_and_mlops.md)|模型服務、登錄、部署原則、漂移監控 |
|[data_engineering_and_pipelines.md](engineering/data_engineering_and_pipelines.md)| ETL/ELT、資料湖、編排、Kafka、特徵儲存 |
|[local_ai_architecture.md](engineering/local_ai_architecture.md)|本地AI部署架構|
|[phi3_and_local_models.md](engineering/phi3_and_local_models.md)|本地運行模型 |
### NLP 和語音
|文件|描述 |
|------|-------------|
|[nlp_fundamentals.md](nlp_and_speech/nlp_fundamentals.md)|文字處理、嵌入、Transformers、BERT、GPT |
|[speech_and_audio_processing.md](nlp_and_speech/speech_and_audio_processing.md)| ASR、TTS、音訊功能、耳語 |
|[time_series_and_forecasting.md](nlp_and_speech/time_series_and_forecasting.md)| ARIMA、Prophet、LSTM、季節性、異常檢測 |
|[computer_vision_fundamentals.md](nlp_and_speech/computer_vision_fundamentals.md)| CNN、目標偵測、分割、遷移學習 |
|[multimodal_ai.md](nlp_and_speech/multimodal_ai.md)|視覺語言模型、CLIP、DALL-E、跨模態學習 |
### 道德与安全
|文件|描述 |
|------|-------------|
|[ai_ethics_and_governance.md](ethics_and_safety/ai_ethics_and_governance.md)|人工智慧偏見、公平、問責、監管、治理 |
|[ai_safety_and_alignment.md](ethics_and_safety/ai_safety_and_alignment.md)|對齊問題、RLHF、可解釋性、AI 安全研究 |
## 建議的閱讀路徑
### **人工智慧初學者路徑**
1. `foundations/artificial_intelligence.md`－什麼是人工智慧？
2.`foundations/ml_evaluation_and_workflow.md`— ML 端對端的工作原理
3.`nlp_and_speech/nlp_fundamentals.md`— 文字與語言處理
4.`nlp_and_speech/computer_vision_fundamentals.md`— 影像與視覺處理
### **機器學習工程師路徑**
1.`foundations/ml_evaluation_and_workflow.md`— 機器學習管道
2. `engineering/data_engineering_and_pipelines.md`－資料基礎設施
3. `engineering/model_optimization_and_deployment.md`－模型最佳化
4.`engineering/ml_engineering_and_mlops.md`— MLOps 和服務
5.`engineering/local_ai_architecture.md`— 部署架構
### **研究路径**
1. `foundations/artificial_intelligence.md`——核心概念
2.`architectures/generative_ai_deep_dive.md`— 生成模型
3.`architectures/graph_neural_networks.md`— 基於圖的模型
4. `architectures/reinforcement_learning.md`－強化學習與決策
5.`ethics_and_safety/ai_safety_and_alignment.md`— 安全考慮