# कृत्रिम बुद्धिमत्ता

## कृत्रिम बुद्धिमत्ता क्या है?

कृत्रिम बुद्धिमत्ता (AI) उन मशीनों में मानव बुद्धि के अनुकरण को संदर्भित करती है जिन्हें सोचने, सीखने और समस्याएँ हल करने के लिए प्रोग्राम किया गया है। AI प्रणालियाँ ऐसे कार्य कर सकती हैं जिनके लिए सामान्यतः मानव बुद्धि की आवश्यकता होती है, जैसे वाणी की पहचान करना, निर्णय लेना, भाषाओं का अनुवाद करना और चित्रों में वस्तुओं की पहचान करना। इस शब्द को John McCarthy ने 1956 में Dartmouth Conference में गढ़ा था, जिसे व्यापक रूप से AI क्षेत्र की स्थापना की घटना माना जाता है।

आधुनिक AI को व्यापक रूप से Narrow AI (जिसे Weak AI भी कहा जाता है) में विभाजित किया जाता है, जो विशिष्ट कार्यों के लिए बनाया जाता है, और सैद्धांतिक Artificial General Intelligence (AGI) में, जो सभी क्षेत्रों में मानव संज्ञानात्मक क्षमता के बराबर या उससे अधिक होगी। वर्तमान के सभी AI सिस्टम Narrow AI हैं।

## AI का इतिहास

AI का इतिहास लगभग आठ दशकों तक फैला हुआ है। प्रारंभिक सैद्धांतिक आधार Alan Turing ने रखे, जिनके 1950 के शोधपत्र "Computing Machinery and Intelligence" ने Turing Test प्रस्तुत किया — यह इस बात का माप है कि कोई मशीन मानव से अप्रभेद्य बुद्धिमान व्यवहार प्रदर्शित कर सकती है या नहीं। 1956 की Dartmouth Conference ने औपचारिक रूप से AI को एक शैक्षणिक अनुशासन के रूप में स्थापित किया।

1950s–1970s में ELIZA (एक सरल chatbot) और LISP (AI के लिए बनाई गई एक programming language) जैसे आशावादी प्रारंभिक प्रोग्राम सामने आए। 1970s और 1980s के "AI winters" ऐसे दौर थे जब अपेक्षाएँ पूरी न होने के कारण फंडिंग और रुचि कम हो गई। 1980s में expert systems के साथ पुनरुत्थान हुआ — नियम-आधारित प्रोग्राम जो मानव विशेषज्ञता को एन्कोड करते थे। 2000s में internet और बढ़ते datasets से प्रेरित machine learning की उपलब्धियाँ आईं। 2010s में deep learning का उदय हुआ, जिसने computer vision, natural language processing (NLP) और reinforcement learning को रूपांतरित कर दिया।

## मशीन लर्निंग

मशीन लर्निंग (ML) AI का एक उपसमुच्चय है जो प्रणालियों को बिना स्पष्ट रूप से प्रोग्राम किए डेटा से सीखने में सक्षम बनाता है। ML की प्रमुख श्रेणियाँ शामिल हैं:

**Supervised Learning**: मॉडल को labelled input-output pairs पर प्रशिक्षित किया जाता है। उदाहरणों में spam detection और image classification शामिल हैं। Algorithms में linear regression, decision trees, support vector machines और neural networks शामिल हैं।

**Unsupervised Learning**: मॉडल unlabelled data में पैटर्न खोजता है। उदाहरणों में customer segmentation और anomaly detection शामिल हैं। Algorithms में k-means clustering और principal component analysis (PCA) शामिल हैं।

**Reinforcement Learning**: एक agent वातावरण के साथ अंतःक्रिया करके, rewards या penalties प्राप्त करते हुए सीखता है। इसका उपयोग game-playing AI (AlphaGo, AlphaZero), robotics और recommendation systems में होता है।

**Semi-Supervised and Self-Supervised Learning**: कम मात्रा के labelled data को बड़े unlabelled datasets के साथ मिलाता है। GPT models pre-training के दौरान self-supervised approach का उपयोग करते हैं।

## डीप लर्निंग

डीप लर्निंग machine learning का एक उपसमुच्चय है जो कई परतों वाले artificial neural networks (deep networks) का उपयोग करता है। मस्तिष्क की neural structure से ढीली प्रेरणा लेते हुए, ये networks डेटा के पदानुक्रमित representations सीखते हैं। Deep learning निम्न को शक्ति देती है:

- **Computer Vision**: image recognition, object detection, medical imaging
- **Natural Language Processing**: machine translation, sentiment analysis, question answering
- **Speech Recognition**: Siri, Alexa, Google Assistant जैसे voice assistants
- **Generative AI**: image generation (DALL-E, Stable Diffusion), text generation (GPT)

मुख्य deep learning architectures में images के लिए convolutional neural networks (CNNs), sequences के लिए recurrent neural networks (RNNs) और LSTMs, language के लिए transformers, और synthesis के लिए generative adversarial networks (GANs) शामिल हैं।

## बड़े भाषा मॉडल (LLMs)

बड़े भाषा मॉडल (LLMs) ऐसे AI सिस्टम हैं जिन्हें विशाल मात्रा के text data पर प्रशिक्षित किया जाता है ताकि वे मानव भाषा को समझ सकें और उत्पन्न कर सकें। ये Transformer architecture पर आधारित हैं, जिसे 2017 के शोधपत्र "Attention is All You Need" में Vaswani et al. ने प्रस्तुत किया था। LLMs किसी sequence में अगला token (word piece) अनुमानित करते हैं, जिससे वे सुसंगत text उत्पन्न कर सकते हैं, प्रश्नों के उत्तर दे सकते हैं, code लिख सकते हैं और reasoning कार्य कर सकते हैं।

उल्लेखनीय LLMs में शामिल हैं:
- **GPT series** (OpenAI): GPT-3, GPT-4 और उत्तरवर्ती मॉडल — chat और code के लिए व्यापक रूप से उपयोग किए जाते हैं
- **Claude** (Anthropic): सुरक्षा और उपयोगिता पर केंद्रित
- **Gemini** (Google DeepMind): multimodal, text, images और code को एकीकृत करता है
- **LLaMA / Llama 3** (Meta): शोध और local deployment के लिए open-weight models
- **Mistral** (Mistral AI): कुशल open models जो बहुत बड़े LLMs के साथ प्रतिस्पर्धी हैं

LLMs को दो चरणों में प्रशिक्षित किया जाता है: pre-training (बड़े text corpora पर unsupervised) और fine-tuning (supervised या reinforcement learning from human feedback, RLHF के माध्यम से)। Context windows यह बताते हैं कि कोई LLM एक बार में कितना text प्रोसेस कर सकता है, जो 4K tokens (early GPT-3) से लेकर सबसे उन्नत 2024 models में 1 million से अधिक tokens तक होता है।

## AI नैतिकता और सुरक्षा

AI महत्वपूर्ण नैतिक प्रश्न उठाता है जिनमें bias, privacy, job displacement और misuse का जोखिम शामिल है। Algorithmic bias तब होता है जब training data ऐतिहासिक असमानताओं को प्रतिबिंबित करता है, जिससे AI सिस्टम भेदभावपूर्ण outputs उत्पन्न करते हैं। Facial recognition systems ने गहरे रंग की त्वचा वाले व्यक्तियों के लिए अधिक error rates दिखाए हैं। Hiring algorithms के बारे में पाया गया है कि वे पुरुष उम्मीदवारों को प्राथमिकता दे सकते हैं।

AI safety वह क्षेत्र है जो यह सुनिश्चित करने के लिए समर्पित है कि AI सिस्टम इच्छित रूप से व्यवहार करें और अनपेक्षित हानि न पहुँचाएँ। प्रमुख चिंताएँ शामिल हैं:
- **Alignment**: यह सुनिश्चित करना कि AI के लक्ष्य मानव मूल्यों से मेल खाएँ
- **Interpretability / Explainability**: यह समझना कि AI ने कोई निर्णय क्यों लिया (विशेष रूप से medicine, law, finance में महत्वपूर्ण)
- **Misuse**: AI-निर्मित deepfakes, disinformation, cyberattacks
- **Existential risk**: सैद्धांतिक चिंता कि भविष्य का AGI ऐसे लक्ष्य अपना सकता है जो मानव अस्तित्व के साथ असंगत हों

AI safety पर काम करने वाले संगठनों में OpenAI की Safety team, Anthropic (जिसकी स्थापना पूर्व OpenAI safety researchers ने की), DeepMind की safety team, और MIRI तथा ARC जैसे स्वतंत्र संस्थान शामिल हैं।

## समाज में AI

AI लगभग हर उद्योग को बदल रहा है:

- **Healthcare**: AI medical images से cancer की पहचान में सहायता करता है, patient outcomes का पूर्वानुमान लगाता है, drug discovery को तेज करता है (AlphaFold ने protein folding structure prediction हल किया), और treatment plans को वैयक्तिकृत करता है।
- **Finance**: fraud detection, algorithmic trading, credit scoring और robo-advisors में ML models का उपयोग होता है।
- **Transportation**: self-driving vehicles computer vision, lidar और reinforcement learning का उपयोग करते हैं। Tesla Autopilot, Waymo और Cruise अग्रणी प्रयास हैं।
- **Education**: personalised learning platforms सामग्री को प्रत्येक छात्र की गति और सीखने की शैली के अनुसार अनुकूलित करते हैं।
- **Creative fields**: AI संगीत, कला और लेखन उत्पन्न करता है; Midjourney, DALL-E और GitHub Copilot जैसे tools ने creative workflows बदल दिए हैं।
- **Cybersecurity**: AI anomalies का पता लगाता है, threats की पहचान करता है, और हमलों तथा बचाव दोनों को शक्ति देता है।

## रोबोटिक्स और Embodied AI

रोबोटिक्स AI को भौतिक मशीनों के साथ जोड़ता है। आधुनिक robots perception (cameras, lidar), planning और control का उपयोग करके वातावरण में नेविगेट करते हैं और वस्तुओं को संचालित करते हैं। Boston Dynamics का Atlas उन्नत द्विपाद movement प्रदर्शित करता है। ABB और FANUC जैसी कंपनियों के industrial robots manufacturing को automate करते हैं। Household robots (Roomba) और surgical robots (da Vinci System) रोज़मर्रा और चिकित्सा परिवेश में AI का उपयोग करते हैं। Embodied AI research उन agents पर केंद्रित है जो दुनिया के साथ अंतःक्रिया करके भौतिक कौशल सीखते हैं, simulated और real environments के बीच की दूरी को कम करते हैं।

## वर्तमान AI रुझान (2020s)

- **Multimodal AI**: ऐसे सिस्टम जो text, images, audio और video को साथ में प्रोसेस करते हैं (GPT-4V, Gemini)
- **Agents and agentic AI**: ऐसे LLMs जो tools का उपयोग कर सकते हैं, web browse कर सकते हैं, code लिख सकते हैं और multi-step actions ले सकते हैं (OpenAI's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta की LLaMA ने researchers के लिए बड़े models तक पहुँच को लोकतांत्रिक बनाया
- **On-device AI**: phones और laptops पर cloud connectivity के बिना स्थानीय रूप से AI models चलाना (Apple Intelligence, Qualcomm NPUs)
- **AI regulation**: EU AI Act (2024) दुनिया का पहला व्यापक AI कानून है, जो AI systems को risk level के अनुसार वर्गीकृत करता है
