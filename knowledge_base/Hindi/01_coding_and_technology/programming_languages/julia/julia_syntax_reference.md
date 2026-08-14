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
# जूलिया - सिंटेक्स संदर्भ
यह दस्तावेज़ जूलिया (1.x) के लिए एक व्यापक, संरचित वाक्यविन्यास संदर्भ प्रदान करता है। यह संपूर्ण सिंटैक्स पैटर्न, मल्टीपल डिस्पैच, मैक्रोज़, मेटाप्रोग्रामिंग और वैज्ञानिक कंप्यूटिंग पर ध्यान केंद्रित करके मुख्य जूलिया संदर्भ को पूरक करता है।
---

## ऑपरेटर्स और अभिव्यक्तियाँ
### कोर ऑपरेटर्स
| ऑपरेटर | नाम | उदाहरण | नोट्स |
|-------|------|------|-------|
| `+``-``*``/``^`| अंकगणित | `2^10`| |
| `÷`| पूर्णांक विभाजन | `7 ÷ 3`|`div(7, 3)`के समान |
| `%``\` | मापांक/शेष | `7 % 3`| |
| `==``!=` | समानता | `a == b`| मूल्य समानता |
| `===`| पहचान | `a === b`| वही वस्तु |
| `<``>``<=``>=` | तुलना | `a >= b`| श्रृंखलाबद्ध:`1 < x < 10`|
| `&&``\|\|``!`| तार्किक | `a && b`| शॉर्ट-सर्किट |
| `&``\|``⊻``~` | बिटवाइज़ | `a & b`| `⊻`XOR है |
| `:`| रेंज | `1:10`| `start:step:stop`|
| `..`| अंतराल | `1..10`| इंटरवलसेट की आवश्यकता है |
| `∈``∉``⊆`| सदस्यता सेट करें | `x ∈ S`| `in(x, S)`|
| `∘`| रचना | `f ∘ g`| `(f ∘ g)(x) == f(g(x))`|
| `\|>`| पाइप | `x \|> f`| `f(x)`|
| `=>`| जोड़ी | `a => b`| हुक्मों के लिए |
| `...`| छींटे | `f(args...)`| संग्रह का विस्तार करें |
### जंजीर तुलना
```julia
# Julia supports mathematical chaining
1 < x < 10          # equivalent to 1 < x && x < 10
0 ≤ y ≤ 1           # Unicode operators work
-a < b < -a + 1     # complex chains allowed
```

---

## प्रवाह को नियंत्रित करें
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

## फ़ंक्शन और एकाधिक प्रेषण
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

## प्रकार एवं संरचनाएँ
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

## संग्रह
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

## मैक्रोज़ और मेटाप्रोग्रामिंग
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

## त्रुटि प्रबंधन और मॉड्यूल
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

## सारांश
जूलिया का वाक्य-विन्यास स्वच्छ, गणितीय और अभिव्यंजक है। एकाधिक प्रेषण कार्यों को सभी तर्क प्रकारों के आधार पर अलग-अलग व्यवहार करने की अनुमति देता है, जिससे सुरुचिपूर्ण कोड संगठन सक्षम होता है। मैक्रोज़ सी-शैली प्रीप्रोसेसर मैक्रोज़ की जटिलता के बिना शक्तिशाली मेटाप्रोग्रामिंग प्रदान करते हैं। प्रकार प्रणाली - पैरामीट्रिक प्रकार, अमूर्त प्रकार और संघ प्रकार के साथ - लचीलापन और प्रदर्शन दोनों को सक्षम बनाती है। जूलिया की 1-आधारित अनुक्रमणिका, समझ और डू-ब्लॉक सिंटैक्स इसे गणितीय और वैज्ञानिक कंप्यूटिंग के लिए स्वाभाविक बनाते हैं। भाषा टाइप अनुमान के साथ जेआईटी संकलन के माध्यम से अपने "पायथन की तरह चलना, सी की तरह दौड़ना" का वादा हासिल करती है।