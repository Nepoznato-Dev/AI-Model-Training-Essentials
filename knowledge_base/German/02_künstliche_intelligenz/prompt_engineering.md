<!-- 
This file was automatically translated from English to German.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
Für Verbesserungen der Genauigkeit bitten wir um Beiträge via Pull Requests.
-->

# Prompt Engineering

Prompt Engineering ist die Praxis des Entwerfens, Verfeinerns und Optimierens von Eingabeaufforderungen, um die bestmögliche Ausgabe von einem Sprachmodell zu erhalten. Es ist sowohl eine Kunst als auch eine Wissenschaft und es ist die primäre Schnittstelle zur Steuerung des LLM-Verhaltens ohne Fine-Tuning.

---

## Grundprinzipien

### Klarheit und Spezifität
Eine klare Aufforderung lässt keinen Raum für Mehrdeutigkeiten. Geben Sie genau an, was Sie wünschen, einschließlich Format, Länge und Perspektive.

**Unpräzise:**
> "Erzählen Sie mir etwas über Python."

**Spezifisch:**
> "Erklären Sie den Global Interpreter Lock (GIL) von Python. Beschreiben Sie dessen Auswirkung auf Multithreading, nennen Sie einen Workaround und halten Sie Ihre Antwort unter 200 Wörtern."

### Kontext bereitstellen
Modelle leisten bessere Arbeit, wenn sie die Rolle, das Publikum und das Ziel kennen.

**Ohne Kontext:**
> "Schreiben Sie eine Funktion zum Sortieren einer Liste."

**Mit Kontext:**
> "Sie sind ein erfahrener Python-Entwickler. Schreiben Sie eine Funktion zum Sortieren einer Liste von Wörterbüchern nach einem gegebenen Schlüssel. Verwenden Sie Typ-Hinweise und behandeln Sie Grenzfälle. Das Publikum sind Junior-Entwickler."

### Positive Anweisungen verwenden
Sagen Sie dem Modell, was es tun soll, nicht was es vermeiden soll. "Vermeiden Sie Fachjargon" ist schwächer als "Verwenden Sie eine einfache Sprache, die für einen 10-Jährigen verständlich ist."

---

## Prompt-Strukturen

### System-/Benutzer-/Assistenten-Rollen
Die meisten LLM-APIs unterstützen eine Multi-Turn-Struktur:

- **Systemnachricht**: Legt das Verhalten, die Persona und die Einschränkungen des Modells fest (bleibt für die gesamte Sitzung bestehen).
- **Benutzernachricht**: Die aktuelle Anfrage oder Anweisung.
- **Assistentennachricht**: Vorherige Antworten des Modells (wird für Kontinuität verwendet).

**Beispiel (OpenAI API-Stil):**
System: Sie sind ein hilfreicher Coding-Assistent. Sie antworten mit prägnanten Codebeispielen und kurzen Erklärungen. Liefern Sie niemals unsicheren Code.
Benutzer: Schreiben Sie eine Python-Funktion zum Herunterladen einer Datei von einer URL.

### Few-Shot Prompting
Geben Sie 2–3 Beispiele für das gewünschte Eingabe-Ausgabe-Format an, bevor Sie das Modell auffordern, die Aufgabe auszuführen. Dies lehrt das Muster.

**Beispiel:**
Benutzer: Wandeln Sie diese Sätze in die Passivform um:
Eingabe: Die Katze jagte die Maus.
Ausgabe: Die Maus wurde von der Katze gejagt.
Eingabe: Der Koch kochte die Mahlzeit.
Ausgabe: Die Mahlzeit wurde vom Koch gekocht.
Eingabe: Der Sturm zerstörte das Haus.
Ausgabe: (Modell vervollständigt)

### Chain-of-Thought (CoT)
Ermutigen Sie das Modell, seine Überlegungen Schritt für Schritt darzulegen. Dies verbessert die Genauigkeit bei arithmetischen, logischen und mehrstufigen Aufgaben.

**Ohne CoT:**
> "Was ist 24 × 37?"

**Mit CoT:**
> "Berechnen Sie 24 × 37. Zeigen Sie Ihre Überlegungen Schritt für Schritt."

Das Modell wird Zwischenschritte produzieren und dadurch Rechenfehler reduzieren.

### Strukturierte Ausgaben
Fordern Sie ein bestimmtes Format wie JSON, YAML oder Markdown-Tabellen an, um das Parsing zuverlässig zu machen.
Benutzer: Listen Sie drei Vorteile und drei Nachteile von Microservices auf. Geben Sie nur ein gültiges JSON-Objekt mit den Schlüsseln "pros" und "cons" zurück, wobei jeder ein Array von Strings ist.

---

## Fortgeschrittene Techniken

### Selbstkonsistenz
Generieren Sie mehrere Antworten für dieselbe Aufforderung (mit einer Temperatur > 0) und bilden Sie eine Mehrheitsentscheidung über die endgültige Antwort. Dies ist besonders effektiv für reasoning tasks.

### Tree-of-Thoughts
Erkunden Sie mehrere Denkwege parallel, bewerten Sie jeden und wählen Sie den besten aus. Dies ist eine Forschungstechnik, kann aber angenähert werden, indem man das Modell auffordert, "alternative Lösungen zu erkunden".

### ReAct (Reasoning + Acting)
Lassen Sie das Modell Überlegungen mit Tool-Aufrufen abwechseln. Es kann denken, dann handeln (z.B. das Web durchsuchen, Code ausführen), dann basierend auf dem Ergebnis wieder denken.

**Prompt-Struktur:**
Sie haben Zugriff auf einen Taschenrechner und eine Suchmaschine. Für jeden Schritt geben Sie aus:
Thought: (Ihre Überlegung)
Action: (Tool-Name, Eingabe)
Observation: (Tool-Ausgabe)
... fahren Sie fort, bis Sie die endgültige Antwort haben.

### Persona-Zuweisung
Weisen Sie eine spezifische Persona zu, um die Antwort zu rahmen.

**Beispiele:**
- "Sie sind ein Linux-Kernel-Entwickler, der einem Absolventen die Speicherverwaltung erklärt."
- "Sie sind eine freundliche Ernährungsberaterin, die einem Klienten allgemeine Ratschläge gibt."
- "Sie sind ein zynischer Tech-Kritiker, der ein neues Gadget rezensiert."

---

## Parameter-Tuning

- **Temperatur** (0,0 – 1,0+): Steuert die Zufälligkeit. Niedriger = deterministischer, höher = kreativer. Verwenden Sie 0,0–0,3 für faktische Antworten; 0,7–1,0 für kreatives Schreiben.
- **Top-p** (Nucleus Sampling): Schneidet die Wahrscheinlichkeitsmasse bei einem bestimmten kumulativen Schwellenwert ab. 0,9 bedeutet, dass das Modell aus den obersten 90% der wahrscheinlichen Tokens sampelt. Normalerweise passen Sie entweder die Temperatur oder top-p an, nicht beides.
- **Max tokens**: Legt die maximale Ausgabelänge fest. Denken Sie daran, Platz für die Antwort innerhalb des Kontextfensters zu reservieren.
- **Frequency penalty**: Reduziert die Wiederholung derselben Tokens.
- **Presence penalty**: Ermutigt das Modell, neue Themen einzuführen.

---

## Häufige Fallstricke und Lösungen

| Problem | Wahrscheinliche Ursache | Lösung |
|---------|--------------|-----|
| Modell ignoriert Teile der Aufforderung | Aufforderung zu lang oder überladen | Kürzen; setzen Sie die wichtigste Anweisung ans Ende |
| Ausgabe ist zu ausführlich | Keine Längeneinschränkung | Fügen Sie "Auf 3 Sätze beschränken" hinzu oder setzen Sie max_tokens |
| Ausgabe ist zu kurz | Zu einschränkend | Fügen Sie "Ausführlich erklären" hinzu oder senken Sie die Temperatur |
| Faktische Halluzinationen | Unzureichender Kontext oder unklare Frage | Fügen Sie "Wenn Sie unsicher sind, sagen Sie 'Ich weiß es nicht'" hinzu und stellen Sie einen RAG-Kontext bereit |
| Inkonsistente Formatierung | Keine explizite Formatierungsanweisung | Fordern Sie JSON, Markdown-Tabelle oder Aufzählungsliste an |
| Modell antwortet in falscher Sprache | Keine Sprachanweisung | Geben Sie explizit an "Antworten Sie auf Deutsch" (oder Ihre Zielsprache) |

---

## Prompt-Vorlagen für häufige Aufgaben

### Zusammenfassung
Fassen Sie den folgenden Text in 3 Stichpunkten zusammen. Konzentrieren Sie sich auf die Hauptargumente und vermeiden Sie Details.

Text: [Text einfügen]


### Code-Generierung
Schreiben Sie eine [Sprache]-Funktion, die [X tut].
Anforderungen:

Verwenden Sie Typ-Hinweise.

Fügen Sie einen Docstring hinzu.

Behandeln Sie Grenzfälle: [Liste].

Verwenden Sie keine externen Bibliotheken, sofern nicht angegeben.


### Erklärung
Erklären Sie [Konzept] für einen [Laien / Universitätsstudenten / Kind]. Verwenden Sie gegebenenfalls eine Analogie.

### Brainstorming
Generieren Sie 10 Ideen für [Thema]. Geben Sie für jede Idee eine Ein-Satz-Beschreibung und eine potenzielle Herausforderung an.

text

### Klassifizierung
Klassifizieren Sie das folgende Kundenfeedback als [positiv, neutral, negativ].
Geben Sie einen Konfidenzwert (0-100) und einen kurzen Grund an.

Feedback: [Text einfügen]

### Übersetzung mit Stil
Übersetzen Sie den folgenden englischen Text ins Spanische. Verwenden Sie einen informellen Ton, der für einen Social-Media-Beitrag geeignet ist.
Text: [Text einfügen]

---

## Evaluation von Prompts

Behandeln Sie Prompts wie Code: versionieren Sie sie, testen Sie sie und iterieren Sie.

- **A/B-Test** verschiedener Prompt-Varianten auf einem zurückgehaltenen Satz von Abfragen.
- **Erfolg messen** durch menschliche Bewertung oder automatisierte Metriken (z.B. exakte Übereinstimmung, BLEU, benutzerdefinierte Bewertung).
- **Prompt-Registry führen** (eine einfache Textdatei oder Tabelle) mit dem Prompt, Version und beobachteter Leistung.

---