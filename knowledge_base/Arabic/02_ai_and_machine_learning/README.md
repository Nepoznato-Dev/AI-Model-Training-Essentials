# الذكاء الاصطناعي والتعلم الآلي
مجموعة منظمة من المستندات المرجعية التي تغطي أساسيات الذكاء الاصطناعي، وبنيات النماذج، وهندسة التعلم الآلي، ومعالجة اللغة والرؤية، وأخلاقيات الذكاء الاصطناعي - بدءًا من المفاهيم الأساسية وحتى نشر الإنتاج.
## بناء
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

## الملفات حسب الفئة الفرعية
### أسس
| ملف | الوصف |
|------|------------|
| [artificial_intelligence.md](foundations/artificial_intelligence.md)| نظرة عامة على الذكاء الاصطناعي، التعلم الآلي، التعلم العميق، ماجستير إدارة الأعمال، الأخلاقيات |
| [ml_evaluation_and_workflow.md](foundations/ml_evaluation_and_workflow.md)| مسارات ML والمقاييس وأفضل الممارسات |
### البنى النموذجية
| ملف | الوصف |
|------|------------|
| [generative_ai_deep_dive.md](architectures/generative_ai_deep_dive.md)| شبكات GAN، VAEs، نماذج الانتشار، ماجستير إدارة الأعمال، تطبيقات الذكاء الاصطناعي التوليدية |
| [graph_neural_networks.md](architectures/graph_neural_networks.md)| شبكات GCN، GATs، تمرير الرسائل، الرسوم البيانية المعرفية |
| [reinforcement_learning.md](architectures/reinforcement_learning.md)| MDPs، Q-learning، تدرجات السياسة، RLHF، أنظمة متعددة الوكلاء |
| [recommendation_systems.md](architectures/recommendation_systems.md)| التصفية التعاونية، القائمة على المحتوى، الهجين، تحليل المصفوفة |
| [federated_learning_and_privacy.md](architectures/federated_learning_and_privacy.md)| تدريب لامركزي، خصوصية تفاضلية، تجميع آمن |
### هندسة تعلم الآلة
| ملف | الوصف |
|------|------------|
| [model_optimization_and_deployment.md](engineering/model_optimization_and_deployment.md)| التكميم، التقليم، التقطير، ONNX، التقديم |
| [ml_engineering_and_mlops.md](engineering/ml_engineering_and_mlops.md)| تقديم النماذج، والسجلات، واستراتيجيات النشر، ومراقبة الانجراف |
| [data_engineering_and_pipelines.md](engineering/data_engineering_and_pipelines.md)| ETL/ELT، بحيرات البيانات، التنسيق، كافكا، المتاجر المميزة |
| [local_ai_architecture.md](engineering/local_ai_architecture.md)| بنيات نشر الذكاء الاصطناعي المحلية |
| [phi3_and_local_models.md](engineering/phi3_and_local_models.md)| تشغيل النماذج محليا |
### البرمجة اللغوية العصبية والكلام
| ملف | الوصف |
|------|------------|
| [nlp_fundamentals.md](nlp_and_speech/nlp_fundamentals.md)| معالجة النصوص، التضمينات، المحولات، بيرت، جي بي تي |
| [speech_and_audio_processing.md](nlp_and_speech/speech_and_audio_processing.md)| ASR، تحويل النص إلى كلام، ميزات الصوت، الهمس |
| [time_series_and_forecasting.md](nlp_and_speech/time_series_and_forecasting.md)| أريما، النبي، LSTMs، الموسمية، كشف الشذوذ |
| [computer_vision_fundamentals.md](nlp_and_speech/computer_vision_fundamentals.md)| CNNs، كشف الأشياء، التجزئة، نقل التعلم |
| [multimodal_ai.md](nlp_and_speech/multimodal_ai.md)| نماذج الرؤية واللغة، CLIP، DALL-E، التعلم متعدد الوسائط |
### الأخلاق والسلامة
| ملف | الوصف |
|------|------------|
| [ai_ethics_and_governance.md](ethics_and_safety/ai_ethics_and_governance.md)| تحيز الذكاء الاصطناعي، والعدالة، والمساءلة، والتنظيم، والحوكمة |
| [ai_safety_and_alignment.md](ethics_and_safety/ai_safety_and_alignment.md)| مشكلة المحاذاة، RLHF، قابلية التفسير، أبحاث سلامة الذكاء الاصطناعي |
## مسارات القراءة المقترحة
### **مسار الذكاء الاصطناعي للمبتدئين**
1.`foundations/artificial_intelligence.md`– ما هو الذكاء الاصطناعي؟
2.`foundations/ml_evaluation_and_workflow.md`— كيف يعمل تعلم الآلة بشكل شامل
3.`nlp_and_speech/nlp_fundamentals.md` — معالجة النصوص واللغة
4.`nlp_and_speech/computer_vision_fundamentals.md` — معالجة الصور والرؤية
### **مسار مهندس تعلم الآلة**
1.`foundations/ml_evaluation_and_workflow.md`— خطوط أنابيب ML
2.`engineering/data_engineering_and_pipelines.md` — البنية التحتية للبيانات
3.`engineering/model_optimization_and_deployment.md` — تحسين النموذج
4.`engineering/ml_engineering_and_mlops.md` — MLOps والتقديم
5.`engineering/local_ai_architecture.md` — بنيات النشر
### **مسار البحث**
1.`foundations/artificial_intelligence.md` — المفاهيم الأساسية
2.`architectures/generative_ai_deep_dive.md` — النماذج التوليدية
3.`architectures/graph_neural_networks.md` — النماذج القائمة على الرسم البياني
4.`architectures/reinforcement_learning.md` — RL وصنع القرار
5.`ethics_and_safety/ai_safety_and_alignment.md` – اعتبارات السلامة