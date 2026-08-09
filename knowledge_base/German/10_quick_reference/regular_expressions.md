---
# Metadata
title: "Regular Expressions Cheat Sheet"
description: "Regex syntax, common patterns, language-specific usage"
category: "Quick Reference"
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

# Spickzettel für reguläre Ausdrücke
Reguläre Ausdrücke (Regex) sind Muster zum Abgleichen von Text. Sie werden überall eingesetzt – beim Suchen und Ersetzen, bei der Eingabevalidierung, beim Parsen von Protokollen, bei der Datenextraktion und mehr. Dies ist eine praktische Referenz, kein Lehrbuch.
---

## Kernsyntax
### Literale Zeichen
Die meisten Zeichen stimmen mit sich selbst überein:`a`entspricht „a“,`cat`entspricht „cat“.
### Sonderzeichen (Metazeichen)
Diese haben eine besondere Bedeutung und müssen mit`\`maskiert werden, damit sie wörtlich übereinstimmen:
| Charakter | Bedeutung |
|-----------|---------|
| `.`| Beliebiges Zeichen außer Newline |
| `^`| Beginn der Zeichenfolge (oder Zeile im mehrzeiligen Modus) |
| `$`| Ende der Zeichenfolge (oder Zeile im mehrzeiligen Modus) |
| `*`| 0 oder mehr der vorangehenden |
| `+`| 1 oder mehrere der vorangehenden |
| `?`| 0 oder 1 des Vorhergehenden (macht Quantifizierer lazy mit`*?`,`+?`) |
| `\|`| Wechsel (ODER) |
| `()`| Gruppieren und Erfassen |
| `[]`| Zeichenklasse |
| `{}`| Quantifiziererbereich |
| `\`| Escape-Zeichen |
---

## Zeichenklassen
| Muster | Übereinstimmungen |
|---------|---------|
| `[abc]`| a, b oder c |
| `[a-z]`| Beliebiger Kleinbuchstabe |
| `[A-Z]`| Beliebiger Großbuchstabe |
| `[0-9]`| Beliebige Ziffer |
| `[a-zA-Z]`| Jeder Buchstabe |
| `[^abc]`| Alles außer a, b oder c (negierte Klasse) |
| `[a-z0-9_]`| Kleinbuchstaben, Ziffern, Unterstrich |
### Kurzschriftklassen
| Muster | Äquivalent | Übereinstimmungen |
|---------|-----------|---------|
| `\d`| `[0-9]`| Ziffer |
| `\D`| `[^0-9]`| Nicht-stellige |
| `\w`| `[a-zA-Z0-9_]`| Wortzeichen |
| `\W`| `[^a-zA-Z0-9_]`| Nicht-Wort-Zeichen |
| `\s`| `[ \t\n\r\f]`| Leerzeichen (Leerzeichen, Tabulator, Zeilenumbruch usw.) |
| `\S`| `[^\s]`| Nicht-Leerzeichen |
---

## Quantifizierer
| Quantifizierer | Bedeutung | Beispiel | Übereinstimmungen |
|-----------|---------|---------|---------|
| `*`| 0 oder mehr | `ab*c`| ac, abc, abbc, abbbc |
| `+`| 1 oder mehr | `ab+c`| abc, abbc, abbbc |
| `?`| 0 oder 1 | `ab?c`| ac, abc |
| `{n}`| Genau n | `a{3}`| aaa |
| `{n,}`| n oder mehr | `a{2,}`| aa, aaa, aaaa... |
| `{n,m}`| Zwischen n und m | `a{2,4}`| aa, aaa, aaaa |
### Gierig gegen Faul
Standardmäßig sind Quantoren **gierig** (sie stimmen so weit wie möglich überein). Fügen Sie`?`hinzu, um sie **faul** zu machen (so wenig Übereinstimmung wie möglich).
| Muster | Zeichenfolge | Gieriges Match | Lazy Match |
|---------|--------|-------------|------------|
| `<.*>`| `<b>hi</b>`| `<b>hi</b>`(gesamte Zeichenfolge) | `<b>`und`</b>`separat |
| `<.+?>`| `<b>hi</b>`| — | `<b>`,`</b>`|
---

## Anker
| Anker | Bedeutung |
|--------|---------|
| `^`| Anfang der Zeichenfolge |
| `$`| Ende der Zeichenfolge |
| `\b`| Wortgrenze |
| `\B`| Nicht-Wortgrenze |
| `(?=...)`| Positiver Ausblick |
| `(?!...)`| Negativer Ausblick |
| `(?<=...)`| Positiver Rückblick |
| `(?<!...)`| Negativer Rückblick |
**Beispiel für eine Wortgrenze**:`\bcat\b`stimmt mit „cat“ in „the cat sat“, aber nicht in „category“ überein.
---

## Gruppen und Erfassung
| Syntax | Beschreibung | Beispiel |
|--------|-------------|---------|
| `(abc)`| Erfassungsgruppe | Extrahieren Sie „abc“ aus einer Übereinstimmung |
| `(?:abc)`| Nicht erfassende Gruppe | Gruppe ohne Erfassung |
| `\1`| Rückverweis auf Gruppe 1 | `(abc)\1`entspricht „abcabc“ |
| `(?<name>abc)`| Benannte Erfassungsgruppe | `(?<year>\d{4})`|
| `a(?=b)`| Positiver Ausblick | Passen Sie „a“ nur an, wenn gefolgt von „b“ |
| `a(?!b)`| Negativer Ausblick | Passen Sie „a“ nur an, wenn NICHT gefolgt von „b“ |
---

## Gemeinsame Muster
### Validierung
| Muster | Übereinstimmungen | Notizen |
|---------|---------|-------|
| `^\d{5}$`| US-Postleitzahl | Genau 5 Ziffern |
| `^\d{5}(-\d{4})?$`| US-PLZ+4 | 5 Ziffern, optional -4 |
| `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`| E-Mail-Adresse | Vereinfacht; RFC 5322 ist weitaus komplexer |
| `^https?:\/\/`| Die URL beginnt mit http:// oder https:// | |
| `^\+?[1-9]\d{1,14}$`| Telefonnummer (E.164-Format) | Internationaler Standard |
| `^(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)$`| IPv4-Adresse | |
| `^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$`| IPv6-Adresse | Vereinfacht |
| `^\d{3}-\d{2}-\d{4}$`| US-SSN-Format | XXX-XX-XXXX |
| `^[A-Z]{1,2}\d{1,4}\s?\d[A-Z]{2}$`| Postleitzahl des Vereinigten Königreichs | Vereinfacht |
### Extraktion
| Muster | Auszüge |
|---------|----------|
| `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b`| E-Mail-Adressen aus Text |
| `https?:\/\/[^\s]+`| URLs aus Text |
| `\b\d{1,3}(\.\d{1,3}){3}\b`| IPv4-Adressen aus Text |
| `\d{4}-\d{2}-\d{2}`| ISO-Daten (JJJJ-MM-TT) |
| `#[0-9a-fA-F]{6}\b`| Hex-Farbcodes |
| `\$\d+(?:\.\d{2})?`| Dollarbeträge |
### Textverarbeitung
| Muster | Zweck |
|---------|---------|
| `\s+`| Entspricht einem oder mehreren Leerzeichen (Leerzeichen reduzieren) |
| `\r?\n`| Zeilenumbrüche abgleichen (behandelt sowohl \n als auch \r\n) |
| `^.*$`| Eine ganze Zeile abgleichen |
| `<[^>]+>`| HTML/XML-Tags abgleichen (vereinfacht; HTML nicht mit Regex analysieren) |
| `["']([^"']*)["']`| Zeichenfolgen in Anführungszeichen abgleichen |
---

## Flags/Modifikatoren
| Flagge | Bedeutung | Wirkung |
|------|---------|--------|
| `i`| Groß-/Kleinschreibung wird nicht beachtet | `cat`entspricht „Cat“, „CAT“, „cAt“ |
| `g`| Global | Alle Treffer finden, nicht nur den ersten |
| `m`| Mehrzeilig | `^`und`$`stimmen mit Zeilengrenzen überein, nicht nur mit der Zeichenfolge |
| `s`| Dotall | `.`entspricht Zeilenumbruchzeichen |
| `x`| Erweitert | Leerzeichen ignorieren und Kommentare im Muster zulassen |
---

## Sprachspezifische Verwendung
### Python
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

### grep / sed / awk (Befehlszeile)
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

## Häufige Fehler
| Fehler | Problem | Fix |
|---------|---------|-----|
| `.*`ist gierig | Stimmt zu viel überein | Verwenden Sie`.*?`für Lazy Matching |
| Vergessen zu entkommen`.`| `file.txt`stimmt auch mit`fileXtxt`überein | Verwenden Sie`file\.txt`|
| Validierungsmuster werden nicht verankert | `^\d{3}$`eingebettet in längere Zeichenfolge | Verwenden Sie`^`und`$`|
| Zeichenklasse innerhalb von`[]`| `[\d+]`entspricht`\`,`d`,`+`– keine Ziffern | Verwenden Sie`\d`außerhalb von`[]`oder`[0-9]`|
| HTML mit Regex analysieren | HTML ist keine reguläre Sprache | Verwenden Sie für echtes Parsen einen HTML-Parser. Regex OK für einfache Extraktion |
| Katastrophaler Rückschritt | Verschachtelte Quantoren wie`(a+)+`können | hängen Vereinfachen Sie das Muster. Atomgruppen verwenden |
| Randfälle werden nicht getestet | Das Muster funktioniert auf dem glücklichen Pfad, schlägt jedoch auf der Kante fehl | Test mit leeren Strings, sehr langer Eingabe, Sonderzeichen |
---

## Testtools
| Werkzeug | Geben Sie | ein URL |
|------|------|-----|
| **Regex101** | Web | regex101.com – Echtzeit-Matching mit Erklärung |
| **RegExr** | Web | regexr.com – interaktives Testen mit Cheatsheet |
| **Regex-Kreuzworträtsel** | Spiel | regexcrossword.com – Lernen durch Lösen von Rätseln |
---

## Zusammenfassung
Regex ist ein Werkzeug zum Mustervergleich im Text. Fangen Sie einfach an – die meisten realen Muster sind nur eine Kombination aus Zeichenklassen, Quantoren, Ankern und Gruppen. Verwenden Sie ein Testtool, um Ihre Muster zu überprüfen, bevor Sie sie in Code einfügen. Und denken Sie daran: Wenn Ihre Regex so komplex wird, dass Sie sie nicht mehr lesen können, ist es wahrscheinlich an der Zeit, stattdessen einen geeigneten Parser zu verwenden.