---
# Metadata
title: "Accessibility and Inclusive Design"
description: "WCAG, inclusive UX, assistive technology, accessible coding"
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

# Dostępność i projektowanie włączające
Dostępność (często w skrócie a11y) to praktyka polegająca na sprawianiu, aby oprogramowanie było użyteczne dla wszystkich – w tym osób z niepełnosprawnością wzrokową, słuchową, motoryczną, poznawczą i neurologiczną. Nie jest miło to mieć; jest to wymóg prawny w wielu jurysdykcjach, obowiązek moralny i dobra inżynieria. Dostępne oprogramowanie to lepsze oprogramowanie dla każdego, ponieważ decyzje projektowe, które pomagają niepełnosprawnym użytkownikom – przejrzysta struktura, nawigacja za pomocą klawiatury, wystarczający kontrast, czytelny tekst – poprawiają wygodę wszystkich użytkowników.
---

## Kto czerpie korzyści z dostępności?
| Rodzaj niepełnosprawności | Przykłady | Technologia wspomagająca |
|----------------|---------|--------------------------------------|
| **Wizualne** | Ślepota, słaby wzrok, ślepota barw | Czytniki ekranu (JAWS, NVDA, VoiceOver); lupy; tryby wysokiego kontrastu |
| **Słuchowe** | Głuchota, niedosłuch | Napisy; transkrypcje; alerty wizualne |
| **Silnik** | Ograniczona sprawność, paraliż, drżenie | Nawigacja wyłącznie za pomocą klawiatury; sterowanie głosem; urządzenia przełączające; śledzenie wzroku |
| **Poznawcze** | Dysleksja, ADHD, autyzm, zaburzenia pamięci | Przejrzysty język; spójna nawigacja; zmniejszone czynniki rozpraszające |
| **Tymczasowe** | Złamana ręka, jasne światło słoneczne, hałaśliwe otoczenie | Takie same udogodnienia jak trwała niepełnosprawność |
| **Sytuacyjne** | Trzymanie dziecka, prowadzenie, jedna ręka zajęta | Interfejsy głosowe; duże cele dotykowe |
**Kluczowe spostrzeżenia**: funkcje ułatwień dostępu zaprojektowane dla użytkowników niepełnosprawnych pomagają każdemu. Krawężniki (podjazdy na chodnikach) zostały zaprojektowane dla wózków inwalidzkich, ale korzystają z nich rodzice z wózkami, pracownicy dostawczy z wózkami i podróżni z bagażem.
---

## Dostępność sieci (WCAG)
Wytyczne dotyczące dostępności treści internetowych (WCAG) to międzynarodowy standard dostępności stron internetowych.
### Zasady WCAG (POUR)
| Zasada | Wymóg |
|---------------|------------|
| **Zauważalne** | Informacje muszą być prezentowane w sposób możliwy do odbioru przez użytkowników (alternatywy tekstu, podpisy, układ, który można dostosować) |
| **Działa** | Interfejs musi umożliwiać nawigację i być użyteczny (dostępny za pomocą klawiatury, wystarczająco dużo czasu, bez treści wywołujących ataki) |
| **Zrozumiałe** | Informacje i działanie muszą być zrozumiałe (czytelne, przewidywalne, pomoc przy wprowadzaniu danych) |
| **Solidny** | Treść musi współpracować z obecnymi i przyszłymi technologiami wspomagającymi
### Poziomy zgodności WCAG
| Poziom | Wymagania | Typowy cel |
|-------|------------|--------------|
| **A** | Poziom minimalny; 30 kryteriów sukcesu | Minimum prawne w niektórych jurysdykcjach |
| **AA** | Usuwa najczęstsze bariery | Standardowy cel dla większości organizacji |
| **AAA** | Najwyższy poziom; nie wszystkie treści mogą to osiągnąć | Treść specjalistyczna; strony edukacyjne |
### Kluczowe kryteria sukcesu (poziom AA)
| Kryterium | Wymóg | Jak osiągnąć |
|---------------|------------|--------------|
| **1.1.1 Treść nietekstowa** | Wszystkie obrazy mają alternatywy tekstowe |  Atrybuty `alt`; `aria-label`dla ikon |
| **1.3.1 Informacje i relacje** | Struktura przekazywana programowo | Semantyczny HTML; nagłówki; listy; zabytki |
| **1.4.3 Kontrast (minimalny)** | Tekst ma współczynnik kontrastu co najmniej 4,5:1 | Przetestuj za pomocą kontrolerów kontrastu; wybierz dostępne palety kolorów |
| **1.4.4 Zmień rozmiar tekstu** | Rozmiar tekstu można zmienić do 200% bez utraty | Używaj jednostek względnych (rem, em); responsywny projekt |
| **2.1.1 Klawiatura** | Wszystkie funkcje dostępne za pośrednictwem klawiatury | Brak pułapek na klawiaturę; widoczne wskaźniki skupienia |
| **2.4.3 Kolejność fokusu** | Porządek skupienia zachowuje znaczenie i funkcjonalność | Logiczna kolejność tabulacji; Kolejność DOM odpowiada porządkowi wizualnemu |
| **2.4.7 Widoczna ostrość** | Aktywność klawiatury jest wskazywana wizualnie | Style CSS `:focus-visible`; nigdy`outline: none`bez zamiennika |
| **3.3.2 Etykiety lub instrukcje** | Dane wejściowe mają etykiety |  elementy `<label>`; `aria-label`|
| **4.1.2 Imię, rola, wartość** | Komponenty interfejsu użytkownika mają dostępne nazwy i role | atrybuty ARIA; semantyczny HTML |
---

## ARIA (dostępne bogate aplikacje internetowe)
ARIA dodaje informacje o dostępności do elementów HTML, które nie mają wbudowanej semantyki.
### Role ARIA
| Rola | Cel | Przykład |
|------|---------|--------|
| `button`| Identyfikuje element jako przycisk |`<div>`w stylu przycisku |
| `dialog`| Okno modalne lub niemodalne | Niestandardowe komponenty modalne |
| `tablist`/`tab`/`tabpanel`| Interfejs karty | Niestandardowe komponenty zakładek |
| `alert`| Ważny komunikat, który pojawia się dynamicznie | Powiadomienia o błędach |
| `progressbar`| Wskaźnik postępu | Ładowanie stanów |
| `menu`/`menuitem`| Nawigacja po menu | Rozwijane menu |
### Atrybuty ARIA
| Atrybut | Cel | Przykład |
|----------|---------|--------|
| `aria-label`| Dostępna nazwa, gdy nie widać tekstu | Przycisk zawierający tylko ikonę:`aria-label="Search"`|
| `aria-describedby`| Linkuje element do jego opisu | Pole formularza z tekstem pomocy |
| `aria-expanded`| Wskazuje, czy sekcja jest rozwinięta | Akordeon; menu rozwijane |
| `aria-hidden`| Ukrywa element przed technologią wspomagającą | Ikony dekoracyjne |
| `aria-live`| Ogłasza dynamiczne zmiany zawartości | Aktualizacje na żywo; powiadomienia |
| `aria-disabled`| Wskazuje, że element jest wyłączony | Przyciski wyszarzone |
### Pierwsza zasada ARIA
> **Nie używaj ARIA, jeśli zamiast tego możesz użyć natywnego HTML.**`<button>`jest już dostępny.`<div role="button">`wymaga ręcznego dodania obsługi klawiatury, zarządzania fokusem i obsługi czytnika ekranu. Najpierw użyj semantycznego HTML; ARIA tylko wtedy, gdy elementy natywne nie mogą wykonać tego zadania.
---

## Nawigacja za pomocą klawiatury
| Klucz | Oczekiwane zachowanie |
|-----|--------------------------------|
| **Zakładka** | Przenieś fokus na następny element interaktywny |
| **Shift + Tab** | Przenieś fokus na poprzedni element interaktywny |
| **Enter / Spacja** | Aktywuj wybrany element (przycisk, link) |
| **Klawisze strzałek** | Nawigacja w obrębie komponentów (menu, zakładek, grup opcji) |
| **Ucieczka** | Zamknij okno dialogowe, menu lub wyskakujące okienko |
| **Strona główna / Koniec** | Przejdź do pierwszej/ostatniej pozycji na liście |
### Typowe pułapki na klawiaturę
| Problem | Napraw |
|--------|-----|
| Fokus wchodzi do komponentu, ale nie może go opuścić | Upewnij się, że Tab przenosi fokus; uchwyt Ucieczka |
| Modal nie zatrzymuje ostrości | Fokus powinien zmieniać się w obrębie modalności; powrót do wyzwalacza po zamknięciu |
| Komponenty niestandardowe nie reagują na klawiaturę | Dodaj moduły obsługi klawiszy dla Enter, Spacja, strzałki |
---

## Kolor i projekt wizualny
| Wytyczne | Wymóg |
|---------------|------------|
| **Współczynnik kontrastu** | 4,5:1 dla normalnego tekstu; 3:1 dla dużego tekstu (18 pkt+ lub 14 pkt+ pogrubienie) |
| **Nie polegaj wyłącznie na kolorze** | Oprócz koloru | używaj ikon, tekstu lub wzorów
| **Wskaźniki ostrości** | Zawsze widoczny; wysoki kontrast; nigdy nie usuwany bez wymiany |
| **Zmiana rozmiaru tekstu** | Układ musi działać przy powiększeniu 200% |
| **Responsywny** | Treść musi ponownie wlać się do szerokości 320 pikseli (na urządzenia mobilne) |
### Uwagi dotyczące ślepoty barw
| Wpisz | Dotknięte kolory | Porada projektowa |
|------|----------------------|------------|
| **Deuteranopia** | Czerwono-zielony (najczęściej) | Nie używaj koloru czerwonego/zielonego do przekazania statusu; użyj ikon + kolor |
| **Protanopia** | Czerwono-zielony | To samo co powyżej |
| **Tritanopia** | Niebiesko-żółty | Nie używaj koloru niebieskiego/żółtego jako jedynego wyróżnika |
---

## Testowanie dostępności
| Metoda | Narzędzie | Co łapie |
|------------|------|----------------|
| **Automatyczne skanowanie** | topór, Latarnia Morska, FALA | Brakujący tekst alternatywny; kwestie kontrastu; Błędy ARIA |
| **Testowanie klawiatury** | Instrukcja: odłącz mysz, używaj tylko klawiatury | Kolejność skupienia; pułapki na klawiaturę; brakujące handlery |
| **Testowanie czytnika ekranu** | NVDA (bezpłatny), VoiceOver (macOS), JAWS | Brakujące etykiety; słaba struktura; niezapowiedziane zmiany |
| **Testowanie zoomu** | Zoom przeglądarki do 200%, 400% | Złamanie układu; obcięty tekst; problemy z przepełnieniem |
| **Kontrast kolorów** | Sprawdzanie kontrastu WebAIM, wtyczka Stark | Niewystarczające współczynniki kontrastu |
| **Testowanie użytkowników** | Test z niepełnosprawnymi użytkownikami | Bariery w świecie rzeczywistym, których pomijają zautomatyzowane narzędzia |
---

## Wymagania prawne
| Prawo | Region | Wymagania |
|---------|--------|------------|
| **ADA** (Ustawa o osobach niepełnosprawnych) | USA | Strony internetowe obiektów użyteczności publicznej muszą być dostępne |
| **Artykuł 508** | USA (federalne) | ICT agencji federalnych muszą być dostępne |
| **EAA** (Europejski akt o dostępności) | UE (2025+) | Produkty i usługi muszą spełniać wymogi dostępności |
| **EN 301 549** | UE | Standard techniczny dostępności ICT |
| **ACA** (Kanadyjska ustawa o dostępności) | Kanada | Branże rządowe i regulowane |
| **Ustawa o równości z 2010 r.** | Wielka Brytania | Usługodawcy muszą dokonać rozsądnych dostosowań |
---

## Dostępność mobilna
| Platforma | Wytyczne | Kluczowe narzędzia |
|---------|-----------|----------|
| **iOS** | Wytyczne Apple dotyczące interfejsu ludzkiego (sekcja Dostępność) | VoiceOver; Typ dynamiczny; Przełącznik sterowania |
| **Android** | Wytyczne dotyczące dostępności Androida | TalkBack; Przełącz dostęp; Wybierz, aby mówić |
| Koncern mobilny | Rozwiązanie |
|-------------------|---------|
| **Dotykaj cele** | Minimum 44×44 punkty (iOS) / 48×48 dp (Android) |
| **Obsługa czytnika ekranu** | Opisy treści; etykiety dostępności |
| **Czułość ruchu** | Przestrzegaj`prefers-reduced-motion`; unikaj automatycznych animacji |
| **Dynamiczny rozmiar tekstu** | Rozmiary czcionek systemu wsparcia; użyj skalowalnych jednostek tekstowych |
---

## Streszczenie
Dostępność nie jest funkcją, którą dodajesz na końcu — to zasada projektowania, która powinna uwzględniać każdą decyzję od samego początku. Użyj semantycznego HTML. Upewnij się, że nawigacja za pomocą klawiatury działa. Zachowaj wystarczający kontrast kolorów. Zapewnij tekstowe alternatywy dla treści nietekstowych. Przetestuj z czytnikami ekranu i prawdziwymi niepełnosprawnymi użytkownikami. Rezultatem jest oprogramowanie, które działa lepiej dla wszystkich — nie tylko dla osób niepełnosprawnych, ale także dla osób z tymczasowymi upośledzeniami, ograniczeniami sytuacyjnymi, starszymi urządzeniami, wolnymi połączeniami i tysiącem innych powodów, dla których rzeczywiste użytkowanie różni się od wyidealizowanego środowiska programisty.