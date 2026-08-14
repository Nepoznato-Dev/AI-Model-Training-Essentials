# هوش مصنوعی و یادگیری ماشین
مجموعه ای ساختاریافته از اسناد مرجع که مبانی هوش مصنوعی، معماری مدل، مهندسی ML، پردازش زبان و بینش، و اخلاق هوش مصنوعی را پوشش می دهد - از مفاهیم اصلی تا استقرار تولید.
## ساختار
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

## فایل ها بر اساس زیر شاخه
### پایه ها
| فایل | توضیحات |
|------|-------------|
| [artificial_intelligence.md](foundations/artificial_intelligence.md)| مروری بر هوش مصنوعی، ML، یادگیری عمیق، LLM، اخلاق |
| [ml_evaluation_and_workflow.md](foundations/ml_evaluation_and_workflow.md)| خطوط لوله ML، معیارها، بهترین شیوه ها |
### معماری مدل
| فایل | توضیحات |
|------|-------------|
| [generative_ai_deep_dive.md](architectures/generative_ai_deep_dive.md)| GANs، VAEs، مدل‌های انتشار، LLMs، برنامه‌های کاربردی هوش مصنوعی مولد |
| [graph_neural_networks.md](architectures/graph_neural_networks.md)| GCN ها، GAT ها، ارسال پیام، نمودارهای دانش |
| [reinforcement_learning.md](architectures/reinforcement_learning.md)| MDP ها، یادگیری Q، شیب سیاست، RLHF، سیستم های چند عاملی |
| [recommendation_systems.md](architectures/recommendation_systems.md)| فیلتر مشارکتی، مبتنی بر محتوا، ترکیبی، فاکتورسازی ماتریسی |
| [federated_learning_and_privacy.md](architectures/federated_learning_and_privacy.md)| آموزش غیرمتمرکز، حریم خصوصی دیفرانسیل، تجمیع امن |
### مهندسی ML
| فایل | توضیحات |
|------|-------------|
| [model_optimization_and_deployment.md](engineering/model_optimization_and_deployment.md)| کوانتیزاسیون، هرس، تقطیر، ONNX، سرو |
| [ml_engineering_and_mlops.md](engineering/ml_engineering_and_mlops.md)| خدمات مدل، رجیستری، استراتژی های استقرار، نظارت دریفت |
| [data_engineering_and_pipelines.md](engineering/data_engineering_and_pipelines.md)| ETL/ELT، دریاچه های داده، ارکستراسیون، کافکا، فروشگاه های ویژه |
| [local_ai_architecture.md](engineering/local_ai_architecture.md)| معماری های استقرار هوش مصنوعی محلی |
| [phi3_and_local_models.md](engineering/phi3_and_local_models.md)| مدل های در حال اجرا به صورت محلی |
### NLP و گفتار
| فایل | توضیحات |
|------|-------------|
| [nlp_fundamentals.md](nlp_and_speech/nlp_fundamentals.md)| پردازش متن، جاسازی، ترانسفورماتور، BERT، GPT |
| [speech_and_audio_processing.md](nlp_and_speech/speech_and_audio_processing.md)| ASR، TTS، ویژگی های صوتی، Whisper |
| [time_series_and_forecasting.md](nlp_and_speech/time_series_and_forecasting.md)| ARIMA، پیامبر، LSTMs، فصلی، تشخیص ناهنجاری |
| [computer_vision_fundamentals.md](nlp_and_speech/computer_vision_fundamentals.md)| CNN ها، تشخیص اشیا، تقسیم بندی، یادگیری انتقال |
| [multimodal_ai.md](nlp_and_speech/multimodal_ai.md)| مدل های زبان بینایی، CLIP، DALL-E، یادگیری متقابل |
### اخلاق و ایمنی
| فایل | توضیحات |
|------|-------------|
| [ai_ethics_and_governance.md](ethics_and_safety/ai_ethics_and_governance.md)| تعصب هوش مصنوعی، انصاف، پاسخگویی، مقررات، حاکمیت |
| [ai_safety_and_alignment.md](ethics_and_safety/ai_safety_and_alignment.md)| مشکل تراز، RLHF، تفسیرپذیری، تحقیقات ایمنی هوش مصنوعی |
## مسیرهای خواندن پیشنهادی
### **مسیر مبتدی هوش مصنوعی**
1.`foundations/artificial_intelligence.md`- هوش مصنوعی چیست؟
2.`foundations/ml_evaluation_and_workflow.md`- چگونه ML سرتاسر کار می کند
3.`nlp_and_speech/nlp_fundamentals.md`- پردازش متن و زبان
4.`nlp_and_speech/computer_vision_fundamentals.md`- پردازش تصویر و بینایی
### **مسیر مهندس ML**
1.`foundations/ml_evaluation_and_workflow.md`- خطوط لوله ML
2.`engineering/data_engineering_and_pipelines.md`- زیرساخت داده
3.`engineering/model_optimization_and_deployment.md`- بهینه سازی مدل
4.`engineering/ml_engineering_and_mlops.md`- MLO و سرویس
5.`engineering/local_ai_architecture.md`- معماری های استقرار
### **مسیر تحقیق**
1.`foundations/artificial_intelligence.md`- مفاهیم اصلی
2.`architectures/generative_ai_deep_dive.md`- مدل های مولد
3.`architectures/graph_neural_networks.md`- مدل های مبتنی بر نمودار
4.`architectures/reinforcement_learning.md`- RL و تصمیم گیری
5.`ethics_and_safety/ai_safety_and_alignment.md`- ملاحظات ایمنی