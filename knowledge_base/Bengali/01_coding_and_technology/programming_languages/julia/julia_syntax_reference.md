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
# জুলিয়া — সিনট্যাক্স রেফারেন্স
এই নথিটি জুলিয়া (1.x) এর জন্য একটি ব্যাপক, কাঠামোগত সিনট্যাক্স রেফারেন্স প্রদান করে। এটি সম্পূর্ণ সিনট্যাক্স প্যাটার্ন, মাল্টিপল ডিসপ্যাচ, ম্যাক্রো, মেটাপ্রোগ্রামিং এবং বৈজ্ঞানিক কম্পিউটিং-এ ফোকাস করে মূল জুলিয়া রেফারেন্সের পরিপূরক।
---

## অপারেটর এবং এক্সপ্রেশন
### মূল অপারেটর
| অপারেটর | নাম | উদাহরণ | নোট |
|----------|------|---------|-------|
| `+``-``*``/``^`| পাটিগণিত | `2^10`| |
| `÷`| পূর্ণসংখ্যা বিভাজন | `7 ÷ 3`|`div(7, 3)`|
| `%``\` | মডুলাস/বাকি | `7 % 3`| |
| `==``!=` | সমতা | `a == b`| মূল্য সমতা |
| `===`| পরিচয় | `a === b`| একই বস্তু |
| `<``>``<=``>=` | তুলনা | `a >= b`| চেইনযোগ্য:`1 < x < 10`|
| `&&``\|\|``!`| যৌক্তিক | `a && b`| শর্ট সার্কিট |
| `&``\|``⊻``~` | বিটওয়াইজ | `a & b`| `⊻`হল XOR |
| `:`| পরিসীমা | `1:10`| `start:step:stop`|
| `..`| ব্যবধান | `1..10`| IntervalSets প্রয়োজন |
| `∈``∉``⊆`| সদস্যপদ সেট করুন | `x ∈ S`| `in(x, S)`|
| `∘`| রচনা | `f ∘ g`| `(f ∘ g)(x) == f(g(x))`|
| `\|>`| পাইপ | `x \|> f`| `f(x)`|
| `=>`| জোড়া | `a => b`| নির্দেশাবলীর জন্য |
| `...`| স্প্ল্যাট | `f(args...)`| সংগ্রহ প্রসারিত করুন |
### শৃঙ্খলিত তুলনা
```julia
# Julia supports mathematical chaining
1 < x < 10          # equivalent to 1 < x && x < 10
0 ≤ y ≤ 1           # Unicode operators work
-a < b < -a + 1     # complex chains allowed
```

---

## নিয়ন্ত্রণ প্রবাহ
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

## ফাংশন এবং একাধিক প্রেরণ
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

## প্রকার ও কাঠামো
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

## সংগ্রহ
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

## ম্যাক্রো এবং মেটাপ্রোগ্রামিং
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

## ত্রুটি হ্যান্ডলিং এবং মডিউল
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

## সারাংশ
জুলিয়ার সিনট্যাক্স পরিষ্কার, গাণিতিক এবং অভিব্যক্তিপূর্ণ। মাল্টিপল ডিসপ্যাচ সকল আর্গুমেন্ট প্রকারের উপর ভিত্তি করে ফাংশনকে ভিন্নভাবে আচরণ করতে দেয়, মার্জিত কোড সংগঠনকে সক্ষম করে। ম্যাক্রো সি-স্টাইল প্রিপ্রসেসর ম্যাক্রোর জটিলতা ছাড়াই শক্তিশালী মেটাপ্রোগ্রামিং প্রদান করে। টাইপ সিস্টেম — প্যারামেট্রিক প্রকার, বিমূর্ত প্রকার এবং ইউনিয়নের ধরন সহ — নমনীয়তা এবং কর্মক্ষমতা উভয়ই সক্ষম করে। জুলিয়ার 1-ভিত্তিক সূচীকরণ, বোধগম্যতা এবং ডু-ব্লক সিনট্যাক্স এটিকে গাণিতিক এবং বৈজ্ঞানিক কম্পিউটিং-এর জন্য স্বাভাবিক করে তোলে। টাইপ ইনফারেন্স সহ JIT সংকলনের মাধ্যমে ভাষাটি তার "পাইথনের মতো হাঁটা, সি এর মতো দৌড়" প্রতিশ্রুতি অর্জন করে।