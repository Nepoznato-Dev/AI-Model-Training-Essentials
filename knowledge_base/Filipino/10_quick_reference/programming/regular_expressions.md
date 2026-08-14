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
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to programming/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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

# Regular Expressions Cheat Sheet
Ang mga regular na expression (regex) ay mga pattern para sa pagtutugma ng teksto. Ginagamit ang mga ito kahit saan — maghanap at palitan, pagpapatunay ng input, pag-parse ng log, pagkuha ng data, at higit pa. Ito ay isang praktikal na sanggunian, hindi isang aklat-aralin.
---

## Core Syntax
### Mga Literal na Tauhan
Karamihan sa mga character ay tumutugma sa kanilang sarili:`a`tumutugma sa "a",`cat`tumutugma sa "pusa".
### Mga Espesyal na Character (Metacharacter)
Ang mga ito ay may espesyal na kahulugan at dapat na i-escape gamit ang`\`upang literal na tumugma:
| Tauhan | Ibig sabihin |
|-----------|---------|
| `.`| Anumang character maliban sa newline |
| `^`| Simula ng string (o linya sa multiline mode) |
| `$`| Katapusan ng string (o linya sa multiline mode) |
| `*`| 0 o higit pa sa naunang |
| `+`| 1 o higit pa sa naunang |
| `?`| 0 o 1 sa naunang (ginagawa ang mga quantifier na tamad sa`*?`,`+?`) |
| `\|`| Paghahalili (OR) |
| `()`| Pagpapangkat at pagkuha |
| `[]`| Klase ng karakter |
| `{}`| Saklaw ng quantifier |
| `\`| Makatakas na character |
---

## Mga Klase ng Character
| Pattern | Mga tugma |
|---------|---------|
| `[abc]`| a, b, o c |
| `[a-z]`| Anumang maliliit na titik |
| `[A-Z]`| Anumang malalaking titik |
| `[0-9]`| Anumang digit |
| `[a-zA-Z]`| Anumang liham |
| `[^abc]`| Anuman maliban sa a, b, o c (negated class) |
| `[a-z0-9_]`| Mga maliliit na titik, digit, underscore |
### Mga Klase ng Shorthand
| Pattern | Katumbas | Mga tugma |
|---------|-----------|---------|
| `\d`| `[0-9]`| Digit |
| `\D`| `[^0-9]`| Non-digit |
| `\w`| `[a-zA-Z0-9_]`| Tauhan ng salita |
| `\W`| `[^a-zA-Z0-9_]`| Hindi salita na character |
| `\s`| `[ \t\n\r\f]`| Whitespace (espasyo, tab, bagong linya, atbp.) |
| `\S`| `[^\s]`| Non-whitespace |
---

## Mga Quantifier
| Quantifier | Ibig sabihin | Halimbawa | Mga tugma |
|-----------|---------|---------|---------|
| `*`| 0 o higit pa | `ab*c`| ac, abc, abbc, abbbc |
| `+`| 1 o higit pa | `ab+c`| abc, abbc, abbbc |
| `?`| 0 o 1 | `ab?c`| ac, abc |
| `{n}`| Eksakto n | `a{3}`| aaa |
| `{n,}`| n o higit pa | `a{2,}`| aa, aaa, aaaa... |
| `{n,m}`| Sa pagitan ng n at m | `a{2,4}`| aa, aaa, aaaa |
### Matakaw vs Tamad
Bilang default, ang mga quantifier ay **matakaw** (magtugma hangga't maaari). Magdagdag ng`?`upang gawin silang **tamad** (magtugma nang kaunti hangga't maaari).
| Pattern | String | Matakaw na Tugma | Tamad na Tugma |
|---------|--------|-------------|------------|
| `<.*>`| `<b>hi</b>`| `<b>hi</b>`(buong string) |  Magkahiwalay ang`<b>`at`</b>`|
| `<.+?>`| `<b>hi</b>`| — | `<b>`,`</b>`|
---

## Mga anchor
| Anchor | Ibig sabihin |
|--------|---------|
| `^`| Simula ng string |
| `$`| Katapusan ng string |
| `\b`| Hangganan ng salita |
| `\B`| Walang salita na hangganan |
| `(?=...)`| Positibong tumingin sa unahan |
| `(?!...)`| Negatibong tingin sa unahan |
| `(?<=...)`| Positibong tingin sa likod |
| `(?<!...)`| Negatibong tingin sa likod |
**Halimbawa ng hangganan ng salita**: Ang`\bcat\b`ay tumutugma sa "pusa" sa "the cat sat" ngunit hindi sa "category".
---

## Mga Grupo at Pagkuha
| Syntax | Paglalarawan | Halimbawa |
|--------|-------------|---------|
| `(abc)`| Kinukuha ang pangkat | I-extract ang "abc" mula sa isang tugma |
| `(?:abc)`| Grupong hindi kumukuha | Magpangkat nang hindi kumukuha |
| `\1`| Backreference sa pangkat 1 | `(abc)\1`tumutugma sa "abcabc" |
| `(?<name>abc)`| Pinangalanang pangkat ng pagkuha | `(?<year>\d{4})`|
| `a(?=b)`| Positibong tumingin sa unahan | Itugma ang "a" lamang kung sinusundan ng "b" |
| `a(?!b)`| Negatibong tingin sa unahan | Itugma ang "a" lamang kung HINDI sinusundan ng "b" |
---

## Mga Karaniwang Pattern
### Pagpapatunay
| Pattern | Mga tugma | Mga Tala |
|---------|---------|-------|
| `^\d{5}$`| US ZIP code | Eksaktong 5 digit |
| `^\d{5}(-\d{4})?$`| US ZIP+4 | 5 digit, opsyonal -4 |
| `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`| Email address | Pinasimple; Ang RFC 5322 ay mas kumplikado |
| `^https?:\/\/`| Nagsisimula ang URL sa http:// o https:// | |
| `^\+?[1-9]\d{1,14}$`| Numero ng telepono (E.164 format) | International na pamantayan |
| `^(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)$`| IPv4 address | |
| `^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$`| IPv6 address | Pinasimple |
| `^\d{3}-\d{2}-\d{4}$`| US SSN format | XXX-XX-XXXX |
| `^[A-Z]{1,2}\d{1,4}\s?\d[A-Z]{2}$`| UK postcode | Pinasimple |
### Pagkuha
| Pattern | Mga extract |
|---------|----------|
| `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b`| Mga email address mula sa text |
| `https?:\/\/[^\s]+`| Mga URL mula sa text |
| `\b\d{1,3}(\.\d{1,3}){3}\b`| Mga IPv4 address mula sa text |
| `\d{4}-\d{2}-\d{2}`| Mga petsa ng ISO (YYYY-MM-DD) |
| `#[0-9a-fA-F]{6}\b`| Mga code ng kulay ng hex |
| `\$\d+(?:\.\d{2})?`| Mga halaga ng dolyar |
### Pagproseso ng Teksto
| Pattern | Layunin |
|---------|---------|
| `\s+`| Itugma ang isa o higit pang mga whitespace na character (i-collapse ang mga puwang) |
| `\r?\n`| Match line breaks (pangasiwaan ang parehong \n at \r\n) |
| `^.*$`| Itugma ang isang buong linya |
| `<[^>]+>`| Itugma ang mga HTML/XML tags (pinasimple; huwag i-parse ang HTML gamit ang regex) |
| `["']([^"']*)["']`| Itugma ang mga naka-quote na string |
---

## Mga Flag / Modifier
| Bandila | Ibig sabihin | Epekto |
|------|---------|--------|
| `i`| Case-insensitive | `cat`tumutugma sa "Cat", "CAT", "cAt" |
| `g`| Global | Hanapin ang lahat ng mga tugma, hindi lamang ang unang |
| `m`| Multiline |  Ang`^`at`$`ay tumutugma sa mga hangganan ng linya, hindi lamang string |
| `s`| Dotall |  Ang`.`ay tumutugma sa mga bagong linyang character |
| `x`| Pinalawak | Huwag pansinin ang whitespace at payagan ang mga komento sa pattern |
---

## Paggamit na Partikular sa Wika
### Sawa
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

### grep / sed / awk (Command Line)
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

## Mga Karaniwang Pagkakamali
| Pagkakamali | Problema | Ayusin |
|---------|---------|-----|
| `.*`ay sakim | Masyadong maraming tugma | Gamitin ang`.*?`para sa tamad na pagtutugma |
| Nakakalimutang tumakas`.`|  Ang`file.txt`ay tumutugma din sa`fileXtxt`| Gamitin ang`file\.txt`|
| Hindi ini-angkla ang mga pattern ng pagpapatunay | `^\d{3}$`na naka-embed sa mas mahabang string | Gamitin ang`^`at`$`|
| Klase ng character sa loob ng`[]`| `[\d+]`tumutugma`\`,`d`,`+`— hindi mga digit | Gamitin ang`\d`sa labas ng`[]`, o`[0-9]`|
| Pag-parse ng HTML gamit ang regex | Ang HTML ay hindi isang regular na wika | Gumamit ng HTML parser para sa tunay na pag-parse; regex OK para sa simpleng pagkuha |
| Sakuna na backtracking | Ang mga nested quantifier tulad ng`(a+)+`ay maaaring mag-hang | Pasimplehin ang pattern; gumamit ng mga atomic group |
| Hindi pagsubok sa mga edge na kaso | Gumagana ang pattern sa masayang landas, nabigo sa gilid | Subukan gamit ang mga walang laman na string, napakahabang input, mga espesyal na character |
---

## Mga Tool sa Pagsubok
| Tool | Uri | URL |
|------|------|-----|
| **Regex101** | Web | regex101.com — real-time na pagtutugma sa paliwanag |
| **RegExr** | Web | regexr.com — interactive na pagsubok gamit ang cheatsheet |
| **regex-crossword** | Laro | regexcrossword.com — matuto sa pamamagitan ng paglutas ng mga puzzle |
---

## Buod
Ang Regex ay isang tool para sa pagtutugma ng pattern sa text. Magsimula nang simple — karamihan sa mga real-world na pattern ay kumbinasyon lamang ng mga klase ng character, quantifier, anchor, at grupo. Gumamit ng tool sa pagsubok upang i-verify ang iyong mga pattern bago ilagay ang mga ito sa code. At tandaan: kung nagiging kumplikado na ang iyong regex na hindi mo na ito mabasa, malamang na oras na para gumamit na lang ng tamang parser.