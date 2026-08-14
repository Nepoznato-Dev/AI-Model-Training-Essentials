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
# 正規表現のチートシート
正規表現 (regex) は、テキストを照合するためのパターンです。これらは、検索と置換、入力検証、ログ解析、データ抽出など、あらゆる場所で使用されます。これは教科書ではなく実用的な参考書です。
---

## コア構文
### リテラル文字
ほとんどの文字はそれ自体に一致します。`a` は「a」に一致し、`cat` は「cat」に一致します。
### 特殊文字 (メタキャラクター)
これらには特別な意味があり、文字通り一致させるには`\`でエスケープする必要があります。
|キャラクター |意味 |
|----------|----------|
| `.`|改行を除く任意の文字 |
| `^`|文字列 (または複数行モードの行) の先頭 |
| `$`|文字列 (または複数行モードの行) の終わり |
| `*`|前述の | の 0 個以上
| `+`|前述の 1 つ以上の |
| `?`|前述の 0 または 1 (`*?`、`+?`で量指定子を遅延させます) |
| `\|`|代替 (OR) |
| `()`|グループ化とキャプチャ |
| `[]`|文字クラス |
| `{}`|量指定子の範囲 |
| `\`|エスケープ文字 |
---

## 文字クラス
|パターン |マッチ |
|----------|----------|
| `[abc]`| a、b、または c |
| `[a-z]`|任意の小文字 |
| `[A-Z]`|任意の大文字 |
| `[0-9]`|任意の数字 |
| `[a-zA-Z]`|任意の文字 |
| `[^abc]`| a、b、または c 以外のすべて (否定クラス) |
| `[a-z0-9_]`|小文字、数字、アンダースコア |
### 短縮クラス
|パターン |同等 |マッチ |
|----------|-----------|----------|
| `\d`| `[0-9]`|数字 |
| `\D`| `[^0-9]`|数字以外の |
| `\w`| `[a-zA-Z0-9_]`|単語の文字 |
| `\W`| `[^a-zA-Z0-9_]`|単語以外の文字 |
| `\s`| `[ \t\n\r\f]`|ホワイトスペース (スペース、タブ、改行など) |
| `\S`| `[^\s]`|空白文字以外 |
---

## 量指定子
|数量子 |意味 |例 |マッチ |
|----------|-----------|-----------|-----------|
| `*`| 0以上 | `ab*c`| ac、abc、abbc、abbbc |
| `+`| 1 つ以上 | `ab+c`| abc、abbc、abbc |
| `?`| 0 または 1 | `ab?c`| ac、abc |
| `{n}`|まさにn | `a{3}`|ああ |
| `{n,}`| n以上 | `a{2,}`|ああ、ああ、ああ... |
| `{n,m}`| n と m の間 | `a{2,4}`|ああ、ああ、ああ |
### 貪欲 vs 怠け者
デフォルトでは、量指定子は **貪欲** (可能な限り一致する) です。`?`を追加して **lazy** にします (一致をできるだけ少なくします)。
|パターン |文字列 |貪欲な試合 |レイジーマッチ |
|-----------|----------|---------------|------------|
| `<.*>`| `<b>hi</b>`| `<b>hi</b>`(文字列全体) | `<b>`と`</b>`を個別に |
| `<.+?>`| `<b>hi</b>`| — |  `<b>`、`</b>` |
---

## アンカー
|アンカー |意味 |
|--------|--------|
| `^`|文字列の先頭 |
| `$`|文字列の終わり |
| `\b`|単語の境界 |
| `\B`|非単語境界 |
| `(?=...)`|前向きな先読み |
| `(?!...)`|否定的な先読み |
| `(?<=...)`|ポジティブな後読み |
| `(?<!...)`|否定的な後読み |
**単語境界の例**:`\bcat\b`は、「the cat sat」の「cat」に一致しますが、「category」には一致しません。
---

## グループとキャプチャ
|構文 |説明 |例 |
|----------|---------------|----------|
| `(abc)`|キャプチャーグループ |一致から「abc」を抽出する |
| `(?:abc)`|非捕捉グループ |キャプチャせずにグループ化 |
| `\1`|グループ 1 への後方参照 | `(abc)\1`は「abcabc」と一致します。
| `(?<name>abc)`|名前付きキャプチャ グループ | `(?<year>\d{4})`|
| `a(?=b)`|前向きな先読み | 「a」の後に「b」が続く場合にのみ一致します。
| `a(?!b)`|否定的な先読み | 「a」の後に「b」が続かない場合にのみ一致します。
---

## 一般的なパターン
### 検証
|パターン |マッチ |メモ |
|-------|-------|------|
| `^\d{5}$`|米国の郵便番号 |ちょうど 5 桁 |
| `^\d{5}(-\d{4})?$`|米国 ZIP+4 | 5 桁、オプション -4 |
| `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`|メールアドレス |簡略化。 RFC 5322 ははるかに複雑です。
| `^https?:\/\/`| URL は http:// または https:// で始まります。 |
| `^\+?[1-9]\d{1,14}$`|電話番号 (E.164 形式) |国際規格 |
| `^(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)$`| IPv4 アドレス | |
| `^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$`| IPv6 アドレス |簡略化 |
| `^\d{3}-\d{2}-\d{4}$`|米国 SSN 形式 | XXX-XX-XXXX |
| `^[A-Z]{1,2}\d{1,4}\s?\d[A-Z]{2}$`|英国の郵便番号 |簡略化 |
### 抽出
|パターン |抜粋 |
|----------|----------|
| `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b`|テキストからのメールアドレス |
| `https?:\/\/[^\s]+`|テキストからの URL |
| `\b\d{1,3}(\.\d{1,3}){3}\b`|テキストからの IPv4 アドレス |
| `\d{4}-\d{2}-\d{2}`| ISO 日付 (YYYY-MM-DD) |
| `#[0-9a-fA-F]{6}\b`| 16進数のカラーコード |
| `\$\d+(?:\.\d{2})?`|ドル金額 |
### テキスト処理
|パターン |目的 |
|----------|----------|
| `\s+`| 1 つ以上の空白文字と一致します (スペースを折りたたむ) |
| `\r?\n`|改行に一致します (\n と \r\n の両方を処理します) |
| `^.*$`|行全体に一致する |
| `<[^>]+>`| HTML/XML タグを照合します (簡略化されています。正規表現を使用して HTML を解析しません)。
| `["']([^"']*)["']`|引用符で囲まれた文字列と一致する |
---

## フラグ/修飾子
|旗 |意味 |効果 |
|------|--------|----------|
| `i`|大文字と小文字を区別しない | `cat`は、「Cat」、「CAT」、「cAt」に一致します。
| `g`|グローバル |最初の一致だけでなく、すべての一致を検索 |
| `m`|複数行 | `^`および`$`は、文字列だけでなく行の境界とも一致します。
| `s`|ドートール | `.`は改行文字と一致します。
| `x`|拡張 |空白を無視し、パターン内でコメントを許可します |
---

## 言語固有の使用法
### パイソン
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

### grep / sed / awk (コマンドライン)
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

## よくある間違い
|間違い |問題 |修正 |
|----------|----------|-----|
| `.*`は貪欲です |一致しすぎます |遅延マッチングには`.*?`を使用します。
|`.`| エスケープするのを忘れています `file.txt`は`fileXtxt`にも一致します。`file\.txt`を使用する |
|検証パターンを固定していない | `^\d{3}$`が長い文字列に埋め込まれています |`^`および`$`を使用する |
|`[]`内の文字クラス | `[\d+]`は`\`、`d`、`+`に一致します — 数字ではありません |`[]`の外側で`\d`を使用するか、`[0-9]`|
|正規表現を使用した HTML の解析 | HTML は通常の言語ではありません |実際の解析には HTML パーサーを使用します。単純な抽出には正規表現 OK |
|壊滅的な後戻り |`(a+)+`のようなネストされた量指定子はハングする可能性があります。パターンを単純化します。原子団を使用する |
|エッジケースをテストしていない |パターンは正常なパスでは機能しますが、エッジでは失敗します。空の文字列、非常に長い入力、特殊文字を使用したテスト |
---

## テストツール
|ツール |タイプ | URL |
|------|------|-----|
| **正規表現101** |ウェブ | regex101.com — 説明付きリアルタイムマッチング |
| **正規Exr** |ウェブ | regexr.com — チートシートを使用した対話型テスト |
| **正規表現クロスワード** |ゲーム | regexcrossword.com — パズルを解いて学ぶ |
---

＃＃ まとめ
Regex は、テキスト内のパターン マッチングのためのツールです。シンプルに始めましょう。実際のパターンのほとんどは、文字クラス、数量指定子、アンカー、およびグループの単なる組み合わせです。パターンをコードに組み込む前に、テスト ツールを使用してパターンを検証します。覚えておいてください: 正規表現が複雑になりすぎて読めなくなった場合は、おそらく代わりに適切なパーサーを使用する必要があります。