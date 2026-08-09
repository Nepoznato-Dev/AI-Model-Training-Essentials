---
# Metadata
title: "Model Optimisation and Deployment"
description: "Quantisation, pruning, distillation, ONNX, serving infrastructure"
category: "AI and Machine Learning"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [model, optimization, deployment, ai-and-machine-learning]
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
# Modelloptimierung und -bereitstellung
Das Trainieren eines großen KI-Modells ist beeindruckend, aber der Großteil der Technik findet in der effizienten Bereitstellung statt. Ein Modell, das 10 Sekunden zum Reagieren benötigt oder acht A100-GPUs benötigt, ist für die meisten realen Anwendungen nutzlos. Modelloptimierung ist die Kunst und Wissenschaft, Modelle kleiner, schneller und kostengünstiger zu machen – ohne zu große Einbußen bei der Qualität. Diese Datei behandelt Quantisierung, Beschneidung, Destillation und die praktischen Werkzeuge, um Modelle in die Produktion zu bringen.
---

## Warum optimieren?
| Sorge | Auswirkungen |
|---------|--------|
| **Latenz** | Benutzer erwarten Antworten in weniger als 1 Sekunde; Alle weiteren 100 ms verlieren das Engagement |
| **Kosten** | GPU-Inferenz ist teuer; Ein 70B-Modell kostet etwa 0,05–0,15 US-Dollar pro 1 Mio. Token auf Cloud-Hardware |
| **Speicher** | Ein 7B-Modell in FP32 benötigt 28 GB VRAM; Die meisten Consumer-GPUs verfügen über 8–24 GB |
| **Energie** | Der Betrieb großer Modelle verbraucht viel Strom; Angelegenheiten für Mobile und Edge |
| **Maßstab** | Um Millionen von Benutzern bedienen zu können, sind Modelle erforderlich, die auf die verfügbare Hardware passen
---

## Quantisierung
Durch die Quantisierung wird die Präzision der Modellgewichte von 32-Bit-Gleitkomma (FP32) auf kleinere Formate wie INT8, INT4 oder noch niedriger reduziert.
### Präzisionsformate
| Formatieren | Bits pro Gewicht | Speicher für 7B-Modell | Qualität |
|--------|----------------|------|---------|
| **FP32** | 32 | 28 GB | Grundlinie (volle Genauigkeit) |
| **FP16 / BF16** | 16 | 14 GB | Nahezu identisch mit FP32 |
| **INT8** | 8 | 7 GB | Sehr geringer Qualitätsverlust |
| **INT4** | 4 | 3,5 GB | Mäßiger Qualitätsverlust; noch verwendbar |
| **INT3 / INT2** | 3-2 | 2,6-1,75 GB | Erheblicher Qualitätsverlust; Forschungsphase |
### Quantisierungsmethoden
| Methode | Wenn es passiert | Wie es funktioniert | Qualität |
|--------|----------------|--------------|---------|
| **Post-Training-Quantisierung (PTQ)** | Nach Abschluss des Trainings | Kalibrieren Sie das Modell anhand eines kleinen Datensatzes. optimale Skalen finden | Gut für INT8; verschlechtert sich bei INT4 |
| **GPTQ** | Nach dem Training | GPU-freundliche INT4-Quantisierung mit ungefähren Informationen zweiter Ordnung | Gute Qualität bei INT4 |
| **AWQ** (Aktivierungsbewusste Gewichtsquantisierung) | Nach dem Training | Schützen Sie hervorstechende Gewichte basierend auf Aktivierungsgrößen | Besser als GPTQ bei INT4 |
| **GGUF** (llama.cpp-Format) | Nach dem Training | CPU-freundliche Quantisierung; gemischte Präzision pro Schicht | Optimiert für CPU-Inferenz |
| **Quantisierungsbewusstes Training (QAT)** | Während des Trainings | Quantisierung während des Trainings simulieren, damit das Modell lernt, damit umzugehen | Beste Qualität; erfordert eine Umschulung |
### Praktische Auswirkungen
| Modell | FP16-Größe | INT4 Größe | Beschleunigung | Qualitätsverlust |
|-------|-----------|-----------|---------|-------------|
| **LLaMA 7B** | 14 GB | 3,5 GB | 2-4x | ~1-2 % auf Benchmarks |
| **LLaMA 70B** | 140 GB | 35 GB | 2-3x | ~2-3 % auf Benchmarks |
---

## Beschneiden
Durch das Beschneiden werden unnötige Gewichte oder Neuronen aus einem trainierten Modell entfernt.
| Geben Sie | ein Beschreibung | Vorteil | Herausforderung |
|------|-------------|-----------|-----------|
| **Unstrukturiert** | Einzelne Gewichte entfernen (auf Null setzen) | Höchste Kompressionsverhältnisse | Erfordert spärliche Hardwareunterstützung |
| **Strukturiert** | Ganze Neuronen, Aufmerksamkeitsköpfe oder Schichten entfernen | Reduziert direkt die Modellgröße | Kann mehr Qualität verlieren |
| **Größenbasiert** | Gewichte mit kleinsten Absolutwerten entfernen | Einfach; funktioniert gut | Möglicherweise fehlen wichtige kleine Gewichte |
| **Wichtigkeitsbasiert** | Entfernen Sie Gewichte basierend auf ihrem Beitrag zur Ausgabe | Bessere Qualitätskonservierung | Teurer zu berechnen |
### Pipeline beschneiden
| Schritt | Beschreibung |
|------|-------------|
| 1. Zug | Trainieren Sie das vollständige Modell normal |
| 2. Ergebnis | Berechnen Sie die Wichtigkeitswerte für jedes Gewicht/Neuron |
| 3. Beschneiden | Entfernen Sie die unwichtigsten Elemente |
| 4. Feinabstimmung | Neu trainieren, um verlorene Genauigkeit wiederherzustellen |
| 5. Wiederholen Sie | Iterative Beschneidung und Feinabstimmung für höhere Komprimierung |
---

## Wissensdestillation
Trainieren Sie ein kleines „Schüler“-Modell, um ein großes „Lehrer“-Modell nachzuahmen.
| Komponente | Rolle |
|-----------|------|
| **Lehrer** | Großes, hochwertiges Modell |
| **Student** | Kleines Modell, das vom Lehrer lernt |
| **Destillationsverlust** | Der Schüler versucht, der Ausgabeverteilung des Lehrers zu entsprechen (Soft Labels) |
### Arten der Destillation
| Geben Sie | ein Beschreibung | Beispiel |
|------|-------------|---------|
| **Logit-basiert** | Der Schüler stimmt mit den Ausgabewahrscheinlichkeiten des Lehrers überein | Hintons Originaldestillation |
| **Funktionsbasiert** | Der Schüler stimmt mit den Zwischendarstellungen des Lehrers überein | FitNets |
| **Beziehungsbasiert** | Student gleicht Beziehungen zwischen Proben ab | RKD (Relationale Wissensdestillation) |
| **Datenfrei** | Keine Original-Trainingsdaten erforderlich; Lehrergeneration nutzen | DAFL, DeepInversion |
### Bemerkenswerte Destillationsbeispiele
| Lehrer | Student | Ergebnis |
|---------|---------|--------|
| **GPT-4** | GPT-3.5-Turbo (gemunkelt) | Kleineres Modell mit viel GPT-4-Qualität |
| **BERT-Groß** | DistilBERT | 40 % kleiner, 60 % schneller, 97 % der Leistung von BERT |
| **LLaMA 70B** | LLaMA 7B (durch Destillation) | Kleines Open-Source-Modell nähert sich der Qualität eines großen Modells |
---

## LLM-spezifische Optimierungen
### KV-Cache-Optimierung
Große Sprachmodelle speichern Schlüssel-Wert-Paare von vorherigen Token im Cache, um eine Neuberechnung zu vermeiden.
| Technik | Beschreibung | Auswirkungen |
|-----------|-------------|--------|
| **Multi-Query Attention (MQA)** | Alle Aufmerksamkeitsköpfe teilen sich ein KV-Paar | Reduziert den Speicher; leichter Qualitätsverlust |
| **Grouped-Query Attention (GQA)** | Gruppen von Köpfen teilen sich KV-Paare | Balance zwischen MQA und Standardaufmerksamkeit |
| **Schiebefenster Achtung** | Kümmere dich nur um die letzten W-Token | Reduziert die KV-Cache-Größe für lange Kontexte |
### Spekulative Dekodierung
| Schritt | Beschreibung |
|------|-------------|
| 1 | Ein kleines „Entwurfs“-Modell generiert schnell K Token |
| 2 | Das große Modell überprüft alle K Token in einem Vorwärtsdurchlauf |
| 3 | Akzeptierte Token bleiben erhalten; Abgelehnte werden neu generiert |
Ergebnis: 2-3-fache Beschleunigung bei der Generierung ohne Qualitätsverlust (das große Modell hat immer das letzte Wort).
### Flash-Aufmerksamkeit
| Funktion | Beschreibung |
|---------|-------------|
| **Problem** | Standardaufmerksamkeit erfordert O(n²) Speicher für die Aufmerksamkeitsmatrix |
| **Lösung** | Berechnen Sie die Aufmerksamkeit in Blöcken. nie die vollständige Matrix im Speicher materialisieren |
| **Ergebnis** | 2-4x schneller; ermöglicht viel längere Kontextfenster |
| **Varianten** | Flash Attention 2 (schneller), FlashDecoding (optimiert für Inferenz) |
---

## Bereitstellen von Frameworks
| Rahmen | Am besten für | Hauptmerkmal |
|-----------|----------|-------------|
| **vLLM** | LLM-Portion | PagedAttention; kontinuierliche Dosierung; hoher Durchsatz |
| **TensorRT-LLM** | NVIDIA-GPU-Schlussfolgerung | Maximale Leistung auf NVIDIA-Hardware |
| **llama.cpp** | Rückschluss auf CPU und Consumer-GPU | Führt quantisierte Modelle auf Laptops und Telefonen aus |
| **Ollama** | Lokales Modell läuft | Benutzerfreundlicher Wrapper um llama.cpp |
| **Triton-Inferenzserver** | Multi-Framework-Bereitstellung | Unterstützt TensorFlow, PyTorch, ONNX, TensorRT |
| **Fackelserve** | PyTorch-Modellbereitstellung | Native PyTorch-Integration |
| **ONNX-Laufzeit** | Plattformübergreifende Inferenz | Optimierte Ausführung auf der gesamten Hardware |
| **BentoML** | Produktionsbereitstellung | Framework-agnostisch; kümmert sich um Verpackung und Servieren |
---

## Bereitstellungsmuster
| Muster | Beschreibung | Wann zu verwenden |
|---------|-------------|-------------|
| **Edge-Bereitstellung** | Führen Sie Modelle auf Telefonen, IoT-Geräten oder eingebetteter Hardware aus | Geringe Latenz; offline; Privatsphäre |
| **Cloud-API** | Hostmodelle auf Cloud-GPUs; über API bereitstellen | Maximale Rechenleistung; Bezahlung pro Nutzung |
| **Hybrid** | Kleines Modell auf Gerät; großes Modell in der Wolke | Das Beste aus beiden Welten |
| **Serverlos** | Auf Null skalieren; Zahlen Sie nur bei Nutzung | Sporadischer Verkehr; kostensensibel |
| **Batch-Inferenz** | Verarbeiten Sie Daten in großen Mengen nach einem Zeitplan | Wenn Echtzeit nicht benötigt wird |
---

## Benchmarking
| Metrisch | Was es misst |
|--------|-----------------|
| **Tokens pro Sekunde** | Erzeugungsdurchsatz (höher ist besser) |
| **Zeit bis zum ersten Token (TTFT)** | Latenz, bevor das erste Ausgabetoken erscheint |
| **Latenz pro Anfrage** | Gesamtzeit von der Eingabe bis zur vollständigen Ausgabe |
| **Speichernutzung** | VRAM oder RAM während der Inferenz verbraucht |
| **Durchsatz** | Pro Sekunde bearbeitete Anfragen |
| **Kosten pro 1 Mio. Token** | Dollarkosten für die Verarbeitung von 1 Million Token |
---

## Praktische Tipps
- **Beginnen Sie mit der Quantisierung.** Die INT4-Quantisierung (AWQ oder GPTQ) bietet den besten Kompromiss zwischen Qualität und Größe. Die meisten 7B-Modelle laufen problemlos auf einer einzelnen Consumer-GPU bei INT4.
- **Verwenden Sie vLLM für die LLM-Bereitstellung.** Dies ist die schnellste Open-Source-Option für LLM-Inferenz mit hohem Durchsatz.
- **Profil vor der Optimierung.** Messen Sie, wo die Zeit tatsächlich verbracht wird. Der Engpass liegt häufig in der Speicherbandbreite und nicht in der Rechenleistung.
- **Passen Sie das Modell an die Aufgabe an.** Ein 7B-Modell reicht für die meisten Aufgaben aus. Verwenden Sie nicht 70B, wenn 7B ausreicht.
- **Erwägen Sie eine Destillation.** Wenn Sie ein kleines, schnelles Modell für die Produktion benötigen, destillieren Sie von einem größeren Modell, anstatt von Grund auf zu trainieren.
- **Kontinuierliche Überwachung.** Die Modellleistung kann sich mit der Zeit verschlechtern, wenn sich die Datenverteilung ändert. Verfolgen Sie Latenz-, Durchsatz- und Qualitätsmetriken.
---

## Zusammenfassung
Die Modelloptimierung ist die Brücke zwischen Forschung und Produktion. Durch die Quantisierung werden Modelle um das 4- bis 8-fache verkleinert, bei minimalem Qualitätsverlust. Durch das Beschneiden wird Eigengewicht entfernt. Die Destillation überträgt Wissen von großen auf kleine Modelle. Flash Attention- und KV-Cache-Tricks beschleunigen die Schlussfolgerung. Zusammen verwandeln diese Techniken ein Modell, das ein Rechenzentrum erfordert, in ein Modell, das auf einem Laptop oder Telefon läuft. Das Feld entwickelt sich schnell – was letztes Jahr acht A100 erforderte, läuft heute auf einer Verbraucher-GPU.