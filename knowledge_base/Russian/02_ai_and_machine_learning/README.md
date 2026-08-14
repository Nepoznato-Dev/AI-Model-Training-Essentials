# ИИ и машинное обучение
Структурированная коллекция справочных документов, охватывающих основы искусственного интеллекта, модельную архитектуру, проектирование машинного обучения, обработку языка и изображения, а также этику искусственного интеллекта — от основных концепций до производственного развертывания.
## Структура
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

## Файлы по подкатегориям
### Фундаменты
| Файл | Описание |
|------|-------------|
| [artificial_intelligence.md](foundations/artificial_intelligence.md)| Обзор искусственного интеллекта, машинное обучение, глубокое обучение, степень магистра права, этика |
| [ml_evaluation_and_workflow.md](foundations/ml_evaluation_and_workflow.md)| Конвейеры машинного обучения, метрики, лучшие практики |
### Модели архитектуры
| Файл | Описание |
|------|-------------|
| [generative_ai_deep_dive.md](architectures/generative_ai_deep_dive.md)| GAN, VAE, диффузионные модели, LLM, генеративные приложения искусственного интеллекта |
| [graph_neural_networks.md](architectures/graph_neural_networks.md)| GCN, GAT, передача сообщений, графы знаний |
| [reinforcement_learning.md](architectures/reinforcement_learning.md)| MDP, Q-обучение, градиенты политики, RLHF, многоагентные системы |
| [recommendation_systems.md](architectures/recommendation_systems.md)| Совместная фильтрация, контентно-ориентированная, гибридная, матричная факторизация |
| [federated_learning_and_privacy.md](architectures/federated_learning_and_privacy.md)| Децентрализованное обучение, дифференцированная конфиденциальность, безопасное агрегирование |
### ML-инжиниринг
| Файл | Описание |
|------|-------------|
| [model_optimization_and_deployment.md](engineering/model_optimization_and_deployment.md)| Квантование, обрезка, дистилляция, ONNX, обслуживание |
| [ml_engineering_and_mlops.md](engineering/ml_engineering_and_mlops.md)| Обслуживание моделей, реестры, стратегии развертывания, мониторинг дрейфа |
| [data_engineering_and_pipelines.md](engineering/data_engineering_and_pipelines.md)| ETL/ELT, озера данных, оркестровка, Kafka, хранилища функций |
| [local_ai_architecture.md](engineering/local_ai_architecture.md)| Локальные архитектуры развертывания ИИ |
| [phi3_and_local_models.md](engineering/phi3_and_local_models.md)| Локальный запуск моделей |
### НЛП и речь
| Файл | Описание |
|------|-------------|
| [nlp_fundamentals.md](nlp_and_speech/nlp_fundamentals.md)| Обработка текста, встраивание, преобразователи, BERT, GPT |
| [speech_and_audio_processing.md](nlp_and_speech/speech_and_audio_processing.md)| ASR, TTS, аудиофункции, Whisper |
| [time_series_and_forecasting.md](nlp_and_speech/time_series_and_forecasting.md)| ARIMA, Prophet, LSTM, сезонность, обнаружение аномалий |
| [computer_vision_fundamentals.md](nlp_and_speech/computer_vision_fundamentals.md)| CNN, обнаружение объектов, сегментация, трансферное обучение |
| [multimodal_ai.md](nlp_and_speech/multimodal_ai.md)| Модели визуального языка, CLIP, DALL-E, кросс-модальное обучение |
### Этика и безопасность
| Файл | Описание |
|------|-------------|
| [ai_ethics_and_governance.md](ethics_and_safety/ai_ethics_and_governance.md)| Предвзятость ИИ, справедливость, подотчетность, регулирование, управление |
| [ai_safety_and_alignment.md](ethics_and_safety/ai_safety_and_alignment.md)| Проблема выравнивания, RLHF, интерпретируемость, исследование безопасности ИИ |
## Рекомендуемые пути чтения
### **Путь для начинающих**
1.`foundations/artificial_intelligence.md`— Что такое ИИ?
2.`foundations/ml_evaluation_and_workflow.md`— Как работает комплексное машинное обучение
3.`nlp_and_speech/nlp_fundamentals.md`— Обработка текста и языка.
4.`nlp_and_speech/computer_vision_fundamentals.md`— обработка изображений и изображений.
### **Путь инженера ML**
1.`foundations/ml_evaluation_and_workflow.md`— конвейеры ML
2.`engineering/data_engineering_and_pipelines.md`— Инфраструктура данных.
3.`engineering/model_optimization_and_deployment.md`— Оптимизация модели.
4.`engineering/ml_engineering_and_mlops.md`— MLOps и обслуживание
5.`engineering/local_ai_architecture.md`— Архитектура развертывания.
### **Путь исследования**
1.`foundations/artificial_intelligence.md`— Основные понятия
2.`architectures/generative_ai_deep_dive.md`— Генеративные модели.
3.`architectures/graph_neural_networks.md`— графические модели.
4.`architectures/reinforcement_learning.md`— RL и принятие решений
5.`ethics_and_safety/ai_safety_and_alignment.md`— Соображения безопасности.