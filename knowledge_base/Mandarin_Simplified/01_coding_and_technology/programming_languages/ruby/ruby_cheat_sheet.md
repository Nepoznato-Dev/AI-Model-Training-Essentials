---
# Metadata
title: "Ruby — Cheat Sheet"
description: "Quick-reference cheat sheet for Ruby syntax, blocks, and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [ruby, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Ruby — 备忘单
## 基础知识
```ruby
# Variables
name = "Alice"       # local variable
AGE = 30             # constant
$name = "global"     # global (avoid)
@age = 30            # instance variable
@@count = 0          # class variable
$: << "./lib"        # load path

# Types
x = 42               # Integer
pi = 3.14             # Float
name = "Alice"        # String
active = true         # TrueClass / FalseClass
nothing = nil         # NilClass
sym = :hello          # Symbol (immutable, interned)

# String interpolation
"Hello, #{name}!"
"2 + 2 = #{2 + 2}"

# String methods
name.length           # 5
name.upcase           # "ALICE"
name.downcase         # "alice"
name.strip            # remove whitespace
name.include?("lic")  # true
name.reverse          # "ecilA"
name.chars.to_a       # ["A","l","i","c","e"]
name.gsub("Alice", "Bob")
name.split(//)        # ["A","l","i","c","e"]
"hello".freeze        # immutable string
```

## 数据结构
```ruby
# Array
arr = [1, 2, 3]
arr << 4              # push
arr.push(5)
arr.pop               # remove last
arr.unshift(0)        # add to front
arr.shift             # remove first
arr[1..3]             # slice [2, 3, 4]
arr.map { |x| x * 2 }
arr.select { |x| x > 2 }
arr.reject { |x| x.even? }
arr.reduce(0) { |sum, x| sum + x }
arr.each { |x| puts x }
arr.each_with_index { |x, i| puts "#{i}: #{x}" }
arr.flat_map { |x| [x, x * 2] }
arr.uniq
arr.compact           # remove nils
arr.zip(other_arr)

# Hash
h = { name: "Alice", age: 30 }
h[:email] = "a@b.com"
h[:name]
h.fetch(:phone, "N/A")  # default
h.keys
h.values
h.each { |k, v| puts "#{k}: #{v}" }
h.merge(other_hash)
h.select { |k, v| v > 25 }
h.transform_keys(&:to_s)
h.transform_values(&:to_s)

# Range
(1..10).to_a          # [1,2,...,10]
(1...10).to_a         # [1,2,...,9]
('a'..'z').to_a
(1..10).include?(5)   # true

# Set
require 'set'
s = Set.new([1, 2, 3])
s << 4
s.include?(2)
```

## 控制流程
```ruby
if condition
  # ...
elsif other
  # ...
else
  # ...
end

# Ternary
result = condition ? "yes" : "no"

# Unless (if not)
puts "empty" unless items.any?

# Case/when
case day
when :monday, :tuesday
  puts "early week"
when :wednesday
  puts "midweek"
else
  puts "later"
end

# Case with pattern matching (Ruby 3+)
case [1, "hello"]
in [Integer => n, String]
  puts "matched: #{n}"
end

# Loops
[1, 2, 3].each { |x| puts x }
3.times { |i| puts i }
5.upto(10) { |i| puts i }
10.downto(1) { |i| puts i }
loop { break if condition }
while condition do ... end
```

## 方法和块
```ruby
# Method definition
def greet(name, greeting = "Hello")
  "#{greeting}, #{name}!"
end

# Splat & keyword args
def flexible(*args, **kwargs)
  puts args    # array of positional
  puts kwargs  # hash of keyword
end
flexible(1, 2, name: "Alice")

# Block (yield)
def with_logging
  puts "before"
  yield
  puts "after"
end
with_logging { puts "inside" }

# Proc & Lambda
square = Proc.new { |x| x ** 2 }
double = ->(x) { x * 2 }
square.call(5)   # 25
double.call(5)   # 10

# Enumerable
(1..10).select(&:even?)
%w[hello world].map(&:upcase)
users.sort_by(&:name)
items.group_by(&:category)
items.chunk(&:status).to_h
```

## 类和模块
```ruby
class Animal
  attr_reader :name
  attr_accessor :age

  def initialize(name, age)
    @name = name
    @age = age
  end

  def speak
    raise NotImplementedError
  end

  def to_s
    "#{name} (#{age})"
  end
end

class Dog < Animal
  def speak
    "#{name} barks"
  end
end

# Module (mixin)
module Greetable
  def greet
    "Hello, I'm #{name}"
  end
end

class User
  include Greetable
  attr_reader :name
end

# Struct (simple data class)
Point = Struct.new(:x, :y) do
  def distance_to(other)
    Math.sqrt((x - other.x)**2 + (y - other.y)**2)
  end
end
```

## 错误处理
```ruby
begin
  result = risky_operation
rescue ArgumentError => e
  puts "Bad arg: #{e.message}"
rescue StandardError => e
  puts "Error: #{e.message}"
  retry  # try again
else
  puts "Success"
ensure
  cleanup
end

raise ArgumentError, "Invalid: #{value}"
```

## 常见模式
```ruby
# Destructuring
first, *rest = [1, 2, 3, 4]
a, b = b, a  # swap

# Safe navigation
user&.address&.street

# Frozen string literal
# frozen_string_literal: true

# Dig (nested hash access)
data.dig(:user, :address, :city)

# Tap (side effects in chain)
user.tap { |u| log(u) }.save

# Then (transform in chain)
result.then { |r| transform(r) }.then { |r| format(r) }
```
