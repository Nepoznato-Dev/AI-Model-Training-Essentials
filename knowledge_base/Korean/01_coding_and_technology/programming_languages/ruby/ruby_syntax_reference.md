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
# Ruby — 구문 참조
이 문서는 Ruby(3.x)에 대한 포괄적이고 구조화된 구문 참조를 제공합니다. 이는 철저한 구문 패턴, 블록 및 클로저, 메타프로그래밍, Ruby 관용어에 중점을 두어 기본 Ruby 참조를 보완합니다.
---

## 연산자 및 표현식
### 핵심 운영자
| 운영자 | 이름 | 예 | 메모 |
|------------|------|---------|-------|
| `+``-``*``/``%``**` | 산술 | `2 ** 10`|  `**`는 지수화입니다 |
| `==``!=``===``<=>` | 평등 | `a == b`|  `===`는 대소문자 동일입니다.  `<=>`는 우주선입니다 |
| `eql?`| 가치평등 | `a.eql?(b)`| `==`보다 엄격함(체크 유형) |
| `equal?`| 정체성 | `a.equal?(b)`| 같은 개체? |
| `<``>``<=``>=` | 비교 | `a >= b`| |
| `&&``\|\|``!`| 논리적 | `a && b`| 단락; 마지막으로 평가된 값을 반환합니다 |
| `and``or``not`| 논리적(낮은 우선순위) | `a and b`| 피하십시오 -`&&`/`\|\|`/`!`|를 사용하십시오.
| `&``\|``^``~``<<``>>` | 비트별 | `a & b`| |
| `=~``!~` | 정규식 일치 | `str =~ /pattern/`| 인덱스 또는 nil을 반환합니다. |
| `..``...` | 범위 | `1..10`| `..`포함; `...`독점 |
| `?.`| 안전한 항해 | `user&.name`| 사용자가 nil인 경우 nil을 반환합니다. |
| `[]``[]=` | 요소 액세스 | `arr[0]`| |
### 진실성
```ruby
# In Ruby, only nil and false are falsy
# Everything else (0, "", [], {}) is truthy
!!0       # true  (unlike most languages!)
!!""      # true
!![]      # true
!!nil     # false
!!false   # false
```

### 연산자 우선 순위(가장 높은 것에서 가장 낮은 것까지)
| 우선순위 | 운영자 |
|------------|------------|
| 1(가장 높음) | `**`|
| 2 | `!``~` `+`(단항) |
| 3 | `*``/``%`|
| 4 | `+``-` |
| 5 | `<<``>>` |
| 6 | `&`|
| 7 | `\|``^` |
| 8 | `>``>=``<``<=` |
| 9 | `<=>``==``===``!=``eql?``equal?` |
| 10 | `&&`|
| 11 | `\|\|`|
| 12 | `..``...`(범위) |
| 13 |  `? :`(3항) |
| 14 | `=``+=` 등(할당) |
| 15(최저) | `not``and``or`|
---

## 제어 흐름
### 조건부
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

### 루프
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

## 블록, 프로세스 및 람다
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

## 클래스 및 모듈
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

## 열거 가능 및 컬렉션
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

## 메타프로그래밍
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

## 오류 처리
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

## 요약
Ruby의 구문은 개발자의 행복을 위해 설계되었습니다. 즉, 영어처럼 읽혀지고 표현력이 향상됩니다. 언어의 강력한 기능은 객체 모델(모든 것이 객체임), 블록 및 클로저, 메타프로그래밍 기능, 풍부한 컬렉션 처리 API를 제공하는 Enumerable 모듈에서 나옵니다. Ruby 3.x에는 패턴 일치, RBS 유형 시그니처, 동시성을 위한 Ractor가 추가되었으며 동시에 언어의 핵심 철학인 프로그래머를 생산적이고 행복하게 만듭니다.