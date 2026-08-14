---
# Metadata
title: "Physics"
description: "Fundamental forces, mechanics, thermodynamics, electromagnetism, relativity, quantum mechanics"
category: "Natural Sciences"
subcategory: "Physical Sciences"
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
    changes: "Split from science_and_nature.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Natural Sciences Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [physics, forces, energy, thermodynamics, electromagnetism, relativity, quantum-mechanics]
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

# Fizyka
Fizyka zadaje najbardziej fundamentalne pytanie w nauce: jak zachowuje się materia i energia? Wszystko inne – chemia, biologia, inżynieria – opiera się na odpowiedziach. Fizyka rozciąga się od skali subatomowej (mechanika kwantowa) po skalę kosmiczną (ogólna teoria względności), a jej zasady leżą u podstaw wszystkich innych nauk przyrodniczych.
---

## Cztery podstawowe siły
Każda interakcja we wszechświecie sprowadza się do czterech sił. Wszystko, co kiedykolwiek czułeś – grunt pod stopami, ciepło słońca, magnes na lodówce – jest jednym z nich.
| Siła | Siła względna | Zakres | Co to robi | Cząstka pośrednicząca |
|-------|--------|-------|------------|--------------------------------|
| **Silna broń nuklearna** | 1 (najsilniejszy) | Subatomowy (~10⁻¹⁵ m) | Utrzymuje razem protony i neutrony w jądrach atomowych | Gluon |
| **Elektromagnetyczne** | ~1/137 | Nieskończony | Reguluje elektryczność, magnetyzm, światło i chemię | Foton |
| **Słaby nuklearny** | ~10⁻⁶ | Subatomowy (~10⁻¹⁸ m) | Odpowiedzialny za rozpad radioaktywny | Bozony W i Z |
| **Grawitacja** | ~10⁻³⁹ (najsłabszy) | Nieskończony | Łączy masy; kształtuje kosmos | Grawiton (hipotetyczny) |
Grawitacja jest absurdalnie słaba w porównaniu z innymi – malutki magnes na lodówkę pokonuje przyciąganie grawitacyjne całej Ziemi. Ale grawitacja ma nieskończony zasięg i nigdy się nie znosi, więc w skali kosmicznej dominuje.
---

## Mechanika klasyczna
Mechanika klasyczna (mechanika Newtona) opisuje ruch obiektów makroskopowych z prędkościami znacznie mniejszymi od prędkości światła. Wystarczający do codziennej inżynierii — mostów, samochodów, pocisków, planet na orbicie.
### Trzy prawa Newtona
| Prawo | Oświadczenie | Implikacja |
|---------|-----------|------------|
| **Pierwszy (bezwładność)** | Obiekt pozostający w spoczynku pozostaje w spoczynku; obiekt w ruchu pozostaje w ruchu — chyba że działa na niego wypadkowa siła zewnętrzna | Definiuje pojęcie inercjalnego układu odniesienia |
| **Drugi (F = ma)** | Siła wypadkowa równa się masie razy przyspieszenie | Określa ilościowo, jak siły zmieniają ruch |
| **Trzeci (akcja-reakcja)** | Na każde działanie istnieje równa i przeciwna reakcja | Siły zawsze występują parami |
### Kluczowe ilości
| Ilość | Symbol | Jednostka | Formuła |
|---------|--------|------|--------|
| **Prędkość** | v | m/s | Przemieszczenie / czas |
| **Przyspieszenie** | | m/s² | Zmiana prędkości/czasu |
| **Siła** | F | Newtony (N) | m × a |
| **Pęd** | p | kg·m/s | m × v |
| **Energia kinetyczna** | KE | Dżule (J) | ½mv² |
| **Energia potencjalna** | PE | Dżule (J) | mgh (grawitacja) |
| **Praca** | W | Dżule (J) | F × d × cos(θ) |
| **Moc** | P | Waty (W) | W / t |
Zasada zachowania pędu i energii należą do najpotężniejszych narzędzi fizyki — dotyczą zderzeń, eksplozji, orbit i praktycznie każdej interakcji mechanicznej.
---

## Termodynamika
Energią rządzą trzy prawa. Są one absolutne — żaden znany proces ich nie narusza.
### Trzy prawa
| Prawo | Oświadczenie | Konsekwencja |
|---------|-----------|------------|
| **Pierwsze prawo** | Energii nie można stworzyć ani zniszczyć, można ją jedynie przekształcić | Całkowita energia w układzie zamkniętym jest stała |
| **Drugie prawo** | Entropia (nieporządek) w układzie zamkniętym zawsze wzrasta | Ciepło przepływa od ciepła do zimna; żaden silnik nie jest w 100% sprawny; czas ma kierunek |
| **Trzecie prawo** | Zero absolutne (-273,15°C / 0 K) jest nieosiągalne | Gdy temperatura zbliża się do zera, entropia zbliża się do minimum |
### Praktyczne implikacje
- Kawa stygnie, ponieważ ciepło rozprasza się w otoczeniu (drugie prawo).
- Silnik samochodowy przetwarza około 25% energii benzyny na ruch; reszta staje się ciepłem odpadowym.
- Lodówki i klimatyzatory przenoszą ciepło z zimnego do gorącego, ale wymagają do tego pracy zewnętrznej (nie naruszają drugiego prawa).
- Maszyny perpetuum mobile są niemożliwe w świetle tych praw.
---

## Elektryczność i magnetyzm
Elektryczność i magnetyzm to dwie strony tej samej siły: elektromagnetyzm. Poruszające się ładunki wytwarzają pola magnetyczne; zmieniające się pola magnetyczne wytwarzają prądy elektryczne. Ta relacja napędza większość nowoczesnych technologii.
### Podstawowe pojęcia
| Koncepcja | Symbol | Jednostka | Co to znaczy |
|--------|--------|------|-------------|
| **Napięcie** | V | Wolty (V) | „Ciśnienie” przepychające ładunki przez obwód |
| **Aktualne** | ja | Ampery (A) | Ile ładunków przepływa przez punkt na sekundę |
| **Opór** | R | Omy (Ω) | Jak bardzo materiał przeciwstawia się przepływowi prądu |
| **Moc** | P | Waty (W) | Szybkość transferu energii (P = V × I) |
**Prawo Ohma** (V = I × R) jest podstawą analizy obwodów. Jeśli znasz dwie wartości, możesz obliczyć trzecią.
**Indukcja elektromagnetyczna** — odkryta przez Faradaya — to sposób, w jaki elektrownie wytwarzają energię elektryczną. Obracaj magnes wewnątrz cewki drutu, a otrzymasz prąd. Zasadniczo robi to każda turbina, niezależnie od tego, czy napędzana jest parą (węgiel, energia jądrowa), wodą (elektrownia wodna), czy wiatrem.
### Równania Maxwella (koncepcyjne)
James Clerk Maxwell ujednolicił elektryczność i magnetyzm w czterech równaniach:
| Równanie | Co to mówi |
|--------------|------------|
| **Prawo Gaussa (elektryczne)** | Ładunki elektryczne wytwarzają pola elektryczne; linie pola zaczynają się i kończą na ładunkach |
| **Prawo Gaussa (magnetyczne)** | Nie ma monopoli magnetycznych; linie pola magnetycznego zawsze tworzą zamknięte pętle |
| **Prawo Faradaya** | Zmieniające się pole magnetyczne wytwarza pole elektryczne (podstawa generatorów) |
| **Prawo Ampera-Maxwella** | Prąd elektryczny i zmienne pola elektryczne wytwarzają pola magnetyczne |
Równania te przewidywały fale elektromagnetyczne, które okazały się światłem. Maxwell wykazał, że światło widzialne, fale radiowe, promieniowanie rentgenowskie i mikrofale są tym samym zjawiskiem o różnych częstotliwościach.
---

## Względność
Dwie teorie względności Einsteina zasadniczo zmieniły nasze rozumienie przestrzeni, czasu i energii.
### Szczególna teoria względności (1905)
| Zasada | Opis |
|---------------|------------|
| **Prędkość światła jest stała** | Światło przemieszcza się z prędkością ~300 000 km/s we wszystkich układach odniesienia, niezależnie od ruchu obserwatora |
| **Dylatacja czasu** | Poruszające się zegary tykają wolniej w porównaniu do nieruchomego obserwatora |
| **Skurczenie długości** | Poruszające się obiekty ulegają skróceniu w kierunku ruchu |
| **Równoważność masy i energii** | E = mc² — niewielka ilość masy zawiera ogromną ilość energii |
E = mc² wyjaśnia, dlaczego świeci słońce (fuzja przekształca niewielki ułamek masy w energię) i jak działa broń nuklearna.
### Ogólna teoria względności (1915)
Ogólna teoria względności rozszerza szczególną teorię względności na grawitację. Masa zakrzywia czasoprzestrzeń i tę krzywiznę odczuwamy jako grawitację. Najważniejsze przewidywania — wszystkie potwierdzone:
- **Soczewkowanie grawitacyjne**: Masywne obiekty załamują wokół siebie światło
- **Grawitacyjne dylatacja czasu**: Zegary tykają wolniej w silniejszych polach grawitacyjnych (satelity GPS muszą to skorygować)
- **Fale grawitacyjne**: zmarszczki w czasoprzestrzeni spowodowane przyspieszaniem masywnych obiektów (po raz pierwszy wykryte przez LIGO w 2015 r.)
- **Czarne dziury**: Regiony, w których zakrzywienie czasoprzestrzeni jest tak ekstremalne, że nic, nawet światło, nie może uciec
---

## Mechanika kwantowa
W skali subatomowej zasady zmieniają się całkowicie. Mechanika kwantowa jest najdokładniej przetestowaną teorią w całej nauce i jest głęboko sprzeczna z intuicją.
### Podstawowe zasady
| Zasada | Opis |
|---------------|------------|
| **Dualizm korpuskularno-falowy** | Cząstki (elektrony, fotony) zachowują się zarówno jak fale, jak i cząstki, w zależności od sposobu ich pomiaru
| **Superpozycja** | Układ kwantowy może istnieć w wielu stanach jednocześnie, dopóki nie zostanie zmierzony |
| **Zasada nieoznaczoności** | Nie można jednocześnie znać dokładnego położenia i dokładnego pędu cząstki (Heisenberg) |
| **Splątanie** | Dwie cząstki można skorelować w taki sposób, że pomiar jednej natychmiast określa stan drugiej, niezależnie od odległości |
| **Kwantyzacja** | Energia występuje w dyskretnych pakietach (kwantach), a nie w wartościach ciągłych
### Dlaczego to ma znaczenie
- **Półprzewodniki**: Cały przemysł elektroniczny opiera się na kwantowym zachowaniu elektronów w krzemie
- **Lasery**: Oparte na wymuszonej emisji fotonów (proces kwantowy)
- **Aparaty do rezonansu magnetycznego**: Wykorzystują jądrowy rezonans magnetyczny, zjawisko kwantowe
- **Obliczenia kwantowe**: Wykorzystują superpozycję i splątanie do rozwiązywania niektórych problemów wykładniczo szybciej niż klasyczne komputery
- **Chemia**: Wiązania chemiczne same w sobie są zjawiskiem kwantowym — elektrony zajmują orbitale molekularne
---

## Energia
Energia występuje w wielu postaciach – kinetycznej (ruch), potencjalnej (magazynowana), cieplnej (ciepło), chemicznej, elektrycznej, jądrowej – ale zawsze przestrzega jednej zasady: nie można jej stworzyć ani zniszczyć, a jedynie przekształcić. Jest to pierwsza zasada termodynamiki i jest ona absolutna.
Drugie prawo jest mniej wesołe: każda przemiana energii traci część energii w postaci ciepła odpadowego. Żaden proces nie jest skuteczny w 100%.
| Źródło energii | Wpisz | Wydajność | Ograniczenie klucza |
|--------------|------|-----------|----------------|
| **Węgiel** | Nieodnawialne | ~33-40% | Emisje CO₂, zanieczyszczenie powietrza |
| **Gaz ziemny** | Nieodnawialne | ~40-60% (cykl łączony) | Metan wycieka, nadal emituje CO₂ |
| **Rozszczepienie jądrowe** | Nieodnawialne (ograniczone paliwem) | ~33-37% | Składowanie odpadów, sprzeciw społeczny |
| **PV** | Odnawialne | ~15-22% | Sporadyczny, wymaga przechowywania |
| **Wiatr** | Odnawialne | ~35-45% | Przerywany, zależny od lokalizacji |
| **Hydroelektryczny** | Odnawialne | ~85-90% | Ograniczony geograficznie, wpływ na ekosystem |
| **Geotermia** | Odnawialne | ~10-23% | Ograniczona lokalizacja (gorące punkty tektoniczne) |
---

## Streszczenie
Fizyka jest podstawą wszelkich nauk przyrodniczych. Cztery podstawowe siły rządzą każdą interakcją we wszechświecie. Mechanika klasyczna opisuje codzienny świat ruchu i sił. Termodynamika wyznacza bezwzględne granice konwersji energii. Elektromagnetyzm jednoczy elektryczność, magnetyzm i światło. Teoria względności ujawnia, że ​​przestrzeń i czas to pojedyncza tkanina zakrzywiona masą. Mechanika kwantowa rządzi światem subatomowym i stanowi podstawę nowoczesnej technologii, od półprzewodników po maszyny MRI. Tym, co jednoczy całą fizykę, jest zaangażowanie w matematyczną precyzję i weryfikację eksperymentalną – każde twierdzenie jest sprawdzane w porównaniu z pomiarami, a każda teoria jest tymczasowa.