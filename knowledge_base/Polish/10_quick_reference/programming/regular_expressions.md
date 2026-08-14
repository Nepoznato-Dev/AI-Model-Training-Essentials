<!--
---
# Metadata
title: "Regular Expressions Cheat Sheet"
description: "Regex syntax, common patterns, language-specific usage"
category: "Quick Reference"
subcategory: "Programming"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to programming/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [regular, expressions, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "11 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Ściągawka dotycząca wyrażeń regularnych
Wyrażenia regularne (regex) to wzorce dopasowywania tekstu. Są używane wszędzie — wyszukiwanie i zamiana, sprawdzanie poprawności danych wejściowych, analizowanie dzienników, ekstrakcja danych i nie tylko. Jest to podręcznik praktyczny, a nie podręcznik.
---

## Podstawowa składnia
### Znaki dosłowne
Większość znaków pasuje do siebie:`a`pasuje do „a”,`cat`pasuje do „cat”.
### Znaki specjalne (metaznaki)
Mają one specjalne znaczenie i należy je poprzedzić `\`, aby dosłownie dopasować:
| Charakter | Znaczenie |
|---------------|--------|
| `.`| Dowolny znak z wyjątkiem nowej linii |
| `^`| Początek ciągu (lub linii w trybie wielowierszowym) |
| `$`| Koniec ciągu (lub linii w trybie wielowierszowym) |
| `*`| 0 lub więcej z poprzednich |
| `+`| 1 lub więcej z poprzednich |
| `?`| 0 lub 1 z poprzedniego (sprawia, że ​​kwantyfikatory są leniwe w przypadku`*?`,`+?`) |
| `\|`| Alternacja (OR) |
| `()`| Grupowanie i przechwytywanie |
| `[]`| Klasa postaci |
| `{}`| Zakres kwantyfikatora |
| `\`| Znak ucieczki |
---

## Klasy postaci
| Wzór | mecze |
|-------------|--------|
| `[abc]`| a, b lub c |
| `[a-z]`| Dowolna mała litera |
| `[A-Z]`| Dowolna wielka litera |
| `[0-9]`| Dowolna cyfra |
| `[a-zA-Z]`| Dowolna litera |
| `[^abc]`| Wszystko oprócz a, b lub c (klasa zanegowana) |
| `[a-z0-9_]`| Małe litery, cyfry, podkreślenie |
### Klasy stenograficzne
| Wzór | Odpowiednik | mecze |
|--------|-----------|--------|
| `\d`| `[0-9]`| Cyfra |
| `\D`| `[^0-9]`| Niecyfrowe |
| `\w`| `[a-zA-Z0-9_]`| Znak słowny |
| `\W`| `[^a-zA-Z0-9_]`| Znak inny niż słowo |
| `\s`| `[ \t\n\r\f]`| Białe znaki (spacja, tabulator, nowa linia itp.) |
| `\S`| `[^\s]`| Bez białych znaków |
---

## Kwantyfikatory
| Kwantyfikator | Znaczenie | Przykład | mecze |
|----------|---------|---------|---------|
| `*`| 0 lub więcej | `ab*c`| ac, abc, abbc, abbbc |
| `+`| 1 lub więcej | `ab+c`| abc, abbc, abbc |
| `?`| 0 lub 1 | `ab?c`| ac, abc |
| `{n}`| Dokładnie n | `a{3}`| aaa |
| `{n,}`| n lub więcej | `a{2,}`| aa, aaa, aaaa... |
| `{n,m}`| Między n i m | `a{2,4}`| aa, aaa, aaaa |
### Chciwy kontra leniwy
Domyślnie kwantyfikatory są **zachłanne** (dopasowują jak najwięcej). Dodaj `?`, aby uczynić je **leniwymi** (dopasuj jak najmniej).
| Wzór | Ciąg | Chciwy mecz | Leniwy mecz |
|--------|--------|------------|------------|
| `<.*>`| `<b>hi</b>`| `<b>hi</b>`(cały ciąg znaków) | `<b>`i`</b>`oddzielnie |
| `<.+?>`| `<b>hi</b>`| — | `<b>`,`</b>`|
---

## Kotwice
| Kotwica | Znaczenie |
|------------|--------|
| `^`| Początek ciągu |
| `$`| Koniec ciągu |
| `\b`| Granica słów |
| `\B`| Granica niebędąca słowem |
| `(?=...)`| Pozytywne spojrzenie w przyszłość |
| `(?!...)`| Negatywne spojrzenie w przyszłość |
| `(?<=...)`| Pozytywne spojrzenie za siebie |
| `(?<!...)`| Negatywne spojrzenie w przeszłość |
**Przykład granicy słowa**:`\bcat\b`dopasowuje „kot” w „kot siedział”, ale nie w „kategorii”.
---

## Grupy i przechwytywanie
| Składnia | Opis | Przykład |
|------------|------------|--------|
| `(abc)`| Grupa przechwytująca | Wyodrębnij „abc” z dopasowania |
| `(?:abc)`| Grupa nieprzechwytująca | Grupuj bez przechwytywania |
| `\1`| Odniesienie wsteczne do grupy 1 | `(abc)\1`pasuje do „abcabc” |
| `(?<name>abc)`| Nazwana grupa przechwytująca | `(?<year>\d{4})`|
| `a(?=b)`| Pozytywne spojrzenie w przyszłość | Dopasuj „a” tylko wtedy, gdy następuje po nim „b” |
| `a(?!b)`| Negatywne spojrzenie w przyszłość | Dopasuj „a” tylko wtedy, gdy NIE następuje po nim „b” |
---

## Typowe wzorce
### Walidacja
| Wzór | mecze | Notatki |
|--------|---------|-------|
| `^\d{5}$`| Kod pocztowy w USA | Dokładnie 5 cyfr |
| `^\d{5}(-\d{4})?$`| Kod pocztowy USA+4 | 5 cyfr, opcjonalnie -4 |
| `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`| Adres e-mail | Uproszczony; RFC 5322 jest znacznie bardziej złożony |
| `^https?:\/\/`| Adres URL zaczyna się od http:// lub https:// | |
| `^\+?[1-9]\d{1,14}$`| Numer telefonu (format E.164) | Międzynarodowy standard |
| `^(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)$`| Adres IPv4 | |
| `^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$`| Adres IPv6 | Uproszczone |
| `^\d{3}-\d{2}-\d{4}$`| Format amerykańskiego numeru SSN | XXX-XX-XXXX |
| `^[A-Z]{1,2}\d{1,4}\s?\d[A-Z]{2}$`| Kod pocztowy w Wielkiej Brytanii | Uproszczone |
### Ekstrakcja
| Wzór | Ekstrakty |
|--------|----------|
| `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b`| Adresy e-mail z tekstu |
| `https?:\/\/[^\s]+`| Adresy URL z tekstu |
| `\b\d{1,3}(\.\d{1,3}){3}\b`| Adresy IPv4 z tekstu |
| `\d{4}-\d{2}-\d{2}`| Daty ISO (RRRR-MM-DD) |
| `#[0-9a-fA-F]{6}\b`| Kody kolorów szesnastkowych |
| `\$\d+(?:\.\d{2})?`| Kwoty w dolarach |
### Przetwarzanie tekstu
| Wzór | Cel |
|-------------|--------|
| `\s+`| Dopasuj jeden lub więcej białych znaków (zwiń spacje) |
| `\r?\n`| Podziały linii dopasowania (obsługuje zarówno \n, jak i \r\n) |
| `^.*$`| Dopasuj całą linię |
| `<[^>]+>`| Dopasuj tagi HTML/XML (uproszczone; nie analizuj HTML za pomocą wyrażeń regularnych) |
| `["']([^"']*)["']`| Dopasuj cytowane ciągi znaków |
---

## Flagi/Modyfikatory
| Flaga | Znaczenie | Efekt |
|------|---------|--------|
| `i`| Wielkość liter nie jest uwzględniana | `cat`odpowiada „Cat”, „CAT”, „cAt” |
| `g`| Globalny | Znajdź wszystkie dopasowania, nie tylko pierwsze |
| `m`| Multilinia | `^`i`$`dopasowują granice linii, a nie tylko ciąg znaków |
| `s`| Dotal | `.`dopasowuje znaki nowej linii |
| `x`| Rozszerzony | Ignoruj ​​białe znaki i zezwalaj na komentarze we wzorcu |
---

## Użycie specyficzne dla języka
### Pythona
```python
import re

text = "Contact us at info@example.com or support@test.org"

# Find all emails
emails = re.findall(r'\b[\w.+-]+@[\w.-]+\.\w{2,}\b', text)
# ['info@example.com', 'support@test.org']

# Search for first match
match = re.search(r'\d{4}-\d{2}-\d{2}', "Date: 2024-03-15")
if match:
    print(match.group())  # "2024-03-15"

# Replace
cleaned = re.sub(r'\s+', '', "hello  world")  # "helloworld"

# Named groups
pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
m = re.match(pattern, "2024-03-15")
print(m.group('year'))  # "2024"

# Compile for reuse
email_re = re.compile(r'\b[\w.+-]+@[\w.-]+\.\w{2,}\b')
results = email_re.findall(text)
```

### JavaScript
```javascript
const text = "Contact us at info@example.com or support@test.org";

// Find all matches
const emails = text.match(/[\w.+-]+@[\w.-]+\.\w{2,}/g);
// ['info@example.com', 'support@test.org']

// Test if pattern matches
const hasDate = /\d{4}-\d{2}-\d{2}/.test("Date: 2024-03-15");  // true

// Replace
const cleaned = "hello  world".replace(/\s+/g, '');  // "helloworld"

// Capture groups
const match = /(\d{4})-(\d{2})-(\d{2})/.exec("2024-03-15");
// match[1] = "2024", match[2] = "03", match[3] = "15"

// Named groups
const dateRe = /(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/;
const m = dateRe.exec("2024-03-15");
console.log(m.groups.year);  // "2024"
```

### grep / sed / awk (Wiersz poleceń)
```bash
# grep: find lines matching a pattern
grep -E '[0-9]{4}-[0-9]{2}-[0-9]{2}' logfile.txt       # Find dates
grep -iE '\b[\w.+-]+@[\w.-]+\.\w{2,}\b' file.txt       # Find emails (case-insensitive)
grep -c 'ERROR' logfile.txt                              # Count matching lines
grep -rn 'TODO' src/                                     # Recursive with line numbers

# sed: find and replace
sed 's/old/new/g' file.txt                               # Replace all occurrences
sed 's/[[:space:]]\+/ /g' file.txt                       # Collapse whitespace
sed -n '/ERROR/p' logfile.txt                            # Print only matching lines
sed 's/^/# /' file.txt                                   # Prepend "# " to each line

# awk: field-based processing
awk '{print $1, $3}' file.txt                            # Print columns 1 and 3
awk -F',' '{print $2}' data.csv                          # CSV: print 2nd column
awk '/ERROR/ {count++} END {print count}' logfile.txt    # Count ERROR lines
awk 'length($0) > 80' file.txt                           # Lines longer than 80 chars
```

---

## Typowe błędy
| Błąd | Problem | Napraw |
|--------|---------|-----|
| `.*`jest zachłanny | Pasuje za dużo | Użyj`.*?`do leniwego dopasowywania |
| Zapominanie o ucieczce z`.`| `file.txt`pasuje również do`fileXtxt`| Użyj`file\.txt`|
| Brak zakotwiczenia wzorców walidacji | `^\d{3}$`osadzony w dłuższym łańcuchu | Użyj`^`i`$`|
| Klasa postaci wewnątrz`[]`| `[\d+]`odpowiada`\`,`d`,`+`— nie cyfrom | Użyj`\d`poza`[]`lub`[0-9]`|
| Parsowanie HTML za pomocą wyrażenia regularnego | HTML nie jest zwykłym językiem | Użyj parsera HTML do prawdziwego analizowania; regex OK dla prostej ekstrakcji |
| Katastrofalne cofanie się | Zagnieżdżone kwantyfikatory, takie jak `(a+)+`, mogą się zawiesić | Uprość wzór; użyj grup atomowych |
| Nie testuję przypadków Edge | Wzór działa na szczęśliwej ścieżce, zawodzi na krawędzi | Test z pustymi ciągami znaków, bardzo długimi danymi wejściowymi, znakami specjalnymi |
---

## Narzędzia do testowania
| Narzędzie | Wpisz | Adres URL |
|------|------|---------|
| **Regex101** | Sieć | regex101.com — dopasowywanie w czasie rzeczywistym z wyjaśnieniem |
| **RegExr** | Sieć | regexr.com — interaktywne testowanie z ściągawką |
| **krzyżówka regex** | Gra | regexcrossword.com — ucz się rozwiązując łamigłówki |
---

## Streszczenie
Regex to narzędzie do dopasowywania wzorców w tekście. Zacznij od prostego — większość wzorców ze świata rzeczywistego to po prostu kombinacja klas znaków, kwantyfikatorów, kotwic i grup. Użyj narzędzia testowego, aby zweryfikować wzorce przed umieszczeniem ich w kodzie. I pamiętaj: jeśli wyrażenie regularne staje się tak skomplikowane, że nie można go odczytać, prawdopodobnie nadszedł czas, aby zamiast tego użyć odpowiedniego analizatora składni.