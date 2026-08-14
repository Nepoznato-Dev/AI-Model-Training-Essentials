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
# Julia - การอ้างอิงไวยากรณ์
เอกสารนี้ให้การอ้างอิงไวยากรณ์ที่มีโครงสร้างและครอบคลุมสำหรับ Julia (1.x) มันเสริมการอ้างอิง Julia หลักโดยมุ่งเน้นไปที่รูปแบบไวยากรณ์ที่ละเอียดถี่ถ้วน การส่งหลายรายการ มาโคร การเขียนโปรแกรมเมตา และการคำนวณทางวิทยาศาสตร์
---

## ตัวดำเนินการและนิพจน์
### ผู้ประกอบการหลัก
| ตัวดำเนินการ | ชื่อ | ตัวอย่าง | หมายเหตุ |
|----------|-|---------|-------|
| `+``-``*``/``^`| เลขคณิต | `2^10`| |
| `÷`| การหารจำนวนเต็ม | `7 ÷ 3`| เหมือนกับ`div(7, 3)`|
| `%``\` | โมดูลัส/ส่วนที่เหลือ | `7 % 3`| |
| `==``!=` | ความเท่าเทียมกัน | `a == b`| ความเท่าเทียมกันของมูลค่า |
| `===`| ตัวตน | `a === b`| วัตถุเดียวกัน |
| `<``>``<=``>=` | การเปรียบเทียบ | `a >= b`| โซ่ได้:`1 < x < 10`|
| `&&``\|\|``!`| ตรรกะ | `a && b`| ลัดวงจร |
| `&``\|``⊻``~` | ระดับบิต | `a & b`| `⊻`คือ XOR |
| `:`| พิสัย | `1:10`| `start:step:stop`|
| `..`| ช่วงเวลา | `1..10`| ต้องใช้ IntervalSets |
| `∈``∉``⊆`| ตั้งค่าสมาชิก | `x ∈ S`| `in(x, S)`|
| `∘`| องค์ประกอบ | `f ∘ g`| `(f ∘ g)(x) == f(g(x))`|
| `\|>`| ท่อ | `x \|> f`| `f(x)`|
| `=>`| จับคู่ | `a => b`| สำหรับคำสั่ง |
| `...`| เครื่องหมาย | `f(args...)`| ขยายคอลเลกชัน |
### การเปรียบเทียบแบบลูกโซ่
```julia
# Julia supports mathematical chaining
1 < x < 10          # equivalent to 1 < x && x < 10
0 ≤ y ≤ 1           # Unicode operators work
-a < b < -a + 1     # complex chains allowed
```

---

## การควบคุมการไหล
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

## ฟังก์ชั่นและการจัดส่งหลายรายการ
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

## ประเภทและโครงสร้าง
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

## คอลเลกชัน
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

## มาโครและการเขียนโปรแกรมเมตา
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

## การจัดการข้อผิดพลาดและโมดูล
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

## สรุป
ไวยากรณ์ของ Julia นั้นสะอาดตา ตรงตามหลักคณิตศาสตร์ และสื่อความหมายได้ การจัดส่งหลายรายการช่วยให้ฟังก์ชันทำงานแตกต่างกันตามประเภทอาร์กิวเมนต์ทั้งหมด ช่วยให้สามารถจัดระเบียบโค้ดที่สวยงามได้ แมโครให้การเขียนโปรแกรมเมตาที่มีประสิทธิภาพโดยไม่มีความซับซ้อนของมาโครตัวประมวลผลล่วงหน้าแบบ C ระบบประเภท — พร้อมด้วยประเภทพารามิเตอร์, ประเภทนามธรรม และประเภทยูเนียน — ช่วยให้เกิดทั้งความยืดหยุ่นและประสิทธิภาพ การจัดทำดัชนี ความเข้าใจ และไวยากรณ์แบบบล็อกแบบอิง 1 ของ Julia ทำให้การคำนวณทางคณิตศาสตร์และวิทยาศาสตร์เป็นเรื่องธรรมชาติ ภาษาบรรลุคำมั่นสัญญา "เดินเหมือน Python วิ่งเหมือน C" ผ่านการคอมไพล์ JIT ด้วยการอนุมานประเภท