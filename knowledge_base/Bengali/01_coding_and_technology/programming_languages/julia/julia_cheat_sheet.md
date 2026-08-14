---
# Metadata
title: "Julia — Cheat Sheet"
description: "Quick-reference cheat sheet for Julia syntax, types, and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [julia, scientific, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# জুলিয়া — চিট শীট
## মৌলিক
```julia
# Variables
name = "Alice"
age = 30
pi = 3.14159
active = true
nothing_val = nothing

# Types
typeof(name)       # String
typeof(42)         # Int64
typeof(42.0)       # Float64
typeof(true)       # Bool
typeof(nothing)    # Nothing
typeof(1 + 2im)    # Complex{Int64}

# Type annotations
x::Int64 = 42
name::String = "Alice"

# String interpolation
"Hello, $name!"
"Age: $(age + 1)"
"Pi: $(round(pi, digits=2))"

# String operations
length(name)
uppercase(name)
lowercase(name)
strip(name)
occursin("lic", name)
replace(name, "Alice" => "Bob")
name[1:3]          # "Ali" (1-indexed!)
split("a,b,c", ",")
join(["a","b","c"], ", ")
repeat("ha", 3)
string(42)
parse(Int, "42")
```

## অ্যারে এবং সংগ্রহ
```julia
# Array
arr = [1, 2, 3, 4, 5]
arr[1]              # 1 (1-indexed!)
arr[2:4]            # [2, 3, 4]
arr[end]            # 5
push!(arr, 6)
pop!(arr)
pushfirst!(arr, 0)
popfirst!(arr)
length(arr)
sum(arr)
mean(arr)           # using Statistics
sort(arr)
sort(arr, rev=true)
unique(arr)
filter(x -> x > 3, arr)
map(x -> x * 2, arr)
reduce(+, arr)
[arr[i] for i in 1:length(arr)]  # comprehension
arr .^ 2            # broadcasting: element-wise square

# Matrix
m = [1 2 3; 4 5 6]
m[1, :]             # first row
m[:, 2]             # second column
m'                  # transpose
m * m'              # matrix multiply
size(m)             # (2, 3)

# Dict
d = Dict("alice" => 90, "bob" => 85)
d["alice"]
get(d, "charlie", 0)
d["charlie"] = 78
keys(d)
values(d)
haskey(d, "alice")

# Tuple (immutable)
t = (1, "hello", 3.14)
t[1]
a, b, c = t         # destructuring

# NamedTuple
nt = (name = "Alice", age = 30)
nt.name
nt[:age]

# Set
s = Set([1, 2, 3])
push!(s, 4)
4 in s              # true
```

## নিয়ন্ত্রণ প্রবাহ
```julia
if condition
    # ...
elseif other
    # ...
else
    # ...
end

# Ternary
result = condition ? "yes" : "no"

# Loops
for i in 1:10
    println(i)
end

for item in collection
    println(item)
end

for (i, val) in enumerate(collection)
    println("$i: $val")
end

for i in 1:2:10     # step 2
    println(i)
end

while condition
    # ...
end

# Comprehensions
[x^2 for x in 1:10]
[x for x in 1:10 if x > 5]
[x*y for x in 1:3, y in 1:3]
```

## ফাংশন
```julia
# Basic function
function add(a, b)
    a + b           # last expression is returned
end

# Short form
add(a, b) = a + b

# Multiple dispatch
greet(name::String) = "Hello, $name!"
greet(name::Symbol) = "Hello, :$name!"

# Default & keyword args
function greet(name; greeting="Hello")
    "$greeting, $name!"
end
greet("Alice"; greeting="Hi")

# Variadic
flexible(args...) = println(args)

# Multiple return values
function stats(x)
    return mean(x), std(x), length(x)
end
m, s, n = stats(data)

# Anonymous function
square = x -> x^2
map(x -> x * 2, arr)

# Do-block
open("file.txt", "w") do io
    write(io, "hello")
end
```

## প্রকার ও কাঠামো
```julia
# Abstract type
abstract type Shape end

# Concrete types
struct Circle <: Shape
    radius::Float64
end

mutable struct Rectangle <: Shape
    width::Float64
    height::Float64
end

# Multiple dispatch
area(c::Circle) = π * c.radius^2
area(r::Rectangle) = r.width * r.height

# Parametric types
struct Point{T<:Number}
    x::T
    y::T
end

# Type unions
const StringOrSymbol = Union{String, Symbol}

# Enums
@enum Color Red Green Blue

# Type stability tip: annotate for performance
function compute(x::Float64)::Float64
    return x^2 + 1.0
end
```

## সম্প্রচার
```julia
# Dot syntax for element-wise operations
arr .+ 1
arr .* 2
arr .^ 2
sin.(arr)

# Broadcasting with functions
f.(arr1, arr2)

# In-place operations
arr .*= 2
arr .+= 1

# Broadcast fusion
result = @. sin(arr)^2 + cos(arr)^2  # fused loop
```

## মডিউল এবং প্যাকেজ
```julia
# Module
module MyModule
    export greet, hello
    greet(name) = "Hello, $name!"
    hello() = "Hi!"
end

using MyModule
import MyModule: greet

# Package management
using Pkg
Pkg.add("DataFrames")
Pkg.add("Plots")

using DataFrames
using Plots
```

## ত্রুটি হ্যান্ডলিং
```julia
try
    result = risky_operation()
catch e
    if e isa DivideError
        println("Division by zero")
    else
        rethrow()
    end
finally
    cleanup()
end

# Custom error
struct MyError <: Exception
    msg::String
end
throw(MyError("something failed"))

# Assertions
@assert x > 0 "x must be positive"

# Logging
using Logging
@info "Information"
@warn "Warning"
@error "Error"
@debug "Debug"
```
