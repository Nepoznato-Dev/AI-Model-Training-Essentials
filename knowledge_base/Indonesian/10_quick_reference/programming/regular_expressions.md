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

# Lembar Cheat Ekspresi Reguler
Ekspresi reguler (regex) adalah pola untuk mencocokkan teks. Mereka digunakan di mana saja — cari dan ganti, validasi input, penguraian log, ekstraksi data, dan banyak lagi. Ini adalah referensi praktis, bukan buku teks.
---

## Sintaks Inti
### Karakter Harafiah
Sebagian besar karakter cocok dengan dirinya sendiri:`a`cocok dengan "a",`cat`cocok dengan "cat".
### Karakter Khusus (Metakarakter)
Ini memiliki arti khusus dan harus di-escape dengan`\`agar cocok secara harfiah:
| Karakter | Arti |
|-----------|---------|
| `.`| Karakter apa pun kecuali baris baru |
| `^`| Awal string (atau garis dalam mode multiline) |
| `$`| Akhir string (atau garis dalam mode multiline) |
| `*`| 0 atau lebih dari | sebelumnya
| `+`| 1 atau lebih dari | sebelumnya
| `?`| 0 atau 1 dari sebelumnya (membuat bilangan menjadi malas dengan`*?`,`+?`) |
| `\|`| Pergantian (ATAU) |
| `()`| Mengelompokkan dan menangkap |
| `[]`| Kelas karakter |
| `{}`| Rentang pembilang |
| `\`| Karakter melarikan diri |
---

## Kelas Karakter
| Pola | Cocok |
|---------|---------|
| `[abc]`| a, b, atau c |
| `[a-z]`| Huruf kecil apa saja |
| `[A-Z]`| Huruf besar apa saja |
| `[0-9]`| Angka apa saja |
| `[a-zA-Z]`| Surat apa saja |
| `[^abc]`| Apa pun kecuali a, b, atau c (kelas yang dinegasikan) |
| `[a-z0-9_]`| Huruf kecil, angka, garis bawah |
### Kelas Singkatan
| Pola | Setara | Cocok |
|---------|-----------|---------|
| `\d`| `[0-9]`| Angka |
| `\D`| `[^0-9]`| Non-digit |
| `\w`| `[a-zA-Z0-9_]`| Karakter kata |
| `\W`| `[^a-zA-Z0-9_]`| Karakter non-kata |
| `\s`| `[ \t\n\r\f]`| Spasi putih (spasi, tab, baris baru, dll.) |
| `\S`| `[^\s]`| Bukan spasi |
---

## Pengukur
| Pengukur | Arti | Contoh | Cocok |
|-----------|---------|---------|---------|
| `*`| 0 atau lebih | `ab*c`| ac, abc, abbc, abbbc |
| `+`| 1 atau lebih | `ab+c`| abc, abbc, abbbc |
| `?`| 0 atau 1 | `ab?c`| ac, abc |
| `{n}`| Tepatnya n | `a{3}`| aaa |
| `{n,}`| n atau lebih | `a{2,}`| aa, aaa, aaa... |
| `{n,m}`| Antara n dan m | `a{2,4}`| aa, aaa, aaa |
### Serakah vs Malas
Secara default, quantifier bersifat **serakah** (cocokkan sebanyak mungkin). Tambahkan`?`untuk membuat mereka **malas** (cocokkan sesedikit mungkin).
| Pola | Tali | Pertandingan Serakah | Pertandingan Malas |
|---------|--------|-------------|------------|
| `<.*>`| `<b>hi</b>`| `<b>hi</b>`(keseluruhan string) | `<b>`dan`</b>`secara terpisah |
| `<.+?>`| `<b>hi</b>`| — | `<b>`,`</b>`|
---

## Jangkar
| Jangkar | Arti |
|--------|---------|
| `^`| Mulai dari string |
| `$`| Akhir string |
| `\b`| Batas kata |
| `\B`| Batas non-kata |
| `(?=...)`| Pandangan positif ke depan |
| `(?!...)`| Pandangan ke depan yang negatif |
| `(?<=...)`| Pandangan positif ke belakang |
| `(?<!...)`| Pandangan negatif ke belakang |
**Contoh batasan kata**:`\bcat\b`cocok dengan "cat" di "the cat sat" namun tidak di "category".
---

## Grup dan Pengambilan
| Sintaks | Deskripsi | Contoh |
|--------|-------------|---------|
| `(abc)`| Menangkap grup | Ekstrak "abc" dari kecocokan |
| `(?:abc)`| Grup yang tidak menangkap | Kelompokkan tanpa menangkap |
| `\1`| Referensi balik ke grup 1 | `(abc)\1`cocok dengan "abcabc" |
| `(?<name>abc)`| Dinamakan grup penangkap | `(?<year>\d{4})`|
| `a(?=b)`| Pandangan positif ke depan | Cocokkan "a" hanya jika diikuti dengan "b" |
| `a(?!b)`| Pandangan ke depan yang negatif | Cocokkan "a" hanya jika TIDAK diikuti dengan "b" |
---

## Pola Umum
### Validasi
| Pola | Cocok | Catatan |
|---------|---------|-------|
| `^\d{5}$`| Kode Pos AS | Tepat 5 digit |
| `^\d{5}(-\d{4})?$`| ZIP+4 AS | 5 digit, opsional -4 |
| `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`| Alamat email | Sederhana; RFC 5322 jauh lebih kompleks |
| `^https?:\/\/`| URL dimulai dengan http:// atau https:// | |
| `^\+?[1-9]\d{1,14}$`| Nomor telepon (format E.164) | Standar Internasional |
| `^(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)$`| Alamat IPv4 | |
| `^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$`| Alamat IPv6 | Sederhana |
| `^\d{3}-\d{2}-\d{4}$`| Format SSN AS | XXX-XX-XXXX |
| `^[A-Z]{1,2}\d{1,4}\s?\d[A-Z]{2}$`| Kode Pos Inggris | Sederhana |
### Ekstraksi
| Pola | Ekstrak |
|---------|----------|
| `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b`| Alamat email dari teks |
| `https?:\/\/[^\s]+`| URL dari teks |
| `\b\d{1,3}(\.\d{1,3}){3}\b`| Alamat IPv4 dari teks |
| `\d{4}-\d{2}-\d{2}`| Tanggal ISO (YYYY-MM-DD) |
| `#[0-9a-fA-F]{6}\b`| Kode warna hex |
| `\$\d+(?:\.\d{2})?`| Jumlah dolar |
### Pemrosesan Teks
| Pola | Tujuan |
|---------|---------|
| `\s+`| Cocokkan satu atau lebih karakter spasi putih (ciutkan spasi) |
| `\r?\n`| Jeda baris yang cocok (menangani \n dan \r\n) |
| `^.*$`| Cocokkan seluruh baris |
| `<[^>]+>`| Cocokkan tag HTML/XML (disederhanakan; jangan parsing HTML dengan regex) |
| `["']([^"']*)["']`| Cocokkan string yang dikutip |
---

## Bendera / Pengubah
| Bendera | Arti | Efek |
|------|---------|--------|
| `i`| Tidak peka huruf besar-kecil | `cat`cocok dengan "Kucing", "CAT", "cAt" |
| `g`| Global | Temukan semua kecocokan, bukan hanya yang pertama |
| `m`| Multibaris | `^`dan`$`cocok dengan batas garis, bukan hanya string |
| `s`| Total | `.`cocok dengan karakter baris baru |
| `x`| Diperpanjang | Abaikan spasi dan izinkan komentar di pola |
---

## Penggunaan Khusus Bahasa
### Piton
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

###JavaScript
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

### grep / sed / awk (Baris Perintah)
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

## Kesalahan Umum
| Kesalahan | Masalah | Perbaiki |
|---------|---------|-----|
| `.*`serakah | Terlalu cocok | Gunakan`.*?`untuk pencocokan malas |
| Lupa melarikan diri`.`| `file.txt`juga cocok dengan`fileXtxt`| Gunakan`file\.txt`|
| Tidak menahan pola validasi | `^\d{3}$`tertanam dalam string yang lebih panjang | Gunakan`^`dan`$`|
| Kelas karakter di dalam`[]`| `[\d+]`cocok dengan`\`,`d`,`+`— bukan angka | Gunakan`\d`di luar`[]`, atau`[0-9]`|
| Mengurai HTML dengan regex | HTML bukan bahasa biasa | Gunakan parser HTML untuk parsing sebenarnya; regex OK untuk ekstraksi sederhana |
| Kemunduran yang dahsyat | Pembilang bersarang seperti`(a+)+`dapat digantung | Sederhanakan polanya; gunakan gugus atom |
| Tidak menguji kasus tepi | Pola berfungsi di jalur bahagia, gagal di tepi | Uji dengan string kosong, masukan sangat panjang, karakter khusus |
---

## Alat Pengujian
| Alat | Ketik | URL |
|------|------|-----|
| **Reguler101** | jaringan | regex101.com — pencocokan waktu nyata dengan penjelasan |
| **RegExr** | jaringan | regexr.com — pengujian interaktif dengan cheatsheet |
| **regex-teka-teki silang** | Permainan | regexcrossword.com — belajar dengan memecahkan teka-teki |
---

## Ringkasan
Regex adalah alat untuk pencocokan pola dalam teks. Mulailah dengan sederhana - sebagian besar pola dunia nyata hanyalah kombinasi kelas karakter, bilangan, jangkar, dan grup. Gunakan alat pengujian untuk memverifikasi pola Anda sebelum memasukkannya ke dalam kode. Dan ingat: jika regex Anda menjadi sangat rumit sehingga Anda tidak dapat membacanya, mungkin inilah saatnya untuk menggunakan parser yang tepat.