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
# NLP-Grundlagen
Natural Language Processing (NLP) ist der Bereich, in dem Maschinen beigebracht werden, menschliche Sprache zu verstehen, zu erzeugen und mit ihr zu arbeiten. Es unterstützt Suchmaschinen, Chatbots, Übersetzungssysteme, Stimmungsanalysen und die großen Sprachmodelle (LLMs), die die KI seit 2020 verändert haben. Diese Datei deckt die Entwicklung von klassischen Techniken zu modernen Transformer-basierten Architekturen ab.
---

## Textvorverarbeitung
Rohtext ist chaotisch. Bevor ein Model es nutzen kann, muss es gereinigt und strukturiert werden.
| Schritt | Was es tut | Beispiel |
|------|-------------|---------|
| **Tokenisierung** | Text in Token aufteilen (Wörter, Unterwörter oder Zeichen) | „Ich liebe NLP“ →`["I", "love", "NLP"]`|
| **Kleinschreibung** | In Kleinbuchstaben umwandeln | „Hallo“ → „Hallo“ |
| **Wortentfernung stoppen** | Entfernen Sie gebräuchliche Wörter (the, is, at) | „die Katze saß“ → „die Katze saß“ |
| **Stemming** | Wortendungen abhacken (roh) | „laufen“ → „laufen“ |
| **Lemmatisierung** | Auf Wörterbuchform reduzieren (kontextbewusst) | „besser“ → „gut“ |
| **Normalisierung** | Codierung korrigieren, Sonderzeichen entfernen, Kontraktionen erweitern | „nicht“ → „nicht“ |
Moderne Transformer-Modelle überspringen häufig die Entfernung von Stoppwörtern und die Wortstammerkennung – sie lernen diese Muster aus Daten.
---

## Textdarstellung
Maschinen brauchen Zahlen, keine Worte. Es ist von grundlegender Bedeutung, wie wir Text als Vektoren darstellen.
### Klassische Ansätze
| Methode | Beschreibung | Einschränkung |
|--------|-------------|-----------|
| **One-Hot-Codierung** | Jedes Wort ist eine einzigartige Position in einem riesigen Vektor | Spärlich; keine semantische Bedeutung |
| **Tasche voller Wörter (BoW)** | Worthäufigkeiten zählen; Reihenfolge ignorieren | Wortreihenfolge geht völlig verloren |
| **TF-IDF** | Wörter nach Häufigkeit im Dokument x Seltenheit im Korpus gewichten | Ignoriert immer noch Reihenfolge und Kontext |
### Worteinbettungen
Einbettungen ordnen Wörter dichten Vektoren zu, in denen ähnliche Wörter nahe beieinander liegen.
| Modell | Schlüsselidee |
|-------|----------|
| **Word2Vec** (2013) | Wort aus Kontext (CBOW) oder Kontext aus Wort (Skip-gram) vorhersagen |
| **Handschuh** (2014) | Globale Statistiken zum gleichzeitigen Vorkommen → dichte Vektoren |
| **FastText** (2016) | Word2Vec + Unterwortinformationen (behandelt seltene Wörter besser) |
Das berühmte Beispiel:`king - man + woman ≈ queen`. Einbettungen erfassen semantische Beziehungen.
**Einschränkung**: Klassische Einbettungen weisen einen Vektor pro Wort zu, sodass sie nicht mit Polysemie (Wörtern mit mehreren Bedeutungen) umgehen können. „Bank“ in „Flussufer“ und „Bankkonto“ erhalten den gleichen Vektor.
---

## Sequenzmodelle
Vor Transformers bestand der Standardansatz für NLP darin, Text sequentiell zu verarbeiten.
| Architektur | Wie es funktioniert | Stärke | Schwäche |
|-------------|-------------|----------|----------|
| **RNN** | Verarbeiten Sie Token einzeln; Verborgenen Zustand beibehalten | Verarbeitet Eingaben variabler Länge | Verschwindende Farbverläufe; lange Abhängigkeiten können nicht erfasst werden |
| **LSTM** | RNN mit Gates (Forget, Input, Output) zur Steuerung des Informationsflusses | Besser bei Abhängigkeiten über große Entfernungen | Immer noch sequentiell; langsam zu trainieren |
| **GRU** | Vereinfachtes LSTM (weniger Tore) | Schneller als LSTM; ähnliche Leistung | Dieselben grundlegenden Einschränkungen |
Diese Modelle verarbeiten Text von links nach rechts, was bedeutet, dass sie langsam trainiert werden können (keine Parallelisierung möglich ist) und mit Abhängigkeiten über große Entfernungen zu kämpfen haben.
---

## Der Aufmerksamkeitsmechanismus
Mithilfe der Aufmerksamkeit kann ein Modell alle Positionen in einer Sequenz gleichzeitig betrachten und entscheiden, welche für die aktuelle Vorhersage am relevantesten sind.
### Wichtige Erkenntnisse
Anstatt einen ganzen Satz in einen einzigen verborgenen Zustand zu komprimieren (wie es bei RNNs der Fall ist), berechnet Attention eine gewichtete Summe aller verborgenen Zustände, wobei die Gewichte gelernt werden.
```
Attention(Q, K, V) = softmax(QK^T / √d_k) V
```

| Komponente | Rolle |
|-----------|------|
| **Abfrage (Q)** | Was suche ich? |
| **Schlüssel (K)** | Was ist in mir enthalten? |
| **Wert (V)** | Welche Informationen stelle ich zur Verfügung? |
| **√d_k** | Skalierungsfaktor zur Vermeidung großer Skalarprodukte |
---

## Die Transformer-Architektur
Der Transformer (Vaswani et al., 2017 – „Attention Is All You Need“) ersetzte die Wiederholung vollständig durch Aufmerksamkeit. Es ist die Grundlage praktisch aller modernen NLP.
### Architektur
| Komponente | Beschreibung |
|-----------|-------------|
| **Encoder** | Liest Eingabetext; erzeugt kontextuelle Darstellungen |
| **Decoder** | Erzeugt Ausgabetext; kümmert sich um die Ausgabe des Encoders |
| **Selbstaufmerksamkeit** | Jeder Token kümmert sich um alle anderen Token in derselben Reihenfolge |
| **Mehrkopfaufmerksamkeit** | Führen Sie mehrere Aufmerksamkeitsköpfe parallel aus; verschiedene Beziehungen erfassen |
| **Positionskodierung** | Positionsinformationen einfügen (da es keine Wiederholung gibt) |
| **Feed-Forward-Netzwerk** | Auf jede Position unabhängig anwendbar |
| **Ebenennormalisierung** | Stabilisieren Sie das Training |
| **Restverbindungen** | Verbindungen für Gradientenfluss überspringen |
### Nur Encoder, Nur Decoder, Encoder-Decoder
| Variante | Architektur | Am besten für | Beispiele |
|---------|-------------|----------|---------|
| **Nur Encoder** | Versteht Text | Klassifizierung, NER, Stimmungsanalyse | BERT, RoBERTa, DeBERTa |
| **Nur Decoder** | Erzeugt Text | Sprachmodelle, Chatbots, Codegenerierung | GPT-3/4, LLaMA, Claude |
| **Encoder-Decoder** | Transformiert Text | Übersetzung, Zusammenfassung | T5, BART, mBART |
---

## Wichtige Modellfamilien
### BERT-Familie (nur Encoder)
| Modell | Hauptmerkmal |
|-------|-------------|
| **BERT** (2018) | Maskiertes Sprachmodell + Vorhersage des nächsten Satzes |
| **RoBERTa** | NSP entfernt; länger mit mehr Daten trainiert |
| **ALBERT** | Parameterfreigabe; geringerer Platzbedarf |
| **DeBERTa** | Entwirrte Aufmerksamkeit; verbesserte NLU |
| **DistilBERT** | 40 % kleiner, 60 % schneller, behält 97 % der BERT-Leistung |
### GPT-Familie (nur Decoder)
| Modell | Parameter | Notizen |
|-------|-----------|-------|
| **GPT-2** | 1,5B | Die gezeigten Nur-Decoder-Modelle können kohärenten Text erzeugen |
| **GPT-3** | 175B | Lernen mit wenigen Schüssen; eher angeregt als fein abgestimmt |
| **GPT-3.5 / GPT-4** | Nicht bekannt gegeben | Instruktionsgestimmt + RLHF; Konversation |
| **LLaMA** (Meta) | 7B–70B | Offenes Gewicht; hat das Open-Source-LLM-Ökosystem hervorgebracht |
| **Mistral / Mixtral** | 7B / 8×7B (MoE) | Effiziente offene Modelle mit starker Leistung |
---

## Kernaufgaben des NLP
| Aufgabe | Beschreibung | Typisches Modell |
|------|-------------|--------------|
| **Textklassifizierung** | Weisen Sie dem Text eine Bezeichnung zu (Spam/kein Spam, positiv/negativ) | BERT, fein abgestimmte Klassifikatoren |
| **Named Entity Recognition (NER)** | Identifizieren Sie Personen, Organisationen und Orte im Text | BERT + CRF-Schicht |
| **Stimmungsanalyse** | Bestimmen Sie den emotionalen Ton | Feinabgestimmtes BERT oder Zero-Shot-LLM |
| **Maschinelle Übersetzung** | Zwischen Sprachen übersetzen | T5, mBART, MarianMT |
| **Fragenbeantwortung** | Beantworten Sie Fragen im gegebenen Kontext | BERT (extraktiv), GPT (generativ) |
| **Zusammenfassung** | Langtext verdichten | T5, BART, GPT |
| **Textgenerierung** | Einen kohärenten Text erstellen | GPT-4, LLaMA, Claude |
---

## Feinabstimmung vs. Aufforderung
| Ansatz | Wie es funktioniert | Wann zu verwenden |
|----------|-------------|-------------|
| **Feinabstimmung** | Aktualisieren Sie die Modellgewichte Ihrer aufgabenspezifischen Daten | Sie haben Daten beschriftet; brauchen maximale Leistung |
| **Aufforderung** | Geben Sie den Modellanweisungen in natürlicher Sprache | Schnelles Prototyping; begrenzte Daten; mit LLMs |
| **Wenige Schüsse** | Fügen Sie Beispiele in die Eingabeaufforderung ein | Wenn Sie ein paar Beispiele haben, aber nicht genug für die Feinabstimmung |
| **LoRA / QLoRA** | Effiziente Feinabstimmung; kleine Matrizen mit niedrigem Rang aktualisieren | Feinabstimmung großer Modelle mit begrenztem GPU-Speicher |
---

## Tools und Frameworks
| Werkzeug | Zweck |
|------|---------|
| **Umarmende Gesichtstransformatoren** | Vorab trainierte Modelle, Tokenisierer, Feinabstimmungspipelines |
| **SpaCy** | NLP-Pipeline in Produktionsqualität (Tokenisierung, NER, POS, Abhängigkeit) |
| **NLTK** | Pädagogisch; klassische NLP-Algorithmen |
| **Gensim** | Themenmodellierung (LDA), Worteinbettungen (Word2Vec, Doc2Vec) |
| **LangChain / LlamaIndex** | Frameworks zum Erstellen von LLM-basierten Anwendungen |
| **vLLM** | LLM-Serving mit hohem Durchsatz |
| **Tokenizer (HF)** | Schnelle Tokenisierung (BPE, WordPiece, SentencePiece) |
---

## Die LLM-Landschaft
Die moderne NLP-Landschaft wird von großen Sprachmodellen dominiert:
| Kategorie | Beispiele | Notizen |
|----------|---------|-------|
| **Proprietär** | GPT-4, Claude, Zwillinge | Beste Leistung; Nur API-Zugriff |
| **Offenes Gewicht** | LLaMA 3, Mistral, Qwen | Verfügbare Gewichte; lokal ausführen |
| **Open-Source** | Pythia, OPT | Vollständig geöffnet (Daten, Gewichte, Code) |
| **Multimodal** | GPT-4V, Gemini, LLaVA | Text + Bilder verarbeiten |
| **Code-spezialisiert** | CodeLlama, StarCoder, DeepSeek Coder | Auf Code geschult |
| **Klein / Effizient** | Phi-3, Gemma, TinyLlama | Starke Leistung im kleinen Maßstab |
Das Feld bewegt sich schnell. Was heute auf dem neuesten Stand ist, kann in Monaten überholt sein. Die Grundlagen – Aufmerksamkeit, Tokenisierung, Feinabstimmung, Bewertung – bleiben stabil.