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
# 正则表达式备忘单
正则表达式 (regex) 是匹配文本的模式。它们无处不在——搜索和替换、输入验证、日志解析、数据提取等等。这是一本实用参考书，不是教科书。
---

## 核心语法
### 文字字符
大多数字符与自身匹配：`a` 匹配“a”，`cat` 匹配“cat”。
### 特殊字符（元字符）
这些具有特殊含义，必须使用`\`进行转义才能按字面匹配：
|人物 |意义|
|------------|---------|
| `.`|除换行符外的任何字符 |
| `^`|字符串的开头（或多行模式下的行）|
| `$`|字符串结束（或多行模式下的行结束）|
| `*`| 0 个或多个前述 |
| `+`|前述 1 个或多个 |
| `?`|前面的 0 或 1 个（使用`*?`、`+?`使量词变得惰性）|
| `\|`|交替 (OR) |
| `()`|分组和捕获|
| `[]`|角色类别|
| `{}`|量词范围 |
| `\`|转义字符|
---

## 字符类
|图案|比赛|
|---------|---------|
| `[abc]`| a、b 或 c |
| `[a-z]`|任何小写字母 |
| `[A-Z]`|任意大写字母 |
| `[0-9]`|任意数字|
| `[a-zA-Z]`|任意字母|
| `[^abc]`|除 a、b 或 c（否定类）之外的任何内容 |
| `[a-z0-9_]`|小写字母、数字、下划线|
### 速记类
|图案|同等|比赛|
|--------|------------|---------|
| `\d`| `[0-9]`|数字|
| `\D`| `[^0-9]`|非数字 |
| `\w`| `[a-zA-Z0-9_]`|字字符|
| `\W`| `[^a-zA-Z0-9_]`|非单词字符 |
| `\s`| `[ \t\n\r\f]`|空白（空格、制表符、换行符等）|
| `\S`| `[^\s]`|非空白 |
---

## 量词
|量词 |意义|示例|比赛|
|------------|---------|---------|---------|
| `*`| 0 或更多 | `ab*c`|交流、abc、abbc、abbbc |
| `+`| 1 个或多个 | `ab+c`| abc、abbc、abbbc |
| `?`| 0 或 1 | `ab?c`|交流，ABC |
| `{n}`|正是 n | `a{3}`|啊啊|
| `{n,}`| n 或更多 | `a{2,}`|啊啊啊啊啊啊……|
| `{n,m}`| n 和 m 之间 | `a{2,4}`|啊，啊啊，啊啊|
### 贪婪与懒惰
默认情况下，量词是**贪婪**（尽可能匹配）。添加`?`使它们**懒惰**（尽可能少地匹配）。
|图案|字符串|贪心匹配|懒惰匹配 |
|--------|--------|-------------|------------|
| `<.*>`| `<b>hi</b>`|  `<b>hi</b>`（整个字符串）| `<b>`和`</b>`分别 |
| `<.+?>`| `<b>hi</b>`| — |  `<b>`、`</b>` |
---

## 锚点
|锚|意义|
|--------|---------|
| `^`|字符串开头 |
| `$`|字符串结尾 |
| `\b`|字边界|
| `\B`|非字边界 |
| `(?=...)`|积极的前瞻 |
| `(?!...)`|负前瞻 |
| `(?<=...)`|积极的回顾 |
| `(?<!...)`|消极回顾 |
**字边界示例**：`\bcat\b` 匹配“the cat sat”中的“cat”，但不匹配“category”中的“cat”。
---

## 分组和捕获
|语法 |描述 |示例|
|--------|-------------|---------|
| `(abc)`|捕获组|从匹配中提取“abc”|
| `(?:abc)`|非捕获组 |分组而不捕获|
| `\1`|反向引用组 1 | `(abc)\1`匹配“abcabc”|
| `(?<name>abc)`|命名捕获组| `(?<year>\d{4})`|
| `a(?=b)`|积极的前瞻 |仅当后跟“b”时才匹配“a”|
| `a(?!b)`|负前瞻 |仅当后面没有“b”时才匹配“a” |
---

## 常见模式
＃＃＃ 验证
|图案|比赛|笔记|
|--------|---------|--------|
| `^\d{5}$`|美国邮政编码 |正好 5 位数字 |
| `^\d{5}(-\d{4})?$`|美国邮政编码+4 | 5 位数字，可选 -4 |
| `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`|电子邮件地址 |简化； RFC 5322 要复杂得多 |
| `^https?:\/\/`| URL 以 http:// 或 https:// 开头 | |
| `^\+?[1-9]\d{1,14}$`|电话号码（E.164 格式）|国际标准|
| `^(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)$`| IPv4地址| |
| `^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$`| IPv6地址|简化 |
| `^\d{3}-\d{2}-\d{4}$`|美国SSN格式| XXX-XX-XXXX |
| `^[A-Z]{1,2}\d{1,4}\s?\d[A-Z]{2}$`|英国邮政编码 |简化 |
### 提取
|图案|摘录|
|---------|----------|
| `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b`|文本中的电子邮件地址 |
| `https?:\/\/[^\s]+`|文本中的 URL |
| `\b\d{1,3}(\.\d{1,3}){3}\b`|文本中的 IPv4 地址 |
| `\d{4}-\d{2}-\d{2}`| ISO 日期 (YYYY-MM-DD) |
| `#[0-9a-fA-F]{6}\b`|十六进制颜色代码 |
| `\$\d+(?:\.\d{2})?`|美元金额 |
### 文本处理
|图案|目的|
|---------|---------|
| `\s+`|匹配一个或多个空白字符（折叠空格）|
| `\r?\n`|匹配换行符（处理 \n 和 \r\n） |
| `^.*$`|匹配整行 |
| `<[^>]+>`|匹配 HTML/XML 标签（简化；不要使用正则表达式解析 HTML）|
| `["']([^"']*)["']`|匹配带引号的字符串 |
---

## 标志/修饰符
|旗帜|意义|效果|
|------|---------|--------|
| `i`|不区分大小写 | `cat`匹配“Cat”、“CAT”、“cAt” |
| `g`|全球|查找所有匹配项，而不仅仅是第一个 |
| `m`|多行| `^`和`$`匹配行边界，而不仅仅是字符串 |
| `s`|多托尔 | `.`匹配换行符 |
| `x`|扩展|忽略空格并允许在模式中添加注释 |
---

## 特定于语言的用法
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

### grep / sed / awk（命令行）
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

## 常见错误
|错误|问题 |修复|
|---------|---------|-----|
| `.*`贪心 |匹配太多 |使用`.*?`进行惰性匹配 |
|忘记逃离`.` | `file.txt`也匹配`fileXtxt`|使用`file\.txt` |
|不锚定验证模式| `^\d{3}$`嵌入更长的字符串 |使用`^`和`$`|
|`[]`中的字符类 | `[\d+]`匹配`\`、`d`、`+`— 不是数字 |在`[]`或`[0-9]`之外使用`\d`|
|使用正则表达式解析 HTML | HTML 不是一种常规语言 |使用HTML解析器进行真正的解析；正则表达式可以进行简单提取|
|灾难性的回溯|像`(a+)+`这样的嵌套量词可以挂起 |简化图案；使用原子组 |
|不测试边缘情况 |模式在快乐的道路上有效，在边缘失败 |使用空字符串、很长的输入、特殊字符进行测试 |
---

## 测试工具
|工具|类型 |网址 |
|------|------|-----|
| **正则表达式101** |网页 | regex101.com — 实时匹配及解释 |
| **正则表达式** |网页 | regexr.com — 使用备忘单进行交互式测试 |
| **正则表达式填字游戏** |游戏| regexcrossword.com — 通过解决难题来学习 |
---

＃＃ 概括
正则表达式是一种用于文本模式匹配的工具。从简单开始——大多数现实世界的模式只是字符类、量词、锚点和组的组合。在将模式放入代码之前，使用测试工具来验证您的模式。请记住：如果您的正则表达式变得如此复杂以至于您无法阅读它，那么可能是时候使用合适的解析器了。