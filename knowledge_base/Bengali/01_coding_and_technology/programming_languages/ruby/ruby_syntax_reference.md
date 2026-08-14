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
# রুবি — সিনট্যাক্স রেফারেন্স
এই নথিটি রুবি (3.x) এর জন্য একটি ব্যাপক, কাঠামোগত সিনট্যাক্স রেফারেন্স প্রদান করে। এটি সম্পূর্ণ সিনট্যাক্স প্যাটার্ন, ব্লক এবং ক্লোজার, মেটাপ্রোগ্রামিং এবং রুবি ইডিয়মগুলিতে ফোকাস করে মূল রুবি রেফারেন্সের পরিপূরক।
---

## অপারেটর এবং এক্সপ্রেশন
### মূল অপারেটর
| অপারেটর | নাম | উদাহরণ | নোট |
|----------|------|---------|-------|
| `+``-``*``/``%``**` | পাটিগণিত | `2 ** 10`| `**`হল সূচক |
| `==``!=``===``<=>` | সমতা | `a == b`| `===`হল কেস সমতা; `<=>`হল মহাকাশযান |
| `eql?`| মূল্য সমতা | `a.eql?(b)`|`==`(চেক টাইপ) এর চেয়ে কঠোর |
| `equal?`| পরিচয় | `a.equal?(b)`| একই বস্তু? |
| `<``>``<=``>=` | তুলনা | `a >= b`| |
| `&&``\|\|``!`| যৌক্তিক | `a && b`| শর্ট সার্কিট; শেষ মূল্যায়ন করা মান ফেরত দেয় |
| `and``or``not`| যৌক্তিক (কম অগ্রাধিকার) | `a and b`| এড়িয়ে চলুন —`&&`/`\|\|`/`!`ব্যবহার করুন |
| `&``\|``^``~``<<``>>` | বিটওয়াইজ | `a & b`| |
| `=~``!~` | Regex ম্যাচ | `str =~ /pattern/`| সূচক বা শূন্য ফেরত দেয় |
| `..``...` | পরিসীমা | `1..10`| `..`অন্তর্ভুক্ত; `...`এক্সক্লুসিভ |
| `?.`| নিরাপদ নেভিগেশন | `user&.name`| যদি ব্যবহারকারী শূন্য হয় |
| `[]``[]=` | উপাদান অ্যাক্সেস | `arr[0]`| |
### সত্যতা
```ruby
# In Ruby, only nil and false are falsy
# Everything else (0, "", [], {}) is truthy
!!0       # true  (unlike most languages!)
!!""      # true
!![]      # true
!!nil     # false
!!false   # false
```

### অপারেটর অগ্রাধিকার (সর্বোচ্চ থেকে সর্বনিম্ন)
| অগ্রাধিকার | অপারেটর |
|------------|------------|
| 1 (সর্বোচ্চ) | `**`|
| 2 | `!``~``+`(ইউনারি) |
| 3 | `*``/``%`|
| 4 | `+``-` |
| 5 | `<<``>>` |
| 6 | `&`|
| 7 | `\|``^` |
| 8 | `>``>=``<``<=` |
| 9 | `<=>``==``===``!=``eql?``equal?` |
| 10 | `&&`|
| 11 | `\|\|`|
| 12 | `..``...` (পরিসীমা) |
| 13 | `? :`(টার্নারি) |
| 14 | `=``+=` ইত্যাদি (অ্যাসাইনমেন্ট) |
| 15 (সর্বনিম্ন) | `not``and``or`|
---

## নিয়ন্ত্রণ প্রবাহ
### শর্তাবলী
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

### লুপ
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

## ব্লক, প্রক্স এবং ল্যাম্বডাস
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

## ক্লাস এবং মডিউল
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

## গণনাযোগ্য এবং সংগ্রহ
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

## মেটাপ্রোগ্রামিং
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

## ত্রুটি হ্যান্ডলিং
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

## সারাংশ
রুবির সিনট্যাক্সটি বিকাশকারীর সুখের জন্য ডিজাইন করা হয়েছে — এটি ইংরেজির মতো পড়ে এবং অভিব্যক্তিকে পুরস্কৃত করে৷ ভাষার শক্তি আসে এর অবজেক্ট মডেল (সবকিছুই একটি অবজেক্ট), ব্লক এবং ক্লোজার, মেটাপ্রোগ্রামিং ক্ষমতা এবং গণনাযোগ্য মডিউল যা একটি সমৃদ্ধ সংগ্রহ প্রক্রিয়াকরণ API প্রদান করে। রুবি 3.x ভাষার মূল দর্শন বজায় রেখে প্যাটার্ন ম্যাচিং, আরবিএস টাইপ স্বাক্ষর এবং র্যাক্টর যোগ করেছে: প্রোগ্রামারদের উত্পাদনশীল এবং সুখী করুন।