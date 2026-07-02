# तकनीकी शब्दावली

आधुनिक AI और computing परिदृश्य में AI मॉडलों, हार्डवेयर, बेंचमार्क और मुख्य अवधारणाओं को समेटने वाली एक संदर्भ शब्दावली।

---

## AI भाषा मॉडल और सहायक

### ChatGPT
ChatGPT OpenAI द्वारा विकसित एक AI chatbot है, जिसे पहली बार नवंबर 2022 में जारी किया गया था।
यह GPT बड़े भाषा मॉडलों (LLMs) की श्रृंखला द्वारा संचालित है। ChatGPT इतिहास के सबसे तेज़ी से बढ़ने वाले उपभोक्ता AI उत्पादों में से एक है, जिसने लॉन्च के दो महीनों के भीतर 100 million users तक पहुँच बनाई। यह पाठ-आधारित बातचीत, code generation, summarisation और रचनात्मक लेखन का समर्थन करता है। सशुल्क स्तर अधिक शक्तिशाली models जैसे GPT-4 और GPT-4o तक पहुँच प्रदान करते हैं।

### GPT (Generative Pre-trained Transformer)
GPT OpenAI द्वारा बनाए गए बड़े भाषा मॉडलों का एक परिवार है। यह architecture एक decoder-only Transformer का उपयोग करता है, जिसे विशाल text corpora पर next-token prediction objective के साथ train किया गया है। मुख्य versions में GPT-2 (2019, 1.5B parameters, "too dangerous to release" प्रचार के लिए उल्लेखनीय), GPT-3 (2020, 175B parameters, API के माध्यम से व्यापक रूप से उपयोग किया गया), GPT-3.5 (मूल ChatGPT की backbone), और GPT-4 (2023, multimodal, कई benchmarks पर मानव विशेषज्ञ स्तर के क़रीब प्रदर्शन) शामिल हैं।

### Claude
Claude Anthropic द्वारा विकसित एक AI assistant है। इसका नाम information theory के संस्थापक Claude Shannon के नाम पर रखा गया है। Anthropic की स्थापना पूर्व OpenAI researchers ने की थी और यह "constitutional AI" पर केंद्रित है — यह एक तकनीक है जो models को सिद्धांतों के एक सेट का पालन करने के लिए train करके उन्हें अधिक सुरक्षित बनाती है। Claude models (Claude 1, 2, 3 Haiku / Sonnet / Opus) अपने long context windows (200,000 tokens तक), सूक्ष्म reasoning और baseline LLMs की तुलना में कम हानिकारक output के लिए जाने जाते हैं।

### Gemini
Gemini Google DeepMind के multimodal AI models का परिवार है, जिसकी घोषणा दिसंबर 2023 में की गई थी। Gemini मूल रूप से multimodal है — इसे शुरू से ही text, images, audio और video पर एक साथ train किया गया, जबकि पहले के models में modalities को fine-tuning के माध्यम से जोड़ा गया था। Versions में Gemini Nano (on-device), Gemini Flash (तेज़, cost-efficient) और Gemini Ultra (सबसे उच्च क्षमता वाला) शामिल हैं। Gemini, Google के AI chatbot Bard (जिसका नाम बदलकर Gemini किया गया) और Google Search AI Overviews को शक्ति देता है।

### Phi-3-mini
Phi-3-mini Microsoft द्वारा विकसित 3.8B parameters वाला एक छोटा भाषा मॉडल (SLM) है। इसे अप्रैल 2024 में जारी किया गया था। अधिकांश बड़े models के विपरीत, Phi-3-mini को सावधानीपूर्वक चुने गए "textbook-quality" dataset पर train किया गया — यह तकनीक Microsoft Research द्वारा आगे बढ़ाई गई थी — जो कच्ची मात्रा की तुलना में data quality को प्राथमिकता देती है। GPT-4 या Claude 3 Opus से बहुत छोटा होने के बावजूद, Phi-3-mini MMLU और HumanEval जैसे reasoning benchmarks पर अपने से कई गुना बड़े models के बराबर या उनसे बेहतर प्रदर्शन करता है। इसका base variant 4k token context window का समर्थन करता है और long-context variant 128k window का समर्थन करता है। पर्याप्त RAM होने पर Phi-3-mini एक single consumer GPU पर या यहाँ तक कि आधुनिक smartphone पर on-device भी चल सकता है।

### Llama (Meta AI)
Llama (Large Language Model Meta AI) Meta द्वारा जारी models का एक open-weights परिवार है। Llama 2 (2023) research और commercial use के लिए 7B से 70B parameters तक के आकारों में जारी किया गया था। Llama 3 (2024) ने प्रदर्शन में उल्लेखनीय सुधार किया, जिसमें models 8B से 70B (और बाद में 400B+) तक रहे। क्योंकि weights सार्वजनिक रूप से download किए जा सकते हैं, Llama models fine-tuned variants (Mistral, Alpaca, Vicuna, आदि) के बड़े ecosystem की नींव हैं और local/private AI deployments के लिए व्यापक रूप से उपयोग किए जाते हैं।

### Mistral
Mistral AI एक French AI company है जो open और proprietary LLMs विकसित करती है। Mistral 7B (2023) ने दिखाया कि 7B-parameter model sliding window attention और grouped-query attention जैसी कुशल तकनीकों का उपयोग करके कहीं बड़े models के प्रदर्शन की बराबरी कर सकता है। Mixtral 8x7B (2024) एक mixture-of-experts model है — यह प्रत्येक token को 8 expert networks के एक subset तक route करता है, जिससे computationally cheaper रहते हुए GPT-3.5-स्तरीय प्रदर्शन प्राप्त होता है। Mistral के models पूरी तरह open-weight हैं और locally चलाए जा सकते हैं।

---

## GPU हार्डवेयर और ग्राफ़िक्स कार्ड

### GPU (Graphics Processing Unit)
GPU एक processor है जिसे अत्यधिक parallel computation के लिए डिज़ाइन किया गया है। मूल रूप से 3D graphics render करने के लिए बनाए गए GPUs, अब AI/ML training और inference के लिए आवश्यक हो गए हैं क्योंकि वे हज़ारों छोटे cores का उपयोग करके एक साथ हज़ारों floating-point operations कर सकते हैं। AI के लिए दो मुख्य GPU निर्माता NVIDIA और AMD हैं।

### NVIDIA GeForce RTX Series
RTX (Ray Tracing Texel eXtreme) series NVIDIA की उपभोक्ता GPU श्रृंखला है। RTX 30xx (Ampere, 2020) और RTX 40xx (Ada Lovelace, 2022) generations में AI operations को तेज़ करने के लिए dedicated Tensor Cores शामिल हैं। VRAM (video RAM) स्थानीय रूप से AI models चलाने के लिए महत्वपूर्ण है — 8GB GPU 4-bit quantisation में 7B parameter models संभाल सकता है; 24GB GPU 4-bit में 70B models संभाल सकता है।

### NVIDIA A-Series and H-Series (Data Centre)
A100 (Ampere, 2020) और H100 (Hopper, 2022) NVIDIA के व्यावसायिक AI accelerators हैं। H100 में 80GB तक HBM3 memory होती है और यह आज अधिकांश large-scale LLM training के पीछे मानक hardware है। ये GPUs प्रति इकाई $25,000–$40,000 तक के होते हैं, लेकिन consumer RTX cards की तुलना में 10–30× AI throughput प्रदान करते हैं।

### AMD Radeon RX Series
AMD की उपभोक्ता GPU श्रृंखला। RX 7900 XTX (2022) में 24GB VRAM है और यह ROCm (AMD का GPU compute stack) के माध्यम से local LLMs चला सकता है। AI frameworks के लिए AMD GPUs को सामान्यतः NVIDIA की तुलना में कम समर्थन मिलता है, हालाँकि समर्थन बेहतर हो रहा है।

### Intel Arc
Intel Arc, Intel की discrete GPU product line है, जिसे 2022 से जारी किया गया। Arc GPUs XeSS (Intel का super-sampling) का समर्थन करते हैं और OpenVINO तथा IPEX-LLM frameworks के माध्यम से AI inference tasks के लिए सीमित लेकिन बढ़ता हुआ समर्थन रखते हैं।

### ARK Intel (ark.intel.com)
ARK, ark.intel.com पर Intel का आधिकारिक product specifications database है। यह हर Intel CPU, GPU, FPGA, और NUC product के लिए विस्तृत तकनीकी विनिर्देश प्रदान करता है, जिनमें core counts, clock speeds, TDP, supported memory types, और instruction-set features शामिल हैं। जब आप सुनते हैं "check ARK for specs," तो उसका अर्थ authoritative hardware information के लिए उस database पर जाना होता है।

---

## AI प्रदर्शन बेंचमार्क

### MMLU (Massive Multitask Language Understanding)
MMLU एक benchmark है जो mathematics, history, law, medicine, और computer science सहित 57 academic subjects में LLM knowledge का परीक्षण करता है। इसमें वास्तविक university-level exams से लिए गए बहुविकल्पीय प्रश्न होते हैं। 70% score लगभग human undergraduate level के बराबर माना जाता है; GPT-4 और Claude 3 86% से ऊपर score करते हैं। Phi-3-mini अपने छोटे आकार के बावजूद लगभग 70% score करता है।

### HumanEval
HumanEval code generation के लिए OpenAI का benchmark है। इसमें automated test cases के साथ 164 Python programming problems शामिल हैं। Models को pass@k पर मापा जाता है — यह वह संभावना है कि k generated solutions में से कम से कम एक सभी tests पास कर दे। GPT-4 लगभग 87% (pass@1) score करता है; एक अच्छी तरह tuned 7B model लगभग 50–60% तक पहुँच सकता है।

### HellaSwag
HellaSwag एक सामान्य-बोध तर्क बेंचमार्क है। Models को किसी साधारण गतिविधि का वर्णन करने वाला एक वाक्य दिया जाता है और उन्हें चार विकल्पों में से सबसे संभावित continuation चुननी होती है। गलत विकल्पों को विशेष रूप से इस तरह बनाया जाता है कि वे plausible लगें लेकिन सूक्ष्म रूप से गलत हों। यह जाँचता है कि model को physical और social situations की grounded understanding है या नहीं।

### ARC (AI2 Reasoning Challenge)
ARC Allen Institute for AI का benchmark है। इसमें grade-school science questions होते हैं, जिन्हें "Easy" और "Challenge" sets में बाँटा गया है। Challenge set में ऐसे प्रश्न होते हैं जिनसे retrieval-based methods और simple statistical models संघर्ष करते हैं, इसलिए उनमें multi-step reasoning की आवश्यकता होती है।

---

## AI/ML की मुख्य अवधारणाएँ

### RAG (Retrieval-Augmented Generation)
RAG एक तकनीक है जो retrieval system (आमतौर पर एक vector database) को language model के साथ जोड़ती है। केवल model के parametric knowledge पर निर्भर रहने के बजाय, RAG पहले external knowledge base से संबंधित documents प्राप्त करता है और फिर उन्हें model के context में शामिल करता है। इससे model up-to-date या domain-specific information के बारे में बिना retraining के प्रश्नों का उत्तर दे सकता है। Potato.ai RAG का एक रूप उपयोग करता है — यह अपने KB से data प्राप्त करता है और response generate करने से पहले परिणामों को context में शामिल करता है।

### Fine-tuning
Fine-tuning वह प्रक्रिया है जिसमें किसी pre-trained model को छोटे, domain-specific dataset पर आगे train किया जाता है। इससे model के weights किसी विशेष task या domain के लिए अनुकूलित हो जाते हैं। उदाहरण के लिए, एक base LLM को medical records पर fine-tune करके medical Q&A assistant बनाया जा सकता है। Fine-tuning computationally expensive है, लेकिन scratch से training करने की तुलना में बहुत सस्ती है।

### Quantisation
Quantisation model weights की numerical precision को घटा देता है (उदाहरण के लिए, 32-bit float से 4-bit integer तक)। इससे memory footprint नाटकीय रूप से कम हो जाता है — 16-bit precision में 7B model को लगभग 14GB VRAM चाहिए; वही model 4-bit (GGUF format) में लगभग 4GB लेता है। Quantisation आमतौर पर accuracy में छोटा लेकिन स्वीकार्य ह्रास लाता है और यही मुख्य तकनीक है जो बड़े models को consumer hardware या यहाँ तक कि mobile devices पर चलाने में सक्षम बनाती है।

### Context Window
Context window वह अधिकतम tokens संख्या है जिसे कोई model एक बार में process कर सकता है, जिसमें prompt और generated response दोनों शामिल होते हैं। GPT-3.5 में 4,096-token window थी; GPT-4 Turbo और Claude 3 128,000 tokens का समर्थन करते हैं; Gemini 1.5 Pro 1,000,000 tokens का समर्थन करता है। बड़ी context window model को एक बार में बातचीत या document का अधिक हिस्सा "देखने" देती है, जिससे लंबे exchanges में coherence बेहतर होती है।

### RLHF (Reinforcement Learning from Human Feedback)
RLHF वह training technique है जो base language model (जो केवल अगला token predict करता है) को ऐसे assistant में बदलती है जो instructions का पालन करता है और उपयोगी व्यवहार करता है। Human raters model outputs को score करते हैं, उनकी preferences पर reward model train किया जाता है, और फिर language model को reinforcement learning का उपयोग करके उसी reward model के विरुद्ध optimise किया जाता है। ChatGPT, Claude और Gemini सभी RLHF या समान alignment techniques (उदाहरण के लिए, Constitutional AI, Direct Preference Optimisation) के variants का उपयोग करते हैं।

### Transformer Architecture
Transformer वह neural network architecture है जो सभी modern LLMs की आधारशिला है। Vaswani et al. द्वारा 2017 के paper "Attention Is All You Need" में प्रस्तुत यह architecture self-attention mechanisms का उपयोग करती है ताकि tokens को sequentially के बजाय parallel में process किया जा सके। Encoder-only Transformers (BERT) understanding tasks के लिए उपयोग किए जाते हैं; decoder-only Transformers (GPT, Llama, Mistral) generation tasks के लिए उपयोग किए जाते हैं; encoder-decoder Transformers (T5, BART) translation और summarisation के लिए उपयोग किए जाते हैं।

### Embeddings और Vector Databases
Embeddings text (या images) के dense numerical representations होते हैं जिन्हें neural network द्वारा बनाया जाता है। अर्थ की दृष्टि से समान texts के embeddings vector space में एक-दूसरे के क़रीब होते हैं। Vector databases (ChromaDB, Pinecone, Weaviate, Qdrant) इन embeddings को store करते हैं और तेज़ approximate nearest-neighbour search का समर्थन करते हैं। यही RAG systems की storage backbone हैं, जिनमें Potato.ai की cold-memory layer भी शामिल है।
