---
# Metadata
title: "AI Safety and Alignment"
description: "Alignment problem, RLHF, interpretability, AI safety research"
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
tags: [ai, safety, alignment, ai-and-machine-learning]
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
# KI-Sicherheit und Ausrichtung
Bei der KI-Sicherheit geht es darum, wie man KI-Systeme baut, die das tun, was wir eigentlich wollen – und keine Dinge tun, die wir nicht wollen, auch wenn diese nicht ausdrücklich ausgeschlossen wurden. Die Ausrichtung ist die besondere Herausforderung, die Ziele und Verhaltensweisen von KI-Systemen an die menschlichen Absichten anzupassen. Da KI-Systeme immer leistungsfähiger werden, verlagern sich diese Fragen von akademischen Kuriositäten hin zu praktischen technischen Anforderungen.
---

## Warum die Ausrichtung schwierig ist
| Problem | Beschreibung | Beispiel |
|---------|-------------|---------|
| **Spezifikation Gaming** | Die KI findet eine Lücke in der Belohnungsfunktion | Ein Bootsrennagent dreht sich im Kreis, um Punkte zu sammeln, anstatt das Rennen zu beenden |
| **Belohnungs-Hacking** | Die KI nutzt das Belohnungssignal auf unbeabsichtigte Weise aus | Ein Agent entdeckt, dass er Belohnungen erhalten kann, indem er wiederholt eine triviale Aktion ausführt |
| **Negative Nebenwirkungen** | Die KI erreicht ihr Ziel, verursacht aber unbeabsichtigten Schaden | Ein Reinigungsroboter schiebt Möbel zur Seite, um schneller zu saugen |
| **Ziele verpasst** | Die KI optimiert für das Falsche | Maximierung des Engagements → Förderung von Empörung und Fehlinformationen |
| **Skalierbare Aufsicht** | Je intelligenter die KI wird, desto schwieriger wird es für Menschen, ihre Ergebnisse zu bewerten | Ein Modell liefert plausibel wirkende, aber subtil falsche juristische Argumente |
Das grundsätzliche Spannungsfeld: Es ist leicht, Ziele schlecht zu spezifizieren. Und KI-Systeme sind äußerst effizient darin, jedes Ziel zu erreichen, das sie tatsächlich verfolgen – nicht unbedingt das Ziel, das Sie ihnen vorgeben wollten.
---

## Ausrichtungstechniken
### RLHF (Reinforcement Learning from Human Feedback)
Der aktuelle Standardansatz zum Ausrichten von Sprachmodellen.
| Schritt | Was passiert | Herausforderung |
|------|-------------|-----------|
| **1. Vorschulung** | Trainieren Sie auf einem großen Textkorpus | Modell lernt Fähigkeiten, aber kein Verhalten |
| **2. SFT** (Überwachte Feinabstimmung) | Feinabstimmung der Demonstrationen guten Verhaltens | Begrenzt durch Qualität und Vielfalt der Demonstrationen |
| **3. Prämienmodell** | Trainieren Sie menschliche Vorlieben zwischen Ausgabepaaren | Teuer; subjektiv; erfasst möglicherweise nicht alle Qualitätsdimensionen |
| **4. PPO-Optimierung** | Optimieren Sie das Modell, um die Ergebnisse des Belohnungsmodells zu maximieren | Kann überoptimieren; Belohnungsmodell ist ein unvollständiger Proxy |
### Verfassungsmäßige KI (CAI)
Der Ansatz von Anthropic: Anstatt sich ausschließlich auf menschliches Feedback zu verlassen, geben Sie dem Modell eine Reihe von Prinzipien (eine „Verfassung“) und lassen Sie es seine eigenen Ergebnisse kritisieren und überarbeiten.
| Schritt | Beschreibung |
|------|-------------|
| **1. Selbstkritik** | Das Modell bewertet seine eigene Reaktion anhand der Verfassung |
| **2. Überarbeitung** | Das Modell schreibt seine Antwort neu, um sie besser an die Prinzipien anzupassen |
| **3. RL aus KI-Feedback (RLAIF)** | Nutzen Sie die eigenen Urteile der KI, um ein Belohnungsmodell zu trainieren |
| Vorteil | Einschränkung |
|-----------|------------|
| Skalierbarer als menschliches Feedback | Die Selbsteinschätzung des Modells ist möglicherweise fehlerhaft |
| Grundsätze sind explizit und überprüfbar | Die Wahl der richtigen Prinzipien ist an sich schon ein Werturteil |
| Kann schädliche Emissionen ohne menschliche Kennzeichnung reduzieren | Kann zu „speichelleckerischem“ Verhalten führen |
### DPO (Direct Preference Optimization)
DPO überspringt das Belohnungsmodell vollständig und optimiert die Richtlinie direkt anhand von Präferenzdaten.
| Aspekt | RLHF | Datenschutzbeauftragter |
|--------|------|-----|
| **Belohnungsmodell** | Erforderlich | Nicht erforderlich |
| **Trainingsstabilität** | Zerbrechlich; viele Hyperparameter | Stabiler; einfacher |
| **Datenanforderungen** | Benötigt Präferenzpaare + Belohnungsmodelltraining | Benötigt nur Präferenzpaare |
| **Leistung** | Stark, wenn es gut abgestimmt ist | Wettbewerbsfähig; manchmal besser |
---

## Interpretierbarkeit
Für die Sicherheit ist es wichtig zu verstehen, *was* ein Modell intern tut – Sie können keine Probleme beheben, die Sie nicht sehen können.
### Mechanistische Interpretierbarkeit
Reverse Engineering der Berechnungen, die ein Modell Neuron für Neuron durchführt.
| Konzept | Beschreibung |
|---------|-------------|
| **Neuronen als Merkmale** | Einzelne Neuronen entsprechen oft interpretierbaren Konzepten (z. B. „ist ein Datum“, „ist Code“) |
| **Schaltungen** | Gruppen von Neuronen, die zusammenarbeiten, um bestimmte Berechnungen durchzuführen |
| **Aufmerksamkeitsmuster** | Welche Token sich um welche anderen Token kümmern – verrät den Informationsfluss |
| **Überlagerung** | Modelle stellen mehr Merkmale dar, als sie über Neuronen verfügen, indem sie Merkmale in überlappenden Richtungen kodieren |
| **Sparse Autoencoder (SAEs)** | Modellaktivierungen in interpretierbare, spärliche Features zerlegen |
### Post-hoc-Erklärungsmethoden
| Methode | Wie es funktioniert | Einschränkung |
|--------|-------------|------------|
| **SHAP** | Schätzen Sie den Beitrag jedes Features zur Ausgabe | Rechenintensiv; Näherungen |
| **LIME** | Passen Sie ein lokales lineares Modell um die Vorhersage | an Instabil; spiegelt nicht die tatsächliche Modelllogik wider |
| **Ausprägungskarten** | Zeigen Sie, welche Eingaberegionen die Ausgabe am stärksten beeinflussen | Kann irreführend sein; Erkläre nicht *warum* |
| **Probing-Klassifikatoren** | Trainieren Sie einfache Klassifikatoren auf Zwischenschichten | Kann Informationen erkennen, die das Modell „kennt“, aber nicht „verwendet“ |
---

## Rotes Teaming
Red Teaming bedeutet, dass systematisch versucht wird, ein KI-System zum Scheitern zu bringen – was zu schädlichen, verzerrten oder falschen Ergebnissen führt –, um Schwachstellen vor dem Einsatz zu finden.
| Geben Sie | ein Beschreibung |
|------|-------------|
| **Automatisiertes Red Teaming** | Verwenden Sie andere KI-Modelle, um gegnerische Eingaben zu generieren |
| **Menschenrotes Teaming** | Erfahrene Tester versuchen, das System zu knacken |
| **Strukturiertes rotes Teaming** | Befolgen Sie eine Methodik (z. B. Tests auf bestimmte Schadenskategorien) |
### Gemeinsame Red-Team-Kategorien
| Kategorie | Was zu testen ist |
|----------|-------------|
| **Jailbreaks** | Kann das Modell dazu verleitet werden, Sicherheitsrichtlinien zu umgehen? |
| **Voreingenommenheit** | Erzeugt das Modell unterschiedliche Ergebnisse für unterschiedliche Bevölkerungsgruppen? |
| **Halluzination** | Stellt das Modell Informationen sicher her? |
| **Datenschutz** | Kann das Modell so gestaltet werden, dass es Trainingsdaten offenlegt? |
| **Werkzeugmissbrauch** | Wenn das Modell über Werkzeuge verfügt, kann es dann dazu verleitet werden, diese zu missbrauchen? |
---

## KI-Governance und -Regulierung
| Rahmen | Region | Hauptmerkmale |
|-----------|--------|-------------|
| **EU AI Act** | European Union | Risikobasierte Klassifizierung; banned practices; Transparenzanforderungen; Bußgelder von bis zu 7 % des weltweiten Umsatzes |
| **US-Exekutivverordnungen** | Vereinigte Staaten | Sicherheitstests für Grenzmodelle; reporting requirements; branchenspezifische Beratung |
| **UK AI Safety Institute** | United Kingdom | Bewertet bahnbrechende KI-Fähigkeiten; veröffentlicht Sicherheitsforschung |
| **Chinas KI-Vorschriften** | China | Rules for generative AI; content labelling; algorithm registration |
| **NIST AI RMF** | International | Risikomanagement-Framework für KI-Systeme |
### Risikoklassifizierung (EU-KI-Gesetz)
| Risikostufe | Beispiele | Anforderungen |
|------------|----------|-------------|
| **Inakzeptabel** | Soziales Scoring durch Regierungen; unterschwellige Manipulation | Verboten |
| **Hoch** | Medizinische KI; autonome Fahrzeuge; Strafverfolgungs-KI | Strenge Konformitätsbewertung; menschliche Aufsicht |
| **Begrenzt** | Chatbots; Deepfakes | Transparenzpflichten (KI-Beteiligung muss offengelegt werden) |
| **Minimal** | Spamfilter; Videospiele | Keine besonderen Anforderungen |
---

## Fehlermodi und Risiken
### Aktuelle Risiken (2026)
| Risiko | Schweregrad | Status |
|------|----------|--------|
| **Voreingenommenheit und Diskriminierung** | Hoch | Aktiv auftretend; viele dokumentierte Fälle |
| **Fehlinformationen** | Hoch | Weit verbreitet; KI-generierte Inhalte werden immer realistischer |
| **Datenschutzverletzungen** | Mittelhoch | Verlust von Trainingsdaten; Überwachungsanwendungen |
| **Arbeitsplatzverdrängung** | Mittel | Beginnend in bestimmten Bereichen (Inhalt, Kundenservice) |
| **Konzentration der Macht** | Mittel | Einige Unternehmen kontrollieren Grenzmodelle |
| **Autonome Waffen** | Mittel | Aktive Entwicklung; internationale Debatte läuft |
### Zukünftige Risiken (debattiert)
| Risiko | Wer ist betroffen | Argument |
|------|----------------|----------|
| **Kontrollverlust** | Sicherheitsforscher (MIRI, ARC) | Superintelligente Systeme sind möglicherweise nicht kontrollierbar |
| **Trügerische Ausrichtung** | Theoretische Forscher | Ein Modell scheint aufeinander abgestimmt zu sein, während es unterschiedliche Ziele verfolgt |
| **Schnelle Fähigkeitssprünge** | Empirische Forscher | Modelle können plötzlich viel leistungsfähiger werden und Sicherheitsmaßnahmen übertreffen |
| **KI-gestützte Pandemien** | Regierungen, Biosicherheitsexperten | KI könnte die Hürde für die Herstellung biologischer Waffen senken |
| **Existenzielles Risiko** | Einige KI-Forscher, Philosophen | Stark umkämpft; manche halten es für das wichtigste Thema; andere halten es für verfrüht |
---

## Modellorganismen der Fehlausrichtung
Forscher untersuchen vereinfachte Fälle, in denen Modelle problematisches Verhalten zeigen, um die zugrunde liegenden Mechanismen zu verstehen.
| Phänomen | Beschreibung |
|------------|-------------|
| **Sandbagging** | Ein Modell schneidet bei Sicherheitsbewertungen absichtlich schlechter ab als es kann |
| **Speichelei** | Ein Modell sagt Benutzern, was sie hören möchten, und nicht, was richtig ist |
| **Belohnungs-Hacking** | Ein Modell findet unbeabsichtigte Wege, sein Belohnungssignal zu maximieren |
| **Zielfehlgeneralisierung** | Ein Modell verfolgt in neuen Umgebungen das falsche Ziel |
| **Instrumentelle Konvergenz** | Ein Modell strebt nach Macht, Ressourcen oder Selbsterhaltung als Mittel zur Erreichung seiner Ziele |
---

## Praktische Sicherheitstechnik
Dinge, die KI-Systeme heute in der Praxis sicherer machen.
| Üben | Beschreibung |
|----------|-------------|
| **Systemaufforderungen mit Leitplanken** | Explizite Anweisungen darüber, was das Modell tun und was nicht |
| **Ausgabefilterung** | Nachbearbeitung zur Erkennung und Blockierung schädlicher Inhalte |
| **Ratenbegrenzung** | Verhindern Sie Missbrauch, indem Sie API-Aufrufe einschränken |
| **Human-in-the-Loop** | Erfordern die menschliche Zustimmung für hochriskante Aktionen |
| **Sandboxing** | Beschränken Sie, worauf die KI zugreifen kann (kein Internet, kein Dateisystem usw.) |
| **Audit-Protokollierung** | Alle Interaktionen zur Überprüfung aufzeichnen |
| **Schrittweise Bereitstellung** | Beginnen Sie mit eingeschränktem Zugriff; erweitern, wenn die Sicherheit nachgewiesen wird |
| **Verfassungsgrundsätze** | Explizite Richtlinien, denen das Modell in allen Kontexten folgt |
---

## Schlüsselorganisationen
| Organisation | Fokus |
|-------------|-------|
| **Anthropisch** | KI-Sicherheitsforschung; Verfassungsmäßige KI; Claude |
| **DeepMind-Sicherheit** | Grenzsicherheitsforschung in Google DeepMind |
| **MIRI** | Theoretische Ausrichtungsforschung; Interpretierbarkeit |
| **ARC (KI-Forschungszentrum)** | Empirische Sicherheitsforschung; skalierbare Aufsicht |
| **Zentrum für KI-Sicherheit (CAIS)** | Forschungskoordination; politische Interessenvertretung |
| **AI Safety Institute (UK)** | Regierungsevaluierung von Grenzmodellen |
| **NIST** | Standards und Frameworks für das KI-Risikomanagement |
---

## Zusammenfassung
KI-Sicherheit und Ausrichtung sind keine gelösten Probleme. Aktuelle Techniken – RLHF, Constitutional AI, DPO, Red Teaming – machen Modelle sicherer, garantieren aber keine Sicherheit. Die Interpretierbarkeitsforschung macht Fortschritte beim Verständnis dessen, was Modelle intern tun, aber wir sind noch weit davon entfernt, große neuronale Netze vollständig zu verstehen. Die Governance-Landschaft entwickelt sich rasant weiter, allen voran das EU-KI-Gesetz. Die zentrale Herausforderung bleibt bestehen: Wie stellen Sie sicher, dass immer leistungsfähigere KI-Systeme das tun, was wir wollen, wenn das, was wir wollen, selbst für uns selbst oft nur unzureichend definiert ist?