---
# Metadata
title: "Julia — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Julia with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# জুলিয়া — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্নস
এই নথিটি সংশোধন সহ জুলিয়ার সবচেয়ে সাধারণ ভুল, ফাঁদ এবং অ্যান্টি-প্যাটার্নগুলি ক্যাটালগ করে৷
---

## 1. ফাংশনে অস্থিরতা টাইপ করুন
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

## 2. পারফরম্যান্স-ক্রিটিকাল কোডে গ্লোবাল ভেরিয়েবল
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

## 3. 1-ভিত্তিক ইন্ডেক্সিং
```julia
# ❌ WRONG — 0-based indexing (from other languages)
arr = [10, 20, 30]
arr[0]  # BoundsError!

# ✅ CORRECT — Julia is 1-indexed
arr[1]  # 10
```

---

## 4. একাধিক ডিসপ্যাচ ব্যবহার করছেন না
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

## 5. লুপগুলিতে অ্যারে বরাদ্দ
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

## 6.`===`বনাম`==`বোঝা যাচ্ছে না
```julia
# ❌ WRONG — == for identity check
NaN == NaN   # false (IEEE 754)
1 === 1.0    # false (different types)

# ✅ CORRECT — === for identity, == for value
NaN === NaN  # true
1 == 1.0     # true (value equality)
```

---

## 7. অ্যান্টি-প্যাটার্ন: সম্প্রচার ব্যবহার না করা
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

## সারাংশ
জুলিয়ার পারফরম্যান্স নির্ভর করে টাইপের স্থায়িত্বের উপর: হট কোডে গ্লোবাল ভেরিয়েবল এড়িয়ে চলুন, টাইপের ক্ষেত্রে if/else এর পরিবর্তে মাল্টিপল ডিসপ্যাচ ব্যবহার করুন, প্রাক-বরাদ্দ অ্যারে, উপাদান-ভিত্তিক ক্রিয়াকলাপের জন্য সম্প্রচার ব্যবহার করুন এবং প্রয়োজনে টীকা টাইপ করুন। জুলিয়া এমন ডেভেলপারদের পুরস্কৃত করে যারা টাইপ-স্টেবল কোড লেখে এবং একাধিক ডিসপ্যাচ লিভারেজ করে।`@code_warntype`ম্যাক্রো টাইপ অস্থিরতা খোঁজার জন্য আপনার সেরা বন্ধু।