<!--
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

-->
# Ruby — 構文リファレンス
このドキュメントは、Ruby (3.x) の包括的で構造化された構文リファレンスを提供します。網羅的な構文パターン、ブロックとクロージャー、メタプログラミング、Ruby のイディオムに焦点を当て、メインの Ruby リファレンスを補完します。
---

## 演算子と式
### コアオペレーター
|オペレーター |名前 |例 |メモ |
|----------|------|----------|----------|
| `+``-``*``/``%``**` |算数 | `2 ** 10`| `**`はべき乗 |
| `==``!=``===``<=>` |平等 | `a == b`| `===`は大文字と小文字が等価です。 `<=>`は宇宙船です |
| `eql?`|値の等しい | `a.eql?(b)`|`==`よりも厳密 (タイプをチェック) |
| `equal?`|アイデンティティ | `a.equal?(b)`|同じオブジェクトですか？ |
| `<``>``<=``>=` |比較 | `a >= b`| |
| `&&``\|\|``!`|論理 | `a && b`|短絡;最後に評価された値を返します |
| `and``or``not`|論理 (優先順位が低い) | `a and b`|回避 —`&&`/`\|\|`/`!`を使用してください。
| `&``\|``^``~``<<``>>` |ビットごと | `a & b`| |
| `=~`|`!~`|正規表現一致 | `str =~ /pattern/`|インデックスまたは nil を返します |
| `..`|`...`|範囲 | `1..10`| `..`を含む。  `...`専用 |
| `?.`|安全なナビゲーション | `user&.name`|ユーザーが nil の場合は nil を返します。
| `[]`|`[]=`|要素へのアクセス | `arr[0]`| |
### 真実性
```ruby
# In Ruby, only nil and false are falsy
# Everything else (0, "", [], {}) is truthy
!!0       # true  (unlike most languages!)
!!""      # true
!![]      # true
!!nil     # false
!!false   # false
```

### 演算子の優先順位 (最高から最低)
|優先順位 |オペレーター |
|-----------|----------|
| 1 (最高) | `**`|
| 2 | `!``~``+`(単項) |
| 3 | `*``/``%`|
| 4 | `+`|`-`|
| 5 | `<<``>>` |
| 6 | `&`|
| 7 | `\|`|`^`|
| 8 | `>``>=``<``<=` |
| 9 | `<=>``==``===``!=``eql?``equal?` |
| 10 | `&&`|
| 11 | `\|\|`|
| 12 | `..``...` (範囲) |
| 13 | `? :`(三値) |
| 14 | `=``+=` など (割り当て) |
| 15 (最低) | `not``and``or`|
---

## 制御フロー
### 条件文
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

### ループ
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

## ブロック、Proc、ラムダ
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

## クラスとモジュール
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

## 列挙可能とコレクション
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

## メタプログラミング
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

## エラー処理
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

＃＃ まとめ
Ruby の構文は開発者が満足できるように設計されており、英語のように読みやすく、表現力が高く評価されます。この言語の能力は、そのオブジェクト モデル (すべてがオブジェクトである)、ブロックとクロージャ、メタプログラミング機能、および豊富なコレクション処理 API を提供する Enumerable モジュールから得られます。 Ruby 3.x では、プログラマーの生産性と満足度を高めるという言語の中心的な哲学を維持しながら、パターン マッチング、RBS 型シグネチャ、同時実行性のための Ractor が追加されました。