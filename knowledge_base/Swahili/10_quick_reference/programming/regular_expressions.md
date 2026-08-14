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

# Maneno ya Kawaida Karatasi ya Kudanganya
Semi za kawaida (regex) ni muundo wa maandishi yanayolingana. Zinatumika kila mahali - tafuta na ubadilishe, uthibitishaji wa ingizo, uchanganuzi wa kumbukumbu, uchimbaji wa data, na zaidi. Hii ni kumbukumbu ya vitendo, sio kitabu cha kiada.
---

## Sintaksia ya Msingi
### Herufi Halisi
Wahusika wengi wanalingana wenyewe:`a`inalingana na "a",`cat`inalingana na "paka".
### Herufi Maalum (Metacharacts)
Hizi zina maana maalum na lazima ziepukwe kwa kutumia`\`ili zilingane kihalisi:
| Tabia | Maana |
|-----------|---------|
| `.`| Mhusika yeyote isipokuwa laini mpya |
| `^`| Mwanzo wa kamba (au mstari katika hali ya mistari mingi) |
| `$`| Mwisho wa mfuatano (au mstari katika hali ya mistari mingi) |
| `*`| 0 au zaidi ya yaliyotangulia |
| `+`| 1 au zaidi ya yaliyotangulia |
| `?`| 0 au 1 kati ya yaliyotangulia (hufanya vitathmini kuwa mvivu kwa`*?`,`+?`) |
| `\|`| Mbadala (AU) |
| `()`| Kupanga na kunasa |
| `[]`| Darasa la wahusika |
| `{}`| Masafa ya kiidadi |
| `\`| Escape character |
---

## Madarasa ya Wahusika
| Muundo | Mechi |
|---------|---------|
| `[abc]`| a, b, au c |
| `[a-z]`| Barua yoyote ndogo |
| `[A-Z]`| Herufi kubwa zozote |
| `[0-9]`| Nambari yoyote |
| `[a-zA-Z]`| Barua yoyote |
| `[^abc]`| Chochote isipokuwa a, b, au c (darasa lililopuuzwa) |
| `[a-z0-9_]`| Herufi ndogo, tarakimu, underscore |
### Madarasa ya kutumia njia fupi
| Muundo | Sawa | Mechi |
|---------|-----------|----------|
| `\d`| `[0-9]`| Nambari |
| `\D`| `[^0-9]`| Isiyo na tarakimu |
| `\w`| `[a-zA-Z0-9_]`| Neno tabia |
| `\W`| `[^a-zA-Z0-9_]`| Tabia isiyo ya neno |
| `\s`| `[ \t\n\r\f]`| Whitespace (nafasi, kichupo, mstari mpya, n.k.) |
| `\S`| `[^\s]`| Isiyo ya wazungu |
---

## Vidhibiti
| Kikadiria | Maana | Mfano | Mechi |
|-----------|---------|--------------------|
| `*`| 0 au zaidi | `ab*c`| ac, abc, abbc, abbc |
| `+`| 1 au zaidi | `ab+c`| abc, abbc, abbc |
| `?`| 0 au 1 | `ab?c`| ac, abc |
| `{n}`| Hasa n | `a{3}`| aa |
| `{n,}`| n au zaidi | `a{2,}`| aa, aaa, aaaa... |
| `{n,m}`| Kati ya n na m | `a{2,4}`| aa, aa, aaaa |
### Mchoyo vs Mvivu
Kwa chaguo-msingi, vikadiriaji ni **choyo** (yanalingana kadri inavyowezekana). Ongeza`?`ili kuwafanya **wavivu** (kulingana kidogo iwezekanavyo).
| Muundo | Kamba | Mechi ya Tamaa | Mechi ya Uvivu |
|---------|----------------------|------------|
| `<.*>`| `<b>hi</b>`| `<b>hi</b>`(kamba nzima) | `<b>`na`</b>`tofauti |
| `<.+?>`| `<b>hi</b>`| - | `<b>`,`</b>`|
---

## Nanga
| Nanga | Maana |
|--------|----------|
| `^`| Mwanzo wa kamba |
| `$`| Mwisho wa kamba |
| `\b`| Mpaka wa maneno |
| `\B`| Mpaka usio wa maneno |
| `(?=...)`| Mtazamo mzuri |
| `(?!...)`| Mtazamo hasi |
| `(?<=...)`| Mtazamo mzuri nyuma |
| `(?<!...)`| Mtazamo hasi nyuma |
**Mfano wa mpaka wa maneno**:`\bcat\b`inalingana na "paka" katika "paka alikaa" lakini sio "kategoria".
---

## Vikundi na Ukamataji
| Sintaksia | Maelezo | Mfano |
|--------|-------------|----------|
| `(abc)`| Kikundi cha kunasa | Dondoo "abc" kutoka kwa mechi |
| `(?:abc)`| Kikundi kisichokamata | Kikundi bila kunasa |
| `\1`| Rejea kwa kikundi 1 | `(abc)\1`inalingana na "abcabc" |
| `(?<name>abc)`| Kikundi cha kunasa kilichopewa jina | `(?<year>\d{4})`|
| `a(?=b)`| Mtazamo mzuri | Linganisha "a" ikiwa tu ikifuatiwa na "b" |
| `a(?!b)`| Mtazamo hasi | Linganisha "a" tu ikiwa HAIFUATWI na "b" |
---

## Miundo ya Kawaida
### Uthibitishaji
| Muundo | Mechi | Vidokezo |
|---------|------------------|
| `^\d{5}$`| Msimbo wa posta wa Marekani | Nambari 5 haswa |
| `^\d{5}(-\d{4})?$`| Marekani ZIP+4 | tarakimu 5, hiari -4 |
| `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`| Barua pepe | Imerahisishwa; RFC 5322 ni ngumu zaidi |
| `^https?:\/\/`| URL inaanza na http:// au https:// | |
| `^\+?[1-9]\d{1,14}$`| Nambari ya simu (umbizo la E.164) | Kiwango cha kimataifa |
| `^(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)$`| Anwani ya IPv4 | |
| `^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$`| Anwani ya IPv6 | Iliyorahisishwa |
| `^\d{3}-\d{2}-\d{4}$`| Umbizo la SSN ya Marekani | XXX-XXX-XXXX |
| `^[A-Z]{1,2}\d{1,4}\s?\d[A-Z]{2}$`| Msimbo wa posta wa Uingereza | Iliyorahisishwa |
### Uchimbaji
| Muundo | Dondoo |
|---------|----------|
| `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b`| Anwani za barua pepe kutoka kwa maandishi |
| `https?:\/\/[^\s]+`| URL kutoka kwa maandishi |
| `\b\d{1,3}(\.\d{1,3}){3}\b`| Anwani za IPv4 kutoka kwa maandishi |
| `\d{4}-\d{2}-\d{2}`| Tarehe za ISO (YYYY-MM-DD) |
| `#[0-9a-fA-F]{6}\b`| Nambari za rangi za Hex |
| `\$\d+(?:\.\d{2})?`| Kiasi cha dola |
### Inachakata Maandishi
| Muundo | Kusudi |
|---------|---------|
| `\s+`| Linganisha herufi moja au zaidi za nafasi nyeupe (kunja nafasi) |
| `\r?\n`| Nafasi za mstari wa mechi (hushughulikia \n na \r\n) |
| `^.*$`| Linganisha mstari mzima |
| `<[^>]+>`| Linganisha lebo za HTML/XML (kilichorahisishwa; usichanganye HTML na regex) |
| `["']([^"']*)["']`| Linganisha mifuatano iliyonukuliwa |
---

## Bendera / Virekebishaji
| Bendera | Maana | Athari |
|------|---------|--------|
| `i`| Haijalishi | `cat`inalingana na "Paka", "CAT", "cAt" |
| `g`| Ulimwenguni | Tafuta mechi zote, sio za kwanza tu |
| `m`| Mistari mingi | `^`na`$`mipaka ya mstari wa mechi, si kamba tu |
| `s`| Dokta | `.`inalingana na herufi mpya |
| `x`| Imepanuliwa | Puuza nafasi nyeupe na uruhusu maoni katika muundo |
---

## Matumizi Maalum ya Lugha
### Chatu
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

### grep / sed / awk (Mstari wa Amri)
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

## Makosa ya Kawaida
| Kosa | Tatizo | Rekebisha |
|---------|---------|-----|
| `.*`ni mchoyo | Inalingana sana | Tumia`.*?`kwa kulinganisha uvivu |
| Kusahau kutoroka`.`| `file.txt`inalingana na`fileXtxt`pia | Tumia`file\.txt`|
| Haitegemezi mifumo ya uthibitishaji | `^\d{3}$`iliyopachikwa katika mfuatano mrefu | Tumia`^`na`$`|
| Darasa la wahusika ndani ya`[]`| `[\d+]`mechi`\`,`d`,`+`— si tarakimu | Tumia`\d`nje ya`[]`, au`[0-9]`|
| Kuchanganua HTML na regex | HTML si lugha ya kawaida | Tumia kichanganuzi cha HTML kwa uchanganuzi halisi; regex Sawa kwa uchimbaji rahisi |
| Kurudi nyuma kwa janga | Vipima kipimo vilivyowekwa kama`(a+)+`vinaweza kuning'inia | Rahisisha muundo; tumia vikundi vya atomiki |
| Sio kujaribu visa vya ukingo | Muundo hufanya kazi kwenye njia ya furaha, inashindwa kwa makali | Jaribu kwa mifuatano tupu, ingizo refu sana, herufi maalum |
---

## Zana za Kujaribu
| Zana | Aina | URL |
|------|------|-----|
| **Regex101** | Mtandao | regex101.com - kulinganisha kwa wakati halisi na maelezo |
| **RegExr** | Mtandao | regexr.com - majaribio maingiliano na cheatsheet |
| **regex-crossword** | Mchezo | regexcrossword.com - jifunze kwa kutatua mafumbo |
---

## Muhtasari
Regex ni zana ya kulinganisha muundo katika maandishi. Anza kwa njia rahisi - mifumo mingi ya ulimwengu halisi ni mchanganyiko wa aina za wahusika, vidhibiti, nanga na vikundi. Tumia zana ya majaribio ili kuthibitisha ruwaza zako kabla ya kuziweka katika msimbo. Na kumbuka: ikiwa regex yako inazidi kuwa ngumu kiasi kwamba huwezi kuisoma, labda ni wakati wa kutumia kichanganuzi sahihi badala yake.