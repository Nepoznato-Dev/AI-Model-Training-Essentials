---
# Metadata
title: "Testing Methodologies"
description: "Unit, integration, E2E, TDD, BDD, test pyramids"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [testing, methodologies, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Testmethoden
Durch das Testen gewinnen Sie die Gewissheit, dass Ihr Code funktioniert – und, was noch wichtiger ist, dass Änderungen daran nicht das zerstören, was bereits funktioniert. Gute Tests erkennen Fehler, bevor es Benutzer tun, dokumentieren das erwartete Verhalten und ermöglichen ein angstfreies Refactoring. Diese Datei deckt das gesamte Spektrum an Teststrategien ab, von Unit-Tests bis hin zu End-to-End-Tests, und die Prinzipien, die Tests effektiv machen.
---

## Die Testpyramide
Die Testpyramide beschreibt die ideale Verteilung der Tests in einem Projekt.
```
        /  E2E  \          ← Few; slow; expensive; test the whole system
       /─────────\
      / Integration\       ← Some; test how components work together
     /───────────────\
    /   Unit Tests    \    ← Many; fast; cheap; test individual functions
   /─────────────────────\
```

| Ebene | Zählen | Geschwindigkeit | Kosten | Was es testet |
|-------|-------|-------|------|---------------|
| **Einheit** | Viele | Schnell (ms) | Niedrig | Einzelne Funktionen, Klassen, Methoden |
| **Integration** | Einige | Mittel (100 ms-s) | Mittel | Wie Komponenten interagieren; Datenbankabfragen; API-Aufrufe |
| **E2E** | Wenige | Langsam (Sekunden-Minuten) | Hoch | Vollständige Benutzerströme durch das reale System |
---

## Unit-Test
Testen einzelner Codeeinheiten isoliert.
### Prinzipien
| Prinzip | Beschreibung |
|-----------|-------------|
| **Schnell** | Jeder Test sollte in Millisekunden ausgeführt werden |
| **Isoliert** | Tests sind nicht voneinander abhängig; kein gemeinsamer Zustand |
| **Deterministisch** | Gleiche Eingabe → jedes Mal gleiche Ausgabe (keine Zufälligkeit, keine Zeitabhängigkeit) |
| **Selbstkontrolle** | Der Test wird automatisch bestanden oder nicht bestanden. keine manuelle Inspektion |
| **Rechtzeitig** | Wird neben oder vor dem Code geschrieben (TDD) |
### Anatomie eines Tests
| Phase | Beschreibung |
|-------|-------------|
| **Anordnen** | Richten Sie die Testdaten und Abhängigkeiten ein |
| **Handeln** | Rufen Sie die zu testende Funktion oder Methode auf |
| **Behaupten** | Überprüfen Sie, ob das Ergebnis den Erwartungen entspricht |
### Was zu testen ist
| Kategorie | Beispiele |
|----------|---------|
| **Glücklicher Weg** | Normale Eingaben erzeugen erwartete Ausgaben |
| **Randfälle** | Leere Eingabe, Null, Null, Maximalwerte, einzelnes Element |
| **Fehlerfälle** | Ungültige Eingabe, fehlende Daten, Berechtigung verweigert |
| **Randbedingungen** | Weg für eins; genau an den Grenzen |
### Spott und Stubbing
| Begriff | Beschreibung | Wann zu verwenden |
|------|-------------|-------------|
| **Mock** | Ein gefälschtes Objekt, das aufzeichnet, wie es aufgerufen wurde | Interaktionen überprüfen (wurde diese Methode aufgerufen?) |
| **Stub** | Ein gefälschtes Objekt, das vorgegebene Werte zurückgibt | Bereitstellung von Testdaten (diesen Benutzer aus der Datenbank zurückgeben) |
| **Spion** | Ein Wrapper, der Aufrufe an ein reales Objekt | aufzeichnet Teilweise Überprüfung |
| **Fälschung** | Eine vereinfachte, aber funktionierende Implementierung | In-Memory-Datenbank für Tests |
| Spottbibliothek | Sprache |
|----------------|--------|
| **unittest.mock** | Python |
| **Scherz** | JavaScript/TypeScript |
| **Mockito** | Java |
| **Moq** | C# |
| **aussagen / gomock** | Geh |
---

## Integrationstests
Testen, wie mehrere Komponenten zusammenarbeiten.
| Was zu testen ist | Beispiel |
|-------------|---------|
| **Datenbankabfragen** | Erzeugt der ORM korrektes SQL? Werden Indizes verwendet? |
| **API-Endpunkte** | Funktioniert der vollständige Anfrage-Antwort-Zyklus? |
| **Dienstinteraktionen** | Ruft Dienst A Dienst B korrekt auf? |
| **Externe Abhängigkeiten** | Funktioniert die Integration des Zahlungsgateways? |
### Strategien
| Strategie | Beschreibung | Kompromiss |
|----------|-------------|-----------|
| **Echte Abhängigkeiten** | Verwenden Sie eine echte Datenbank, eine echte Nachrichtenwarteschlange | Am realistischsten; Langsamer; schwieriger einzurichten |
| **Testbehälter** | Docker-Container für jeden Testlauf hochfahren | Gute Balance; reproduzierbar |
| **In-Memory-Alternativen** | H2 statt PostgreSQL; In-Memory-Nachrichtenbus | Schnell; kann reale Probleme übersehen |
| **Vertragstests** | Stellen Sie sicher, dass die Dienste ihre API-Verträge einhalten | Fängt Schnittstellenänderungen ab |
---

## End-to-End (E2E)-Tests
Testen des Gesamtsystems aus Anwendersicht.
| Werkzeug | Geben Sie | ein Am besten für |
|------|------|----------|
| **Dramatiker** | Browser-Automatisierung | Webanwendungen; browserübergreifend |
| **Zypresse** | Browser-Automatisierung | Webanwendungen; Entwicklererfahrung |
| **Selen** | Browser-Automatisierung | Vermächtnis; breite Sprachunterstützung |
| **Entgiftung** | Mobiles E2E | Native Apps reagieren |
| **Appium** | Mobiles E2E | Native und hybride mobile Apps |
| **Maestro** | Mobiles E2E | Mobile Apps; einfache YAML-Syntax |
| **k6 / Heuschrecke** | Belastungstest | Leistung unter Last |
### Best Practices für E2E
| Üben | Warum |
|----------|-----|
| **Nur kritische Pfade testen** | E2E-Tests sind langsam; Konzentrieren Sie sich auf das Wesentliche |
| **Testdatenfabriken verwenden** | Testdaten programmgesteuert erstellen; Verlassen Sie sich nicht auf Seed-Daten |
| **Nach den Tests aufräumen** | Jeder Test sollte das System in einem bekannten Zustand verlassen |
| **Vermeiden Sie das Testen von UI-Details** | Testverhalten, nicht CSS-Klassen oder Elementpositionen |
| **In CI ausführen** | E2E-Tests müssen bei jeder Änderung automatisch ausgeführt werden |
---

## Testgetriebene Entwicklung (TDD)
Schreiben Sie zuerst den Test und dann den Code, um ihn zu bestehen.
| Schritt | Beschreibung |
|------|-------------|
| **1. Rot** | Schreiben Sie einen fehlgeschlagenen Test, der das gewünschte Verhalten beschreibt |
| **2. Grün** | Schreiben Sie den Mindestcode, damit der Test erfolgreich ist |
| **3. Refaktorieren** | Bereinigen Sie den Code, während die Tests grün bleiben |
| Nutzen | Beschreibung |
|---------|-------------|
| **Design-Feedback** | Tests zwingen Sie, vor der Implementierung über Schnittstellen nachzudenken |
| **Regressionssicherheit** | Jeder Fehler wird einem Test unterzogen; Der Fehler kann niemals zurückkehren |
| **Dokumentation** | Tests dienen der lebendigen Dokumentation erwarteten Verhaltens |
| **Vertrauen** | Hohe Testabdeckung ermöglicht angstfreies Refactoring |
---

## Verhaltensgesteuerte Entwicklung (BDD)
BDD erweitert TDD durch das Schreiben von Tests in natürlicher Sprache, die das Verhalten aus der Perspektive des Benutzers beschreiben.
### Gegeben-Wann-Dann-Format
```
Given a user with an empty shopping cart
When they add a "Python Book" priced at $29.99
Then the cart total should be $29.99
And the cart should contain 1 item
```

| Werkzeug | Sprache |
|------|----------|
| **Gurke** | Java, JavaScript, Ruby und andere |
| **Benimm dich** | Python |
| **SpecFlow** | C# |
| **Scherz** (mit beschreiben/es) | JavaScript |
---

## Andere Testarten
| Geben Sie | ein Was es testet | Werkzeuge |
|------|--------------|-------|
| **Leistung/Last** | Systemverhalten unter Last | k6, JMeter, Locust, Gatling |
| **Sicherheit** | Schwachstellen und Angriffsvektoren | OWASP ZAP, Burp Suite, Snyk |
| **Barrierefreiheit** | WCAG-Konformität | Axt, Leuchtturm, pa11y |
| **Vertrag** | API-Kompatibilität zwischen Diensten | Pakt, Spring Cloud-Vertrag |
| **Mutation** | Qualität der Testsuite selbst | Stryker, mutmut, PIT |
| **Visuelle Regression** | UI-Änderungen zwischen Versionen | Percy, Chromatic, BackstopJS |
| **Chaos** | Ausfallsicherheit des Systems | Chaosaffe, Lackmus, Gremlin |
| **Rauch** | Grundlegende Funktionalität nach der Bereitstellung | Benutzerdefinierte Skripte; Gesundheitschecks |
| **Einweichen** | Systemverhalten über einen längeren Zeitraum | Langzeitlasttests |
---

## Testorganisation
| Muster | Beschreibung | Wann zu verwenden |
|---------|-------------|-------------|
| **Gemeinsam gelegen** | Tests neben dem Code, den sie testen (`src/utils.test.ts`) | Die meisten Projekte; leicht zu finden |
| **Separates Verzeichnis** | Tests in einem `tests/`- oder `__tests__/`-Ordner | Große Projekte; klare Trennung |
| **Testvorrichtungen** | Freigegebene Testdaten in einem `fixtures/`-Verzeichnis | Wenn mehrere Tests dieselben Daten benötigen |
| **Testdienstprogramme** | Gemeinsam genutzte Helfer in einem `test-utils/`-Verzeichnis | Wenn die Setup-Logik komplex ist |
---

## Codeabdeckung
| Metrisch | Was es misst | Einschränkung |
|--------|---|------------|
| **Leitungsabdeckung** | Prozentsatz der von Tests ausgeführten Codezeilen | Misst nicht die Qualität von Aussagen |
| **Filialabdeckung** | Prozentsatz der genommenen Zweige (falls/sonst) | Besser als Leitungsabdeckung; Erkennt immer noch nicht alle Fehler |
| **Pfadabdeckung** | Prozentsatz der verwendeten Ausführungspfade | Am gründlichsten; exponentiell in komplexem Code |
| **Mutationsbewertung** | Prozentsatz der durch Tests erkannten Mutationen | Bestes Maß für die Testqualität |
**Ziel**: 80 % Leitungsabdeckung ist ein angemessener Standard. Aber die Abdeckung ist ein Richtwert und kein Ziel – eine 100-prozentige Abdeckung mit schwachen Aussagen ist schlechter als eine 70-prozentige Abdeckung mit gründlichen Tests.
---

## Kontinuierliche Integration und Tests
| Üben | Beschreibung |
|----------|-------------|
| **Alle Unit-Tests bei jedem Commit ausführen** | Schnelles Feedback; fängt Regressionen sofort auf |
| **Integrationstests für PR ausführen** | Fängt Probleme ab, die Unit-Tests übersehen |
| **Führen Sie E2E-Tests jede Nacht oder beim Zusammenführen zum Hauptserver aus** | Langsam, aber gründlich |
| **Schnell scheitern** | Stoppen Sie die Pipeline beim ersten Fehler, um Zeit zu sparen |
| **Flockige Testrichtlinie** | Flakige Tests sofort unter Quarantäne stellen oder löschen; ignoriere niemals |
| **Parallelisierung testen** | Führen Sie Tests parallel aus, um die CI-Zeit zu verkürzen |
---

## Praktische Tipps
- **Tests klar benennen.**`test_calculates_tax_for_high_earner`sagt Ihnen, was kaputt gegangen ist. `test_1`sagt dir nichts.
- **Eine Behauptung pro Test (sofern praktikabel).** Erleichtert die Diagnose von Fehlern.
- **Implementierungsdetails nicht testen.** Testverhalten. Wenn Sie Interna umgestalten, sollten Tests nicht kaputt gehen.
- **Vermeiden Sie das Testen von Code von Drittanbietern.** Scheinen Sie externe Bibliotheken; Testen Sie die Interaktion Ihres Codes mit ihnen.
- **Machen Sie Tests schnell.** Wenn Ihre Testsuite 10 Minuten dauert, wird die Ausführung durch die Entwickler gestoppt. Optimieren Sie unermüdlich.
- **Tote Tests löschen.** Tests, die immer bestanden werden oder entfernten Code testen, sind Rauschen.
- **Behandeln Sie Testcode wie Produktionscode.** Er sollte lesbar, wartbar und gut strukturiert sein.
---

## Zusammenfassung
Testen ist nicht optional – es geht darum, wie Sie Software erstellen, die nicht kaputt geht. Die Testpyramide führt Sie zu vielen schnellen Unit-Tests, einigen Integrationstests und einigen E2E-Tests. TDD und BDD bieten strukturierte Ansätze. Mocking isoliert Einheiten zum Testen. Die Codeabdeckung misst die Breite, nicht jedoch die Tiefe. Der wichtigste Grundsatz lautet: Wenn es nicht getestet wird, ist es kaputt – man weiß es nur noch nicht.