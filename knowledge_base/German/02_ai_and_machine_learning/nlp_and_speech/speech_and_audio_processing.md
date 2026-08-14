---
# Metadata
title: "Speech and Audio Processing"
description: "ASR, TTS, audio features, Whisper, speech pipelines"
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
tags: [speech, audio, processing, ai-and-machine-learning]
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

# Sprach- und Audioverarbeitung
Sprach- und Audioverarbeitung umfasst die Technologien, die es Maschinen ermöglichen, Geräusche zu hören, zu verstehen, zu erzeugen und zu manipulieren. Dazu gehören Spracherkennung (Umwandlung gesprochener Wörter in Text), Sprachsynthese (Umwandlung von Text in gesprochene Wörter), Sprecheridentifikation, Musikerzeugung und Verständnis von Umgebungsgeräuschen. Das Gebiet hat sich durch Deep Learning verändert – moderne Systeme nähern sich der Genauigkeit der Spracherkennung auf menschlichem Niveau und erzeugen unheimlich natürliche synthetische Stimmen.
---

## Grundlagen des digitalen Audios
Schall ist eine Druckwelle. Um sie digital zu verarbeiten, tasten wir die Welle in regelmäßigen Abständen ab.
| Konzept | Beschreibung | Typischer Wert |
|---------|-------------|---------------|
| **Abtastrate** | Wie oft pro Sekunde wird der Schall gemessen | 8 kHz (Telefon), 16 kHz (Sprache), 44,1 kHz (CD), 48 kHz (professionell) |
| **Bittiefe** | Präzision jeder Probe | 16-Bit (CD), 24-Bit (professionell), 32-Bit-Float (Verarbeitung) |
| **Kanäle** | Mono (1), Stereo (2), Surround (5.1, 7.1) | Stereoanlage für Musik; Mono für Sprache |
| **Dauer** | Länge des Audios | Variiert |
Eine 1-minütige Monoaufnahme mit 16 kHz, 16 Bit = 1,92 MB. Ein 3-minütiger Stereosong mit 44,1 kHz, 16-Bit = 30,3 MB.
---

## Audio-Feature-Extraktion
Es ist für Modelle schwierig, direkt mit rohen Audiowellenformen zu arbeiten. Wir extrahieren Merkmale, die die wichtigen Eigenschaften des Klangs erfassen.
| Funktion | Was es erfasst | Anwendungsfall |
|---------|-----------------|----------|
| **Mel-Spektrogramm** | Frequenzinhalt im Zeitverlauf, abgebildet auf die menschliche Hörwahrnehmung | Spracherkennung, Musikklassifizierung |
| **MFCC** (Mel-Frequency Cepstral Coefficients) | Kompakte Darstellung der Spektralhülle | Traditionelle Spracherkennung |
| **Chromagramm** | Tonhöhenklassenverteilung (welche Noten werden gespielt) | Musikanalyse, Akkorderkennung |
| **Nulldurchgangsrate** | Wie oft kreuzt das Signal Null | Stimmhafte vs. stimmlose Erkennung |
| **RMS-Energie** | Signallautstärke im Zeitverlauf | Sprachaktivitätserkennung |
| **Tonhöhe (F0)** | Grundfrequenz | Sprecheridentifikation, Musiktranskription |
### Mel-Spektrogramm
Die gebräuchlichste Audiodarstellung für Deep Learning. Es wandelt das Audio in ein 2D-bildähnliches Format um:
| Achse | Stellt | dar
|------|-----------|
| **X-Achse** | Zeit |
| **Y-Achse** | Frequenz (auf der Mel-Skala – wahrnehmungsbezogen) |
| **Farbe/Intensität** | Energie bei dieser Frequenz und Zeit |
Die Mel-Skala ähnelt dem menschlichen Gehör: Wir können tiefe Frequenzen besser unterscheiden als hohe.
---

## Automatische Spracherkennung (ASR)
ASR wandelt gesprochene Sprache in Text um. Es ist eine der kommerziell wichtigsten Anwendungen der Audio-KI.
### Entwicklung von ASR
| Ära | Ansatz | Einschränkung |
|-----|----------|------------|
| **Vor 2010** | Versteckte Markov-Modelle + Gaußsche Mischungsmodelle | Erfordert umfangreiche Handarbeit; schlecht bei lauten Bedingungen |
| **2010-2015** | DNN-HMM-Hybrid | Neuronale Netze ersetzten GMMs; deutliche Verbesserung |
| **2015-2020** | End-to-End-Modelle (Deep Speech, LAS) | Einzelnes neuronales Netzwerk von Audio zu Text |
| **2020+** | Transformatorbasiert (Whisper, Conformer) | Modernste Genauigkeit; mehrsprachig; robust |
### Wichtige ASR-Modelle
| Modell | Architektur | Trainingsdaten | Bemerkenswerte Funktion |
|-------|-------------|---------------|-----------------|
| **Flüstern** (OpenAI) | Encoder-Decoder-Transformator | 680.000 Stunden, 99 Sprachen | Mehrsprachig; robust gegenüber Akzenten und Lärm; Open-Source |
| **Konformer** | Faltung + Selbstaufmerksamkeit | Verschiedene | Kombiniert lokale (Conv) und globale (Aufmerksamkeit) Funktionen |
| **wav2vec 2.0** | Selbstüberwachter Transformator | Unbeschriftete Rede | Lernt aus Rohaudio ohne Transkriptionen |
| **USM** (Google) | Universelles Sprachmodell | 2 Millionen Stunden, über 300 Sprachen | Die meisten Sprachen werden abgedeckt |
| **MMS** (Meta) | Massiv mehrsprachige Sprache | Über 1.400 Sprachen | Erweitert die Abdeckung auf Sprachen mit geringen Ressourcen |
### ASR-Metriken
| Metrisch | Beschreibung |
|--------|-------------|
| **WER** (Wortfehlerrate) | Prozentsatz der falsch transkribierten Wörter. Niedriger ist besser. Die menschliche Leistungsfähigkeit für sauberes Englisch liegt bei ca. 4–5 %. |
| **CER** (Zeichenfehlerrate) | Wie WER, aber auf Charakterebene. Wird für Sprachen ohne Wortgrenzen (Chinesisch, Japanisch) verwendet. |
### Häufige ASR-Herausforderungen
| Herausforderung | Beschreibung |
|-----------|-------------|
| **Akzente und Dialekte** | Die Leistung sinkt bei nicht standardmäßigen Akzenten erheblich |
| **Hintergrundgeräusche** | Musik, Verkehr und andere Lautsprecher beeinträchtigen die Genauigkeit |
| **Code-Umschaltung** | Sprecher wechseln mitten im Satz zwischen den Sprachen |
| **Homophone** | „Da“ vs. „ihr“ vs. „sie sind“ – erfordert Kontext |
| **Interpunktion und Formatierung** | Die ASR-Ausgabe erfolgt normalerweise ohne Interpunktion. benötigt Nachbearbeitung |
| **Ressourcenarme Sprachen** | Die meisten Modelle schneiden bei Sprachen mit wenigen Trainingsdaten schlecht ab |
---

## Text-to-Speech (TTS)
TTS wandelt geschriebenen Text in gesprochenes Audio um. Moderne Systeme erzeugen Sprache, die oft nicht von menschlichen Aufnahmen zu unterscheiden ist.
### Entwicklung von TTS
| Ära | Ansatz | Qualität |
|-----|----------|---------|
| **Vor 2010** | Konkatenativ (Aufgezeichnete Fragmente zusammenfügen) | Roboter; begrenzte Ausdruckskraft |
| **2010-2017** | Statistische Parametrie (HMMs, frühe neuronale) | Besser, aber immer noch als synthetisch erkennbar |
| **2017-2020** | Neuronal (Tacotron, WaveNet) | Nahezu menschliche Qualität; ausdrucksstark |
| **2020+** | Neuronaler Codec (VALL-E, Bark) | Klonen von Stimmen; wenige Schüsse; höchst natürlich |
### Wichtige TTS-Modelle
| Modell | Architektur | Bemerkenswerte Funktion |
|-------|-------------|-----------------|
| **WaveNet** (DeepMind) | Autoregressives generatives Modell | Erstes wirklich natürlich klingendes TTS |
| **Tacotron 2** (Google) | Seq2seq + Vocoder | End-to-End; hohe Qualität |
| **VITS** | Variationsinferenz + kontradiktorisches Training | Schnell; gute Qualität; weit verbreitet |
| **VALL-E** (Microsoft) | Neuronales Codec-Sprachmodell | Klonen von Stimmen aus einem 3-Sekunden-Sample |
| **Rinde** (Suno) | Transformatorbasiert | Mehrsprachig; nichtsprachliche Geräusche (Lachen, Musik) |
| **ElevenLabs** | Kommerziell | Branchenführendes Stimmenklonen |
| **ChatTTS** | Open-Source | Optimiert für Konversationssprache |
| **Fischrede** | Open-Source | Schnell; mehrsprachig |
### Sprachklonen
Durch das Klonen von Stimmen wird aus einem kurzen Audiobeispiel eine synthetische Stimme erstellt, die wie eine bestimmte Person klingt.
| Methode | Benötigte Daten | Qualität |
|--------|------------|---------|
| **Feinabstimmung** | 10-60 Minuten Rede | Hohe Qualität; sprecherspezifisch |
| **Wenige Schüsse** | 3-30 Sekunden Redezeit | Gute Qualität; schnelle Einrichtung |
| **Nullschuss** | Keine Zielsprecherdaten | Verwendet Referenzaudio zur Inferenzzeit |
**Ethische Bedenken**: Das Klonen von Stimmen kann für Identitätsdiebstahl, Betrug und Deepfakes genutzt werden. Die meisten kommerziellen Anbieter erfordern eine stimmliche Einwilligung.
---

## Sprechererkennung
| Aufgabe | Beschreibung | Bewerbung |
|------|-------------|-------------|
| **Sprecherverifizierung** | „Ist diese Person die Person, für die sie sich ausgeben?“ | Telefonbanking, Geräteentsperrung |
| **Sprecheridentifikation** | "Wer ist dran?" | Transkription von Besprechungen, Forensik |
| **Sprechertagebuch** | „Wer hat wann gesprochen?“ (in Audio mit mehreren Lautsprechern) | Besprechungszusammenfassungen, Untertitelgenerierung |
| Modell | Ansatz |
|-------|----------|
| **ECAPA-TDNN** | Einbettungsbasiert; State-of-the-Art zur Verifizierung |
| **d-Vektor** | Einfache Sprechereinbettungen von DNN |
| **x-Vektor** | Verbesserte Sprechereinbettungen; weit verbreitet |
---

## Abruf von Musikinformationen
| Aufgabe | Beschreibung | Werkzeuge/Modelle |
|------|-------------|-------------|
| **Musiktranskription** | Konvertieren Sie Audio in Noten / MIDI | Spotify Basic Pitch, Spleeter |
| **Quellentrennung** | Einzelne Instrumente oder Gesang isolieren | Demucs, Spleeter, Musikquellentrennung |
| **Genreklassifizierung** | Musik nach Genre kategorisieren | CNNs auf Spektrogrammen |
| **Beat-Tracking** | Tempo und Beatpositionen erkennen | Librosa, Madmom |
| **Akkorderkennung** | Akkorde in der Musik identifizieren | Chord-CNN, CRF-Modelle |
| **Musikgeneration** | Neue Musik erstellen | MusicGen, MuseNet, AIVA |
---

## Erkennung von Umgebungsgeräuschen
| Aufgabe | Beschreibung | Bewerbung |
|------|-------------|-------------|
| **Erkennung von Schallereignissen** | Identifizieren Sie Geräusche in einer Umgebung | Smart Home (Glas zerbricht, Baby weint) |
| **Klassifizierung akustischer Szenen** | Klassifizierung der Umgebung (Büro, Park, Verkehr) | Kontextsensitive Geräte |
| **Anomalieerkennung** | Ungewöhnliche Geräusche erkennen | Industrielle Überwachung (machineæ•…éšœ) |
| Datensatz | Geräusche | Größe |
|---------|--------|------|
| **AudioSet** | 632 Klangklassen | Über 2 Millionen YouTube-Clips |
| **ESC-50** | 50 Umweltschallklassen | 2.000 Clips |
| **UrbanSound8K** | Urbane Klänge | 8.732 Clips |
---

## Tools und Frameworks
| Werkzeug | Zweck |
|------|---------|
| **Librosa** | Python-Bibliothek zur Audioanalyse (Funktionen, Effekte, Visualisierung) |
| **Pydub** | Einfache Audiomanipulation (Ausschneiden, Verketten, Exportieren) |
| **FFmpeg** | Audio-/Videoverarbeitung über die Befehlszeile (das Schweizer Taschenmesser) |
| **Fackelaudio** | PyTorch-Audioverarbeitung (Transformationen, Datensätze, Modelle) |
| **Umarmendes Gesicht (Transformer)** | Vorab trainierte ASR- und TTS-Modelle |
| **Flüstern (OpenAI)** | Spracherkennung (Open-Source) |
| **Coqui TTS** | Open-Source-TTS-Toolkit |
| **Demucs** | Trennung von Musikquellen |
| **SpeechBrain** | Komplettes Sprach-Toolkit (ASR, TTS, Sprechererkennung) |
---

## Praktische Tipps
- **Hören Sie sich immer Ihre Daten an.** Hören Sie sich vor dem Training die Beispielaudiodaten an. Beachten Sie die Abtastrate, den Geräuschpegel und die Lautsprechereigenschaften.
- **Abtastraten anpassen.** Whisper erwartet 16 kHz. Wenn Ihr Audio 44,1 kHz hat, sampeln Sie es erneut – beachten Sie jedoch, dass durch das Downsampling Informationen verloren gehen.
- **Audiodaten erweitern.** Hintergrundgeräusche hinzufügen, Geschwindigkeit und Tonhöhe variieren, verschiedene Mikrofone simulieren. Dies verbessert die Robustheit erheblich.
- **Verwenden Sie vorab trainierte Modelle.** Whisper für ASR und VITS/Bark für TTS sind hervorragende Ausgangspunkte. Feinabstimmung ist fast immer besser als Training von Grund auf.
- **Behandeln Sie Stille.** Die Sprachaktivitätserkennung (VAD) entfernt Stille vor der Verarbeitung, spart Rechenleistung und verbessert die Genauigkeit. Silero VAD und WebRTC VAD sind beliebte Optionen.
- **Lautstärke normalisieren.** Verschiedene Aufnahmen haben sehr unterschiedliche Lautstärkepegel. Vor der Verarbeitung auf ein einheitliches Niveau normalisieren.
---

## Zusammenfassung
Die Sprach- und Audioverarbeitung wurde durch Deep Learning revolutioniert. Moderne ASR-Systeme wie Whisper erreichen in Dutzenden von Sprachen eine Genauigkeit auf menschlichem Niveau. TTS-Systeme erzeugen Sprache, die zunehmend nicht mehr von menschlichen Aufnahmen zu unterscheiden ist. Das Klonen von Stimmen funktioniert ab Sekunden Audio. Die Musikerzeugung, die Quellentrennung und die Erkennung von Umgebungsgeräuschen machen rasante Fortschritte. Der Bereich steht vor anhaltenden Herausforderungen – ressourcenarme Sprachen, laute Umgebungen, ethische Bedenken im Zusammenhang mit dem Klonen von Stimmen –, aber die Richtung ist klar: Maschinen werden beim Hören, Verstehen und Erzeugen von Geräuschen genauso gut wie Menschen.