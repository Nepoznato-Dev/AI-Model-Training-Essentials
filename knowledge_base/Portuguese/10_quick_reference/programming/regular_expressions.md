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
# Folha de referências de expressões regulares
Expressões regulares (regex) são padrões para correspondência de texto. Eles são usados ​​em qualquer lugar: pesquisa e substituição, validação de entrada, análise de log, extração de dados e muito mais. Esta é uma referência prática, não um livro didático.
---

## Sintaxe Central
### Caracteres Literais
A maioria dos caracteres corresponde a si mesmo:`a`corresponde a "a",`cat`corresponde a "gato".
### Caracteres Especiais (Metacaracteres)
Eles têm um significado especial e devem ser escapados com`\`para corresponder literalmente:
| Personagem | Significado |
|-----------|---------|
| `.`| Qualquer caractere, exceto nova linha |
| `^`| Início da string (ou linha no modo multilinha) |
| `$`| Fim da string (ou linha no modo multilinha) |
| `*`| 0 ou mais dos anteriores |
| `+`| 1 ou mais dos anteriores |
| `?`| 0 ou 1 dos anteriores (torna os quantificadores preguiçosos com`*?`,`+?`) |
| `\|`| Alternância (OU) |
| `()`| Agrupamento e captura |
| `[]`| Classe de personagem |
| `{}`| Faixa de quantificador |
| `\`| Personagem de fuga |
---

## Classes de personagens
| Padrão | Partidas |
|--------|---------|
| `[abc]`| a, b ou c |
| `[a-z]`| Qualquer letra minúscula |
| `[A-Z]`| Qualquer letra maiúscula |
| `[0-9]`| Qualquer dígito |
| `[a-zA-Z]`| Qualquer carta |
| `[^abc]`| Qualquer coisa exceto a, b ou c (classe negada) |
| `[a-z0-9_]`| Letras minúsculas, dígitos, sublinhado |
### Aulas de taquigrafia
| Padrão | Equivalente | Partidas |
|--------|-----------|---------|
| `\d`| `[0-9]`| Dígito |
| `\D`| `[^0-9]`| Não dígito |
| `\w`| `[a-zA-Z0-9_]`| Caráter de palavra |
| `\W`| `[^a-zA-Z0-9_]`| Caractere sem palavra |
| `\s`| `[ \t\n\r\f]`| Espaço em branco (espaço, tabulação, nova linha, etc.) |
| `\S`| `[^\s]`| Não espaço em branco |
---

## Quantificadores
| Quantificador | Significado | Exemplo | Partidas |
|-----------|---------|---------|---------|
| `*`| 0 ou mais | `ab*c`| ac, abc, abc, abbbc |
| `+`| 1 ou mais | `ab+c`| abc, abc, abbbc |
| `?`| 0 ou 1 | `ab?c`| ac, abc |
| `{n}`| Exatamente n | `a{3}`| aaa |
| `{n,}`| n ou mais | `a{2,}`| aa, aaa, aaa... |
| `{n,m}`| Entre n e m | `a{2,4}`| aa, aaa, aaa |
### Ganancioso vs Preguiçoso
Por padrão, os quantificadores são **gananciosos** (correspondem o máximo possível). Adicione`?`para torná-los **preguiçosos** (corresponder o mínimo possível).
| Padrão | Corda | Partida gananciosa | Partida preguiçosa |
|--------|--------|-------------|------------|
| `<.*>`| `<b>hi</b>`| `<b>hi</b>`(sequência inteira) | `<b>`e`</b>`separadamente |
| `<.+?>`| `<b>hi</b>`| — | `<b>`,`</b>`|
---

## Âncoras
| Âncora | Significado |
|--------|---------|
| `^`| Início da string |
| `$`| Fim da string |
| `\b`| Limite da palavra |
| `\B`| Limite sem palavra |
| `(?=...)`| Antecipação positiva |
| `(?!...)`| Antecipação negativa |
| `(?<=...)`| Olhar positivo para trás |
| `(?<!...)`| Olhar negativo para trás |
**Exemplo de limite de palavra**:`\bcat\b`corresponde a "gato" em "o gato sentado", mas não em "categoria".
---

## Grupos e captura
| Sintaxe | Descrição | Exemplo |
|--------|-------------|---------|
| `(abc)`| Capturando grupo | Extraia "abc" de uma correspondência |
| `(?:abc)`| Grupo não capturador | Agrupar sem capturar |
| `\1`| Referência retroativa ao grupo 1 | `(abc)\1`corresponde a "abcabc" |
| `(?<name>abc)`| Grupo de captura nomeado | `(?<year>\d{4})`|
| `a(?=b)`| Antecipação positiva | Corresponder "a" somente se seguido por "b" |
| `a(?!b)`| Antecipação negativa | Corresponder "a" somente se NÃO for seguido por "b" |
---

## Padrões Comuns
### Validação
| Padrão | Partidas | Notas |
|--------|---------|-------|
| `^\d{5}$`| CEP dos EUA | Exatamente 5 dígitos |
| `^\d{5}(-\d{4})?$`| CEP dos EUA+4 | 5 dígitos, opcional -4 |
| `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`| Endereço de e-mail | Simplificado; RFC 5322 é muito mais complexo |
| `^https?:\/\/`| URL começa com http:// ou https:// | |
| `^\+?[1-9]\d{1,14}$`| Número de telefone (formato E.164) | Padrão internacional |
| `^(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)$`| Endereço IPv4 | |
| `^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$`| Endereço IPv6 | Simplificado |
| `^\d{3}-\d{2}-\d{4}$`| Formato SSN dos EUA | XXX-XX-XXXX |
| `^[A-Z]{1,2}\d{1,4}\s?\d[A-Z]{2}$`| Código postal do Reino Unido | Simplificado |
### Extração
| Padrão | Extratos |
|--------|----------|
| `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b`| Endereços de e-mail de texto |
| `https?:\/\/[^\s]+`| URLs de texto |
| `\b\d{1,3}(\.\d{1,3}){3}\b`| Endereços IPv4 do texto |
| `\d{4}-\d{2}-\d{2}`| Datas ISO (AAAA-MM-DD) |
| `#[0-9a-fA-F]{6}\b`| Códigos de cores hexadecimais |
| `\$\d+(?:\.\d{2})?`| Valores em dólares |
### Processamento de texto
| Padrão | Finalidade |
|--------|---------|
| `\s+`| Combine um ou mais caracteres de espaço em branco (recolher espaços) |
| `\r?\n`| Corresponder quebras de linha (lida com \n e \r\n) |
| `^.*$`| Combine uma linha inteira |
| `<[^>]+>`| Corresponder tags HTML/XML (simplificado; não analisar HTML com regex) |
| `["']([^"']*)["']`| Corresponder strings entre aspas |
---

## Sinalizadores/Modificadores
| Bandeira | Significado | Efeito |
|------|---------|--------|
| `i`| Não diferencia maiúsculas de minúsculas | `cat`corresponde a "Gato", "CAT", "cAt" |
| `g`| Globais | Encontre todas as correspondências, não apenas a primeira |
| `m`| Multilinha | `^`e`$`correspondem aos limites da linha, não apenas à string |
| `s`| Dotal | `.`corresponde a caracteres de nova linha |
| `x`| Estendido | Ignore os espaços em branco e permita comentários no padrão |
---

## Uso específico do idioma
###Píton
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

### grep/sed/awk (linha de comando)
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

## Erros Comuns
| Erro | Problema | Correção |
|--------|---------|-----|
| `.*`é ganancioso | Combina demais | Use`.*?`para correspondência lenta |
| Esquecendo de escapar`.`| `file.txt`também corresponde a`fileXtxt`| Use`file\.txt`|
| Não ancorar padrões de validação | `^\d{3}$`incorporado em string mais longa | Use`^`e`$`|
| Classe de personagem dentro de`[]`| `[\d+]`corresponde a`\`,`d`,`+`— não dígitos | Use`\d`fora de`[]`ou`[0-9]`|
| Analisando HTML com regex | HTML não é uma linguagem regular | Use um analisador HTML para análise real; regex OK para extração simples |
| Retrocesso catastrófico | Quantificadores aninhados como`(a+)+`podem travar | Simplifique o padrão; usar grupos atômicos |
| Não testando casos extremos | Padrão funciona no caminho certo, mas falha no limite | Teste com strings vazias, entrada muito longa, caracteres especiais |
---

## Ferramentas de teste
| Ferramenta | Tipo | URL |
|------|------|-----|
| **Regex101** | Rede | regex101.com — correspondência em tempo real com explicação |
| **RegExr** | Rede | regexr.com — testes interativos com cheatsheet |
| **palavras cruzadas regex** | Jogo | regexcrossword.com — aprenda resolvendo quebra-cabeças |
---

## Resumo
Regex é uma ferramenta para correspondência de padrões em texto. Comece de forma simples – a maioria dos padrões do mundo real são apenas uma combinação de classes de caracteres, quantificadores, âncoras e grupos. Use uma ferramenta de teste para verificar seus padrões antes de colocá-los no código. E lembre-se: se sua regex estiver ficando tão complexa que você não consiga lê-la, provavelmente é hora de usar um analisador adequado.