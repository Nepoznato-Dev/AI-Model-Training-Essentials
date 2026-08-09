---
# मेटाडेटा
शीर्षक: "बैश एंड शैल स्क्रिप्टिंग चीट शीट"
विवरण: "बैश स्क्रिप्टिंग, टेक्स्ट प्रोसेसिंग, उपयोगी वन-लाइनर्स"
श्रेणी: "त्वरित संदर्भ"
संस्करण: "1.0.0"
स्थिति: "सक्रिय"
#योगदान
लेखक:
  - नाम: "एआई मॉडल ट्रेनिंग टीम"
    ईमेल: ""
    भूमिका: "मूल_लेखक"
योगदानकर्ता: []
चेंजलॉग:
  - संस्करण: "1.0.0"
    दिनांक: "2026-08-05"
    लेखक: "एआई मॉडल ट्रेनिंग टीम"
    परिवर्तन: "योगदानकर्ता ट्रैकिंग के लिए YAML फ्रंटमैटर मेटाडेटा जोड़ा गया"
#समीक्षा
बनाया गया: "2026-08-05"
अंतिम_संशोधित: "2026-08-05"
समीक्षा दिनांक: "2027-02-05"
review_by: "त्वरित संदर्भ नॉलेज बेस टीम"
अगली_समीक्षा: "2027-08-05"
#वर्गीकरण
टैग: [बैश, शेल, स्क्रिप्टिंग, त्वरित-संदर्भ]
कठिनाई_स्तर: "शुरुआती"
पूर्वावश्यकताएँ: []
अनुमानित_पढ़ने_का समय: "19 मिनट"
# योगदान मार्गदर्शिका
योगदान:
  लाइसेंस: "एमआईटी"
  फीडबैक_चैनल: "गिटहब मुद्दे"
  कैसे_तो_योगदान करें: "परिवर्तनों के साथ एक पीआर सबमिट करें और चेंजलॉग अपडेट करें"
  समीक्षा_प्रक्रिया: "विलय से पहले श्रेणी अनुरक्षकों द्वारा परिवर्तनों की समीक्षा की जाती है"
---
# बैश और शैल स्क्रिप्टिंग चीट शीट
बैश में शेल स्क्रिप्ट लिखने के लिए एक व्यावहारिक संदर्भ - अधिकांश लिनक्स और मैकओएस सिस्टम पर डिफ़ॉल्ट शेल। इसमें सिंटैक्स, सामान्य पैटर्न, टेक्स्ट प्रोसेसिंग और उपयोगी वन-लाइनर्स शामिल हैं।
---

## स्क्रिप्ट संरचना
प्रत्येक बैश स्क्रिप्ट **शेबैंग** लाइन से शुरू होती है:
```bash
#!/usr/bin/env bash
set -euo pipefail   # Safe defaults
```

| झंडा | प्रभाव |
|------|--------|
|  __संरक्षित_0__ | यदि कोई आदेश विफल हो जाता है तो तुरंत बाहर निकलें |
|  __संरक्षित_1__ | अनसेट वेरिएबल्स को त्रुटियों के रूप में मानें |
|  __संरक्षित_2__ | यदि इसमें कोई कमांड विफल हो जाता है तो पाइपलाइन विफल हो जाती है |
|  __संरक्षित_3__ | निष्पादित करने से पहले प्रत्येक कमांड को प्रिंट करें (डीबग मोड) |
एक स्क्रिप्ट चलाएँ:`chmod +x script.sh && ./script.sh`या `bash script.sh`
---

## चर
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

## विशेष चर
| परिवर्तनीय | मतलब |
|---|----|
|  __संरक्षित_0__ | स्क्रिप्ट का नाम |
|  __संरक्षित_1__ , __संरक्षित_2__ , ... | स्थितीय तर्क |
|  __संरक्षित_3__ | स्थितीय तर्कों की संख्या |
|  __संरक्षित_4__ | सभी स्थितीय तर्क (अलग शब्दों के रूप में) |
|  __संरक्षित_5__ | सभी स्थितीय तर्क (एकल स्ट्रिंग के रूप में) |
|  __संरक्षित_6__ | अंतिम कमांड की निकास स्थिति (0 = सफलता) |
|  __संरक्षित_7__ | वर्तमान प्रक्रिया की पीआईडी ​​|
|  __संरक्षित_8__ | अंतिम पृष्ठभूमि प्रक्रिया की पीआईडी ​​|
|  __संरक्षित_9__ | पिछले आदेश का अंतिम तर्क |
---

## सशर्त
### यदि / एलिफ़ / अन्यथा
```bash
if [[ -f "$FILE" ]]; then
    echo "File exists"
elif [[ -d "$FILE" ]]; then
    echo "It's a directory"
else
    echo "Not found"
fi
```

### परीक्षण संचालक
| परीक्षण | मतलब |
|------|---------|
|  __संरक्षित_0__ | फ़ाइल मौजूद है और एक नियमित फ़ाइल है |
|  __संरक्षित_1__ | निर्देशिका मौजूद है |
|  __संरक्षित_2__ | फ़ाइल/निर्देशिका मौजूद है (कुछ भी) |
|  __संरक्षित_3__ | पठनीय |
|  __संरक्षित_4__ | लिखने योग्य |
|  __संरक्षित_5__ | निष्पादन योग्य |
|  __संरक्षित_6__ | स्ट्रिंग खाली है |
|  __संरक्षित_7__ | स्ट्रिंग खाली नहीं है |
|  __संरक्षित_8__ | स्ट्रिंग समानता |
|  __संरक्षित_9__ | स्ट्रिंग असमानता |
|  __संरक्षित_10__ | रेगेक्स मैच |
|  __संरक्षित_11__ | पूर्णांक समानता |
|  __संरक्षित_12__ | पूर्णांक असमानता |
|  __संरक्षित_13__ | से भी बड़ा |
|  __संरक्षित_14__ | से कम |
|  __संरक्षित_15__ | से बड़ा या बराबर |
|  __संरक्षित_16__ | से कम या बराबर |
### लॉजिकल ऑपरेटर्स
```bash
[[ -f "$a" && -f "$b" ]]   # AND
[[ -f "$a" || -f "$b" ]]   # OR
[[ ! -f "$a" ]]             # NOT
```

---

## लूप्स
### पाश के लिए
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

### जबकि लूप
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

### लूप तक
```bash
until [[ -f /tmp/ready ]]; do
    echo "Waiting..."
    sleep 1
done
```

---

## कार्य
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

## स्ट्रिंग ऑपरेशन
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

## सारणियाँ
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

## पाइपिंग और पुनर्निर्देशन
| सिंटैक्स | मतलब |
|-------|------|
|  __संरक्षित_0__ | stdout को फ़ाइल पर पुनर्निर्देशित करें (ओवरराइट करें) |
|  __संरक्षित_1__ | stdout को फ़ाइल (संलग्न) पर पुनर्निर्देशित करें |
|  __संरक्षित_2__ | रीडायरेक्ट stderr |
|  __संरक्षित_3__ | stdout और stderr दोनों को पुनर्निर्देशित करें |
|  __संरक्षित_4__ | cmd1 के पाइप stdout से cmd2 के stdin तक |
|  __संरक्षित_5__ | पाइप stdout और stderr दोनों |
|  __संरक्षित_6__ | फ़ाइल को stdin | पर पुनर्निर्देशित करें
|  __संरक्षित_7__ | यहां-दस्तावेज़ (मल्टी-लाइन इनपुट) |
|  __संरक्षित_8__ | यहां-स्ट्रिंग (सिंगल-लाइन इनपुट) |
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

## टेक्स्ट प्रोसेसिंग
### काटना
```bash
echo "a,b,c" | cut -d',' -f2        # b (field 2, comma-delimited)
echo "hello world" | cut -c1-5      # hello (characters 1-5)
cut -d':' -f1 /etc/passwd           # First field (usernames)
```

### क्रम से लगाना
```bash
sort file.txt                       # Alphabetical sort
sort -n numbers.txt                 # Numeric sort
sort -r file.txt                    # Reverse sort
sort -t',' -k2 file.csv             # Sort by 2nd field, comma-delimited
sort -u file.txt                    # Sort and remove duplicates
```

### अद्वितीय
```bash
sort names.txt | uniq               # Remove consecutive duplicates (sort first!)
sort names.txt | uniq -c            # Count occurrences
sort names.txt | uniq -d            # Show only duplicated lines
```

### अजीब
```bash
awk '{print $1, $3}' file.txt              # Print columns 1 and 3
awk -F',' '{print $2}' data.csv            # CSV: print 2nd column
awk '/ERROR/ {print NR": "$0}' log.txt     # Print ERROR lines with line numbers
awk '{sum += $1} END {print sum}' nums.txt # Sum first column
awk 'length($0) > 80' file.txt             # Lines longer than 80 chars
awk '{print toupper($0)}' file.txt         # Uppercase every line
awk -F: '{print $1}' /etc/passwd           # Usernames from passwd file
```

### सेड
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

### ग्रेप
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

## उपयोगी एक-पंक्ति
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

## स्क्रिप्टिंग पैटर्न
### तर्क विश्लेषण
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

### त्रुटि प्रबंधन
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

### निर्भरता की जाँच करना
```bash
for cmd in git docker python3; do
    if ! command -v "$cmd" &>/dev/null; then
        echo "Error: $cmd is not installed" >&2
        exit 1
    fi
done
```

### अस्थायी फ़ाइलें
```bash
TMPFILE=$(mktemp)
trap 'rm -f "$TMPFILE"' EXIT
echo "working..." > "$TMPFILE"
```

---

## सारांश
बैश स्क्रिप्टिंग कंप्यूटर के साथ काम करने वाले किसी भी व्यक्ति के लिए एक बल गुणक है। आपको हर झंडे को याद रखने की ज़रूरत नहीं है - आपको यह जानना होगा कि क्या संभव है और इसे कहाँ देखना है। बुनियादी बातों से शुरू करें: वेरिएबल, कंडीशनल, लूप, पाइप। फिर आवश्यकतानुसार टेक्स्ट प्रोसेसिंग टूल्स (grep, sed, awk) का उपयोग करें। और हमेशा`set -euo pipefail`का उपयोग करें - भविष्य में आप आभारी रहेंगे।