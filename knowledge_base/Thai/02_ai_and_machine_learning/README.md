# AI และการเรียนรู้ของเครื่อง
คอลเลกชันเอกสารอ้างอิงที่มีโครงสร้างครอบคลุมพื้นฐานปัญญาประดิษฐ์ สถาปัตยกรรมแบบจำลอง วิศวกรรม ML การประมวลผลภาษาและการมองเห็น และจริยธรรมของ AI ตั้งแต่แนวคิดหลักไปจนถึงการใช้งานจริง
## โครงสร้าง
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

## ไฟล์ตามหมวดหมู่ย่อย
### มูลนิธิ
| ไฟล์ | คำอธิบาย |
|-|-------------|
| [artificial_intelligence.md](foundations/artificial_intelligence.md)| ภาพรวม AI, ML, การเรียนรู้เชิงลึก, LLM, จริยธรรม |
| [ml_evaluation_and_workflow.md](foundations/ml_evaluation_and_workflow.md)| ไปป์ไลน์ ML, ตัวชี้วัด, แนวทางปฏิบัติที่ดีที่สุด |
### สถาปัตยกรรมแบบจำลอง
| ไฟล์ | คำอธิบาย |
|-|-------------|
| [generative_ai_deep_dive.md](architectures/generative_ai_deep_dive.md)| GAN, VAE, โมเดลการแพร่กระจาย, LLM, แอปพลิเคชัน AI เชิงสร้างสรรค์ |
| [graph_neural_networks.md](architectures/graph_neural_networks.md)| GCN, GAT, การส่งข้อความ, กราฟความรู้ |
| [reinforcement_learning.md](architectures/reinforcement_learning.md)| MDP, การเรียนรู้แบบ Q, การไล่ระดับนโยบาย, RLHF, ระบบหลายตัวแทน |
| [recommendation_systems.md](architectures/recommendation_systems.md)| การกรองการทำงานร่วมกัน ตามเนื้อหา ไฮบริด การแยกตัวประกอบเมทริกซ์ |
| [federated_learning_and_privacy.md](architectures/federated_learning_and_privacy.md)| การฝึกอบรมแบบกระจายอำนาจ ความเป็นส่วนตัวที่แตกต่าง การรวมกลุ่มที่ปลอดภัย |
### ม.ล.วิศวะ
| ไฟล์ | คำอธิบาย |
|-|-------------|
| [model_optimization_and_deployment.md](engineering/model_optimization_and_deployment.md)| การหาปริมาณ การตัดแต่งกิ่ง การกลั่น ONNX การให้บริการ |
| [ml_engineering_and_mlops.md](engineering/ml_engineering_and_mlops.md)| การให้บริการโมเดล การลงทะเบียน กลยุทธ์การปรับใช้ การตรวจสอบดริฟท์ |
| [data_engineering_and_pipelines.md](engineering/data_engineering_and_pipelines.md)| ETL/ELT, Data Lake, การเรียบเรียง, Kafka, ร้านค้าฟีเจอร์ |
| [local_ai_architecture.md](engineering/local_ai_architecture.md)| สถาปัตยกรรมการปรับใช้ AI ในพื้นที่ |
| [phi3_and_local_models.md](engineering/phi3_and_local_models.md)| ใช้งานโมเดลในเครื่อง |
### NLP และคำพูด
| ไฟล์ | คำอธิบาย |
|-|-------------|
| [nlp_fundamentals.md](nlp_and_speech/nlp_fundamentals.md)| การประมวลผลข้อความ, การฝัง, Transformers, BERT, GPT |
| [speech_and_audio_processing.md](nlp_and_speech/speech_and_audio_processing.md)| ASR, TTS, คุณสมบัติด้านเสียง, Whisper |
| [time_series_and_forecasting.md](nlp_and_speech/time_series_and_forecasting.md)| ARIMA, ศาสดา, LSTM, ฤดูกาล, การตรวจจับความผิดปกติ |
| [computer_vision_fundamentals.md](nlp_and_speech/computer_vision_fundamentals.md)| CNN, การตรวจจับวัตถุ, การแบ่งส่วน, การถ่ายโอนการเรียนรู้ |
| [multimodal_ai.md](nlp_and_speech/multimodal_ai.md)| แบบจำลองภาษาวิสัยทัศน์, CLIP, DALL-E, การเรียนรู้แบบข้ามกิริยา |
### จริยธรรมและความปลอดภัย
| ไฟล์ | คำอธิบาย |
|-|-------------|
| [ai_ethics_and_governance.md](ethics_and_safety/ai_ethics_and_governance.md)| อคติ AI, ความเป็นธรรม, ความรับผิดชอบ, กฎระเบียบ, การกำกับดูแล |
| [ai_safety_and_alignment.md](ethics_and_safety/ai_safety_and_alignment.md)| ปัญหาการจัดตำแหน่ง RLHF การตีความได้ การวิจัยด้านความปลอดภัยของ AI |
## เส้นทางการอ่านที่แนะนำ
### **เส้นทางเริ่มต้น AI**
1.`foundations/artificial_intelligence.md`— AI คืออะไร
2.`foundations/ml_evaluation_and_workflow.md`— วิธีการทำงานของ ML แบบครบวงจร
3.`nlp_and_speech/nlp_fundamentals.md`— การประมวลผลข้อความและภาษา
4.`nlp_and_speech/computer_vision_fundamentals.md`— การประมวลผลภาพและการมองเห็น
### **เส้นทางวิศวกร ML**
1.`foundations/ml_evaluation_and_workflow.md`— ไปป์ไลน์ ML
2.`engineering/data_engineering_and_pipelines.md`— โครงสร้างพื้นฐานข้อมูล
3.`engineering/model_optimization_and_deployment.md`— การเพิ่มประสิทธิภาพโมเดล
4.`engineering/ml_engineering_and_mlops.md`— MLOps และการให้บริการ
5.`engineering/local_ai_architecture.md`— สถาปัตยกรรมการปรับใช้
### **เส้นทางการวิจัย**
1.`foundations/artificial_intelligence.md`— แนวคิดหลัก
2.`architectures/generative_ai_deep_dive.md`— โมเดลเจนเนอเรทีฟ
3.`architectures/graph_neural_networks.md`— โมเดลตามกราฟ
4.`architectures/reinforcement_learning.md`— RL และการตัดสินใจ
5.`ethics_and_safety/ai_safety_and_alignment.md`— ข้อควรพิจารณาด้านความปลอดภัย