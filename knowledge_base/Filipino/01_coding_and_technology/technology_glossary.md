<!--
---
# Metadata
title: "Technology Glossary"
description: "Technical terminology (AI models, hardware, benchmarks)"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [technology, glossary, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Glossary ng Teknolohiya
Isang reference na glossary na sumasaklaw sa mga modelo ng AI, hardware, benchmark, at pangunahing konsepto
sa modernong AI at computing landscape.
---

## AI Language Models at Assistants
### ChatGPT
Ang ChatGPT ay isang AI chatbot na binuo ng OpenAI, na unang inilabas noong Nobyembre 2022.
Ito ay pinapagana ng serye ng GPT ng malalaking modelo ng wika (LLMs). Ang ChatGPT ay isa
ng pinakamabilis na lumalagong mga produkto ng consumer AI sa kasaysayan, na umaabot sa 100 milyon
mga user sa loob ng dalawang buwan ng paglunsad. Sinusuportahan nito ang text-based na pag-uusap, code
henerasyon, pagbubuod, at malikhaing pagsulat. Ang mga bayad na tier ay nagbibigay ng access sa
mas makapangyarihang mga modelo tulad ng GPT-4 at GPT-4o.
### GPT (Generative Pre-trained Transformer)
Ang GPT ay isang pamilya ng malalaking modelo ng wika na nilikha ng OpenAI. Ang arkitektura
gumagamit ng decoder-only na Transformer na sinanay na may susunod na token na layunin ng hula sa
napakalaking text corpora. Kasama sa mga pangunahing bersyon ang GPT-2 (2019, 1.5B na mga parameter, kapansin-pansin
para sa "masyadong mapanganib na ilabas" na publisidad), GPT-3 (2020, 175B na mga parameter, malawak
ginamit sa pamamagitan ng API), GPT-3.5 (ang gulugod ng orihinal na ChatGPT), at GPT-4
(2023, multimodal, pagganap na malapit sa antas ng eksperto ng tao sa maraming benchmark).
### Claude
Si Claude ay isang AI assistant na binuo ng Anthropic. Ipinangalan ito kay Claude
Shannon, ang nagtatag ng teorya ng impormasyon. Ang Anthropic ay itinatag ng dating
Mga mananaliksik ng OpenAI at tumutuon sa "constitutional AI" — isang pamamaraan na gagawin
mga modelong mas ligtas sa pamamagitan ng pagsasanay sa kanila na sundin ang isang hanay ng mga prinsipyo. Mga modelo ni Claude
(Claude 1, 2, 3 Haiku / Sonnet / Opus) ay kilala para sa mahabang konteksto window (pataas
sa 200,000 tokens), nuanced reasoning, at binawasan ang mapaminsalang output kumpara sa
baseline na mga LLM.
### Gemini
Ang Gemini ay ang pamilya ng Google DeepMind ng mga multimodal AI models, na inihayag sa
Disyembre 2023. Ang Gemini ay katutubong multimodal — sinanay mula sa simula hanggang
teksto, mga larawan, audio, at video nang sabay-sabay, hindi tulad ng mga naunang modelo na nagkaroon
mga modalidad na idinagdag sa pamamagitan ng fine-tuning. Kasama sa mga bersyon ang Gemini Nano (on-device),
Gemini Flash (mabilis, cost-efficient), at Gemini Ultra (pinakamataas na kakayahan).
Pinapalakas ng Gemini ang AI chatbot ng Google na Bard (pinangalanang Gemini) at Google Search AI
Pangkalahatang-ideya.
### Phi-3-mini
Ang Phi-3-mini ay isang maliit na modelo ng wika (SLM) na binuo ng Microsoft na may 3.8B
mga parameter. Inilabas ito noong Abril 2024. Hindi tulad ng karamihan sa malalaking modelo, ang Phi-3-mini
ay sinanay sa isang maingat na na-curate na "kalidad ng textbook" na dataset — isang pamamaraan
pinasimunuan ng Microsoft Research — na inuuna ang kalidad ng data kaysa raw volume.
Sa kabila ng pagiging mas maliit kaysa sa GPT-4 o Claude 3 Opus, ang Phi-3-mini ay tumutugma o
mas malaki ang pagganap ng mga modelo sa mga benchmark ng pangangatwiran gaya ng MMLU at
HumanEval. Sinusuportahan nito ang isang window ng konteksto ng 4k token sa base na variant nito at isang 128k
window sa long-context na variant. Maaaring tumakbo ang Phi-3-mini sa iisang consumer GPU
o kahit sa device sa isang modernong smartphone na may sapat na RAM.
### Llama (Meta AI)
Ang Llama (Large Language Model Meta AI) ay isang open-weights na pamilya ng mga modelo
inilabas ng Meta. Ang Llama 2 (2023) ay inilabas para sa pananaliksik at komersyal na paggamit
na may mga sukat mula 7B hanggang 70B na mga parameter. Napabuti ang Llama 3 (2024).
makabuluhang pagganap, na may mga modelong mula 8B hanggang 70B (at mas bago ay 400B+).
Dahil ang mga timbang ay pampublikong nada-download, ang mga modelo ng Llama ang pundasyon
para sa isang malaking ecosystem ng mga fine-tuned na variant (Alpaca, Vicuna, atbp.)
at malawakang ginagamit para sa mga lokal/pribadong AI deployment.
### Mistral
Ang Mistral AI ay isang kumpanya ng French AI na bumubuo ng mga bukas at pagmamay-ari na LLM.
Ipinakita ng Mistral 7B (2023) na maaaring tumugma ang isang 7B-parameter na modelo sa
pagganap ng mas malalaking modelo gamit ang mahusay na mga diskarte tulad ng pag-slide
pansin sa bintana at atensyong nakagrupo-query. Ang Mixtral 8x7B (2023) ay isang halo-
of-experts model — dinadala nito ang bawat token sa isang subset ng 8 ekspertong network,
pagkamit ng GPT-3.5-level na pagganap habang mas mura sa computation.
Ang mga modelo ng Mistral ay ganap na bukas-timbang at maaaring patakbuhin nang lokal.
---

## GPU Hardware at Graphics Card
### GPU (Graphics Processing Unit)
Ang GPU ay isang processor na idinisenyo para sa massively parallel computation. Orihinal na
na binuo para sa pag-render ng 3D graphics, naging mahalaga ang mga GPU para sa pagsasanay sa AI/ML
at hinuha dahil nakakagawa sila ng libu-libong floating-point operations
sabay-sabay na gumagamit ng libu-libong maliliit na core. Ang dalawang pangunahing tagagawa ng GPU
para sa AI ay NVIDIA at AMD.
### NVIDIA GeForce RTX Series
Ang serye ng RTX (Ray Tracing Texel eXtreme) ay ang consumer GPU line ng NVIDIA. RTX
Kasama sa 30xx (Ampere, 2020) at RTX 40xx (Ada Lovelace, 2022) na henerasyon ang
nakalaang Tensor Cores para sa pagpapabilis ng mga operasyon ng AI. Ang VRAM (video RAM) ay
kritikal para sa lokal na pagpapatakbo ng mga modelo ng AI — kayang hawakan ng 8GB GPU ang 7B parameter
mga modelo sa 4-bit na quantization; kayang hawakan ng 24GB GPU ang 70B na mga modelo sa 4-bit.
### NVIDIA A-Series at H-Series (Data Center)
Ang A100 (Ampere, 2020) at H100 (Hopper, 2022) ay ang propesyonal na AI ng NVIDIA
mga accelerators. Ang isang H100 ay may hanggang 80GB ng HBM3 memory at ito ang pamantayan
hardware sa likod ng karamihan sa malakihang pagsasanay sa LLM ngayon. Ang mga GPU na ito ay nagkakahalaga ng $25,000–
$40,000 bawat isa ngunit nag-aalok ng 10–30× ang AI throughput ng mga consumer RTX card.
### Serye ng AMD Radeon RX
Ang linya ng consumer GPU ng AMD. Ang RX 7900 XTX (2022) ay may 24GB VRAM at maaaring tumakbo
mga lokal na LLM sa pamamagitan ng ROCm (GPU compute stack ng AMD). Ang mga AMD GPU ay karaniwang mas mababa
mahusay na suportado kaysa sa NVIDIA para sa AI frameworks, kahit na ang suporta ay bumubuti.
### Intel Arc
Ang Intel Arc ay ang discrete GPU na linya ng produkto ng Intel, na inilabas simula noong 2022. Arc
Sinusuportahan ng mga GPU ang XeSS (super-sampling ng Intel) at may limitado ngunit lumalaking suporta
para sa AI inference tasks sa pamamagitan ng OpenVINO at IPEX-LLM frameworks.
### ARK Intel (ark.intel.com)
Ang ARK ay ang opisyal na database ng mga detalye ng produkto ng Intel sa ark.intel.com. Ito
nagbibigay ng mga detalyadong teknikal na detalye para sa bawat Intel CPU, GPU, FPGA, at
produkto ng NUC, kabilang ang mga pangunahing bilang, bilis ng orasan, TDP, mga sinusuportahang uri ng memorya,
at mga tampok na set ng pagtuturo. Kapag narinig mo ang "suriin ang ARK para sa mga detalye," ang ibig sabihin nito
pagbisita sa database na iyon para sa makapangyarihang impormasyon ng hardware.
---

## Mga Benchmark ng Pagganap ng AI
### MMLU (Massive Multitask Language Understanding)
Ang MMLU ay isang benchmark na sumusubok sa LLM na kaalaman sa 57 akademikong paksa kabilang ang
matematika, kasaysayan, batas, medisina, at computer science. Binubuo ito ng
maramihang-pagpipiliang tanong na nakuha mula sa mga tunay na pagsusulit sa antas ng unibersidad. Isang marka ng
70% ay halos antas ng undergraduate ng tao; Ang marka ng GPT-4 at Claude 3 ay higit sa 86%.
Ang Phi-3-mini ay nakakuha ng humigit-kumulang 69% sa kabila ng maliit na sukat nito.
### HumanEval
Ang HumanEval ay ang benchmark ng OpenAI para sa pagbuo ng code. Binubuo ito ng 164 Python
mga problema sa programming sa mga awtomatikong kaso ng pagsubok. Ang mga modelo ay sinusukat sa
pass@k — ang posibilidad na kahit isa sa k na nabuong mga solusyon ay pumasa sa lahat
mga pagsubok. Mga marka ng GPT-4 ~87% (pass@1); ang isang well-tuned na 7B na modelo ay maaaring umabot sa ~50–60%.
### HellaSwag
Ang HellaSwag ay isang commonsense reasoning benchmark. Ang mga modelo ay binibigyan ng pangungusap
naglalarawan ng isang makamundong aktibidad at dapat piliin ang pinaka-malamang na pagpapatuloy mula sa
apat na pagpipilian. Ang mga maling opsyon ay espesyal na idinisenyo upang maging kapani-paniwala ngunit
bahagyang mali. Sinusuri nito kung ang isang modelo ay may batayan na pag-unawa sa pisikal
at mga sitwasyong panlipunan.
### ARC (AI2 Reasoning Challenge)
Ang ARC ay isang benchmark mula sa Allen Institute para sa AI. Binubuo ito ng grade-school
mga tanong sa agham, na hinati sa hanay ng "Madali" at "Hamon." Ang Challenge set
naglalaman ng mga tanong na nakabatay sa pagkuha ng mga pamamaraan at simpleng istatistikal na modelo
pakikibaka sa, nangangailangan ng multi-step na pangangatwiran.
---

## Mga Pangunahing Konsepto ng AI/ML
### RAG (Retrieval-Augmented Generation)
Ang RAG ay isang pamamaraan na pinagsasama ang isang retrieval system (karaniwang isang vector
database) na may modelo ng wika. Sa halip na umasa lamang sa modelo
parametric na kaalaman, kinukuha muna ng RAG ang mga nauugnay na dokumento mula sa isang panlabas
base ng kaalaman at pagkatapos ay isama ang mga ito sa konteksto ng modelo. Ito ay nagpapahintulot sa
modelo upang sagutin ang mga tanong tungkol sa napapanahon o impormasyong tukoy sa domain
nang walang muling pagsasanay. Gumagamit ang Potato.ai ng isang anyo ng RAG — kinukuha nito mula sa KB nito
at kasama ang mga resulta sa konteksto bago makabuo ng tugon.
### Fine-tuning
Ang fine-tuning ay ang proseso ng patuloy na pagsasanay ng isang pre-trained na modelo sa isang
mas maliit, dataset na tukoy sa domain. Inaangkop nito ang mga timbang ng modelo para sa a
partikular na gawain o domain. Halimbawa, maaaring maayos ang isang base LLM
mga medikal na rekord upang lumikha ng isang medikal na Q&A assistant. Ang fine-tuning ay
computationally mahal ngunit mas mura kaysa sa pagsasanay mula sa simula.
### Quantization
Binabawasan ng quantization ang numerical precision ng mga timbang ng modelo (hal. mula sa 32-bit
lumutang sa 4-bit integer). Ito ay kapansin-pansing binabawasan ang memory footprint - isang 7B na modelo
sa 16-bit na katumpakan ay nangangailangan ng ~14GB VRAM; ang parehong modelo sa 4-bit (GGUF format)
nangangailangan ng ~4GB. Ang quantization ay karaniwang nagdudulot ng maliit ngunit katanggap-tanggap na katumpakan
degradasyon at ito ang pangunahing pamamaraan na nagbibigay-daan sa malalaking modelo na tumakbo sa consumer
hardware o kahit na mga mobile device.
### Context Window
Ang window ng konteksto ay ang maximum na bilang ng mga token na maaaring iproseso ng isang modelo nang sabay-sabay,
kabilang ang parehong prompt at ang nabuong tugon. Ang GPT-3.5 ay mayroong 4,096-token
bintana; Sinusuportahan ng GPT-4 Turbo at Claude 3 ang 128,000 token; Gemini 1.5 Pro
sumusuporta sa 1,000,000 token. Ang isang mas malaking window ng konteksto ay nagbibigay-daan sa modelo na "makita"
higit pa sa isang pag-uusap o dokumento nang sabay-sabay, pagpapabuti ng pagkakaugnay-ugnay sa loob ng mahabang panahon
palitan.
### RLHF (Reinforcement Learning mula sa Human Feedback)
Ang RLHF ay ang diskarte sa pagsasanay na nagbabago ng isang batayang modelo ng wika (na
hinuhulaan lamang ang susunod na token) sa isang katulong na sumusunod sa mga tagubilin at
kumikilos nang matulungin. Mga output ng modelo ng marka ng mga human rater, isang modelo ng reward ang sinanay
sa kanilang mga kagustuhan, at ang modelo ng wika ay na-optimize laban dito
modelo ng reward gamit ang reinforcement learning. Ginagamit lahat ng ChatGPT, Claude, at Gemini
mga variant ng RLHF o mga katulad na diskarte sa pag-align (hal. Constitutional AI,
Direktang Pag-optimize ng Kagustuhan).
### Arkitektura ng Transformer
Ang Transformer ay ang neural network architecture na pinagbabatayan ng lahat ng modernong LLM.
Ipinakilala sa 2017 na papel na "Attention Is All You Need" ni Vaswani et al., ito
ay gumagamit ng mga mekanismo ng pagtutuon sa sarili upang iproseso ang lahat ng mga token nang magkatulad sa halip na
sunud-sunod. Ang Encoder-only Transformers (BERT) ay ginagamit para sa pag-unawa sa mga gawain;
Ang decoder-only na mga Transformer (GPT, Llama, Mistral) ay ginagamit para sa mga gawain sa pagbuo;
Ang encoder-decoder Transformers (T5, BART) ay ginagamit para sa pagsasalin at pagbubuod.
### Mga Embedding at Vector Database
Ang mga pag-embed ay siksik na numerical na representasyon ng teksto (o mga larawan) na ginawa ni
isang neural network. Ang mga tekstong may kaparehong semantiko ay may mga naka-embed na malapit
espasyo ng vector. Tindahan ng mga vector database (ChromaDB, Pinecone, Weaviate, Qdrant).
ang mga pag-embed na ito at sumusuporta sa mabilis na tinatayang paghahanap ng pinakamalapit na kapitbahay. Sila ay
ang storage backbone ng RAG system, kabilang ang cold-memory layer ng Potato.ai.