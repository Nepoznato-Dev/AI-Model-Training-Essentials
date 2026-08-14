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
# Джулия — Распространенные ошибки и антипаттерны
В этом документе перечислены наиболее распространенные ошибки, ловушки и антишаблоны в Julia с исправлениями.
---

## 1. Нестабильность типов в функциях
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

## 2. Глобальные переменные в коде, критичном к производительности
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

## 3. Индексация на основе 1
```julia
# ❌ WRONG — 0-based indexing (from other languages)
arr = [10, 20, 30]
arr[0]  # BoundsError!

# ✅ CORRECT — Julia is 1-indexed
arr[1]  # 10
```

---

## 4. Не использовать множественную отправку
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

## 5. Распределение массива в циклах
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

## 6. Непонимание`===`и `==`
```julia
# ❌ WRONG — == for identity check
NaN == NaN   # false (IEEE 754)
1 === 1.0    # false (different types)

# ✅ CORRECT — === for identity, == for value
NaN === NaN  # true
1 == 1.0     # true (value equality)
```

---

## 7. Антипаттерн: отказ от широковещания
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

## Краткое содержание
Производительность Julia зависит от стабильности типов: избегайте глобальных переменных в «горячем» коде, используйте множественную отправку вместо if/else для типов, предварительно выделяйте массивы, используйте широковещательную рассылку для поэлементных операций и при необходимости аннотируйте типы. Джулия награждает разработчиков, которые пишут стабильный по типам код и используют множественную диспетчеризацию. Макрос`@code_warntype`— ваш лучший помощник в обнаружении нестабильности типов.