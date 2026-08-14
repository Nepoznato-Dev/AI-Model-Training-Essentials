<!--
---
# Metadata
title: "Julia — Syntax Reference"
description: "Detailed syntax reference for Julia covering multiple dispatch, macros, metaprogramming, parallelism, and scientific computing patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [julia, syntax-reference, multiple-dispatch, macros, metaprogramming, parallelism, scientific, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Julia — 語法參考
本文檔為 Julia (1.x) 提供了全面、結構化的語法參考。它透過關注詳盡的語法模式、多重調度、宏、元編程和科學計算來補充主要的 Julia 參考。
---

## 運算子和表達式
### 核心運營商
|操作員|名稱 |範例|筆記|
|----------|------|---------|--------|
|`+``-``*``/``^`|算術|`2^10`| |
|`÷`|整數除法 |`7 ÷ 3`|與`div(7, 3)`相同 |
|`%``\` |模數/餘數 |`7 % 3`| |
|`==``!=` |平等|`a == b`|價值平等|
|`===`|身分|`a === b`|相同的物件 |
|`<``>``<=``>=` |比較|`a >= b`|可連結：`1 < x < 10` |
|`&&``\|\|``!`|邏輯 |`a && b`|短路|
|`&``\|``⊻``~` |位元|`a & b`|`⊻`是異或 |
|`:`|範圍 |`1:10`|`start:step:stop`|
|`..`|間隔 |`1..10`|需要 IntervalSets |
|`∈``∉``⊆`|設定會員 |`x ∈ S`|`in(x, S)`|
|`∘`|成分|`f ∘ g`|`(f ∘ g)(x) == f(g(x))`|
|`\|>`|管材|`x \|> f`|`f(x)`|
|`=>`|配對 |`a => b`|對於聽寫 |
|`...`|啪啪 |`f(args...)`|擴大收藏|
### 連鎖比較
```julia
# Julia supports mathematical chaining
1 < x < 10          # equivalent to 1 < x && x < 10
0 ≤ y ≤ 1           # Unicode operators work
-a < b < -a + 1     # complex chains allowed
```

---

## 控制流程
```julia
# if / elseif / else
if x > 0
    "positive"
elseif x < 0
    "negative"
else
    "zero"
end

# Ternary
status = x > 0 ? "positive" : "non-positive"

# Short-circuit evaluation
x > 0 && println("positive")
x == 0 || println("not zero")

# for loops
for i in 1:10
    println(i)
end

# Nested loops (cartesian product)
for i in 1:3, j in 1:3
    print("($i,$j) ")
end

# Iterate over collections
for (key, value) in dict
    println("$key => $value")
end

for (index, value) in enumerate(array)
    println("$index: $value")
end

# while
while condition
    do_something()
end

# Comprehensions
squares = [x^2 for x in 1:10]
evens = [x for x in 1:100 if x % 2 == 0]
matrix = [i + j for i in 1:3, j in 1:3]
dict_comp = Dict(x => x^2 for x in 1:5)

# Generator expressions (lazy)
sum(x^2 for x in 1:1000000)  # no intermediate array
```

---

## 函數與多重調度
```julia
# Basic function
function add(x, y)
    x + y
end

# Single-expression shorthand
add(x, y) = x + y

# Type annotations
function divide(x::Float64, y::Float64)::Float64
    x / y
end

# Multiple dispatch — different methods for different types
area(c::Circle) = π * c.radius^2
area(r::Rectangle) = r.width * r.height
area(t::Triangle) = 0.5 * t.base * t.height

# Optional and keyword arguments
function greet(name; greeting="Hello", punctuation="!")
    "$greeting, $name$punctuation"
end
greet("Alice")                        # "Hello, Alice!"
greet("Bob", greeting="Hi")           # "Hi, Bob!"

# Variadic arguments
function mysum(args...)
    total = 0
    for a in args
        total += a
    end
    total
end
mysum(1, 2, 3, 4)  # 10

# Do-block syntax
map([1, 2, 3]) do x
    x^2
end
# equivalent to: map(x -> x^2, [1, 2, 3])

# Anonymous functions
square = x -> x^2
add = (x, y) -> x + y

# Closures
function make_adder(n)
    x -> x + n
end
add5 = make_adder(5)
add5(10)  # 15
```

---

## 類型和結構
```julia
# Concrete type (like a C struct)
struct Point
    x::Float64
    y::Float64
end
p = Point(1.0, 2.0)
p.x  # 1.0

# Mutable struct
mutable struct Counter
    value::Int
end
c = Counter(0)
c.value += 1

# Parametric types
struct Pair{T, S}
    first::T
    second::S
end
Pair(1, "hello")  # Pair{Int64, String}(1, "hello")

# Abstract types
abstract type Shape end
struct Circle <: Shape
    radius::Float64
end
struct Rectangle <: Shape
    width::Float64
    height::Float64
end

# Type hierarchy
supertype(Circle)  # Shape
subtypes(Shape)    # [Circle, Rectangle]

# Union types
IntOrString = Union{Int, String}
function process(x::IntOrString)
    x isa Int ? x * 2 : x * "!"
end

# Nothing and Missing
nothing   # represents no value (like null)
missing   # represents missing data (statistical)
isnothing(x)
ismissing(x)
skipmissing([1, missing, 3])  # iterator skipping missing
```

---

## 收藏
```julia
# Array (mutable, 1-indexed)
arr = [1, 2, 3, 4, 5]
push!(arr, 6)
pop!(arr)
arr[1]           # 1 (1-indexed!)
arr[end]         # 5
arr[2:4]         # [2, 3, 4]
arr[end-2:end]   # [3, 4, 5]

# Matrix
mat = [1 2 3; 4 5 6; 7 8 9]
mat[2, 3]        # 6
mat[:, 1]        # [1, 4, 7] (first column)
mat'             # transpose

# Dict
d = Dict("a" => 1, "b" => 2)
d["a"]           # 1
get(d, "z", 0)   # 0 (default)
haskey(d, "a")

# Tuple (immutable)
t = (1, "hello", 3.14)
t[1]             # 1
a, b, c = t      # destructuring

# NamedTuple
nt = (name="Alice", age=30)
nt.name          # "Alice"
nt[:age]         # 30

# Set
s = Set([1, 2, 3, 2, 1])  # Set([1, 2, 3])
push!(s, 4)
4 ∈ s            # true

# Array operations
sum(arr)
prod(arr)
maximum(arr)
minimum(arr)
sort(arr)
sort(arr, rev=true)
unique(arr)
filter(x -> x > 3, arr)
map(x -> x^2, arr)
reduce(+, arr)
cumsum(arr)
```

---

## 巨集和元編程
```julia
# Macro definition
macro sayhello(name)
    return :(println("Hello, " * $name * "!"))
end
@sayhello "World"

# Timing macro
@time [x^2 for x in 1:1000000]
@btime sort(rand(1000))

# Expression introspection
ex = :(x + y * z)
dump(ex)           # show structure
Meta.show_sexpr(ex) # S-expression

# Generated functions (compile-time specialization)
@generated function fast_op(x)
    if x <: Integer
        return :(x * 2)
    else
        return :(x + 0.5)
    end
end

# Quote — capture expression without evaluation
ex = quote
    x = 1
    y = 2
    x + y
end
```

---

## 錯誤處理和模組
```julia
# try / catch / finally
try
    result = risky_operation()
catch e
    @error "Failed" exception=e
finally
    cleanup()
end

# Custom exception
struct ValidationError <: Exception
    field::String
    msg::String
end
throw(ValidationError("age", "must be positive"))

# Module
module MyModule
    export public_func, PublicType

    function public_func()
        "hello"
    end

    struct PublicType
        value::Int
    end

    function _private_func()  # not exported
        "internal"
    end
end

using MyModule
import MyModule: public_func
```

---

＃＃ 概括
Julia 的語法簡潔、數學且富有表現力。多重分派允許函數根據所有參數類型表現不同，從而實現優雅的程式碼​​組織。巨集提供了強大的元編程，而沒有 C 風格預處理器巨集的複雜性。類型系統（具有參數類型、抽象類型和聯合類型）可實現靈活性和效能。 Julia 基於 1 的索引、推導式和 do-block 語法使其非常適合數學和科學計算。該語言透過帶有類型推斷的 JIT 編譯實現了「像 Python 一樣行走，像 C 一樣運行」的承諾。