---
# Metadata
title: "Julia — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Julia with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [julia, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Julia — ข้อผิดพลาดทั่วไปและการต่อต้านรูปแบบ
เอกสารนี้รวบรวมข้อผิดพลาด กับดัก และรูปแบบการต่อต้านที่พบบ่อยที่สุดใน Julia พร้อมการแก้ไข
---

## 1. พิมพ์ความไม่เสถียรในฟังก์ชัน
```julia
# ❌ WRONG — return type changes
function compute(x)
    if x > 0
        return x        # Int
    else
        return "negative"  # String — type unstable!
    end
end

# ✅ CORRECT — consistent return types
function compute(x)
    if x > 0
        return x
    else
        return -1  # always Int
    end
end

# ✅ CORRECT — use Union if needed
function parse_value(s::String)::Union{Int, Nothing}
    tryparse(Int, s)
end
```

---

## 2. ตัวแปรทั่วโลกในโค้ดที่มีความสำคัญต่อประสิทธิภาพ
```julia
# ❌ WRONG — global variables are slow
x = 1.0
function slow_sum()
    total = 0.0
    for i in 1:1000000
        total += x * i  # x is global, type unstable
    end
    return total
end

# ✅ CORRECT — pass as argument or use const
const X = 1.0  # const globals are fast
function fast_sum()
    total = 0.0
    for i in 1:1000000
        total += X * i
    end
    return total
end

# ✅ BEST — use local variables
function fastest_sum(x::Float64)
    total = 0.0
    for i in 1:1000000
        total += x * i
    end
    return total
end
```

---

## 3. การจัดทำดัชนีแบบ 1-Based
```julia
# ❌ WRONG — 0-based indexing (from other languages)
arr = [10, 20, 30]
arr[0]  # BoundsError!

# ✅ CORRECT — Julia is 1-indexed
arr[1]  # 10
```

---

## 4. ไม่ใช้การจัดส่งหลายรายการ
```julia
# ❌ WRONG — if/else on type
function area(shape)
    if shape isa Circle
        return π * shape.r^2
    elseif shape isa Rectangle
        return shape.w * shape.h
    end
end

# ✅ CORRECT — multiple dispatch
area(c::Circle) = π * c.r^2
area(r::Rectangle) = r.w * r.h
```

---

## 5. การจัดสรรอาร์เรย์ในลูป
```julia
# ❌ WRONG — allocating arrays in loops
function process(data)
    results = []
    for x in data
        push!(results, x^2)  # type-unstable, reallocations
    end
    return results
end

# ✅ CORRECT — pre-allocate
function process(data::Vector{Float64})
    results = Vector{Float64}(undef, length(data))
    for i in eachindex(data)
        results[i] = data[i]^2
    end
    return results
end

# ✅ BEST — broadcasting
process(data) = data .^ 2
```

---

## 6. ไม่เข้าใจ`===`กับ `==`
```julia
# ❌ WRONG — == for identity check
NaN == NaN   # false (IEEE 754)
1 === 1.0    # false (different types)

# ✅ CORRECT — === for identity, == for value
NaN === NaN  # true
1 == 1.0     # true (value equality)
```

---

## 7. การต่อต้านรูปแบบ: ไม่ใช้การออกอากาศ
```julia
# ❌ WRONG — explicit loops for element-wise operations
result = similar(a)
for i in eachindex(a, b)
    result[i] = a[i] + b[i]
end

# ✅ CORRECT — broadcasting
result = a .+ b
result = sin.(a) .+ cos.(b)
```

---

## สรุป
ประสิทธิภาพของ Julia ขึ้นอยู่กับความเสถียรของประเภท: หลีกเลี่ยงตัวแปรส่วนกลางในโค้ดร้อน ใช้การจัดส่งหลายรายการแทนการใช้ if/else บนประเภท การจัดสรรอาร์เรย์ล่วงหน้า ใช้การออกอากาศสำหรับการดำเนินการตามองค์ประกอบ และใส่คำอธิบายประกอบประเภทเมื่อจำเป็น Julia ให้รางวัลแก่นักพัฒนาที่เขียนโค้ดประเภทเสถียรและใช้ประโยชน์จากการจัดส่งหลายรายการ มาโคร`@code_warntype`เป็นเพื่อนที่ดีที่สุดของคุณในการค้นหาความไม่เสถียรของประเภท