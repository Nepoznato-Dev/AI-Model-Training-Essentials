---
# Metadata
title: "Perl — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Perl with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [perl, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Perl — Những lỗi thường gặp và các mẫu phản đối
Tài liệu này liệt kê các lỗi, bẫy và phản mẫu phổ biến nhất trong Perl kèm theo các bản sửa lỗi.
---

## 1. Không sử dụng`strict`và `warnings`
```perl
# ❌ WRONG — no safety checks
$x = 5;  # creates global $x silently
print $y;  # typo, prints nothing

# ✅ CORRECT — always use strict and warnings
use strict;
use warnings;
my $x = 5;
```

---

## 2. Ngữ cảnh vô hướng và danh sách
```perl
# ❌ WRONG — context confusion
my @arr = (1, 2, 3);
my $count = @arr;  # 3 (scalar context — count)
my ($first) = @arr;  # 1 (list context — first element)
my $first = @arr;    # 3! (scalar context — count, not element)

# ✅ CORRECT — be explicit about context
my $count = scalar @arr;
my ($first) = @arr;
```

---

## 3. Biến toàn cục
```perl
# ❌ WRONG — package variables
$name = "Alice";
sub greet { print "Hello, $name\n"; }

# ✅ CORRECT — lexical variables
my $name = "Alice";
sub greet { print "Hello, $name\n"; }
```

---

## 4. Không sử dụng tham chiếu cho dữ liệu phức tạp
```perl
# ❌ WRONG — array of arrays (flattened)
my @matrix = ((1,2), (3,4));  # just (1,2,3,4)

# ✅ CORRECT — array of array references
my @matrix = ([1,2], [3,4]);
print $matrix[0][1];  # 2
```

---

## 5. Regex không có dấu phân cách rõ ràng
```perl
# ❌ WRONG — hard to read regex
$s =~ /\/usr\/local\/bin/;

# ✅ CORRECT — use different delimiters
$s =~ m{/usr/local/bin};
```

---

## 6. Không sử dụng các tính năng Perl hiện đại
```perl
# ❌ WRONG — old Perl style
my $name = shift @_;
my $age = shift @_;

# ✅ CORRECT — modern Perl (5.20+)
sub greet($name, $age) {
    say "Hello, $name! Age: $age";
}

# ✅ CORRECT — say instead of print
say "Hello, world!";

# ✅ CORRECT — // for defined-or
my $value = $input // 'default';
```

---

## Bản tóm tắt
Tính linh hoạt của Perl rất nguy hiểm: luôn`use strict; use warnings;`, hiểu ngữ cảnh (vô hướng so với danh sách), sử dụng các biến từ vựng (`my`), sử dụng tham chiếu cho dữ liệu lồng nhau và nắm lấy các tính năng Perl hiện đại (chữ ký,`say`,`//`). Perl thưởng cho những người sử dụng công cụ biểu thức chính quy phong phú và hệ sinh thái CPAN của nó một cách khôn ngoan.