# IA e aprendizado de máquina
Uma coleção estruturada de documentos de referência que abrangem fundamentos de inteligência artificial, arquiteturas de modelos, engenharia de ML, processamento de linguagem e visão e ética de IA — desde conceitos básicos até implantação de produção.
## Estrutura
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

## Arquivos por subcategoria
### Fundações
| Arquivo | Descrição |
|------|-------------|
| [artificial_intelligence.md](foundations/artificial_intelligence.md)| Visão geral de IA, ML, aprendizagem profunda, LLMs, ética |
| [ml_evaluation_and_workflow.md](foundations/ml_evaluation_and_workflow.md)| Pipelines de ML, métricas, práticas recomendadas |
### Arquiteturas de Modelo
| Arquivo | Descrição |
|------|-------------|
| [generative_ai_deep_dive.md](architectures/generative_ai_deep_dive.md)| GANs, VAEs, modelos de difusão, LLMs, aplicações generativas de IA |
| [graph_neural_networks.md](architectures/graph_neural_networks.md)| GCNs, GATs, passagem de mensagens, gráficos de conhecimento |
| [reinforcement_learning.md](architectures/reinforcement_learning.md)| MDPs, Q-learning, gradientes de políticas, RLHF, sistemas multiagentes |
| [recommendation_systems.md](architectures/recommendation_systems.md)| Filtragem colaborativa, baseada em conteúdo, híbrida, fatoração matricial |
| [federated_learning_and_privacy.md](architectures/federated_learning_and_privacy.md)| Treinamento descentralizado, privacidade diferencial, agregação segura |
### Engenharia de ML
| Arquivo | Descrição |
|------|-------------|
| [model_optimization_and_deployment.md](engineering/model_optimization_and_deployment.md)| Quantização, poda, destilação, ONNX, serviço |
| [ml_engineering_and_mlops.md](engineering/ml_engineering_and_mlops.md)| Atendimento de modelos, registros, estratégias de implantação, monitoramento de desvios |
| [data_engineering_and_pipelines.md](engineering/data_engineering_and_pipelines.md)| ETL/ELT, data lakes, orquestração, Kafka, feature stores |
| [local_ai_architecture.md](engineering/local_ai_architecture.md)| Arquiteturas locais de implantação de IA |
| [phi3_and_local_models.md](engineering/phi3_and_local_models.md)| Executando modelos localmente |
### PNL e fala
| Arquivo | Descrição |
|------|-------------|
| [nlp_fundamentals.md](nlp_and_speech/nlp_fundamentals.md)| Processamento de texto, embeddings, Transformers, BERT, GPT |
| [speech_and_audio_processing.md](nlp_and_speech/speech_and_audio_processing.md)| ASR, TTS, recursos de áudio, Whisper |
| [time_series_and_forecasting.md](nlp_and_speech/time_series_and_forecasting.md)| ARIMA, Profeta, LSTMs, sazonalidade, detecção de anomalias |
| [computer_vision_fundamentals.md](nlp_and_speech/computer_vision_fundamentals.md)| CNNs, detecção de objetos, segmentação, aprendizagem por transferência |
| [multimodal_ai.md](nlp_and_speech/multimodal_ai.md)| Modelos de linguagem visual, CLIP, DALL-E, aprendizagem intermodal |
### Ética e Segurança
| Arquivo | Descrição |
|------|-------------|
| [ai_ethics_and_governance.md](ethics_and_safety/ai_ethics_and_governance.md)| Preconceito da IA, justiça, responsabilidade, regulamentação, governança |
| [ai_safety_and_alignment.md](ethics_and_safety/ai_safety_and_alignment.md)| Problema de alinhamento, RLHF, interpretabilidade, pesquisa de segurança de IA |
## Caminhos de leitura sugeridos
### **Caminho para iniciantes em IA**
1.`foundations/artificial_intelligence.md`— O que é IA?
2.`foundations/ml_evaluation_and_workflow.md`— Como o ML funciona de ponta a ponta
3.`nlp_and_speech/nlp_fundamentals.md`— Processamento de texto e linguagem
4.`nlp_and_speech/computer_vision_fundamentals.md`— Processamento de imagem e visão
### **Caminho de engenheiro de ML**
1.`foundations/ml_evaluation_and_workflow.md`— pipelines de ML
2.`engineering/data_engineering_and_pipelines.md`— Infraestrutura de dados
3.`engineering/model_optimization_and_deployment.md`— Otimização do modelo
4.`engineering/ml_engineering_and_mlops.md`— MLOps e veiculação
5.`engineering/local_ai_architecture.md`— Arquiteturas de implantação
### **Caminho de pesquisa**
1.`foundations/artificial_intelligence.md`— Conceitos básicos
2.`architectures/generative_ai_deep_dive.md`— Modelos generativos
3.`architectures/graph_neural_networks.md`— Modelos baseados em gráficos
4.`architectures/reinforcement_learning.md`— RL e tomada de decisão
5.`ethics_and_safety/ai_safety_and_alignment.md`— Considerações de segurança