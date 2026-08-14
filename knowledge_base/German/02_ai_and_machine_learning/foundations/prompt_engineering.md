<!--
---
# Metadata
title: "Prompt Engineering"
description: "Prompt techniques and strategies"
category: "AI and Machine Learning"
subcategory: "Foundations"
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
    changes: "Moved to foundations/ subfolder; added subcategory field"
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
tags: [prompt, engineering, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Schnelles Engineering
Unter Prompt Engineering versteht man die Praxis des Entwerfens, Verfeinerns und Optimierens von Eingabeaufforderungen, um die bestmögliche Ausgabe eines Sprachmodells zu erzielen. Es ist sowohl eine Kunst als auch eine Wissenschaft und die primäre Schnittstelle zur Steuerung des LLM-Verhaltens ohne Feinabstimmung.
---

## Grundprinzipien
### Klarheit und Spezifität
Eine klare Aufforderung lässt keinen Raum für Unklarheiten. Geben Sie genau an, was Sie möchten, einschließlich Format, Länge und Perspektive.
**Vage:**
> „Erzähl mir etwas über Python.“
**Spezifisch:**
> „Erklären Sie Pythons Global Interpreter Lock (GIL). Beschreiben Sie seine Auswirkungen auf Multithreading, geben Sie einen Workaround an und beschränken Sie Ihre Antwort auf weniger als 200 Wörter.“
### Geben Sie Kontext an
Models schneiden besser ab, wenn sie die Rolle, das Publikum und das Ziel kennen.
**Ohne Kontext:**
> „Schreiben Sie eine Funktion zum Sortieren einer Liste.“
**Mit Kontext:**
> „Sie sind ein erfahrener Python-Entwickler. Schreiben Sie eine Funktion, um eine Liste von Wörterbüchern nach einem bestimmten Schlüssel zu sortieren. Verwenden Sie Typhinweise und behandeln Sie Randfälle. Die Zielgruppe sind Nachwuchsentwickler.“
### Verwenden Sie positive Anweisungen
Sagen Sie dem Modell, was es tun soll, nicht was es vermeiden soll. „Keine Fachsprache verwenden“ ist schwächer als „Verwenden Sie eine einfache Sprache, die einem 10-Jährigen verständlich ist.“
---

## Prompt-Strukturen
### System-/Benutzer-/Assistentenrollen
Die meisten LLM-APIs unterstützen eine Multiturn-Struktur:
- **Systemmeldung**: Legt das Verhalten, die Persona und die Einschränkungen des Modells fest (bleibt für die gesamte Sitzung bestehen).
- **Benutzernachricht**: Die aktuelle Abfrage oder Anweisung.
- **Assistentennachricht**: Die vorherigen Antworten des Modells (aus Gründen der Kontinuität verwendet).
**Beispiel (OpenAI-API-Stil):**
System: Sie sind ein hilfreicher Programmierassistent. Sie antworten mit prägnanten Codebeispielen und kurzen Erklärungen. Geben Sie niemals unsicheren Code an.
Benutzer: Schreiben Sie eine Python-Funktion, um eine Datei von einer URL herunterzuladen.
### Wenige-Schuss-Eingabeaufforderung
Geben Sie zwei bis drei Beispiele für das gewünschte Eingabe-Ausgabe-Format an, bevor Sie das Modell bitten, die Aufgabe auszuführen. Dies lehrt das Muster.
**Beispiel:**
Benutzer: Wandeln Sie diese Sätze ins Passiv um:
Eingabe: Die Katze hat die Maus gejagt.
Ausgabe: Die Maus wurde von der Katze gejagt.
Eingabe: Der Koch hat das Essen zubereitet.
Ausgabe: Das Essen wurde vom Koch zubereitet.
Eingabe: Der Sturm hat das Haus zerstört.
Ausgabe: (Modell abgeschlossen)
### Chain-of-Thought (CoT)
Ermutigen Sie das Modell, seine Argumentation Schritt für Schritt darzulegen. Dies verbessert die Genauigkeit bei arithmetischen, logischen und mehrstufigen Aufgaben.
**Ohne Kinderbett:**
> „Was ist 24 × 37?“
**Mit Kinderbett:**
> „Berechnen Sie 24 × 37. Zeigen Sie Ihre Argumentation Schritt für Schritt.“
Das Modell erzeugt Zwischenschritte und reduziert so Rechenfehler.
### Strukturierte Ausgaben
Fordern Sie ein bestimmtes Format wie JSON, YAML oder Markdown-Tabellen an, um das Parsen zuverlässig zu gestalten.
Benutzer: Nennen Sie drei Vor- und Nachteile von Microservices. Geben Sie nur ein gültiges JSON-Objekt mit den Schlüsseln „pros“ und „cons“ zurück, jeweils ein Array von Zeichenfolgen.
---

## Fortgeschrittene Techniken
### Selbstkonsistenz
Generieren Sie mehrere Antworten für dieselbe Eingabeaufforderung (mit einer Temperatur > 0) und stimmen Sie mit der Mehrheit über die endgültige Antwort ab. Dies ist besonders effektiv bei Denkaufgaben.
### Baum der Gedanken
Erkunden Sie mehrere Argumentationspfade parallel, bewerten Sie jeden und wählen Sie den besten aus. Hierbei handelt es sich um eine Technik auf Forschungsebene, die jedoch angenähert werden kann, indem das Modell aufgefordert wird, „alternative Lösungen zu erkunden“.
### ReAct (Begründung + Handeln)
Lassen Sie das Modell Argumentation mit Werkzeugaufrufen verschränken. Es kann denken, dann handeln (z. B. das Web durchsuchen, Code ausführen) und dann basierend auf dem Ergebnis noch einmal nachdenken.
**Eingabeaufforderungsstruktur:**
Sie haben Zugriff auf einen Rechner und eine Suchmaschine. Geben Sie für jeden Schritt Folgendes aus:
Gedanke: (Ihre Argumentation)
Aktion: (Werkzeugname, Eingabe)
Beobachtung: (Werkzeugausgabe)
... fahren Sie fort, bis Sie die endgültige Antwort haben.
### Persona-Zuweisung
Weisen Sie eine bestimmte Persona zu, um die Antwort zu gestalten.
**Beispiele:**
- „Sie sind ein Linux-Kernel-Entwickler und erklären einem neuen Absolventen die Speicherverwaltung.“
- „Sie sind ein freundlicher Ernährungsberater, der einem Kunden allgemeine Ratschläge gibt.“
– „Sie sind ein zynischer Technikkritiker, der ein neues Gerät rezensiert.“
---

## Parameteroptimierung
- **Temperatur** (0,0 – 1,0+): Steuert die Zufälligkeit. Niedriger = deterministischer, höher = kreativer. Für sachliche Antworten verwenden Sie 0,0–0,3; 0,7–1,0 für kreatives Schreiben.
- **Top-p** (Kernprobenahme): Schneidet die Wahrscheinlichkeitsmasse bei einem bestimmten kumulativen Schwellenwert ab. 0,9 bedeutet, dass die Modellproben aus den oberen 90 % der wahrscheinlichen Token stammen. Passen Sie normalerweise entweder die Temperatur oder den Top-P-Wert an, nicht beides.
- **Max. Tokens**: Legt die maximale Ausgabelänge fest. Denken Sie daran, im Kontextfenster Platz für die Antwort zu reservieren.
- **Häufigkeitsnachteil**: Reduziert die Wiederholung derselben Token.
- **Präsenzstrafe**: Ermutigt das Modell, neue Themen einzuführen.
---

## Häufige Fallstricke und Lösungen
| Problem | Wahrscheinliche Ursache | Fix |
|---------|--------------|-----|
| Das Modell ignoriert Teile der Eingabeaufforderung | Eingabeaufforderung zu lang oder überlastet | Verkürzen; Setzen Sie die wichtigste Anweisung ans Ende |
| Die Ausgabe ist zu ausführlich | Keine Längenbeschränkung | Fügen Sie „Auf 3 Sätze beschränken“ hinzu oder legen Sie max_tokens | fest
| Die Ausgabe ist zu knapp | Zu restriktiv | „Im Detail erklären“ hinzufügen oder Temperatur senken |
| Faktische Halluzinationen | Unzureichender Kontext oder mehrdeutige Frage | Fügen Sie „Wenn Sie unsicher sind, sagen Sie ‚Ich weiß es nicht‘“ hinzu und geben Sie einen RAG-Kontext an |
| Inkonsistente Formatierung | Keine explizite Formatanweisung | Fragen Sie nach JSON, Markdown-Tabelle oder Aufzählungsliste |
| Musterantworten in falscher Sprache | Kein Sprachunterricht | Geben Sie ausdrücklich „Auf Englisch antworten“ (oder Ihre Zielsprache) an |
---

## Eingabeaufforderungsvorlagen für häufige Aufgaben
### Zusammenfassung
Fassen Sie den folgenden Text in drei Aufzählungspunkten zusammen. Konzentrieren Sie sich auf die Hauptargumente und vermeiden Sie Details.
Text: [Text einfügen]

### Codegenerierung
Schreiben Sie eine [Sprache]-Funktion, die [X ausführt].
Anforderungen:
Verwenden Sie Typhinweise.
Fügen Sie eine Dokumentzeichenfolge ein.
Randfälle behandeln: [Liste].
Verwenden Sie keine externen Bibliotheken, sofern nicht anders angegeben.

### Erklärung
Erklären Sie [Konzept] einem [Nichtfachmann/Universitätsstudent/Kind]. Verwenden Sie gegebenenfalls eine Analogie.
### Brainstorming
Generieren Sie 10 Ideen für [Thema]. Geben Sie für jede Idee eine Beschreibung in einem Satz und eine mögliche Herausforderung an.
Text
### Klassifizierung
Klassifizieren Sie das folgende Kundenfeedback als [positiv, neutral, negativ].
Geben Sie einen Konfidenzwert (0–100) und einen kurzen Grund an.
Feedback: [Text einfügen]
### Übersetzung mit Stil
Übersetzen Sie den folgenden englischen Text ins Spanische. Verwenden Sie einen informellen Ton, der zu einem Social-Media-Beitrag passt.
Text: [Text einfügen]
---

## Auswertung von Eingabeaufforderungen
Behandeln Sie Eingabeaufforderungen als Code: Versionieren Sie sie, testen Sie sie und iterieren Sie.
- **A/B-Test** verschiedener Eingabeaufforderungsvarianten für eine zurückgehaltene Reihe von Abfragen.
- **Erfolg messen** durch menschliche Bewertung oder automatisierte Metriken (z. B. genaue Übereinstimmung, BLEU, benutzerdefinierte Bewertung).
- **Führen Sie eine Eingabeaufforderungsregistrierung** (eine einfache Textdatei oder Tabelle) mit der Eingabeaufforderung, der Version und der beobachteten Leistung.
---