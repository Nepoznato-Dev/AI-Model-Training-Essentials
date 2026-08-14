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

# ریگولر ایکسپریشن چیٹ شیٹ
ریگولر ایکسپریشنز (ریجیکس) متن کو ملانے کے پیٹرن ہیں۔ وہ ہر جگہ استعمال ہوتے ہیں — تلاش اور بدلنا، ان پٹ کی توثیق، لاگ پارس کرنا، ڈیٹا نکالنا، اور بہت کچھ۔ یہ ایک عملی حوالہ ہے، نصابی کتاب نہیں۔
---

## بنیادی نحو
### لغوی حروف
زیادہ تر حروف خود سے ملتے ہیں:`a`"a" سے ملتا ہے،`cat`"بلی" سے ملتا ہے۔
### خصوصی کردار (میٹاکریکٹر)
یہ خاص معنی رکھتے ہیں اور لفظی طور پر مماثل ہونے کے لیے`\`کے ساتھ فرار ہونا ضروری ہے:
| کردار | معنی |
|------------|---------|
| `.`| نیو لائن کے علاوہ کوئی بھی کردار |
| `^`| سٹرنگ کا آغاز (یا ملٹی لائن موڈ میں لائن) |
| `$`| سٹرنگ کا اختتام (یا ملٹی لائن موڈ میں لائن) |
| `*`| 0 یا پچھلے سے زیادہ |
| `+`| 1 یا پہلے سے زیادہ |
| `?`| پچھلے کا 0 یا 1 (`*?` ,`+?`کے ساتھ کوانٹیفائر کو سست بناتا ہے) |
| `\|`| الٹرنیشن (OR) |
| `()`| گروپ بندی اور گرفتاری |
| `[]`| کریکٹر کلاس |
| `{}`| کوانٹیفائر رینج |
| `\`| فرار کردار |
---

## کریکٹر کلاسز
| پیٹرن | میچز |
|---------|---------|
| `[abc]`| a، b، یا c |
| `[a-z]`| کوئی بھی چھوٹے حروف |
| `[A-Z]`| کوئی بھی بڑے حروف |
| `[0-9]`| کوئی بھی ہندسہ |
| `[a-zA-Z]`| کوئی بھی خط |
| `[^abc]`| a، b، یا c کے علاوہ کچھ بھی (منفی کلاس) |
| `[a-z0-9_]`| چھوٹے حروف، ہندسے، انڈر سکور |
### شارٹ ہینڈ کلاسز
| پیٹرن | مساوی | میچز |
|---------|------------|---------|
| `\d`| `[0-9]`| ہندسہ |
| `\D`| `[^0-9]`| غیر ہندسے |
| `\w`| `[a-zA-Z0-9_]`| لفظ کردار |
| `\W`| `[^a-zA-Z0-9_]`| غیر لفظی کردار |
| `\s`| `[ \t\n\r\f]`| وائٹ اسپیس (اسپیس، ٹیب، نیو لائن، وغیرہ) |
| `\S`| `[^\s]`| غیر وائٹ اسپیس |
---

## کوانٹیفائرز
| کوانٹیفائر | معنی | مثال | میچز |
|------------|---------|---------|---------|
| `*`| 0 یا اس سے زیادہ | `ab*c`| ac, abc, abbc, abbbc |
| `+`| 1 یا زیادہ | `ab+c`| abc, abbc, abbbc |
| `?`| 0 یا 1 | `ab?c`| ac, abc |
| `{n}`| بالکل ن | `a{3}`| aaa |
| `{n,}`| n یا اس سے زیادہ | `a{2,}`| آ، آآ، آآا... |
| `{n,m}`| n اور m کے درمیان | `a{2,4}`| aa, aaaa, aaaa |
### لالچی بمقابلہ سست
پہلے سے طے شدہ طور پر، کوانٹیفائر **لالچی** ہوتے ہیں (زیادہ سے زیادہ میچ کریں)۔ انہیں **سست** بنانے کے لیے`?`شامل کریں (جتنا ممکن ہو کم میچ کریں)۔
| پیٹرن | سٹرنگ | لالچی میچ | سست میچ |
|---------|---------|---------------|------------|
| `<.*>`| `<b>hi</b>`| `<b>hi</b>`(پوری تار) | `<b>`اور`</b>`الگ الگ |
| `<.+?>`| `<b>hi</b>`| - | `<b>`,`</b>`|
---

## اینکرز
| اینکر | معنی |
|---------|---------|
| `^`| سٹرنگ کا آغاز |
| `$`| سٹرنگ کا اختتام |
| `\b`| لفظ کی حد |
| `\B`| غیر لفظی حد |
| `(?=...)`| مثبت نظر |
| `(?!...)`| منفی نظر |
| `(?<=...)`| مثبت نظر کے پیچھے |
| `(?<!...)`| منفی نظر کے پیچھے |
**لفظ کی حد کی مثال**:`\bcat\b`"کیٹ سیٹ" میں "کیٹ" سے مماثل ہے لیکن "زمرہ" میں نہیں۔
---

## گروپس اور کیپچرنگ
| نحو | تفصیل | مثال |
|---------|------------|---------|
| `(abc)`| کیپچرنگ گروپ | ایک میچ سے "abc" نکالیں |
| `(?:abc)`| نان کیپچرنگ گروپ | کیپچر کیے بغیر گروپ |
| `\1`| گروپ 1 کے پیچھے حوالہ | `(abc)\1`"abcabc" سے میل کھاتا ہے |
| `(?<name>abc)`| نام کیپچرنگ گروپ | `(?<year>\d{4})`|
| `a(?=b)`| مثبت نظر | "a" کو صرف اس صورت میں جوڑیں جب اس کے بعد "b" |
| `a(?!b)`| منفی نظر | "a" کو صرف اس صورت میں جوڑیں جب اس کے بعد "b" نہ ہو۔
---

## مشترکہ پیٹرن
### توثیق
| پیٹرن | میچز | نوٹس |
|---------|---------|-------|
| `^\d{5}$`| امریکی زپ کوڈ | بالکل 5 ہندسے |
| `^\d{5}(-\d{4})?$`| US ZIP+4 | 5 ہندسے، اختیاری -4 |
| `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`| ای میل ایڈریس | آسان RFC 5322 کہیں زیادہ پیچیدہ ہے |
| `^https?:\/\/`| URL http:// یا https:// | سے شروع ہوتا ہے۔ |
| `^\+?[1-9]\d{1,14}$`| فون نمبر (E.164 فارمیٹ) | بین الاقوامی معیار |
| `^(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)$`| IPv4 پتہ | |
| `^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$`| IPv6 پتہ | آسان |
| `^\d{3}-\d{2}-\d{4}$`| US SSN فارمیٹ | XXX-XXX-XXXX |
| `^[A-Z]{1,2}\d{1,4}\s?\d[A-Z]{2}$`| یو کے پوسٹ کوڈ | آسان |
### نکالنا
| پیٹرن | نچوڑ |
|---------|------------|
| `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b`| متن سے ای میل پتے |
| `https?:\/\/[^\s]+`| متن سے URLs |
| `\b\d{1,3}(\.\d{1,3}){3}\b`| متن سے IPv4 پتے |
| `\d{4}-\d{2}-\d{2}`| ISO تاریخیں (YYYY-MM-DD) |
| `#[0-9a-fA-F]{6}\b`| ہیکس کلر کوڈز |
| `\$\d+(?:\.\d{2})?`| ڈالر کی مقدار |
### ٹیکسٹ پروسیسنگ
| پیٹرن | مقصد |
|---------|---------|
| `\s+`| ایک یا زیادہ وائٹ اسپیس حروف سے ملائیں (خالی جگہیں) |
| `\r?\n`| میچ لائن بریکس (\n اور \r\n دونوں کو ہینڈل کرتا ہے) |
| `^.*$`| ایک پوری لائن سے ملائیں |
| `<[^>]+>`| HTML/XML ٹیگز سے میچ کریں (آسان؛ HTML کو regex کے ساتھ پارس نہ کریں) |
| `["']([^"']*)["']`| اقتباس کردہ تاروں کو میچ کریں |
---

## جھنڈے / ترمیم کرنے والے
| پرچم | معنی | اثر |
|------|---------|---------|
| `i`| کیس غیر حساس | `cat`"Cat", "CAT", "cAt" | سے مماثل ہے۔
| `g`| عالمی | تمام میچ تلاش کریں، نہ صرف پہلا |
| `m`| ملٹی لائن | `^`اور`$`لائن کی حدود سے مماثل ہے، نہ کہ صرف تار |
| `s`| ڈوٹل | `.`نئے لائن حروف سے میل کھاتا ہے |
| `x`| توسیعی | خالی جگہ کو نظر انداز کریں اور پیٹرن میں تبصروں کی اجازت دیں |
---

## زبان کا مخصوص استعمال
### ازگر
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

### جاوا اسکرپٹ
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

### grep / sed / awk (کمانڈ لائن)
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

## عام غلطیاں
| غلطی | مسئلہ | درست کریں |
|---------|---------|------|
| `.*`لالچی ہے | بہت زیادہ میچ | سست میچنگ کے لیے`.*?`استعمال کریں۔
|`.`سے فرار ہونا بھول جانا | `file.txt``fileXtxt` سے بھی میل کھاتا ہے |`file\.txt`استعمال کریں۔
| توثیق کے نمونوں کو لنگر انداز نہیں کرنا | `^\d{3}$`لمبی تار میں سرایت شدہ |`^`اور`$`استعمال کریں۔
|`[]`کے اندر کریکٹر کلاس | `[\d+]``\` ,`d`,`+`سے مماثل ہے — ہندسے نہیں |`\d``[]`، یا`[0-9]`سے باہر استعمال کریں |
| HTML کو regex کے ساتھ پارس کرنا | HTML ایک باقاعدہ زبان نہیں ہے | حقیقی تجزیہ کے لیے HTML پارسر استعمال کریں۔ regex OK سادہ نکالنے کے لیے |
| تباہ کن بیک ٹریکنگ |`(a+)+`جیسے نیسٹڈ کوانٹیفائر لٹک سکتے ہیں | پیٹرن کو آسان بنائیں؛ جوہری گروپوں کا استعمال کریں |
| ایج کیسز کی جانچ نہیں کر رہا ہے | پیٹرن خوشگوار راستے پر کام کرتا ہے، کنارے پر ناکام ہوجاتا ہے | خالی تاروں، بہت طویل ان پٹ، خصوصی حروف کے ساتھ ٹیسٹ کریں |
---

## ٹیسٹنگ ٹولز
| ٹول | قسم | URL |
|------|------|------|
| **Regex101** | ویب | regex101.com — وضاحت کے ساتھ اصل وقت کی مماثلت |
| **RegExr** | ویب | regexr.com - چیٹ شیٹ کے ساتھ انٹرایکٹو ٹیسٹنگ |
| **ریجیکس-کراس ورڈ** | کھیل | regexcrossword.com - پہیلیاں حل کرکے سیکھیں |
---

## خلاصہ
Regex متن میں پیٹرن کے ملاپ کے لیے ایک ٹول ہے۔ سادہ شروع کریں — زیادہ تر حقیقی دنیا کے نمونے صرف کریکٹر کلاسز، کوانٹیفائرز، اینکرز اور گروپس کا مجموعہ ہیں۔ کوڈ میں ڈالنے سے پہلے اپنے نمونوں کی تصدیق کرنے کے لیے ٹیسٹنگ ٹول کا استعمال کریں۔ اور یاد رکھیں: اگر آپ کا ریجیکس اتنا پیچیدہ ہو رہا ہے کہ آپ اسے پڑھ نہیں سکتے، تو شاید اس کے بجائے مناسب تجزیہ کار استعمال کرنے کا وقت آگیا ہے۔