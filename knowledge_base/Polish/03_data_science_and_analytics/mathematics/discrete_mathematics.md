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
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-10"
    author: "AI Model Training Team"
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

# Matematyka dyskretna
Matematyka dyskretna to badanie struktur matematycznych, które są zasadniczo policzalne lub oddzielone — w przeciwieństwie do matematyki ciągłej (rachunek różniczkowy, analiza rzeczywista), która zajmuje się gładkimi, nieprzerwanymi wielkościami. Matematyka dyskretna stanowi podstawę informatyki, kryptografii, projektowania algorytmów i struktur danych. Jeśli matematyka ciągła opisuje świat fizyczny, matematyka dyskretna opisuje świat obliczeniowy.
---

## Teoria mnogości w głębi
Zbiory stanowią podstawę, na której zbudowana jest prawie cała współczesna matematyka. **Zbiór** to nieuporządkowany zbiór odrębnych obiektów, zwanych **elementami** lub **elementami**.
### Podstawy aksjomatyczne (ZFC)
Współczesna teoria mnogości opiera się na **aksjomatach Zermelo-Fraenkla z aksjomatem wyboru (ZFC)**. Te aksjomaty rozwiązują paradoksy, takie jak Paradoks Russella („zbiór wszystkich zbiorów, które nie zawierają siebie”), ograniczając sposób tworzenia zbiorów.
| Aksjomat | Nieformalne oświadczenie |
|-------|--------------------------------------|
| Rozszerzalność | Dwa zbiory są równe, jeśli mają te same elementy |
| Pusty zestaw | Istnieje zbiór bez elementów: ∅ |
| Parowanie | Dla dowolnego a, b istnieje {a, b} |
| Unia | Dla dowolnej rodziny zbiorów istnieje ich związek |
| Zestaw mocy | Dla dowolnego zbioru S istnieje zbiór wszystkich podzbiorów S: P(S) |
| Nieskończoność | Istnieje nieskończony zbiór |
| Specyfikacja | Dla dowolnego zbioru A i własności P istnieje {x ∈ A : P(x)} |
| Zastąpienie | Obraz zbioru pod definiowalną funkcją jest zbiorem |
| Regularność | Każdy niepusty zbiór zawiera element od niego rozłączny (zapobiega samoprzynależności) |
| Wybór | Dla dowolnej rodziny niepustych zbiorów rozłącznych parami istnieje funkcja wyboru |
### Liczność i wielkość zbiorów
**Liczność** zbioru, oznaczona |S|, mierzy jego „rozmiar”.
| Koncepcja | Definicja | Przykład |
|--------|------------|--------|
| Skończony zbiór | Ma liczbę naturalną jako liczność | |{a, b, c}| = 3 |
| Policzalnie nieskończony | Taka sama liczność jak ℕ | ℤ, ℚ są przeliczalnie nieskończone |
| Niepoliczalne | Większy niż ℕ | ℝ, P(ℕ), zbiór wszystkich funkcji ℕ → {0,1} |
| Twierdzenie Cantora | Dla dowolnego zbioru S, |P(S)| > |S| | |P(ℕ)| > |ℕ| |
**Argument diagonalny Cantora** dowodzi, że ℝ jest niepoliczalne: załóżmy, że możesz wypisać wszystkie liczby rzeczywiste w [0,1], a następnie skonstruuj nową liczbę rzeczywistą, która różni się od n-tej wymienionej liczby rzeczywistej na n-tym miejscu po przecinku – sprzeczność.
### Operacje na zbiorach
| Operacja | Notacja | Definicja | Nieruchomość |
|---------------|----------|------------|--------------|
| Unia | A ∪ B | {x : x ∈ A lub x ∈ B} | Przemienne, łączne |
| Przecięcie | A ∩ B | {x : x ∈ A i x ∈ B} | Przemienne, łączne |
| Różnica | A \ B | {x: x ∈ A i x ∉ B} | Nie przemienne |
| Różnica symetryczna | A △ B | (A \ B) ∪ (B \ A) | Przemienne, łączne |
| Uzupełnij | Aᶜ | U \ A (gdzie U jest zbiorem uniwersalnym) | (Aᶜ)ᶜ = A |
| Produkt kartezjański | A × B | {(a,b) : a ∈ A, b ∈ B} | |A × B| = |A| · |B| |
**Prawa De Morgana:**
- (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ
- (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ
**Zasada włączenia-wyłączenia** (dla zbiorów skończonych):
|A₁ ∪ A₂ ∪ ... ∪ Aₙ| = Σ|Aᵢ| − Σ|Aᵢ ∩ Aⱼ| + Σ|Aᵢ ∩ Aⱼ ∩ Aₖ| − ... + (−1)ⁿ⁺¹|A₁ ∩ ... ∩ Aₙ|
---

## Relacje
A **relacja** R na zbiorach A i B jest podzbiorem A × B. Gdy (a, b) ∈ R, piszemy aRb.
### Rodzaje relacji
Relacja R na zbiorze A może mieć następujące właściwości:
| Nieruchomość | Definicja | Przykład |
|---------|------------|--------|
| Refleksyjny | ∀a ∈ A: aRa | ≤ na ℤ |
| Bezrefleksyjny | ∀a ∈ ZA: ¬(aRa) | < na ℤ |
| Symetryczny | ∀a,b: aRb → bRa | = na dowolnym zestawie |
| Antysymetryczny | ∀a,b: aRb ∧ bRa → a = b | ≤ na ℤ |
| Przechodnie | ∀a,b,c: aRb ∧ bRc → aRc | <, ≤, = na ℤ |
### Relacje równoważności
**Relacja równoważności** jest zwrotna, symetryczna i przechodnia. Dzieli zbiór na rozłączne **klasy równoważności**.
**Przykład:** arytmetyka modułowa. Zdefiniuj a ~ b jeśli a ≡ b (mod n). Klasy równoważności to [0], [1], ..., [n-1], które dzielą ℤ na n klas.
**Przykład praktyczny:** Na ℤ × ℤ zdefiniuj (a, b) ~ (c, d) iff a + d = b + c. Jest to relacja równoważności. Klasa [(0,0)] = {(n,n) : n ∈ ℤ}. Klasa [(1,0)] = {(n+1,n) : n ∈ ℤ}. Ta konstrukcja faktycznie definiuje liczby całkowite na podstawie liczb naturalnych.
### Częściowe zamówienia
**Porządek częściowy** jest zwrotny, antysymetryczny i przechodni. Zbiór o częściowym porządku nazywany jest **zbiorem częściowo uporządkowanym (poset)**.
| Koncepcja | Definicja | Przykład |
|--------|------------|--------|
| Postaw | (S, ≤) z ≤ porządkiem częściowym | (P(A), ⊆) — podzbiory uporządkowane według włączenia |
| Łańcuch | Całkowicie uporządkowany podzbiór | {∅, {a}, {a,b}} w P({a,b,c}) |
| Antyłańcuch | Podzbiór, w którym żadne dwa elementy nie są porównywalne | {{a}, {b}} w P({a,b}) |
| Diagram Hassego | Wizualna reprezentacja pozy | Rysuj krawędzie tylko w celu zakrycia relacji |
| Górna granica | Element ≥ każdy element w podzbiorze | sup({2,3}) = 6 cali (ℤ, \|) (podzielność) |
| Najmniejsza górna granica (nad) | Najmniejsza górna granica | sup({2,3}) w (ℕ, ≤) wynosi 3 |
| Największa dolna granica (inf) | Największa dolna granica | inf({4,6}) w (ℕ, \|) wynosi 2 |
---

## Funkcje
A **funkcja** f: A → B przypisuje każdemu elementowi A dokładnie jeden element B.
### Klasyfikacja funkcji
| Wpisz | Definicja | Przykład |
|------|------------|--------|
| Injekcyjny (jeden do jednego) | f(a) = f(b) → a = b | f(x) = 2x od ℤ → ℤ |
| Suriektywny (na) | ∀b ∈ B, ∃a ∈ ZA: f(a) = b | f(x) = x mod 2 z ℤ → {0,1} |
| Bijektywny | Zarówno injektywny, jak i surjektywny | f(x) = x + 1 z ℤ → ℤ |
### Ważne pojęcia dotyczące funkcji
| Koncepcja | Definicja | Przypadek użycia |
|--------|------------|---------|
| Funkcja odwrotna | f⁻¹ istnieje, jeśli f jest bijektywne | Odszyfrowywanie zaszyfrowanych danych |
| Skład | (g ∘ f)(x) = g(f(x)) | Łańcuchowe transformacje |
| Funkcja tożsamości | identyfikator(x) = x | Neutralny element kompozycji |
| Punkt stały | f(x) = x | Definicje rekurencyjne, semantyka |
| Permutacja | Bijekcja zbioru do siebie | Zmiana kolejności danych, tasowanie |
### Funkcje zliczania
Dane zbiory skończone |A| = m i |B| = n:
| Wpisz | Hrabia |
|------|-------|
| Wszystkie funkcje A → B | nie |
| Funkcje iniekcyjne | N! / (n-m)! (jeśli n ≥ m, w przeciwnym razie 0) |
| Funkcje surjektywne | Σₖ₌₀ⁿ (−1)ᵏ · C(n,k) · (n−k)ᵐ (przez włączenie-wyłączenie) |
| Funkcje bijektywne | N! (kiedy m = n) |
---

## Kombinatoryka
Kombinatoryka to matematyka polegająca na liczeniu, organizowaniu i wybieraniu.
### Podstawowe zasady liczenia
| Zasada | Oświadczenie | Przykład |
|----------|-----------|---------|
| Reguła sumy | Jeśli A i B są rozłączne, |A ∪ B| = |A| + |B| | Wybór owocu: 3 jabłka + 4 pomarańcze = 7 opcji |
| Zasada produktu | |A × B| = |A| · |B| | Strój: 3 koszule × 4 spodnie = 12 strojów |
| Reguła bijekcji | Jeżeli f: A → B jest bijekcją, |A| = |B| | Policz podzbiory, zliczając ciągi binarne |
| Uzupełnij | |A| = |U| − |Aᶜ| | Policz „co najmniej jeden” jako całość minus „brak” |
### Permutacje i kombinacje
| Notacja | Imię | Formuła | Znaczenie |
|---------|------|---------|---------|
| C(n, k) lub (n k) | Współczynnik dwumianowy | N! / (k!(n−k)!) | Sposoby wyboru k elementów z n (kolejność nie ma znaczenia) |
| P(n, k) | k-permutacje n | N! / (n-k)! | Sposoby ułożenia k elementów z n (sprawa porządku) |
| N! | Silnia | n × (n−1) × ... × 1 | Sposoby ułożenia wszystkich n elementów |
| (n k) z powtórzeniem | Wielokrotnego wyboru | C(n+k−1, k) | Wybierz k z n z możliwością powtórzenia |
**Twierdzenie o dwumianie:**
(x + y)ⁿ = Σₖ₌₀ⁿ C(n,k) · xᵏ · yⁿ⁻ᵏ
**Tożsamość Pascala:** C(n,k) = C(n−1,k−1) + C(n−1,k)
### Zasada szufladkowania
**Forma podstawowa:** Jeśli w n pudełkach umieści się n+1 obiektów, to w co najmniej jednym pudełku znajdą się ≥ 2 obiekty.
**Forma ogólna:** Jeśli N obiektów zostanie umieszczonych w k pudełkach, co najmniej jedno pudełko zawiera ≥ ⌈N/k⌉ obiektów.
**Praktyczne przykłady:**
1. Spośród dowolnych 13 osób co najmniej 2 mają wspólny miesiąc urodzenia. (13 osób, 12 miesięcy → szufladka.)
2. Pokaż, że wśród dowolnych 5 liczb całkowitych istnieją 3, których suma jest podzielna przez 3.
   - Rozważ pozostałości mod 3: {0, 1, 2}. Przy 5 liczbach całkowitych i 3 klasach reszt, według uogólnionej szufladki, co najmniej ⌈5/3⌉ = 2 mają wspólną resztę.
   - Jeśli 3 mają wspólną resztę r: ich suma ≡ 3r ≡ 0 (mod 3).
   - Jeśli 2 mają wspólną resztę 0 i 2 mają wspólną resztę 1: wybierz po jednym z każdej pary plus element reszty 0 → suma ≡ 0 (mod 3).
3. **Zastosowanie w CS:** Każdy algorytm kompresji bezstratnej musi rozszerzać niektóre wejścia. (Gdyby każdy n-bitowy ciąg skompresowany do < n bitów, odwzorowywałbyś 2ⁿ ciągi na mniej niż 2ⁿ skompresowane ciągi — naruszając tym samym iniekcyjność.)
### Liczby katalońskie
N-ta **liczba katalońska** Cₙ = C(2n, n) / (n+1) liczy:
| Struktura | Przykład |
|---------------|--------|
| Prawidłowe sekwencje nawiasów | ()(), (()) dla n = 2 |
| Drzewa binarne z n węzłami wewnętrznymi | 2 drzewa dla n = 2 |
| Ścieżki nie przecinające przekątnej | Ścieżki siatki od (0,0) do (n,n) pozostające poniżej y = x |
| Triangulacje wielokąta | Sposoby dzielenia (n+2)-gotu na trójkąty |
Kilka pierwszych: C₀ = 1, C₁ = 1, C₂ = 2, C₃ = 5, C₄ = 14, C₅ = 42.
Powtarzanie: Cₙ₊₁ = Σᵢ₌₀ⁿ Cᵢ · Cₙ₋ᵢ
---

## Relacje nawrotów
**Relacja powtarzania** definiuje każdy wyraz sekwencji jako funkcję poprzedzających wyrazów.
### Typy i rozwiązania
| Wpisz | Formularz | Metoda rozwiązania |
|------|------|--------------------------------|
| Liniowy jednorodny (stały współczynnik) | aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ | Równanie charakterystyczne |
| Liniowy niejednorodny | aₙ = c₁aₙ₋₁ + ... + f(n) | Szczególny roztwór + roztwór jednorodny |
| Dziel i rządź | T(n) = aT(n/b) + f(n) | Główne twierdzenie |
### Metoda równań charakterystycznych
Dla aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ utwórz równanie charakterystyczne:
r² – c₁r – c₂ = 0
| Sprawa | Korzenie | Rozwiązanie ogólne |
|------|-------|----------------------|
| Dwa różne pierwiastki rzeczywiste r₁, r₂ | r₁ ≠ r₂ | aₙ = A·r₁ⁿ + B·r₂ⁿ |
| Powtórzony pierwiastek r | r₁ = r₂ = r | aₙ = (A + Bn)·rⁿ |
| Złożone pierwiastki α ± βi | Zamień na biegunowy: r·e^(±iθ) | aₙ = rⁿ(A cos(nθ) + B sin(nθ)) |
**Przykład praktyczny:** ciąg Fibonacciego Fₙ = Fₙ₋₁ + Fₙ₋₂, F₀ = 0, F₁ = 1.
- Równanie charakterystyczne: r² - r - 1 = 0
- Pierwiastki: r = (1 ± √5) / 2 → φ = (1+√5)/2 ≈ 1,618, ψ = (1−√5)/2 ≈ −0,618
- Rozwiązanie ogólne: Fₙ = A·φⁿ + B·ψⁿ
- Z warunków początkowych: A = 1/√5, B = −1/√5
- **Forma zamknięta:** Fₙ = (φⁿ − ψⁿ) / √5 (wzór Bineta)
### Główne twierdzenie
Dla nawrotów postaci T(n) = aT(n/b) + f(n) gdzie a ≥ 1, b > 1:
Niech c = log_b(a).
| Sprawa | Stan | Rozwiązanie |
|------|-----------|---------|
| 1 | f(n) = O(nᵈ) gdzie d< c | T(n) = Θ(nᶜ) |
| 2 | f(n) = Θ(nᶜ) | T(n) = Θ(nᶜ log n) |
| 3 | f(n) = Θ(nᵈ) where d >c i af(n/b) ≤ kf(n) dla pewnego k < 1 | T(n) = Θ(nᵈ) |
**Przykłady:**
- Sortowanie przez scalanie: T(n) = 2T(n/2) + O(n). Tutaj a=2, b=2, c=1, f(n)=n=Θ(n¹). Przypadek 2: T(n) = Θ(n log n).
- Wyszukiwanie binarne: T(n) = T(n/2) + O(1). Tutaj a=1, b=2, c=0, f(n)=1=Θ(n⁰). Przypadek 2: T(n) = Θ(log n).
---

## Generowanie funkcji
**Funkcja generująca** koduje ciąg (aₙ) jako współczynniki formalnego szeregu potęgowego.
### Typy
| Wpisz | Formularz | Przypadek użycia |
|------|------|--------------|
| Zwykły (OGF) | G(x) = Σₙ₌₀^∞ aₙxⁿ | Nieoznakowane struktury, kompozycje |
| Wykładniczy (EGF) | E(x) = Σₙ₌₀^∞ aₙxⁿ/n! | Struktury oznaczone, permutacje |
### Wspólne funkcje generujące
| Sekwencja aₙ | OGF G(x) |
|------------|---------------|
| 1, 1, 1, 1, ... | 1/(1-x) |
| 1, 2, 3, 4, ... | 1/(1-x)² |
| 1, r, r², r³, ... | 1/(1−rx) |
| C(n,k) dla ustalonego k | xᵏ/(1−x)ᵏ⁺¹ |
| Fibonacciego Fₙ | x/(1−x−x²) |
| kataloński Cₙ | (1 − √(1−4x)) / (2x) |
### Używanie funkcji generujących do rozwiązywania powtórzeń
**Przykład praktyczny:** Rozwiąż aₙ = 3aₙ₋₁ − 2aₙ₋₂, a₀ = 1, a₁ = 3.
1. Niech G(x) = Σ aₙxⁿ.
2. Z powtarzalności: G(x) − a₀ − a₁x = 3x(G(x) − a₀) − 2x²G(x)
3. Zastąp: G(x) − 1 − 3x = 3x(G(x) − 1) − 2x²G(x)
4. G(x)(1 − 3x + 2x²) = 1
5. G(x) = 1 / (1 − 3x + 2x²) = 1 / ((1−x)(1−2x))
6. Ułamki cząstkowe: G(x) = 2/(1−2x) − 1/(1−x)
7. Wyodrębnij współczynniki: aₙ = 2·2ⁿ − 1 = 2ⁿ⁺¹ − 1
**Weryfikacja:** a₀ = 2−1 = 1, a₁ = 4−1 = 3, a₂ = 8−1 = 7. Sprawdź: 3(3) − 2(1) = 7.
---

## Algebra Boole'a i logika zdań
Algebra Boole'a jest algebrą dwóch wartości logicznych: **True (1)** i **False (0)**. Jest to matematyczna podstawa obwodów cyfrowych, zapytań do baz danych i programowania warunkowego.
### Operacje i prawa
| Operacja | Symbol | Znaczenie | Tabela Prawdy |
|----------|--------|---------|------------|
| ORAZ | p ∧ q | Prawdziwe tylko wtedy, gdy oba są prawdziwe | T∧T=T, T∧F=F, F∧T=F, F∧F=F |
| LUB | p ∨ q | Prawda, gdy przynajmniej jedno jest prawdą | T∨T=T, T∨F=T, F∨T=T, F∨F=F |
| NIE | ¬p | Negacja | ¬T=F, ¬F=T |
| XOR | p ⊕ q | Prawda, gdy dokładnie jedno jest prawdą | T⊕T=F, T⊕F=T, F⊕T=T, F⊕F=F |
| implikuje | p → q | Fałsz tylko wtedy, gdy p=T i q=F | T → T = T, T → F = F, F → T = T, F → F = T |
| DWUWARUNKOWE | p ↔ q | Prawda, gdy oba mają tę samą wartość | T↔T=T, T↔F=F, F↔T=F, F↔F=T |
### Kluczowe tożsamości logiczne
| Prawo | Formuła |
|-----|--------|
| Przemienność | p ∧ q = q ∧ p; p ∨ q = q ∨ p |
| Łączność | (p ∧ q) ∧ r = p ∧ (q ∧ r) |
| Dystrybutywność | p ∧ (q ∨ r) = (p ∧ q) ∨ (p ∧ r) |
| Prawa De Morgana | ¬(p ∧ q) = ¬p ∨ ¬q; ¬(p ∨ q) = ¬p ∧ ¬q |
| Podwójna negacja | ¬(¬p) = p |
| Idempotencja | p ∧ p = p; p ∨ p = p |
| Absorpcja | p ∨ (p ∧ q) = p; p ∧ (p ∨ q) = p |
| Kontrapozytywny | (p → q) ≡ (¬q → ¬p) |
### Normalne formularze
| Formularz | Struktura | Przypadek użycia |
|------|-----------|---------|
| Łączna postać normalna (CNF) | ORAZ OR: (A∨B) ∧ (C∨D) | Solvery SAT, dowodzenie twierdzenia o rozdzielczości |
| Rozłączna postać normalna (DNF) | LUB AND: (A∧B) ∨ (C∧D) | Projektowanie obwodów, systemy oparte na regułach |
**Konwersja do CNF:** Zastosuj prawa De Morgana, rozłóż OR na AND, wyeliminuj podwójne negacje.
---

## Arytmetyka modułowa i kongruencje
Arytmetyka modułowa bada liczby całkowite w oparciu o działanie „reszty po dzieleniu”. Jest niezbędny w kryptografii, mieszaniu i teorii liczb.
### Podstawowe definicje
| Koncepcja | Notacja | Definicja |
|--------|----------|------------|
| Zgodność | a ≡ b (mod n) | n dzieli (a - b) |
| Klasa pozostałości | [a]ₙ | Zbiór {a + kn: k ∈ ℤ} |
| Odwrotność modułowa | a⁻¹ mod n | Wartość x taka, że ​​ax ≡ 1 (mod n) |
| Totian Eulera | φ(n) | Liczba liczb całkowitych w {1,...,n} względnie pierwszej do n |
### Właściwości klucza
| Nieruchomość | Oświadczenie |
|---------|----------|
| Dodatek | Jeśli a ≡ b i c ≡ d (mod n), to a+c ≡ b+d (mod n) |
| Mnożenie | Jeśli a ≡ b i c ≡ d (mod n), to ac ≡ bd (mod n) |
| Małe Twierdzenie Fermata | Jeśli p jest liczbą pierwszą i gcd(a,p) = 1, to aᵖ⁻¹ ≡ 1 (mod p) |
| Twierdzenie Eulera | Jeśli gcd(a,n) = 1, to a^φ(n) ≡ 1 (mod n) |
| Chińskie twierdzenie o resztach | Jeżeli gcd(m,n) = 1, to układ x ≡ a (mod m), x ≡ b (mod n) ma jednoznaczne rozwiązanie mod mn |
### Obliczanie współczynnika Eulera
Dla n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ (rozkład na czynniki pierwsze):
φ(n) = n · (1 – 1/p₁) · (1 – 1/p₂) · ... · (1 – 1/pₖ)
**Przykład:** φ(12) = 12 · (1 − 1/2) · (1 − 1/3) = 12 · 1/2 · 2/3 = 4. Rzeczywiście, {1, 5, 7, 11} są względnie pierwsze do 12.
### Zastosowanie: Kryptografia RSA (przegląd)
1. Wybierz duże liczby pierwsze p, q. Oblicz n = pq, φ(n) = (p−1)(q−1).
2. Wybierz e takie, że gcd(e, φ(n)) = 1 (wykładnik publiczny).
3. Oblicz d ≡ e⁻¹ (mod φ(n)) (wykładnik prywatny).
4. Szyfruj: c = mᵉ mod n. Odszyfruj: m = cᵈ mod n.
5. Bezpieczeństwo opiera się na trudności rozkładu n na czynniki w celu znalezienia p i q.
---

## Indukcja matematyczna
**Indukcja matematyczna** jest podstawową techniką dowodową twierdzeń dotyczących wszystkich liczb naturalnych.
### Struktura dowodu przez indukcję
1. **Przypadek podstawowy:** Udowodnij twierdzenie dla n = 0 (lub n = 1).
2. **Krok indukcyjny:** Załóżmy, że twierdzenie zachodzi dla n = k (hipoteza indukcyjna), a następnie udowodnij je dla n = k + 1.
### Warianty
| Wariant | Kiedy stosować |
|--------|------------|
| Prosta indukcja | Udowodnić P(k) → P(k+1) |
| Silna indukcja | Załóżmy, że P(0), P(1), ..., P(k) aby udowodnić P(k+1) |
| Indukcja strukturalna | Udowodnić właściwości rekurencyjnie zdefiniowanych struktur (drzewa, formuły) |
| Indukcja pozaskończona | Rozszerz indukcję na zbiory dobrze uporządkowane poza ℕ |
**Przykład praktyczny (silna indukcja):** Udowodnij, że każdą liczbę całkowitą n ≥ 2 można zapisać jako iloczyn liczb pierwszych.
- Podstawa: n = 2 jest liczbą pierwszą, więc jest iloczynem liczb pierwszych (samej).
- Krok indukcyjny: Załóżmy, że jest prawdziwy dla wszystkich liczb całkowitych od 2 do k. Rozważ k+1.
  - Jeśli k+1 jest liczbą pierwszą, gotowe.
  - Jeśli k+1 jest złożone, k+1 = ab gdzie 2 ≤ a, b ≤ k. Zgodnie z hipotezą indukcyjną zarówno a, jak i b są iloczynami liczb pierwszych, zatem k+1 jest iloczynem liczb pierwszych.
---

## Znaczenie dla uczenia maszynowego i nauki o danych
| Koncepcja matematyki dyskretnej | Zastosowanie w ML / Data Science |
|----------------------|------------------------------------------------|
| Teoria mnogości | Operacje na bazach danych (złączenia SQL), manipulacja zestawami cech, zdarzenia prawdopodobieństwa |
| Relacje | Schematy baz danych, modelowanie relacji encja, grafy wiedzy |
| Funkcje | Funkcje aktywacji, transformacje cech, odwzorowania pomiędzy przestrzeniami |
| Kombinatoryka | Wybór funkcji (wybór k z n), rozmiar wyszukiwania siatki hiperparametrów |
| Zasada przegródki | Kolizje haszujące, dolne granice kompresji, dowody teorii informacji |
| Relacje powtarzalności | Programowanie dynamiczne, analiza złożoności algorytmów, modele szeregów czasowych |
| Generowanie funkcji | Funkcje generujące prawdopodobieństwo, rozwiązywanie problemów kombinatorycznych w inżynierii cech |
| Liczby katalońskie | Liczenie struktur drzewiastych (drzewa decyzyjne), parsowanie wyrażeń, operacje na stosach |
| Teoria grafów (patrz następny plik) | Analiza sieci społecznościowych, systemy rekomendacji, reprezentacja wiedzy |
---

## Streszczenie
| Temat | Podstawowy pomysł | Kluczowe narzędzie |
|-------|-----------|---------|
| Teoria mnogości | Kolekcje różnych obiektów | Aksjomaty ZFC, liczność, operacje |
| Relacje | Połączenia między elementami | Relacje równoważności, porządki cząstkowe |
| Funkcje | Odwzorowania pomiędzy zbiorami | Iniekcyjność, surjektywność, bijekcja |
| Kombinatoryka | Ustalenia dotyczące liczenia | Współczynniki dwumianowe, zasada szufladki |
| Relacje nawrotów | Sekwencje zdefiniowane rekurencyjnie | Równania charakterystyczne, twierdzenie główne |
| Generowanie funkcji | Ciągi jako szeregi potęgowe | OGF/EGF, algebraiczne rozwiązywanie nawrotów |
Matematyka dyskretna zapewnia język i narzędzia do wnioskowania o strukturach skończonych lub policzalnych — czyli dokładnie tym, czym manipulują komputery. Każdy algorytm, struktura danych, zapytanie do bazy danych i protokół kryptograficzny opierają się na dyskretnych podstawach. Opanowanie tych tematów wyostrza umiejętność rozwiązywania problemów i zapewnia słownictwo potrzebne do zaawansowanych badań w zakresie algorytmów, teorii złożoności i uczenia maszynowego.