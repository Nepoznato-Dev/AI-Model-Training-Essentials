---
# Metadata
title: "Ruby — Syntax Reference"
description: "Detailed syntax reference for Ruby covering operators, control flow, blocks, metaprogramming, classes, modules, and Ruby idioms."
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
tags: [ruby, syntax-reference, operators, blocks, metaprogramming, oop, coding-and-technology]
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
# Ruby — 语法参考
本文档提供了 Ruby (3.x) 的全面、结构化语法参考。它通过关注详尽的语法模式、块和闭包、元编程和 Ruby 习惯用法来补充主要的 Ruby 参考。
---

## 运算符和表达式
### 核心运营商
|操作员|名称 |示例|笔记|
|----------|------|---------|--------|
| `+``-``*``/``%``**` |算术| `2 ** 10`| `**`是求幂 |
| `==``!=``===``<=>` |平等| `a == b`| `===`是大小写相等； `<=>`是宇宙飞船 |
| `eql?`|价值平等| `a.eql?(b)`|比`==`更严格（检查类型）|
| `equal?`|身份| `a.equal?(b)`|同一物体？ |
| `<``>``<=``>=` |比较| `a >= b`| |
| `&&``\|\|``!`|逻辑 | `a && b`|短路；返回最后评估的值 |
| `and``or``not`|逻辑（低优先级）| `a and b`|避免 — 使用`&&`/`\|\|`/`!`|
| `&``\|``^``~``<<``>>` |按位| `a & b`| |
| `=~``!~` |正则表达式匹配 | `str =~ /pattern/`|返回索引或 nil |
| `..``...` |范围 | `1..10`| `..`包括在内；  `...`独家|
| `?.`|安全导航| `user&.name`|如果用户为零则返回零 |
| `[]``[]=` |元素访问 | `arr[0]`| |
### 真实性
```ruby
# In Ruby, only nil and false are falsy
# Everything else (0, "", [], {}) is truthy
!!0       # true  (unlike most languages!)
!!""      # true
!![]      # true
!!nil     # false
!!false   # false
```

### 运算符优先级（从最高到最低）
|优先级|运营商|
|------------|------------|
| 1（最高）| `**`|
| 2 | `!``~` `+`（一元） |
| 3 | `*``/``%`|
| 4 | `+``-` |
| 5 | `<<``>>` |
| 6 | `&`|
| 7 | `\|``^` |
| 8 | `>``>=``<``<=` |
| 9 | `<=>``==``===``!=``eql?``equal?` |
| 10 | 10 `&&`|
| 11 | 11 `\|\|`|
| 12 | 12 `..``...`（范围）|
| 13 |  `? :`（三元）|
| 14 | 14 `=``+=` 等（作业） |
| 15（最低）| `not``and``or`|
---

## 控制流程
### 条件
```ruby
# if / elsif / else
if score >= 90
  grade = "A"
elsif score >= 80
  grade = "B"
else
  grade = "F"
end

# Modifier form
puts "pass" if score >= 60
return unless valid?

# unless (inverse if)
raise "invalid" unless user.active?

# case/when — uses === (case equality)
case status
when :active    then "Currently active"
when :pending   then "Awaiting activation"
when /error/i   then "Error state"
when 200..299   then "Success range"
when String     then "Unknown string status"
else                 "Unknown"
end

# case as expression (returns value)
description = case shape
              in { type: "circle", radius: r }
                Math::PI * r**2
              in { type: "rectangle", width: w, height: h }
                w * h
              end
```

### 循环
```ruby
# while
count = 0
while count < 10
  count += 1
end

# until (inverse while)
until done?
  process_next
end

# each — the idiomatic Ruby loop
[1, 2, 3].each { |n| puts n }
(1..10).each { |n| print "#{n} " }

# times, upto, downto
5.times { |i| puts i }        # 0..4
1.upto(10) { |n| puts n }     # 1..10
10.downto(1) { |n| puts n }   # 10..1

# loop (infinite — break to exit)
loop do
  break if done?
  process
end

# Loop control
[1, 2, 3, 4, 5].each do |n|
  next if n.even?    # Skip to next iteration
  break if n > 3     # Exit loop
  puts n
end
```

---

## 块、过程和 Lambda 函数
```ruby
# Block — implicit
def with_logging
  puts "Before"
  yield              # Execute the block
  puts "After"
end
with_logging { puts "Inside!" }

# Block with arguments
def each_pair(hash)
  hash.each { |key, value| yield(key, value) }
end

# Explicit block parameter
def measure(&block)
  start = Time.now
  result = block.call
  puts "Took #{Time.now - start}s"
  result
end

# Proc — object wrapper for a block
square = Proc.new { |x| x * x }
puts square.call(5)    # 25
puts square[5]         # 25 — alternative syntax

# Lambda — strict argument checking, local return
double = ->(x) { x * 2 }
puts double.call(5)    # 10
# double.call(1, 2)    # ArgumentError

# Proc vs lambda return behavior
def test_proc
  p = Proc.new { return "from proc" }
  p.call
  "after proc"         # Never reached
end
test_proc               # => "from proc"

def test_lambda
  l = -> { return "from lambda" }
  result = l.call
  "after: #{result}"    # Reached
end
test_lambda             # => "after: from lambda"
```

---

## 类和模块
```ruby
# Class with constructor
class Person
  attr_reader :name, :age
  attr_accessor :email

  def initialize(name, age)
    @name = name
    @age = age
  end

  def greet
    "Hello, I'm #{@name} and I'm #{@age}"
  end

  # Class method
  def self.create(data)
    new(data[:name], data[:age])
  end

  # to_s override
  def to_s
    "#<Person: #{@name}>"
  end
end

# Inheritance
class Employee < Person
  attr_reader :department

  def initialize(name, age, department)
    super(name, age)
    @department = department
  end
end

# Module — mixin for shared behavior
module Printable
  def print_details
    puts inspect
  end
end

module Comparable
  def <=>(other)
    age <=> other.age
  end
end

class User < Person
  include Printable
  include Comparable
end

# Struct — lightweight data class
Point = Struct.new(:x, :y) do
  def distance_to(other)
    Math.sqrt((x - other.x)**2 + (y - other.y)**2)
  end
end
p1 = Point.new(0, 0)
p2 = Point.new(3, 4)
p1.distance_to(p2)  # 5.0

# Data class (Ruby 3.2+) — immutable
Measurement = Data.define(:value, :unit)
m = Measurement.new(value: 100, unit: "mg")
# m.value = 200  # NoMethodError — immutable
```

---

## 枚举和集合
```ruby
# Array
arr = [1, 2, 3, 4, 5]
arr.map { |x| x * 2 }          # [2, 4, 6, 8, 10]
arr.select { |x| x > 3 }       # [4, 5]
arr.reject { |x| x.even? }     # [1, 3, 5]
arr.reduce(0) { |sum, x| sum + x }  # 15
arr.flat_map { |x| [x, x * 10] }    # [1, 10, 2, 20, ...]
arr.each_with_object({}) { |x, h| h[x] = x**2 }  # {1=>1, 2=>4, ...}
arr.group_by(&:even?)          # {false=>[1,3,5], true=>[2,4]}
arr.chunk_while { |a, b| b - a == 1 }.to_a  # [[1,2,3,4,5]]

# Hash
hash = { a: 1, b: 2, c: 3 }
hash.transform_values { |v| v * 10 }    # {a: 10, b: 20, c: 30}
hash.transform_keys(&:to_s)             # {"a"=>1, "b"=>2, "c"=>3}
hash.merge({ d: 4 })                    # {a:1, b:2, c:3, d:4}
hash.slice(:a, :c)                      # {a: 1, c: 3}
hash.except(:b)                         # {a: 1, c: 3}
hash.fetch(:z, 0)                       # 0 (default)

# String
"hello world".split          # ["hello", "world"]
"hello".chars.to_a           # ["h", "e", "l", "l", "o"]
"  spaces  ".strip           # "spaces"
"hello".upcase               # "HELLO"
"Hello #{name}"              # String interpolation
<<~HEREDOC                   # Squiggly heredoc (strips indentation)
  Multi-line
  string content
HEREDOC
```

---

## 元编程
```ruby
# Dynamic method definition
class Calculator
  [:add, :subtract, :multiply, :divide].each do |op|
    define_method(op) do |a, b|
      a.send({ add: :+, subtract: :-, multiply: :*, divide: :/ }[op], b)
    end
  end
end

# method_missing — catch undefined methods
class DynamicRecord
  def initialize(attrs = {})
    @attrs = attrs
  end

  def method_missing(name, *args)
    key = name.to_s.chomp("=").to_sym
    if name.to_s.end_with?("=")
      @attrs[key] = args.first
    elsif @attrs.key?(key)
      @attrs[key]
    else
      super
    end
  end

  def respond_to_missing?(name, include_private = false)
    key = name.to_s.chomp("=").to_sym
    @attrs.key?(key) || name.to_s.end_with?("=") || super
  end
end

# send — call method by name
obj.send(:method_name, arg1, arg2)

# instance_eval / class_eval
obj.instance_eval { @private_var }
MyClass.class_eval { define_method(:dynamic) { "hello" } }

# Refinements — scoped monkey patching (Ruby 2.0+)
module StringExt
  refine String do
    def shout
      upcase + "!!!"
    end
  end
end

using StringExt
"hello".shout  # "HELLO!!!"
```

---

## 错误处理
```ruby
# begin / rescue / else / ensure
begin
  result = risky_operation
rescue SpecificError => e
  logger.error(e.message)
  retry if attempts < 3
rescue AnotherError
  fallback
else
  # Runs only if no exception
  log_success(result)
ensure
  # Always runs — cleanup
  cleanup
end

# Inline rescue
value = parse(input) rescue default_value

# Custom exceptions
class AppError < StandardError; end
class NotFoundError < AppError; end
raise NotFoundError, "User not found: #{id}"
```

---

＃＃ 概括
Ruby 的语法是为开发人员的快乐而设计的——它读起来像英语，并且奖励表达能力。该语言的力量来自于它的对象模型（一切都是对象）、块和闭包、元编程功能以及提供丰富的集合处理 API 的 Enumerable 模块。 Ruby 3.x 添加了模式匹配、RBS 类型签名和用于并发的 Ractor，同时保持了该语言的核心理念：让程序员高效且快乐。