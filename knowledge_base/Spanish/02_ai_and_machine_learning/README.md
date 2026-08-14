# IA y aprendizaje automático
Una colección estructurada de documentos de referencia que cubren los fundamentos de la inteligencia artificial, las arquitecturas de modelos, la ingeniería de aprendizaje automático, el procesamiento del lenguaje y la visión y la ética de la IA, desde los conceptos básicos hasta la implementación de producción.
## Estructura
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

## Archivos por subcategoría
### Fundaciones
| Archivo | Descripción |
|------|-------------|
| [artificial_intelligence.md](foundations/artificial_intelligence.md)| Descripción general de IA, ML, aprendizaje profundo, LLM, ética |
| [ml_evaluation_and_workflow.md](foundations/ml_evaluation_and_workflow.md)| Canalizaciones de aprendizaje automático, métricas y mejores prácticas |
### Arquitecturas modelo
| Archivo | Descripción |
|------|-------------|
| [generative_ai_deep_dive.md](architectures/generative_ai_deep_dive.md)| GAN, VAE, modelos de difusión, LLM, aplicaciones de IA generativa |
| [graph_neural_networks.md](architectures/graph_neural_networks.md)| GCN, GAT, paso de mensajes, gráficos de conocimiento |
| [reinforcement_learning.md](architectures/reinforcement_learning.md)| MDP, Q-learning, gradientes de políticas, RLHF, sistemas multiagente |
| [recommendation_systems.md](architectures/recommendation_systems.md)| Filtrado colaborativo, basado en contenidos, híbrido, factorización matricial |
| [federated_learning_and_privacy.md](architectures/federated_learning_and_privacy.md)| Formación descentralizada, privacidad diferencial, agregación segura |
### Ingeniería de aprendizaje automático
| Archivo | Descripción |
|------|-------------|
| [model_optimization_and_deployment.md](engineering/model_optimization_and_deployment.md)| Cuantificación, poda, destilación, ONNX, servicio |
| [ml_engineering_and_mlops.md](engineering/ml_engineering_and_mlops.md)| Servicio de modelos, registros, estrategias de implementación, monitoreo de deriva |
| [data_engineering_and_pipelines.md](engineering/data_engineering_and_pipelines.md)| ETL/ELT, lagos de datos, orquestación, Kafka, almacenes de funciones |
| [local_ai_architecture.md](engineering/local_ai_architecture.md)| Arquitecturas de implementación de IA local |
| [phi3_and_local_models.md](engineering/phi3_and_local_models.md)| Ejecutando modelos localmente |
### PNL y habla
| Archivo | Descripción |
|------|-------------|
| [nlp_fundamentals.md](nlp_and_speech/nlp_fundamentals.md)| Procesamiento de textos, incrustaciones, Transformers, BERT, GPT |
| [speech_and_audio_processing.md](nlp_and_speech/speech_and_audio_processing.md)| ASR, TTS, funciones de audio, Whisper |
| [time_series_and_forecasting.md](nlp_and_speech/time_series_and_forecasting.md)| ARIMA, Prophet, LSTM, estacionalidad, detección de anomalías |
| [computer_vision_fundamentals.md](nlp_and_speech/computer_vision_fundamentals.md)| CNN, detección de objetos, segmentación, aprendizaje por transferencia |
| [multimodal_ai.md](nlp_and_speech/multimodal_ai.md)| Modelos visión-lenguaje, CLIP, DALL-E, aprendizaje intermodal |
### Ética y Seguridad
| Archivo | Descripción |
|------|-------------|
| [ai_ethics_and_governance.md](ethics_and_safety/ai_ethics_and_governance.md)| Sesgo de IA, equidad, responsabilidad, regulación, gobernanza |
| [ai_safety_and_alignment.md](ethics_and_safety/ai_safety_and_alignment.md)| Problema de alineación, RLHF, interpretabilidad, investigación de seguridad de IA |
## Rutas de lectura sugeridas
### **Ruta para principiantes de IA**
1. `foundations/artificial_intelligence.md`: ¿Qué es la IA?
2. `foundations/ml_evaluation_and_workflow.md`: cómo funciona el aprendizaje automático de un extremo a otro
3. `nlp_and_speech/nlp_fundamentals.md`: procesamiento de texto y lenguaje
4. `nlp_and_speech/computer_vision_fundamentals.md`: procesamiento de imágenes y visión
### **Ruta del ingeniero de aprendizaje automático**
1. `foundations/ml_evaluation_and_workflow.md`: canalizaciones de aprendizaje automático
2. `engineering/data_engineering_and_pipelines.md`: infraestructura de datos
3. `engineering/model_optimization_and_deployment.md`: optimización del modelo
4. `engineering/ml_engineering_and_mlops.md`: MLOps y servicio
5. `engineering/local_ai_architecture.md`: arquitecturas de implementación
### **Ruta de investigación**
1. `foundations/artificial_intelligence.md`: conceptos básicos
2.`architectures/generative_ai_deep_dive.md`- Modelos generativos
3. `architectures/graph_neural_networks.md`: modelos basados en gráficos
4.`architectures/reinforcement_learning.md`— RL y toma de decisiones
5. `ethics_and_safety/ai_safety_and_alignment.md`: consideraciones de seguridad