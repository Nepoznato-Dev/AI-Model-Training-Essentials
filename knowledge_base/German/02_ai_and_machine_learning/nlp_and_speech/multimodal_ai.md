---
# Metadata
title: "Multimodal AI"
description: "Vision-language models, CLIP, DALL-E, cross-modal learning"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
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
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
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
tags: [multimodal, ai, ai-and-machine-learning]
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

# Multimodale KI
Multimodale KI-Systeme verarbeiten und kombinieren Informationen aus mehreren Datentypen – Text, Bilder, Audio, Video und mehr – gleichzeitig. Während frühere KI-Systeme typischerweise auf einer einzigen Modalität beruhten (nur Text, nur Bilder), sind die leistungsfähigsten modernen Systeme multimodal. GPT-4V liest Bilder und Text zusammen; Gemini verarbeitet Text, Bilder, Audio und Video nativ; und Systeme wie Sora generieren Videos aus Textbeschreibungen. In dieser Datei wird erläutert, wie multimodale KI funktioniert, welche Architekturen dahinter stecken und warum die Kombination von Modalitäten so leistungsstark ist.
---

## Warum multimodal?
| Vorteil | Beschreibung | Beispiel |
|---------|-------------|---------|
| **Reicheres Verständnis** | Verschiedene Modalitäten bieten ergänzende Informationen | Ein Video vermittelt Bewegung, Ton und Kontext, was Text allein nicht kann
| **Bessere Verallgemeinerung** | Modalitätsübergreifendes Lernen schafft robustere Darstellungen | Ein Modell, das sowohl Bilder als auch Textbeschreibungen von „Katze“ gesehen hat, versteht das Konzept besser |
| **Natürlichere Interaktion** | Menschen kommunizieren über mehrere Kanäle | Sprachassistenten, die sehen, worauf Sie zeigen |
| **Kreuzmodaler Transfer** | Wissen aus einer Modalität hilft bei einer anderen | Bildverständnis verbessert die Textgenerierung und umgekehrt |
---

## Kernarchitekturen
### Vision-Language-Modelle (VLMs)
Modelle, die Bilder und Text gemeinsam verarbeiten.
| Architektur | Wie es funktioniert | Beispiele |
|-------------|-------------|---------|
| **Dual-Encoder** | Separate Encoder für Bild und Text; zu einem späteren Zeitpunkt kombinieren | CLIP, AUSRICHTEN |
| **Fusion-Encoder** | Bild- und Text-Tokens werden verschachtelt und gemeinsam verarbeitet | Flamingo, Zwillinge |
| **Queraufmerksamkeit** | Text-Token kümmern sich um Bildfunktionen (oder umgekehrt) | Flamingo, CoCa |
| **Einheitlicher Tokenisierer** | Bilder werden in Token umgewandelt und zusammen mit Text-Tokens verarbeitet | Zwillinge, Chamäleon |
### Wie Vision-Language-Modelle funktionieren
| Schritt | Beschreibung |
|------|-------------|
| **1. Bild kodieren** | Ein Vision-Encoder (ViT, SigLIP) wandelt das Bild in eine Reihe von Merkmalsvektoren um |
| **2. Text kodieren** | Ein Sprachencoder verarbeitet die Text-Tokens |
| **3. Sicherungsmodalitäten** | Bildmerkmale werden in den Einbettungsraum des Sprachmodells projiziert |
| **4. Generieren** | Das Sprachmodell erzeugt Text, der sowohl von Bild- als auch von Texteingaben abhängig ist |
### Wichtige Vision-Language-Modelle
| Modell | Entwickler | Architektur | Bemerkenswerte Funktion |
|-------|-----------|-------------|-----------------|
| **CLIP** | OpenAI | Dual-Encoder (ViT + Text-Encoder) | Zero-Shot-Bildklassifizierung per Text |
| **LLaVA** | Open-Source | LLaMA + CLIP visueller Encoder | Open-Source-VLM; starke Gemeinschaft |
| **GPT-4V / 4o** | OpenAI | Einheitliches multimodales | Verarbeitet Text, Bilder, Audio zusammen |
| **Zwillinge** | Google DeepMind | Nativ multimodal aus der Ausbildung | Von Grund auf für Multimodalität konzipiert |
| **Claude** | Anthropisch | Vision + Text | Stark im Verständnis von Dokumenten und Diagrammen |
| **Qwen-VL** | Alibaba | Offenes VLM | Konkurrenzfähig mit geschlossenen Modellen |
| **InternVL** | Open-Source | Multiskalen-Vision-Encoder | Starke Open-Source-Option |
---

## Audio- und Sprachmodelle
### Spracherkennung (ASR)
| Modell | Architektur | Bemerkenswerte Funktion |
|-------|-------------|-----------------|
| **Flüstern** (OpenAI) | Encoder-Decoder-Transformator | Geschult in 680.000 Stunden mehrsprachigem Audio; robust |
| **Konformer** | Faltung + Selbstaufmerksamkeit | Kombiniert lokale und globale Funktionen |
| **wav2vec 2.0** | Selbstüberwacht | Lernt aus unbenannter Sprache |
| **USM** (Google) | Universelles Sprachmodell | 2 Mio. Stunden beschriftete Daten; Über 300 Sprachen |
### Text-to-Speech (TTS)
| Modell | Ansatz | Bemerkenswerte Funktion |
|-------|----------|-----------------|
| **VALL-E** (Microsoft) | Neuronaler Codec | Klonen von Stimmen aus einem 3-Sekunden-Sample |
| **Rinde** (Suno) | Transformatorbasiert | Mehrsprachig; enthält Nicht-Sprachlaute |
| **ElevenLabs** | Kommerziell | Hochwertiges Klonen von Stimmen |
| **ChatTTS** | Open-Source | Konversationsrede mit natürlicher Prosodie |
| **Fischrede** | Open-Source | Mehrsprachig; schnelle Schlussfolgerung |
### Audioverständnis
| Modell | Fähigkeit |
|-------|-----------|
| **AudioLDM** | Generierung von Soundeffekten aus Text |
| **MusicGen** (Meta) | Text-zu-Musik-Generierung |
| **Qwen-Audio** | Audioverständnis (Sprache, Musik, Umgebungsgeräusche) |
| **LACHS** | Sprach-, Audio-, Sprach-, Musik- und Geräuschverständnis |
---

## Videomodelle
Video kombiniert Bilder, Audio, Text und Zeit und ist damit die komplexeste Modalität.
| Modell | Geben Sie | ein Fähigkeit |
|-------|------|-------------|
| **Sora** (OpenAI) | Text-zu-Video | Bis zu 1080p; versteht Physik |
| **Zwillinge** | Videoverständnis | Kann lange Videos mit Audio analysieren |
| **Video-LLaVA** | Video + Text | Open-Source-Videoverständnis |
| **Landebahn Gen-3** | Text/Bild-zu-Video | Kommerzielle Videoerstellung |
| **Kling** | Text-zu-Video | Generierung von Langformatvideos |
### Herausforderungen beim Videoverständnis
| Herausforderung | Beschreibung |
|-----------|-------------|
| **Zeitliche Argumentation** | Ereignisse verstehen, die sich im Laufe der Zeit abspielen |
| **Langer Kontext** | Videos können Stunden lang sein; Die Verarbeitung aller Frames ist teuer |
| **Audiovisuelle Synchronisierung** | Gesagtes mit Gezeigtem verbinden |
| **Kausalität** | Ursache und Wirkung in Videosequenzen verstehen |
---

## Cross-Modal Retrieval
Suche nach relevanten Inhalten über verschiedene Modalitäten hinweg.
| Aufgabe | Beschreibung | Beispiel |
|------|-------------|---------|
| **Text → Bild** | Finden Sie Bilder, die zu einer Textabfrage passen | Suchen Sie in einer Fotobibliothek nach „Sonnenuntergang über Bergen“.
| **Bild → Text** | Für ein Bild relevanten Text finden | Bildunterschriften erstellen |
| **Text → Audio** | Sounds finden, die einer Beschreibung entsprechen | Sounddesign: „Schritte auf Schotter“ |
| **Bild → Bild** | Visuell ähnliche Bilder finden | Produktsuche nach Bild |
### CLIP für Cross-Modal Retrieval
Der gemeinsame Einbettungsraum von CLIP ermöglicht einen modalübergreifenden Zero-Shot-Abruf:
| Schritt | Beschreibung |
|------|-------------|
| 1 | Alle Bilder mit dem Vision-Encoder | kodieren
| 2 | Codieren Sie die Textabfrage mit dem Text-Encoder |
| 3 | Berechnen Sie die Kosinusähnlichkeit zwischen Texteinbettungen und allen Bildeinbettungen |
| 4 | Gibt die Bilder mit der höchsten Ähnlichkeit zurück |
Dies funktioniert ohne aufgabenspezifisches Training – eine Eigenschaft, die als **Zero-Shot**-Fähigkeit bezeichnet wird.
---

## Verkörperte KI
Verkörperte KI kombiniert multimodale Wahrnehmung mit körperlicher Aktion.
| System | Modalität | Bewerbung |
|--------|----------|-------------|
| **RT-2** (Google) | Vision + Sprache → Roboteraktionen | Universelle Robotersteuerung anhand von Textanweisungen |
| **Oktober** | Open-Source-Roboterrichtlinie | Auf diverse Roboterdaten trainiert |
| **Tesla Optimus** | Sehen + Sprache → körperliche Aufgaben | Humanoider Roboter für allgemeine Aufgaben |
| **Abbildung 01** | Vision + Sprache + Sprache | Humanoider Roboter mit Konversationsfähigkeit |
### Herausforderungen in der verkörperten KI
| Herausforderung | Warum es schwer ist |
|-----------|--------------|
| **Sim-zu-Real-Lücke** | Die Simulation erfasst die reale Physik nicht perfekt |
| **Geschicklichkeit** | Die Feinmotorik (Hände, Finger) ist äußerst schwierig |
| **Sicherheit** | Physische Roboter können echten Schaden anrichten |
| **Echtzeitverarbeitung** | Muss in Millisekunden wahrnehmen, entscheiden und handeln |
| **Verallgemeinerung** | Ein Roboter, der darauf trainiert ist, rote Tassen aufzunehmen, kann bei blauen scheitern |
---

## Daten und Schulung
### Multimodale Trainingsdaten
| Datensatz | Modalitäten | Größe |
|---------|-----------|------|
| **LAION-5B** | Bild-Text-Paare | 5,85 Milliarden Paare |
| **DataComp** | Kuratierter Bildtext | Benchmark für Datensatzdesign |
| **WIT** (Wikipedia) | Bildtext aus Wikipedia | 11,5 Millionen Paare |
| **HowTo100M** | Videotext (Anleitungsvideos) | 100 Millionen Clips |
| **LibriSpeech** | Sprachtext | 1.000 Stunden Englisch |
| **Gemeinsame Stimme** | Sprachtext | Mehrsprachig; von der Community beigesteuert |
### Trainingsstrategien
| Strategie | Beschreibung | Wann zu verwenden |
|----------|-------------|-------------|
| **Gemeinsames Training** | Trainieren Sie alle Modalitäten gleichzeitig | Wenn Sie multimodale Daten ausgerichtet haben |
| **Lehrplan-Lernen** | Beginnen Sie mit einfachen Beispielen; Schwierigkeitsgrad erhöhen | Verbessert die Konvergenz |
| **Kontrastives Lernen** | Lernen Sie, verwandte Paare modalitätsübergreifend abzugleichen (CLIP-Stil) | Gemeinsame Darstellungen erstellen |
| **Anweisungsoptimierung** | Trainieren Sie mit multimodalen Anweisungs-Antwort-Paaren | Modelle nach multimodalen Anweisungen erstellen |
---

## Auswertung
| Benchmark | Modalitäten | Was es testet |
|-----------|-----------|---------------|
| **MMLU** | Text | Wissen aus 57 Fächern |
| **MMMU** | Text + Bilder | Argumentation auf Hochschulniveau mit Diagrammen |
| **MathVista** | Text + Bilder | Mathematische Argumentation mit visuellen Daten |
| **Video-MME** | Text + Video | Videoverständnis und zeitliches Denken |
| **HELM** | Text + Audio | Multimodale Langzeitkontextbewertung |
| **SWE-Bank** | Text + Code | Praxisnahe Software-Engineering-Aufgaben |
---

## Zusammenfassung
Multimodale KI stellt den Wandel von Einzweckmodellen hin zu Systemen dar, die alle Arten von Daten wahrnehmen und schlussfolgern. Vision-Language-Modelle wie GPT-4V und Gemini können Bilder und Text gemeinsam verstehen; Sprachmodelle wie Whisper und VALL-E verarbeiten Audio; Videomodelle beginnen, die volle Komplexität bewegter Bilder mit Ton zu verarbeiten. Der Trend ist klar: Die leistungsfähigsten KI-Systeme der Zukunft werden von Natur aus multimodal sein und alle Arten von Informationen gleichzeitig verarbeiten. Die Herausforderungen – Datenausrichtung, Rechenkosten, Bewertung und integrierte Bereitstellung – sind erheblich, aber die Fortschritte im Zeitraum 2024–2026 waren schnell.