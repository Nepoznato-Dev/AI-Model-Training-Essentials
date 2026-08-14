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
# Aide-mémoire sur les expressions régulières
Les expressions régulières (regex) sont des modèles permettant de faire correspondre du texte. Ils sont utilisés partout : recherche et remplacement, validation des entrées, analyse des journaux, extraction de données, etc. Ceci est une référence pratique, pas un manuel.
---

## Syntaxe de base
### Caractères littéraux
La plupart des caractères se correspondent :`a`correspond à "a",`cat`correspond à "cat".
### Caractères spéciaux (métacaractères)
Ceux-ci ont une signification particulière et doivent être échappés avec`\`pour correspondre littéralement :
| Caractère | Signification |
|-----------|---------|
| `.`| N'importe quel caractère sauf la nouvelle ligne |
| `^`| Début de chaîne (ou de ligne en mode multiligne) |
| `$`| Fin de chaîne (ou de ligne en mode multiligne) |
| `*`| 0 ou plus des réponses précédentes |
| `+`| 1 ou plusieurs des réponses précédentes |
| `?`| 0 ou 1 des éléments précédents (rend les quantificateurs paresseux avec`*?`,`+?`) |
| `\|`| Alternance (OR) |
| `()`| Regroupement et capture |
| `[]`| Classe de personnage |
| `{}`| Plage du quantificateur |
| `\`| Caractère d'évasion |
---

## Classes de personnages
| Modèle | Matchs |
|---------|---------|
| `[abc]`| une, b ou c |
| `[a-z]`| Toute lettre minuscule |
| `[A-Z]`| Toute lettre majuscule |
| `[0-9]`| N'importe quel chiffre |
| `[a-zA-Z]`| N'importe quelle lettre |
| `[^abc]`| Tout sauf a, b ou c (classe niée) |
| `[a-z0-9_]`| Lettres minuscules, chiffres, trait de soulignement |
### Cours de sténographie
| Modèle | Équivalent | Matchs |
|---------|-----------|---------|
| `\d`| `[0-9]`| Chiffre |
| `\D`| `[^0-9]`| Sans chiffres |
| `\w`| `[a-zA-Z0-9_]`| Caractère de mot |
| `\W`| `[^a-zA-Z0-9_]`| Caractère autre qu'un mot |
| `\s`| `[ \t\n\r\f]`| Espaces (espace, tabulation, nouvelle ligne, etc.) |
| `\S`| `[^\s]`| Non-espaces |
---

## Quantificateurs
| Quantificateur | Signification | Exemple | Matchs |
|-----------|---------|---------|---------|
| `*`| 0 ou plus | `ab*c`| ac, abc, abbc, abbbc |
| `+`| 1 ou plus | `ab+c`| abc, abbc, abbbc |
| `?`| 0 ou 1 | `ab?c`| ac, abc |
| `{n}`| Exactement n | `a{3}`| aaa |
| `{n,}`| n ou plus | `a{2,}`| aa, aaa, aaaa... |
| `{n,m}`| Entre n et m | `a{2,4}`| aa, aaa, aaaa |
### Gourmands ou paresseux
Par défaut, les quantificateurs sont **gourmands** (correspondent autant que possible). Ajoutez`?`pour les rendre **paresseux** (faites correspondre le moins possible).
| Modèle | Chaîne | Match gourmand | Match paresseux |
|---------|--------|-------------|------------|
| `<.*>`| `<b>hi</b>`| `<b>hi</b>`(chaîne entière) | `<b>`et`</b>`séparément |
| `<.+?>`| `<b>hi</b>`| — | `<b>`,`</b>`|
---

## Ancres
| Ancre | Signification |
|--------|---------|
| `^`| Début de chaîne |
| `$`| Fin de chaîne |
| `\b`| Limite de mot |
| `\B`| Limite non-mot |
| `(?=...)`| Perspectives positives |
| `(?!...)`| Anticipation négative |
| `(?<=...)`| Regard positif derrière |
| `(?<!...)`| Lookbehind négatif |
**Exemple de limite de mot** :`\bcat\b`correspond à "cat" dans "le chat assis" mais pas dans "catégorie".
---

## Groupes et capture
| Syntaxe | Descriptif | Exemple |
|--------|-------------|---------|
| `(abc)`| Groupe de capture | Extraire "abc" d'une correspondance |
| `(?:abc)`| Groupe non capturant | Groupe sans capturer |
| `\1`| Retour-référence au groupe 1 | `(abc)\1`correspond à "abcabc" |
| `(?<name>abc)`| Groupe de capture nommé | `(?<year>\d{4})`|
| `a(?=b)`| Perspectives positives | Correspond à "a" uniquement s'il est suivi de "b" |
| `a(?!b)`| Anticipation négative | Correspond à "a" uniquement s'il n'est PAS suivi de "b" |
---

## Modèles courants
### Validation
| Modèle | Matchs | Remarques |
|---------|---------|-------|
| `^\d{5}$`| Code postal américain | Exactement 5 chiffres |
| `^\d{5}(-\d{4})?$`| ZIP américain+4 | 5 chiffres, facultatif -4 |
| `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`| Adresse e-mail | Simplifié; La RFC 5322 est beaucoup plus complexe |
| `^https?:\/\/`| L'URL commence par http:// ou https:// | |
| `^\+?[1-9]\d{1,14}$`| Numéro de téléphone (format E.164) | Norme internationale |
| `^(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)$`| Adresse IPv4 | |
| `^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$`| Adresse IPv6 | Simplifié |
| `^\d{3}-\d{2}-\d{4}$`| Format du numéro de sécurité sociale américain | XXX-XX-XXXX |
| `^[A-Z]{1,2}\d{1,4}\s?\d[A-Z]{2}$`| Code postal du Royaume-Uni | Simplifié |
### Extraction
| Modèle | Extraits |
|---------|----------|
| `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b`| Adresses e-mail à partir du texte |
| `https?:\/\/[^\s]+`| URL à partir du texte |
| `\b\d{1,3}(\.\d{1,3}){3}\b`| Adresses IPv4 à partir du texte |
| `\d{4}-\d{2}-\d{2}`| Dates ISO (AAAA-MM-JJ) |
| `#[0-9a-fA-F]{6}\b`| Codes de couleur hexadécimaux |
| `\$\d+(?:\.\d{2})?`| Montants en dollars |
### Traitement de texte
| Modèle | Objectif |
|---------|---------|
| `\s+`| Faire correspondre un ou plusieurs caractères d'espacement (espaces de réduction) |
| `\r?\n`| Faire correspondre les sauts de ligne (gère à la fois \n et \r\n) |
| `^.*$`| Faire correspondre une ligne entière |
| `<[^>]+>`| Faites correspondre les balises HTML/XML (simplifié ; n'analysez pas le HTML avec regex) |
| `["']([^"']*)["']`| Faire correspondre les chaînes entre guillemets |
---

## Drapeaux / Modificateurs
| Drapeau | Signification | Effet |
|------|---------|--------|
| `i`| Insensible à la casse | `cat`correspond à "Cat", "CAT", "cAt" |
| `g`| Mondial | Trouvez toutes les correspondances, pas seulement la première |
| `m`| Multiligne | `^`et`$`correspondent aux limites de ligne, pas seulement à la chaîne |
| `s`| Dotall | `.`correspond aux caractères de nouvelle ligne |
| `x`| Étendu | Ignorez les espaces et autorisez les commentaires dans le modèle |
---

## Utilisation spécifique à la langue
###Python
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

###JavaScript
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

### grep / sed / awk (ligne de commande)
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

## Erreurs courantes
| Erreur | Problème | Corriger |
|---------|---------|-----|
| `.*`est gourmand | Correspond trop | Utilisez`.*?`pour une correspondance paresseuse |
| Oublier d'échapper`.`| `file.txt`correspond également à`fileXtxt`| Utiliser`file\.txt`|
| Ne pas ancrer les modèles de validation | `^\d{3}$`intégré dans une chaîne plus longue | Utilisez`^`et`$`|
| Classe de caractères à l'intérieur de`[]`| `[\d+]`correspond à`\`,`d`,`+`— pas de chiffres | Utilisez`\d`en dehors de`[]`ou`[0-9]`|
| Analyser du HTML avec regex | HTML n'est pas un langage normal | Utilisez un analyseur HTML pour une véritable analyse ; regex OK pour une extraction simple |
| Retour en arrière catastrophique | Les quantificateurs imbriqués comme`(a+)+`peuvent se bloquer | Simplifiez le modèle ; utiliser des groupes atomiques |
| Ne pas tester les cas extrêmes | Le modèle fonctionne sur un chemin heureux, échoue à la limite | Test avec chaînes vides, saisie très longue, caractères spéciaux |
---

## Outils de test
| Outil | Tapez | URL |
|------|------|-----|
| **Regex101** | Internet | regex101.com — correspondance en temps réel avec explication |
| **RegExr** | Internet | regexr.com — tests interactifs avec aide-mémoire |
| **regex-mots croisés** | Jeu | regexcrossword.com — apprenez en résolvant des énigmes |
---

## Résumé
Regex est un outil de correspondance de modèles dans le texte. Commencez simplement : la plupart des modèles du monde réel ne sont qu'une combinaison de classes de caractères, de quantificateurs, d'ancres et de groupes. Utilisez un outil de test pour vérifier vos modèles avant de les mettre dans le code. Et rappelez-vous : si votre expression régulière devient si complexe que vous ne pouvez pas la lire, il est probablement temps d'utiliser un analyseur approprié à la place.