---
# Metadata
title: "NLP Fundamentals"
description: "Text processing, embeddings, Transformers, BERT, GPT"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [nlp, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# NLP Fundamentals
Ang Natural Language Processing (NLP) ay ang larangan ng pagtuturo ng mga makina upang maunawaan, makabuo, at magtrabaho sa wika ng tao. Pinapagana nito ang mga search engine, chatbots, translation system, sentiment analysis, at ang malalaking language models (LLMs) na nagpabago sa AI mula noong 2020. Sinasaklaw ng file na ito ang ebolusyon mula sa mga klasikal na diskarte hanggang sa modernong Transformer-based na mga arkitektura.
---

## Text Preprocessing
Magulo ang raw text. Bago ito magamit ng isang modelo, kailangan itong linisin at ayusin.
| Hakbang | Ano ang Ginagawa Nito | Halimbawa |
|------|-------------|---------|
| **Tokenization** | Hatiin ang text sa mga token (mga salita, subword, o character) | "Mahal ko ang NLP" →`["I", "love", "NLP"]`|
| **Lowercasing** | I-convert sa lowercase | "Hello" → "hello" |
| **Ihinto ang pag-alis ng salita** | Alisin ang mga karaniwang salita (ang, ay, sa) | "nakaupo ang pusa" → "nakaupo ang pusa" |
| **Stemming** | I-chop ang mga dulo ng salita (crude) | "tumatakbo" → "tumatakbo" |
| **Lemmatization** | Bawasan sa anyo ng diksyunaryo (malay sa konteksto) | "mas mabuti" → "mabuti" |
| **Normalization** | Ayusin ang pag-encode, alisin ang mga espesyal na character, palawakin ang mga contraction | "huwag" → "huwag" |
Ang mga modernong modelo ng Transformer ay madalas na lumalaktaw sa paghinto ng pag-alis ng salita at pag-stem — natutunan nila ang mga pattern na ito mula sa data.
---

## Representasyon ng Teksto
Ang mga makina ay nangangailangan ng mga numero, hindi mga salita. Kung paano namin kinakatawan ang teksto bilang mga vector ay mahalaga.
### Mga Klasikal na Pagdulog
| Paraan | Paglalarawan | Limitasyon |
|--------|-------------|-----------|
| **One-Hot Encoding** | Ang bawat salita ay isang natatanging posisyon sa isang malaking vector | Kalat-kalat; walang semantikong kahulugan |
| **Bag of Words (BoW)** | Bilangin ang mga frequency ng salita; huwag pansinin ang order | Nawala ang pagkakasunud-sunod ng salita nang buo |
| **TF-IDF** | Timbangin ang mga salita ayon sa dalas sa dokumento × pambihira sa buong corpus | Hindi pa rin pinapansin ang kaayusan at konteksto |
### Mga Pag-embed ng Salita
Ang mga pag-embed ay nagmamapa ng mga salita sa mga siksik na vector kung saan magkakalapit ang magkakatulad na salita.
| Modelo | Pangunahing Ideya |
|-------|----------|
| **Word2Vec** (2013) | Hulaan ang salita mula sa konteksto (CBOW) o konteksto mula sa salita (Skip-gram) |
| **GloVe** (2014) | Global co-occurrence statistics → siksik na vectors |
| **FastText** (2016) | Word2Vec + impormasyon ng subword (mas mahusay na pinangangasiwaan ang mga bihirang salita) |
Ang sikat na halimbawa:`king - man + woman ≈ queen`. Ang mga pag-embed ay kumukuha ng mga semantikong relasyon.
**Limitation**: Ang mga classical na embeddings ay nagtatalaga ng isang vector bawat salita, kaya hindi nila mahawakan ang polysemy (mga salitang may maraming kahulugan). Ang "Bank" sa "bank ng ilog" at "bank account" ay nakakakuha ng parehong vector.
---

## Mga Modelo ng Pagkakasunud-sunod
Bago ang mga Transformer, ang karaniwang diskarte para sa NLP ay upang iproseso ang teksto nang sunud-sunod.
| Arkitektura | Paano Ito Gumagana | Lakas | Kahinaan |
|-------------|-------------|----------|----------|
| **RNN** | Iproseso ang mga token nang paisa-isa; panatilihin ang nakatagong estado | Pinangangasiwaan ang variable-length na input | Naglalaho na mga gradient; hindi makuha ang mahabang dependencies |
| **LSTM** | RNN na may mga gate (forget, input, output) para kontrolin ang daloy ng impormasyon | Mas mahusay sa long-range dependencies | Sunod-sunod pa rin; mabagal magsanay |
| **GRU** | Pinasimpleng LSTM (mas kaunting gate) | Mas mabilis kaysa sa LSTM; katulad na pagganap | Parehong pangunahing mga limitasyon |
Pinoproseso ng mga modelong ito ang teksto mula kaliwa-pakanan, na nangangahulugang mabagal silang magsanay (hindi maihahalintulad) at nakikipagpunyagi sa mga long-range na dependency.
---

## Ang Mekanismo ng Atensyon
Ang atensyon ay nagbibigay-daan sa isang modelo na tingnan ang lahat ng mga posisyon sa isang pagkakasunud-sunod nang sabay-sabay at magpasya kung alin ang pinaka-may-katuturan para sa kasalukuyang hula.
### Pangunahing Insight
Sa halip na i-compress ang isang buong pangungusap sa iisang nakatagong estado (tulad ng ginagawa ng mga RNN), kinukuwenta ng pansin ang isang timbang na kabuuan ng lahat ng mga nakatagong estado, kung saan natutunan ang mga timbang.
```
Attention(Q, K, V) = softmax(QK^T / √d_k) V
```

| Bahagi | Tungkulin |
|-----------|------|
| **Query (Q)** | Ano ang hinahanap ko? |
| **Susi (K)** | Ano ang nilalaman ko? |
| **Halaga (V)** | Anong impormasyon ang ibibigay ko? |
| **√d_k** | Salik sa pag-scale para maiwasan ang malalaking tuldok na produkto |
---

## Ang Arkitektura ng Transformer
Ang Transformer (Vaswani et al., 2017 — "Attention Is All You Need") ganap na pinalitan ng pansin ang pag-ulit. Ito ang pundasyon ng halos lahat ng modernong NLP.
### Arkitektura
| Bahagi | Paglalarawan |
|-----------|-------------|
| **Encoder** | Nagbabasa ng input text; gumagawa ng mga kontekstwal na representasyon |
| **Decoder** | Bumubuo ng teksto ng output; dumadalo sa output ng encoder |
| ** Pansariling Pansin** | Ang bawat token ay dumadalo sa lahat ng iba pang mga token sa parehong pagkakasunud-sunod |
| **Multi-Head Attention** | Magpatakbo ng maramihang mga ulo ng atensyon nang magkatulad; makuha ang iba't ibang mga relasyon |
| **Positional Encoding** | Mag-inject ng impormasyon sa posisyon (dahil walang pag-ulit) |
| **Feed-Forward Network** | Inilapat sa bawat posisyon nang nakapag-iisa |
| **Layer Normalization** | Patatagin ang pagsasanay |
| **Mga Natirang Koneksyon** | Laktawan ang mga koneksyon para sa gradient flow |
### Encoder-Only, Decoder-Only, Encoder-Decoder
| Variant | Arkitektura | Pinakamahusay Para sa | Mga halimbawa |
|---------|-------------|----------|---------|
| **Encoder-only** | Nauunawaan ang teksto | Pag-uuri, NER, pagsusuri ng damdamin | BERT, RoBERTa, DeBERTa |
| **Decoder-only** | Bumubuo ng teksto | Mga modelo ng wika, chatbots, pagbuo ng code | GPT-3/4, LLaMA, Claude |
| **Encoder-Decoder** | Binabago ang teksto | Pagsasalin, pagbubuod | T5, BART, mBART |
---

## Mga Pangunahing Modelong Pamilya
### BERT Family (Encoder-Only)
| Modelo | Pangunahing Tampok |
|-------|-------------|
| **BERT** (2018) | Modelo ng Masked Language + Next Sentence Prediction |
| **RoBERTa** | Inalis ang NSP; sinanay nang mas matagal na may mas maraming data |
| **ALBERT** | Pagbabahagi ng parameter; mas maliit na bakas ng paa |
| **DeBERTa** | Nawala ang pansin; pinahusay na NLU |
| **DistilBERT** | 40% na mas maliit, 60% na mas mabilis, nagpapanatili ng 97% ng pagganap ng BERT |
### GPT Family (Decoder-Only)
| Modelo | Mga Parameter | Mga Tala |
|-------|-----------|-------|
| **GPT-2** | 1.5B | Ang mga ipinakitang decoder-only na modelo ay maaaring makabuo ng magkakaugnay na teksto |
| **GPT-3** | 175B | Few-shot learning; sinenyasan sa halip na pinong-pino |
| **GPT-3.5 / GPT-4** | Hindi isiniwalat | Instruction-tuned + RLHF; pakikipag-usap |
| **LLaMA** (Meta) | 7B–70B | Bukas-timbang; nagbunga ng open-source na LLM ecosystem |
| **Mistral / Mixtral** | 7B / 8×7B (MoE) | Mahusay na bukas na mga modelo na may malakas na pagganap |
---

## Mga Pangunahing Gawain sa NLP
| Gawain | Paglalarawan | Karaniwang Modelo |
|------|-------------|--------------|
| **Pag-uuri ng Teksto** | Magtalaga ng label sa text (spam/hindi spam, positibo/negatibo) | BERT, mga fine-tuned classifier |
| **Named Entity Recognition (NER)** | Tukuyin ang mga tao, organisasyon, lokasyon sa text | BERT + CRF layer |
| **Pagsusuri ng Sentimento** | Tukuyin ang emosyonal na tono | Fine-tuned BERT o zero-shot LLM |
| **Pagsasalin sa Makina** | Magsalin sa pagitan ng mga wika | T5, mBART, MarianMT |
| **Pagsagot sa Tanong** | Sagutin ang mga tanong na ibinigay sa konteksto | BERT (extractive), GPT (generative) |
| **Pagbubuod** | I-condense ang mahabang text | T5, BART, GPT |
| **Pagbuo ng Teksto** | Gumawa ng magkakaugnay na teksto | GPT-4, LLaMA, Claude |
---

## Fine-Tuning vs Prompting
| Diskarte | Paano Ito Gumagana | Kailan Gagamitin |
|----------|-------------|-------------|
| **Fine-tuning** | I-update ang mga timbang ng modelo sa iyong data na tukoy sa gawain | Ikaw ay may label na data; kailangan ng maximum na pagganap |
| **Pag-prompt** | Ibigay ang mga tagubilin ng modelo sa natural na wika | Mabilis na prototyping; limitadong data; gamit ang mga LLM |
| **Few-shot** | Isama ang mga halimbawa sa prompt | Kapag mayroon kang ilang mga halimbawa ngunit hindi sapat para sa fine-tuning |
| **LoRA / QLoRA** | Mahusay na fine-tuning; i-update ang maliliit na mababang ranggo na matrice | I-fine-tune ang malalaking modelo na may limitadong GPU memory |
---

## Mga Tool at Framework
| Tool | Layunin |
|------|---------|
| **Hugging Face Transformers** | Mga pre-trained na modelo, tokeniser, fine-tuning pipelines |
| **spaCy** | Production-grade NLP pipeline (tokenization, NER, POS, dependency) |
| **NLTK** | Pang-edukasyon; klasikal na NLP algorithm |
| **Gensim** | Pagmomodelo ng paksa (LDA), mga pag-embed ng salita (Word2Vec, Doc2Vec) |
| **LangChain / LlamaIndex** | Mga Framework para sa pagbuo ng mga application na pinapagana ng LLM |
| **vLLM** | High-throughput na paghahatid ng LLM |
| **Mga Tokenizer (HF)** | Mabilis na tokenization (BPE, WordPiece, SentencePiece) |
---

## Ang LLM Landscape
Ang modernong landscape ng NLP ay pinangungunahan ng Malaking Mga Modelo ng Wika:
| Kategorya | Mga halimbawa | Mga Tala |
|----------|---------|-------|
| **Pagmamay-ari** | GPT-4, Claude, Gemini | Pinakamahusay na pagganap; API access lang |
| **Open-weight** | LLaMA 3, Mistral, Qwen | Available ang mga timbang; tumakbo nang lokal |
| **Open-source** | Pythia, OPT | Ganap na bukas (data, timbang, code) |
| **Multimodal** | GPT-4V, Gemini, LLaVA | Iproseso ang teksto + mga larawan |
| **Espesyalista sa code** | CodeLlama, StarCoder, DeepSeek Coder | Sinanay sa code |
| **Maliit / Mahusay** | Phi-3, Gemma, TinyLlama | Malakas na pagganap sa maliit na sukat |
Mabilis ang takbo ng field. Ano ang cutting-edge ngayon ay maaaring palitan sa mga buwan. Ang mga pangunahing kaalaman — atensyon, tokenization, fine-tuning, pagsusuri — ay nananatiling matatag.