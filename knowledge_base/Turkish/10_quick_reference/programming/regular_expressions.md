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
# Normal İfadeler Hile Sayfası
Normal ifadeler (regex), metni eşleştirmeye yönelik kalıplardır. Her yerde kullanılırlar: arama ve değiştirme, giriş doğrulama, günlük ayrıştırma, veri çıkarma ve daha fazlası. Bu bir ders kitabı değil, pratik bir referanstır.
---

## Temel Söz Dizimi
### Değişmez Karakterler
Çoğu karakter birbiriyle eşleşir:`a`"a" ile eşleşir,`cat`"kedi" ile eşleşir.
### Özel Karakterler (Metakarakterler)
Bunların özel bir anlamı vardır ve kelimenin tam anlamıyla eşleşmesi için`\`ile kaçınılmalıdır:
| Karakter | Anlamı |
|-----------|------------|
| `.`| Satırsonu dışında herhangi bir karakter |
| `^`| Dizenin başlangıcı (veya çok satırlı modda satır) |
| `$`| Dizenin sonu (veya çok satırlı modda satır) |
| `*`| 0 veya öncekilerden daha fazlası |
| `+`| Öncekilerden 1 veya daha fazlası |
| `?`| Öncekilerden 0 veya 1'i (`*?` ,`+?`ile niceleyicileri tembelleştirir) |
| `\|`| Değişim (VEYA) |
| `()`| Gruplama ve yakalama |
| `[]`| Karakter sınıfı |
| `{}`| Niceleyici aralığı |
| `\`| Kaçış karakteri |
---

## Karakter Sınıfları
| Desen | Maçlar |
|-----------|-----------|
| `[abc]`| a, b veya c |
| `[a-z]`| Herhangi bir küçük harf |
| `[A-Z]`| Herhangi bir büyük harf |
| `[0-9]`| Herhangi bir rakam |
| `[a-zA-Z]`| Herhangi bir harf |
| `[^abc]`| a, b veya c (olumsuz sınıf) dışında herhangi bir şey |
| `[a-z0-9_]`| Küçük harfler, rakamlar, alt çizgi |
### Steno Dersleri
| Desen | Eşdeğer | Maçlar |
|-----------|-----------|-----------|
| `\d`| `[0-9]`| Rakam |
| `\D`| `[^0-9]`| Rakamsız |
| `\w`| `[a-zA-Z0-9_]`| Kelime karakteri |
| `\W`| `[^a-zA-Z0-9_]`| Kelime olmayan karakter |
| `\s`| `[ \t\n\r\f]`| Boşluk (boşluk, sekme, yeni satır vb.) |
| `\S`| `[^\s]`| Boşluksuz |
---

## Niceleyiciler
| Niceleyici | Anlamı | Örnek | Maçlar |
|-----------|------------|------------|---------|
| `*`| 0 veya daha fazla | `ab*c`| ac, abc, abbc, abbbc |
| `+`| 1 veya daha fazla | `ab+c`| abc, abbc, abbbc |
| `?`| 0 veya 1 | `ab?c`| ac, abc |
| `{n}`| Kesinlikle n | `a{3}`| aa |
| `{n,}`| n veya daha fazla | `a{2,}`| aa, aa, aaaa... |
| `{n,m}`| n ve m arasında | `a{2,4}`| aa, aa, aaa |
### Açgözlü vs Tembel
Varsayılan olarak nicelik belirteçleri **açgözlüdür** (mümkün olduğunca eşleşir). Onları **tembel** yapmak için`?`ekleyin (mümkün olduğunca az eşleştirin).
| Desen | Dize | Açgözlü Maç | Tembel Maç |
|------------|-----------|-------------|------------|
| `<.*>`| `<b>hi</b>`| `<b>hi</b>`(dizgenin tamamı) | `<b>`ve`</b>`ayrı ayrı |
| `<.+?>`| `<b>hi</b>`| — | `<b>`,`</b>`|
---

## Çapalar
| Çapa | Anlamı |
|----------|------------|
| `^`| Dizenin başlangıcı |
| `$`| Dizenin sonu |
| `\b`| Kelime sınırı |
| `\B`| Kelimesiz sınır |
| `(?=...)`| Olumlu bakış |
| `(?!...)`| Negatif bakış |
| `(?<=...)`| Olumlu geriye bakış |
| `(?<!...)`| Negatif geriye bakış |
**Kelime sınırı örneği**:`\bcat\b`"kedi" ile "kedi oturdu" içinde eşleşir ancak "kategori" ile eşleşmez.
---

## Gruplar ve Yakalama
| Sözdizimi | Açıklama | Örnek |
|----------|----------------|------------|
| `(abc)`| Yakalama grubu | Bir maçtan "abc"yi çıkarın |
| `(?:abc)`| Yakalamayan grup | Yakalamadan grup |
| `\1`| Grup 1'e geri referans | `(abc)\1`"abcabc" ile eşleşiyor |
| `(?<name>abc)`| Adlandırılmış yakalama grubu | `(?<year>\d{4})`|
| `a(?=b)`| Olumlu bakış | "a"yı yalnızca arkasından "b" geliyorsa eşleştirin |
| `a(?!b)`| Negatif bakış | "a"yı yalnızca ardından "b" gelmiyorsa eşleştirin |
---

## Ortak Desenler
### Doğrulama
| Desen | Maçlar | Notlar |
|-----------|------------|-------|
| `^\d{5}$`| ABD Posta kodu | Tam 5 hane |
| `^\d{5}(-\d{4})?$`| ABD Posta Kodu+4 | 5 hane, isteğe bağlı -4 |
| `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`| E-posta adresi | Basitleştirilmiş; RFC 5322 çok daha karmaşıktır |
| `^https?:\/\/`| URL http:// veya https:// ile başlar | |
| `^\+?[1-9]\d{1,14}$`| Telefon numarası (E.164 biçimi) | Uluslararası standart |
| `^(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)$`| IPv4 adresi | |
| `^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$`| IPv6 adresi | Basitleştirilmiş |
| `^\d{3}-\d{2}-\d{4}$`| ABD SSN formatı | XXX-XX-XXXX |
| `^[A-Z]{1,2}\d{1,4}\s?\d[A-Z]{2}$`| İngiltere posta kodu | Basitleştirilmiş |
### Ekstraksiyon
| Desen | Alıntılar |
|-----------|----------|
| `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b`| Metinden e-posta adresleri |
| `https?:\/\/[^\s]+`| Metinden URL'ler |
| `\b\d{1,3}(\.\d{1,3}){3}\b`| Metinden IPv4 adresleri |
| `\d{4}-\d{2}-\d{2}`| ISO tarihleri ​​(YYYY-AA-GG) |
| `#[0-9a-fA-F]{6}\b`| Hex renk kodları |
| `\$\d+(?:\.\d{2})?`| Dolar miktarları |
### Metin İşleme
| Desen | Amaç |
|-----------|-----------|
| `\s+`| Bir veya daha fazla boşluk karakteriyle eşleştirin (boşlukları daraltın) |
| `\r?\n`| Satır sonlarını eşleştir (hem \n hem de \r\n'yi yönetir) |
| `^.*$`| Bir satırın tamamını eşleştir |
| `<[^>]+>`| HTML/XML etiketlerini eşleştirin (basitleştirilmiş; HTML'yi normal ifadeyle ayrıştırmayın) |
| `["']([^"']*)["']`| Alıntılanan dizeleri eşleştir |
---

## Bayraklar / Değiştiriciler
| Bayrak | Anlamı | Efekt |
|------|------------|--------|
| `i`| Büyük/küçük harfe duyarlı |  `cat`, "Cat", "CAT", "cAt" ile eşleşir |
| `g`| Küresel | Yalnızca ilkini değil, tüm eşleşmeleri bulun |
| `m`| Çok satırlı | `^`ve`$`yalnızca dizeyle değil çizgi sınırlarıyla da eşleşir |
| `s`| Nokta | `.`yeni satır karakterleriyle eşleşir |
| `x`| Genişletilmiş | Boşlukları yok sayın ve kalıpta yorumlara izin verin |
---

## Dile Özel Kullanım
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

### grep / sed / awk (Komut Satırı)
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

## Yaygın Hatalar
| Hata | Sorun | Düzelt |
|-----------|-----------|-----|
| `.*`açgözlü | Çok fazla eşleşiyor | Tembel eşleştirme için`.*?`kullanın |
| Kaçmayı unutmak`.`|  `file.txt`,`fileXtxt`ile de eşleşiyor |`file\.txt`kullanın |
| Doğrulama modellerini sabitlememek | `^\d{3}$`daha uzun dizeye gömülü |`^`ve`$`kullanın |
|`[]`içindeki karakter sınıfı |  `[\d+]`,`\`,`d`,`+`ile eşleşir - rakamlarla değil | `\d`'yi`[]`dışında veya`[0-9]`|
| Regex ile HTML'yi ayrıştırma | HTML normal bir dil değildir | Gerçek ayrıştırma için bir HTML ayrıştırıcı kullanın; basit çıkarma için regex Tamam |
| Yıkıcı geri izleme |`(a+)+`gibi iç içe niceleyiciler askıda kalabilir | Deseni basitleştirin; atom gruplarını kullan |
| Uç vakaları test etmiyoruz | Desen mutlu yolda çalışır, kenarda başarısız olur | Boş dizelerle, çok uzun girişlerle, özel karakterlerle test edin |
---

## Test Araçları
| Araç | Tür | URL'si |
|------|----------|-----|
| **Regex101** | Web | regex101.com — açıklamayla gerçek zamanlı eşleştirme |
| **RegExr** | Web | regexr.com — hile sayfasıyla etkileşimli test |
| **regex-bulmaca** | Oyun | regexcrossword.com — bulmacaları çözerek öğrenin |
---

## Özet
Regex, metinde kalıp eşleştirmeye yönelik bir araçtır. Basit başlayın; gerçek dünyadaki kalıpların çoğu, karakter sınıflarının, niceleyicilerin, çapaların ve grupların yalnızca bir birleşimidir. Kalıplarınızı koda koymadan önce doğrulamak için bir test aracı kullanın. Ve unutmayın: Regex'iniz okuyamayacak kadar karmaşık hale geliyorsa, muhtemelen bunun yerine uygun bir ayrıştırıcı kullanmanın zamanı gelmiştir.