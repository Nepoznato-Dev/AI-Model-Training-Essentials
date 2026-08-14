<!--
---
# Metadata
title: "Julia — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, idiomatic Julia code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [julia, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Julia — wzorce idiomatyczne i najlepsze praktyki
W tym przewodniku opisano idiomatyczne wzorce i najlepsze praktyki dotyczące pisania czystego, idiomatycznego kodu Julii.
---

## Stabilność typu
```julia
# ✅ Type-stable functions
function compute(x::Float64)::Float64
    return x^2 + 1.0
end

# ✅ Avoid type instability
# ❌
function bad(x)
    if x > 0
        return 1      # Int
    else
        return 1.0    # Float64
    end
end

# ✅
function good(x)
    if x > 0
        return 1.0    # Float64
    else
        return 0.0    # Float64
    end
end

# ✅ Concrete types in structs
struct User
    name::String
    age::Int
    email::String
end
```

---

## Wiele wysyłek
```julia
# ✅ Define methods for different types
area(c::Circle) = π * c.r^2
area(r::Rectangle) = r.w * r.h
area(s::Square) = s.side^2

# ✅ Parametric types
struct Point{T<:Real}
    x::T
    y::T
end

distance(p1::Point{T}, p2::Point{T}) where {T} = 
    sqrt((p1.x - p2.x)^2 + (p1.y - p2.y)^2)
```

---

## Nadawanie
```julia
# ✅ Broadcasting with .
result = sin.(x) .+ cos.(x)
squared = x .^ 2

# ✅ Dot fusion (avoids temporary arrays)
result = @. sin(x) + cos(x)

# ✅ Broadcast with functions
f.(args...)

# ✅ Map for simple cases
map(x -> x^2, items)
```

---

## Wzorce funkcjonalne
```julia
# ✅ Pipe operator (|>)
result = data |>
    filter(x -> x > 0) |>
    map(x -> x^2) |>
    sum

# ✅ Comprehensions
squares = [x^2 for x in 1:10]
evens = [x for x in 1:100 if iseven(x)]
matrix = [i + j for i in 1:3, j in 1:3]

# ✅ Reduce
total = reduce(+, items)
combined = foldl(*, strings)

# ✅ Do syntax
open("file.txt") do f
    for line in eachline(f)
        println(line)
    end
end
```

---

## Obsługa błędów
```julia
# ✅ Custom exceptions
struct ValidationError <: Exception
    field::String
    message::String
end

Base.showerror(io::IO, e::ValidationError) = 
    print(io, "Validation: $(e.field) - $(e.message)")

# ✅ try/catch
try
    result = risky_operation()
catch e
    if e isa ValidationError
        println("Validation failed: ", e.field)
    else
        rethrow()
    end
end

# ✅ Assertions
@assert x > 0 "x must be positive"
```

---

## Wydajność
```julia
# ✅ Pre-allocate arrays
function process(n::Int)
    result = Vector{Float64}(undef, n)
    for i in 1:n
        result[i] = compute(i)
    end
    return result
end

# ✅ Use views to avoid copies
@views result = data[1:100]

# ✅ Avoid globals (use const or let)
const PI = 3.14159265358979

# ✅ Type annotations for function arguments
function fast_sum(x::Vector{Float64})::Float64
    total = 0.0
    @inbounds for i in eachindex(x)
        total += x[i]
    end
    return total
end
```

---

## Streszczenie
Idiomy Julii kładą nacisk na: stabilność typów, wielokrotne wysyłanie, nadawanie za pomocą`.`, rozumienie i wydajność poprzez konkretne typy. Postępuj zgodnie z Przewodnikiem po stylach Julii, użyj JuliaFormatter do formatowania i JET do analizy wnioskowania o typie. Julia ceni „domyślnie rób to szybko” — napisz czysty kod i pozwól kompilatorowi JIT na optymalizację.