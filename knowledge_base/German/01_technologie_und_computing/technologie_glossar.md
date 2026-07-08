<!-- 
This file was automatically translated from English to German.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
Für Verbesserungen der Genauigkeit bitten wir um Beiträge via Pull Requests.
-->

# Technologie-Glossar

Ein Referenz-Glossar covering AI-Modelle, Hardware, Benchmarks und Kernkonzepte
in der modernen KI- und Datenverarbeitungslandschaft.

---

## KI-Sprachmodelle und Assistenten

### ChatGPT
ChatGPT ist ein von OpenAI entwickelter KI-Chatbot, der erstmals im November 2022 veröffentlicht wurde.
Er basiert auf der GPT-Reihe von großen Sprachmodellen (LLMs). ChatGPT ist eines
der am schnellsten wachsenden consumer-KI-Produkte in der Geschichte und erreichte innerhalb von zwei Monaten nach dem Launch 100 Millionen
Nutzer. Es unterstützt textbasierte Konversationen, Code-Generierung, Zusammenfassungen und kreatives Schreiben. Bezahlte Tarife bieten Zugang zu
leistungsstärkeren Modellen wie GPT-4 und GPT-4o.

### GPT (Generative Pre-trained Transformer)
GPT ist eine Familie von großen Sprachmodellen, die von OpenAI erstellt wurde. Die Architektur
verwendet einen nur-Decoder-Transformer, der mit einem Next-Token-Prediction-Ziel auf
massiven Textkorpora trainiert wurde. Wichtige Versionen umfassen GPT-2 (2019, 1,5 Mrd. Parameter, bekannt
für die „zu gefährlich zur Veröffentlichung"-Publicity), GPT-3 (2020, 175 Mrd. Parameter, weit verbreitet
über die API genutzt), GPT-3.5 (das Rückgrat des ursprünglichen ChatGPT) und GPT-4
(2023, multimodal, Leistung nahe dem menschlichen Expertenniveau bei vielen Benchmarks).

### Claude
Claude ist ein von Anthropic entwickelter KI-Assistent. Er ist benannt nach Claude
Shannon, dem Begründer der Informationstheorie. Anthropic wurde von ehemaligen
OpenAI-Forschern gegründet und konzentriert sich auf „Constitutional AI" — eine Technik, um
Modelle sicherer zu machen, indem sie darauf trainiert werden, einer Reihe von Prinzipien zu folgen. Claude-Modelle
(Claude 1, 2, 3 Haiku / Sonnet / Opus) sind bekannt für lange Kontextfenster (bis
zu 200.000 Tokens), nuanciertes Reasoning und reduzierte schädliche Ausgaben im Vergleich zu
Basis-LLMs.

### Gemini
Gemini ist Google DeepMinds Familie von multimodalen KI-Modellen, angekündigt im
Dezember 2023. Gemini ist nativ multimodal — von Grund auf gleichzeitig auf
Text, Bilder, Audio und Video trainiert, im Gegensatz zu früheren Modellen, denen
Modalitäten durch Fine-Tuning hinzugefügt wurden. Versionen umfassen Gemini Nano (on-device),
Gemini Flash (schnell, kosteneffizient) und Gemini Ultra (höchste Leistungsfähigkeit).
Gemini betreibt Googles KI-Chatbot Bard (umbenannt in Gemini) und Google Search AI
Overviews.

### Phi-3-mini
Phi-3-mini ist ein kleines Sprachmodell (SLM), das von Microsoft mit 3,8 Mrd.
Parametern entwickelt wurde. Es wurde im April 2024 veröffentlicht. Im Gegensatz zu den meisten großen Modellen
wurde Phi-3-mini auf einem sorgfältig kuratierten „Lehrbuch-quality" Datensatz trainiert — eine Technik,
die von Microsoft Research pionierhaft entwickelt wurde — die Datenqualität über rohes Volumen priorisiert.
Trotz seiner viel kleineren Größe im Vergleich zu GPT-4 oder Claude 3 Opus erreicht oder
übertrifft Phi-3-mini Modelle, die ein Vielfaches größer sind, bei Reasoning-Benchmarks wie MMLU und
HumanEval. Es unterstützt ein 4k-Token-Kontextfenster in seiner Basisvariante und ein 128k-
Fenster in der Long-Context-Variante. Phi-3-mini kann auf einer einzelnen Consumer-GPU
oder sogar on-device auf einem modernen Smartphone mit ausreichend RAM laufen.

### Llama (Meta AI)
Llama (Large Language Model Meta AI) ist eine Open-Weights-Familie von Modellen,
die von Meta veröffentlicht wurde. Llama 2 (2023) wurde für Forschung und kommerzielle Nutzung
mit Größen von 7B bis 70B Parametern veröffentlicht. Llama 3 (2024) verbesserte
die Leistung erheblich, mit Modellen von 8B bis 70B (und später 400B+).
Da die Gewichte öffentlich herunterladbar sind, bilden Llama-Modelle die Grundlage
für ein großes Ökosystem von feinabgestimmten Varianten (Mistral, Alpaca, Vicuna usw.)
und werden häufig für lokale/private KI-Deployments verwendet.

### Mistral
Mistral AI ist ein französisches KI-Unternehmen, das offene und proprietäre LLMs entwickelt.
Mistral 7B (2023) demonstrierte, dass ein 7B-Parameter-Modell die
Leistung viel größerer Modelle mit effizienten Techniken wie Sliding-
Window-Attention und Grouped-Query-Attention erreichen kann. Mixtral 8x7B (2024) ist ein Mixture-
of-Experts-Modell — es leitet jedes Token an eine Teilmenge von 8 Expertennetzwerken weiter
und erreicht GPT-3.5-Leistung bei geringeren Rechenkosten.
Mistrals Modelle sind vollständig Open-Weight und können lokal ausgeführt werden.

---

## GPU-Hardware und Grafikkarten

### GPU (Graphics Processing Unit)
Eine GPU ist ein Prozessor, der für massiv parallele Berechnungen entwickelt wurde. Ursprünglich
für das Rendering von 3D-Grafiken gebaut, sind GPUs für KI/ML-Training
und Inferenz unverzichtbar geworden, da sie Tausende von Gleitkommaoperationen
gleichzeitig mit Tausenden von kleinen Kernen durchführen können. Die beiden wichtigsten GPU-Hersteller
für KI sind NVIDIA und AMD.

### NVIDIA GeForce RTX-Serie
Die RTX (Ray Tracing Texel eXtreme)-Serie ist NVIDIAs Consumer-GPU-Linie. Die RTX
30xx (Ampere, 2020) und RTX 40xx (Ada Lovelace, 2022) Generationen umfassen
dedizierte Tensor Cores zur Beschleunigung von KI-Operationen. VRAM (Video-RAM) ist
kritisch für das lokale Ausführen von KI-Modellen — eine 8GB-GPU kann 7B-Parameter-
Modelle in 4-Bit-Quantisierung handhaben; eine 24GB-GPU kann 70B-Modelle in 4-Bit handhaben.

### NVIDIA A-Serie und H-Serie (Datenzentrum)
Der A100 (Ampere, 2020) und H100 (Hopper, 2022) sind NVIDIAs professionelle KI-
Beschleuniger. Ein H100 hat bis zu 80GB HBM3-Speicher und ist der Standard-
Hardware hinter den meisten groß angelegten LLM-Trainings heutzutage. Diese GPUs kosten $25.000–
$40.000 pro Stück, bieten aber das 10–30-fache des KI-Durchsatzes von Consumer-RTX-Karten.

### AMD Radeon RX-Serie
AMDs Consumer-GPU-Linie. Die RX 7900 XTX (2022) hat 24GB VRAM und kann
lokale LLMs über ROCm (AMDs GPU-Compute-Stack) ausführen. AMD-GPUs sind für KI-Frameworks im Allgemeinen weniger
gut unterstützt als NVIDIA, obwohl sich die Unterstützung verbessert.

### Intel Arc
Intel Arc ist Intels Produktlinie für diskrete GPUs, die ab 2022 veröffentlicht wurde. Arc-
GPUs unterstützen XeSS (Intels Super-Sampling) und haben begrenzte, aber wachsende Unterstützung
für KI-Inferenz-Aufgaben über OpenVINO und IPEX-LLM-Frameworks.

### ARK Intel (ark.intel.com)
ARK ist Intels offizielle Produktspezifikationsdatenbank unter ark.intel.com. Sie
bietet detaillierte technische Spezifikationen für jedes Intel-CPU-, GPU-, FPGA- und
NUC-Produkt, einschließlich Kernanzahlen, Taktraten, TDP, unterstützte Speichertypen
und Befehlssatz-Features. Wenn man hört „check ARK for specs", bedeutet dies,
diese Datenbank für autoritative Hardware-Informationen zu besuchen.

---

## KI-Leistungsbenchmarks

### MMLU (Massive Multitask Language Understanding)
MMLU ist ein Benchmark, der das LLM-Wissen über 57 akademische Fächer testet, einschließlich
Mathematik, Geschichte, Recht, Medizin und Informatik. Er besteht aus
Multiple-Choice-Fragen, die von echten universitären Prüfungen stammen. Eine Punktzahl von
70% entspricht ungefähr dem Niveau eines menschlichen Bachelorabsolventen; GPT-4 und Claude 3 erzielen über 86%.
Phi-3-mini erzielt trotz seiner geringen Größe etwa 70%.

### HumanEval
HumanEval ist OpenAIs Benchmark für Code-Generierung. Er besteht aus 164 Python-
Programmieraufgaben mit automatisierten Testfällen. Modelle werden anhand von
pass@k gemessen — der Wahrscheinlichkeit, dass mindestens eine von k generierten Lösungen alle
Tests besteht. GPT-4 erzielt ~87% (pass@1); ein gut abgestimmtes 7B-Modell kann ~50–60% erreichen.

### HellaSwag
HellaSwag ist ein Commonsense-Reasoning-Benchmark. Modellen wird ein Satz
gegeben, der eine alltägliche Aktivität beschreibt, und sie müssen die wahrscheinlichste Fortsetzung aus
vier Optionen auswählen. Die falschen Optionen sind speziell so gestaltet, dass sie plausibel, aber
subtil falsch sind. Er testet, ob ein Modell ein fundiertes Verständnis von physischen
und sozialen Situationen hat.

### ARC (AI2 Reasoning Challenge)
ARC ist ein Benchmark vom Allen Institute for AI. Er besteht aus Grundschul-
Wissenschaftsfragen, aufgeteilt in „Easy" und „Challenge" Sets. Das Challenge-Set
enthält Fragen, bei denen retrieval-basierte Methoden und einfache statistische Modelle
Schwierigkeiten haben und die mehrstufiges Reasoning erfordern.

---

## Kern-KI/ML-Konzepte

### RAG (Retrieval-Augmented Generation)
RAG ist eine Technik, die ein Retrieval-System (typischerweise eine Vektor-
Datenbank) mit einem Sprachmodell kombiniert. Anstatt sich ausschließlich auf das parametrische Wissen des Modells zu verlassen, ruft RAG zuerst relevante Dokumente aus einer externen
Wissensdatenbank ab und fügt sie dann in den Kontext des Modells ein. Dies ermöglicht dem
Modell, Fragen zu aktuellen oder domänenspezifischen Informationen zu beantworten,
ohne neu trainiert zu werden. Potato.ai verwendet eine Form von RAG — es ruft aus seiner KB
ab und fügt die Ergebnisse in den Kontext ein, bevor es eine Antwort generiert.

### Fine-Tuning
Fine-Tuning ist der Prozess, bei dem ein vortrainiertes Modell weiterhin auf einem
kleineren, domänenspezifischen Datensatz trainiert wird. Dies passt die Gewichte des Modells für eine
bestimmte Aufgabe oder Domäne an. Zum Beispiel könnte ein Basis-LLM auf
medizinischen Aufzeichnungen feinabgestimmt werden, um einen medizinischen Q&A-Assistenten zu erstellen. Fine-Tuning ist
rechenintensiv, aber viel günstiger als Training von Grund auf.

### Quantisierung
Quantisierung reduziert die numerische Präzision von Modellgewichten (z.B. von 32-Bit-
Float zu 4-Bit-Integer). Dies reduziert den Speicherbedarf drastisch — ein 7B-Modell
in 16-Bit-Präzision benötigt ~14GB VRAM; dasselbe Modell in 4-Bit (GGUF-Format)
benötigt ~4GB. Quantisierung verursacht typischerweise eine kleine, aber akzeptable Genauigkeits-
Degradation und ist die Haupttechnik, die es großen Modellen ermöglicht, auf Consumer-
Hardware oder sogar mobilen Geräten zu laufen.

### Kontextfenster
Das Kontextfenster ist die maximale Anzahl von Tokens, die ein Modell gleichzeitig verarbeiten kann,
einschließlich sowohl des Prompts als auch der generierten Antwort. GPT-3.5 hatte ein 4.096-Token-
Fenster; GPT-4 Turbo und Claude 3 unterstützen 128.000 Tokens; Gemini 1.5 Pro
unterstützt 1.000.000 Tokens. Ein größeres Kontextfenster ermöglicht es dem Modell, mehr
von einer Konversation oder einem Dokument auf einmal zu „sehen", was die Kohärenz über lange
Austausche hinweg verbessert.

### RLHF (Reinforcement Learning from Human Feedback)
RLHF ist die Trainingstechnik, die ein Basis-Sprachmodell (das
lediglich das nächste Token vorhersagt) in einen Assistenten verwandelt, der Anweisungen befolgt und
sich hilfreich verhält. Menschliche Bewerter bewerten Modellausgaben, ein Reward-Modell wird auf
ihren Präferenzen trainiert, und das Sprachmodell wird dann gegen dieses
Reward-Modell mittels Reinforcement Learning optimiert. ChatGPT, Claude und Gemini verwenden alle
Varianten von RLHF oder ähnliche Alignment-Techniken (z.B. Constitutional AI,
Direct Preference Optimization).

### Transformer-Architektur
Der Transformer ist die neuronale Netzwerkarchitektur, die allen modernen LLMs zugrunde liegt.
Eingeführt im 2017er Paper „Attention Is All You Need" von Vaswani et al., verwendet er
Self-Attention-Mechanismen, um alle Tokens parallel statt sequenziell zu verarbeiten. Nur-Encoder-Transformer (BERT) werden für Verständnisaufgaben verwendet;
nur-Decoder-Transformer (GPT, Llama, Mistral) werden für Generierungsaufgaben verwendet;
Encoder-Decoder-Transformer (T5, BART) werden für Übersetzung und Zusammenfassung verwendet.

### Embeddings und Vektordatenbanken
Embeddings sind dichte numerische Darstellungen von Text (oder Bildern), die von
einem neuronalen Netzwerk erzeugt werden. Semantisch ähnliche Texte haben Embeddings, die im
Vektorraum nahe beieinander liegen. Vektordatenbanken (ChromaDB, Pinecone, Weaviate, Qdrant) speichern
diese Embeddings und unterstützen schnelle approximative Nearest-Neighbour-Suche. Sie sind
das Speicher-Rückgrat von RAG-Systemen, einschließlich Potato.ai's Cold-Memory-Layer.
