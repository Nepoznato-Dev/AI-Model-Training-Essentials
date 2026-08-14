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
# Bảng cheat biểu thức chính quy
Biểu thức chính quy (regex) là các mẫu để khớp văn bản. Chúng được sử dụng ở mọi nơi — tìm kiếm và thay thế, xác thực đầu vào, phân tích cú pháp nhật ký, trích xuất dữ liệu, v.v. Đây là tài liệu tham khảo thực tế chứ không phải sách giáo khoa.
---

## Cú pháp cốt lõi
### Ký tự chữ
Hầu hết các ký tự khớp với nhau:`a`khớp với "a",`cat`khớp với "mèo".
### Ký tự đặc biệt (Siêu ký tự)
Chúng có ý nghĩa đặc biệt và phải được thoát bằng`\`để khớp với nghĩa đen:
| Nhân vật | Ý nghĩa |
|----------||----------|
| `.`| Bất kỳ ký tự nào ngoại trừ dòng mới |
| `^`| Bắt đầu chuỗi (hoặc dòng ở chế độ nhiều dòng) |
| `$`| Kết thúc chuỗi (hoặc dòng ở chế độ nhiều dòng) |
| `*`| 0 hoặc nhiều hơn trước |
| `+`| 1 hoặc nhiều hơn trước |
| `?`| 0 hoặc 1 trong số các giá trị trước (làm cho bộ định lượng trở nên lười biếng với`*?`,`+?`) |
| `\|`| Luân phiên (HOẶC) |
| `()`| Nhóm và chụp |
| `[]`| Lớp nhân vật |
| `{}`| Phạm vi định lượng |
| `\`| Nhân vật thoát hiểm |
---

## Lớp nhân vật
| Mẫu | Trận đấu |
|----------|----------|
| `[abc]`| a, b hoặc c |
| `[a-z]`| Bất kỳ chữ cái viết thường nào |
| `[A-Z]`| Bất kỳ chữ hoa nào |
| `[0-9]`| Bất kỳ chữ số nào |
| `[a-zA-Z]`| Thư bất kỳ |
| `[^abc]`| Bất kỳ thứ gì ngoại trừ a, b hoặc c (lớp phủ định) |
| `[a-z0-9_]`| Chữ thường, chữ số, dấu gạch dưới |
### Lớp viết tắt
| Mẫu | Tương đương | Trận đấu |
|----------|-------------|----------|
| `\d`| `[0-9]`| Chữ số |
| `\D`| `[^0-9]`| Không có chữ số |
| `\w`| `[a-zA-Z0-9_]`| Ký tự từ |
| `\W`| `[^a-zA-Z0-9_]`| Ký tự không phải từ |
| `\s`| `[ \t\n\r\f]`| Khoảng trắng (dấu cách, tab, dòng mới, v.v.) |
| `\S`| `[^\s]`| Không có khoảng trắng |
---

## Bộ định lượng
| Định lượng | Ý nghĩa | Ví dụ | Trận đấu |
|----------||----------|----------|--------|
| `*`| 0 trở lên | `ab*c`| ac, abc, abbc, abbbc |
| `+`| 1 hoặc nhiều hơn | `ab+c`| abc, abbc, abbbc |
| `?`| 0 hoặc 1 | `ab?c`| ac, abc |
| `{n}`| Chính xác n | `a{3}`| aaa |
| `{n,}`| n trở lên | `a{2,}`| aaa, aaa, aaa... |
| `{n,m}`| Giữa n và m | `a{2,4}`| aaa, aaa, aaa |
### Tham lam vs Lười biếng
Theo mặc định, các bộ định lượng là **tham lam** (khớp càng nhiều càng tốt). Thêm`?`để khiến họ **lười biếng** (match càng ít càng tốt).
| Mẫu | Chuỗi | Trận Đấu Tham Lam | Trận đấu lười biếng |
|----------|--------|-------------|----------||
| `<.*>`| `<b>hi</b>`| `<b>hi</b>`(toàn bộ chuỗi) |  riêng`<b>`và`</b>`|
| `<.+?>`| `<b>hi</b>`| — | `<b>`,`</b>`|
---

## Neo
| Neo | Ý nghĩa |
|--------|----------|
| `^`| Bắt đầu chuỗi |
| `$`| Kết thúc chuỗi |
| `\b`| Ranh giới từ |
| `\B`| Ranh giới phi từ |
| `(?=...)`| Cái nhìn tích cực |
| `(?!...)`| Cái nhìn tiêu cực |
| `(?<=...)`| Cái nhìn tích cực phía sau |
| `(?<!...)`| Cái nhìn tiêu cực phía sau |
**Ví dụ về ranh giới từ**:`\bcat\b`khớp với "cat" trong "the cat sat" nhưng không khớp với "category".
---

## Nhóm và chụp
| Cú pháp | Mô tả | Ví dụ |
|--------|-------------|----------|
| `(abc)`| Nhóm bắt giữ | Trích xuất "abc" từ một trận đấu |
| `(?:abc)`| Nhóm không bắt giữ | Nhóm không chụp |
| `\1`| Ngược lại nhóm 1 | `(abc)\1`khớp với "abcabc" |
| `(?<name>abc)`| Nhóm bắt giữ được đặt tên | `(?<year>\d{4})`|
| `a(?=b)`| Cái nhìn tích cực | Chỉ khớp "a" nếu theo sau là "b" |
| `a(?!b)`| Cái nhìn tiêu cực | Chỉ khớp "a" nếu KHÔNG được theo sau bởi "b" |
---

## Các mẫu phổ biến
### Xác thực
| Mẫu | Trận đấu | Ghi chú |
|----------|----------|-------|
| `^\d{5}$`| Mã ZIP của Hoa Kỳ | Chính xác 5 chữ số |
| `^\d{5}(-\d{4})?$`| ZIP+4 của Hoa Kỳ | 5 chữ số, tùy chọn -4 |
| `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`| Địa chỉ email | Đơn giản hóa; RFC 5322 phức tạp hơn nhiều |
| `^https?:\/\/`| URL bắt đầu bằng http:// hoặc https:// | |
| `^\+?[1-9]\d{1,14}$`| Số điện thoại (định dạng E.164) | Tiêu chuẩn quốc tế |
| `^(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)\.(25[0-5]\|2[0-4]\d\|[01]?\d\d?)$`| Địa chỉ IPv4 | |
| `^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$`| Địa chỉ IPv6 | Đơn giản hóa |
| `^\d{3}-\d{2}-\d{4}$`| Định dạng SSN của Hoa Kỳ | XXX-XX-XXXX |
| `^[A-Z]{1,2}\d{1,4}\s?\d[A-Z]{2}$`| Mã bưu điện Vương quốc Anh | Đơn giản hóa |
### Khai thác
| Mẫu | Chiết xuất |
|----------|----------|
| `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b`| Địa chỉ email từ văn bản |
| `https?:\/\/[^\s]+`| URL từ văn bản |
| `\b\d{1,3}(\.\d{1,3}){3}\b`| Địa chỉ IPv4 từ văn bản |
| `\d{4}-\d{2}-\d{2}`| Ngày ISO (YYYY-MM-DD) |
| `#[0-9a-fA-F]{6}\b`| Mã màu hex |
| `\$\d+(?:\.\d{2})?`| Số tiền đô la |
### Xử lý văn bản
| Mẫu | Mục đích |
|----------|----------|
| `\s+`| Khớp một hoặc nhiều ký tự khoảng trắng (thu gọn khoảng trắng) |
| `\r?\n`| Ngắt dòng khớp (xử lý cả \n và \r\n) |
| `^.*$`| Khớp toàn bộ dòng |
| `<[^>]+>`| Khớp các thẻ HTML/XML (được đơn giản hóa; không phân tích cú pháp HTML bằng biểu thức chính quy) |
| `["']([^"']*)["']`| Khớp các chuỗi trích dẫn |
---

## Cờ / Công cụ sửa đổi
| Cờ | Ý nghĩa | Hiệu ứng |
|------|----------|--------|
| `i`| Không phân biệt chữ hoa chữ thường | `cat`khớp với "Cat", "CAT", "cAt" |
| `g`| Toàn cầu | Tìm tất cả các kết quả phù hợp, không chỉ kết quả đầu tiên |
| `m`| Đa dòng | `^`và`$`khớp với ranh giới dòng chứ không chỉ chuỗi |
| `s`| Dotall | `.`khớp với các ký tự dòng mới |
| `x`| Mở rộng | Bỏ qua khoảng trắng và cho phép nhận xét trong mẫu |
---

## Cách sử dụng ngôn ngữ cụ thể
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

###Javascript
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

### grep / sed / awk (Dòng lệnh)
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

## Những lỗi thường gặp
| Sai lầm | Vấn đề | Sửa chữa |
|----------|----------|------|
| `.*`tham lam | Phù hợp quá nhiều | Sử dụng`.*?`để khớp lười |
| Quên thoát`.`| `file.txt`cũng khớp với`fileXtxt`| Sử dụng`file\.txt`|
| Không neo các mẫu xác thực | `^\d{3}$`được nhúng trong chuỗi dài hơn | Sử dụng`^`và`$`|
| Lớp nhân vật bên trong`[]`| `[\d+]`khớp với`\`,`d`,`+`— không phải chữ số | Sử dụng`\d`bên ngoài`[]`hoặc`[0-9]`|
| Phân tích cú pháp HTML bằng biểu thức chính quy | HTML không phải là ngôn ngữ thông thường | Sử dụng trình phân tích cú pháp HTML để phân tích cú pháp thực sự; Regex OK để trích xuất đơn giản |
| Sự lùi bước thảm khốc | Các bộ định lượng lồng nhau như`(a+)+`có thể treo | Đơn giản hóa mẫu; sử dụng nhóm nguyên tử |
| Không thử nghiệm các trường hợp cạnh | Mô hình hoạt động trên con đường hạnh phúc, thất bại ở rìa | Kiểm tra với chuỗi trống, đầu vào rất dài, ký tự đặc biệt |
---

## Công cụ kiểm tra
| Công cụ | Loại | URL |
|------|------|------|
| **Regex101** | Web | Regex101.com — khớp thời gian thực với lời giải thích |
| **RegExr** | Web | regrec.com — thử nghiệm tương tác với cheatsheet |
| **regex-ô chữ** | Trò chơi | regreccrossword.com — học bằng cách giải câu đố |
---

## Bản tóm tắt
Regex là công cụ khớp mẫu trong văn bản. Bắt đầu đơn giản - hầu hết các mẫu trong thế giới thực chỉ là sự kết hợp của các lớp ký tự, bộ định lượng, điểm neo và nhóm. Sử dụng công cụ kiểm tra để xác minh mẫu của bạn trước khi đưa chúng vào mã. Và hãy nhớ: nếu biểu thức chính quy của bạn ngày càng phức tạp đến mức bạn không thể đọc được thì có lẽ đã đến lúc sử dụng một trình phân tích cú pháp thích hợp để thay thế.