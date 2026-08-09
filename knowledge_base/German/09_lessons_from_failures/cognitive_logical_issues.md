---
# Metadata
title: "Cognitive Biases and Logical Fallacies"
description: "Reasoning errors and cognitive biases"
category: "Lessons from Failures"
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
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cognitive, logical, issues, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "27 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Kognitive Vorurteile und logische Irrtümer
Dieses Dokument konsolidiert kognitive Vorurteile, logische Irrtümer und Denkfehler, die sich sowohl auf die menschliche Entscheidungsfindung als auch auf die Ergebnisse von KI-Systemen auswirken.
---

## Kognitive Vorurteile
Kognitive Verzerrungen sind systematische Muster der Abweichung von der Rationalität bei Urteilen und Entscheidungen. In der Softwareentwicklung und bei KI-Systemen können diese zu schlechten Designentscheidungen, fehlerhaften Anforderungen und voreingenommenem Modellverhalten führen.
### Bestätigungsverzerrung
**Was es ist:** Die Tendenz, Informationen auf eine Weise zu suchen, zu interpretieren und abzurufen, die bereits bestehende Überzeugungen bestätigt.
**Schlechtes Beispiel in der Entwicklung:**```python
# Developer believes their algorithm is O(n log n)
def analyze_complexity(code):
    # Only looks for evidence supporting O(n log n)
    sees_divide_and_conquer = True
    sees_recursion = True
    
    # Ignores contradictory evidence
    nested_loop_present = True  # Actually makes it O(n²)
    redundant_computation = True  # Adds extra factor
    
    return "O(n log n)"  # Wrong conclusion
```

**In Codeüberprüfungen:**```markdown
Developer A (senior): "This looks good, nice work!"
Developer B (junior): "This has several potential issues..."

Team accepts Developer A's review without scrutiny but questions Developer B's feedback excessively.
```

**Abhilfe:**
- Suchen Sie aktiv nach entkräftenden Beweisen
- Verwenden Sie Blindcode-Reviews
- Ermutigen Sie abweichende Meinungen
- Dokumentieren Sie Annahmen explizit
### Verankerungsbias
**Was es ist:** Verlassen Sie sich zu sehr auf die erste Information, auf die Sie stoßen.
**Schlechtes Beispiel:**```markdown
Project Manager: "This feature should take about 2 days."
Developer: (Anchored to 2 days, even though realistic estimate is 5 days)
"Okay, I'll try to finish in 2 days."

Result: Rushed work, technical debt, missed deadlines anyway.
```

**Abhilfe:**
- Holen Sie mehrere unabhängige Schätzungen ein
- Nutzen Sie Planungspoker zur Schätzung
- Berücksichtigen Sie Spannen anstelle von Punktschätzungen
- Referenzieren Sie historische Daten
### Irrtum über versunkene Kosten
**Was es ist:** Ein Unterfangen aufgrund zuvor investierter Ressourcen (Zeit, Geld, Mühe) fortzusetzen, auch wenn es besser wäre, es abzubrechen.
**Schlechtes Beispiel:**```markdown
"We've already spent 6 months building this custom framework. 
We can't switch to the industry standard now, even though 
it would save us time in the long run."
```

**Abhilfe:**
- Bewerten Sie Entscheidungen auf der Grundlage des zukünftigen Werts, nicht der vergangenen Investitionen
- Bewerten Sie die Projektdurchführbarkeit regelmäßig neu
- Schaffen Sie psychologische Sicherheit für das Schwenken
- Verwenden Sie objektive Kriterien für Fortführungs-/Stopp-Entscheidungen
### Verfügbarkeitsheuristik
**Was es ist:** Überschätzung der Bedeutung von Informationen, die leicht verfügbar oder aktuell sind.
**Schlechtes Beispiel:**```markdown
"I just read about a SQL injection attack, so we should 
prioritize SQL injection prevention over XSS, even though 
our security audit shows XSS is our bigger risk."
```

**Abhilfe:**
- Nutzen Sie datengesteuerte Entscheidungsfindung
- Konsultieren Sie umfassende Bedrohungsmodelle
- Schauen Sie sich die Basistarife und Statistiken an
- Vermeiden Sie Aktualitätsfehler bei der Priorisierung
### Mahn-Krüger-Effekt
**Was es ist:** Menschen mit geringen Fähigkeiten bei einer Aufgabe überschätzen ihre Fähigkeiten; Experten unterschätzen möglicherweise ihre.
**Schlechtes Beispiel:**```markdown
Junior Developer: "I've completed a Python tutorial. 
I'm ready to architect our entire microservices platform."

Senior Developer: "I've been building distributed systems for 10 years. 
I'm probably missing something important in this design."
```

**Abhilfe:**
- Fördern Sie kontinuierliches Lernen
- Implementieren Sie Peer-Review-Prozesse
- Erstellen Sie Mentoring-Programme
- Fördern Sie Demut und Neugier
---

## Logische Irrtümer
Logische Irrtümer sind Denkfehler, die die Gültigkeit von Argumenten untergraben. KI-Modelle können Ergebnisse erzeugen, die diese Irrtümer enthalten.
### Ad Hominem (Angriff gegen die Person)
**Was es ist:** Angriff auf die Person, die ein Argument vorbringt, und nicht auf das Argument selbst.
**Schlechtes Beispiel:**```markdown
"This code review is wrong because the reviewer is a junior developer."
```

**Warum es schlecht ist:** Die Gültigkeit eines Feedbacks hängt von seinem Inhalt ab, nicht vom Dienstalter des Rezensenten.
### Appell an die Behörde
**Was es ist:** Die Behauptung, etwas sei wahr, weil eine Autoritätsperson dies sagt, ohne Beweise.
**Schlechtes Beispiel:**```markdown
"This architecture must be correct because Google uses it."
```

**Warum es schlecht ist:** Was für Google in seiner Größenordnung funktioniert, funktioniert möglicherweise nicht für Ihren Anwendungsfall.
### Falsche Dichotomie (Schwarz-Weiß-Denken)
**Was es ist:** Es werden nur zwei Optionen angezeigt, wenn es mehr gibt.
**Schlechtes Beispiel:**```markdown
"We either rewrite everything in Rust or accept that our 
codebase will always be slow and buggy."
```

**Realität:** Zwischen diesen Extremen gibt es viele Optionen (Hot Paths optimieren, Rust für bestimmte Komponenten verwenden, Python-Code verbessern usw.)
### Rutschiger Hang
**Was es ist:** Die Argumentation, dass ein Ereignis unweigerlich zu einer Kette negativer Konsequenzen führen wird.
**Schlechtes Beispiel:**```markdown
"If we allow this small technical debt, soon our entire 
codebase will be unmaintainable and the company will fail."
```

**Warum es schlecht ist:** Geht von einem unvermeidlichen Fortschreiten ohne Beweise aus; mildernde Faktoren werden ignoriert.
### Zirkuläres Denken
**Was es ist:** Die Schlussfolgerung als Prämisse verwenden.
**Schlechtes Beispiel:**```markdown
"Our code is high quality because we write good code."
```

### Post Hoc Ergo Propter Hoc (falsche Ursache)
**Was es ist:** Angenommen, dass A B verursacht hat, weil B A folgte.
**Schlechtes Beispiel:**```markdown
"We deployed the new feature and then saw increased latency. 
The new feature must be causing the latency."
```

**Realität:** Korrelation bedeutet keine Kausalität. Andere Faktoren könnten dafür verantwortlich sein.
### Strohmann
**Was es ist:** Das Argument einer Person falsch darstellen, um den Angriff zu erleichtern.
**Schlechtes Beispiel:**```markdown
Developer A: "We should add more tests for edge cases."
Developer B: "So you want us to spend all our time writing tests 
and never ship features?"
```

### Bandwagon-Irrtum
**Was es ist:** Etwas zu argumentieren ist richtig, weil viele Leute es glauben.
**Schlechtes Beispiel:**```markdown
"Everyone is using Kubernetes, so we should too."
```

**Warum es schlecht ist:** Beliebtheit garantiert nicht die Eignung für Ihre spezifischen Bedürfnisse.
---

## Argumentationsfehler in der KI
### Mehrstufige Logikfehler
**Schlechtes Beispiel:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Yes, Alice must be a programmer.
```

**Warum es schlecht ist:**
- Begeht den Trugschluss, die Konsequenz zu bestätigen
- Alice könnte Code schreiben, ohne Programmiererin zu sein
- Logische Struktur: (P→Q, Q) ⊬ P
**Richtige Begründung:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Not necessarily. While all programmers write code, not everyone
who writes code is a programmer. Alice could be a student, hobbyist, or
work in another field that involves coding.
```

### Fehler beim mathematischen Denken
**Schlechtes Beispiel:**```
User: A bat and ball cost $1.10 together. The bat costs $1 more than the ball.
How much does the ball cost?
Assistant: The ball costs $0.10.
```

**Realität:** Wenn der Ball 0,10 $ kostet und der Schläger 1 $ mehr kostet (1,10 $), beträgt die Gesamtsumme 1,20 $. Die richtige Antwort ist 0,05 $ für den Ball und 1,05 $ für den Schläger.
### Kausale Argumentationsfehler
**Schlechtes Beispiel:**```
User: Ice cream sales and drowning rates both increase in summer. Does ice cream cause drowning?
Assistant: Yes, there appears to be a causal relationship.
```

**Realität:** Beide werden durch einen dritten Faktor (heißes Wetter) verursacht, nicht durch einander.
---

## Strategien zur Verbesserung
### Für die menschliche Entscheidungsfindung
1. **Sensibilisierungstraining**: Lernen Sie, häufige Vorurteile zu erkennen
2. **Verwendung von Checklisten**: Verwenden Sie Entscheidungschecklisten, um Vorurteilen entgegenzuwirken
3. **Diverse Teams**: Beziehen Sie Menschen mit unterschiedlichen Perspektiven ein
4. **Pre-Mortems**: Stellen Sie sich ein Scheitern vor und arbeiten Sie rückwärts, um die Ursachen zu identifizieren
5. **Dokumentation**: Begründung zur späteren Überprüfung aufzeichnen
### Für KI-Systeme
1. **Aufforderung zur Gedankenkette**: Bitten Sie das Modell, Argumentationsschritte zu zeigen
2. **Selbstkorrektur**: Lassen Sie das Modell seine Antworten überprüfen und kritisieren
3. **Formale Verifizierung**: Verwenden Sie symbolische Argumentationswerkzeuge für kritische Logik
4. **Zerlegung**: Komplexe Probleme in kleinere Schritte aufteilen
5. **Externe Tools**: Verwenden Sie Taschenrechner und Löser für mathematische Aufgaben
6. **Mehrere Stichproben**: Mehrere Antworten generieren und vergleichen
---

## Verwandte Themen
- **AI/LLM-Fehler**: Siehe`ai_llm_failures.md`für Halluzinationen und Denkprobleme
- **Widersprüchliche Quellen**: Siehe Dokumentation zur Bewertung widersprüchlicher Informationen
- **Kritisches Denken**: Wenden Sie diese Konzepte an, um Argumente und Beweise zu bewerten
- **Prompt Engineering**: Techniken zur Reduzierung von Argumentationsfehlern finden Sie unter `../02_artificial_intelligence/prompt_engineering.md`
---

## Zusätzliche kognitive Verzerrungen in der Softwareentwicklung
### Status Quo Bias
**Was es ist:** Präferenz für die Beibehaltung des aktuellen Status; Jede Veränderung wird als Verlust empfunden.
**Schlechtes Beispiel:**```markdown
Team Lead: "Should we upgrade to Python 3.12? It has performance improvements 
and security fixes."

Developer: "Python 3.8 works fine. Why risk breaking things?"

Reality: Staying on an older version increases technical debt, security risks,
and makes future upgrades harder.
```

**Abhilfe:**
- Quantifizieren Sie die Kosten, die entstehen, wenn Sie sich nicht ändern
- Legen Sie regelmäßige Upgrade-Zeitpläne fest
- Schaffen Sie sichere Experimentierumgebungen
- Frame-Änderungen als Chancen, nicht als Bedrohungen
### Optimismus-Tendenz
**Was es ist:** Zeit, Kosten und Risiken unterschätzen und gleichzeitig den Nutzen überschätzen.
**Schlechtes Beispiel:**```markdown
Project Plan:
- Development: 2 weeks (realistic: 4 weeks)
- Testing: 3 days (realistic: 1 week)
- Bug fixes: 2 days (realistic: 1-2 weeks)
- Contingency: None

Result: Project takes 3x longer than planned.
```

**Abhilfe:**
- Referenzklassenprognosen verwenden (im Vergleich zu ähnlichen früheren Projekten)
- Fügen Sie Notfallpuffer hinzu (20–50 %).
- Führen Sie Obduktionen durch
- Verfolgen Sie die Schätzgenauigkeit im Laufe der Zeit
### Survivorship Bias
**Was es ist:** Konzentrieren Sie sich auf erfolgreiche Beispiele und ignorieren Sie Fehler.
**Schlechtes Beispiel:**```markdown
"Look at all these successful startups that didn't do market research!
We don't need market research either."

Reality: Many more startups failed without market research, but they're 
not visible because they didn't survive.
```

**Abhilfe:**
- Studieren Sie sowohl Erfolge als auch Misserfolge
- Suchen Sie nach Basispreisen und Statistiken
- Berücksichtigen Sie unsichtbare Daten
- Vermeiden Sie Rosinenpickerei-Beispiele
### Grundlegender Zuordnungsfehler
**Was es ist:** Das Verhalten anderer auf den Charakter und nicht auf die Umstände zurückführen.
**Schlechtes Beispiel:**```markdown
"That developer made a bug because they're careless."

Reality: The bug might be due to unclear requirements, time pressure,
lack of testing infrastructure, or fatigue.
```

**Abhilfe:**
- Berücksichtigen Sie situative Faktoren
- Übe Empathie
- Konzentrieren Sie sich auf Systeme, nicht auf Einzelpersonen
- Verwenden Sie unschuldige Obduktionen
### Rückschaufehler
**Was es ist:** Nachdem ein Ereignis eingetreten ist, wird davon ausgegangen, dass es die ganze Zeit über vorhersehbar war.
**Schlechtes Beispiel:**```markdown
After production outage:
"I knew that deployment was risky. This was totally predictable."

Reality: The outcome wasn't obvious beforehand; hindsight makes it seem clear.
```

**Abhilfe:**
- Dokumentieren Sie Vorhersagen vor den Ergebnissen
- Überprüfen Sie den Entscheidungskontext, nicht nur die Ergebnisse
- Vermeiden Sie die „Ich habe es dir doch gesagt“-Kultur
- Konzentrieren Sie sich auf die Verbesserung von Prozessen und nicht auf die Zuweisung von Schuldzuweisungen
---

## Weitere logische Irrtümer
### Appell an Neuheit
**Was es ist:** Angenommen, etwas ist besser, weil es neuer ist.
**Schlechtes Beispiel:**```markdown
"We should rewrite our entire backend in the latest framework. 
It's the newest, so it must be better."

Reality: Newer doesn't mean better for your specific use case.
Mature technologies often have better support and stability.
```

### Appell an die Tradition
**Was es ist:** Etwas zu argumentieren ist richtig, weil es schon immer so gemacht wurde.
**Schlechtes Beispiel:**```markdown
"We've always deployed on Fridays at 5 PM. We shouldn't change that."

Reality: Just because something is traditional doesn't make it optimal.
(Actually, deploying on Friday at 5 PM is generally considered bad practice!)
```

### Tu Quoque (Appell an die Heuchelei)
**Was es ist:** Kritik abweisen, indem man auf die Inkonsistenz des Kritikers hinweist.
**Schlechtes Beispiel:**```markdown
Senior Dev: "You should write tests for this code."
Junior Dev: "But you don't write tests for your code either!"

Reality: The validity of the advice is independent of who gives it.
```

### Geladene Frage
**Was es ist:** Eine Frage stellen, die eine Annahme enthält.
**Schlechtes Beispiel:**```markdown
"Why did you write such terrible code for this module?"

Reality: The question assumes the code is terrible, putting the respondent
on the defensive regardless of actual code quality.
```

### Kein echter Schotte
**Was es ist:** Eine Ausnahme von einem Universalanspruch machen, wenn dieser angefochten wird.
**Schlechtes Beispiel:**```markdown
Person A: "No professional developer writes code without tests."
Person B: "But John is a professional developer and doesn't write tests."
Person A: "Well, no TRUE professional developer writes code without tests."

Reality: This redefines the category to exclude counterexamples rather 
than revising the claim.
```

### Genetischer Irrtum
**Was es ist:** Etwas anhand seiner Herkunft und nicht anhand seines aktuellen Verdienstes zu beurteilen.
**Schlechtes Beispiel:**```markdown
"That library came from a small startup, so it can't be enterprise-grade."

Reality: The origin doesn't determine current quality. Evaluate based on
actual characteristics, not source.
```

### Mittelweg-Irrtum
**Was es ist:** Die Annahme, dass die Wahrheit immer in der Mitte von zwei Extremen liegt.
**Schlechtes Beispiel:**```markdown
Developer A: "We should add comprehensive error handling."
Developer B: "Error handling isn't important, skip it."
Compromise: "Let's add some error handling, but not too much."

Reality: One position might be clearly correct. Compromise isn't always wise.
```

---

## Kognitive Verzerrungen in KI-Systemen
### Trainingsdatenverzerrung
KI-Modelle erben in ihren Trainingsdaten vorhandene Vorurteile.
**Beispiel:**```markdown
Training data contains: "The doctor said..." (mostly male pronouns)
                       "The nurse said..." (mostly female pronouns)

Model learns: Doctors are typically male, nurses are typically female.

Result: Model exhibits gender bias in profession associations.
```

**Abhilfe:**
- Überprüfen Sie die Trainingsdaten auf Vorurteile
- Verwenden Sie Debiasing-Techniken
- Testen Sie auf voreingenommene Ausgaben
- Vielfältige Datenerfassung
### Automatisierungsbias
**Was es ist:** Sich zu sehr auf automatisierte Systeme zu verlassen, auch wenn diese falsch liegen.
**Beispiel:**```markdown
AI suggests code with a subtle bug.
Developer accepts it without review because "the AI is usually right."

Result: Bug makes it to production.
```

**Abhilfe:**
- Behalten Sie die menschliche Aufsicht bei
- Ermutigen Sie zur kritischen Bewertung von KI-Ergebnissen
- Behandeln Sie KI nicht als unfehlbar
- Implementieren Sie Überprüfungsprozesse
### Illusion des Verstehens
**Was es ist:** Zu glauben, dass Sie verstehen, wie eine KI funktioniert, wenn Sie es nicht wissen.
**Beispiel:**```markdown
User: "The AI understands what I mean, it's like talking to a person."

Reality: LLMs predict tokens based on patterns, they don't truly 
"understand" in the human sense. This illusion leads to over-trust.
```

**Abhilfe:**
- Informieren Sie Benutzer über die Einschränkungen der KI
- Seien Sie transparent darüber, wie Systeme funktionieren
- Vermeiden Sie die Vermenschlichung der KI
- Setzen Sie angemessene Erwartungen
---

## Fallstudien
### Fallstudie 1: Bestätigungsverzerrung bei der Architekturauswahl
**Vorfall:** Ein Team wählte eine Microservices-Architektur für eine kleine Anwendung.
**Grundursache:** Der Teamleiter hatte mehrere Artikel gelesen, in denen Microservices gelobt wurden 
suchte nur nach Informationen, die diese Wahl bestätigten, und ignorierte Warnungen vor der Komplexität.
**Auswirkung:**
- Enormer Overhead für ein Team von 3 Entwicklern
– Die Komplexität der Bereitstellung wurde um das Zehnfache erhöht
– Leistungseinbußen aufgrund von Netzwerkaufrufen
- Projekt um 6 Monate verzögert
**Lektion:** Bewerten Sie Architekturen basierend auf Ihrem spezifischen Kontext, nicht nur 
positive Erfahrungsberichte. Berücksichtigen Sie Kompromisse explizit.
### Fallstudie 2: Versunkene Kosten im Altsystem
**Vorfall:** Das Unternehmen unterhielt fünf Jahre lang weiterhin ein maßgeschneidertes CRM 
trotz besserer Alternativen.
**Ursache:** „Wir haben bereits 2 Millionen US-Dollar investiert, wir können es jetzt nicht aufgeben.“
**Auswirkung:**
- Jährliche Wartungskosten: 500.000 $
- Opportunitätskosten: Moderne Funktionen konnten nicht genutzt werden
- Probleme bei der Talentbindung (Entwickler wollten mit moderner Technologie arbeiten)
- Gesamtkosten für 5 Jahre: 4,5 Mio. USD gegenüber 1,5 Mio. USD für die SaaS-Alternative
**Lektion:** Vergangene Investitionen sind gesunken. Treffen Sie Entscheidungen basierend auf dem zukünftigen Wert.
### Fallstudie 3: Verfügbarkeitsheuristik in der Sicherheit
**Vorfall:** Das Team hat der Verteidigung gegen einen kürzlich veröffentlichten Angriff Priorität eingeräumt 
Vektor, während wahrscheinlichere Bedrohungen ignoriert werden.
**Ursache:** Durch die aktuelle Berichterstattung ist ein Bedrohungstyp hochverfügbar geworden 
im Gedächtnis, verzerrte Risikobewertung.
**Auswirkung:**
- 100.000 US-Dollar für die Eindämmung einer Bedrohung mit geringer Wahrscheinlichkeit ausgegeben
- Der tatsächliche Verstoß erfolgte durch einen vernachlässigten Vektor
- Wiederherstellungskosten: 500.000 $+
**Lektion:** Verwenden Sie eine datengesteuerte Bedrohungsmodellierung, keine auf Aktualität basierende Priorisierung.
---

## Praktische Übungen
### Übung zur Bias-Erkennung
Überprüfen Sie aktuelle Entscheidungen und fragen Sie:
1. Welche Annahmen haben wir getroffen?
2. Welche Beweise würden unserer Schlussfolgerung widersprechen?
3. Haben wir mehrere Optionen in Betracht gezogen oder uns an der ersten Idee orientiert?
4. Machen wir aufgrund des zukünftigen Werts oder früherer Investitionen weiter?
5. Was würden wir empfehlen, wenn uns jemand anderes fragen würde?
### Logische Irrtümer erkennen
Üben Sie, Irrtümer in alltäglichen Diskussionen zu erkennen:
```markdown
Statement: "If we don't adopt AI now, we'll be left behind forever."

Analysis: This is a slippery slope fallacy. It assumes inevitable 
progression to being "left behind" without evidence. Also presents 
a false dichotomy (adopt AI or be left behind).
```

### Pre-Mortem-Technik
Bevor Sie ein Projekt starten:
1. Stellen Sie sich vor, es sind 6 Monate in der Zukunft
2. Das Projekt ist spektakulär gescheitert
3. Schreiben Sie die Geschichte, warum es gescheitert ist
4. Arbeiten Sie rückwärts, um diese Fehlermodi zu verhindern
Dies wirkt dem Optimismus-Bias und der Verfügbarkeitsheuristik entgegen.
---

## Tools und Frameworks
### Vorlage für ein Entscheidungsjournal
```markdown
Date: [When]
Decision: [What we decided]
Context: [Situation and constraints]
Options Considered: [Alternatives evaluated]
Expected Outcome: [What we think will happen]
Confidence Level: [How sure we are]
Review Date: [When to revisit]

[Later] Actual Outcome: [What actually happened]
Lessons Learned: [What we'd do differently]
```

### Bias-Checkliste
Bevor Sie wichtige Entscheidungen treffen:
- [ ] Haben wir nach entkräftenden Beweisen gesucht?
- [ ] Sind wir auf den ersten Informationen verankert?
- [ ] Beeinflussen uns versunkene Kosten?
- [ ] Sind wir in unseren Schätzungen zu selbstsicher?
- [ ] Haben wir über Grundzinsen nachgedacht?
- [ ] Fallen wir auf den Verfügbarkeits-/Aktualitätsbias herein?
- [ ] Würden wir die gleiche Wahl treffen, wenn wir neu anfangen würden?
### Rote-Team-Übung
Beauftragen Sie jemanden, gegen die vorgeschlagene Entscheidung zu argumentieren:
- Ihre Aufgabe ist es, Fehler zu finden
- Sie müssen alternative Standpunkte vertreten
- Das Team übt, konstruktiv auf Kritik zu reagieren
- Bedenken hinsichtlich des Dokuments geäußert und behoben
Dies wirkt Bestätigungsvoreingenommenheit und Gruppendenken entgegen.