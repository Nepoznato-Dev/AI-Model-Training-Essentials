---
# Metadata
title: "Logic and Critical Thinking"
description: "Formal logic, logical fallacies, argument analysis, and critical thinking frameworks"
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Split from mathematics_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [logic, critical-thinking, fallacies, arguments, reasoning, boolean-algebra]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "12 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Logika i krytyczne myślenie
Logika to nauka o prawidłowym rozumowaniu — o tym, jak konstruować rozsądne argumenty i identyfikować błędne. Krytyczne myślenie to zdyscyplinowany nawyk kwestionowania założeń, oceniania dowodów i uważnego rozumowania. Umiejętności te są niezbędne nie tylko w matematyce i informatyce, ale także w codziennym podejmowaniu decyzji, badaniach naukowych i poruszaniu się po świecie bogatym w informacje.
---

## Co to jest argument?
W logice **argument** to zbiór stwierdzeń (przesłanek) mających na celu poparcie wniosku.
| Składnik | Rola | Przykład |
|----------|------|--------|
| **Przesłanka** | Oświadczenie przedstawione jako dowód | „Wszyscy ludzie są śmiertelni” |
| **Wniosek** | Roszczenie o wsparcie lokalu | „Sokrates jest śmiertelny” |
| **Wniosek** | Logiczny krok od przesłanek do wniosków | „Sokrates jest zatem człowiekiem…” |
### Prawidłowe a dźwiękowe
| Termin | Znaczenie | Przykład |
|------|---------|--------|
| **Ważne** | Jeśli przesłanki są prawdziwe, wniosek musi być prawdziwy | Struktura jest poprawna, nawet jeśli przesłanki są fałszywe |
| **Nieprawidłowe** | Wniosek nie wynika z przesłanek | Struktura logiczna jest zepsuta |
| **Dźwięk** | Ważne ORAZ wszystkie przesłanki są rzeczywiście prawdziwe | Złoty standard argumentacji |
| **Niezdrowe** | Albo jest nieprawidłowy, albo ma fałszywe przesłanki | Najbardziej błędne argumenty |
---

## Rodzaje rozumowania
| Wpisz | Kierunek | siła | Przykład |
|------|-----------|----------|---------|
| **Dedukcyjne** | Ogólne → szczegółowe | Pewne (jeśli ważne) | „Wszystkie ssaki mają płuca. Wieloryb jest ssakiem. Dlatego wieloryb ma płuca”. |
| **Indukcyjny** | Konkretne → ogólne | Prawdopodobne | „Każdy łabędź, którego widziałem, jest biały. Dlatego prawdopodobnie wszystkie łabędzie są białe”. |
| **Uprowadzenie** | Obserwacja → najlepsze wyjaśnienie | Prawdopodobne | „Trawa jest mokra. Najlepszym wyjaśnieniem jest to, że padał deszcz”. |
---

## Logika zdań
Logika zdań zajmuje się prostymi zdaniami i sposobami ich łączenia:
### Łączniki logiczne
| Łączny | Symbol | Znaczenie | Warunek prawdy |
|----------|--------|---------|----------------|
| **I** | ∧ (p ∧ q) | koniunkcja | Prawdziwe tylko wtedy, gdy oba są prawdziwe |
| **LUB** | ∨ (p ∨ q) | Rozłączenie | Prawda, gdy przynajmniej jedno jest prawdą |
| **NIE** | ¬ (¬p) | Negacja | Przeciwna wartość prawdy |
| **JEŚLI...WTEDY** | → (p → q) | Implikacja | Fałsz tylko wtedy, gdy p jest prawdą, a q jest fałszem |
| **IF** | ↔ (p ↔ q) | Dwuwarunkowy | Prawda, gdy oba mają tę samą wartość logiczną |
### Tabela prawdy dla implikacji (p → q)
| p | q | p → q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |
Uwaga: Fałszywa przesłanka sprawia, że ​​implikacja jest bezsensownie prawdziwa. „Jeśli księżyc to ser, to ja jestem papieżem” jest logicznie prawdziwe.
---

## Algebra Boole’a
Algebra Boole'a to matematyka wartości prawda/fałsz i stanowi podstawę projektowania i programowania obwodów cyfrowych:
| Prawo | Wyrażenie | Znaczenie |
|---------|-----------|---------|
| **Przemienna** | ZA ∧ B = B ∧ ZA | Kolejność nie ma znaczenia |
| **Skojarzone** | (A ∧ B) ∧ do = ZA ∧ (B ∧ C) | Grupowanie nie ma znaczenia |
| **Rozdzielczość** | ZA ∧ (B ∨ do) = (A ∧ B) ∨ (A ∧ do) | AND rozdziela na OR |
| **De Morgana** | ¬(A ∧ B) = ¬A ∨ ¬B | Negacja zamienia AND na OR |
| **De Morgana** | ¬(A ∨ B) = ¬A ∧ ¬B | Negacja zamienia OR na AND |
| **Podwójna negacja** | ¬(¬A) = A | Dwie negacje anulują |
| **Tożsamość** | ZA ∧ T = ZA; ZA ∨ fa = ZA | Elementy tożsamości |
| **Uzupełnienie** | ZA ∧ ¬A = F; ZA ∨ ¬A = T | Sprzeczność i tautologia |
---

## Typowe błędy logiczne
Rozpoznawanie błędów jest niezbędne do krytycznego myślenia:
### Błędy formalne (błędy strukturalne)
| Błąd | Struktura | Przykład |
|--------|-----------|--------|
| **Potwierdzenie następstwa** | Jeśli P, to Q. Q. Zatem P. | „Jeśli pada deszcz, ziemia jest mokra. Ziemia jest mokra. Dlatego padał deszcz”. (Może to być zraszacz.) |
| **Zaprzeczanie poprzednikowi** | Jeśli P, to Q. Nie P. Zatem nie Q. | „Jeśli pada deszcz, ziemia jest mokra. Nie padało. Dlatego ziemia nie jest mokra”. |
### Nieformalne błędy (błędy w treści)
| Błąd | Opis | Przykład |
|--------|-------------|--------|
| **Ad Hominem** | Atakowanie osoby, a nie argumentu | „Nie można ufać jej planom gospodarczym – ona nie jest nawet ekonomistką”. |
| **Słomkowy Człowiek** | Fałszywe przedstawienie argumentu, aby ułatwić atak | „Chcecie zmniejszyć wydatki na wojsko? Więc chcecie pozostawić kraj bezbronny!” |
| **Apel do Władzy** | Powołanie się na autorytet, który nie jest ekspertem w danej dziedzinie | „Ta gwiazda twierdzi, że ta dieta działa, więc musi być skuteczna”. |
| **Fałszywy dylemat** | Przedstawiam tylko dwie opcje, gdy istnieje ich więcej | „Albo jesteś z nami, albo przeciwko nam”. |
| **Śliskie zbocze** | Twierdzenie, że jedno wydarzenie nieuchronnie doprowadzi do skrajnego wyniku | „Jeśli na to pozwolimy, następną rzeczą będzie całkowity chaos”. |
| **Rozumowanie okrężne** | Wniosek zakłada się w przesłankach | „Książka jest prawdziwa, ponieważ mówi, że to prawda”. |
| **Pośpieszne uogólnienie** | Wyciągnięcie szerokiego wniosku z niewystarczających dowodów | „Spotkałem dwóch niegrzecznych ludzi z tego miasta. Wszyscy tam muszą być niegrzeczni”. |
| **Post Hoc Ergo Propter Hoc** | Zakładając przyczynowość z sekwencji czasowej | „Wziąłem ten suplement i poczułem się lepiej, więc to musi działać”. |
| **Czerwony Śledź** | Wprowadzenie nieistotnego tematu dla odwrócenia uwagi | „Pytacie o moją politykę dotyczącą edukacji, ale tak naprawdę liczy się gospodarka”. |
| **Moda** | Coś jest prawdą, ponieważ wiele osób w to wierzy | „Każdy kupuje ten produkt, więc musi być najlepszy”. |
---

## Ocena argumentów: lista kontrolna
| Krok | Pytanie |
|------|--------------|
| 1. **Określ wniosek** | Co argument próbuje udowodnić? |
| 2. **Określić lokal** | Jakie dowody są oferowane? |
| 3. **Sprawdź ważność** | Czy wniosek wynika z przesłanek? |
| 4. **Sprawdź solidność** | Czy przesłanki są rzeczywiście prawdziwe? |
| 5. **Szukaj błędów** | Czy występują błędy strukturalne lub merytoryczne? |
| 6. **Rozważ kontrargumenty** | Jakie mogą być zastrzeżenia? |
| 7. **Ocena jakości dowodów** | Czy dowody są wiarygodne, wystarczające i istotne? |
---

## Dlaczego to ma znaczenie
Logika i krytyczne myślenie są podstawą matematyki, informatyki, prawa i badań naukowych. W świecie pełnym dezinformacji, reklam i perswazyjnej retoryki umiejętność rygorystycznej oceny argumentów to nie tylko umiejętność akademicka — to umiejętność przetrwania. Niezależnie od tego, czy debugujesz kod, projektujesz algorytmy, czy podejmujesz życiowe decyzje, jasne rozumowanie oddziela dobre oceny od złych.