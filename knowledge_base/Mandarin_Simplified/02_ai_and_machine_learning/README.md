# 人工智能和机器学习
结构化的参考文档集合，涵盖人工智能基础知识、模型架构、机器学习工程、语言和视觉处理以及人工智能伦理——从核心概念到生产部署。
＃＃ 结构
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

## 文件（按子类别）
### 基础
|文件|描述 |
|------|-------------|
| [artificial_intelligence.md](foundations/artificial_intelligence.md)|人工智能概述、机器学习、深度学习、法学硕士、伦理 |
| [ml_evaluation_and_workflow.md](foundations/ml_evaluation_and_workflow.md)|机器学习管道、指标、最佳实践 |
### 模型架构
|文件|描述 |
|------|-------------|
| [generative_ai_deep_dive.md](architectures/generative_ai_deep_dive.md)| GAN、VAE、扩散模型、法学硕士、生成式人工智能应用 |
| [graph_neural_networks.md](architectures/graph_neural_networks.md)| GCN、GAT、消息传递、知识图 |
| [reinforcement_learning.md](architectures/reinforcement_learning.md)| MDP、Q-learning、策略梯度、RLHF、多智能体系统 |
| [recommendation_systems.md](architectures/recommendation_systems.md)|协作过滤、基于内容、混合、矩阵分解 |
| [federated_learning_and_privacy.md](architectures/federated_learning_and_privacy.md)|去中心化训练、差异隐私、安全聚合 |
### 机器学习工程
|文件|描述 |
|------|-------------|
| [model_optimization_and_deployment.md](engineering/model_optimization_and_deployment.md)|量化、剪枝、蒸馏、ONNX、服务 |
| [ml_engineering_and_mlops.md](engineering/ml_engineering_and_mlops.md)|模型服务、注册表、部署策略、漂移监控 |
| [data_engineering_and_pipelines.md](engineering/data_engineering_and_pipelines.md)| ETL/ELT、数据湖、编排、Kafka、特征存储 |
| [local_ai_architecture.md](engineering/local_ai_architecture.md)|本地AI部署架构|
| [phi3_and_local_models.md](engineering/phi3_and_local_models.md)|本地运行模型 |
### NLP 和语音
|文件|描述 |
|------|-------------|
| [nlp_fundamentals.md](nlp_and_speech/nlp_fundamentals.md)|文本处理、嵌入、Transformers、BERT、GPT |
| [speech_and_audio_processing.md](nlp_and_speech/speech_and_audio_processing.md)| ASR、TTS、音频功能、耳语 |
| [time_series_and_forecasting.md](nlp_and_speech/time_series_and_forecasting.md)| ARIMA、Prophet、LSTM、季节性、异常检测 |
| [computer_vision_fundamentals.md](nlp_and_speech/computer_vision_fundamentals.md)| CNN、目标检测、分割、迁移学习 |
| [multimodal_ai.md](nlp_and_speech/multimodal_ai.md)|视觉语言模型、CLIP、DALL-E、跨模态学习 |
### 道德与安全
|文件|描述 |
|------|-------------|
| [ai_ethics_and_governance.md](ethics_and_safety/ai_ethics_and_governance.md)|人工智能偏见、公平、问责、监管、治理 |
| [ai_safety_and_alignment.md](ethics_and_safety/ai_safety_and_alignment.md)|对齐问题、RLHF、可解释性、AI 安全研究 |
## 建议的阅读路径
### **人工智能初学者路径**
1. `foundations/artificial_intelligence.md`——什么是人工智能？
2.`foundations/ml_evaluation_and_workflow.md`— ML 端到端的工作原理
3.`nlp_and_speech/nlp_fundamentals.md`— 文本和语言处理
4.`nlp_and_speech/computer_vision_fundamentals.md`— 图像和视觉处理
### **机器学习工程师路径**
1.`foundations/ml_evaluation_and_workflow.md`— 机器学习管道
2. `engineering/data_engineering_and_pipelines.md`——数据基础设施
3. `engineering/model_optimization_and_deployment.md`——模型优化
4.`engineering/ml_engineering_and_mlops.md`— MLOps 和服务
5.`engineering/local_ai_architecture.md`— 部署架构
### **研究路径**
1. `foundations/artificial_intelligence.md`——核心概念
2.`architectures/generative_ai_deep_dive.md`— 生成模型
3.`architectures/graph_neural_networks.md`— 基于图的模型
4. `architectures/reinforcement_learning.md`——强化学习和决策
5.`ethics_and_safety/ai_safety_and_alignment.md`— 安全考虑