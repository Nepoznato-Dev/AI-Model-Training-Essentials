<!-- 
This file was automatically translated from English to German.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
Für Verbesserungen der Genauigkeit bitten wir um Beiträge via Pull Requests.
-->

# Prompt Engineering

Prompt Engineering ist die Praxis, Eingabeaufforderungen so zu entwerfen, zu verfeinern und zu optimieren, dass ein Sprachmodell die bestmögliche Ausgabe erzeugt. Es ist zugleich Handwerk und Wissenschaft und die wichtigste Schnittstelle, um das Verhalten eines LLM ohne Fine-Tuning zu steuern.

---

## Grundprinzipien

### Klarheit und Spezifität
Eine klare Eingabeaufforderung lässt keinen Raum für Mehrdeutigkeiten. Geben Sie genau an, was Sie möchten, einschließlich Format, Länge und Perspektive.

**Unpräzise:**
> "Erzählen Sie mir etwas über Python."

**Spezifisch:**
> "Erklären Sie den Global Interpreter Lock (GIL) von Python. Beschreiben Sie seine Auswirkungen auf Multithreading, nennen Sie einen Workaround und halten Sie Ihre Antwort unter 200 Wörtern."

### Kontext bereitstellen
Modelle liefern bessere Ergebnisse, wenn sie Rolle, Zielgruppe und Ziel kennen.

**Ohne Kontext:**
> "Schreiben Sie eine Funktion zum Sortieren einer Liste."

**Mit Kontext:**
> "Sie sind ein erfahrener Python-Entwickler. Schreiben Sie eine Funktion, die eine Liste von Wörterbüchern nach einem angegebenen Schlüssel sortiert. Verwenden Sie Typ-Hinweise und berücksichtigen Sie Randfälle. Die Zielgruppe sind Junior-Entwickler."

### Positive Anweisungen verwenden
Sagen Sie dem Modell lieber, was es tun soll, als nur, was es vermeiden soll. "Vermeiden Sie Fachjargon" ist schwächer als "Verwenden Sie einfache Sprache, die ein 10-jähriges Kind verstehen kann."

---

## Prompt-Strukturen

### System-/Benutzer-/Assistenten-Rollen
Die meisten LLM-APIs unterstützen eine Multi-Turn-Struktur:

- **Systemnachricht**: Legt Verhalten, Persona und Einschränkungen des Modells fest und gilt für die gesamte Sitzung.
- **Benutzernachricht**: Die aktuelle Anfrage oder Anweisung.
- **Assistentennachricht**: Frühere Antworten des Modells, die für Kontinuität sorgen.

**Beispiel (OpenAI API-Stil):**
System: Sie sind ein hilfreicher Coding-Assistent. Sie antworten mit prägnanten Codebeispielen und kurzen Erklärungen. Geben Sie niemals unsicheren Code aus.
Benutzer: Schreiben Sie eine Python-Funktion zum Herunterladen einer Datei von einer URL.

### Few-Shot Prompting
Geben Sie vor der eigentlichen Aufgabe 2–3 Beispiele für das gewünschte Ein- und Ausgabeformat an. So lernt das Modell das Muster.

**Beispiel:**
Benutzer: Wandeln Sie diese Sätze ins Passiv um:
Eingabe: Die Katze jagte die Maus.
Ausgabe: Die Maus wurde von der Katze gejagt.
Eingabe: Der Koch kochte die Mahlzeit.
Ausgabe: Die Mahlzeit wurde vom Koch gekocht.
Eingabe: Der Sturm zerstörte das Haus.
Ausgabe: (Modell vervollständigt)

### Chain-of-Thought (CoT)
Ermutigen Sie das Modell, seine Überlegungen Schritt für Schritt offenzulegen. Das verbessert die Genauigkeit bei arithmetischen, logischen und mehrstufigen Aufgaben.

**Ohne CoT:**
> "Was ist 24 × 37?"

**Mit CoT:**
> "Berechnen Sie 24 × 37. Zeigen Sie Ihre Überlegungen Schritt für Schritt."

Das Modell erzeugt Zwischenschritte und reduziert dadurch Rechenfehler.

### Strukturierte Ausgaben
Fordern Sie ein bestimmtes Format wie JSON, YAML oder Markdown-Tabellen an, damit die Ausgabe zuverlässig weiterverarbeitet werden kann.
Benutzer: Nennen Sie drei Vorteile und drei Nachteile von Microservices. Geben Sie nur ein gültiges JSON-Objekt mit den Schlüsseln "pros" und "cons" zurück, wobei jeder Schlüssel ein Array aus Strings enthält.

---

## Fortgeschrittene Techniken

### Selbstkonsistenz
Erzeugen Sie mehrere Antworten auf denselben Prompt (mit einer Temperatur > 0) und bestimmen Sie per Mehrheitsentscheidung die endgültige Antwort. Das ist besonders wirksam bei Aufgaben mit starkem reasoning-Anteil.

### Tree-of-Thoughts
Erkunden Sie mehrere Denkpfade parallel, bewerten Sie diese und wählen Sie anschließend den besten aus. Das ist eine Forschungstechnik, lässt sich aber annähern, indem man das Modell auffordert, „alternative Lösungen zu erkunden“.

### ReAct (Reasoning + Acting)
Lassen Sie das Modell Überlegungen und Tool-Aufrufe abwechseln. Es kann erst denken, dann handeln (z. B. das Web durchsuchen oder Code ausführen) und auf Grundlage des Ergebnisses weiterdenken.

**Prompt-Struktur:**
Sie haben Zugriff auf einen Taschenrechner und eine Suchmaschine. Geben Sie für jeden Schritt Folgendes aus:
Thought: (Ihre Überlegung)
Action: (Tool-Name, Eingabe)
Observation: (Tool-Ausgabe)
... fahren Sie fort, bis Sie die endgültige Antwort haben.

### Persona-Zuweisung
Weisen Sie dem Modell eine bestimmte Persona zu, um die Antwort passend zu rahmen.

**Beispiele:**
- "Sie sind ein Linux-Kernel-Entwickler, der einem Berufseinsteiger die Speicherverwaltung erklärt."
- "Sie sind eine freundliche Ernährungsberaterin, die einem Klienten allgemeine Ratschläge gibt."
- "Sie sind ein zynischer Tech-Kritiker, der ein neues Gadget rezensiert."

---

## Parameter-Tuning

- **Temperatur** (0,0 – 1,0+): Steuert die Zufälligkeit. Niedriger = deterministischer, höher = kreativer. Verwenden Sie 0,0–0,3 für faktische Antworten und 0,7–1,0 für kreatives Schreiben.
- **Top-p** (Nucleus Sampling): Schneidet die Wahrscheinlichkeitsmasse bei einem bestimmten kumulativen Schwellenwert ab. 0,9 bedeutet, dass das Modell aus den wahrscheinlichsten 90 % der Tokens sampelt. Normalerweise passt man entweder Temperatur oder top-p an, nicht beides.
- **Max tokens**: Legt die maximale Ausgabelänge fest. Reservieren Sie im Kontextfenster genügend Platz für die Antwort.
- **Frequency penalty**: Verringert die Wiederholung derselben Tokens.
- **Presence penalty**: Ermutigt das Modell, neue Themen einzubringen.

---

## Häufige Fallstricke und Lösungen

| Problem | Wahrscheinliche Ursache | Lösung |
|---------|--------------|-----|
| Modell ignoriert Teile der Aufforderung | Prompt zu lang oder überladen | Kürzen; die wichtigste Anweisung ans Ende setzen |
| Ausgabe ist zu ausführlich | Keine Längenbegrenzung | "Auf 3 Sätze beschränken" hinzufügen oder `max_tokens` setzen |
| Ausgabe ist zu kurz | Zu stark eingeschränkt | "Ausführlicher erklären" hinzufügen oder die Temperatur erhöhen |
| Faktische Halluzinationen | Unzureichender Kontext oder unklare Frage | "Wenn Sie unsicher sind, sagen Sie 'Ich weiß es nicht'" ergänzen und RAG-Kontext bereitstellen |
| Inkonsistente Formatierung | Keine explizite Formatvorgabe | JSON, Markdown-Tabelle oder Aufzählungsliste verlangen |
| Modell antwortet in der falschen Sprache | Keine Sprachvorgabe | Explizit anweisen: "Antworten Sie auf Deutsch" (oder in der gewünschten Sprache) |

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

Behandeln Sie Randfälle: [Liste].

Verwenden Sie keine externen Bibliotheken, sofern nicht anders angegeben.


### Erklärung
Erklären Sie [Konzept] für einen [Laien / Universitätsstudenten / ein Kind]. Verwenden Sie bei Bedarf eine Analogie.

### Brainstorming
Generieren Sie 10 Ideen für [Thema]. Geben Sie zu jeder Idee eine Ein-Satz-Beschreibung und eine mögliche Herausforderung an.

Text

### Klassifizierung
Klassifizieren Sie das folgende Kundenfeedback als [positiv, neutral, negativ].
Geben Sie einen Konfidenzwert (0–100) und eine kurze Begründung an.

Feedback: [Text einfügen]

### Übersetzung mit Stil
Übersetzen Sie den folgenden englischen Text ins Spanische. Verwenden Sie einen informellen Ton, der sich für einen Social-Media-Beitrag eignet.
Text: [Text einfügen]

---

## Bewertung von Prompts

Behandeln Sie Prompts wie Code: versionieren Sie sie, testen Sie sie und verbessern Sie sie iterativ.

- **A/B-Tests** verschiedener Prompt-Varianten auf einem zurückgehaltenen Satz von Abfragen.
- **Erfolg messen** durch menschliche Bewertung oder automatisierte Metriken (z. B. exakte Übereinstimmung, BLEU, benutzerdefinierte Bewertung).
- **Prompt-Registry führen** (z. B. als einfache Textdatei oder Tabelle) mit Prompt, Version und beobachteter Leistung.

---
