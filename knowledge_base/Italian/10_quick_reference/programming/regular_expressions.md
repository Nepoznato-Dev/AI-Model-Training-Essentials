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
# Foglio informativo sulle espressioni regolari
Le espressioni regolari (regex) sono modelli per la corrispondenza del testo. Sono utilizzati ovunque: ricerca e sostituzione, convalida dell'input, analisi dei log, estrazione dei dati e altro ancora. Questo è un riferimento pratico, non un libro di testo.
---

## Sintassi principale
### Caratteri letterali
La maggior parte dei caratteri corrisponde a se stessi:`a`corrisponde a "a",`cat`corrisponde a "cat".
### Caratteri speciali (metacaratteri)
Questi hanno un significato speciale e devono essere codificati con`\`per corrispondere letteralmente:
| Carattere | Significato |
|-----------|---------|
| `.`| Qualsiasi carattere tranne il fine riga |
| `^`| Inizio della stringa (o della riga in modalità multilinea) |
| `$`| Fine della stringa (o della riga in modalità multilinea) |
| `*`| 0 o più dei precedenti |
| `+`| 1 o più dei precedenti |
| `?`| 0 o 1 dei precedenti (rende pigri i quantificatori con`*?`,`+?`) |
| `\|`| Alternanza (OR) |
| `()`| Raggruppamento e acquisizione |
| `[]`| Classe di caratteri |
| `{}`| Intervallo quantificatore |
| `\`| Carattere di fuga |
---

## Classi di caratteri
| Modello | Partite |
|---------|---------|
| `[abc]`| a, b o c |
| `[a-z]`| Qualsiasi lettera minuscola |
| `[A-Z]`| Qualsiasi lettera maiuscola |
| `[0-9]`| Qualsiasi cifra |
| `[a-zA-Z]`| Qualsiasi lettera |
| `[^abc]`| Tutto tranne a, b o c (classe negata) |
| `[a-z0-9_]`| Lettere minuscole, cifre, trattino basso |
### Lezioni di stenografia
| Modello | Equivalente | Partite |
|---------|-----------|---------|
| `\d`| `[0-9]`| Cifra |
| `\D`| `[^0-9]`| Non cifra |
| `\w`| `[a-zA-Z0-9_]`| Carattere della parola |
| `\W`| `[^a-zA-Z0-9_]`| Carattere non verbale |
| `\s`| `[ \t\n\r\f]`| Spazio bianco (spazio, tabulazione, nuova riga, ecc.) |
| `\S`| `[^\s]`| Non spazi bianchi |
---

## Quantificatori
| Quantificatore | Significato | Esempio | Partite |
|-----------|---------|---------|---------|
| `*`| 0 o più | `ab*c`| ac, abc, abbc, abbbc |
| `+`| 1 o più | `ab+c`| abc, abbc, abbbc |
| `?`| 0 o 1 | `ab?c`| ac, abc |
| `{n}`| Esattamente n | `a{3}`| aaa |
| `{n,}`| n o più | `a{2,}`| aa, aaa, aaaa... |
| `{n,m}`| Tra n e m | `a{2,4}`| aa, aaa, aaaa |
### Avido contro pigro
Per impostazione predefinita, i quantificatori sono **greedy** (corrispondono il più possibile). Aggiungi`?`per renderli **pigri** (abbina il meno possibile).
| Modello | Stringa | Partita golosa | Partita pigra |
|---------|--------|-----|------------|
| `<.*>`| `<b>hi</b>`| `<b>hi</b>`(stringa intera) | `<b>`e`</b>`separatamente |
| `<.+?>`| `<b>hi</b>`| — | `<b>`,`</b>`|
---

## Ancore
| Ancora | Significato |
|--------|---------|
| `^`| Inizio della stringa |
| `$`| Fine della stringa |
| `\b`| Confine di parole |
| `\B`| Confine non verbale |
| `(?=...)`| Sguardo positivo |
| `(?!...)`| Look-ahead negativo |
| `(?<=...)`| Lookbehind positivo |
| `(?<!...)`| Lookbehind negativo |
**Esempio di limite di parole**:`\bcat\b`corrisponde a "gatto" in "il gatto seduto" ma non in "categoria".
---

## Gruppi e cattura
| Sintassi | Descrizione | Esempio |
|--------|-----|---------|
| `(abc)`| Gruppo di acquisizione | Estrai "abc" da una corrispondenza |
| `(?:abc)`| Gruppo non catturante | Raggruppa senza acquisire |
| `\1`| Riferimento al gruppo 1 | `(abc)\1`corrisponde a "abcabc" |
| `(?<name>abc)`| Gruppo di acquisizione denominato | `(?<year>\d{4})`|
| `a(?=b)`| Sguardo positivo | Trova "a" solo se seguito da "b" |
| `a(?!b)`| Look-ahead negativo | Trova "a" solo se NON seguito da "b" |
---

## Modelli comuni
### Convalida
| Modello | Partite | Note |
|---------|---------|-------|
| `^\d{5}$`| Codice postale USA | Esattamente 5 cifre |
| `^\d{5}(-\d{4})?$`| CAP USA+4 | 5 cifre, opzionale -4 |
| `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`| Indirizzo e-mail | Semplificato; RFC 5322 è molto più complesso |
| `^https?:\/\/`| L'URL inizia con http:// o https:// | |
| `^\+?[1-9]\d{1,14}$`| Numero di telefono (formato E.164) | Norma internazionale |
| `^(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)$`| Indirizzo IPv4 | |
| `^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$`| Indirizzo IPv6 | Semplificato |
| `^\d{3}-\d{2}-\d{4}$`| Formato SSN statunitense | XXX-XX-XXXX |
| `^[A-Z]{1,2}\d{1,4}\s?\d[A-Z]{2}$`| Codice postale del Regno Unito | Semplificato |
### Estrazione
| Modello | Estratti |
|---------|----------|
| `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b`| Indirizzi email dal testo |
| `https?:\/\/[^\s]+`| URL dal testo |
| `\b\d{1,3}(\.\d{1,3}){3}\b`| Indirizzi IPv4 dal testo |
| `\d{4}-\d{2}-\d{2}`| Date ISO (AAAA-MM-GG) |
| `#[0-9a-fA-F]{6}\b`| Codici colore esadecimali |
| `\$\d+(?:\.\d{2})?`| Importi in dollari |
### Elaborazione del testo
| Modello | Scopo |
|---------|---------|
| `\s+`| Corrisponde a uno o più caratteri di spazio bianco (compressione spazi) |
| `\r?\n`| Corrisponde alle interruzioni di riga (gestisce sia \n che \r\n) |
| `^.*$`| Corrisponde a un'intera riga |
| `<[^>]+>`| Corrisponde ai tag HTML/XML (semplificato; non analizzare HTML con regex) |
| `["']([^"']*)["']`| Corrisponde alle stringhe tra virgolette |
---

## Flag/Modificatori
| Bandiera | Significato | Effetto |
|------|---------|--------|
| `i`| Senza distinzione tra maiuscole e minuscole | `cat`corrisponde a "Cat", "CAT", "cAt" |
| `g`| Globale | Trova tutte le corrispondenze, non solo la prima |
| `m`| Multilinea | `^`e`$`corrispondono ai limiti della linea, non solo alla stringa |
| `s`| Dotall | `.`corrisponde ai caratteri di nuova riga |
| `x`| Esteso | Ignora gli spazi bianchi e consenti i commenti nel modello |
---

## Utilizzo specifico della lingua
### Pitone
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

### grep/sed/awk (riga di comando)
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

## Errori comuni
| Errore | Problema | Correzione |
|---------|---------|-----|
| `.*`è goloso | Corrisponde troppo | Utilizzare`.*?`per la corrispondenza pigra |
| Dimenticarsi di scappare da`.`| `file.txt`corrisponde anche a`fileXtxt`| Utilizzare`file\.txt`|
| Non ancoraggio dei modelli di validazione | `^\d{3}$`incorporato in una stringa più lunga | Utilizzare`^`e`$`|
| Classe di caratteri all'interno di`[]`| `[\d+]`corrisponde a`\`,`d`,`+`— non cifre | Utilizza`\d`all'esterno di`[]`o`[0-9]`|
| Analisi dell'HTML con regex | L'HTML non è un linguaggio normale | Utilizza un parser HTML per l'analisi reale; regex OK per una semplice estrazione |
| Backtracking catastrofico | I quantificatori nidificati come`(a+)+`possono essere bloccati | Semplifica il modello; utilizzare i gruppi atomici |
| Non testare i casi limite | Il modello funziona su un percorso felice, fallisce sul limite | Test con stringhe vuote, input molto lungo, caratteri speciali |
---

## Strumenti di test
| Strumento | Digitare | URL |
|------|------|-----|
| **Regex101** | Rete | regex101.com — corrispondenza in tempo reale con spiegazione |
| **RegExr** | Rete | regexr.com — test interattivi con cheatsheet |
| **cruciverba regex** | Gioco | regexcrossword.com — impara risolvendo enigmi |
---

## Riepilogo
Regex è uno strumento per la corrispondenza di modelli nel testo. Inizia in modo semplice: la maggior parte dei modelli del mondo reale sono solo una combinazione di classi di personaggi, quantificatori, ancore e gruppi. Utilizza uno strumento di test per verificare i tuoi modelli prima di inserirli nel codice. E ricorda: se la tua espressione regolare sta diventando così complessa che non puoi leggerla, probabilmente è ora di usare invece un parser adeguato.