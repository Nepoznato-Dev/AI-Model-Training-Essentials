# AI and Machine Learning

A structured collection of reference documents covering artificial intelligence fundamentals, model architectures, ML engineering, language and vision processing, and AI ethics — from core concepts to production deployment.

## Structure

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

## Files by Subcategory

### Foundations
| File | Description |
|------|-------------|
| [artificial_intelligence.md](foundations/artificial_intelligence.md) | AI overview, ML, deep learning, LLMs, ethics |
| [ml_evaluation_and_workflow.md](foundations/ml_evaluation_and_workflow.md) | ML pipelines, metrics, best practices |

### Model Architectures
| File | Description |
|------|-------------|
| [generative_ai_deep_dive.md](architectures/generative_ai_deep_dive.md) | GANs, VAEs, diffusion models, LLMs, generative AI applications |
| [graph_neural_networks.md](architectures/graph_neural_networks.md) | GCNs, GATs, message passing, knowledge graphs |
| [reinforcement_learning.md](architectures/reinforcement_learning.md) | MDPs, Q-learning, policy gradients, RLHF, multi-agent systems |
| [recommendation_systems.md](architectures/recommendation_systems.md) | Collaborative filtering, content-based, hybrid, matrix factorisation |
| [federated_learning_and_privacy.md](architectures/federated_learning_and_privacy.md) | Decentralised training, differential privacy, secure aggregation |

### ML Engineering
| File | Description |
|------|-------------|
| [model_optimization_and_deployment.md](engineering/model_optimization_and_deployment.md) | Quantisation, pruning, distillation, ONNX, serving |
| [ml_engineering_and_mlops.md](engineering/ml_engineering_and_mlops.md) | Model serving, registries, deployment strategies, drift monitoring |
| [data_engineering_and_pipelines.md](engineering/data_engineering_and_pipelines.md) | ETL/ELT, data lakes, orchestration, Kafka, feature stores |
| [local_ai_architecture.md](engineering/local_ai_architecture.md) | Local AI deployment architectures |
| [phi3_and_local_models.md](engineering/phi3_and_local_models.md) | Running models locally |

### NLP and Speech
| File | Description |
|------|-------------|
| [nlp_fundamentals.md](nlp_and_speech/nlp_fundamentals.md) | Text processing, embeddings, Transformers, BERT, GPT |
| [speech_and_audio_processing.md](nlp_and_speech/speech_and_audio_processing.md) | ASR, TTS, audio features, Whisper |
| [time_series_and_forecasting.md](nlp_and_speech/time_series_and_forecasting.md) | ARIMA, Prophet, LSTMs, seasonality, anomaly detection |
| [computer_vision_fundamentals.md](nlp_and_speech/computer_vision_fundamentals.md) | CNNs, object detection, segmentation, transfer learning |
| [multimodal_ai.md](nlp_and_speech/multimodal_ai.md) | Vision-language models, CLIP, DALL-E, cross-modal learning |

### Ethics and Safety
| File | Description |
|------|-------------|
| [ai_ethics_and_governance.md](ethics_and_safety/ai_ethics_and_governance.md) | AI bias, fairness, accountability, regulation, governance |
| [ai_safety_and_alignment.md](ethics_and_safety/ai_safety_and_alignment.md) | Alignment problem, RLHF, interpretability, AI safety research |

## Suggested Reading Paths

### **AI Beginner Path**
1. `foundations/artificial_intelligence.md` — What is AI?
2. `foundations/ml_evaluation_and_workflow.md` — How ML works end-to-end
3. `nlp_and_speech/nlp_fundamentals.md` — Text and language processing
4. `nlp_and_speech/computer_vision_fundamentals.md` — Image and vision processing

### **ML Engineer Path**
1. `foundations/ml_evaluation_and_workflow.md` — ML pipelines
2. `engineering/data_engineering_and_pipelines.md` — Data infrastructure
3. `engineering/model_optimization_and_deployment.md` — Model optimization
4. `engineering/ml_engineering_and_mlops.md` — MLOps and serving
5. `engineering/local_ai_architecture.md` — Deployment architectures

### **Research Path**
1. `foundations/artificial_intelligence.md` — Core concepts
2. `architectures/generative_ai_deep_dive.md` — Generative models
3. `architectures/graph_neural_networks.md` — Graph-based models
4. `architectures/reinforcement_learning.md` — RL and decision-making
5. `ethics_and_safety/ai_safety_and_alignment.md` — Safety considerations
