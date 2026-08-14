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
# Technologie-Glossar
Ein Referenzglossar zu KI-Modellen, Hardware, Benchmarks und Kernkonzepten
in der modernen KI- und Computerlandschaft.
---

## KI-Sprachmodelle und Assistenten
### ChatGPT
ChatGPT ist ein von OpenAI entwickelter KI-Chatbot, der erstmals im November 2022 veröffentlicht wurde.
Es basiert auf der GPT-Serie großer Sprachmodelle (LLMs). ChatGPT ist eines
eines der am schnellsten wachsenden KI-Produkte für Verbraucher in der Geschichte und erreicht 100 Millionen
Benutzer innerhalb von zwei Monaten nach dem Start. Es unterstützt textbasierte Konversation und Code
Generierung, Zusammenfassung und kreatives Schreiben. Bezahlte Stufen bieten Zugriff auf
leistungsstärkere Modelle wie GPT-4 und GPT-4o.
### GPT (Generative Pre-Trained Transformer)
GPT ist eine Familie großer Sprachmodelle, die von OpenAI erstellt wurden. Die Architektur
verwendet einen Nur-Decoder-Transformer, der mit einem nächsten Token-Vorhersageziel trainiert wurde
riesige Textkorpora. Zu den wichtigsten Versionen gehört GPT-2 (2019, 1,5B-Parameter, bemerkenswert
für „zu gefährlich zum Freigeben“-Werbung), GPT-3 (2020, 175B Parameter, weithin
über die API verwendet), GPT-3.5 (das Rückgrat des ursprünglichen ChatGPT) und GPT-4
(2023, multimodal, Leistung nahe dem menschlichen Expertenniveau bei vielen Benchmarks).
### Claude
Claude ist ein von Anthropic entwickelter KI-Assistent. Es ist nach Claude benannt
Shannon, der Begründer der Informationstheorie. Anthropic wurde von ehemaligen gegründet
OpenAI-Forscher konzentrieren sich auf „verfassungsmäßige KI“ – eine Technik, die es zu entwickeln gilt
Machen Sie Modelle sicherer, indem Sie ihnen beibringen, eine Reihe von Grundsätzen zu befolgen. Claude-Modelle
(Claude 1, 2, 3 Haiku / Sonett / Opus) sind bekannt für lange Kontextfenster (oben).
bis zu 200.000 Token), differenziertere Argumentation und reduzierter schädlicher Output im Vergleich zu
Basis-LLMs.
### Zwillinge
Gemini ist die Familie multimodaler KI-Modelle von Google DeepMind, angekündigt in
Dezember 2023. Zwillinge sind von Natur aus multimodal – von Grund auf trainiert
Text, Bilder, Audio und Video gleichzeitig, anders als bei früheren Modellen
durch Feinabstimmung hinzugefügte Modalitäten. Zu den Versionen gehören Gemini Nano (auf dem Gerät),
Gemini Flash (schnell, kosteneffizient) und Gemini Ultra (höchste Leistungsfähigkeit).
Gemini unterstützt Googles KI-Chatbot Bard (umbenannt in Gemini) und Google Search AI
Übersichten.
### Phi-3-mini
Phi-3-mini ist ein kleines Sprachmodell (SLM), das von Microsoft mit 3.8B entwickelt wurde
Parameter. Es wurde im April 2024 veröffentlicht. Im Gegensatz zu den meisten großen Modellen ist Phi-3-mini
wurde anhand eines sorgfältig kuratierten Datensatzes in „Lehrbuchqualität“ geschult – einer Technik
entwickelt von Microsoft Research – das der Datenqualität Vorrang vor dem Rohvolumen einräumt.
Obwohl Phi-3-mini viel kleiner als GPT-4 oder Claude 3 Opus ist, entspricht es bzw
übertrifft Modelle um ein Vielfaches größer bei Argumentations-Benchmarks wie MMLU und
HumanEval. Es unterstützt ein 4K-Token-Kontextfenster in seiner Basisvariante und ein 128K-Token-Kontextfenster
Fenster in der Langkontext-Variante. Phi-3-mini kann auf einer einzelnen Consumer-GPU ausgeführt werden
oder sogar auf dem Gerät auf einem modernen Smartphone mit ausreichend RAM.
### Lama (Meta-KI)
Llama (Large Language Model Meta AI) ist eine Modellfamilie mit offenen Gewichten
veröffentlicht von Meta. Llama 2 (2023) wurde für Forschungs- und kommerzielle Zwecke freigegeben
mit Größen von 7B bis 70B Parametern. Lama 3 (2024) verbessert
Leistung erheblich, mit Modellen von 8B bis 70B (und später 400B+).
Da die Gewichte öffentlich herunterladbar sind, bilden Lama-Modelle die Grundlage
für ein großes Ökosystem fein abgestimmter Varianten (Mistral, Alpaka, Vicuna usw.)
und werden häufig für lokale/private KI-Bereitstellungen verwendet.
### Mistral
Mistral AI ist ein französisches KI-Unternehmen, das offene und proprietäre LLMs entwickelt.
Mistral 7B (2023) hat gezeigt, dass ein 7B-Parametermodell mit dem übereinstimmen kann
Leistung viel größerer Modelle mithilfe effizienter Techniken wie Gleiten
Fensteraufmerksamkeit und Aufmerksamkeit für gruppierte Abfragen. Mixtral 8x7B (2023) ist eine Mischung-
Expertenmodell – es leitet jedes Token an eine Teilmenge von 8 Expertennetzwerken weiter,
Erzielen einer Leistung auf GPT-3.5-Niveau bei gleichzeitig geringerem Rechenaufwand.
Die Modelle von Mistral sind vollständig offengewichtig und können lokal betrieben werden.
---

## GPU-Hardware und Grafikkarten
### GPU (Grafikverarbeitungseinheit)
Eine GPU ist ein Prozessor, der für massiv parallele Berechnungen ausgelegt ist. Ursprünglich
GPUs wurden für die Darstellung von 3D-Grafiken entwickelt und sind für das KI/ML-Training unverzichtbar geworden
und Inferenz, da sie Tausende von Gleitkommaoperationen ausführen können
Gleichzeitige Verwendung von Tausenden kleiner Kerne. Die beiden größten GPU-Hersteller
für KI sind NVIDIA und AMD.
### NVIDIA GeForce RTX-Serie
Die RTX-Serie (Ray Tracing Texel eXtreme) ist NVIDIAs Consumer-GPU-Reihe. RTX
Zu den Generationen 30xx (Ampere, 2020) und RTX 40xx (Ada Lovelace, 2022) gehören
dedizierte Tensorkerne zur Beschleunigung von KI-Operationen. VRAM (Video-RAM) ist
Entscheidend für die lokale Ausführung von KI-Modellen – eine 8-GB-GPU kann 7B-Parameter verarbeiten
Modelle in 4-Bit-Quantisierung; Eine 24-GB-GPU kann 70B-Modelle in 4-Bit verarbeiten.
### NVIDIA A-Serie und H-Serie (Rechenzentrum)
Der A100 (Ampere, 2020) und der H100 (Hopper, 2022) sind NVIDIAs professionelle KI
Beschleuniger. Ein H100 verfügt standardmäßig über bis zu 80 GB HBM3-Speicher
Hardware, die heute hinter den meisten groß angelegten LLM-Schulungen steckt. Diese GPUs kosten 25.000 US-Dollar –
40.000 US-Dollar pro Stück, bieten aber den 10- bis 30-fachen KI-Durchsatz von RTX-Karten für Endverbraucher.
### AMD Radeon RX-Serie
AMDs Consumer-GPU-Reihe. Die RX 7900 XTX (2022) verfügt über 24 GB VRAM und kann ausgeführt werden
lokale LLMs über ROCm (AMDs GPU-Compute-Stack). AMD-GPUs sind im Allgemeinen weniger
besser unterstützt als NVIDIA für KI-Frameworks, obwohl die Unterstützung besser wird.
### Intel Arc
Intel Arc ist die diskrete GPU-Produktlinie von Intel, die ab 2022 auf den Markt kommt. Arc
GPUs unterstützen XeSS (Intels Supersampling) und werden nur begrenzt, aber zunehmend unterstützt
für KI-Inferenzaufgaben über OpenVINO- und IPEX-LLM-Frameworks.
### ARK Intel (ark.intel.com)
ARK ist Intels offizielle Produktspezifikationsdatenbank unter ark.intel.com. Es
Bietet detaillierte technische Spezifikationen für jede Intel-CPU, GPU, FPGA und
NUC-Produkt, einschließlich Kernanzahl, Taktraten, TDP, unterstützte Speichertypen,
und Befehlssatzfunktionen. Wenn Sie „Prüfen Sie ARK auf Spezifikationen“ hören, bedeutet das
Besuchen Sie diese Datenbank, um verlässliche Hardwareinformationen zu erhalten.
---

## KI-Leistungsbenchmarks
### MMLU (Massive Multitask Language Understanding)
MMLU ist ein Benchmark, der LLM-Wissen in 57 akademischen Fächern testet, darunter
Mathematik, Geschichte, Jura, Medizin und Informatik. Es besteht aus
Multiple-Choice-Fragen aus echten Prüfungen auf Universitätsniveau. Eine Punktzahl von
70 % entsprechen ungefähr dem menschlichen Niveau eines Studenten; GPT-4 und Claude 3 erzielen einen Wert von über 86 %.
Trotz seiner geringen Größe erreicht Phi-3-mini rund 70 %.
### HumanEval
HumanEval ist OpenAIs Benchmark für die Codegenerierung. Es besteht aus 164 Python
Programmierprobleme mit automatisierten Testfällen. Modelle werden gemessen
pass@k – die Wahrscheinlichkeit, dass mindestens eine von k generierten Lösungen alle besteht
Tests. GPT-4 erzielt ~87 % (bestanden bei 1); Ein gut abgestimmtes 7B-Modell kann ~50–60 % erreichen.
### HellaSwag
HellaSwag ist ein Benchmark für vernünftiges Denken. Models erhalten einen Satz
beschreibt eine alltägliche Aktivität und muss die wahrscheinlichste Fortsetzung auswählen
vier Optionen. Die falschen Optionen sind speziell darauf ausgelegt, plausibel zu sein
subtil falsch. Dabei wird geprüft, ob ein Modell über ein fundiertes physikalisches Verständnis verfügt
und soziale Situationen.
### ARC (AI2 Reasoning Challenge)
ARC ist ein Benchmark des Allen Institute for AI. Es besteht aus einer Grundschule
Wissenschaftliche Fragen, aufgeteilt in „Easy“- und „Challenge“-Sets. Das Challenge-Set
enthält Fragen, die auf Retrieval-basierten Methoden und einfachen statistischen Modellen basieren
Schwierigkeiten haben und eine mehrstufige Argumentation erfordern.
---

## Kern-KI/ML-Konzepte
### RAG (Retrieval-Augmented Generation)
RAG ist eine Technik, die ein Retrieval-System (typischerweise einen Vektor) kombiniert
Datenbank) mit einem Sprachmodell. Anstatt sich ausschließlich auf die Modelle zu verlassen
Um das parametrische Wissen zu nutzen, ruft RAG zunächst relevante Dokumente von einer externen Stelle ab
Wissensbasis und bindet sie dann in den Kontext des Modells ein. Dies ermöglicht die
Modell zur Beantwortung von Fragen zu aktuellen oder domänenspezifischen Informationen
ohne Umschulung. Potato.ai verwendet eine Form von RAG – es ruft aus seiner KB ab
und bezieht die Ergebnisse in den Kontext ein, bevor eine Antwort generiert wird.
### Feinabstimmung
Unter Feinabstimmung versteht man den Prozess, ein vorab trainiertes Modell weiter auf einem zu trainieren
kleinerer, domänenspezifischer Datensatz. Dadurch werden die Gewichte des Modells für a angepasst
bestimmte Aufgabe oder Domäne. Beispielsweise könnte eine Feinabstimmung eines Basis-LLM erfolgen
Krankenakten, um einen medizinischen Q&A-Assistenten zu erstellen. Feinabstimmung ist
rechenintensiv, aber viel günstiger als das Training von Grund auf.
### Quantisierung
Die Quantisierung verringert die numerische Präzision von Modellgewichten (z. B. von 32-Bit).
Float zu 4-Bit-Ganzzahl). Dadurch wird der Speicherbedarf drastisch reduziert – ein 7B-Modell
in 16-Bit-Genauigkeit sind ca. 14 GB VRAM erforderlich; das gleiche Modell in 4-Bit (GGUF-Format)
erfordert ~4GB. Die Quantisierung führt typischerweise zu einer geringen, aber akzeptablen Genauigkeit
Degradation und ist die Haupttechnik, die es ermöglicht, große Modelle auf Verbraucherbasis zu betreiben
Hardware oder sogar mobile Geräte.
### Kontextfenster
Das Kontextfenster ist die maximale Anzahl von Token, die ein Modell gleichzeitig verarbeiten kann.
einschließlich der Eingabeaufforderung und der generierten Antwort. GPT-3.5 hatte einen 4.096-Token
Fenster; GPT-4 Turbo und Claude 3 unterstützen 128.000 Token; Gemini 1.5 Pro
unterstützt 1.000.000 Token. Ein größeres Kontextfenster ermöglicht dem Modell das „Sehen“
mehr ein Gespräch oder ein Dokument auf einmal, wodurch die Kohärenz über einen längeren Zeitraum hinweg verbessert wird
Austausch.
### RLHF (Reinforcement Learning from Human Feedback)
RLHF ist die Trainingstechnik, die ein Basissprachmodell transformiert (welches
sagt einfach den nächsten Token voraus) in einen Assistenten, der Anweisungen befolgt und
verhält sich hilfsbereit. Menschliche Bewerter bewerten die Modellergebnisse, ein Belohnungsmodell wird trainiert
auf deren Präferenzen und das Sprachmodell wird dann darauf optimiert
Belohnungsmodell mit Verstärkungslernen. ChatGPT, Claude und Gemini verwenden alle
Varianten von RLHF oder ähnlichen Alignment-Techniken (z. B. Constitutional AI,
Direkte Präferenzoptimierung).
### Transformatorarchitektur
Der Transformer ist die neuronale Netzwerkarchitektur, die allen modernen LLMs zugrunde liegt.
Es wurde 2017 in der Arbeit „Attention Is All You Need“ von Vaswani et al. vorgestellt
verwendet Selbstaufmerksamkeitsmechanismen, um alle Token parallel zu verarbeiten
Der Reihe nach. Nur-Encoder-Transformatoren (BERT) werden zum Verstehen von Aufgaben verwendet.
Nur-Decoder-Transformatoren (GPT, Llama, Mistral) werden für Erzeugungsaufgaben verwendet.
Encoder-Decoder-Transformatoren (T5, BART) werden zur Übersetzung und Zusammenfassung verwendet.
### Einbettungen und Vektordatenbanken
Einbettungen sind dichte numerische Darstellungen von Text (oder Bildern), die von erstellt werden
ein neuronales Netzwerk. Semantisch ähnliche Texte haben Einbettungen, die nahe beieinander liegen
Vektorraum. Vektordatenbanken (ChromaDB, Pinecone, Weaviate, Qdrant) speichern
Diese Einbettungen ermöglichen eine schnelle, ungefähre Suche nach dem nächsten Nachbarn. Das sind sie
das Speicherrückgrat von RAG-Systemen, einschließlich der Cold-Memory-Schicht von Potato.ai.