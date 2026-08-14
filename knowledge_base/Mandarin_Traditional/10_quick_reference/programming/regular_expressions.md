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

# 正規表示式備忘單
正規表示式 (regex) 是符合文字的模式。它們無所不在——搜尋和替換、輸入驗證、日誌解析、資料提取等等。這是一本實用參考書，不是教科書。
---

## 核心語法
### 文字字符
大多數字元與自身匹配：`a` 匹配“a”，`cat` 匹配“cat”。
### 特殊字元（元字元）
這些具有特殊意義，必須使用`\`進行轉義才能按字面匹配：
|人物 |意義|
|------------|---------|
|`.`|除換行符號以外的任何字元 |
|`^`|字串的開頭（或多行模式下的行）|
|`$`|字串結束（或多行模式下的行結束）|
|`*`| 0 個或多個前述 |
|`+`|前述 1 個或更多 |
|`?`|前面的 0 或 1 個（使用`*?`、`+?`使量詞變得惰性）|
|`\|`|交替 (OR) |
|`()`|分組與擷取|
|`[]`|角色類別|
|`{}`|量詞範圍 |
|`\`|轉義字元|
---

## 字元類
|圖案|比賽|
|---------|---------|
|`[abc]`| a、b 或 c |
|`[a-z]`|任何小寫字母 |
|`[A-Z]`|任意大寫字母 |
|`[0-9]`|任意數字|
|`[a-zA-Z]`|任意字母|
|`[^abc]`| a、b 或 c（否定類）以外的任何內容 |
|`[a-z0-9_]`|小寫字母、數字、底線|
### 速記類
|圖案|同等|比賽|
|--------|------------|---------|
|`\d`|`[0-9]`|數位|
|`\D`|`[^0-9]`|非數字 |
|`\w`|`[a-zA-Z0-9_]`|字字元|
|`\W`|`[^a-zA-Z0-9_]`|非單字字元 |
|`\s`|`[ \t\n\r\f]`|空白（空格、製表符、換行符等）|
|`\S`|`[^\s]`|非空白 |
---

## 量詞
|量詞 |意義|範例|比賽|
|------------|---------|---------|---------|
|`*`| 0 或更多 |`ab*c`|交流、abc、abbc、abbbc |
|`+`| 1 個或更多 |`ab+c`| abc、abbc、abbbc |
|`?`| 0 或 1 |`ab?c`|交流，ABC |
|`{n}`|正是 n |`a{3}`|啊啊|
|`{n,}`| n 或更多 |`a{2,}`|啊啊啊啊啊啊…|
|`{n,m}`| n 和 m 之間 |`a{2,4}`|啊，啊啊，啊啊|
### 貪婪與懶惰
預設情況下，量詞是**貪婪**（盡可能匹配）。添加`?`使它們**懶惰**（盡可能少地匹配）。
|圖案|字串|貪心匹配|懶惰匹配 |
|--------|--------|-------------|------------|
|`<.*>`|`<b>hi</b>`| `<b>hi</b>`（整個字串）|`<b>`和`</b>`分別 |
|`<.+?>`|`<b>hi</b>`| — | `<b>`、`</b>` |
---

## 錨點
|錨|意義|
|--------|---------|
|`^`|字串開頭 |
|`$`|字串結束 |
|`\b`|字邊界|
|`\B`|非字邊界 |
|`(?=...)`|積極的前瞻性 |
|`(?!...)`|負前瞻 |
|`(?<=...)`|正面的回顧 |
|`(?<!...)`|負面回顧 |
**字邊界範例**：`\bcat\b` 符合“the cat sat”中的“cat”，但不符合“category”中的“cat”。
---

## 分組和捕獲
|語法 |描述 |範例|
|--------|-------------|---------|
|`(abc)`|捕獲組|從匹配中提取“abc”|
|`(?:abc)`|非捕獲組 |分組而不捕獲|
|`\1`|反向引用群組 1 |`(abc)\1`符合「abcabc」|
|`(?<name>abc)`|命名擷取群組|`(?<year>\d{4})`|
|`a(?=b)`|積極的前瞻性 |僅當後跟“b”時才匹配“a”|
|`a(?!b)`|負前瞻 |只有在後面沒有「b」時才符合「a」 |
---

## 常見模式
＃＃＃ 驗證
|圖案|比賽|筆記|
|--------|---------|--------|
|`^\d{5}$`|美國郵遞區號 |剛好 5 位數 |
|`^\d{5}(-\d{4})?$`|美國郵遞區號+4 | 5 位數字，可選 -4 |
|`^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`|電子郵件地址 |簡化；RFC 5322 要複雜得多 |
|`^https?:\/\/`| URL 以 http:// 或 https:// 開頭 | |
|`^\+?[1-9]\d{1,14}$`|電話號碼（E.164 格式）|國際標準|
|`^(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)$`| IPv4位址| |
|`^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$`| IPv6位址|簡化 |
|`^\d{3}-\d{2}-\d{4}$`|美國SSN格式| XXX-XX-XXXX |
|`^[A-Z]{1,2}\d{1,4}\s?\d[A-Z]{2}$`|英國郵遞區號 |簡化 |
### 提取
|圖案|摘錄|
|---------|----------|
|`\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b`|文字中的電子郵件地址 |
| `https?:\/\/[^\s]+`|文本中的 URL |
| `\b\d{1,3}(\.\d{1,3}){3}\b`|文本中的 IPv4 地址 |
| `\d{4}-\d{2}-\d{2}`| ISO 日期 (YYYY-MM-DD) |
| `#[0-9a-fA-F]{6}\b`|十六进制颜色代码 |
| `\$\d+(?:\.\d{2})?`|美元金额 |
### 文字處理
|圖案|目的|
|---------|---------|
|`\s+`|符合一個或多個空白字元（折疊空格）|
|`\r?\n`|符合換行符號（處理 \n 和 \r\n） |
|`^.*$`|符合整行 |
|`<[^>]+>`|符合 HTML/XML 標籤（簡化；不要使用正規表示式解析 HTML）|
|`["']([^"']*)["']`|符合引號的字串 |
---

## 標誌/修飾符
|旗幟|意義|效果|
|------|---------|--------|
|`i`|不區分大小寫 |`cat`符合「Cat」、「CAT」、「cAt」 |
|`g`|全球|尋找所有匹配項，而不僅僅是第一個 |
|`m`|多行|`^`和`$`符合行邊界，而不僅僅是字串 |
|`s`|多托爾 |`.`匹配換行符 |
|`x`|擴充|忽略空格並允許在模式中新增註解 |
---

## 特定於語言的用法
＃＃＃ Python
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

### grep / sed / awk（命令列）
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

## 常見錯誤
|錯誤|問題 |修復|
|---------|---------|-----|
|`.*`貪心 |搭配太多 |使用`.*?`進行惰性匹配 |
|忘記逃離`.` |`file.txt`也配對`fileXtxt`|使用`file\.txt` |
|不錨定驗證模式|`^\d{3}$`嵌入更長的字串 |使用`^`和`$`|
|`[]`中的字元類別 |`[\d+]`匹配`\`、`d`、`+`— 不是數字 |在`[]`或`+`— 不是數字 |QQZ14X5XQZ 或`[0-9]`|
|使用正規表示式解析 HTML | HTML 不是一種常規語言 |使用HTML解析器進行真正的解析；正規表示式可以簡單提取|
|災難性的回溯|像`(a+)+`這樣的嵌套量詞可以掛起 |簡化圖案；使用原子組 |
|不測試邊緣情況 |模式在快樂的道路上有效，在邊緣失敗 |使用空字串、很長的輸入、特殊字元進行測試 |
---

## 測試工具
|工具|類型 |網址 |
|------|------|-----|
| **正規表示式101** |網頁 | regex101.com — 即時比對及解釋 |
| **正規表示式** |網頁 | regexr.com — 使用備忘單進行互動式測試 |
| **正規表示式填字遊戲** |遊戲| regexcrossword.com — 透過解題來學習 |
---

＃＃ 概括
正規表示式是一種用於文字模式匹配的工具。從簡單開始——大多數現實世界的模式只是字符類、量詞、錨點和組的組合。在將模式放入程式碼之前，請使用測試工具來驗證您的模式。請記住：如果您的正規表示式變得如此複雜以至於您無法閱讀它，那麼可能是時候使用合適的解析器了。