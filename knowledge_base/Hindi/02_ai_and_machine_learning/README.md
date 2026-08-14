# एआई और मशीन लर्निंग
मुख्य अवधारणाओं से लेकर उत्पादन परिनियोजन तक - कृत्रिम बुद्धिमत्ता के बुनियादी सिद्धांतों, मॉडल आर्किटेक्चर, एमएल इंजीनियरिंग, भाषा और दृष्टि प्रसंस्करण और एआई नैतिकता को कवर करने वाले संदर्भ दस्तावेजों का एक संरचित संग्रह।
## संरचना
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

## उपश्रेणी के अनुसार फ़ाइलें
### नींव
| फ़ाइल | विवरण |
|------|----||
| [artificial_intelligence.md](foundations/artificial_intelligence.md)| एआई सिंहावलोकन, एमएल, गहन शिक्षा, एलएलएम, नैतिकता |
| [ml_evaluation_and_workflow.md](foundations/ml_evaluation_and_workflow.md)| एमएल पाइपलाइन, मेट्रिक्स, सर्वोत्तम अभ्यास |
### मॉडल आर्किटेक्चर
| फ़ाइल | विवरण |
|------|----||
| [generative_ai_deep_dive.md](architectures/generative_ai_deep_dive.md)| जीएएन, वीएई, प्रसार मॉडल, एलएलएम, जेनरेटिव एआई अनुप्रयोग |
| [graph_neural_networks.md](architectures/graph_neural_networks.md)| जीसीएन, जीएटी, संदेश पासिंग, ज्ञान ग्राफ |
| [reinforcement_learning.md](architectures/reinforcement_learning.md)| एमडीपी, क्यू-लर्निंग, पॉलिसी ग्रेडिएंट्स, आरएलएचएफ, मल्टी-एजेंट सिस्टम |
| [recommendation_systems.md](architectures/recommendation_systems.md)| सहयोगात्मक फ़िल्टरिंग, सामग्री-आधारित, हाइब्रिड, मैट्रिक्स फ़ैक्टराइज़ेशन |
| [federated_learning_and_privacy.md](architectures/federated_learning_and_privacy.md)| विकेंद्रीकृत प्रशिक्षण, विभेदक गोपनीयता, सुरक्षित एकत्रीकरण |
### एमएल इंजीनियरिंग
| फ़ाइल | विवरण |
|------|----||
| [model_optimization_and_deployment.md](engineering/model_optimization_and_deployment.md)| परिमाणीकरण, छंटाई, आसवन, ओएनएनएक्स, परोसना |
| [ml_engineering_and_mlops.md](engineering/ml_engineering_and_mlops.md)| मॉडल सेवा, रजिस्ट्रियां, परिनियोजन रणनीतियाँ, बहाव निगरानी |
| [data_engineering_and_pipelines.md](engineering/data_engineering_and_pipelines.md)| ईटीएल/ईएलटी, डेटा लेक, ऑर्केस्ट्रेशन, काफ्का, फीचर स्टोर |
| [local_ai_architecture.md](engineering/local_ai_architecture.md)| स्थानीय एआई परिनियोजन आर्किटेक्चर |
| [phi3_and_local_models.md](engineering/phi3_and_local_models.md)| स्थानीय स्तर पर चल रहे मॉडल |
### एनएलपी और भाषण
| फ़ाइल | विवरण |
|------|----||
| [nlp_fundamentals.md](nlp_and_speech/nlp_fundamentals.md)| टेक्स्ट प्रोसेसिंग, एम्बेडिंग, ट्रांसफॉर्मर, बीईआरटी, जीपीटी |
| [speech_and_audio_processing.md](nlp_and_speech/speech_and_audio_processing.md)| एएसआर, टीटीएस, ऑडियो फीचर्स, व्हिस्पर |
| [time_series_and_forecasting.md](nlp_and_speech/time_series_and_forecasting.md)| ARIMA, पैगंबर, LSTM, मौसमी, विसंगति का पता लगाना |
| [computer_vision_fundamentals.md](nlp_and_speech/computer_vision_fundamentals.md)| सीएनएन, ऑब्जेक्ट डिटेक्शन, सेगमेंटेशन, ट्रांसफर लर्निंग |
| [multimodal_ai.md](nlp_and_speech/multimodal_ai.md)| विज़न-भाषा मॉडल, CLIP, DALL-E, क्रॉस-मोडल लर्निंग |
### नैतिकता और सुरक्षा
| फ़ाइल | विवरण |
|------|----||
| [ai_ethics_and_governance.md](ethics_and_safety/ai_ethics_and_governance.md)| एआई पूर्वाग्रह, निष्पक्षता, जवाबदेही, विनियमन, शासन |
| [ai_safety_and_alignment.md](ethics_and_safety/ai_safety_and_alignment.md)| संरेखण समस्या, आरएलएचएफ, व्याख्यात्मकता, एआई सुरक्षा अनुसंधान |
## सुझाए गए पढ़ने के रास्ते
### **एआई शुरुआती पथ**
1.`foundations/artificial_intelligence.md`- AI क्या है?
2.`foundations/ml_evaluation_and_workflow.md`- एमएल शुरू से आखिर तक कैसे काम करता है
3.`nlp_and_speech/nlp_fundamentals.md`- पाठ और भाषा प्रसंस्करण
4.`nlp_and_speech/computer_vision_fundamentals.md`- छवि और दृष्टि प्रसंस्करण
### **एमएल इंजीनियर पथ**
1.`foundations/ml_evaluation_and_workflow.md`- एमएल पाइपलाइन
2.`engineering/data_engineering_and_pipelines.md`- डेटा इंफ्रास्ट्रक्चर
3.`engineering/model_optimization_and_deployment.md`- मॉडल अनुकूलन
4.`engineering/ml_engineering_and_mlops.md`- एमएलओप्स और सर्विंग
5.`engineering/local_ai_architecture.md`- परिनियोजन आर्किटेक्चर
### **अनुसंधान पथ**
1.`foundations/artificial_intelligence.md`- मूल अवधारणाएँ
2.`architectures/generative_ai_deep_dive.md`- जनरेटिव मॉडल
3.`architectures/graph_neural_networks.md`- ग्राफ़-आधारित मॉडल
4.`architectures/reinforcement_learning.md`- आरएल और निर्णय लेना
5.`ethics_and_safety/ai_safety_and_alignment.md`- सुरक्षा संबंधी विचार