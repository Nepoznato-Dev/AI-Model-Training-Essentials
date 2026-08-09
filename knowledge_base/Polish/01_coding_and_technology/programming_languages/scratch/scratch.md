---
# Metadata
title: "Scratch"
description: "Comprehensive reference for the Scratch programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
tags: [scratch, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "29 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Zadrapanie
Scratch to wizualny język programowania oparty na blokach opracowany przez MIT Media Lab i wydany po raz pierwszy w 2007 roku. Zamiast pisać kod tekstowy, użytkownicy łączą kolorowe bloki, aby tworzyć programy. Scratch został zaprojektowany specjalnie dla dzieci w wieku 8–16 lat (chociaż używają go uczniowie w każdym wieku), aby uczyć podstawowych pojęć programistycznych — pętli, warunków warunkowych, zmiennych, zdarzeń i funkcji — bez bariery błędów składniowych.
Scratch to najpopularniejszy na świecie język programowania dla początkujących, z ponad 100 milionami zarejestrowanych użytkowników i dostępny w ponad 70 językach. Działa w przeglądarce internetowej i jest bezpłatny.
---

## Dlaczego Scratch ma znaczenie
- **Najlepsze wprowadzenie do programowania**: Całkowicie usuwa bariery składniowe. Pojęcia są nauczane poprzez manipulację wizualną.
- **Myślenie obliczeniowe**: uczy dekompozycji, rozpoznawania wzorców, abstrakcji i projektowania algorytmów.
- **Napędzani kreatywnością**: Dzieci tworzą gry, animacje, historie i muzykę — ucząc się programowania, jest to produkt uboczny tworzenia rzeczy, na których im zależy.
- **Globalny zasięg**: Używany w szkołach na całym świecie. Dostępne w ponad 70 językach. Bezpłatny i oparty na przeglądarce.
- **Społeczność**: internetowa społeczność Scratch uczy dzielenia się, remiksowania i wspólnego uczenia się.
## Kompromisy
| Ograniczenie | Szczegóły | Typowe obejście |
|----------|---------|--------------------------------|
| **Nie jest to „prawdziwy” język programowania** | Nie można tworzyć oprogramowania produkcyjnego, interfejsów API ani systemów | Przejście na Python, JavaScript lub języki tekstowe |
| **Ograniczone możliwości** | Żadnych operacji wejścia/wyjścia plików, sieci ani zaawansowanych struktur danych | Używaj do nauki; przejdź na języki tekstowe dla prawdziwych projektów |
| **Wydajność** | Tłumaczone, wolne dla złożonych projektów | Nie przeznaczony do pracy, w której wydajność ma kluczowe znaczenie |
| **Postrzeganie wieku** | Często postrzegany jako „tylko dla dzieci” | Scratch to narzędzie do nauki, a nie profesjonalny język |
---

## Jak działa Scratch
Programy Scratch (zwane „projektami”) składają się z **duszków** (znaków/obiektów), które reagują na **bloki** połączone ze sobą w skryptach.
### Podstawowe koncepcje (nauczane poprzez bloki)
| Koncepcja | Kategoria bloku zarysowania | Przykład |
|--------|----------------------|--------|
| **Sekwencje** | Ruch, wygląd | „Przesuń się o 10 kroków”, a następnie „Przywitaj się” |
| **Pętle** | Kontrola (żółty) | „Powtórz 10”, „Na zawsze”, „Powtarzaj do” |
| **Warunki** | Kontrola (żółty) | „Jeśli… to”, „Jeśli… to… jeszcze” |
| **Zmienne** | Zmienne (pomarańczowe) | „Ustaw wynik na 0”, „Zmień wynik o 1” |
| **Wydarzenia** | Wydarzenia (żółty) | „Po kliknięciu zielonej flagi”, „Po naciśnięciu klawisza” |
| **Funkcje** | Moje bloki (niestandardowe) | Zdefiniuj sekwencje bloków wielokrotnego użytku |
| **Listy (tablice)** | Zmienne (pomarańczowe) | „Dodaj do listy”, „Pozycja listy” |
| **Nadawanie** | Wydarzenia | Wysyłaj wiadomości pomiędzy duszkami |
### Przykład: prosta logika gry
```
When green flag clicked:
  Set [score] to 0
  Forever:
    If <touching [enemy]?> then:
      Change [score] by -1
      Play sound [ouch]
    If <touching [coin]?> then:
      Change [score] by 1
      Go to random position
```

---

## Zaawansowana składnia i wzorce
### Szczegóły blokowania kategorii
Scratch 3.0 organizuje bloki w kategorie oznaczone kolorami:
| Kategoria | Kolor | Typy bloków |
|---------|--------|------------|
| **Ruch** | Niebieski | poruszaj się, skręcaj, idź, szybuj, wskaż, zmień x/y |
| **Wygląda** | Fioletowy | powiedz, pomyśl, zmień kostium, zmień rozmiar, pokaż/ukryj |
| **Dźwięk** | Różowy | odtwarzaj dźwięk, zatrzymuj dźwięki, zmieniaj głośność, zmieniaj wysokość dźwięku |
| **Wydarzenia** | Żółty | po kliknięciu flagi, po naciśnięciu klawisza, po kliknięciu duszka, transmisja |
| **Kontrola** | Złoto | czekaj, powtarzaj, na zawsze, jeśli, jeśli-w przeciwnym razie, powtarzaj aż, przestań |
| **Wyczuwanie** | Jasnoniebieski | dotykanie, naciśnięcie klawisza, mysz, odległość, pytanie/odpowiedź, minutnik |
| **Operatorzy** | Zielony | operacje matematyczne, operacje tekstowe, porównanie i/lub/nie, losowe |
| **Zmienne** | Pomarańczowy | ustaw/zmień zmienną, operacje na listach |
| **Moje bloki** | Ciemnoczerwony | niestandardowe definicje bloków (funkcje) |
### Zaawansowane wzory blokowe
```
// Pattern: Timer-based movement (smooth animation)
When green flag clicked:
  Set [speed] to 5
  Forever:
    Change x by (speed)
    If <(x position) > 200> then
      Set [speed] to ((speed) * -1)
    If <(x position) < -200> then
      Set [speed] to ((speed) * -1)

// Pattern: State machine using variables
When green flag clicked:
  Set [game_state] to [menu]
  Forever:
    If <(game_state) = [menu]> then
      Show
      Go to x: 0 y: 0
    If <(game_state) = [playing]> then
      Hide
    If <(game_state) = [game_over]> then
      Say [Game Over!] for 2 secs

// Pattern: Object-oriented sprite (each sprite manages its own state)
When green flag clicked:
  Set [hp] to 100
  Set [max_hp] to 100
  Set [is_alive] to true
  Forever:
    If <(is_alive) = true> then
      If <touching [enemy]?> then
        Change [hp] by -10
        If <(hp) < 1> then
          Set [is_alive] to false
          Broadcast [player_dead]
```

### Bloki niestandardowe (funkcje)
```
// Define a custom block with parameters
Define: Jump (height) times (count)
  Repeat (count):
    Change y by (height)
    Wait 0.2 seconds
    Change y by ((height) * -1)
    Wait 0.2 seconds

// Usage:
When space key pressed:
  Jump height: 50 times: 3

// Custom block with "run without screen refresh" (optimization)
Define: Draw fractal (depth) (size)
  Run without screen refresh: true
  If <(depth) = 0> then
    Move (size) steps
  Else:
    Draw fractal depth: ((depth) - 1) size: ((size) / 2)
    Turn right 60 degrees
    Draw fractal depth: ((depth) - 1) size: ((size) / 2)
    Turn left 120 degrees
    Draw fractal depth: ((depth) - 1) size: ((size) / 2)
    Turn right 60 degrees
```

### Operacje na listach (tablice)
```
// Creating and using lists
When green flag clicked:
  Delete all of [scores]
  Add [100] to [scores]
  Add [85] to [scores]
  Add [92] to [scores]
  Add [78] to [scores]
  
  // Access items (1-indexed)
  Set [total] to 0
  Set [i] to 1
  Repeat (length of [scores]):
    Change [total] by (item (i) of [scores])
    Change [i] by 1
  
  Set [average] to ((total) / (length of [scores]))
  Say (join [Average: ] (average)) for 2 secs

// Sorting a list (bubble sort)
Define: Sort List
  Set [n] to (length of [scores])
  Repeat (n)
    Set [i] to 1
    Repeat ((n) - 1)
      If <(item (i) of [scores]) > (item ((i) + 1) of [scores])> then
        // Swap
        Set [temp] to (item (i) of [scores])
        Replace item (i) of [scores] with (item ((i) + 1) of [scores])
        Replace item ((i) + 1) of [scores] with (temp)
      Change [i] by 1
```

### Nadawanie (komunikacja między duszkami)
```
// Sprite 1 (Player):
When space key pressed:
  Broadcast [fire_bullet]

// Sprite 2 (Bullet):
When I receive [fire_bullet]:
  Go to [Player]
  Show
  Repeat 50:
    Change y by 10
  Hide

// Sprite 3 (Enemy):
When I receive [fire_bullet]:
  If <touching [Bullet]?> then
    Change [hp] by -25
    If <(hp) < 1> then
      Broadcast [enemy_destroyed]
      Hide
```

---

## Architektura i projektowanie systemów
### Projektowanie sterowane zdarzeniami
Scratch wykorzystuje architekturę sterowaną zdarzeniami. Każdy skrypt zaczyna się od bloku zdarzenia (bloku kapelusza) i jest uruchamiany w odpowiedzi na to zdarzenie.
```
Event Types:
+-------------------------------------------+
| when [green flag] clicked    (startup)     |
| when [space] key pressed     (keyboard)    |
| when this sprite clicked     (mouse)       |
| when [backdrop] switches to  (stage event) |
| when [loudness] > [10]       (sound)       |
| when I receive [message]     (broadcast)   |
| when video motion > [10]     (camera)      |
+-------------------------------------------+
```

### Struktura projektu
```
scratch-project/
├── project.sb3              * Saved project file (ZIP format)
├── sprites/
│   ├── Player/              * Player sprite
│   │   ├── costumes/        * Costume images
│   │   └── sounds/          * Sound files
│   ├── Enemy/
│   │   ├── costumes/
│   │   └── sounds/
│   └── Bullet/
├── stage/
│   ├── backdrops/           * Background images
│   └── sounds/              * Stage sounds
└── README.md
```

### System klonowania (tworzenie obiektów)
```
// Creating clones (like creating object instances)
When green flag clicked:
  Forever:
    Wait 1 seconds
    Create clone of [Enemy]

When I start as a clone:
  Go to random position
  Show
  Set [hp] to 3
  Forever:
    Change y by -3
    If <(y position) < -170> then
      Delete this clone
    If <touching [Bullet]?> then
      Change [hp] by -1
      If <(hp) < 1> then
        Change [score] by 10
        Delete this clone
```

---

## Konfiguracja projektu i budowanie systemu
### Rozszerzenia Scratcha
Scratch obsługuje oficjalne i społecznościowe rozszerzenia, które dodają możliwości:
| Rozszerzenie | Cel |
|---------------|--------|
| **Pióro** | Rysuj linie i kształty na scenie |
| **Wykrywanie wideo** | Użyj kamery internetowej do wykrywania ruchu |
| **Tekst na mowę** | Konwertuj tekst na dźwięk mówiony |
| **Tłumacz** | Tłumaczenie tekstu między językami |
| **Makey Makey** | Podłącz obiekty fizyczne jako dane wejściowe |
| **mikro:bit** | Podłącz sprzęt BBC micro:bit |
| **LEGO Burze umysłów** | Kontroluj roboty LEGO |
| **Muzyka** | Graj na nutach i instrumentach |
### Format pliku Scratch
```
Scratch 3.0 projects (.sb3) are ZIP archives containing:
├── project.json             * All scripts, sprites, and metadata
├── [md5hash].svg           * Costume images (SVG or PNG)
├── [md5hash].png           * Additional costumes
└── [md5hash].wav           * Sound files

The project.json contains:
{
  "targets": [
    {
      "isStage": true,
      "name": "Stage",
      "costumes": [...],
      "sounds": [...],
      "blocks": {...}
    },
    {
      "isStage": false,
      "name": "Sprite1",
      "position": {"x": 0, "y": 0},
      "blocks": {...}
    }
  ],
  "monitors": [...],
  "meta": {"semver": "3.0.0"}
}
```

### Edytor offline
```
Scratch Desktop (offline editor) available for:
- Windows 10+ (Microsoft Store or direct download)
- macOS 10.13+
- ChromeOS

Installation:
1. Download from https://scratch.mit.edu/download
2. Install and run — no internet required
3. Projects save as .sb3 files locally
```

---

## Testowanie i debugowanie
### Wbudowane narzędzia do debugowania
Scratch udostępnia kilka wbudowanych narzędzi do debugowania projektów:
| Narzędzie | Jak używać |
|------|-----------|
| **Tryb żółwia** | Kliknij prawym przyciskiem myszy duszka i wybierz „pokaż debugowanie”, aby zobaczyć współrzędne |
| **Zmienne monitory** | Kliknij zmienną prawym przyciskiem myszy i wybierz „pokaż”, aby zobaczyć jej wartość w czasie rzeczywistym |
| **Lista monitorów** | Wyświetlanie zawartości listy w trybie normalnym, wierszowym lub kolumnowym |
| **Tryb Turbo** | Przytrzymaj Shift i kliknij zieloną flagę, aby przyspieszyć wykonanie |
| **Tryb jednoetapowy** | Kliknij prawym przyciskiem myszy zieloną flagę dla „jednego kroku” (spowalnia wykonanie) |
### Wzorce debugowania
```
// Debug: Display variable values on sprite
When green flag clicked:
  Forever:
    Say (join [Score: ] (score))

// Debug: Visual boundary checking
When green flag clicked:
  Forever:
    If <(x position) > 240> then
      Say [TOO FAR RIGHT!] for 0.5 secs
      Set x to 240
    If <(x position) < -240> then
      Say [TOO FAR LEFT!] for 0.5 secs
      Set x to -240

// Debug: Frame counter
When green flag clicked:
  Set [frames] to 0
  Forever:
    Change [frames] by 1
    If <(frames) mod 30 = 0> then
      Say (join [FPS: ] ((frames) / (timer))) for 0.1 secs
```

### Typowe problemy
| Problem | Przyczyna | Rozwiązanie |
|--------|-------|---------|
| Sprite nie odpowiada | Brak kapelusza wydarzenia | Dodaj „Po kliknięciu zielonej flagi” lub inne wydarzenie |
| Klon nie działa | Klon utworzony, ale nie pokazany | Dodaj blok „Pokaż” po „Kiedy zaczynam jako klon” |
| Zmienna współdzielona pomiędzy duszkami | Zamieszanie zmiennych globalnych i lokalnych | Użyj opcji „Tylko dla tego duszka” |
| Transmisja nie została odebrana | Zła nazwa wiadomości | Sprawdź, czy nazwy transmisji i odbioru są dokładnie zgodne |
| Zamrożenie nieskończonej pętli | „Na zawsze” bez czekania | Dodaj małe bloki „Czekaj” w ciasnych pętlach |
---

## Interoperacyjność
### Rozszerzenia sprzętowe
Scratch może łączyć się ze sprzętem fizycznym poprzez rozszerzenia:
```
Supported Hardware:
├── micro:bit
│   ├── Accelerometer/gyroscope input
│   ├── LED matrix display output
│   ├── Button input
│   └── Radio communication
├── LEGO Education
│   ├── SPIKE Prime / Essential
│   ├── EV3 (older)
│   └── Motors and sensors
├── Makey Makey
│   ├── Capacitive touch input
│   ├── Any conductive object as button
│   └── USB connection (no drivers needed)
├── Arduino (via extensions)
│   ├── GPIO pin control
│   ├── Sensor readings
│   └── Motor control
└── Camera / Webcam
    ├── Video sensing (motion detection)
    └── Face detection (via extensions)
```

### API rozszerzeń Scratch (rozszerzenia niestandardowe)
```javascript
// Custom Scratch extension (JavaScript)
class MyExtension {
  getInfo() {
    return {
      id: 'myExtension',
      name: 'My Extension',
      blocks: [
        {
          opcode: 'greet',
          blockType: Scratch.BlockType.REPORTER,
          text: 'greet [NAME]',
          arguments: {
            NAME: { type: Scratch.ArgumentType.STRING, defaultValue: 'World' }
          }
        },
        {
          opcode: 'addNumbers',
          blockType: Scratch.BlockType.REPORTER,
          text: '[A] + [B]',
          arguments: {
            A: { type: Scratch.ArgumentType.NUMBER, defaultValue: 1 },
            B: { type: Scratch.ArgumentType.NUMBER, defaultValue: 2 }
          }
        }
      ]
    };
  }
  greet(args) { return 'Hello, ' + args.NAME + '!'; }
  addNumbers(args) { return Number(args.A) + Number(args.B); }
}
Scratch.extensions.register(new MyExtension());
```
---

## Wzorce projektowe
### Wzór 1: Ruch platformowy
```
When green flag clicked:
  Set [gravity] to -1
  Set [velocity_y] to 0
  Set [speed] to 5
  Set [is_jumping] to false
  Forever:
    // Horizontal movement
    If <key [right arrow] pressed?> then
      Change x by (speed)
    If <key [left arrow] pressed?> then
      Change x by ((speed) * -1)
    // Jumping
    If <key [space] pressed?> then
      If <(is_jumping) = false> then
        Set [velocity_y] to 12
        Set [is_jumping] to true
    // Gravity
    Change [velocity_y] by (gravity)
    Change y by (velocity_y)
    // Ground collision
    If <(y position) < -100> then
      Set y to -100
      Set [velocity_y] to 0
      Set [is_jumping] to false
```

### Wzór 2: Przewijane tło
```
// Background sprite scrolls left to create side-scrolling effect
When green flag clicked:
  Forever:
    Change x by -5
    If <(x position) < -240> then
      Set x to 240

// Or use two copies for seamless scrolling
When I start as a clone:
  Forever:
    Change x by -5
    If <(x position) < -480> then
      Change x by 960
```

### Wzór 3: Podążanie za duszkiem (ściganie AI)
```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### Wzorzec 4: System inwentaryzacji z listami
```
When green flag clicked:
  Delete all of [inventory]
  Add [Sword] to [inventory]
  Add [Shield] to [inventory]
  Add [Potion] to [inventory]

When key [i] pressed:
  // Display inventory
  Set [display] to []
  Set [idx] to 1
  Repeat (length of [inventory]):
    Set [display] to (join (display) (join (item (idx) of [inventory]) [
]))
    Change [idx] by 1
  Say (display) for 3 secs

When key [1] pressed:
  // Use first item
  If <(length of [inventory]) > 0> then
    Set [used_item] to (item 1 of [inventory])
    Delete 1 of [inventory]
    Say (join [Used: ] (used_item)) for 1 secs
```

### Wzorzec 5: Układ cząstek z klonami
```
// Create particles on click
When this sprite clicked:
  Repeat 10:
    Create clone of [Particle]

// Each particle moves randomly and fades
When I start as a clone:
  Go to [mouse-pointer]
  Point in direction (pick random 0 to 360)
  Set [size] to (pick random 20 to 50)
  Set [ghost] to 0
  Show
  Repeat 20:
    Move 5 steps
    Change [ghost] by 5
  Hide
  Delete this clone
```

---

## Wydajność i optymalizacja
### Optymalizacja Sprite'a
| Technika | Wpływ | Opis |
|---------------|--------|------------|
| **Minimalizuj klony** | Wysoki | Każdy klon zużywa pamięć; usuń po zakończeniu |
| **Zmniejsz kostiumy** | Średni | Mniej przełączników kostiumów oznacza mniejsze obciążenie związane z renderowaniem |
| **Użyj opcji „uruchom bez odświeżania ekranu”** | Wysoki | Niestandardowe bloki bez odświeżania ekranu działają szybciej |
| **Ogranicz bloki „powiedz”** | Średni | Dymki powodują narzut renderowania |
| **Unikaj słowa „na zawsze” w każdym duszku** | Średni | Używaj transmisji i wydarzeń zamiast ciągłego odpytywania |
### Zarządzanie klonami
```
// BAD: Creating clones without cleanup
When green flag clicked:
  Forever:
    Create clone of [Enemy]
    Wait 0.1 secs
    // Clones pile up and slow everything down

// GOOD: Limit active clones
When green flag clicked:
  Set [max_enemies] to 10
  Forever:
    If <(enemy_count) < (max_enemies)> then
      Create clone of [Enemy]
      Change [enemy_count] by 1
    Wait 1 secs

When I start as a clone:
  // ... enemy behaviour ...
  // When done:
  Change [enemy_count] by -1
  Delete this clone
```

### Lista kontrolna optymalizacji
| Technika | Wpływ | Opis |
|---------------|--------|------------|
| **Uruchom bez odświeżania ekranu** | Bardzo wysoki | Bloki niestandardowe pomijają renderowanie ze względu na szybkość |
| **Minimalizuj aktywne klony** | Wysoki | Usuń klony, gdy tylko nie będą już potrzebne |
| **Używaj programów oszczędnie** | Średni | Zbyt wiele transmisji na klatkę powoduje opóźnienie |
| **Uprość kostiumy** | Średni | Mniejsze obrazy renderują się szybciej |
| **Operacje na listach skróconych** | Średni | Unikaj skanowania dużych list w każdej klatce |
| **Użyj bloków „czekaj”** | Niski | Zapobiegaj blokowaniu procesora w pętlach wiecznych |
---

## Wdrożenie i użytkowanie w świecie rzeczywistym
### Udostępnianie projektów
```
Deployment Options:
├── Scratch Community (online)
│   ├── Upload to scratch.mit.edu
│   ├── Share with community
│   └── Allow remixing by others
├── Local sharing
│   ├── Save as .sb3 file
│   ├── Share via email/USB/cloud
│   └── Open in Scratch Desktop or web editor
├── Embedding
│   ├── Embed on websites via iframe
│   └── <iframe src="https://scratch.mit.edu/projects/embed/PROJECT_ID">
└── Standalone apps (via third-party tools)
    ├── TurboWarp (desktop packaging)
    ├── Electron-based wrappers
    └── HTML5 export tools
```

### Rzeczywiste wykorzystanie edukacyjne
| Kontekst | Jak używany jest Scratch | Skala |
|--------|---------|-------|
| **Szkoły K-12** | Wprowadzenie do programowania na zajęciach CS | Używany w ponad 190 krajach |
| **Kluby kodowania** | Klub Scratcha / Warsztaty CoderDojo | Ponad 3000 klubów na całym świecie |
| **Biblioteki** | Programy pozaszkolne | Systemy bibliotek publicznych |
| **Nauka w domu** | Samodzielna edukacja w zakresie programowania | Miliony uczniów uczących się w domu |
| **Uniwersytet CS0** | Inne niż główne kursy wprowadzające CS | Uniwersyteckie programy pomostowe |
| **Dostępność** | Nauczanie programowania osób niewidomych | Obsługa czytnika ekranu |
| **Terapia** | Rozwój umiejętności poznawczych i motorycznych | Terapia zajęciowa |
### Scratch w badaniach edukacyjnych
Badania wykazały, że Scratch skutecznie uczy:
- **Myślenie sekwencyjne**: Dzielenie problemów na uporządkowane kroki
- **Umiejętności debugowania**: Znajdowanie i naprawianie błędów w logice
- **Ekspresja twórcza**: Łączenie sztuki, muzyki i programowania
- **Współpraca**: Remiksowanie i opracowywanie projektów innych osób
- **Trwałość**: Powtarzanie projektów w celu ich ulepszenia
---

## Przejście od zera
Po nauczeniu się języka Scratch typowe kolejne kroki obejmują:
| Następny język | Dlaczego |
|-------------|-----|
| **Pyton** | Najbardziej naturalne przejście — czytelna składnia, podobne koncepcje logiczne |
| **JavaScript** | Jeśli interesujesz się internetem/grami — natychmiastowa informacja wizualna |
| **Lua (przez Roblox/Love2D)** | Jeśli jesteś zainteresowany tworzeniem gier |
| **Wynalazca aplikacji** | Bloki wizualne dla aplikacji na Androida (ten sam rodowód MIT) |
| **Blokowo** | Biblioteka programowania wizualnego Google (podobne koncepcje) |
### Mapowanie koncepcji: Scratch do Pythona
| Koncepcja Scratcha | Odpowiednik Pythona |
|----------------|--------------------------------|
| `set [x] to 0`| `x = 0`|
| `change [x] by 1`| `x += 1`|
| `repeat 10`| `for i in range(10):`|
| `forever`| `while True:`|
| `if ... then`| `if ...:`|
| `broadcast [msg]`| Wywołanie funkcji lub system zdarzeń |
| `My Blocks`| `def function():`|
| `list`| `list = []`|
| `item 1 of [list]`| `list[0]`(indeks 0!) |
| `length of [list]`| `len(list)`|
---

## Kiedy używać Scratcha
| Scenariusz | Dlaczego Scratch | Lepsza alternatywa |
|---------|-----------|--------------------------------|
| Nauczanie dzieci (8-16 lat) kodowania | Zaprojektowany specjalnie do tego | — |
| Przedstawiamy myślenie obliczeniowe | Wizualnie, bez błędów składniowych | — |
| Warsztaty szkolne / kluby kodowania | Bezpłatny, oparty na przeglądarce, bez konfiguracji | — |
| Wizualne prototypowanie pomysłów na gry | Szybka iteracja | — |
| Rozwój zawodowy | Nie do tego przeznaczony | Python, JavaScript, dowolny język tekstowy |
| Edukacja CS na poziomie uniwersyteckim | Zbyt proste | Python, Java, C |
---

## Streszczenie
Scratch nie jest językiem programowania w tradycyjnym sensie – jest środowiskiem do nauki. Jego geniusz polega na usuwaniu wszelkich barier pomiędzy dzieckiem a radością tworzenia czegoś interaktywnego. Koncentrując się na koncepcjach, a nie na składni, Scratch uczy podstaw programowania, które można przenieść na dowolny język. Jeśli chodzi o wprowadzanie programowania dla młodych uczniów, Scratch jest złotym standardem.