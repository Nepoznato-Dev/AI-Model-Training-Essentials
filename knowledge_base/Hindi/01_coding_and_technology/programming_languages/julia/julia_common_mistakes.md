<!--
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

-->
# जूलिया - सामान्य गलतियाँ और विरोधी पैटर्न
यह दस्तावेज़ सुधार के साथ जूलिया में सबसे आम गलतियों, जाल और विरोधी पैटर्न को सूचीबद्ध करता है।
---

## 1. कार्यों में प्रकार की अस्थिरता
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

## 2. प्रदर्शन-महत्वपूर्ण कोड में वैश्विक चर
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

## 3. 1-आधारित अनुक्रमण
```julia
# ❌ WRONG — 0-based indexing (from other languages)
arr = [10, 20, 30]
arr[0]  # BoundsError!

# ✅ CORRECT — Julia is 1-indexed
arr[1]  # 10
```

---

## 4. मल्टीपल डिस्पैच का उपयोग न करना
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

## 5. लूप्स में ऐरे आवंटन
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

## 6.`===`बनाम`==`को नहीं समझना
```julia
# ❌ WRONG — == for identity check
NaN == NaN   # false (IEEE 754)
1 === 1.0    # false (different types)

# ✅ CORRECT — === for identity, == for value
NaN === NaN  # true
1 == 1.0     # true (value equality)
```

---

## 7. एंटी-पैटर्न: प्रसारण का उपयोग नहीं करना
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

## सारांश
जूलिया का प्रदर्शन प्रकार की स्थिरता पर निर्भर करता है: हॉट कोड में वैश्विक चर से बचें, प्रकारों पर if/else के बजाय एकाधिक प्रेषण का उपयोग करें, पूर्व-आवंटन सरणी, तत्व-वार संचालन के लिए प्रसारण का उपयोग करें, और आवश्यकता होने पर प्रकारों को एनोटेट करें। जूलिया उन डेवलपर्स को पुरस्कृत करती है जो टाइप-स्टेबल कोड लिखते हैं और मल्टीपल डिस्पैच का लाभ उठाते हैं। प्रकार की अस्थिरता का पता लगाने के लिए`@code_warntype`मैक्रो आपका सबसे अच्छा मित्र है।