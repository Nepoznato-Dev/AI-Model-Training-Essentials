---
# Metadata
title: "Ruby — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, Rubyish code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [ruby, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "14 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Ruby — 관용적 패턴 및 모범 사례
이 가이드에서는 깔끔한 Rubyish 코드를 작성하기 위한 관용적 패턴과 모범 사례를 다룹니다.
---

## 루비 스타일
```ruby
# ✅ Prefer single quotes unless interpolation needed
name = 'Alice'
greeting = "Hello, #{name}!"

# ✅ Symbol keys in hashes (not string keys)
config = { host: 'localhost', port: 8080 }

# ✅ Symbol#to_proc
users.map(&:name)
# instead of: users.map { |u| u.name }

# ✅ Prefer do/end for multi-line, {} for single-line
users.each do |user|
  puts user.name
end

names = users.map { |u| u.name }

# ✅ Implicit return (last expression)
def full_name
  "#{first_name} #{last_name}"
end
```

---

## 블록 및 반복자
```ruby
# ✅ yield for block acceptance
def with_logging
  puts "Starting..."
  yield
  puts "Done!"
end

# ✅ block_given? for optional blocks
def process(items)
  items.each { |item| block_given? ? yield(item) : item }
end

# ✅ Enumerable methods
users.select(&:active?)
users.reject { |u| u.banned? }
users.find { |u| u.id == target_id }
users.group_by(&:role)
users.sort_by(&:name)
users.min_by(&:age)
users.count { |u| u.admin? }
users.any?(&:active?)
users.all?(&:verified?)
users.none?(&:banned?)
users.sum(&:salary)

# ✅ each_with_object
result = items.each_with_object({}) do |item, hash|
  hash[item.key] = item.value
end
```

---

## 패턴 매칭(Ruby 3+)
```ruby
# ✅ Pattern matching
case user
in { name:, role: "admin" }
  grant_access(user)
in { name:, age: 18.. }
  puts "#{name} is an adult"
in { name: } if name.start_with?("A")
  puts "Name starts with A"
end

# ✅ Hash pattern matching
case response
in { status: 200, body: }
  process(body)
in { status: 404 }
  handle_not_found
end

# ✅ Array pattern
case point
in [x, y]
  puts "Point at (#{x}, #{y})"
in [x, y, z]
  puts "3D point at (#{x}, #{y}, #{z})"
end
```

---

## 오리 타이핑 및 프로토콜
```ruby
# ✅ Duck typing — respond_to?
def process(item)
  item.save if item.respond_to?(:save)
end

# ✅ Module for shared behavior
module Serializable
  def to_json
    JSON.generate(to_h)
  end
end

class User
  include Serializable
end

# ✅ Struct for simple data
Point = Struct.new(:x, :y) do
  def distance_to(other)
    Math.sqrt((x - other.x)**2 + (y - other.y)**2)
  end
end

# ✅ Data class (Ruby 3.2+, immutable)
Measure = Data.define(:amount, :unit)
```

---

## 오류 처리
```ruby
# ✅ Rescue specific exceptions
begin
  result = risky_operation
rescue ArgumentError => e
  logger.warn("Invalid argument: #{e.message}")
rescue StandardError => e
  logger.error("Failed: #{e.message}")
  raise
end

# ✅ Inline rescue for defaults
value = hash.fetch(:key, default_value)
count = items.length rescue 0

# ✅ Custom exceptions
class ValidationError < StandardError
  attr_reader :field
  def initialize(field, message)
    @field = field
    super("#{field}: #{message}")
  end
end
```

---

## 메타프로그래밍
```ruby
# ✅ attr_reader, attr_writer, attr_accessor
class User
  attr_reader :name
  attr_accessor :email
end

# ✅ class methods with self
class User
  def self.find(id)
    # ...
  end
end

# ✅ delegate
class Order
  delegate :name, :email, to: :user, prefix: true
  # user_name, user_email
end

# ✅ define_method for dynamic methods
%w[admin user guest].each do |role|
  define_method("#{role}?") { self.role == role }
end
```

---

## 요약
Ruby 관용어는 개발자의 행복, 구성에 대한 관례, 블록 및 반복자, 덕 타이핑 및 표현 구문을 강조합니다. Ruby 스타일 가이드를 따르고 Linting에는 RuboCop을, 독자적인 형식 지정에는 StandardRB를 사용하세요. Ruby는 가독성을 중요하게 생각합니다. 코드는 영어처럼 읽어야 합니다. 수동 루프보다 열거 가능한 방법을 선호하고, 식별자에 기호를 사용하고, 반복 및 리소스 관리를 위해 블록을 수용합니다.