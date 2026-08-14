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
# برگه تقلب عبارات منظم
عبارات منظم (regex) الگوهایی برای مطابقت متن هستند. آنها در همه جا استفاده می شوند - جستجو و جایگزینی، اعتبار سنجی ورودی، تجزیه گزارش، استخراج داده ها، و موارد دیگر. این یک مرجع عملی است نه یک کتاب درسی.
---

## نحو هسته
### شخصیت های تحت اللفظی
بیشتر کاراکترها با خودشان مطابقت دارند:`a`با "a"،`cat`با "cat" مطابقت دارد.
### کاراکترهای خاص (فراداکترها)
اینها معنای خاصی دارند و باید با`\`حذف شوند تا به معنای واقعی کلمه مطابقت داشته باشند:
| شخصیت | معنی |
|-----------|---------|
| `.`| هر کاراکتری به جز خط جدید |
|  `^` | شروع رشته (یا خط در حالت چند خطی) |
| `$`| انتهای رشته (یا خط در حالت چند خطی) |
|  `*` | 0 یا بیشتر از موارد قبلی |
| `+`| 1 یا بیشتر از موارد قبلی |
| `?`| 0 یا 1 مورد قبل (با استفاده از `*?`، `+?`، ​​کمی‌سازها را تنبل می‌کند) |
| `\|`| جایگزینی (OR) |
|  `()` | گروه بندی و گرفتن |
| `[]`| کلاس کاراکتر |
| `{}`| محدوده کمیت |
| `\`| شخصیت فرار |
---

## کلاس های شخصیت
| الگو | مسابقات |
|---------|---------|
| `[abc]`| a، b، یا c |
|  `[a-z]` | هر حرف کوچک |
| `[A-Z]`| هر حرف بزرگ |
|  `[0-9]` | هر رقمی |
| `[a-zA-Z]`| هر حرف |
| `[^abc]`| هر چیزی به جز a، b یا c (کلاس منفی) |
|  `[a-z0-9_]` | حروف کوچک، اعداد، زیرخط |
### کلاس های کوتاه نویسی
| الگو | معادل | مسابقات |
|---------|-----------|---------|
| `\d`|  `[0-9]` | رقم |
| `\D`|  `[^0-9]` | غیر رقمی |
| `\w`| `[a-zA-Z0-9_]`| کاراکتر کلمه |
|  `\W` | `[^a-zA-Z0-9_]`| کاراکتر غیرکلمه ای |
| `\s`|  `[ \t\n\r\f]` | فضای خالی (فضا، برگه، خط جدید و غیره) |
| `\S`| `[^\s]`| بدون فضای سفید |
---

## کمیت کننده ها
| کمیت | معنی | مثال | مسابقات |
|-----------|---------|---------|---------|
| `*`| 0 یا بیشتر |  `ab*c` | ac, abc, abbc, abbbc |
| `+`| 1 یا بیشتر |  `ab+c` | abc, abbc, abbbc |
| `?`| 0 یا 1 | `ab?c`| ac, abc |
|  `{n}` | دقیقا n | `a{3}`| aaa |
| `{n,}`| n یا بیشتر |  `a{2,}` | آآآآآآآآآآآآآآ... |
| `{n,m}`| بین n و m | `a{2,4}`| aa, aaa, aaaa |
### حریص در مقابل تنبل
به‌طور پیش‌فرض، کمی‌سازها ** حریصانه** هستند (تا حد امکان مطابقت دارند).`?`را اضافه کنید تا آنها را **تنبل** کنید (تا حد امکان کمتر مطابقت داشته باشد).
| الگو | رشته | حریص مسابقه | کبریت تنبل |
|---------|--------|------------|------------|
| `<.*>`|  `<b>hi</b>` | `<b>hi</b>`(کل رشته) | `<b>`و`</b>`به طور جداگانه |
| `<.+?>`|  `<b>hi</b>` | — |  `<b>`، ​​`</b>` |
---

## لنگرها
| لنگر | معنی |
|--------|---------|
| `^`| شروع رشته |
|  `<b>hi</b>` | انتهای رشته |
| `\b`| مرز کلمه |
|  `*` | مرز غیر کلمه |
| `(?=...)`| نگاه مثبت |
| `(?!...)`| پیش بینی منفی |
|  `<b>hi</b>` | نگاه مثبت به پشت |
| `(?<!...)`| نگاه منفی به پشت |
**مثال مرز کلمه**:`\bcat\b`با «cat» در «گربه نشسته» مطابقت دارد اما در «رده» نه.
---

## گروه ها و گرفتن
| نحو | توضیحات | مثال |
|--------|------------|---------|
| `(abc)`| گروه گرفتن | استخراج "abc" از یک مسابقه |
|  `<b>hi</b>` | گروه غیر اسیر | گروه بدون گرفتن |
| `\1`| ارجاع به گروه 1 | `(abc)\1`با "abcabc" مطابقت دارد |
| `(?<name>abc)`| نام گروه گرفتن | `(?<year>\d{4})`|
|  `<b>hi</b>` | نگاه مثبت | فقط در صورتی با "a" مطابقت دهید که "b" |
| `a(?!b)`| پیش بینی منفی | فقط در صورتی با "a" مطابقت دهید که "b" دنبال نشود |
---

## الگوهای رایج
### اعتبارسنجی
| الگو | مسابقات | یادداشت ها |
|---------|---------|-------|
| `^\d{5}$`| کد پستی ایالات متحده | دقیقا 5 رقمی |
|  `<b>hi</b>` | ZIP+4 ایالات متحده | 5 رقمی، اختیاری -4 |
| `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`| آدرس ایمیل | ساده شده؛ RFC 5322 بسیار پیچیده تر است |
|  `*` | URL با http:// یا https:// | شروع می شود |
| `^\+?[1-9]\d{1,14}$`| شماره تلفن (فرمت E.164) | استاندارد بین المللی |
| `^(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)$`| آدرس IPv4 | |
|  `<b>hi</b>` | آدرس IPv6 | ساده شده |
| `^\d{3}-\d{2}-\d{4}$`| فرمت SSN ایالات متحده | XXX-XXX-XXXX |
| `^[A-Z]{1,2}\d{1,4}\s?\d[A-Z]{2}$`| کد پستی انگلستان | ساده شده |
### استخراج
| الگو | عصاره ها |
|---------|----------|
| `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b`| آدرس ایمیل از متن |
|  `<b>hi</b>` | URL از متن |
| `\b\d{1,3}(\.\d{1,3}){3}\b`| آدرس های IPv4 از متن |
|  `*` | تاریخ ISO (YYYY-MM-DD) |
| `#[0-9a-fA-F]{6}\b`| کدهای رنگ هگز |
| `\$\d+(?:\.\d{2})?`| مقادیر دلار |
### پردازش متن
| الگو | هدف |
|---------|---------|
| `\s+`| تطبیق یک یا چند کاراکتر فضای خالی (فضاهای کوچک) |
|  `<b>hi</b>` | شکست خط مطابقت (هم \n و هم \r\n را کنترل می کند) |
| `^.*$`| مطابقت یک خط کامل |
|  `*` | تگ های HTML/XML را مطابقت دهید (ساده شده؛ HTML را با regex تجزیه نکنید) |
| `["']([^"']*)["']`| مطابقت با رشته های نقل قول |
---

## پرچم ها / اصلاح کننده ها
| پرچم | معنی | اثر |
|------|---------|--------|
| `i`| حساس به حروف بزرگ و کوچک | `cat`"Cat"، "CAT"، "cAt" |
| `g`| جهانی | همه موارد منطبق را پیدا کنید، نه فقط اولین |
|  `*` | چند خطی | `^`و`$`با مرزهای خط مطابقت دارند، نه فقط رشته |
|  `<b>hi</b>` | دوتال | `.`با کاراکترهای خط جدید مطابقت دارد |
| `x`| تمدید شده | فضای خالی را نادیده بگیرید و اجازه دهید نظرات در الگوی |
---

## استفاده خاص زبان
### پایتون
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

### جاوا اسکریپت
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

### grep / sed / awk (خط فرمان)
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

## اشتباهات رایج
| اشتباه | مشکل | رفع |
|---------|---------|-----|
| `.*`حریص است | منطبق بیش از حد | استفاده از`.*?`برای تطبیق تنبل |
| فراموش کردن فرار`.`| `file.txt`با`fileXtxt`نیز مطابقت دارد | استفاده از`file\.txt`|
| الگوهای اعتبار سنجی | `^\d{3}$`تعبیه شده در رشته طولانی تر | استفاده از`^`و`$`|
| کلاس کاراکتر در`[]`| `[\d+]`با `\`، `d`،`+`مطابقت دارد — نه رقم | استفاده از`\d`در خارج از `[]`، یا`[0-9]`|
| تجزیه HTML با regex | HTML یک زبان معمولی نیست | از یک تجزیه کننده HTML برای تجزیه واقعی استفاده کنید. regex OK برای استخراج ساده |
| عقب نشینی فاجعه بار | کمیت‌سازهای تودرتو مانند`(a+)+`می‌توانند آویزان شوند | الگو را ساده کنید؛ استفاده از گروه های اتمی |
| تست نشدن موارد لبه | الگو در مسیر شاد کار می کند، در لبه شکست می خورد | تست با رشته های خالی، ورودی بسیار طولانی، کاراکترهای ویژه |
---

## ابزارهای تست
| ابزار | نوع | آدرس اینترنتی |
|------|------|-----|
| **Regex101** | وب | regex101.com — تطبیق بلادرنگ با توضیح |
| **RegExr** | وب | regexr.com — تست تعاملی با چیت شیت |
| **regex-crossword** | بازی | regexcrossword.com — آموزش با حل پازل |
---

## خلاصه
Regex ابزاری برای تطبیق الگو در متن است. ساده شروع کنید - بیشتر الگوهای دنیای واقعی فقط ترکیبی از کلاس‌های کاراکتر، کمی‌کننده‌ها، لنگرها و گروه‌ها هستند. از یک ابزار تست برای تأیید الگوهای خود قبل از قرار دادن آنها در کد استفاده کنید. و به یاد داشته باشید: اگر regex شما آنقدر پیچیده می شود که نمی توانید آن را بخوانید، احتمالاً زمان آن رسیده است که به جای آن از تجزیه کننده مناسب استفاده کنید.