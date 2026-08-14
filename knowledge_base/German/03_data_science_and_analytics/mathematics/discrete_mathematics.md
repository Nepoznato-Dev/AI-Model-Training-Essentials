---
# Metadata
title: "Discrete Mathematics"
description: "Sets in depth, relations, functions, combinatorics, pigeonhole principle, recurrence relations, and generating functions"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "Nepoznato-Dev"
    changes: "Initial deep-dive into discrete mathematics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [discrete-mathematics, set-theory, relations, combinatorics, pigeonhole-principle, recurrence-relations, generating-functions]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "../logic_and_critical_thinking.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Diskrete Mathematik
Diskrete Mathematik ist das Studium mathematischer Strukturen, die grundsätzlich abzählbar oder getrennt sind – im Gegensatz zur kontinuierlichen Mathematik (Infinitesimalrechnung, reelle Analysis), die sich mit glatten, ungebrochenen Größen befasst. Diskrete Mathematik bildet die Grundlage für Informatik, Kryptographie, Algorithmendesign und Datenstrukturen. Während die kontinuierliche Mathematik die physikalische Welt beschreibt, beschreibt die diskrete Mathematik die rechnerische Welt.
---

## Mengenlehre im Detail
Mengen sind die Grundlage, auf der fast die gesamte moderne Mathematik aufbaut. Ein **Satz** ist eine ungeordnete Sammlung verschiedener Objekte, die **Elemente** oder **Mitglieder** genannt werden.
### Axiomatische Grundlagen (ZFC)
Die moderne Mengenlehre basiert auf den **Zermelo-Fraenkel-Axiomen mit dem Axiom of Choice (ZFC)**. Diese Axiome lösen Paradoxien wie Russells Paradox („die Menge aller Mengen, die sich selbst nicht enthalten“) auf, indem sie die Art und Weise einschränken, wie Mengen gebildet werden können.
| Axiom | Informelle Erklärung |
|-------|------|
| Extensionalität | Zwei Mengen sind genau dann gleich, wenn sie die gleichen Elemente | haben
| Leeres Set | Es existiert eine Menge ohne Elemente: ∅ |
| Paarung | Für jedes a, b gibt es {a, b} |
| Gewerkschaft | Für jede Mengenfamilie existiert ihre Vereinigung |
| Kraftset | Für jede Menge S existiert die Menge aller Teilmengen von S: P(S) |
| Unendlichkeit | Es gibt eine unendliche Menge |
| Spezifikation | Für jede Menge A und jede Eigenschaft P existiert {x ∈ A : P(x)} |
| Ersatz | Das Bild einer Menge unter einer definierbaren Funktion ist eine Menge |
| Regelmäßigkeit | Jede nichtleere Menge enthält ein davon disjunktes Element (verhindert Selbstmitgliedschaft) |
| Wahl | Für jede Familie nicht leerer paarweise disjunkter Mengen existiert eine Auswahlfunktion |
### Kardinalität und Größe von Mengen
Die **Kardinalität** einer Menge, mit |S| bezeichnet, misst ihre „Größe“.
| Konzept | Definition | Beispiel |
|---------|------------|---------|
| Endliche Menge | Hat eine natürliche Zahl als Kardinalität | |{a, b, c}| = 3 |
| Abzählbar unendlich | Gleiche Kardinalität wie ℕ | ℤ, ℚ sind abzählbar unendlich |
| Unzählige | Größer als ℕ | ℝ, P(ℕ), die Menge aller Funktionen ℕ → {0,1} |
| Satz von Cantor | Für jede Menge S gilt |P(S)| > |S| | |P(ℕ)| > |ℕ| |
**Cantors Diagonalargument** beweist, dass ℝ überzählbar ist: Nehmen wir an, Sie können alle reellen Zahlen in [0,1] auflisten, und konstruieren Sie dann eine neue reelle Zahl, die sich von der n-ten aufgelisteten reellen Zahl an der n-ten Dezimalstelle unterscheidet – Widerspruch.
### Operationen auf Mengen
| Betrieb | Notation | Definition | Eigentum |
|-----------|----------|------------|----------|
| Gewerkschaft | A ∪ B | {x : x ∈ A oder x ∈ B} | Kommutativ, assoziativ |
| Kreuzung | A ∩ B | {x : x ∈ A und x ∈ B} | Kommutativ, assoziativ |
| Unterschied | A \ B | {x : x ∈ A und x ∉ B} | Nicht kommutativ |
| Symmetrische Differenz | A △ B | (A \ B) ∪ (B \ A) | Kommutativ, assoziativ |
| Komplement | Aᶜ | U \ A (wobei U die Universalmenge ist) | (Aᶜ)ᶜ = A |
| Kartesisches Produkt | A × B | {(a,b) : a ∈ A, b ∈ B} | |A × B| = |A| · |B| |
**De Morgans Gesetze:**
- (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ
- (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ
**Einschluss-Ausschluss-Prinzip** (für endliche Mengen):
|A₁ ∪ A₂ ∪ ... ∪ Aₙ| = Σ|Aᵢ| − Σ|Aᵢ ∩ Aⱼ| + Σ|Aᵢ ∩ Aⱼ ∩ Aₖ| − ... + (−1)ⁿ⁺¹|A₁ ∩ ... ∩ Aₙ|
---

## Beziehungen
Eine **Beziehung** R auf den Mengen A und B ist eine Teilmenge von A × B. Wenn (a, b) ∈ R, schreiben wir aRb.
### Arten von Beziehungen
Eine Relation R auf einer Menge A kann folgende Eigenschaften haben:
| Eigentum | Definition | Beispiel |
|----------|------------|---------|
| Reflexiv | ∀a ∈ A: aRa | ≤ auf ℤ |
| Irreflexiv | ∀a ∈ A: ¬(aRa) | < auf ℤ |
| Symmetrisch | ∀a,b: aRb → bRa | = auf jeder Menge |
| Antisymmetrisch | ∀a,b: aRb ∧ bRa → a = b | ≤ auf ℤ |
| Transitiv | ∀a,b,c: aRb ∧ bRc → aRc | <, ≤, = auf ℤ |
### Äquivalenzbeziehungen
Eine **Äquivalenzrelation** ist reflexiv, symmetrisch und transitiv. Es unterteilt eine Menge in disjunkte **Äquivalenzklassen**.
**Beispiel:** Modulare Arithmetik. Definieren Sie a ~ b genau dann, wenn a ≡ b (mod n). Die Äquivalenzklassen sind [0], [1], ..., [n−1], die ℤ in n Klassen unterteilen.
**Arbeitsbeispiel:** Definieren Sie für ℤ × ℤ (a,b) ~ (c,d) genau dann, wenn a + d = b + c. Dies ist eine Äquivalenzrelation. Die Klasse [(0,0)] = {(n,n) : n ∈ ℤ}. Die Klasse [(1,0)] = {(n+1,n) : n ∈ ℤ}. Diese Konstruktion definiert tatsächlich die ganzen Zahlen aus den natürlichen Zahlen.
### Teilbestellungen
Eine **partielle Ordnung** ist reflexiv, antisymmetrisch und transitiv. Eine Menge mit einer teilweisen Ordnung wird als **teilweise geordnete Menge (Poset)** bezeichnet.
| Konzept | Definition | Beispiel |
|---------|------------|---------|
| Pose | (S, ≤) mit ≤ einer Teilordnung | (P(A), ⊆) – nach Inklusion geordnete Teilmengen |
| Kette | Eine vollständig geordnete Teilmenge | {∅, {a}, {a,b}} in P({a,b,c}) |
| Antichain | Eine Teilmenge, in der keine zwei Elemente vergleichbar sind | {{a}, {b}} in P({a,b}) |
| Hasse-Diagramm | Visuelle Darstellung eines Posets | Zeichnen Sie Kanten nur zur Abdeckung von Beziehungen |
| Obergrenze | Ein Element ≥ jedes Element in einer Teilmenge | sup({2,3}) = 6 in (ℤ, \|) (Teilbarkeit) |
| Kleinste Obergrenze (sup) | Kleinste Obergrenze | sup({2,3}) in (ℕ, ≤) ist 3 |
| Größte Untergrenze (inf) | Größte Untergrenze | inf({4,6}) in (ℕ, \|) ist 2 |
---

## Funktionen
Eine **Funktion** f: A → B weist jedem Element von A genau ein Element von B zu.
### Klassifizierung von Funktionen
| Geben Sie | ein Definition | Beispiel |
|------|------------|---------|
| Injektiv (eins zu eins) | f(a) = f(b) → a = b | f(x) = 2x von ℤ → ℤ |
| Surjektiv (auf) | ∀b ∈ B, ∃a ∈ A: f(a) = b | f(x) = x mod 2 von ℤ → {0,1} |
| Bijektiv | Sowohl injektiv als auch surjektiv | f(x) = x + 1 von ℤ → ℤ |
### Wichtige Funktionskonzepte
| Konzept | Definition | Anwendungsfall |
|---------|------------|----------|
| Umkehrfunktion | f⁻¹ existiert genau dann, wenn f bijektiv ist | Verschlüsselte Daten entschlüsseln |
| Zusammensetzung | (g ∘ f)(x) = g(f(x)) | Verkettungstransformationen |
| Identitätsfunktion | id(x) = x | Neutrales Element für die Komposition |
| Festpunkt | f(x) = x | Rekursive Definitionen, Semantik |
| Permutation | Eine Bijektion von einer Menge zu sich selbst | Daten neu anordnen, mischen |
### Zählfunktionen
Gegeben endliche Mengen |A| = m und |B| = n:
| Geben Sie | ein Zählen |
|------|-------|
| Alle Funktionen A → B | nᵐ |
| Injektionsfunktionen | N! / (n−m)! (wenn n ≥ m, sonst 0) |
| Surjektive Funktionen | Σₖ₌₀ⁿ (−1)ᵏ · C(n,k) · (n−k)ᵐ (durch Einschluss-Ausschluss) |
| Bijektive Funktionen | N! (wenn m = n) |
---

## Kombinatorik
Kombinatorik ist die Mathematik des Zählens, Ordnens und Auswählens.
### Grundlegende Zählprinzipien
| Prinzip | Aussage | Beispiel |
|-----------|-----------|---------|
| Summenregel | Wenn A und B disjunkt sind, gilt |A ∪ B| = |A| + |B| | Auswahl einer Frucht: 3 Äpfel + 4 Orangen = 7 Optionen |
| Produktregel | |A × B| = |A| · |B| | Outfit: 3 Hemden × 4 Hosen = 12 Outfits |
| Bijektionsregel | Wenn f: A → B eine Bijektion ist, |A| = |B| | Zählen Sie Teilmengen durch Zählen von Binärzeichenfolgen |
| Komplement | |A| = |U| − |Aᶜ| | Zählen Sie „mindestens eins“ als Gesamtsumme minus „keine“ |
### Permutationen und Kombinationen
| Notation | Name | Formel | Bedeutung |
|----------|------|---------|---------|
| C(n, k) oder (n k) | Binomialkoeffizient | N! / (k!(n−k)!) | Möglichkeiten, k Elemente aus n auszuwählen (Reihenfolge spielt keine Rolle) |
| P(n, k) | k-Permutationen von n | N! / (n−k)! | Möglichkeiten, k Elemente aus n anzuordnen (Reihenfolge ist wichtig) |
| N! | Fakultät | n × (n−1) × ... × 1 | Möglichkeiten, alle n Elemente anzuordnen |
| (n k) mit Wiederholung | Mehrfachauswahl | C(n+k−1, k) | Wählen Sie k aus n mit erlaubter Wiederholung |
**Binomialsatz:**
(x + y)ⁿ = Σₖ₌₀ⁿ C(n,k) · xᵏ · yⁿ⁻ᵏ
**Pascals Identität:** C(n,k) = C(n−1,k−1) + C(n−1,k)
### Das Pigeonhole-Prinzip
**Grundform:** Wenn n+1 Objekte in n Boxen platziert werden, enthält mindestens eine Box ≥ 2 Objekte.
**Allgemeine Form:** Wenn N Objekte in k Boxen platziert werden, enthält mindestens eine Box ≥ ⌈N/k⌉ Objekte.
**Arbeitsbeispiele:**
1. Von 13 Personen müssen mindestens 2 denselben Geburtsmonat haben. (13 Personen, 12 Monate → Schublade.)
2. Zeigen Sie, dass es unter 5 beliebigen ganzen Zahlen 3 gibt, deren Summe durch 3 teilbar ist.
   - Betrachten Sie die Reste Mod 3: {0, 1, 2}. Bei 5 ganzen Zahlen und 3 Restklassen teilen sich nach verallgemeinerter Schublade mindestens ⌈5/3⌉ = 2 einen Rest.
   - Wenn 3 einen Rest r teilen: ihre Summe ≡ 3r ≡ 0 (mod 3).
   - Wenn 2 Rest 0 und 2 Rest 1 teilen: Wählen Sie eines aus jedem Paar plus ein Rest-0-Element → Summe ≡ 0 (Mod 3).
3. **Anwendung in CS:** Jeder verlustfreie Komprimierungsalgorithmus muss einige Eingaben erweitern. (Wenn jeder n-Bit-String auf < n Bits komprimiert würde, würden Sie 2ⁿ Strings in weniger als 2ⁿ komprimierte Strings abbilden – was gegen die Injektivität verstößt.)
### Katalanische Zahlen
Die n-te **katalanische Zahl** Cₙ = C(2n, n) / (n+1) zählt:
| Struktur | Beispiel |
|-----------|---------|
| Gültige Klammersequenzen | ()(), (()) für n = 2 |
| Binärbäume mit n internen Knoten | 2 Bäume für n = 2 |
| Wege, die die Diagonale nicht kreuzen | Gitterpfade von (0,0) bis (n,n), die unter y = x | bleiben
| Triangulationen eines Polygons | Möglichkeiten, ein (n+2)-Eck in Dreiecke zu unterteilen |
Erste paar: C₀ = 1, C₁ = 1, C₂ = 2, C₃ = 5, C₄ = 14, C₅ = 42.
Wiederholung: Cₙ₊₁ = Σᵢ₌₀ⁿ Cᵢ · Cₙ₋ᵢ
---

## Wiederholungsbeziehungen
Eine **Wiederholungsbeziehung** definiert jeden Term einer Sequenz als Funktion vorhergehender Terme.
### Typen und Lösungen
| Geben Sie | ein Formular | Lösungsmethode |
|------|------|---|
| Linear homogen (konstanter Koeffizient) | aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ | Charakteristische Gleichung |
| Linear inhomogen | aₙ = c₁aₙ₋₁ + ... + f(n) | Besondere Lösung + homogene Lösung |
| Teile und herrsche | T(n) = aT(n/b) + f(n) | Mastersatz |
### Charakteristische Gleichungsmethode
Bilden Sie für aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ die charakteristische Gleichung:
r² − c₁r − c₂ = 0
| Fall | Wurzeln | Allgemeine Lösung |
|------|-------|------------------|
| Zwei verschiedene reelle Wurzeln r₁, r₂ | r₁ ≠ r₂ | aₙ = A·r₁ⁿ + B·r₂ⁿ |
| Wiederholte Wurzel r | r₁ = r₂ = r | aₙ = (A + Bn)·rⁿ |
| Komplexe Wurzeln α ± βi | In Polar umwandeln: r·e^(±iθ) | aₙ = rⁿ(A cos(nθ) + B sin(nθ)) |
**Arbeitsbeispiel:** Fibonacci-Folge Fₙ = Fₙ₋₁ + Fₙ₋₂, F₀ = 0, F₁ = 1.
- Charakteristische Gleichung: r² − r − 1 = 0
- Wurzeln: r = (1 ± √5) / 2 → φ = (1+√5)/2 ≈ 1,618, ψ = (1−√5)/2 ≈ −0,618
- Allgemeine Lösung: Fₙ = A·φⁿ + B·ψⁿ
- Aus Anfangsbedingungen: A = 1/√5, B = −1/√5
- **Geschlossene Form:** Fₙ = (φⁿ − ψⁿ) / √5 (Binet-Formel)
### Das Master-Theorem
Für Wiederholungen der Form T(n) = aT(n/b) + f(n) mit a ≥ 1, b > 1:
Sei c = log_b(a).
| Fall | Zustand | Lösung |
|------|-----------|----------|
| 1 | f(n) = O(nᵈ) mit d< c | T(n) = Θ(nᶜ) |
| 2 | f(n) = Θ(nᶜ) | T(n) = Θ(nᶜ log n) |
| 3 | f(n) = Θ(nᵈ) where d >c und af(n/b) ≤ kf(n) für ein k < 1 | T(n) = Θ(nᵈ) |
**Beispiele:**
- Zusammenführungssortierung: T(n) = 2T(n/2) + O(n). Hier a=2, b=2, c=1, f(n)=n=Θ(n¹). Fall 2: T(n) = Θ(n log n).
- Binäre Suche: T(n) = T(n/2) + O(1). Hier a=1, b=2, c=0, f(n)=1=Θ(n⁰). Fall 2: T(n) = Θ(log n).
---

## Generieren von Funktionen
Eine **erzeugende Funktion** kodiert eine Folge (aₙ) als Koeffizienten einer formalen Potenzreihe.
### Typen
| Geben Sie | ein Formular | Anwendungsfall |
|------|------|----------|
| Gewöhnlich (OGF) | G(x) = Σₙ₌₀^∞ aₙxⁿ | Unbeschriftete Strukturen, Kompositionen |
| Exponentiell (EGF) | E(x) = Σₙ₌₀^∞ aₙxⁿ/n! | Beschriftete Strukturen, Permutationen |
### Gemeinsame Generierungsfunktionen
| Sequenz aₙ | OGF G(x) |
|-------------|-----------|
| 1, 1, 1, 1, ... | 1/(1−x) |
| 1, 2, 3, 4, ... | 1/(1−x)² |
| 1, r, r², r³, ... | 1/(1−rx) |
| C(n,k) für festes k | xᵏ/(1−x)ᵏ⁺¹ |
| Fibonacci Fₙ | x/(1−x−x²) |
| Katalanisch Cₙ | (1 − √(1−4x)) / (2x) |
### Verwenden von Generierungsfunktionen zum Lösen von Wiederholungen
**Arbeitsbeispiel:** Lösen Sie aₙ = 3aₙ₋₁ − 2aₙ₋₂, a₀ = 1, a₁ = 3.
1. Sei G(x) = Σ aₙxⁿ.
2. Aus der Wiederholung: G(x) − a₀ − a₁x = 3x(G(x) − a₀) − 2x²G(x)
3. Ersatz: G(x) − 1 − 3x = 3x(G(x) − 1) − 2x²G(x)
4. G(x)(1 − 3x + 2x²) = 1
5. G(x) = 1 / (1 − 3x + 2x²) = 1 / ((1−x)(1−2x))
6. Partielle Brüche: G(x) = 2/(1−2x) − 1/(1−x)
7. Koeffizienten extrahieren: aₙ = 2·2ⁿ − 1 = 2ⁿ⁺¹ − 1
**Verifizierung:** a₀ = 2−1 = 1, a₁ = 4−1 = 3, a₂ = 8−1 = 7. Überprüfen Sie: 3(3) − 2(1) = 7.
---

## Boolesche Algebra und Aussagenlogik
Die Boolesche Algebra ist die Algebra zweier Wahrheitswerte: **Wahr (1)** und **Falsch (0)**. Es ist die mathematische Grundlage digitaler Schaltkreise, Datenbankabfragen und Programmierbedingungen.
### Operationen und Gesetze
| Betrieb | Symbol | Bedeutung | Wahrheitstabelle |
|-----------|--------|---------|-------------|
| UND | p ∧ q | Nur wahr, wenn beide wahr sind | T∧T=T, T∧F=F, F∧T=F, F∧F=F |
| ODER | p ∨ q | Wahr, wenn mindestens einer wahr ist | T∨T=T, T∨F=T, F∨T=T, F∨F=F |
| NICHT | ¬p | Negation | ¬T=F, ¬F=T |
| XOR | p ⊕ q | Wahr, wenn genau einer wahr ist | T⊕T=F, T⊕F=T, F⊕T=T, F⊕F=F |
| IMPLIZIERT | p → q | Nur falsch, wenn p=T und q=F | T→T=T, T→F=F, F→T=T, F→F=T |
| BIKONDITIONAL | p ↔ q | Wahr, wenn beide denselben Wert | haben T↔T=T, T↔F=F, F↔T=F, F↔F=T |
### Wichtige boolesche Identitäten
| Recht | Formel |
|-----|--------|
| Kommutativität | p ∧ q = q ∧ p; p ∨ q = q ∨ p |
| Assoziativität | (p ∧ q) ∧ r = p ∧ (q ∧ r) |
| Distributivität | p ∧ (q ∨ r) = (p ∧ q) ∨ (p ∧ r) |
| De Morgans Gesetze | ¬(p ∧ q) = ¬p ∨ ¬q; ¬(p ∨ q) = ¬p ∧ ¬q |
| Doppelte Verneinung | ¬(¬p) = p |
| Idempotenz | p ∧ p = p; p ∨ p = p |
| Absorption | p ∨ (p ∧ q) = p; p ∧ (p ∨ q) = p |
| Kontrapositiv | (p → q) ≡ (¬q → ¬p) |
### Normalformen
| Formular | Struktur | Anwendungsfall |
|------|-----------|----------|
| Konjunktive Normalform (CNF) | UND von ORs: (A∨B) ∧ (C∨D) | SAT-Löser, Beweis des Auflösungstheorems |
| Disjunktive Normalform (DNF) | ODER von ANDs: (A∧B) ∨ (C∧D) | Schaltungsentwurf, regelbasierte Systeme |
**Konvertierung in CNF:** Wenden Sie die Gesetze von De Morgan an, verteilen Sie ODER über UND, eliminieren Sie doppelte Verneinungen.
---

## Modulare Arithmetik und Kongruenzen
Die modulare Arithmetik untersucht ganze Zahlen unter der Operation „Rest nach Division“. Es ist wichtig für Kryptographie, Hashing und Zahlentheorie.
### Kerndefinitionen
| Konzept | Notation | Definition |
|---------|----------|------------|
| Kongruenz | a ≡ b (mod n) | n teilt (a − b) |
| Rückstandsklasse | [a]ₙ | Die Menge {a + kn : k ∈ ℤ} |
| Modulare Umkehrung | a⁻¹ mod n | Wert x, so dass ax ≡ 1 (mod n) |
| Eulers Gesamtheit | φ(n) | Anzahl der ganzen Zahlen in {1,...,n} teilerfremd zu n |
### Schlüsseleigenschaften
| Eigentum | Aussage |
|----------|----------|
| Zusatz | Wenn a ≡ b und c ≡ d (mod n), dann a+c ≡ b+d (mod n) |
| Multiplikation | Wenn a ≡ b und c ≡ d (mod n), dann ist ac ≡ bd (mod n) |
| Fermats kleiner Satz | Wenn p eine Primzahl ist und ggT(a,p) = 1, dann ist aᵖ⁻¹ ≡ 1 (mod p) |
| Satz von Euler | Wenn ggT(a,n) = 1, dann a^φ(n) ≡ 1 (mod n) |
| Chinesischer Restsatz | Wenn gcd(m,n) = 1, hat das System x ≡ a (mod m), x ≡ b (mod n) eine eindeutige Lösung mod mn |
### Berechnung von Eulers Totient
Für n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ (Primfaktorzerlegung):
φ(n) = n · (1 − 1/p₁) · (1 − 1/p₂) · ... · (1 − 1/pₖ)
**Beispiel:** φ(12) = 12 · (1 − 1/2) · (1 − 1/3) = 12 · 1/2 · 2/3 = 4. Tatsächlich sind {1, 5, 7, 11} teilerfremd zu 12.
### Anwendung: RSA-Kryptographie (Übersicht)
1. Wählen Sie große Primzahlen p, q. Berechnen Sie n = pq, φ(n) = (p−1)(q−1).
2. Wählen Sie e so, dass gcd(e, φ(n)) = 1 (öffentlicher Exponent).
3. Berechnen Sie d ≡ e⁻¹ (mod φ(n)) (privater Exponent).
4. Verschlüsseln: c = mᵉ mod n. Entschlüsseln: m = cᵈ mod n.
5. Die Sicherheit beruht auf der Schwierigkeit, n zu faktorisieren, um p und q zu finden.
---

## Mathematische Induktion
**Mathematische Induktion** ist die primäre Beweistechnik für Aussagen über alle natürlichen Zahlen.
### Struktur eines Beweises durch Induktion
1. **Basisfall:** Beweisen Sie die Aussage für n = 0 (oder n = 1).
2. **Induktiver Schritt:** Nehmen Sie an, dass die Aussage für n = k gilt (induktive Hypothese), und beweisen Sie sie dann für n = k + 1.
### Varianten
| Variante | Wann zu verwenden |
|---------|-------------|
| Einfache Induktion | Beweisen Sie P(k) → P(k+1) |
| Starke Induktion | Nehmen Sie P(0), P(1), ..., P(k) an, um P(k+1) | zu beweisen
| Strukturelle Induktion | Eigenschaften rekursiv definierter Strukturen (Bäume, Formeln) beweisen |
| Transfinite Induktion | Erweitern Sie die Induktion auf wohlgeordnete Mengen über ℕ | hinaus
**Arbeitsbeispiel (starke Induktion):** Beweisen Sie, dass jede ganze Zahl n ≥ 2 als Produkt von Primzahlen geschrieben werden kann.
- Basis: n = 2 ist eine Primzahl, also ein Produkt von Primzahlen (sich selbst).
- Induktiver Schritt: Annahme wahr für alle ganzen Zahlen von 2 bis k. Betrachten Sie k+1.
  - Wenn k+1 eine Primzahl ist, fertig.
  - Wenn k+1 zusammengesetzt ist, ist k+1 = ab, wobei 2 ≤ a, b ≤ k. Nach der Induktionsannahme sind sowohl a als auch b Produkte von Primzahlen, also ist k+1 ein Produkt von Primzahlen.
---

## Relevanz für maschinelles Lernen und Datenwissenschaft
| Diskretes mathematisches Konzept | Anwendung in ML / Data Science |
|---------|--------------------|
| Mengenlehre | Datenbankoperationen (SQL JOINs), Feature-Set-Manipulation, Wahrscheinlichkeitsereignisse |
| Beziehungen | Datenbankschemata, Entity-Relationship-Modellierung, Wissensgraphen |
| Funktionen | Aktivierungsfunktionen, Feature-Transformationen, Zuordnungen zwischen Leerzeichen |
| Kombinatorik | Merkmalsauswahl (Auswahl von k aus n), Größenbestimmung der Hyperparameter-Rastersuche |
| Schubladenprinzip | Hashing-Kollisionen, Untergrenzen der Komprimierung, Beweise der Informationstheorie |
| Wiederholungsbeziehungen | Dynamische Programmierung, Algorithmenkomplexitätsanalyse, Zeitreihenmodelle |
| Funktionen generieren | Wahrscheinlichkeitserzeugende Funktionen, Lösung kombinatorischer Probleme im Feature Engineering |
| Katalanische Zahlen | Baumstrukturen zählen (Entscheidungsbäume), Ausdrücke analysieren, Stapeloperationen |
| Graphentheorie (siehe nächste Datei) | Analyse sozialer Netzwerke, Empfehlungssysteme, Wissensrepräsentation |
---

## Zusammenfassung
| Thema | Kernidee | Schlüsselwerkzeug |
|-------|-----------|----------|
| Mengenlehre | Sammlungen verschiedener Objekte | ZFC-Axiome, Kardinalität, Operationen |
| Beziehungen | Verbindungen zwischen Elementen | Äquivalenzrelationen, Teilordnungen |
| Funktionen | Zuordnungen zwischen Mengen | Injektivität, Surjektivität, Bijektion |
| Kombinatorik | Zählvereinbarungen | Binomialkoeffizienten, Schubladenprinzip |
| Wiederholungsbeziehungen | Rekursiv definierte Sequenzen | Charakteristische Gleichungen, Master-Theorem |
| Funktionen generieren | Folgen als Potenzreihen | OGF/EGF, Rezidiven algebraisch lösen |
Die diskrete Mathematik liefert die Sprache und die Werkzeuge zum Nachdenken über endliche oder abzählbare Strukturen – und das ist genau das, was Computer manipulieren. Jeder Algorithmus, jede Datenstruktur, jede Datenbankabfrage und jedes kryptografische Protokoll basiert auf diskreten Grundlagen. Die Beherrschung dieser Themen schärft die Fähigkeit zur Problemlösung und bietet das Vokabular für fortgeschrittene Studien in Algorithmen, Komplexitätstheorie und maschinellem Lernen.