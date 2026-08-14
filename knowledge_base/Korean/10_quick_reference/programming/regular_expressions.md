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
# 정규식 치트 시트
정규식(regex)은 텍스트 일치를 위한 패턴입니다. 검색 및 바꾸기, 입력 유효성 검사, 로그 구문 분석, 데이터 추출 등 모든 곳에서 사용됩니다. 이것은 교과서가 아닌 실무 참고서입니다.
---

## 핵심 구문
### 리터럴 문자
대부분의 문자는 자신과 일치합니다. `a`는 "a"와 일치하고 `cat`는 "cat"과 일치합니다.
### 특수 문자(메타 문자)
이는 특별한 의미를 가지며 문자 그대로 일치시키려면 `\`로 이스케이프되어야 합니다.
| 캐릭터 | 의미 |
|------------|---------|
| `.`| 개행 문자를 제외한 모든 문자 |
| `^`| 문자열(또는 여러 줄 모드의 줄) 시작 |
| `$`| 문자열 끝(또는 여러 줄 모드의 줄) |
| `*`| 이전 항목 중 0개 이상 |
| `+`| 위 항목 중 1개 이상 |
| `?`| 위 항목 중 0 또는 1(`*?` ,`+?`를 사용하면 수량자를 게으르게 만듭니다) |
| `\|`| 교대(OR) |
| `()`| 그룹화 및 캡처 |
| `[]`| 캐릭터 클래스 |
| `{}`| 수량자 범위 |
| `\`| 이스케이프 문자 |
---

## 문자 클래스
| 패턴 | 경기 |
|---------|---------|
| `[abc]`| a, b 또는 c |
| `[a-z]`| 모든 소문자 |
| `[A-Z]`| 모든 대문자 |
| `[0-9]`| 임의의 숫자 |
| `[a-zA-Z]`| 모든 편지 |
| `[^abc]`| a, b 또는 c를 제외한 모든 항목(부정 클래스) |
| `[a-z0-9_]`| 소문자, 숫자, 밑줄 |
### 속기 수업
| 패턴 | 동등한 | 경기 |
|---------|------------|---------|
| `\d`| `[0-9]`| 숫자 |
| `\D`| `[^0-9]`| 숫자가 아닌 |
| `\w`| `[a-zA-Z0-9_]`| 단어 문자 |
| `\W`| `[^a-zA-Z0-9_]`| 비단어 문자 |
| `\s`| `[ \t\n\r\f]`| 공백(공백, 탭, 줄 바꿈 등) |
| `\S`| `[^\s]`| 공백이 아닌 |
---

## 수량자
| 수량자 | 의미 | 예 | 경기 |
|------------|---------|---------|---------|
| `*`| 0개 이상 | `ab*c`| ac, abc, abbc, abbbc |
| `+`| 1개 이상 | `ab+c`| abc, abbc, abbbc |
| `?`| 0 또는 1 | `ab?c`| 교류, ABC |
| `{n}`| 정확히 n | `a{3}`| 아아아 |
| `{n,}`| n 이상 | `a{2,}`| 아아아아아아아... |
| `{n,m}`| n과 m 사이 | `a{2,4}`| 아아아아아아아아아 |
### 욕심 많은 대 게으른
기본적으로 수량자는 **탐욕적**입니다(최대한 많이 일치함). `?`를 추가하여 **게으른**(가능한 한 적게 일치하도록) 만드세요.
| 패턴 | 문자열 | 그리디 매치 | 게으른 경기 |
|---------|---------|------------|------------|
| `<.*>`| `<b>hi</b>`|  `<b>hi</b>`(전체 문자열) | `<b>`및`</b>`별도로 |
| `<.+?>`| `<b>hi</b>`| — | `<b>`,`</b>`|
---

## 앵커
| 앵커 | 의미 |
|---------|---------|
| `^`| 문자열의 시작 |
| `$`| 문자열의 끝 |
| `\b`| 단어 경계 |
| `\B`| 비단어 경계 |
| `(?=...)`| 긍정적인 예측 |
| `(?!...)`| 부정적인 예측 |
| `(?<=...)`| 긍정적인 뒷모습 |
| `(?<!...)`| 부정적인 뒤돌아보기 |
**단어 경계 예**: `\bcat\b`는 "the cat sat"의 "cat"과 일치하지만 "category"에서는 일치하지 않습니다.
---

## 그룹 및 캡처
| 구문 | 설명 | 예 |
|---------|-------------|---------|
| `(abc)`| 캡처 그룹 | 일치 항목에서 "abc" 추출 |
| `(?:abc)`| 비캡처 그룹 | 캡쳐하지 않고 그룹화 |
| `\1`| 그룹 1에 대한 역참조 |  `(abc)\1`는 "abcabc"와 일치합니다 |
| `(?<name>abc)`| 명명된 캡처 그룹 | `(?<year>\d{4})`|
| `a(?=b)`| 긍정적인 예측 | "b"가 뒤에 오는 경우에만 "a"와 일치 |
| `a(?!b)`| 부정적인 예측 | "b"가 뒤에 오지 않는 경우에만 "a"와 일치 |
---

## 일반적인 패턴
### 유효성 검사
| 패턴 | 경기 | 메모 |
|---------|---------|-------|
| `^\d{5}$`| 미국 우편번호 | 정확히 5자리 |
| `^\d{5}(-\d{4})?$`| 미국 우편번호+4 | 5자리, 선택사항 -4 |
| `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`| 이메일 주소 | 쉽게 한; RFC 5322는 훨씬 더 복잡합니다 |
| `^https?:\/\/`| URL이 http:// 또는 https://로 시작 | |
| `^\+?[1-9]\d{1,14}$`| 전화번호(E.164 형식) | 국제표준 |
| `^(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)$`| IPv4 주소 | |
| `^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$`| IPv6 주소 | 단순화 |
| `^\d{3}-\d{2}-\d{4}$`| 미국 SSN 형식 | XXX-XX-XXXX |
| `^[A-Z]{1,2}\d{1,4}\s?\d[A-Z]{2}$`| 영국 우편번호 | 단순화 |
### 추출
| 패턴 | 추출물 |
|---------|----------|
| `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b`| 텍스트의 이메일 주소 |
| `https?:\/\/[^\s]+`| 텍스트의 URL |
| `\b\d{1,3}(\.\d{1,3}){3}\b`| 텍스트의 IPv4 주소 |
| `\d{4}-\d{2}-\d{2}`| ISO 날짜(YYYY-MM-DD) |
| `#[0-9a-fA-F]{6}\b`| 16진수 색상 코드 |
| `\$\d+(?:\.\d{2})?`| 달러 금액 |
### 텍스트 처리
| 패턴 | 목적 |
|---------|---------|
| `\s+`| 하나 이상의 공백 문자 일치(축소 공백) |
| `\r?\n`| 줄 바꿈 일치(\n 및 \r\n 모두 처리) |
| `^.*$`| 전체 줄 일치 |
| `<[^>]+>`| HTML/XML 태그 일치(단순화, 정규식으로 HTML을 구문 분석하지 않음) |
| `["']([^"']*)["']`| 인용된 문자열 일치 |
---

## 플래그/수정자
| 플래그 | 의미 | 효과 |
|------|---------|---------|
| `i`| 대소문자를 구분하지 않음 |  `cat`는 "Cat", "CAT", "cAt"와 일치 |
| `g`| 글로벌 | 첫 번째 일치 항목뿐만 아니라 모든 일치 항목 찾기 |
| `m`| 여러 줄 | `^`및 `$`는 문자열뿐만 아니라 줄 경계도 일치 |
| `s`| 도트 |  `.`는 개행 문자와 일치합니다 |
| `x`| 확장 | 공백을 무시하고 패턴에 주석을 허용 |
---

## 언어별 사용법
### 파이썬
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

### 자바스크립트
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

### grep / sed / awk (명령줄)
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

## 흔히 저지르는 실수
| 실수 | 문제 | 수정 |
|---------|---------|------|
|  `.*`는 욕심쟁이입니다 | 너무 많이 일치함 | 게으른 일치를 위해`.*?`사용 |
|`.`이스케이프를 잊어버린 경우 |  `file.txt`는 `fileXtxt`와도 일치합니다 |`file\.txt`사용 |
| 유효성 검사 패턴을 고정하지 않음 |  더 긴 문자열에 포함된`^\d{3}$`|`^`및`$`사용 |
|`[]`내부의 문자 클래스 |  `[\d+]`는 숫자가 아닌`\`,`d`,`+`와 일치합니다 |`[]`외부에서`\d`사용 또는`[0-9]`|
| 정규식으로 HTML 구문 분석 | HTML은 일반 언어가 아닙니다 | 실제 구문 분석을 위해 HTML 파서를 사용하십시오. 간단한 추출을 위한 정규식 OK |
| 치명적인 역추적 | `(a+)+`와 같은 중첩 수량자는 중단될 수 있습니다. | 패턴을 단순화하세요. 원자 그룹 사용 |
| 극단적인 경우를 테스트하지 않음 | 패턴은 행복한 경로에서 작동하지만 가장자리에서는 실패합니다 | 빈 문자열, 매우 긴 입력, 특수 문자로 테스트 |
---

## 테스트 도구
| 도구 | 유형 | URL |
|------|------|------|
| **정규식101** | 웹 | regex101.com — 설명과 실시간 매칭 |
| **RegExr** | 웹 | regexr.com — 치트시트를 사용한 대화형 테스트 |
| **정규식 크로스워드** | 게임 | regexcrossword.com — 퍼즐을 풀면서 배우기 |
---

## 요약
Regex는 텍스트의 패턴 일치를 위한 도구입니다. 간단하게 시작하세요. 대부분의 실제 패턴은 문자 클래스, 수량자, 앵커 및 그룹의 조합일 뿐입니다. 패턴을 코드에 넣기 전에 테스트 도구를 사용하여 패턴을 확인하세요. 그리고 기억하세요: 정규 표현식이 너무 복잡해져서 읽을 수 없다면, 대신 적절한 파서를 사용해야 할 때일 것입니다.