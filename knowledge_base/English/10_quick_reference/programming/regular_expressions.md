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

# Regular Expressions Cheat Sheet

Regular expressions (regex) are patterns for matching text. They're used everywhere — search and replace, input validation, log parsing, data extraction, and more. This is a practical reference, not a textbook.

---

## Core Syntax

### Literal Characters

Most characters match themselves: `a` matches "a", `cat` matches "cat".

### Special Characters (Metacharacters)

These have special meaning and must be escaped with `\` to match literally:

| Character | Meaning |
|-----------|---------|
| `.` | Any character except newline |
| `^` | Start of string (or line in multiline mode) |
| `$` | End of string (or line in multiline mode) |
| `*` | 0 or more of the preceding |
| `+` | 1 or more of the preceding |
| `?` | 0 or 1 of the preceding (makes quantifiers lazy with `*?`, `+?`) |
| `\|` | Alternation (OR) |
| `()` | Grouping and capturing |
| `[]` | Character class |
| `{}` | Quantifier range |
| `\` | Escape character |

---

## Character Classes

| Pattern | Matches |
|---------|---------|
| `[abc]` | a, b, or c |
| `[a-z]` | Any lowercase letter |
| `[A-Z]` | Any uppercase letter |
| `[0-9]` | Any digit |
| `[a-zA-Z]` | Any letter |
| `[^abc]` | Anything except a, b, or c (negated class) |
| `[a-z0-9_]` | Lowercase letters, digits, underscore |

### Shorthand Classes

| Pattern | Equivalent | Matches |
|---------|-----------|---------|
| `\d` | `[0-9]` | Digit |
| `\D` | `[^0-9]` | Non-digit |
| `\w` | `[a-zA-Z0-9_]` | Word character |
| `\W` | `[^a-zA-Z0-9_]` | Non-word character |
| `\s` | `[ \t\n\r\f]` | Whitespace (space, tab, newline, etc.) |
| `\S` | `[^\s]` | Non-whitespace |

---

## Quantifiers

| Quantifier | Meaning | Example | Matches |
|-----------|---------|---------|---------|
| `*` | 0 or more | `ab*c` | ac, abc, abbc, abbbc |
| `+` | 1 or more | `ab+c` | abc, abbc, abbbc |
| `?` | 0 or 1 | `ab?c` | ac, abc |
| `{n}` | Exactly n | `a{3}` | aaa |
| `{n,}` | n or more | `a{2,}` | aa, aaa, aaaa... |
| `{n,m}` | Between n and m | `a{2,4}` | aa, aaa, aaaa |

### Greedy vs Lazy

By default, quantifiers are **greedy** (match as much as possible). Add `?` to make them **lazy** (match as little as possible).

| Pattern | String | Greedy Match | Lazy Match |
|---------|--------|-------------|------------|
| `<.*>` | `<b>hi</b>` | `<b>hi</b>` (entire string) | `<b>` and `</b>` separately |
| `<.+?>` | `<b>hi</b>` | — | `<b>`, `</b>` |

---

## Anchors

| Anchor | Meaning |
|--------|---------|
| `^` | Start of string |
| `$` | End of string |
| `\b` | Word boundary |
| `\B` | Non-word boundary |
| `(?=...)` | Positive lookahead |
| `(?!...)` | Negative lookahead |
| `(?<=...)` | Positive lookbehind |
| `(?<!...)` | Negative lookbehind |

**Word boundary example**: `\bcat\b` matches "cat" in "the cat sat" but not in "category".

---

## Groups and Capturing

| Syntax | Description | Example |
|--------|-------------|---------|
| `(abc)` | Capturing group | Extract "abc" from a match |
| `(?:abc)` | Non-capturing group | Group without capturing |
| `\1` | Backreference to group 1 | `(abc)\1` matches "abcabc" |
| `(?<name>abc)` | Named capturing group | `(?<year>\d{4})` |
| `a(?=b)` | Positive lookahead | Match "a" only if followed by "b" |
| `a(?!b)` | Negative lookahead | Match "a" only if NOT followed by "b" |

---

## Common Patterns

### Validation

| Pattern | Matches | Notes |
|---------|---------|-------|
| `^\d{5}$` | US ZIP code | Exactly 5 digits |
| `^\d{5}(-\d{4})?$` | US ZIP+4 | 5 digits, optional -4 |
| `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$` | Email address | Simplified; RFC 5322 is far more complex |
| `^https?:\/\/` | URL starts with http:// or https:// | |
| `^\+?[1-9]\d{1,14}$` | Phone number (E.164 format) | International standard |
| `^(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)$` | IPv4 address | |
| `^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$` | IPv6 address | Simplified |
| `^\d{3}-\d{2}-\d{4}$` | US SSN format | XXX-XX-XXXX |
| `^[A-Z]{1,2}\d{1,4}\s?\d[A-Z]{2}$` | UK postcode | Simplified |

### Extraction

| Pattern | Extracts |
|---------|----------|
| `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b` | Email addresses from text |
| `https?:\/\/[^\s]+` | URLs from text |
| `\b\d{1,3}(\.\d{1,3}){3}\b` | IPv4 addresses from text |
| `\d{4}-\d{2}-\d{2}` | ISO dates (YYYY-MM-DD) |
| `#[0-9a-fA-F]{6}\b` | Hex colour codes |
| `\$\d+(?:\.\d{2})?` | Dollar amounts |

### Text Processing

| Pattern | Purpose |
|---------|---------|
| `\s+` | Match one or more whitespace characters (collapse spaces) |
| `\r?\n` | Match line breaks (handles both \n and \r\n) |
| `^.*$` | Match an entire line |
| `<[^>]+>` | Match HTML/XML tags (simplified; don't parse HTML with regex) |
| `["']([^"']*)["']` | Match quoted strings |

---

## Flags / Modifiers

| Flag | Meaning | Effect |
|------|---------|--------|
| `i` | Case-insensitive | `cat` matches "Cat", "CAT", "cAt" |
| `g` | Global | Find all matches, not just the first |
| `m` | Multiline | `^` and `$` match line boundaries, not just string |
| `s` | Dotall | `.` matches newline characters |
| `x` | Extended | Ignore whitespace and allow comments in the pattern |

---

## Language-Specific Usage

### Python

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

### grep / sed / awk (Command Line)

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

## Common Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| `.*` is greedy | Matches too much | Use `.*?` for lazy matching |
| Forgetting to escape `.` | `file.txt` matches `fileXtxt` too | Use `file\.txt` |
| Not anchoring validation patterns | `^\d{3}$` embedded in longer string | Use `^` and `$` |
| Character class inside `[]` | `[\d+]` matches `\`, `d`, `+` — not digits | Use `\d` outside `[]`, or `[0-9]` |
| Parsing HTML with regex | HTML is not a regular language | Use an HTML parser for real parsing; regex OK for simple extraction |
| Catastrophic backtracking | Nested quantifiers like `(a+)+` can hang | Simplify the pattern; use atomic groups |
| Not testing edge cases | Pattern works on happy path, fails on edge | Test with empty strings, very long input, special characters |

---

## Testing Tools

| Tool | Type | URL |
|------|------|-----|
| **Regex101** | Web | regex101.com — real-time matching with explanation |
| **RegExr** | Web | regexr.com — interactive testing with cheatsheet |
| **regex-crossword** | Game | regexcrossword.com — learn by solving puzzles |

---

## Summary

Regex is a tool for pattern matching in text. Start simple — most real-world patterns are just a combination of character classes, quantifiers, anchors, and groups. Use a testing tool to verify your patterns before putting them in code. And remember: if your regex is getting so complex that you can't read it, it's probably time to use a proper parser instead.
