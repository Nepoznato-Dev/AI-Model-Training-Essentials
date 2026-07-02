# Prompt Engineering

Prompt Engineering ist die Praxis, Eingabe-Prompts so zu entwerfen, zu verfeinern und zu optimieren, dass ein Sprachmodell die bestmögliche Ausgabe liefert. Es ist sowohl eine Kunst als auch eine Wissenschaft und die wichtigste Schnittstelle, um das Verhalten von LLMs ohne Fine-Tuning zu steuern.

---

## Grundprinzipien

### Klarheit und Spezifität
Ein klarer Prompt lässt keinen Raum für Mehrdeutigkeit. Gib genau an, was du möchtest, einschließlich Format, Länge und Perspektive.

**Vage:**
> "Erzähl mir etwas über Python."

**Spezifisch:**
> "Erkläre den Global Interpreter Lock (GIL) von Python. Beschreibe seine Auswirkungen auf Multithreading, nenne einen Workaround und halte deine Antwort unter 200 Wörtern."

### Kontext bereitstellen
Modelle performen besser, wenn sie Rolle, Zielgruppe und Ziel kennen.

**Ohne Kontext:**
> "Schreibe eine Funktion zum Sortieren einer Liste."

**Mit Kontext:**
> "Du bist ein erfahrener Python-Entwickler. Schreibe eine Funktion, die eine Liste von Dictionaries anhand eines angegebenen Schlüssels sortiert. Verwende type hints und behandle Edge Cases. Die Zielgruppe sind Junior-Entwickler."

### Positive Anweisungen verwenden
Sage dem Modell, was es tun soll, nicht was es vermeiden soll. „Verwende keinen Jargon“ ist schwächer als „Verwende einfache Sprache, die für ein 10-jähriges Kind verständlich ist.“

---

## Prompt-Strukturen

### Rollen System / User / Assistant
Die meisten LLM-APIs unterstützen eine Multi-Turn-Struktur:

- **System message**: Legt Verhalten, Persona und Einschränkungen des Modells fest (bleibt für die ganze Sitzung erhalten).
- **User message**: Die aktuelle Anfrage oder Anweisung.
- **Assistant message**: Die vorherigen Antworten des Modells (für Kontinuität verwendet).

**Beispiel (OpenAI-API-Stil):**
System: Du bist ein hilfreicher Coding-Assistent. Du antwortest mit knappen Codebeispielen und kurzen Erklärungen. Gib niemals unsicheren Code aus.
User: Schreibe eine Python-Funktion, um eine Datei von einer URL herunterzuladen.

### Few-Shot Prompting
Gib 2–3 Beispiele für das gewünschte Ein-/Ausgabeformat, bevor du das Modell bittest, die Aufgabe auszuführen. So lernt es das Muster.

**Beispiel:**
User: Wandle diese Sätze in das Passiv um:
Input: The cat chased the mouse.
Output: The mouse was chased by the cat.
Input: The chef cooked the meal.
Output: The meal was cooked by the chef.
Input: The storm destroyed the house.
Output: (Modell vervollständigt)

### Chain-of-Thought (CoT)
Fordere das Modell auf, sein Reasoning Schritt für Schritt zu zeigen. Das verbessert die Genauigkeit bei Arithmetik, Logik und mehrstufigen Aufgaben.

**Ohne CoT:**
> "Was ist 24 × 37?"

**Mit CoT:**
> "Berechne 24 × 37. Zeige dein Reasoning Schritt für Schritt."

Das Modell erzeugt Zwischenschritte und reduziert dadurch Rechenfehler.

### Strukturierte Ausgaben
Fordere ein bestimmtes Format wie JSON, YAML oder Markdown-Tabellen an, damit die Verarbeitung zuverlässig bleibt.
User: Liste drei Vor- und drei Nachteile von Microservices auf. Gib nur ein gültiges JSON-Objekt mit den Schlüsseln "pros" und "cons" zurück, jeweils ein Array von Strings.

---

## Fortgeschrittene Techniken

### Self-Consistency
Erzeuge mehrere Antworten auf denselben Prompt (mit einer temperature > 0) und verwende ein Majority Voting für die endgültige Antwort. Das ist besonders effektiv bei Reasoning-Aufgaben.

### Tree-of-Thoughts
Erkunde mehrere Reasoning-Pfade parallel, bewerte jeden und wähle den besten aus. Das ist eine Technik auf Forschungsniveau, lässt sich aber annähern, indem man das Modell auffordert, „alternative Lösungen zu erkunden“.

### ReAct (Reasoning + Acting)
Lass das Modell Reasoning mit Tool-Aufrufen verweben. Es kann nachdenken, dann handeln (z. B. im Web suchen, Code ausführen) und anschließend auf Basis des Ergebnisses erneut nachdenken.

**Prompt-Struktur:**
Du hast Zugriff auf einen Taschenrechner und eine Suchmaschine. Gib für jeden Schritt aus:
Thought: (dein Reasoning)
Action: (Tool-Name, Eingabe)
Observation: (Tool-Ausgabe)
... fahre fort, bis du die endgültige Antwort hast.

### Persona-Zuweisung
Weise eine bestimmte Persona zu, um die Antwort zu rahmen.

**Beispiele:**
- "Du bist ein Linux-Kernel-Entwickler, der Speicherverwaltung einem frisch Graduierten erklärt."
- "Du bist ein freundlicher Ernährungsberater, der einem Klienten allgemeine Ratschläge gibt."
- "Du bist ein zynischer Technikkritiker, der ein neues Gadget rezensiert."

---

## Parameter-Tuning

- **Temperature** (0.0 – 1.0+): Steuert Zufälligkeit. Niedriger = deterministischer, höher = kreativer. Verwende 0.0–0.3 für faktische Antworten; 0.7–1.0 für kreatives Schreiben.
- **Top-p** (nucleus sampling): Schneidet die Wahrscheinlichkeitsmasse an einer bestimmten kumulativen Schwelle ab. 0.9 bedeutet, dass das Modell aus den wahrscheinlichsten 90 % der Tokens sampelt. Normalerweise passt man entweder temperature oder top-p an, nicht beides.
- **Max tokens**: Legt die maximale Ausgabelänge fest. Denke daran, Platz für die Antwort innerhalb des Kontextfensters zu reservieren.
- **Frequency penalty**: Reduziert Wiederholungen derselben Tokens.
- **Presence penalty**: Ermutigt das Modell, neue Themen einzuführen.

---

## Häufige Fallstricke und Korrekturen

| Problem | Wahrscheinliche Ursache | Lösung |
|---------|-------------------------|--------|
| Modell ignoriert Teile des Prompts | Prompt zu lang oder überladen | Kürzen; die wichtigste Anweisung ans Ende setzen |
| Ausgabe ist zu ausführlich | Keine Längenbeschränkung | „Begrenze auf 3 Sätze“ hinzufügen oder max_tokens setzen |
| Ausgabe ist zu knapp | Zu restriktiv | „Erkläre detailliert“ hinzufügen oder temperature senken |
| Faktische Halluzinationen | Unzureichender Kontext oder mehrdeutige Frage | „Wenn du unsicher bist, sage 'I don't know'“ hinzufügen und einen RAG-Kontext bereitstellen |
| Inkonsistentes Format | Keine explizite Formatanweisung | JSON, Markdown-Tabelle oder Aufzählung anfordern |
| Modell antwortet in der falschen Sprache | Keine Sprachvorgabe | Explizit „Respond in English“ (oder die Zielsprache) angeben |

---

## Prompt-Vorlagen für häufige Aufgaben

### Zusammenfassung
Fasse den folgenden Text in 3 Stichpunkten zusammen. Konzentriere dich auf die Hauptargumente und vermeide Details.

Text: [Text einfügen]


### Codegenerierung
Schreibe eine [language]-Funktion, die [X tut].
Requirements:

Use type hints.

Include a docstring.

Handle edge cases: [list].

Do not use external libraries unless specified.


### Erklärung
Erkläre [concept] für eine [nicht fachkundige Person / Universitätsstudentin oder Universitätsstudent / ein Kind]. Verwende, wenn passend, eine Analogie.

### Brainstorming
Generiere 10 Ideen zu [topic]. Gib für jede Idee eine Beschreibung in einem Satz und eine potenzielle Herausforderung an.

Text

### Klassifikation
Klassifiziere das folgende Kundenfeedback als [positive, neutral, negative].
Gib einen Confidence Score (0-100) und einen kurzen Grund an.

Feedback: [Text einfügen]

### Übersetzung mit Stil
Übersetze den folgenden englischen Text ins Spanische. Verwende einen informellen Ton, der für einen Social-Media-Post geeignet ist.
Text: [Text einfügen]

---

## Bewertung von Prompts

Behandle Prompts wie Code: versioniere sie, teste sie und verbessere sie iterativ.

- **A/B-teste** verschiedene Prompt-Varianten auf einem zurückgehaltenen Satz von Anfragen.
- **Miss den Erfolg** durch menschliche Bewertung oder automatisierte Metriken (z. B. exact match, BLEU, benutzerdefinierte Bewertung).
- **Führe ein prompt registry** (eine einfache Textdatei oder Tabelle) mit Prompt, Version und beobachteter Leistung.

---
