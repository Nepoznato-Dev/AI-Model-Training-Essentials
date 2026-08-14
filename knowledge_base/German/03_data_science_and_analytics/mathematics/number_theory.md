---
# Metadata
title: "Number Theory"
description: "Divisibility, primes, modular arithmetic, Euler's theorem, Fermat's little theorem, Chinese Remainder Theorem, and applications to cryptography"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial deep-dive into number theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [number-theory, primes, divisibility, modular-arithmetic, cryptography, euler-theorem, fermat, chinese-remainder-theorem]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Zahlentheorie
Die Zahlentheorie ist das Studium der ganzen Zahlen – ganze Zahlen und ihrer Eigenschaften. Gauß nannte es „die Königin der Mathematik“. Trotz der Untersuchung der einfachsten Objekte (1, 2, 3, ...) wirft die Zahlentheorie einige der tiefgreifendsten und schwierigsten Probleme der gesamten Mathematik auf. Heute ist es die Grundlage für moderne Kryptographie, Hashing-Algorithmen, Fehlerkorrekturcodes und die Generierung von Zufallszahlen.
---

## Teilbarkeit und der Divisionsalgorithmus
### Kerndefinitionen
| Begriff | Definition | Beispiel |
|------|------------|---------|
| **Teilt** | ein \| b bedeutet ∃k ∈ ℤ: b = ak | 3 \| 12 (da 12 = 3 × 4) |
| **Divisor** | Eine Zahl, die ein anderes | teilt Teiler von 12: 1, 2, 3, 4, 6, 12 |
| **Mehrere** | b ist ein Vielfaches von a, wenn a \| b | 15 ist ein Vielfaches von 5 |
| **Quotient** | Das Ergebnis der Division | 17 ÷ 5 = Quotient 3 |
| **Rest** | Was nach der Teilung übrig bleibt | 17 ÷ 5 = Rest 2 |
### Der Divisionsalgorithmus
Für alle ganzen Zahlen a und b mit b > 0 gibt es eindeutige ganze Zahlen q (Quotient) und r (Rest), sodass:
a = bq + r, wobei 0 ≤ r < b
**Beispiel:** 23 = 5 × 4 + 3. Quotient q = 4, Rest r = 3.
### Eigenschaften der Teilbarkeit
| Eigentum | Aussage |
|----------|-----------|
| Transitivität | Wenn ein \| b und b \| c, dann ein \| c |
| Linearität | Wenn ein \| b und a \| c, dann ein \| (bx + cy) für alle ganzen Zahlen x, y |
| Vergleich | Wenn ein \| b und b > 0, dann a ≤ b |
| Trivial | ein \| 0 für alle a; 1 \| a für alle a; ein \| a für alle a ≠ 0 |
---

## Größter gemeinsamer Teiler (GCD)
Der **größte gemeinsame Teiler** von a und b, bezeichnet als ggT(a, b), ist die größte positive ganze Zahl, die sowohl a als auch b teilt.
### Der euklidische Algorithmus
Der effizienteste klassische Algorithmus zur Berechnung des GCD.
**Wichtige Erkenntnis:** gcd(a, b) = gcd(b, a mod b)
**Algorithmus:**```
function gcd(a, b):
    while b ≠ 0:
        t = b
        b = a mod b
        a = t
    return a
```

**Arbeitsbeispiel:** gcd(252, 105)
- 252 = 105 × 2 + 42 → gcd(105, 42)
- 105 = 42 × 2 + 21 → gcd(42, 21)
- 42 = 21 × 2 + 0 → gcd(21, 0)
- Ergebnis: gcd(252, 105) = 21
| Eigentum | Wert |
|----------|-------|
| Zeitkomplexität | O(log(min(a, b))) |
| Raumkomplexität | O(1) iterativ |
### Bézouts Identität
Für alle ganzen Zahlen a, b gibt es ganze Zahlen x, y, so dass:
ax + by = ggT(a, b)
**Erweiterter euklidischer Algorithmus** berechnet gcd(a, b) und die Koeffizienten x, y gleichzeitig.
**Arbeitsbeispiel:** Finden Sie x, y, sodass 252x + 105y = 21.
- Rücksubstitution aus dem euklidischen Algorithmus:
  - 21 = 105 − 42 × 2
  - 42 = 252 − 105 × 2
  - 21 = 105 − (252 − 105 × 2) × 2 = 105 × 5 − 252 × 2
- Also x = −2, y = 5. Überprüfen Sie: 252(−2) + 105(5) = −504 + 525 = 21.
### Schlüsseleigenschaften von GCD
| Eigentum | Aussage |
|----------|-----------|
| gcd(a, 0) | = ein |
| gcd(a, 1) | = 1 (a und 1 sind immer teilerfremd) |
| gcd(a, b) = gcd(b, a) | Kommutativ |
| gcd(a, b) = gcd(a, b + ka) | Durch das Hinzufügen von Vielfachen ändert sich GCD | nicht
| gcd(ca, cb) | = c · ggT(a, b) |
| Coprime | gcd(a, b) = 1 bedeutet, dass a und b keine gemeinsamen Faktoren haben |
---

## Primzahlen
Eine **Primzahl** ist eine ganze Zahl größer als 1, deren einzige positive Teiler 1 und sich selbst sind.
### Grundlegende Eigenschaften
| Eigentum | Aussage |
|----------|-----------|
| **Grundsatz der Arithmetik** | Jede ganze Zahl n > 1 hat eine eindeutige Primfaktorzerlegung |
| **Unendliche Primzahlen** | Es gibt unendlich viele Primzahlen (Euklid, ~300 v. Chr.) |
| **Primzahlsatz** | Die Anzahl der Primzahlen ≤ n beträgt ungefähr n / ln(n) |
| **Bertrands Postulat** | Für jedes n > 1 gibt es eine Primzahl p mit n < p < 2n |
### Die ersten Primzahlen
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97...

### Primfaktorisierung
Jede ganze Zahl n > 1 kann eindeutig geschrieben werden als:
n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ
wobei p₁ < p₂ < ... < pₖ Primzahlen sind und aᵢ ≥ 1.
**Beispiele:**
- 60 = 2² × 3 × 5
- 360 = 2³ × 3² × 5
- 1001 = 7 × 11 × 13
**Faktorisierung zur Berechnung von GCD und LCM verwenden:**
- gcd(a, b) = Produkt der minimalen Potenzen gemeinsamer Primzahlen
- lcm(a, b) = Produkt der maximalen Potenzen aller Primzahlen
**Beispiel:** a = 12 = 2² × 3, b = 18 = 2 × 3²
- gcd(12, 18) = 2¹ × 3¹ = 6
- lcm(12, 18) = 2² × 3² = 36
### Sieb des Eratosthenes
Der klassische Algorithmus zum Finden aller Primzahlen bis zu einem Grenzwert N.
| Eigentum | Wert |
|----------|-------|
| Zeitkomplexität | O(N log log N) |
| Raumkomplexität | O(N) |
**Algorithmus:**
1. Listen Sie alle ganzen Zahlen von 2 bis N auf.
2. Beginnen Sie mit p = 2. Streichen Sie alle Vielfachen von p durch (beginnend mit p²).
3. Finden Sie die nächste ungekreuzte Zahl > S. Setze p auf diese Zahl.
4. Wiederholen, bis p² > N. Alle ungekreuzten Zahlen sind Primzahlen.
### Primalitätstest
| Methode | Geben Sie | ein Zeit | Anwendungsfall |
|--------|------|------|----------|
| Versuchsabteilung | Deterministisch | O(√n) | Kleine Zahlen |
| Fermat-Test | Wahrscheinlichkeit | O(k log² n) | Schnelles Screening |
| Miller-Rabin | Wahrscheinlichkeit | O(k log² n) | Allzweck |
| AKS | Deterministisch | O(log⁶ n) | Theoretische Bedeutung |
**Fermat-Primalitätstest:** Wenn p eine Primzahl ist und ggT(a, p) = 1, dann ist aᵖ⁻¹ ≡ 1 (mod p). Wenn dies für einige a fehlschlägt, dann ist p definitiv zusammengesetzt. Wenn es für viele zufällige a-Werte gilt, ist p wahrscheinlich eine Primzahl.
**Vorbehalt:** Carmichael-Zahlen (z. B. 561) bestehen den Fermat-Test für alle teilerfremden Basen, sind aber zusammengesetzt. Miller-Rabin vermeidet dieses Problem.
---

## Modulare Arithmetik
Die modulare Arithmetik untersucht ganze Zahlen unter „Wraparound“ – Arithmetik auf einem Zifferblatt.
### Kongruenzbeziehungen
a ≡ b (mod n) bedeutet n | (a − b), d. h. a und b lassen bei Division durch n den gleichen Rest übrig.
### Arithmetische Eigenschaften
| Betrieb | Regel |
|-----------|------|
| Zusatz | (a + b) mod n = ((a mod n) + (b mod n)) mod n |
| Multiplikation | (a × b) mod n = ((a mod n) × (b mod n)) mod n |
| Potenzierung | aᵇ mod n kann durch wiederholtes Quadrieren | effizient berechnet werden
| Negation | (−a) mod n = n − (a mod n) |
### Modulare Potenzierung
Effizientes Berechnen von aᵇ mod n mithilfe von **wiederholter Quadrierung**:
**Arbeitsbeispiel:** 3¹³ Mod 7
- 13 im Binärformat: 1101
- 3¹ = 3 mod 7 = 3
- 3² = 9 mod 7 = 2
- 3⁴ = 4 mod 7 = 4
- 3⁸ = 16 mod 7 = 2
- 3¹³ = 3⁸ × 3⁴ × 3¹ = 2 × 4 × 3 = 24 mod 7 = 3
| Eigentum | Wert |
|----------|-------|
| Zeitkomplexität | O(log b · log² n) |
| Raumkomplexität | O(1) |
### Eulers Totient-Funktion
φ(n) zählt die ganzen Zahlen von 1 bis n, die teilerfremd zu n sind.
| n | φ(n) | Teilerfremde ganze Zahlen |
|---|------|----|
| 1 | 1 | {1} |
| 2 | 1 | {1} |
| 6 | 2 | {1, 5} |
| 7 | 6 | {1, 2, 3, 4, 5, 6} (7 ist eine Primzahl) |
| 10 | 4 | {1, 3, 7, 9} |
| 12 | 4 | {1, 5, 7, 11} |
**Formeln:**
- Wenn p eine Primzahl ist: φ(p) = p − 1
- Wenn p eine Primzahl ist: φ(pᵏ) = pᵏ − pᵏ⁻¹ = pᵏ⁻¹(p − 1)
- Wenn ggT(m, n) = 1: φ(mn) = φ(m) · φ(n) (Multiplikativität)
- Allgemein: φ(n) = n · Π_{p|n} (1 − 1/p), wobei das Produkt über verschiedenen Primfaktoren von n liegt
---

## Schlüsselsätze
### Fermats kleiner Satz
Wenn p eine Primzahl ist und ggT(a, p) = 1, dann:
aᵖ⁻¹ ≡ 1 (mod p)
**Folge (für alle a):** aᵖ ≡ a (mod p)
**Verwendung:** Schnelle modulare Umkehrung, wenn Modul prim ist: a⁻¹ ≡ aᵖ⁻² (mod p)
**Arbeitsbeispiel:** Finden Sie 3⁻¹ Mod 7.
- Von Fermat: 3⁻¹ ≡ 3⁵ (mod 7)
- 3² = 9 ≡ 2 (mod 7)
- 3⁴ = 4 (Mod 7)
- 3⁵ = 3⁴ × 3 = 4 × 3 = 12 ≡ 5 (Mod 7)
- Prüfen: 3 × 5 = 15 ≡ 1 (Mod 7).
### Satz von Euler (Verallgemeinerung von Fermat)
Wenn gcd(a, n) = 1, dann:
a^φ(n) ≡ 1 (mod n)
Dies verallgemeinert Fermats kleinen Satz von Primzahlen auf jeden Modul.
### Chinesischer Restsatz (CRT)
Wenn m₁, m₂, ..., mₖ paarweise teilerfremd sind, gilt für das System:
x ≡ a₁ (mod m₁)
x ≡ a₂ (mod m₂)
...
x ≡ aₖ (mod mₖ)
hat eine eindeutige Lösung modulo M = m₁ · m₂ · ... · mₖ.
**Arbeitsbeispiel:** Lösen Sie x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7).
- M = 3 × 5 × 7 = 105
- M₁ = 105/3 = 35; M₂ = 105/5 = 21; M₃ = 105/7 = 15
- Finden Sie Umkehrungen: 35y₁ ≡ 1 (mod 3) → 2y₁ ≡ 1 → y₁ = 2
  21y₂ ≡ 1 (mod 5) → y₂ ≡ 1 (mod 5) → y₂ = 1
  15y₃ ≡ 1 (mod 7) → y₃ ≡ 1 (mod 7) → y₃ = 1
- x = 2·35·2 + 3·21·1 + 2·15·1 = 140 + 63 + 30 = 233
- x ≡ 233 mod 105 = 23
- Überprüfen Sie: 23 Mod 3 = 2, 23 Mod 5 = 3, 23 Mod 7 = 2.
### Satz von Wilson
(p − 1)! ≡ −1 (mod p) genau dann, wenn p eine Primzahl ist.
Hauptsächlich von theoretischem Interesse – für Primzahltests nicht praktisch, da die Berechnung von Fakultäten teuer ist.
### Quadratische Reste
Eine ganze Zahl a ist ein **quadratischer Rest mod n**, wenn x² ≡ a (mod n) eine Lösung hat.
**Eulers Kriterium:** a ist ein quadratischer Rest mod prime p genau dann, wenn a^((p−1)/2) ≡ 1 (mod p).
**Legendes Symbol:** (a/p) = a^((p−1)/2) mod p, was +1, −1 oder 0 ergibt.
**Quadratische Reziprozität** (Gauss): Für verschiedene ungerade Primzahlen p, q:
(p/q)(q/p) = (−1)^((p−1)/2 · (q−1)/2)
Dieser tiefe Satz verbindet quadratische Residuen über verschiedene Primzahlen hinweg und verfügt über acht Zusatzgesetze für die Fälle p = 2.
---

## Anwendungen zur Kryptographie
### RSA-Kryptosystem
Das am weitesten verbreitete Public-Key-Kryptosystem, basierend auf der Schwierigkeit, große ganze Zahlen zu faktorisieren.
**Einrichtung:**
1. Wählen Sie zwei große Primzahlen p, q (typischerweise jeweils 1024+ Bits)
2. Berechnen Sie n = pq und φ(n) = (p−1)(q−1)
3. Wählen Sie e, so dass 1 < e < φ(n) und ggT(e, φ(n)) = 1 (häufig: e = 65537)
4. Berechnen Sie d ≡ e⁻¹ (mod φ(n)) mit dem erweiterten euklidischen Algorithmus
5. **Öffentlicher Schlüssel:** (n, e). **Privater Schlüssel:** (n, d)
**Verschlüsselung:** c = mᵉ mod n (wobei m die Klartextnachricht ist)
**Entschlüsselung:** m = cᵈ mod n
**Warum es funktioniert:** cᵈ = m^(ed) ≡ m (mod n) nach dem Satz von Euler, da ed ≡ 1 (mod φ(n)).
**Sicherheit:** Die Faktorisierung von n in p und q ist für große n (2048+ Bits) rechnerisch nicht durchführbar. Ohne p und q kann ein Angreifer φ(n) nicht berechnen und somit d nicht finden.
### Diffie-Hellman-Schlüsselaustausch
Ermöglicht zwei Parteien, über einen unsicheren Kanal ein gemeinsames Geheimnis herzustellen.
**Aufbau:** Vereinbaren Sie eine große Primzahl p und einen Generator g (mod p).
**Protokoll:**
1. Alice wählt Geheimnis a und sendet A = gᵃ mod p an Bob
2. Bob wählt Geheimnis b und sendet B = gᵇ mod p an Alice
3. Alice berechnet s = Bᵃ mod p = gᵃᵇ mod p
4. Bob berechnet s = Aᵇ mod p = gᵃᵇ mod p
5. Beide teilen das Geheimnis s = gᵃᵇ mod p
**Sicherheit:** Basierend auf der Schwierigkeit des **diskreten Logarithmusproblems** – Finden von a aus gᵃ mod p.
### Hash-Funktionen und Zahlentheorie
Gute Hash-Funktionen verwenden modulare Arithmetik, um Schlüssel gleichmäßig zu verteilen:
- **Multiplikatives Hashing:** h(k) = (k · A) mod m, wobei A ≈ m · (√5 − 1) / 2 (Goldener Schnitt)
- **Universelles Hashing:** h(k) = ((ak + b) mod p) mod m, wobei p eine Primzahl ist, a, b zufällig sind
---

## Relevanz für maschinelles Lernen und Datenwissenschaft
| Konzept der Zahlentheorie | Bewerbung |
|--------|-------------|
| Modulare Arithmetik | Hashing (Hash-Tabellen, Hash-Maps), Zufallszahlengenerierung |
| Primzahlen | Hash-Tabellengröße (Primärtabellengrößen verwenden, um Kollisionen zu reduzieren) |
| GCD / Euklidischer Algorithmus | Rationale Arithmetik, Vereinfachung von Brüchen in der Wahrscheinlichkeit |
| Modulare Potenzierung | Kryptografische Sicherheit für die Bereitstellung des ML-Modells über HTTPS |
| Eulers Gesamtheit | RSA-Schlüsselgenerierung, kryptografische Garantien verstehen |
| Chinesischer Restsatz | Verteilte Berechnung, parallele modulare Arithmetik |
| Primzahltest | Generieren von Primzahlen für kryptografische Operationen |
| Quadratische Residuen | Quadratisches Residuositätsproblem in der fortgeschrittenen Kryptographie |
| Endliche Felder (GF(p), GF(2ᵏ)) | Fehlerkorrekturcodes, Reed-Solomon-Codes, AES-Verschlüsselung |
---

## Zusammenfassung
| Thema | Kernidee | Wichtigstes Ergebnis |
|-------|-----------|------------|
| Teilbarkeit | Division mit Rest | Divisionsalgorithmus: a = bq + r |
| GCD | Größter gemeinsamer Faktor | Euklidischer Algorithmus: O(log n) |
| Primzahlen | Atome der ganzen Zahlen | Grundsatz der Arithmetik (eindeutige Faktorisierung) |
| Modulare Arithmetik | Umlaufarithmetik | Kongruenzklassen, modulare Potenzierung |
| Eulers Totient | Koprime-Ganzzahlen zählen | φ(n) = n · Π(1 − 1/p) |
| Fermats kleiner Satz | Abkürzung für Primzahlmodul | aᵖ⁻¹ ≡ 1 (mod p) |
| Satz von Euler | Verallgemeinerter Fermat | a^φ(n) ≡ 1 (mod n) |
| Chinesischer Restsatz | Modulare Systeme kombinieren | Einzigartiges Lösungsmod-Produkt von Koprime-Modulen |
| Kryptographie | Harte zahlentheoretische Probleme | RSA (Factoring), Diffie-Hellman (diskretes Protokoll) |
Die Zahlentheorie verwandelt einfache Fragen zu ganzen Zahlen in tiefgreifende Mathematik mit tiefgreifenden praktischen Anwendungen. Jede sichere Webverbindung, jede verschlüsselte Nachricht und jede digitale Signatur basiert auf zahlentheoretischen Ergebnissen, die Jahrhunderte vor der Existenz von Computern entdeckt wurden. Für Datenwissenschaftler und ML-Ingenieure bietet das Verständnis der Zahlentheorie Einblicke in Hashing, Zufallszahlengenerierung und die kryptografische Infrastruktur, die Daten während der Übertragung und im Ruhezustand schützt.