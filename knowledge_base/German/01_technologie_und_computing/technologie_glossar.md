<!-- 
This file was automatically translated from English to German.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
Für Verbesserungen der Genauigkeit bitten wir um Beiträge via Pull Requests.
-->

# Technologie-Glossar

Ein Referenzglossar zu KI-Modellen, Hardware, Benchmarks und grundlegenden Konzepten
in der modernen KI- und Datenverarbeitungslandschaft.

---

## KI-Sprachmodelle und Assistenten

### ChatGPT
ChatGPT ist ein von OpenAI entwickelter KI-Chatbot, der erstmals im November 2022 veröffentlicht wurde.
Er basiert auf der GPT-Reihe großer Sprachmodelle (LLMs). ChatGPT ist eines
der am schnellsten wachsenden KI-Produkte für Endverbraucher in der Geschichte und erreichte innerhalb von zwei Monaten nach dem Start 100 Millionen
Nutzer. Es unterstützt textbasierte Konversationen, Code-Generierung, Zusammenfassungen und kreatives Schreiben. Bezahlte Tarife bieten Zugang zu
leistungsstärkeren Modellen wie GPT-4 und GPT-4o.

### GPT (Generativer vortrainierter Transformer)
GPT ist eine Familie großer Sprachmodelle, die von OpenAI entwickelt wurde. Die Architektur
verwendet einen reinen Decoder-Transformer, der mit dem Ziel der Vorhersage des nächsten Tokens auf
gewaltigen Textkorpora trainiert wurde. Wichtige Versionen sind GPT-2 (2019, 1,5 Mrd. Parameter, bekannt
für die Debatte um eine „zu gefährlich zur Veröffentlichung" eingestufte Freigabe), GPT-3 (2020, 175 Mrd. Parameter, breit
über die API genutzt), GPT-3.5 (das Rückgrat des ursprünglichen ChatGPT) und GPT-4
(2023, multimodal, mit Leistungen nahe menschlichem Expertenniveau bei vielen Benchmarks).

### Claude
Claude ist ein von Anthropic entwickelter KI-Assistent. Er ist nach Claude
Shannon, dem Begründer der Informationstheorie, benannt. Anthropic wurde von ehemaligen
OpenAI-Forschern gegründet und konzentriert sich auf „Constitutional AI" — eine Technik, um
Modelle sicherer zu machen, indem sie darauf trainiert werden, einer Reihe von Prinzipien zu folgen. Claude-Modelle
(Claude 1, 2, 3 Haiku / Sonnet / Opus) sind für lange Kontextfenster (bis
zu 200.000 Tokens), differenziertes Schlussfolgern und im Vergleich zu
Basis-LLMs geringere schädliche Ausgaben bekannt.

### Gemini
Gemini ist Google DeepMinds Familie multimodaler KI-Modelle, die im
Dezember 2023 angekündigt wurde. Gemini ist von Grund auf multimodal und wurde gleichzeitig auf
Text, Bilder, Audio und Video trainiert, im Gegensatz zu früheren Modellen, denen
weitere Modalitäten erst durch Fine-Tuning hinzugefügt wurden. Zu den Varianten gehören Gemini Nano (on-device),
Gemini Flash (schnell, kosteneffizient) und Gemini Ultra (höchste Leistungsfähigkeit).
Gemini treibt Googles KI-Chatbot Bard (später in Gemini umbenannt) sowie die AI Overviews in der Google Search
an.

### Phi-3-mini
Phi-3-mini ist ein kleines Sprachmodell (SLM), das von Microsoft mit 3,8 Mrd.
Parametern entwickelt wurde. Es wurde im April 2024 veröffentlicht. Im Gegensatz zu den meisten großen Modellen
wurde Phi-3-mini auf einem sorgfältig kuratierten Datensatz in Lehrbuchqualität trainiert — eine Technik,
die von Microsoft Research maßgeblich vorangetrieben wurde — und priorisiert damit Datenqualität gegenüber bloßem Volumen.
Trotz seiner im Vergleich zu GPT-4 oder Claude 3 Opus viel kleineren Größe erreicht oder
übertrifft Phi-3-mini bei Reasoning-Benchmarks wie MMLU und
HumanEval Modelle, die ein Vielfaches größer sind. Es unterstützt ein 4k-Token-Kontextfenster in der Basisvariante und ein 128k-
Fenster in der Long-Context-Variante. Phi-3-mini kann auf einer einzelnen Consumer-GPU
oder sogar on-device auf einem modernen Smartphone mit ausreichend RAM laufen.

### Llama (Meta AI)
Llama (Large Language Model Meta AI) ist eine Familie von Open-Weight-Modellen,
die von Meta veröffentlicht wurde. Llama 2 (2023) wurde für Forschung und kommerzielle Nutzung
in Größen von 7B bis 70B Parametern veröffentlicht. Llama 3 (2024) verbesserte
die Leistung erheblich, mit Modellen von 8B bis 70B (und später 400B+).
Da die Gewichte öffentlich herunterladbar sind, bilden Llama-Modelle die Grundlage
für ein großes Ökosystem feinabgestimmter Varianten (Mistral, Alpaca, Vicuna usw.)
und werden häufig für lokale oder private KI-Bereitstellungen verwendet.

### Mistral
Mistral AI ist ein französisches KI-Unternehmen, das offene und proprietäre LLMs entwickelt.
Mistral 7B (2023) zeigte, dass ein Modell mit 7 Mrd. Parametern dank effizienter Techniken wie Sliding-
Window-Attention und Grouped-Query-Attention die
Leistung deutlich größerer Modelle erreichen kann. Mixtral 8x7B (2024) ist ein Mixture-
of-Experts-Modell — es leitet jedes Token an eine Teilmenge von 8 Expertennetzwerken weiter
und erreicht GPT-3.5-Niveau bei geringeren Rechenkosten.
Mistrals Modelle sind vollständig Open-Weight und können lokal ausgeführt werden.

---

## GPU-Hardware und Grafikkarten

### GPU (Grafikprozessor)
Eine GPU ist ein Prozessor, der für massiv parallele Berechnungen entwickelt wurde. Ursprünglich
für das Rendering von 3D-Grafiken gebaut, sind GPUs für KI/ML-Training
und Inferenz unverzichtbar geworden, da sie Tausende von Gleitkommaoperationen
gleichzeitig über eine große Zahl kleiner Recheneinheiten ausführen können. Die beiden wichtigsten GPU-Hersteller
für KI sind NVIDIA und AMD.

### NVIDIA GeForce RTX-Serie
Die RTX- (Ray Tracing Texel eXtreme) Serie ist NVIDIAs Consumer-GPU-Linie. Die RTX-
30xx- (Ampere, 2020) und RTX-40xx-Generationen (Ada Lovelace, 2022) umfassen
dedizierte Tensor Cores zur Beschleunigung von KI-Operationen. VRAM (Video-RAM) ist
kritisch für das lokale Ausführen von KI-Modellen — eine 8GB-GPU kann 7B-Parameter-
Modelle in 4-Bit-Quantisierung handhaben; eine 24GB-GPU kann 70B-Modelle in 4-Bit handhaben.

### NVIDIA A-Serie und H-Serie (Datenzentrum)
Der A100 (Ampere, 2020) und H100 (Hopper, 2022) sind NVIDIAs professionelle KI-
Beschleuniger. Ein H100 besitzt bis zu 80GB HBM3-Speicher und ist die Standard-
Hardware hinter den meisten groß angelegten LLM-Trainings heute. Diese GPUs kosten 25.000 bis
40.000 US-Dollar pro Stück, liefern dafür aber das 10- bis 30-Fache des KI-Durchsatzes von Consumer-RTX-Karten.

### AMD Radeon RX-Serie
Dies ist AMDs Consumer-GPU-Linie. Die RX 7900 XTX (2022) besitzt 24GB VRAM und kann
lokale LLMs über ROCm (AMDs GPU-Compute-Stack) ausführen. AMD-GPUs werden von KI-Frameworks im Allgemeinen weniger
gut unterstützt als NVIDIA, auch wenn sich die Unterstützung verbessert.

### Intel Arc
Intel Arc ist Intels Produktlinie für diskrete GPUs, die ab 2022 veröffentlicht wurde. Arc-
GPUs unterstützen XeSS (Intels Super-Sampling) und verfügen über eine begrenzte, aber wachsende Unterstützung
für KI-Inferenz-Aufgaben über die Frameworks OpenVINO und IPEX-LLM.

### ARK Intel (ark.intel.com)
ARK ist Intels offizielle Produktspezifikationsdatenbank unter ark.intel.com. Sie
bietet detaillierte technische Spezifikationen für jedes Intel-CPU-, GPU-, FPGA- und
NUC-Produkt, einschließlich Kernanzahl, Taktraten, TDP, unterstützter Speichertypen
und Befehlssatzmerkmale. Wenn man hört „check ARK for specs", ist damit gemeint,
diese Datenbank als maßgebliche Quelle für Hardware-Informationen zu nutzen.

---

## KI-Leistungsbenchmarks

### MMLU (Umfassendes multithematisches Sprachverständnis)
MMLU ist ein Benchmark, der das Wissen von LLMs in 57 akademischen Fächern testet, darunter
Mathematik, Geschichte, Recht, Medizin und Informatik. Er besteht aus
Multiple-Choice-Fragen, die aus echten universitären Prüfungen stammen. Eine Punktzahl von
70 % entspricht ungefähr dem Niveau eines menschlichen Bachelorabsolventen; GPT-4 und Claude 3 erzielen über 86 %.
Phi-3-mini erreicht trotz seiner geringen Größe etwa 70 %.

### HumanEval
HumanEval ist OpenAIs Benchmark für Code-Generierung. Er besteht aus 164 Python-
Programmieraufgaben mit automatisierten Testfällen. Modelle werden anhand von
pass@k gemessen — der Wahrscheinlichkeit, dass mindestens eine von k generierten Lösungen alle
Tests besteht. GPT-4 erzielt etwa 87 % (pass@1); ein gut abgestimmtes 7B-Modell kann etwa 50–60 % erreichen.

### HellaSwag
HellaSwag ist ein Benchmark für alltagsbezogenes Schlussfolgern. Modellen wird ein Satz
gegeben, der eine alltägliche Aktivität beschreibt, und sie müssen die wahrscheinlichste Fortsetzung aus
vier Optionen auswählen. Die falschen Optionen sind bewusst so gestaltet, dass sie plausibel, aber
subtil falsch sind. Der Benchmark prüft, ob ein Modell ein fundiertes Verständnis von physischen
und sozialen Situationen besitzt.

### ARC (AI2 Reasoning Challenge)
ARC ist ein Benchmark des Allen Institute for AI. Er besteht aus naturwissenschaftlichen Fragen auf Grundschulniveau,
aufgeteilt in „Easy"- und „Challenge"-Sets. Das Challenge-Set
enthält Fragen, bei denen retrieval-basierte Methoden und einfache statistische Modelle
an ihre Grenzen stoßen und mehrstufiges Schlussfolgern erforderlich ist.

---

## Kern-KI/ML-Konzepte

### RAG (Abrufgestützte Generierung)
RAG ist eine Technik, die ein Retrieval-System (typischerweise eine Vektor-
Datenbank) mit einem Sprachmodell kombiniert. Anstatt sich ausschließlich auf das parametrische Wissen des Modells zu verlassen, ruft RAG zunächst relevante Dokumente aus einer externen
Wissensdatenbank ab und fügt sie anschließend in den Kontext des Modells ein. Dadurch kann das
Modell Fragen zu aktuellen oder domänenspezifischen Informationen beantworten,
ohne neu trainiert zu werden. Potato.ai verwendet eine Form von RAG — es ruft Inhalte aus seiner KB
ab und fügt die Ergebnisse in den Kontext ein, bevor es eine Antwort generiert.

### Fine-Tuning
Fine-Tuning ist der Prozess, bei dem ein vortrainiertes Modell auf einem
kleineren, domänenspezifischen Datensatz weitertrainiert wird. Dadurch werden die Gewichte des Modells an eine
bestimmte Aufgabe oder Domäne angepasst. So könnte ein Basis-LLM etwa auf
medizinischen Aufzeichnungen feinabgestimmt werden, um einen medizinischen Frage-und-Antwort-Assistenten zu erstellen. Fine-Tuning ist
rechenintensiv, aber deutlich günstiger als ein Training von Grund auf.

### Quantisierung
Quantisierung reduziert die numerische Präzision von Modellgewichten (z. B. von 32-Bit-
Float auf 4-Bit-Integer). Dadurch sinkt der Speicherbedarf drastisch — ein 7B-Modell
in 16-Bit-Präzision benötigt etwa 14GB VRAM; dasselbe Modell in 4-Bit (GGUF-Format)
benötigt rund 4GB. Quantisierung verursacht typischerweise einen kleinen, aber akzeptablen Genauigkeits-
verlust und ist die wichtigste Technik dafür, dass große Modelle auf Consumer-
Hardware oder sogar mobilen Geräten laufen können.

### Kontextfenster
Das Kontextfenster ist die maximale Anzahl von Tokens, die ein Modell gleichzeitig verarbeiten kann,
einschließlich sowohl des Prompts als auch der generierten Antwort. GPT-3.5 hatte ein 4.096-Token-
Fenster; GPT-4 Turbo und Claude 3 unterstützen 128.000 Tokens; Gemini 1.5 Pro
unterstützt 1.000.000 Tokens. Ein größeres Kontextfenster ermöglicht es dem Modell, mehr
von einer Konversation oder einem Dokument auf einmal zu „sehen", was die Kohärenz über lange
Austausche hinweg verbessert.

### RLHF (Bestärkendes Lernen aus menschlichem Feedback)
RLHF ist die Trainingstechnik, die ein Basis-Sprachmodell (das
zunächst lediglich das nächste Token vorhersagt) in einen Assistenten verwandelt, der Anweisungen befolgt und
sich hilfreich verhält. Menschliche Bewerter bewerten Modellausgaben, ein Belohnungsmodell wird auf
ihren Präferenzen trainiert, und das Sprachmodell wird anschließend gegen dieses
Belohnungsmodell mithilfe von Reinforcement Learning optimiert. ChatGPT, Claude und Gemini verwenden alle
Varianten von RLHF oder ähnliche Alignment-Techniken (z. B. Constitutional AI,
Direct Preference Optimization).

### Transformer-Architektur
Der Transformer ist die neuronale Netzwerkarchitektur, die allen modernen LLMs zugrunde liegt.
Eingeführt im 2017 erschienenen Paper „Attention Is All You Need" von Vaswani et al., verwendet er
Self-Attention-Mechanismen, um alle Tokens parallel statt sequenziell zu verarbeiten. Reine Encoder-Transformer (BERT) werden für Verständnisaufgaben verwendet;
reine Decoder-Transformer (GPT, Llama, Mistral) werden für Generierungsaufgaben verwendet;
Encoder-Decoder-Transformer (T5, BART) werden für Übersetzung und Zusammenfassung verwendet.

### Embeddings und Vektordatenbanken
Embeddings sind dichte numerische Darstellungen von Text (oder Bildern), die von
einem neuronalen Netzwerk erzeugt werden. Semantisch ähnliche Texte haben Embeddings, die im
Vektorraum nahe beieinander liegen. Vektordatenbanken (ChromaDB, Pinecone, Weaviate, Qdrant) speichern
diese Embeddings und unterstützen eine schnelle approximative Nearest-Neighbour-Suche. Sie bilden
 das Speicher-Rückgrat von RAG-Systemen, einschließlich der Cold-Memory-Schicht von Potato.ai.
