---
# Metadata
title: "Local AI Architecture"
description: "Local AI deployment architectures"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to engineering/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [local, ai, architecture, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Usanifu wa AI wa Mitaa
Mwongozo wa vitendo wa kuendesha miundo mikubwa ya lugha kwenye kifaa - mazingatio ya maunzi, injini za makisio, uboreshaji wa kumbukumbu, na muundo wa mfumo kwa ajili ya matumizi makali.
---

## Kwa Nini Uendeshe AI ​​Ndani Yake?
- **Faragha**: Hakuna data inayoondoka kwenye kifaa.
- **Gharama**: Hakuna ada za API kwa kila tokeni.
- **Latency**: Utabiri unaotabirika, usio na mtandao.
- **Upatikanaji wa nje ya mtandao**: Inafanya kazi bila mtandao.
- **Udhibiti**: Udhibiti kamili juu ya toleo la mfano, ubinafsishaji, na urekebishaji mzuri.
---

## Mahitaji ya maunzi
### Kumbukumbu ya GPU (VRAM)
Rasilimali muhimu zaidi. Ukubwa wa mfano katika kumbukumbu ≈ **vigezo × baiti kwa kila parameta**.
| Usahihi | Baiti kwa kila kigezo | 3.8B mfano | 7B mfano | 13B mfano | 70B mfano |
|-----------|--------------------|------------|----------------------------------|
| FP32 | 4 | ~ GB 15 | ~ GB 28 | ~ GB 52 | ~ GB 280 |
| FP16 | 2 | ~ GB 7.6 | ~ GB 14 | ~ GB 26 | ~ GB 140 |
| INT8 (8-bit) | 1 | ~ GB 3.8 | ~ GB 7 | ~ GB 13 | ~ GB 70 |
| INT4 (4-bit) | 0.5 | ~ GB 1.9 | ~ GB 3.5 | ~ GB 6.5 | ~ GB 35 |
**Miongozo ya vitendo:**
- 8GB VRAM → hadi miundo 7B kwa 4-bit.
- 12GB VRAM → hadi miundo 13B kwa 4-bit.
- 24GB VRAM → hadi miundo 70B kwa 4-bit (au 13B kwa 8-bit).
- Apple Silicon (kumbukumbu iliyounganishwa) inaweza kutumia mifano ya 70B kwenye mifumo ya 64GB+.
### RAM (Kumbukumbu ya Mfumo)
- Kwa uelekezaji wa CPU, unahitaji RAM ya mfumo wa kutosha kupakia modeli (sawa na nambari za VRAM).
- Kwa makisio ya GPU, RAM ya mfumo ni muhimu kwa kupakia muundo kwenye kumbukumbu kabla ya kupakia kwenye VRAM.
### Hifadhi
- Vipimo vya uzani wa mfano huchukua GB chache (k.m., 4-bit 7B ≈ GB 4 kwenye diski). Hakikisha angalau GB 20-50 bila malipo kwa miundo mingi.
### CPU
- Kwa usindikaji wa haraka (kujaza mapema) na upakiaji wa CPU, CPU ya kisasa ya msingi nyingi husaidia.
- Chipu za mfululizo wa Apple M zina utendakazi bora kwa LLMs kwa sababu ya kumbukumbu iliyounganishwa na Injini ya Neural.
---

## Ukadiriaji
Ukadiriaji hupunguza usahihi wa nambari za uzani, kukata kumbukumbu kwa kiasi kikubwa na kuongeza kasi kwa gharama ndogo ya usahihi.
### Miundo Maarufu
| Umbizo | Biti | Maelezo | Matumizi ya kawaida |
|--------|------|-------------|-------------|
| **GGUF** | 4-8 | umbizo la llama.cpp, lililoboreshwa kwa mseto wa CPU/GPU | Bora kwa makisio ya ndani |
| **GPTQ** | 4-8 | GPU pekee, yenye ufanisi kwenye CUDA | Bora kwa GPU za NVIDIA |
| **AWQ** | 4 | Uamilisho-fahamu, GPU pekee | Nzuri kwa makisio ya kundi kwenye GPUs |
| **ONNX** | tofauti | Sanifu, jukwaa-msingi | Huduma ya uzalishaji |
### Kuchagua Kiwango cha Kuhesabu
- ** Q8_0 ** (8-bit): hasara ndogo ya ubora, ukubwa mkubwa zaidi.
- **Q6_K** (6-bit): ubora mzuri, ukandamizaji mzuri.
- **Q5_K_M** (5-bit): sehemu tamu ya kawaida.
- **Q4_K_M** (4-bit): ubora mdogo zaidi, unaokubalika kwa kazi nyingi.
- **IQ4_XS** / **IQ3_XS**: Ukadiriaji ulioboreshwa na mkanganyiko bora katika biti 4/3.
**Kanuni ya kidole gumba:** Tumia Q4_K_M kwa usawa mzuri wa ubora na ukubwa. Ikiwa una VRAM ya ziada, tumia Q5 au Q6.
---

## Injini za Maelekezo (Ndani)
### llama.cpp
- Imeandikwa katika C++.
- Inasaidia umbizo la GGUF.
- Imeboreshwa kwa CPU na GPU (kupitia CUDA, Metal, OpenCL).
- Haraka sana, haswa kwenye CPU.
- Mstari wa amri, hali ya seva, na vifungo vya Python.
**Mfano wa amri:**```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
# -ngl 32 offloads 32 layers to GPU
```

### Ollama
- Hufunika llama.cpp na CLI rahisi na REST API.
- Miundo ya kupakua kiotomatiki, inasimamia.
- Nzuri kwa prototyping na programu za eneo-kazi.
- Inasaidia Modelfiles desturi kwa papo kwa mfumo.
```bash
ollama run phi3:3.8b
ollama run llama3:8b
```

### LM Studio
- Programu ya picha ya desktop ya Windows, macOS, Linux.
- Bonyeza moja kupakua na kiolesura cha gumzo.
- Seva ya ndani iliyojengwa ndani na API inayolingana ya OpenAI.
- Nzuri kwa watumiaji wasio wa kiufundi na majaribio ya haraka.
### Vibadilishaji vya Kukumbatiana vya Uso + bitsandbytes
- Maktaba ya kawaida ya Python ya mifano ya HF.
- Tumia`bitsandbytes`kwa ukadiriaji wa biti 4 (`load_in_4bit=True`).
- Inaweza kunyumbulika zaidi kwa urekebishaji mzuri lakini polepole kuliko llama.cpp kwa makisio.
### ExLlamaV2
- Uelekezaji wa haraka sana wa GPU kwa GPTQ na AWQ.
- Utendaji bora kwenye NVIDIA GPU.
- Inasaidia kizazi kilichounganishwa.
### mlx (Apple)
- Mfumo wa Apple kwa chips za M-mfululizo.
- Imeboreshwa sana kwa Silicon ya Apple.
- Python API.
---

#Usimamizi wa Kumbukumbu
### Dirisha la Muktadha na Akiba ya KV
Akiba ya KV huhifadhi jozi za thamani-msingi kwa kila safu na kila tokeni katika muktadha. Inakua kwa mstari na urefu wa muktadha.
Gharama ya kumbukumbu ≈ 2 × tabaka × (vichwa vya KV × hafifu ya kichwa) × tokeni × baiti kwa kila thamani
Kwa mfano wa safu 32 na vichwa 8 vya KV na dim ya kichwa 128, kila ishara inagharimu ~ 32 × 8 × 128 × 2 bytes = 65 KB kwa tokeni. Kwa tokeni 128k, hiyo ni ~ GB 8 kwa kache tu.
### Mikakati ya Kupakia
- **Kupakua kwa tabaka**: Weka tabaka kadhaa kwenye GPU, zingine kwenye CPU. Kasi kuliko CPU safi, hitaji la chini la VRAM.
- **Utiririshaji wa ishara**: Shika tokeni kwa nyongeza badala ya zote mara moja.
### Uakibishaji wa haraka
Tumia tena akiba za KV kwenye vidokezo sawa ili kuepuka kukokotoa tena awamu ya kujaza mapema. Baadhi ya mifumo inasaidia hili (k.m., vLLM, llama.cpp na`--prompt-cache`).
### Faili Zilizowekwa kwenye Kumbukumbu
Pakia uzani wa modeli moja kwa moja kutoka kwa diski bila kuzipakia kabisa kwenye RAM (muhimu kwa miundo mikubwa kwenye mifumo isiyo na kumbukumbu). llama.cpp hutumia ramani ya kumbukumbu kwa chaguo-msingi.
---

## Usanifu wa Usambazaji
### Hali ya Kifaa Kimoja
Mfano mmoja huendesha kwenye mashine moja (laptop, smartphone, kifaa cha makali). Inatumika kwa wasaidizi wa kibinafsi, programu za kuchukua madokezo, kukamilisha msimbo.
### Ukingo wa Mseto-Wingu
Mfano wa ndani hushughulikia maswali ya kawaida; kurudi kwenye muundo wa wingu kwa maswali changamano. Hii inatoa bora zaidi ya dunia zote mbili - kasi/faragha kwa wengi, uwezo wa matukio makali.
### Uelekezaji Uliosambazwa (Multi-GPU)
Kwa miundo mikubwa, gawanya tabaka kwenye GPU nyingi (usambamba wa tensor) au muktadha uliogawanyika kwenye vifaa (usambamba wa bomba). Tumia llama.cpp iliyo na`-ngl`au ExLlamaV2 iliyo na`--num-gpu-layers`.
### Usambazaji wa Simu ya Mkononi
- **Android**: Tumia llama.cpp kupitia vifungo vya JNI au ML Kit.
- **iOS**: Tumia llama.cpp kupitia Swift bindings au mlx.
- **Mtandao**: Tumia WebLLM (inaendesha WebGPU kupitia muda wa utekelezaji wa ONNX) au transformers.js.
---

## Uboreshaji wa Utendaji
### Kiwango cha Makini
Huongeza kasi ya ukokotoaji wa umakini na kupunguza utumiaji wa kumbukumbu. Inapatikana katika llama.cpp, ExLlamaV2, na maktaba za transfoma za kisasa.
### Maoni ya Kundi
Mchakato wa vidokezo vingi katika pasi moja ya mbele. Huongeza utumaji kwa kasi. Tumia`llama-batch`au vLLM.
### Kusimamisha Mapema / Bajeti ya Ishara
Weka kiwango cha juu cha bajeti ya tokeni ili kuzuia uzalishaji usio na mipaka.
### Usimbuaji wa Kukisia
Tumia muundo mdogo wa haraka (rasimu) kutabiri tokeni, kisha uthibitishe na muundo mkubwa sambamba. Inaweza kutoa kasi ya 2-3×.
---

## Mwongozo wa Usanidi wa Vitendo
### 1. Weka Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Vuta Mfano
```bash
ollama pull phi3:3.8b-q4_K_M
```

### 3. Endesha na API
```bash
ollama serve
```

Kisha tuma maombi kwa`http://localhost:11434/api/generate`.
### 4. Muunganisho wa Chatu
```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
```

### 5. (Mbadala) Tumia llama.cpp moja kwa moja
```bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
```

---

## Ufuatiliaji na Uangalizi
- Fuatilia utumiaji wa GPU (`nvidia-smi`kwenye Linux, Monitor ya Shughuli kwenye macOS).
- Fuatilia utumiaji wa kumbukumbu (RAM na VRAM).
- Kufuatilia ishara kwa pili (kupitia).
- Fuatilia wakati kwa ishara ya kwanza (latency).
- Tumia ukataji wa miti uliojengewa ndani kutoka kwa llama.cpp au Ollama.
---

## Mapungufu na Marekebisho
- **Pengo la ubora**: Miundo ndogo ya ndani (3.8B–7B) kwa ujumla ina utendaji duni wa miundo mikubwa ya wingu (GPT-4, Claude 3.5) kwenye hoja changamano.
- **Kukatika kwa maarifa**: Maarifa ya kielelezo hugandishwa wakati wa mafunzo; tumia RAG kuingiza habari ya sasa.
- **Lugha nyingi**: Miundo midogo zaidi inaweza kuwa na uwezo mdogo wa lugha nyingi.
- **Matumizi ya zana**: Mitiririko ya kazi ya mawakala (upigaji simu wa kitendakazi) huenda isiwe ya kuaminika sana kwenye miundo midogo.
Kwa kazi nyingi za kila siku (muhtasari, Maswali na Majibu, kukamilisha msimbo, uainishaji), mifano ya ndani tayari inatosha na inaboresha haraka.