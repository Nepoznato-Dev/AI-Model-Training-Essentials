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
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-10"
    author: "Nepoznato-Dev"
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
# Teoria liczb
Teoria liczb zajmuje się badaniem liczb całkowitych — liczb całkowitych i ich właściwości. Gauss nazwał ją „królową matematyki”. Pomimo badania najprostszych obiektów (1, 2, 3, ...) teoria liczb stwarza jedne z najgłębszych i najtrudniejszych problemów w całej matematyce. Dziś stanowi podstawę współczesnej kryptografii, algorytmów mieszania, kodów korygujących błędy i generowania liczb losowych.
---

## Podzielność i algorytm dzielenia
### Podstawowe definicje
| Termin | Definicja | Przykład |
|------|------------|--------|
| **Dzieli** | \| b oznacza ∃k ∈ ℤ: b = ak | 3 \| 12 (ponieważ 12 = 3 × 4) |
| **Dzielnik** | Liczba dzieląca inną | Dzielniki 12: 1, 2, 3, 4, 6, 12 |
| **Wiele** | b jest wielokrotnością a jeśli a \| b | 15 jest wielokrotnością 5 |
| **Iloraz** | Wynik dzielenia | 17 ÷ 5 = iloraz 3 |
| **Reszta** | Co pozostało po dzieleniu | 17 ÷ 5 = reszta 2 |
### Algorytm dzielenia
Dla dowolnych liczb całkowitych aib z b > 0 istnieją unikalne liczby całkowite q (iloraz) i r (reszta) takie, że:
a = bq + r, gdzie 0 ≤ r < b
**Przykład:** 23 = 5 × 4 + 3. Iloraz q = 4, reszta r = 3.
### Właściwości podzielności
| Nieruchomość | Oświadczenie |
|---------|-----------|
| Przechodniość | Jeśli \| b i b \| c, następnie \| c |
| Liniowość | Jeśli \| b i a \| c, następnie \| (bx + cy) dla wszystkich liczb całkowitych x, y |
| Porównanie | Jeśli \| b i b > 0, następnie a ≤ b |
| Trywialne | \| 0 dla wszystkich a; 1 \| dla wszystkich; \| a dla wszystkich a ≠ 0 |
---

## Największy wspólny dzielnik (GCD)
**największy wspólny dzielnik** aib, oznaczony jako gcd(a, b), jest największą dodatnią liczbą całkowitą dzielącą zarówno aib.
### Algorytm euklidesowy
Najskuteczniejszy klasyczny algorytm obliczania GCD.
**Kluczowe spostrzeżenia:** gcd(a, b) = gcd(b, a mod b)
**Algorytm:**```
function gcd(a, b):
    while b ≠ 0:
        t = b
        b = a mod b
        a = t
    return a
```

**Przykład praktyczny:** gcd(252, 105)
- 252 = 105 × 2 + 42 → gcd(105, 42)
- 105 = 42 × 2 + 21 → gcd(42, 21)
- 42 = 21 × 2 + 0 → gcd(21, 0)
- Wynik: gcd(252, 105) = 21
| Nieruchomość | Wartość |
|---------|-------|
| Złożoność czasowa | O(log(min(a, b))) |
| Złożoność przestrzeni | O(1) iteracyjny |
### Tożsamość Bézouta
Dla dowolnych liczb całkowitych a, b istnieją liczby całkowite x, y takie, że:
topór + by = gcd(a, b)
**Rozszerzony algorytm euklidesowy** oblicza jednocześnie gcd(a, b) i współczynniki x, y.
**Przykład praktyczny:** Znajdź x, y takie, że 252x + 105y = 21.
- Podstawianie wsteczne z algorytmu Euklidesa:
  - 21 = 105 - 42 × 2
  - 42 = 252 - 105 × 2
  - 21 = 105 - (252 - 105 × 2) × 2 = 105 × 5 - 252 × 2
- Zatem x = −2, y = 5. Sprawdź: 252(−2) + 105(5) = −504 + 525 = 21.
### Kluczowe właściwości GCD
| Nieruchomość | Oświadczenie |
|---------|-----------|
| gcd(a, 0) | = a |
| gcd(a, 1) | = 1 (a i 1 są zawsze względnie pierwsze) |
| gcd(a, b) = gcd(b, a) | Przemienne |
| gcd(a, b) = gcd(a, b + ka) | Dodanie wielokrotności nie zmienia NWD |
| gcd(ca, cb) | = c · gcd(a, b) |
| Wysoka jakość | gcd(a, b) = 1 oznacza, że ​​aib nie mają wspólnych czynników |
---

## Liczby pierwsze
**Liczba pierwsza** to liczba całkowita większa niż 1, której jedynymi dodatnimi dzielnikami są 1 i ona sama.
### Podstawowe właściwości
| Nieruchomość | Oświadczenie |
|---------|-----------|
| **Podstawowe twierdzenie arytmetyki** | Każda liczba całkowita n > 1 ma unikalną rozkład na czynniki pierwsze |
| **Nieskończoność liczb pierwszych** | Istnieje nieskończenie wiele liczb pierwszych (Euklides, ~300 p.n.e.) |
| **Twierdzenie o liczbach pierwszych** | Liczba liczb pierwszych ≤ n wynosi w przybliżeniu n / ln(n) |
| **Postulat Bertranda** | Dla każdego n > 1 istnieje liczba pierwsza p z n < p < 2n |
### Pierwsze liczby pierwsze
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97...

### Faktoryzacja pierwsza
Każdą liczbę całkowitą n > 1 można zapisać jednoznacznie jako:
n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ
gdzie p₁ < p₂ < ... < pₖ są liczbami pierwszymi i aᵢ ≥ 1.
**Przykłady:**
- 60 = 2² × 3 × 5
- 360 = 2³ × 3² × 5
- 1001 = 7 × 11 × 13
**Użycie faktoryzacji do obliczenia GCD i LCM:**
- gcd(a, b) = iloczyn minimalnych potęg wspólnych liczb pierwszych
- lcm(a, b) = iloczyn maksymalnych potęg wszystkich liczb pierwszych
**Przykład:** a = 12 = 2² × 3, b = 18 = 2 × 3²
- gcd(12, 18) = 2¹ × 3¹ = 6
- lcm(12, 18) = 2² × 3² = 36
### Sito Eratostenesa
Klasyczny algorytm znajdowania wszystkich liczb pierwszych aż do granicy N.
| Nieruchomość | Wartość |
|---------|-------|
| Złożoność czasowa | O(N log log N) |
| Złożoność przestrzeni | O(N) |
**Algorytm:**
1. Wypisz wszystkie liczby całkowite od 2 do N.
2. Zacznij od p = 2. Skreśl wszystkie wielokrotności p (zaczynając od p²).
3. Znajdź następną nieprzekreśloną liczbę > str. Ustaw p na tę liczbę.
4. Powtarzaj aż p² > N. Wszystkie nieprzekreślone liczby są pierwsze.
### Testowanie pierwszości
| Metoda | Wpisz | Czas | Przypadek użycia |
|------------|------|------|---------|
| Oddział próbny | Deterministyczny | O(√n) | Małe liczby |
| Test Fermata | Probabilistyczne | O(k log² n) | Szybki pokaz |
| Miller-Rabin | Probabilistyczny | O(k log² n) | Cel ogólny |
| AK | Deterministyczny | O(log⁶ n) | Znaczenie teoretyczne |
**Test pierwszości Fermata:** Jeśli p jest liczbą pierwszą i gcd(a, p) = 1, to aᵖ⁻¹ ≡ 1 (mod p). Jeśli to się nie powiedzie dla jakiegoś a, to p jest zdecydowanie złożone. Jeśli przechodzi przez wiele losowych wartości a, p jest prawdopodobnie liczbą pierwszą.
**Uwaga:** Liczby Carmichaela (np. 561) przechodzą test Fermata dla wszystkich zasad względnie pierwszych, ale są złożone. Miller-Rabin unika tej kwestii.
---

## Arytmetyka modułowa
Arytmetyka modułowa bada liczby całkowite w ramach „zawijania” - arytmetyka na tarczy zegara.
### Relacje kongruencji
a ≡ b (mod n) oznacza n | (a - b), tj. aib pozostawiają tę samą resztę przy dzieleniu przez n.
### Właściwości arytmetyczne
| Operacja | Zasada |
|----------|------|
| Dodatek | (a + b) mod n = ((a mod n) + (b mod n)) mod n |
| Mnożenie | (a × b) mod n = ((a mod n) × (b mod n)) mod n |
| Potęgowanie | aᵇ mod n można efektywnie obliczyć poprzez wielokrotne podniesienie do kwadratu |
| Negacja | (-a) mod n = n - (a mod n) |
### Potęgowanie modułowe
Efektywne obliczanie aᵇ mod n przy użyciu **powtarzanego kwadratury**:
**Przykład praktyczny:** 3¹³ mod 7
- 13 w formacie binarnym: 1101
- 3¹ = 3 mod 7 = 3
- 3² = 9 mod 7 = 2
- 3⁴ = 4 mod 7 = 4
- 3⁸ = 16 mod 7 = 2
- 3¹³ = 3⁸ × 3⁴ × 3¹ = 2 × 4 × 3 = 24 mod 7 = 3
| Nieruchomość | Wartość |
|---------|-------|
| Złożoność czasowa | O(log b · log² n) |
| Złożoność przestrzeni | O(1) |
### Funkcja Totientu Eulera
φ(n) liczy liczby całkowite od 1 do n, które są względnie pierwsze do n.
| n | φ(n) | Liczby całkowite względnie pierwsze |
|---|------|----------------------|
| 1 | 1 | {1} |
| 2 | 1 | {1} |
| 6 | 2 | {1, 5} |
| 7 | 6 | {1, 2, 3, 4, 5, 6} (7 jest liczbą pierwszą) |
| 10 | 4 | {1, 3, 7, 9} |
| 12 | 4 | {1, 5, 7, 11} |
**Formuły:**
- Jeśli p jest liczbą pierwszą: φ(p) = p - 1
- Jeśli p jest liczbą pierwszą: φ(pᵏ) = pᵏ − pᵏ⁻¹ = pᵏ⁻¹(p − 1)
- Jeśli gcd(m, n) = 1: φ(mn) = φ(m) · φ(n) (multiplikatywność)
- Ogólne: φ(n) = n · Π_{p|n} (1 − 1/p) gdzie iloczyn jest po różnych czynnikach pierwszych n
---

## Kluczowe twierdzenia
### Małe twierdzenie Fermata
Jeśli p jest liczbą pierwszą i gcd(a, p) = 1, to:
aᵖ⁻¹ ≡ 1 (mod p)
**Wniosek (dla wszystkich a):** aᵖ ≡ a (mod p)
**Zastosowanie:** Szybka odwrotność modułowa, gdy moduł jest liczbą pierwszą: a⁻¹ ≡ aᵖ⁻² (mod p)
**Przykład praktyczny:** Znajdź 3⁻¹ mod 7.
- Według Fermata: 3⁻¹ ≡ 3⁵ (mod 7)
- 3² = 9 ≡ 2 (mod 7)
- 3⁴ = 4 (mod 7)
- 3⁵ = 3⁴ × 3 = 4 × 3 = 12 ≡ 5 (mod 7)
- Sprawdź: 3 × 5 = 15 ≡ 1 (mod 7).
### Twierdzenie Eulera (uogólnienie Fermata)
Jeśli gcd(a, n) = 1, to:
a^φ(n) ≡ 1 (mod n)
To uogólnia Małe Twierdzenie Fermata z liczb pierwszych na dowolny moduł.
### Chińskie twierdzenie o resztach (CRT)
Jeśli m₁, m₂, ..., mₖ są parami względnie pierwsze, to układ:
x ≡ a₁ (mod m₁)
x ≡ a₂ (mod m₂)
...
x ≡ aₖ (mod mₖ)
ma unikalne rozwiązanie modulo M = m₁ · m₂ · ... · mₖ.
**Przykład praktyczny:** Rozwiąż x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7).
- M = 3 × 5 × 7 = 105
- M₁ = 105/3 = 35; M₂ = 105/5 = 21; M₃ = 105/7 = 15
- Znajdź odwrotności: 35y₁ ≡ 1 (mod 3) → 2y₁ ≡ 1 → y₁ = 2
  21y₂ ≡ 1 (mod 5) → y₂ ≡ 1 (mod 5) → y₂ = 1
  15y₃ ≡ 1 (mod 7) → y₃ ≡ 1 (mod 7) → y₃ = 1
- x = 2,35,2 + 3,21,1 + 2,15,1 = 140 + 63 + 30 = 233
- x ≡ 233 mod 105 = 23
- Sprawdź: 23 mod 3 = 2, 23 mod 5 = 3, 23 mod 7 = 2.
### Twierdzenie Wilsona
(p-1)! ≡ −1 (mod p) wtedy i tylko wtedy, gdy p jest liczbą pierwszą.
Głównie o znaczeniu teoretycznym — niepraktyczny w przypadku testowania pierwszości, ponieważ obliczanie silni jest drogie.
### Reszty kwadratowe
Liczba całkowita a jest **reszta kwadratowa mod n** jeśli x² ≡ a (mod n) ma rozwiązanie.
**Kryterium Eulera:** a jest resztą kwadratową mod prime p iff a^((p−1)/2) ≡ 1 (mod p).
**Symbol legendy:** (a/p) = a^((p−1)/2) mod p, dający +1, −1 lub 0.
**Wzajemność kwadratowa** (Gauss): Dla różnych nieparzystych liczb pierwszych p, q:
(p/q)(q/p) = (−1)^((p−1)/2 · (q−1)/2)
To głębokie twierdzenie łączy reszty kwadratowe na różnych liczbach pierwszych i ma osiem dodatkowych praw regulujących przypadki p = 2.
---

## Zastosowania w kryptografii
### Kryptosystem RSA
Najszerzej stosowany kryptosystem klucza publicznego, oparty na trudności rozkładania na czynniki dużych liczb całkowitych.
**Konfiguracja:**
1. Wybierz dwie duże liczby pierwsze p, q (zwykle ponad 1024 bity każda)
2. Oblicz n = pq i φ(n) = (p−1)(q−1)
3. Wybierz e takie, że 1 < e < φ(n) i gcd(e, φ(n)) = 1 (wspólne: e = 65537)
4. Oblicz d ≡ e⁻¹ (mod φ(n)) korzystając z rozszerzonego algorytmu euklidesowego
5. **Klucz publiczny:** (n, e). **Klucz prywatny:** (n, d)
**Szyfrowanie:** c = mᵉ mod n (gdzie m to wiadomość w postaci zwykłego tekstu)
**Deszyfrowanie:** m = cᵈ mod n
**Dlaczego to działa:** cᵈ = m^(ed) ≡ m (mod n) według twierdzenia Eulera, ponieważ ed ≡ 1 (mod φ(n)).
**Bezpieczeństwo:** Rozłożenie n na p i q jest niewykonalne obliczeniowo w przypadku dużych n (ponad 2048 bitów). Bez p i q atakujący nie może obliczyć φ(n), a zatem nie może znaleźć d.
### Wymiana kluczy Diffiego-Hellmana
Umożliwia dwóm stronom ustalenie wspólnego sekretu za pośrednictwem niezabezpieczonego kanału.
**Ustawienie:** Zgadzam się na dużą liczbę pierwszą p i generator g (mod p).
**Protokół:**
1. Alicja wybiera sekret a, wysyła Bobowi A = gᵃ mod p
2. Bob wybiera sekret b, wysyła B = gᵇ mod p do Alicji
3. Alicja oblicza s = Bᵃ mod p = gᵃᵇ mod p
4. Bob oblicza s = Aᵇ mod p = gᵃᵇ mod p
5. Obydwa mają wspólny sekret s = gᵃᵇ mod p
**Bezpieczeństwo:** W oparciu o trudność **problemu logarytmu dyskretnego** — znajdowanie a z gᵃ mod p.
### Funkcje skrótu i ​​teoria liczb
Dobre funkcje skrótu wykorzystują arytmetykę modułową do równomiernego rozprowadzania kluczy:
- **Multiplikatywne hashowanie:** h(k) = (k · A) mod m, gdzie A ≈ m · (√5 − 1) / 2 (złoty podział)
- **Uniwersalne hashowanie:** h(k) = ((ak + b) mod p) mod m, gdzie p jest liczbą pierwszą, a, b są losowe
---

## Znaczenie dla uczenia maszynowego i nauki o danych
| Koncepcja teorii liczb | Aplikacja |
|----------------------|------------|
| Arytmetyka modułowa | Haszowanie (tabele skrótów, mapy skrótów), generowanie liczb losowych |
| Liczby pierwsze | Rozmiar tabeli mieszającej (użyj głównych rozmiarów tabeli, aby zmniejszyć kolizje) |
| GCD / Algorytm Euklidesa | Racjonalna arytmetyka, upraszczanie ułamków prawdopodobnych |
| Potęgowanie modułowe | Bezpieczeństwo kryptograficzne dla modelu ML obsługującego HTTPS |
| Totian Eulera | Generowanie klucza RSA, zrozumienie gwarancji kryptograficznych |
| Chińskie twierdzenie o resztach | Obliczenia rozproszone, równoległa arytmetyka modułowa |
| Testowanie pierwszości | Generowanie liczb pierwszych do operacji kryptograficznych |
| Pozostałości kwadratowe | Problem resztowości kwadratowej w zaawansowanej kryptografii |
| Pola skończone (GF(p), GF(2ᵏ)) | Kody korygujące błędy, kody Reeda-Solomona, szyfrowanie AES |
---

## Streszczenie
| Temat | Podstawowy pomysł | Kluczowy wynik |
|-------|-----------|------------|
| Podzielność | Dzielenie z resztą | Algorytm dzielenia: a = bq + r |
| NWD | Największy wspólny czynnik | Algorytm euklidesowy: O(log n) |
| liczby pierwsze | Atomy liczb całkowitych | Podstawowe twierdzenie arytmetyki (unikalna faktoryzacja) |
| Arytmetyka modułowa | Arytmetyka ogólna | Klasy kongruencji, potęgowanie modułowe |
| Totient Eulera | Liczenie liczb całkowitych względnie pierwszych | φ(n) = n · Π(1 – 1/p) |
| Małe Twierdzenie Fermata | Skrót modułu pierwszego | aᵖ⁻¹ ≡ 1 (mod p) |
| Twierdzenie Eulera | Uogólniony Fermat | a^φ(n) ≡ 1 (mod n) |
| Chińskie twierdzenie o resztach | Łączenie systemów modułowych | Unikalne rozwiązanie mod produktu o równych modułach |
| Kryptografia | Trudne problemy teorii liczb | RSA (faktoring), Diffie-Hellman (log dyskretny) |
Teoria liczb przekształca proste pytania dotyczące liczb całkowitych w głęboką matematykę o głębokich zastosowaniach praktycznych. Każde bezpieczne połączenie internetowe, zaszyfrowana wiadomość i podpis cyfrowy opierają się na wynikach teorii liczb odkrytych na wieki przed pojawieniem się komputerów. Analitykom zajmującym się danymi i inżynierom uczenia maszynowego zrozumienie teorii liczb zapewnia wgląd w haszowanie, generowanie liczb losowych i infrastrukturę kryptograficzną, która chroni dane podczas przesyłania i przechowywania.