<!--
---
# Metadata
title: "Game Theory and Strategic Thinking"
description: "Nash equilibrium, prisoner's dilemma, mechanism design, auctions"
category: "Business and Economics"
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
reviewed_by: "Business & Economics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [game, theory, business-and-economics]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Teoria gier i myślenie strategiczne
Teoria gier to matematyczne badanie interakcji strategicznych — sytuacji, w których wynik zależy nie tylko od tego, co robisz, ale od tego, co robią inni. Ma to zastosowanie wszędzie: konkurencja biznesowa, stosunki międzynarodowe, aukcje, negocjacje, biologia ewolucyjna i codzienne decyzje, takie jak wybór trasy w ruchu ulicznym. Podstawowy wniosek jest taki, że racjonalni aktorzy w sytuacjach strategicznych nie tylko optymalizują swoją własną strategię — oni przewidują, co zrobią inni, a inni robią to samo.
---

## Podstawowe pojęcia
### Kluczowa terminologia
| Termin | Definicja |
|------|-----------|
| **Gra** | Każda sytuacja, w której jest dwóch lub więcej decydentów (graczy), których wybory wpływają na wzajemne wyniki |
| **Gracz** | Osoba podejmująca decyzje w grze |
| **Strategia** | Kompletny plan działania na każdą sytuację, która może się pojawić |
| **Wypłata** | Wynik, jaki gracz otrzymuje w wyniku określonej kombinacji strategii |
| **Równowaga Nasha** | Zestaw strategii, w przypadku których żaden gracz nie może poprawić swojej wypłaty poprzez jednostronną zmianę swojej strategii |
| **Strategia dominująca** | Strategia, która jest najlepsza niezależnie od tego, co robią inni gracze |
| **Gra o sumie zerowej** | Zysk jednego gracza jest dokładnie stratą drugiego
| **Gra o sumie niezerowej** | Gracze mogą potencjalnie wszyscy zyskać lub wszyscy stracić |
| **Gra kooperacyjna** | Gracze mogą zawierać wiążące umowy |
| **Gra bez współpracy** | Brak wiążących umów; każdy gracz działa we własnym interesie |
---

## Klasyczne gry
### Dylemat więźnia
Dwóch podejrzanych zostaje aresztowanych. Każdy może współpracować (milczeć) lub zdradzać (przyznać się).
| | B Współpracuje | B Wady |
|---|------------|-----------|
| **A Współpracuje** | A: 1 rok, B: 1 rok | A: 10 lat, B: bezpłatnie |
| **Wady** | A: bezpłatnie, B: 10 lat | A: 5 lat, B: 5 lat |
| Wgląd | Opis |
|--------|------------|
| **Strategia dominująca** | Defekt dominuje u obu zawodników |
| **Równowaga Nasha** | Obie wady (po 5 lat) |
| **Optymalny w Pareto** | Obaj współpracują (po 1 roku) |
| **Lekcja** | Racjonalne indywidualne decyzje mogą prowadzić do gorszych wyników ogółem
### Inne klasyczne gry
| Gra | Opis | Równowaga Nasha | Lekcja |
|------|------------|----------------|------------|
| **Kurczak (Jastrząb-Gołąb)** | Dwóch kierowców kieruje się ku sobie; zbocz lub jedź prosto | Jeden skręca, drugi jedzie prosto | Ryzykanctwo; wiarygodność zaangażowania |
| **Polowanie na jelenie** | Polujcie razem na jelenia (wysoka nagroda) lub samotnie zapoluj na zająca (niska nagroda) | Oba jelenie lub oba zające | Koordynacja; zaufaj |
| **Wojna płci** | Dwóch graczy preferuje różne wyniki, ale chce koordynować | Obaj idą na to samo wydarzenie | Wielokrotne równowagi; kto porusza się pierwszy, ma przewagę |
| **Gra w ultimatum** | Wnioskodawca dzieli pieniądze; odpowiadający akceptuje lub odrzuca (oba nic nie dostają) | Oferent oferuje minimum; odpowiadający akceptuje | Ludzie odrzucają nieuczciwe oferty (irracjonalne, ale powszechne) |
| **Gra o dobro publiczne** | Wesprzyj wspólną pulę lub bezpłatną przejażdżkę | Wszyscy jeżdżą na darmo | Tragedia wspólnego pastwiska; potrzeba egzekwowania |
---

## Rodzaje gier
### Według czasu
| Wpisz | Opis | Przykład |
|------|------------|--------|
| **Jednoczesne** | Gracze poruszają się w tym samym czasie (lub nie wiedząc o ruchach innych) | Papier-kamień-nożyce; aukcje z zapieczętowaną ofertą |
| **Sekwencyjny** | Gracze poruszają się jeden po drugim; późniejsi gracze obserwują wcześniejsze ruchy | Szachy; decyzje o wejściu na rynek |
| **Powtórzone** | Ta sama gra odtwarzana wiele razy | Powtarzający się dylemat więźnia; ciągła konkurencja biznesowa |
### Według informacji
| Wpisz | Opis | Przykład |
|------|------------|--------|
| **Doskonała informacja** | Wszyscy gracze znają wszystkie poprzednie ruchy | Szachy; warcaby |
| **Niedoskonała informacja** | Niektóre ruchy są ukryte | Poker; konkurencja biznesowa |
| **Pełne informacje** | Wszyscy gracze znają wszystkie wypłaty i strategie | Większość gier podręcznikowych |
| **Informacje niepełne** | Niektóre wypłaty lub typy są nieznane | Aukcje; negocjacje |
---

## Koncepcje rozwiązań
### Równowaga Nasha
| Aspekt | Opis |
|------------|------------|
| **Definicja** | Żaden gracz nie jest w stanie poprawić swojej wypłaty, zmieniając samodzielnie strategię |
| **Jak znaleźć** | Znajdź dla każdego gracza najlepszą odpowiedź na strategie innych; gdzie one wszystkie się przecinają, to równowaga Nasha |
| **Istnienie** | Każda skończona gra ma co najmniej jedną równowagę Nasha (prawdopodobnie w strategiach mieszanych) |
| **Wyjątkowość** | Gry mogą mieć wiele równowag Nasha; pojawiają się problemy z koordynacją |
| **Ograniczenie** | Równowaga Nasha nie mówi, która równowaga zostanie wybrana; nie uwzględnia uczciwości |
### Równowaga strategii dominującej
| Krok | Opis |
|------|------------|
| **1. Identyfikacja strategii** | Lista wszystkich dostępnych strategii dla każdego gracza |
| **2. Znajdź strategie dominujące** | Strategia, która jest najlepsza niezależnie od tego, co robią inni |
| **3. Jeśli wszyscy gracze mają** | Kombinacja jest dominującą strategią równowagi |
| **4. Jeśli nie** | Użyj iterowanej eliminacji strategii zdominowanych lub równowagi Nasha |
### Wsteczna indukcja (gry sekwencyjne)
| Krok | Opis |
|------|------------|
| **1. Narysuj drzewo gry** | Węzły = punkty decyzyjne; gałęzie = działania |
| **2. Zacznij od końca** | Zidentyfikuj optymalny wybór ostatniego gracza w każdym węźle końcowym |
| **3. Pracuj wstecz** | W każdym wcześniejszym węźle wybierz akcję, która prowadzi do najlepszego wyniku |
| **4. Wynik** | Doskonała równowaga podgry — optymalna strategia w każdym punkcie decyzyjnym |
---

## Zaawansowane koncepcje
### Strategie mieszane
| Koncepcja | Opis | Przykład |
|--------|-------------|--------|
| **Strategia mieszana** | Losowanie działań według prawdopodobieństw | Kamień-papier-nożyce: graj każdym z prawdopodobieństwem 1/3 |
| **Dlaczego randomizować?** | Uniemożliwia przeciwnikom przewidzenie Twojego ruchu | Rzuty karne w piłce nożnej; audyty podatkowe |
| **Strategia mieszanaRównowaga Nasha** | Każdy gracz jest obojętny pomiędzy swoimi czystymi strategiami | Żaden z graczy nie może wykorzystać drugiego |
### Powtarzające się gry i twierdzenie ludowe
| Koncepcja | Opis |
|--------|------------|
| **Skończenie powtarzane** | Indukcja wsteczna niszczy współpracę; tak samo jak gra jednorazowa | Dezercja w ostatniej rundzie rozprzestrzenia się wstecz |
| **Nieskończenie powtarzane** | Współpraca może być podtrzymywana poprzez groźbę przyszłej kary | Wet za wet; ponure strategie wyzwalania |
| **Twierdzenie ludowe** | Każda indywidualnie racjonalna wypłata może być równowagą Nasha w nieskończenie powtarzanej grze | Współpraca jest możliwa, jeśli przyszłość ma wystarczające znaczenie |
| **Współczynnik rabatowy** | Jak bardzo gracze cenią przyszłe wypłaty; wyżej = większa współpraca | Cierpliwi gracze współpracują więcej |
### Projekt mechanizmu (teoria odwróconej gry)
| Koncepcja | Opis |
|--------|------------|
| **Cel** | Zaprojektuj zasady gry, aby osiągnąć pożądany wynik |
| **Aplikacje** | Aukcje; systemy głosowania; projekt kontraktu; projektowanie rynku |
| **Zasada objawienia** | Każdy wynik możliwy do osiągnięcia za pomocą dowolnego mechanizmu można osiągnąć za pomocą prawdziwego mechanizmu bezpośredniego |
| **Przykład** | Aukcja Vickrey (zapieczętowana oferta drugiej ceny) — licytowanie prawdziwej wartości jest strategią dominującą |
---

## Aplikacje
### Biznes
| Aplikacja | Koncepcja teorii gier | Wgląd |
|------------|---------|--------|
| **Konkurencja cenowa** | Dylemat więźnia | Wojny cenowe szkodzą obu firmom; cicha zmowa w powtarzających się grach |
| **Wejście na rynek** | Gra sekwencyjna; zaangażowanie | Groźba ze strony operatora zasiedziałego dotycząca walki z wejściem na rynek jest wiarygodna tylko wtedy, gdy zainwestuje on w potencjał |
| **Aukcje** | Projekt mechanizmu | Aukcje drugiej ceny ujawniają prawdziwe wartości; aukcje widma zbierają miliardy |
| **Negocjacje** | Gra targowa; Równowaga Nasha | Podziel nadwyżkę; przewaga pierwszego gracza w grach ultimatum |
| **Sygnalizacja** | Model edukacji Spence'a | Drogie sygnały są wiarygodne, bo typów niskiej jakości na nie nie stać
### Stosunki międzynarodowe
| Aplikacja | Koncepcja teorii gier | Wgląd |
|------------|---------|--------|
| **Wyścig zbrojeń** | Dylemat więźnia | Obie strony lepiej by się rozbroiły, ale nie mogą sobie ufać |
| **Wojny handlowe** | Powtórzona gra | Wet za wet: współpracuj aż do innych wad, a następnie zemścij się |
| **Porozumienia klimatyczne** | Gra dóbr publicznych | Jazda na gapę jest racjonalna; potrzebne mechanizmy egzekwowania prawa |
| **Odstraszanie** | Kurczak; wiarygodne zaangażowanie | Wzajemnie zapewnione zniszczenie jest równowagą Nasha |
---

## Streszczenie
Teoria gier bada strategiczne interakcje, w których wynik zależy od działań innych. Równowaga Nasha – w której żaden gracz nie odnosi korzyści ze zmiany strategii samodzielnie – jest centralną koncepcją rozwiązania. Klasyczne gry, takie jak dylemat więźnia, pokazują, że racjonalne indywidualne decyzje mogą przynieść zbiorowo złe skutki. Gry sekwencyjne rozwiązuje się metodą indukcji wstecznej. Powtarzające się gry mogą podtrzymać współpracę pod groźbą przyszłej kary. Strategie mieszane obejmują randomizację, aby zachować nieprzewidywalność. Projekt mechanizmu odwraca pytanie: zamiast przewidywać wyniki, projektuje zasady umożliwiające osiągnięcie pożądanych wyników (jak w przypadku aukcji). Zastosowania obejmują biznes (ceny, wejście, aukcje), politykę (głosowanie, traktaty), biologię (strategie stabilne ewolucyjnie) i życie codzienne. Podstawową lekcją jest to, że strategia nie polega tylko na tym, co robisz, ale na przewidywaniu, co zrobią inni, wiedząc, że robią to samo.