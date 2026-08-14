# AI와 머신러닝
핵심 개념부터 프로덕션 배포까지 인공 지능 기초, 모델 아키텍처, ML 엔지니어링, 언어 및 비전 처리, AI 윤리를 다루는 구조화된 참조 문서 모음입니다.
## 구조
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

## 하위 범주별 파일
### 기초
| 파일 | 설명 |
|------|-------------|
| [artificial_intelligence.md](foundations/artificial_intelligence.md)| AI 개요, ML, 딥 러닝, LLM, 윤리 |
| [ml_evaluation_and_workflow.md](foundations/ml_evaluation_and_workflow.md)| ML 파이프라인, 측정항목, 모범 사례 |
### 모델 아키텍처
| 파일 | 설명 |
|------|-------------|
| [generative_ai_deep_dive.md](architectures/generative_ai_deep_dive.md)| GAN, VAE, 확산 모델, LLM, 생성 AI 애플리케이션 |
| [graph_neural_networks.md](architectures/graph_neural_networks.md)| GCN, GAT, 메시지 전달, 지식 그래프 |
| [reinforcement_learning.md](architectures/reinforcement_learning.md)| MDP, Q-러닝, 정책 변화도, RLHF, 다중 에이전트 시스템 |
| [recommendation_systems.md](architectures/recommendation_systems.md)| 협업 필터링, 콘텐츠 기반, 하이브리드, 행렬 분해 |
| [federated_learning_and_privacy.md](architectures/federated_learning_and_privacy.md)| 분산형 교육, 차등 개인 정보 보호, 보안 집계 |
### ML 엔지니어링
| 파일 | 설명 |
|------|-------------|
| [model_optimization_and_deployment.md](engineering/model_optimization_and_deployment.md)| 정량화, 가지치기, 증류, ONNX, 서빙 |
| [ml_engineering_and_mlops.md](engineering/ml_engineering_and_mlops.md)| 모델 제공, 레지스트리, 배포 전략, 드리프트 모니터링 |
| [data_engineering_and_pipelines.md](engineering/data_engineering_and_pipelines.md)| ETL/ELT, 데이터 레이크, 오케스트레이션, Kafka, 피처 스토어 |
| [local_ai_architecture.md](engineering/local_ai_architecture.md)| 로컬 AI 배포 아키텍처 |
| [phi3_and_local_models.md](engineering/phi3_and_local_models.md)| 로컬에서 모델 실행 |
### NLP와 연설
| 파일 | 설명 |
|------|-------------|
| [nlp_fundamentals.md](nlp_and_speech/nlp_fundamentals.md)| 텍스트 처리, 임베딩, 변환기, BERT, GPT |
| [speech_and_audio_processing.md](nlp_and_speech/speech_and_audio_processing.md)| ASR, TTS, 오디오 기능, 속삭임 |
| [time_series_and_forecasting.md](nlp_and_speech/time_series_and_forecasting.md)| ARIMA, Prophet, LSTM, 계절성, 이상 탐지 |
| [computer_vision_fundamentals.md](nlp_and_speech/computer_vision_fundamentals.md)| CNN, 객체 감지, 분할, 전이 학습 |
| [multimodal_ai.md](nlp_and_speech/multimodal_ai.md)| 비전 언어 모델, CLIP, DALL-E, 교차 모달 학습 |
### 윤리 및 안전
| 파일 | 설명 |
|------|-------------|
| [ai_ethics_and_governance.md](ethics_and_safety/ai_ethics_and_governance.md)| AI 편견, 공정성, 책임, 규제, 거버넌스 |
| [ai_safety_and_alignment.md](ethics_and_safety/ai_safety_and_alignment.md)| 정렬 문제, RLHF, 해석성, AI 안전성 연구 |
## 권장 읽기 경로
### **AI 초보자 경로**
1.`foundations/artificial_intelligence.md`— AI란 무엇입니까?
2.`foundations/ml_evaluation_and_workflow.md`— ML이 엔드 투 엔드로 작동하는 방식
3.`nlp_and_speech/nlp_fundamentals.md`— 텍스트 및 언어 처리
4.`nlp_and_speech/computer_vision_fundamentals.md`— 이미지 및 비전 처리
### **ML 엔지니어 경로**
1.`foundations/ml_evaluation_and_workflow.md`— ML 파이프라인
2.`engineering/data_engineering_and_pipelines.md`— 데이터 인프라
3.`engineering/model_optimization_and_deployment.md`— 모델 최적화
4.`engineering/ml_engineering_and_mlops.md`— MLOps 및 제공
5.`engineering/local_ai_architecture.md`— 배포 아키텍처
### **연구 경로**
1.`foundations/artificial_intelligence.md`— 핵심 개념
2.`architectures/generative_ai_deep_dive.md`— 생성 모델
3.`architectures/graph_neural_networks.md`— 그래프 기반 모델
4.`architectures/reinforcement_learning.md`— RL 및 의사결정
5.`ethics_and_safety/ai_safety_and_alignment.md`— 안전 고려사항