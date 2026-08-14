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

# Julia — Kesalahan Umum & Anti-Pola
Dokumen ini berisi katalog kesalahan, jebakan, dan anti-pola paling umum di Julia beserta koreksinya.
---

## 1. Ketik Ketidakstabilan di Fungsi
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

## 2. Variabel Global dalam Kode Kritis Kinerja
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

## 3. Pengindeksan Berbasis 1
```julia
# ❌ WRONG — 0-based indexing (from other languages)
arr = [10, 20, 30]
arr[0]  # BoundsError!

# ✅ CORRECT — Julia is 1-indexed
arr[1]  # 10
```

---

## 4. Tidak Menggunakan Banyak Pengiriman
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

## 5. Alokasi Array dalam Loop
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

## 6. Tidak Memahami`===`vs `==`
```julia
# ❌ WRONG — == for identity check
NaN == NaN   # false (IEEE 754)
1 === 1.0    # false (different types)

# ✅ CORRECT — === for identity, == for value
NaN === NaN  # true
1 == 1.0     # true (value equality)
```

---

## 7. Anti Pola : Tidak Menggunakan Broadcasting
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

## Ringkasan
Performa Julia bergantung pada stabilitas tipe: hindari variabel global dalam kode panas, gunakan beberapa pengiriman alih-alih if/else pada tipe, pra-alokasi array, gunakan penyiaran untuk operasi berdasarkan elemen, dan anotasi tipe bila diperlukan. Julia memberi penghargaan kepada pengembang yang menulis kode tipe stabil dan memanfaatkan banyak pengiriman. Makro`@code_warntype`adalah teman terbaik Anda untuk menemukan ketidakstabilan tipe.