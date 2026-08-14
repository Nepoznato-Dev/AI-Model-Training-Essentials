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
# Hoja de trucos de expresiones regulares
Las expresiones regulares (regex) son patrones para hacer coincidir texto. Se utilizan en todas partes: búsqueda y reemplazo, validación de entradas, análisis de registros, extracción de datos y más. Esta es una referencia práctica, no un libro de texto.
---

## Sintaxis principal
### Caracteres literales
La mayoría de los caracteres coinciden entre sí:`a`coincide con "a",`cat`coincide con "cat".
### Caracteres especiales (metacaracteres)
Estos tienen un significado especial y deben tener como escape`\`para que coincidan literalmente:
| Personaje | Significado |
|-----------|------------------|
| `.`| Cualquier carácter excepto nueva línea |
| `^`| Inicio de cadena (o línea en modo multilínea) |
| `$`| Fin de cadena (o línea en modo multilínea) |
| `*`| 0 o más de los anteriores |
| `+`| 1 o más de los anteriores |
| `?`| 0 o 1 de los anteriores (hace que los cuantificadores sean perezosos con`*?`,`+?`) |
| `\|`| Alternancia (O) |
| `()`| Agrupación y captura |
| `[]`| Clase de personaje |
| `{}`| Rango del cuantificador |
| `\`| Carácter de escape |
---

## Clases de personajes
| Patrón | Partidos |
|---------|---------|
| `[abc]`| a, b o c |
| `[a-z]`| Cualquier letra minúscula |
| `[A-Z]`| Cualquier letra mayúscula |
| `[0-9]`| Cualquier dígito |
| `[a-zA-Z]`| Cualquier carta |
| `[^abc]`| Cualquier cosa excepto a, b o c (clase negada) |
| `[a-z0-9_]`| Letras minúsculas, dígitos, guiones bajos |
### Clases de taquigrafía
| Patrón | Equivalente | Partidos |
|---------|-----------|---------|
| `\d`| `[0-9]`| Dígito |
| `\D`| `[^0-9]`| Sin dígitos |
| `\w`| `[a-zA-Z0-9_]`| Carácter de palabra |
| `\W`| `[^a-zA-Z0-9_]`| Carácter sin palabra |
| `\s`| `[ \t\n\r\f]`| Espacios en blanco (espacio, tabulación, nueva línea, etc.) |
| `\S`| `[^\s]`| Sin espacios en blanco |
---

## Cuantificadores
| Cuantificador | Significado | Ejemplo | Partidos |
|-----------|---------|---------|---------|
| `*`| 0 o más | `ab*c`| ca, abc, abbc, abbbc |
| `+`| 1 o más | `ab+c`| abc, abbc, abbbc |
| `?`| 0 o 1 | `ab?c`| ca, abc |
| `{n}`| Exactamente norte | `a{3}`| aaa |
| `{n,}`| no más | `a{2,}`| aa, aaa, aaaa... |
| `{n,m}`| Entre n y m | `a{2,4}`| aa, aaa, aaaa |
### Codicioso vs Perezoso
De forma predeterminada, los cuantificadores son **codiciosos** (coinciden tanto como sea posible). Agrega`?`para hacerlos **perezosos** (combinan lo menos posible).
| Patrón | Cadena | Partido codicioso | Partido perezoso |
|---------|--------|-------------|------------|
| `<.*>`| `<b>hi</b>`| `<b>hi</b>`(cadena completa) | `<b>`y`</b>`por separado |
| `<.+?>`| `<b>hi</b>`| — | `<b>`,`</b>`|
---

## Anclas
| Ancla | Significado |
|--------|---------|
| `^`| Inicio de cadena |
| `$`| Fin de la cadena |
| `\b`| Límite de palabra |
| `\B`| Límite sin palabras |
| `(?=...)`| Previsión positiva |
| `(?!...)`| Previsión negativa |
| `(?<=...)`| Mirada atrás positiva |
| `(?<!...)`| Mirada atrás negativa |
**Ejemplo de límite de palabra**:`\bcat\b`coincide con "gato" en "el gato sentado" pero no en "categoría".
---

## Grupos y captura
| Sintaxis | Descripción | Ejemplo |
|--------|-------------|---------|
| `(abc)`| Grupo de captura | Extraer "abc" de una coincidencia |
| `(?:abc)`| Grupo sin captura | Grupo sin capturar |
| `\1`| Referencia anterior al grupo 1 | `(abc)\1`coincide con "abcabc" |
| `(?<name>abc)`| Grupo de captura nombrado | `(?<year>\d{4})`|
| `a(?=b)`| Previsión positiva | Coincide con "a" sólo si va seguida de "b" |
| `a(?!b)`| Previsión negativa | Coincide con "a" sólo si NO va seguida de "b" |
---

## Patrones comunes
### Validación
| Patrón | Partidos | Notas |
|---------|---------|-------|
| `^\d{5}$`| Código postal de EE. UU. | Exactamente 5 dígitos |
| `^\d{5}(-\d{4})?$`| Código postal de EE. UU.+4 | 5 dígitos, opcional -4 |
| `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`| Dirección de correo electrónico | Simplificado; RFC 5322 es mucho más complejo |
| `^https?:\/\/`| La URL comienza con http:// o https:// | |
| `^\+?[1-9]\d{1,14}$`| Número de teléfono (formato E.164) | Estándar internacional |
| `^(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)$`| Dirección IPv4 | |
| `^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$`| Dirección IPv6 | Simplificado |
| `^\d{3}-\d{2}-\d{4}$`| Formato SSN de EE. UU. | XXX-XX-XXXX |
| `^[A-Z]{1,2}\d{1,4}\s?\d[A-Z]{2}$`| Código postal del Reino Unido | Simplificado |
### Extracción
| Patrón | Extractos |
|---------|----------|
| `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b`| Direcciones de correo electrónico de texto |
| `https?:\/\/[^\s]+`| URL de texto |
| `\b\d{1,3}(\.\d{1,3}){3}\b`| Direcciones IPv4 a partir de texto |
| `\d{4}-\d{2}-\d{2}`| Fechas ISO (AAAA-MM-DD) |
| `#[0-9a-fA-F]{6}\b`| Códigos de colores hexadecimales |
| `\$\d+(?:\.\d{2})?`| Cantidades en dólares |
### Procesamiento de texto
| Patrón | Propósito |
|---------|---------|
| `\s+`| Haga coincidir uno o más caracteres de espacio en blanco (contraer espacios) |
| `\r?\n`| Saltos de línea coincidentes (maneja tanto \n como \r\n) |
| `^.*$`| Unir una línea completa |
| `<[^>]+>`| Haga coincidir etiquetas HTML/XML (simplificado; no analice HTML con expresiones regulares) |
| `["']([^"']*)["']`| Coincidir cadenas entre comillas |
---

## Banderas / Modificadores
| Bandera | Significado | Efecto |
|------|---------|--------|
| `i`| No distingue entre mayúsculas y minúsculas | `cat`coincide con "Cat", "CAT", "cAt" |
| `g`| Mundial | Encuentra todas las coincidencias, no solo la primera |
| `m`| Multilínea | `^`y`$`coinciden con los límites de las líneas, no solo con las cadenas |
| `s`| Dotall | `.`coincide con caracteres de nueva línea |
| `x`| Extendido | Ignora los espacios en blanco y permite comentarios en el patrón |
---

## Uso específico del idioma
### Pitón
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

### grep/sed/awk (Línea de comando)
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

## Errores comunes
| Error | Problema | Arreglar |
|---------|---------|-----|
| `.*`es codicioso | Coincide demasiado | Utilice`.*?`para realizar coincidencias diferidas |
| Olvidando escapar`.`| `file.txt`también coincide con`fileXtxt`| Utilice`file\.txt`|
| No anclar patrones de validación | `^\d{3}$`incrustado en una cadena más larga | Utilice`^`y`$`|
| Clase de personaje dentro de`[]`| `[\d+]`coincide con `\`, `d`, `+`, no dígitos | Utilice`\d`fuera de`[]`o`[0-9]`|
| Analizando HTML con expresiones regulares | HTML no es un lenguaje normal | Utilice un analizador HTML para un análisis real; expresión regular OK para extracción simple |
| Retroceso catastrófico | Los cuantificadores anidados como`(a+)+`pueden colgarse | Simplifica el patrón; utilizar grupos atómicos |
| No probar casos extremos | El patrón funciona en el camino feliz, falla al límite | Prueba con cadenas vacías, entradas muy largas, caracteres especiales |
---

## Herramientas de prueba
| Herramienta | Tipo | URL |
|------|------|-----|
| **Regex101** | Web | regex101.com — coincidencia en tiempo real con explicación |
| **RegExr** | Web | regexr.com — pruebas interactivas con hoja de referencia |
| **crucigrama de expresiones regulares** | Juego | regexcrossword.com — aprende resolviendo acertijos |
---

## Resumen
Regex es una herramienta para la coincidencia de patrones en texto. Comience de manera simple: la mayoría de los patrones del mundo real son solo una combinación de clases de caracteres, cuantificadores, anclajes y grupos. Utilice una herramienta de prueba para verificar sus patrones antes de codificarlos. Y recuerde: si su expresión regular se vuelve tan compleja que no puede leerla, probablemente sea hora de utilizar un analizador adecuado.