---
# Metadata
title: "SQL — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in SQL with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [sql, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# SQL — Các lỗi thường gặp & Mẫu phản đối
Tài liệu này liệt kê các lỗi, bẫy và mẫu chống phổ biến nhất trong SQL kèm theo các bản sửa lỗi.
---

## 1. CHỌN * trong Sản xuất
```sql
-- ❌ WRONG — returns all columns, breaks on schema change
SELECT * FROM users WHERE active = true;

-- ✅ CORRECT — specify columns
SELECT id, name, email FROM users WHERE active = true;
```

---

## 2. So sánh NULL
```sql
-- ❌ WRONG — NULL = NULL is NULL, not TRUE
SELECT * FROM users WHERE email = NULL;  -- returns nothing

-- ✅ CORRECT — use IS NULL
SELECT * FROM users WHERE email IS NULL;
SELECT * FROM users WHERE email IS NOT NULL;
```

---

## 3. Chèn SQL
```sql
-- ❌ WRONG — string concatenation
query = "SELECT * FROM users WHERE name = '" + userInput + "'";

-- ✅ CORRECT — parameterized queries
-- SELECT * FROM users WHERE name = ?;
-- Then bind userInput to the parameter
```

---

## 4. Không sử dụng chỉ mục (Truy vấn SARGable)
```sql
-- ❌ WRONG — function on column prevents index use
SELECT * FROM users WHERE YEAR(created_at) = 2024;

-- ✅ CORRECT — range condition (SARGable)
SELECT * FROM users
WHERE created_at >= '2024-01-01'
  AND created_at < '2025-01-01';
```

---

## 5. Chuyển đổi kiểu ngầm định
```sql
-- ❌ WRONG — comparing string to number
SELECT * FROM users WHERE phone = 1234567890;
-- phone is VARCHAR, implicit conversion may skip index

-- ✅ CORRECT — match types
SELECT * FROM users WHERE phone = '1234567890';
```

---

## 6. Sản phẩm Descartes
```sql
-- ❌ WRONG — missing JOIN condition
SELECT * FROM users, orders;  -- every user × every order!

-- ✅ CORRECT — explicit JOIN with condition
SELECT u.name, o.total
FROM users u
JOIN orders o ON u.id = o.user_id;
```

---

## 7. GROUP BY Không có tất cả các cột không tổng hợp
```sql
-- ❌ WRONG — non-aggregated column not in GROUP BY
SELECT name, email, COUNT(*) FROM users GROUP BY name;
-- email is ambiguous!

-- ✅ CORRECT — all non-aggregated columns in GROUP BY
SELECT name, email, COUNT(*) FROM users GROUP BY name, email;
```

---

## Bản tóm tắt
Bản chất khai báo của SQL che giấu các bẫy hiệu suất: luôn chỉ định các cột (không phải`SELECT *`), sử dụng`IS NULL`để kiểm tra null, tham số hóa các truy vấn để ngăn chặn việc chèn, ghi các điều kiện SARGable để sử dụng chỉ mục, so khớp các loại so sánh, sử dụng THAM GIA rõ ràng và bao gồm tất cả các cột không tổng hợp trong GROUP BY. SQL tốt là suy nghĩ theo tập hợp chứ không phải theo hàng.