<!--
---
# Metadata
title: "Accessibility and Inclusive Design"
description: "WCAG, inclusive UX, assistive technology, accessible coding"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [accessibility, inclusive, design, coding-and-technology]
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

-->
# Barrierefreiheit und integratives Design
Barrierefreiheit (oft als a11y abgekürzt) ist die Praxis, Software für jedermann nutzbar zu machen – auch für Menschen mit Seh-, Hör-, motorischen, kognitiven und neurologischen Behinderungen. In vielen Ländern ist dies gesetzlich vorgeschrieben und eine gängige technische Praxis. Barrierefreie Software ist eine bessere Software für alle, da die Designentscheidungen, die behinderte Benutzer unterstützen – klare Struktur, Tastaturnavigation, ausreichender Kontrast, lesbarer Text – das Erlebnis für alle Benutzer verbessern.
---

## Wer profitiert von Barrierefreiheit?
| Behinderungsart | Beispiele | Unterstützende Technologie |
|----------------|---------|-------|
| **Visuell** | Blindheit, Sehbehinderung, Farbenblindheit | Bildschirmleseprogramme (JAWS, NVDA, VoiceOver); Lupen; kontrastreiche Modi |
| **Akustisch** | Taubheit, Schwerhörigkeit | Bildunterschriften; Transkripte; visuelle Warnungen |
| **Motor** | Eingeschränkte Geschicklichkeit, Lähmung, Zittern | Nur-Tastatur-Navigation; Sprachsteuerung; Schaltgeräte; Blickverfolgung |
| **Kognitiv** | Legasthenie, ADHS, Autismus, Gedächtnisstörungen | Klare Sprache; konsistente Navigation; reduzierte Ablenkungen |
| **Vorübergehend** | Gebrochener Arm, helles Sonnenlicht, laute Umgebung | Gleiche Vorkehrungen wie dauerhafte Behinderungen |
| **Situativ** | Ein Baby haltend, fahrend, eine Hand besetzt | Sprachschnittstellen; große Touch-Ziele |
**Wichtige Erkenntnis**: Barrierefreiheitsfunktionen, die für Benutzer mit Behinderungen entwickelt wurden, helfen allen. Bordsteinkanten (Rampen an Gehwegen) wurden für Rollstühle konzipiert, werden aber von Eltern mit Kinderwagen, Lieferarbeitern mit Einkaufswagen und Reisenden mit Gepäck genutzt.
---

## Web-Barrierefreiheit (WCAG)
Die Web Content Accessibility Guidelines (WCAG) sind der internationale Standard für Web-Barrierefreiheit.
### WCAG-Grundsätze (POUR)
| Prinzip | Anforderung |
|-----------|-------------|
| **Wahrnehmbar** | Informationen müssen für den Benutzer wahrnehmbar darstellbar sein (Textalternativen, Bildunterschriften, anpassbares Layout) |
| **Bedienbar** | Die Benutzeroberfläche muss navigierbar und benutzbar sein (Tastatur zugänglich, genügend Zeit, keine anfallsauslösenden Inhalte) |
| **Verständlich** | Informationen und Bedienung müssen verständlich sein (lesbar, vorhersehbar, Eingabehilfen) |
| **Robust** | Inhalte müssen mit aktuellen und zukünftigen unterstützenden Technologien funktionieren |
### WCAG-Konformitätsstufen
| Ebene | Anforderungen | Typisches Ziel |
|-------|-------------|---------------|
| **A** | Mindestniveau; 30 Erfolgskriterien | Gesetzliches Minimum in einigen Gerichtsbarkeiten |
| **AA** | Beseitigt die häufigsten Hindernisse | Standardziel für die meisten Organisationen |
| **AAA** | Höchstes Niveau; nicht alle Inhalte können dies erreichen | Spezialisierte Inhalte; Bildungsseiten |
### Wichtige Erfolgskriterien (AA-Stufe)
| Kriterium | Anforderung | So erreichen Sie |
|-----------|-------------|---------------|
| **1.1.1 Nicht-Text-Inhalt** | Alle Bilder haben Textalternativen |  `alt`-Attribute; `aria-label`für Symbole |
| **1.3.1 Informationen und Beziehungen** | Struktur programmatisch vermittelt | Semantisches HTML; Überschriften; Listen; Wahrzeichen |
| **1.4.3 Kontrast (Minimum)** | Der Text hat ein Kontrastverhältnis von mindestens 4,5:1 | Test mit Kontrastprüfern; Wählen Sie zugängliche Farbpaletten |
| **1.4.4 Textgröße ändern** | Die Textgröße kann ohne Verlust auf 200 % geändert werden | Verwenden Sie relative Einheiten (rem, em); responsives Design |
| **2.1.1 Tastatur** | Alle Funktionen über die Tastatur verfügbar | Keine Tastaturfallen; sichtbare Fokusindikatoren |
| **2.4.3 Fokusreihenfolge** | Fokusreihenfolge bewahrt Bedeutung und Bedienbarkeit | Logische Tab-Reihenfolge; DOM-Reihenfolge entspricht visueller Reihenfolge |
| **2.4.7 Fokus sichtbar** | Der Tastaturfokus wird visuell angezeigt | CSS `:focus-visible`-Stile; nie`outline: none`ohne Ersatz |
| **3.3.2 Etiketten oder Anweisungen** | Eingaben haben Beschriftungen |  `<label>`-Elemente; `aria-label`|
| **4.1.2 Name, Rolle, Wert** | UI-Komponenten haben zugängliche Namen und Rollen | ARIA-Attribute; semantisches HTML |
---

## ARIA (Accessible Rich Internet Applications)
ARIA fügt HTML-Elementen, die keine integrierte Semantik haben, Informationen zur Barrierefreiheit hinzu.
### ARIA-Rollen
| Rolle | Zweck | Beispiel |
|------|---------|---------|
| `button`| Identifiziert ein Element als Schaltfläche | Ein`<div>`im Stil einer Schaltfläche |
| `dialog`| Modaler oder nichtmodaler Dialog | Benutzerdefinierte modale Komponenten |
| `tablist`/`tab`/`tabpanel`| Tab-Schnittstelle | Benutzerdefinierte Registerkartenkomponenten |
| `alert`| Wichtige Meldung, die dynamisch erscheint | Fehlermeldungen |
| `progressbar`| Fortschrittsanzeige | Ladezustände |
| `menu`/`menuitem`| Menünavigation | Dropdown-Menüs |
### ARIA-Attribute
| Attribut | Zweck | Beispiel |
|-----------|---------|---------|
| `aria-label`| Zugänglicher Name, wenn kein sichtbarer Text | Nur-Symbol-Schaltfläche:`aria-label="Search"`|
| `aria-describedby`| Verknüpft Element mit seiner Beschreibung | Formularfeld mit Hilfetext |
| `aria-expanded`| Gibt an, ob ein Abschnitt erweitert ist | Akkordeon; Dropdown |
| `aria-hidden`| Versteckt Element vor unterstützender Technologie | Dekorative Ikonen |
| `aria-live`| Kündigt dynamische Inhaltsänderungen an | Live-Updates; Benachrichtigungen |
| `aria-disabled`| Zeigt an, dass das Element deaktiviert ist | Ausgegraute Schaltflächen |
### Die erste Regel von ARIA
> **Verwenden Sie ARIA nicht, wenn Sie stattdessen natives HTML verwenden können.** Ein`<button>`ist bereits zugänglich. Bei einem`<div role="button">`müssen Sie die Tastaturbedienung, die Fokusverwaltung und die Unterstützung für Bildschirmleseprogramme manuell hinzufügen. Verwenden Sie zuerst semantisches HTML. ARIA nur, wenn native Elemente die Aufgabe nicht erfüllen können.
---

## Tastaturnavigation
| Schlüssel | Erwartetes Verhalten |
|-----|-----|
| **Tabulatortaste** | Fokus auf das nächste interaktive Element verschieben |
| **Umschalt + Tab** | Fokus auf das vorherige interaktive Element verschieben |
| **Eingabe / Leertaste** | Aktivieren Sie das fokussierte Element (Schaltfläche, Link) |
| **Pfeiltasten** | Navigieren innerhalb von Komponenten (Menüs, Registerkarten, Optionsgruppen) |
| **Flucht** | Schließen Sie ein Dialogfeld, ein Menü oder ein Popover |
| **Startseite / Ende** | Zum ersten/letzten Element in einer Liste springen |
### Häufige Tastaturfallen
| Problem | Fix |
|---------|-----|
| Der Fokus betritt eine Komponente, kann sie aber nicht verlassen | Stellen Sie sicher, dass Tab den Fokus nach außen verschiebt. handle Escape |
| Modal fängt den Fokus nicht ein | Der Fokus sollte innerhalb des Modals wechseln; Rückkehr zum Auslöser beim Schließen |
| Benutzerdefinierte Komponenten reagieren nicht auf die Tastatur | Keydown-Handler für Eingabetaste, Leertaste und Pfeile hinzufügen |
---

## Farbe und visuelles Design
| Richtlinie | Anforderung |
|-----------|-------------|
| **Kontrastverhältnis** | 4,5:1 für normalen Text; 3:1 für großen Text (18pt+ oder 14pt+ fett) |
| **Verlassen Sie sich nicht nur auf die Farbe** | Verwenden Sie zusätzlich zur Farbe | Symbole, Text oder Muster
| **Fokusindikatoren** | Immer sichtbar; hoher Kontrast; nie ersatzlos entfernt |
| **Größenänderung des Textes** | Das Layout muss bei 200 % Zoom funktionieren |
| **Reaktionsfähig** | Der Inhalt muss mit einer Breite von 320 Pixeln umbrochen werden (mobil) |
### Überlegungen zur Farbenblindheit
| Geben Sie | ein Betroffene Farben | Design-Tipp |
|------|---|------------|
| **Deuteranopie** | Rotgrün (am häufigsten) | Verwenden Sie Rot/Grün nicht, um den Status zu vermitteln; Verwenden Sie Symbole + Farbe |
| **Protanopie** | Rot-Grün | Wie oben |
| **Tritanopie** | Blau-Gelb | Verwenden Sie nicht Blau/Gelb als alleiniges Unterscheidungsmerkmal |
---

## Zugänglichkeit testen
| Methode | Werkzeug | Was es fängt |
|--------|------|----------------|
| **Automatisiertes Scannen** | Axt, Leuchtturm, WELLE | Fehlender Alternativtext; Kontrastprobleme; ARIA-Fehler |
| **Tastaturtest** | Handbuch: Maus ausstecken, nur Tastatur verwenden | Fokusreihenfolge; Tastaturfallen; fehlende Handler |
| **Screenreader-Tests** | NVDA (kostenlos), VoiceOver (macOS), JAWS | Fehlende Etiketten; schlechte Struktur; unangekündigte Änderungen |
| **Zoom-Test** | Browser-Zoom auf 200 %, 400 % | Layoutbruch; abgeschnittener Text; Überlaufprobleme |
| **Farbkontrast** | WebAIM-Kontrastprüfer, Stark-Plugin | Unzureichende Kontrastverhältnisse |
| **Benutzertests** | Test mit behinderten Benutzern | Reale Barrieren, die automatisierte Tools übersehen |
---

## Gesetzliche Anforderungen
| Recht | Region | Anforderungen |
|-----|--------|-------------|
| **ADA** (Americans with Disabilities Act) | USA | Webseiten öffentlicher Unterkünfte müssen barrierefrei sein |
| **Abschnitt 508** | USA (Bundesstaat) | Die IKT der Bundesbehörden müssen zugänglich sein |
| **EAA** (Europäisches Gesetz zur Barrierefreiheit) | EU (2025+) | Produkte und Dienstleistungen müssen Barrierefreiheitsanforderungen erfüllen |
| **EN 301 549** | EU | Technischer Standard für IKT-Barrierefreiheit |
| **ACA** (Accessibility Canada Act) | Kanada | Staatliche und regulierte Industrien |
| **Gleichstellungsgesetz 2010** | Großbritannien | Dienstleister müssen angemessene Anpassungen vornehmen |
---

## Mobile Zugänglichkeit
| Plattform | Richtlinien | Schlüsselwerkzeuge |
|----------|-----------|-----------|
| **iOS** | Richtlinien für die Benutzeroberfläche von Apple (Abschnitt „Barrierefreiheit“) | VoiceOver; Dynamischer Typ; Schaltersteuerung |
| **Android** | Richtlinien zur Barrierefreiheit von Android | TalkBack; Schalterzugriff; Zum Sprechen auswählen |
| Mobiles Anliegen | Lösung |
|---------------|----------|
| **Ziele berühren** | Mindestens 44×44 Punkte (iOS) / 48×48 dp (Android) |
| **Screenreader-Unterstützung** | Inhaltsbeschreibungen; Barrierefreiheitsetiketten |
| **Bewegungsempfindlichkeit** | Respektiere`prefers-reduced-motion`; Vermeiden Sie automatisch abspielende Animationen |
| **Dynamische Textgröße** | Unterstützt Systemschriftgrößen; skalierbare Texteinheiten verwenden |
---

## Zusammenfassung
Barrierefreiheit ist ein Designprinzip, das jede Entscheidung von Anfang an beeinflussen sollte, und keine am Ende hinzugefügte Funktion. Verwenden Sie semantisches HTML. Stellen Sie sicher, dass die Tastaturnavigation funktioniert. Achten Sie auf ausreichenden Farbkontrast. Stellen Sie Textalternativen für Nicht-Text-Inhalte bereit. Testen Sie mit Bildschirmlesegeräten und behinderten Benutzern. Das Ergebnis ist Software, die für alle besser funktioniert – auch für diejenigen mit vorübergehenden Beeinträchtigungen, situativen Einschränkungen, älteren Geräten, langsamen Verbindungen und den vielen Unterschieden zwischen der realen Nutzung und einer kontrollierten Entwicklungsumgebung.