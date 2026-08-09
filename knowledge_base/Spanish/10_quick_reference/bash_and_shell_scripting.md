---
# Metadatos
título: "Hoja de trucos para secuencias de comandos de Bash y Shell"
descripción: "Secuencias de comandos Bash, procesamiento de texto, frases útiles"
categoría: "Referencia rápida"
versión: "1.0.0"
estado: "activo"
# Contribución
autores:
  - nombre: "Equipo de formación del modelo de IA"
    correo electrónico: ""
    rol: "autor_original"
colaboradores: []
registro de cambios:
  - versión: "1.0.0"
    fecha: "2026-08-05"
    autor: "Equipo de formación del modelo de IA"
    cambios: "Se agregaron metadatos de temas frontales de YAML para el seguimiento de los contribuyentes"
# Revisión
creado: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
review_by: "Equipo de la base de conocimientos de referencia rápida"
next_review: "2027-08-05"
# Clasificación
Etiquetas: [bash, shell, secuencias de comandos, referencia rápida]
nivel_dificultad: "principiante"
requisitos previos: []
estimado_reading_time: "19 minutos"
# Guía de contribución
contribución:
  licencia: "MIT"
  feedback_channel: "Problemas de GitHub"
  how_to_contribute: "Enviar un PR con cambios y actualizar el registro de cambios"
  review_process: "Los mantenedores de categorías revisan los cambios antes de fusionarlos"
---
# Hoja de trucos para secuencias de comandos de Bash y Shell
Una referencia práctica para escribir scripts de shell en Bash, el shell predeterminado en la mayoría de los sistemas Linux y macOS. Cubre sintaxis, patrones comunes, procesamiento de texto y frases útiles.
---

## Estructura del guión
Cada script Bash comienza con una línea **shebang**:
```bash
#!/usr/bin/env bash
set -euo pipefail   # Safe defaults
```

| Bandera | Efecto |
|------|--------|
| `set -e`| Salir inmediatamente si falla un comando |
| `set -u`| Trate las variables no configuradas como errores |
| `set -o pipefail`| La canalización falla si falla algún comando en ella |
| `set -x`| Imprima cada comando antes de ejecutarlo (modo de depuración) |
Ejecute un script:`chmod +x script.sh && ./script.sh`o `bash script.sh`
---

##Variables
```bash
# Assignment (no spaces around =)
NAME="Alice"
COUNT=42

# Usage
echo "$NAME"          # Alice
echo "${NAME}"        # Alice (explicit delimiter)
echo "Hello, $NAME!"  # Hello, Alice!

# Read-only
readonly PI=3.14159

# Command substitution
TODAY=$(date +%Y-%m-%d)
FILES=$(ls -1 | wc -l)

# Default values
echo "${UNSET_VAR:-default}"   # Prints "default" if UNSET_VAR is empty/unset
: "${REQUIRED_VAR:?Error: REQUIRED_VAR is not set}"  # Exit with error if unset

# Arithmetic
echo $((2 + 3))        # 5
echo $((COUNT * 2))    # 84
((COUNT++))            # Increment
```

---

## Variables especiales
| Variables | Significado |
|----------|---------|
| `$0`| Nombre del guión |
|  `$1`, `$2`, ... | Argumentos posicionales |
| `$#`| Número de argumentos posicionales |
| `$@`| Todos los argumentos posicionales (como palabras separadas) |
| `$*`| Todos los argumentos posicionales (como una sola cadena) |
| `$?`| Estado de salida del último comando (0 = éxito) |
| `$$`| PID del proceso actual |
| `$!`| PID del último proceso en segundo plano |
| `$_`| Último argumento del comando anterior |
---

## Condicionales
### si/elif/si no
```bash
if [[ -f "$FILE" ]]; then
    echo "File exists"
elif [[ -d "$FILE" ]]; then
    echo "It's a directory"
else
    echo "Not found"
fi
```

### Operadores de prueba
| Prueba | Significado |
|------|---------|
| `[[ -f "$x" ]]`| El archivo existe y es un archivo normal |
| `[[ -d "$x" ]]`| El directorio existe |
| `[[ -e "$x" ]]`| El archivo/directorio existe (cualquier cosa) |
| `[[ -r "$x" ]]`| Legible |
| `[[ -w "$x" ]]`| Escribible |
| `[[ -x "$x" ]]`| Ejecutable |
| `[[ -z "$x" ]]`| La cadena está vacía |
| `[[ -n "$x" ]]`| La cadena no está vacía |
| `[[ "$a" == "$b" ]]`| Igualdad de cadenas |
| `[[ "$a" != "$b" ]]`| Desigualdad de cadenas |
| `[[ "$a" =~ regex ]]`| Coincidencia de expresiones regulares |
| `[[ $a -eq $b ]]`| Igualdad de enteros |
| `[[ $a -ne $b ]]`| Desigualdad entera |
| `[[ $a -gt $b ]]`| Mayor que |
| `[[ $a -lt $b ]]`| Menos de |
| `[[ $a -ge $b ]]`| Mayor o igual que |
| `[[ $a -le $b ]]`| Menor o igual |
### Operadores lógicos
```bash
[[ -f "$a" && -f "$b" ]]   # AND
[[ -f "$a" || -f "$b" ]]   # OR
[[ ! -f "$a" ]]             # NOT
```

---

## Bucles
### para bucle
```bash
# C-style
for ((i = 0; i < 10; i++)); do
    echo "$i"
done

# Over a list
for item in apple banana cherry; do
    echo "$item"
done

# Over files
for file in *.txt; do
    echo "Processing $file"
done

# Over command output
for line in $(cat list.txt); do
    echo "$line"
done
```

### mientras bucle
```bash
while [[ $COUNT -gt 0 ]]; do
    echo "$COUNT"
    ((COUNT--))
done

# Read file line by line
while IFS= read -r line; do
    echo "$line"
done < input.txt
```

### hasta bucle
```bash
until [[ -f /tmp/ready ]]; do
    echo "Waiting..."
    sleep 1
done
```

---

## Funciones
```bash
# Define
greet() {
    local name="$1"          # local variable
    echo "Hello, ${name}!"
}

# Call
greet "Alice"               # Hello, Alice!

# Return values (use echo + command substitution)
add() {
    echo $(( $1 + $2 ))
}
RESULT=$(add 3 5)           # 8
```

---

## Operaciones de cadena
```bash
STR="Hello, World!"

echo "${#STR}"              # Length: 13
echo "${STR:0:5}"           # Substring: "Hello"
echo "${STR,,}"             # Lowercase: "hello, world!"
echo "${STR^^}"             # Uppercase: "HELLO, WORLD!"
echo "${STR/World/Bash}"    # Replace first: "Hello, Bash!"
echo "${STR//l/L}"          # Replace all: "HeLLo, WorLd!"
echo "${STR#*,}"            # Remove shortest prefix matching ,: " World!"
echo "${STR%,*}"            # Remove shortest suffix matching ,: "Hello"
```

---

## matrices
```bash
# Indexed array
FRUITS=("apple" "banana" "cherry")
echo "${FRUITS[0]}"         # apple
echo "${FRUITS[@]}"         # all elements
echo "${#FRUITS[@]}"        # length: 3

# Append
FRUITS+=("date")

# Associative array (Bash 4+)
declare -A AGES
AGES[Alice]=30
AGES[Bob]=25
echo "${AGES[Alice]}"       # 30
echo "${!AGES[@]}"          # keys: Alice Bob
```

---

## Tubería y redirección
| Sintaxis | Significado |
|--------|---------|
| `cmd > file`| Redirigir salida estándar al archivo (sobrescribir) |
| `cmd >> file`| Redirigir salida estándar al archivo (añadir) |
| `cmd 2> errors.log`| Redirigir stderr |
| `cmd &> all.log`| Redirigir tanto stdout como stderr |
| `cmd1 \| cmd2`| Conecte la salida estándar de cmd1 a la entrada estándar de cmd2 |
| `cmd1 \|& cmd2`| Tubería tanto stdout como stderr |
| `cmd < file`| Redirigir archivo a stdin |
| `cmd <<EOF ... EOF`| Aquí-documento (entrada de varias líneas) |
| `cmd <<< "string"`| Here-string (entrada de una sola línea) |
```bash
# Here-document
cat <<EOF
Name: $NAME
Date: $(date)
EOF

# Process substitution
diff <(sort file1.txt) <(sort file2.txt)
```

---

## Procesamiento de texto
### cortar
```bash
echo "a,b,c" | cut -d',' -f2        # b (field 2, comma-delimited)
echo "hello world" | cut -c1-5      # hello (characters 1-5)
cut -d':' -f1 /etc/passwd           # First field (usernames)
```

### clasificar
```bash
sort file.txt                       # Alphabetical sort
sort -n numbers.txt                 # Numeric sort
sort -r file.txt                    # Reverse sort
sort -t',' -k2 file.csv             # Sort by 2nd field, comma-delimited
sort -u file.txt                    # Sort and remove duplicates
```

### único
```bash
sort names.txt | uniq               # Remove consecutive duplicates (sort first!)
sort names.txt | uniq -c            # Count occurrences
sort names.txt | uniq -d            # Show only duplicated lines
```

### mal
```bash
awk '{print $1, $3}' file.txt              # Print columns 1 and 3
awk -F',' '{print $2}' data.csv            # CSV: print 2nd column
awk '/ERROR/ {print NR": "$0}' log.txt     # Print ERROR lines with line numbers
awk '{sum += $1} END {print sum}' nums.txt # Sum first column
awk 'length($0) > 80' file.txt             # Lines longer than 80 chars
awk '{print toupper($0)}' file.txt         # Uppercase every line
awk -F: '{print $1}' /etc/passwd           # Usernames from passwd file
```

### sed
```bash
sed 's/old/new/' file.txt           # Replace first occurrence per line
sed 's/old/new/g' file.txt          # Replace all occurrences
sed 's/old/new/gi' file.txt         # Case-insensitive replace all
sed '/pattern/d' file.txt           # Delete lines matching pattern
sed -n '5,10p' file.txt             # Print lines 5-10
sed 's/^/# /' file.txt              # Prepend "# " to every line
sed 's/[[:space:]]\+$//' file.txt   # Remove trailing whitespace
sed '10,20d' file.txt               # Delete lines 10-20
sed -i 's/old/new/g' file.txt       # Edit in place (macOS: sed -i '' ...)
```

### grep
```bash
grep "pattern" file.txt             # Basic search
grep -i "pattern" file.txt          # Case-insensitive
grep -r "pattern" directory/        # Recursive search
grep -rn "pattern" src/             # Recursive with line numbers
grep -c "ERROR" log.txt             # Count matching lines
grep -v "pattern" file.txt          # Invert match (exclude)
grep -E "regex" file.txt            # Extended regex
grep -l "pattern" *.txt             # List files containing match
grep -w "word" file.txt             # Match whole word only
grep -A 3 "pattern" file.txt        # Show 3 lines after match
grep -B 2 "pattern" file.txt        # Show 2 lines before match
grep -C 2 "pattern" file.txt        # Show 2 lines of context
```

---

## Frases útiles
```bash
# Find largest files
find / -type f -exec du -h {} + 2>/dev/null | sort -rh | head -20

# Count lines of code in a directory
find . -name "*.py" | xargs wc -l | tail -1

# Monitor a log file in real time
tail -f /var/log/syslog | grep --line-buffered "ERROR"

# Find and replace in all files
find . -name "*.txt" -exec sed -i 's/old/new/g' {} +

# Check which process is using a port
lsof -i :8080          # macOS/Linux
ss -tlnp | grep 8080   # Linux

# Compress a directory
tar -czf archive.tar.gz directory/

# Extract a tarball
tar -xzf archive.tar.gz

# Download a file
curl -O https://example.com/file.zip      # Save with original name
wget https://example.com/file.zip          # Alternative

# Generate a random password
openssl rand -base64 24
# or
tr -dc 'A-Za-z0-9!@#$%' < /dev/urandom | head -c 20

# JSON pretty-print
cat data.json | python3 -m json.tool
# or
cat data.json | jq .

# CSV to TSV
tr ',' '\t' < data.csv

# Remove duplicate lines (preserving order)
awk '!seen[$0]++' file.txt

# Find files modified in the last 24 hours
find . -type f -mtime -1

# Kill all processes matching a name
pkill -f "python app.py"

# Disk usage summary
du -sh */ | sort -rh | head -10

# System info one-liner
uname -a; echo "---"; uptime; echo "---"; df -h; echo "---"; free -h
```

---

## Patrones de secuencias de comandos
### Análisis de argumentos
```bash
#!/usr/bin/env bash
set -euo pipefail

usage() {
    echo "Usage: $0 [-n NAME] [-v] FILE"
    exit 1
}

VERBOSE=false
while getopts "n:v" opt; do
    case $opt in
        n) NAME="$OPTARG" ;;
        v) VERBOSE=true ;;
        *) usage ;;
    esac
done
shift $((OPTIND - 1))

FILE="${1:?Error: FILE argument required}"
echo "Name: ${NAME:-not set}, Verbose: $VERBOSE, File: $FILE"
```

### Manejo de errores
```bash
#!/usr/bin/env bash
set -euo pipefail

cleanup() {
    echo "Cleaning up..."
    rm -f /tmp/tempfile
}
trap cleanup EXIT

error_handler() {
    echo "Error on line $1, exit code $2" >&2
}
trap 'error_handler ${LINENO} $?' ERR
```

### Comprobando dependencias
```bash
for cmd in git docker python3; do
    if ! command -v "$cmd" &>/dev/null; then
        echo "Error: $cmd is not installed" >&2
        exit 1
    fi
done
```

### Archivos temporales
```bash
TMPFILE=$(mktemp)
trap 'rm -f "$TMPFILE"' EXIT
echo "working..." > "$TMPFILE"
```

---

## Resumen
Las secuencias de comandos Bash son un multiplicador de fuerza para cualquiera que trabaje con computadoras. No es necesario memorizar todas las banderas; es necesario saber qué es posible y dónde buscarlo. Comience con lo básico: variables, condicionales, bucles, canalizaciones. Luego, aplique capas de herramientas de procesamiento de texto (grep, sed, awk) según las necesite. Y utilice siempre `set -euo pipefail`; en el futuro se lo agradecerá.