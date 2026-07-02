# Technologieglossar

Ein Referenzglossar zu AI-Modellen, Hardware, Benchmarks und Kernkonzepten
in der modernen AI- und Computing-Landschaft.

---

## Sprachmodelle und Assistenten für AI

### ChatGPT
ChatGPT ist ein von OpenAI entwickelter AI-Chatbot, der erstmals im November 2022 veröffentlicht wurde.
Es basiert auf der GPT-Serie großer Sprachmodelle (LLMs). ChatGPT ist eines
 der am schnellsten wachsenden Verbraucher-AI-Produkte der Geschichte und erreichte innerhalb von zwei Monaten nach dem Start 100 Millionen Nutzer. Es unterstützt textbasierte Konversation, Codegenerierung, Zusammenfassungen und kreatives Schreiben. Kostenpflichtige Stufen bieten Zugang zu leistungsfähigeren Modellen wie GPT-4 und GPT-4o.

### GPT (Generative Pre-trained Transformer)
GPT ist eine Familie großer Sprachmodelle, die von OpenAI entwickelt wurde. Die Architektur
verwendet einen Decoder-only-Transformer, der mit dem Ziel der Vorhersage des nächsten Tokens auf
massiven Textkorpora trainiert wurde. Wichtige Versionen sind GPT-2 (2019, 1.5B Parameter, bekannt
für die „too dangerous to release“-Publizität), GPT-3 (2020, 175B Parameter, breit
über die API genutzt), GPT-3.5 (das Rückgrat des ursprünglichen ChatGPT) und GPT-4
(2023, multimodal, Leistung nahe am Niveau menschlicher Experten in vielen Benchmarks).

### Claude
Claude ist ein von Anthropic entwickelter AI-Assistent. Er ist nach Claude
Shannon, dem Begründer der Informationstheorie, benannt. Anthropic wurde von ehemaligen
OpenAI-Forschern gegründet und konzentriert sich auf „constitutional AI“ — eine Technik, um
Modelle sicherer zu machen, indem sie darauf trainiert werden, einer Reihe von Prinzipien zu folgen. Claude-Modelle
(Claude 1, 2, 3 Haiku / Sonnet / Opus) sind bekannt für lange Kontextfenster (bis
zu 200,000 Tokens), differenziertes Denken und reduzierte schädliche Ausgaben im Vergleich zu
Basis-LLMs.

### Gemini
Gemini ist Google DeepMinds Familie multimodaler AI-Modelle, angekündigt im
Dezember 2023. Gemini ist nativ multimodal — von Grund auf gleichzeitig auf
Text, Bilder, Audio und Video trainiert, im Gegensatz zu früheren Modellen, bei denen
Modalitäten per Fine-Tuning hinzugefügt wurden. Versionen umfassen Gemini Nano (on-device),
Gemini Flash (schnell, kosteneffizient) und Gemini Ultra (höchste Leistungsfähigkeit).
Gemini treibt Googles AI-Chatbot Bard (umbenannt in Gemini) und Google Search AI
Overviews an.

### Phi-3-mini
Phi-3-mini ist ein kleines Sprachmodell (SLM) von Microsoft mit 3.8B
Parametern. Es wurde im April 2024 veröffentlicht. Im Gegensatz zu den meisten großen Modellen wurde Phi-3-mini
auf einem sorgfältig kuratierten Datensatz in „Textbook-Qualität“ trainiert — eine von Microsoft Research
vorangetriebene Technik —, die Datenqualität gegenüber reiner Menge priorisiert.
Trotz seiner deutlich geringeren Größe als GPT-4 oder Claude 3 Opus erreicht oder übertrifft Phi-3-mini
Modelle, die um ein Vielfaches größer sind, bei Reasoning-Benchmarks wie MMLU und
HumanEval. Es unterstützt ein Kontextfenster von 4k Tokens in der Basisvariante und ein 128k-
Fenster in der Long-Context-Variante. Phi-3-mini kann auf einer einzelnen Consumer-GPU
oder sogar on-device auf einem modernen Smartphone mit ausreichend RAM laufen.

### Llama (Meta AI)
Llama (Large Language Model Meta AI) ist eine Familie von Modellen mit offenen Gewichten,
veröffentlicht von Meta. Llama 2 (2023) wurde für Forschung und kommerzielle Nutzung
mit Größen von 7B bis 70B Parametern veröffentlicht. Llama 3 (2024) verbesserte die
Leistung deutlich, mit Modellen von 8B bis 70B (und später 400B+).
Da die Gewichte öffentlich herunterladbar sind, bilden Llama-Modelle die Grundlage
für ein großes Ökosystem feinabgestimmter Varianten (Mistral, Alpaca, Vicuna usw.)
und werden häufig für lokale/private AI-Deployments eingesetzt.

### Mistral
Mistral AI ist ein französisches AI-Unternehmen, das offene und proprietäre LLMs entwickelt.
Mistral 7B (2023) zeigte, dass ein Modell mit 7B Parametern die
Leistung wesentlich größerer Modelle durch effiziente Techniken wie Sliding
Window Attention und Grouped-Query Attention erreichen kann. Mixtral 8x7B (2024) ist ein Mixture-
of-Experts-Modell — es leitet jedes Token an eine Teilmenge von 8 Expertennetzwerken weiter,
und erreicht dabei Leistung auf GPT-3.5-Niveau bei geringeren Rechenkosten.
Die Modelle von Mistral haben vollständig offene Gewichte und können lokal ausgeführt werden.

---

## GPU-Hardware und Grafikkarten

### GPU (Graphics Processing Unit)
Eine GPU ist ein Prozessor, der für massiv parallele Berechnungen ausgelegt ist. Ursprünglich
für das Rendern von 3D-Grafik entwickelt, sind GPUs für AI/ML-Training
und Inferenz unverzichtbar geworden, weil sie Tausende von Gleitkommaoperationen
mithilfe Tausender kleiner Kerne gleichzeitig ausführen können. Die zwei wichtigsten GPU-Hersteller
für AI sind NVIDIA und AMD.

### NVIDIA GeForce RTX Series
Die RTX-Reihe (Ray Tracing Texel eXtreme) ist die Consumer-GPU-Linie von NVIDIA. Die Generationen RTX
30xx (Ampere, 2020) und RTX 40xx (Ada Lovelace, 2022) enthalten dedizierte Tensor Cores zur
Beschleunigung von AI-Operationen. VRAM (Video RAM) ist entscheidend,
um AI-Modelle lokal auszuführen — eine 8GB-GPU kann 7B-Parameter-
Modelle in 4-Bit-Quantisierung verarbeiten; eine 24GB-GPU kann 70B-Modelle in 4-Bit verarbeiten.

### NVIDIA A-Series und H-Series (Data Centre)
Der A100 (Ampere, 2020) und der H100 (Hopper, 2022) sind die professionellen AI-
Beschleuniger von NVIDIA. Ein H100 verfügt über bis zu 80GB HBM3-Speicher und ist die Standard-
Hardware hinter dem Großteil des heutigen großskaligen LLM-Trainings. Diese GPUs kosten jeweils $25,000–
$40,000, bieten aber die 10–30-fache AI-Throughput-Leistung von Consumer-RTX-Karten.

### AMD Radeon RX Series
AMDs Consumer-GPU-Linie. Die RX 7900 XTX (2022) hat 24GB VRAM und kann
lokale LLMs über ROCm (AMDs GPU-Compute-Stack) ausführen. AMD-GPUs werden für AI-Frameworks im Allgemeinen weniger
gut unterstützt als NVIDIA, auch wenn die Unterstützung besser wird.

### Intel Arc
Intel Arc ist Intels Produktlinie diskreter GPUs, die ab 2022 veröffentlicht wurde. Arc-
GPUs unterstützen XeSS (Intels Super-Sampling) und haben eine begrenzte, aber wachsende Unterstützung
für AI-Inferenzaufgaben über die Frameworks OpenVINO und IPEX-LLM.

### ARK Intel (ark.intel.com)
ARK ist Intels offizielle Datenbank für Produktspezifikationen unter ark.intel.com. Sie
bietet detaillierte technische Spezifikationen für jedes Intel-CPU-, GPU-, FPGA- und
NUC-Produkt, einschließlich Kernanzahl, Taktfrequenzen, TDP, unterstützten Speichertypen
und Befehlssatzmerkmalen. Wenn man hört „check ARK for specs“, bedeutet das,
diese Datenbank für maßgebliche Hardwareinformationen zu besuchen.

---

## AI-Leistungs-Benchmarks

### MMLU (Massive Multitask Language Understanding)
MMLU ist ein Benchmark, der das Wissen von LLMs über 57 akademische Fächer testet, darunter
Mathematik, Geschichte, Recht, Medizin und Informatik. Er besteht aus
Multiple-Choice-Fragen aus echten Prüfungen auf Universitätsniveau. Ein Wert von
70% entspricht ungefähr dem Niveau menschlicher Studierender; GPT-4 und Claude 3 liegen über 86%.
Phi-3-mini erreicht trotz seiner kleinen Größe etwa 70%.

### HumanEval
HumanEval ist OpenAIs Benchmark für Codegenerierung. Er besteht aus 164 Python-
Programmieraufgaben mit automatisierten Testfällen. Modelle werden anhand von
pass@k gemessen — der Wahrscheinlichkeit, dass mindestens eine von k generierten Lösungen alle
Tests besteht. GPT-4 erreicht ~87% (pass@1); ein gut abgestimmtes 7B-Modell kann ~50–60% erreichen.

### HellaSwag
HellaSwag ist ein Benchmark für Common-Sense-Reasoning. Modelle bekommen einen Satz,
der eine alltägliche Aktivität beschreibt, und müssen aus
vier Optionen die wahrscheinlichste Fortsetzung wählen. Die falschen Optionen sind gezielt so gestaltet, dass sie plausibel,
aber subtil falsch sind. Der Benchmark testet, ob ein Modell ein fundiertes Verständnis physischer
und sozialer Situationen hat.

### ARC (AI2 Reasoning Challenge)
ARC ist ein Benchmark des Allen Institute for AI. Er besteht aus naturwissenschaftlichen Fragen auf Grundschulniveau,
aufgeteilt in „Easy“- und „Challenge“-Sets. Das Challenge-Set
enthält Fragen, mit denen retrieval-basierte Methoden und einfache statistische Modelle
Schwierigkeiten haben und die mehrstufiges Reasoning erfordern.

---

## Zentrale AI/ML-Konzepte

### RAG (Retrieval-Augmented Generation)
RAG ist eine Technik, die ein Retrieval-System (typischerweise eine Vektor-
Datenbank) mit einem Sprachmodell kombiniert. Anstatt sich ausschließlich auf das
parametrische Wissen des Modells zu verlassen, ruft RAG zunächst relevante Dokumente aus einer externen
Wissensbasis ab und fügt sie dann dem Kontext des Modells hinzu. Dadurch kann das
Modell Fragen zu aktuellen oder domänenspezifischen Informationen beantworten,
ohne neu trainiert zu werden. Potato.ai verwendet eine Form von RAG — es ruft Inhalte aus seiner KB ab
und fügt die Ergebnisse dem Kontext hinzu, bevor eine Antwort generiert wird.

### Fine-tuning
Fine-tuning ist der Prozess, ein vortrainiertes Modell auf einem
kleineren, domänenspezifischen Datensatz weiter zu trainieren. Dadurch werden die Gewichte des Modells für eine
bestimmte Aufgabe oder Domäne angepasst. Ein Basis-LLM könnte zum Beispiel auf
Krankenakten feinabgestimmt werden, um einen medizinischen Q&A-Assistenten zu erstellen. Fine-tuning ist
rechenintensiv, aber deutlich günstiger als ein Training von Grund auf.

### Quantisierung
Quantisierung reduziert die numerische Präzision von Modellgewichten (z. B. von 32-Bit-
Float auf 4-Bit-Integer). Das reduziert den Speicherbedarf drastisch — ein 7B-Modell
in 16-Bit-Präzision benötigt ~14GB VRAM; dasselbe Modell in 4-Bit (GGUF-Format)
benötigt ~4GB. Quantisierung verursacht typischerweise einen kleinen, aber akzeptablen Genauigkeits-
verlust und ist die wichtigste Technik, mit der große Modelle auf Consumer-
Hardware oder sogar mobilen Geräten laufen können.

### Kontextfenster
Das Kontextfenster ist die maximale Anzahl an Tokens, die ein Modell auf einmal verarbeiten kann,
einschließlich Prompt und generierter Antwort. GPT-3.5 hatte ein 4,096-Token-
Fenster; GPT-4 Turbo und Claude 3 unterstützen 128,000 Tokens; Gemini 1.5 Pro
unterstützt 1,000,000 Tokens. Ein größeres Kontextfenster ermöglicht es dem Modell, „mehr“
von einer Konversation oder einem Dokument gleichzeitig zu „sehen“, was die Kohärenz über lange
Austausche hinweg verbessert.

### RLHF (Reinforcement Learning from Human Feedback)
RLHF ist die Trainingstechnik, die ein Basis-Sprachmodell (das
nur das nächste Token vorhersagt) in einen Assistenten verwandelt, der Anweisungen befolgt und
hilfreich agiert. Menschliche Bewerter bewerten Modellausgaben, ein Reward-Modell wird
auf ihren Präferenzen trainiert, und das Sprachmodell wird anschließend mithilfe von Reinforcement Learning
gegen dieses Reward-Modell optimiert. ChatGPT, Claude und Gemini verwenden alle
Varianten von RLHF oder ähnlichen Alignment-Techniken (z. B. Constitutional AI,
Direct Preference Optimisation).

### Transformer-Architektur
Der Transformer ist die neuronale Netzwerkarchitektur, die allen modernen LLMs zugrunde liegt.
Eingeführt im Paper von 2017 „Attention Is All You Need“ von Vaswani et al.,
verwendet er Self-Attention-Mechanismen, um alle Tokens parallel statt
sequentiell zu verarbeiten. Encoder-only-Transformer (BERT) werden für Understanding-Aufgaben verwendet;
Decoder-only-Transformer (GPT, Llama, Mistral) werden für Generierungsaufgaben verwendet;
Encoder-Decoder-Transformer (T5, BART) werden für Übersetzung und Zusammenfassung verwendet.

### Embeddings und Vektor-Datenbanken
Embeddings sind dichte numerische Repräsentationen von Text (oder Bildern), die von
einem neuronalen Netzwerk erzeugt werden. Semantisch ähnliche Texte haben Embeddings, die im
Vektorraum nahe beieinander liegen. Vektor-Datenbanken (ChromaDB, Pinecone, Weaviate, Qdrant) speichern
diese Embeddings und unterstützen eine schnelle approximate-nearest-neighbour-Suche. Sie bilden
das Speicher-Rückgrat von RAG-Systemen, einschließlich der Cold-Memory-Schicht von Potato.ai.
