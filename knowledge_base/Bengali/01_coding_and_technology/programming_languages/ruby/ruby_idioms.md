<!--
---
# Metadata
title: "Ruby — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, Rubyish code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# রুবি — ইডিওম্যাটিক প্যাটার্নস এবং সেরা অভ্যাস
এই নির্দেশিকাটি পরিচ্ছন্ন, রুবিশ কোড লেখার জন্য বাহাদুরী নিদর্শন এবং সর্বোত্তম অনুশীলনগুলি কভার করে।
---

## রুবি স্টাইল
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

## ব্লক এবং পুনরাবৃত্তিকারী
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

## প্যাটার্ন ম্যাচিং (রুবি 3+)
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

## হাঁস টাইপিং এবং প্রোটোকল
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

## ত্রুটি হ্যান্ডলিং
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

## মেটাপ্রোগ্রামিং
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

## সারাংশ
রুবি ইডিয়মগুলি জোর দেয়: বিকাশকারীর সুখ, কনফিগারেশনের উপর কনভেনশন, ব্লক এবং পুনরাবৃত্তিকারী, হাঁস টাইপিং এবং অভিব্যক্তিপূর্ণ বাক্য গঠন। রুবি স্টাইল গাইড অনুসরণ করুন, লিন্টিংয়ের জন্য রুবোকপ এবং মতামতযুক্ত বিন্যাসের জন্য স্ট্যান্ডার্ডআরবি ব্যবহার করুন। রুবি পঠনযোগ্যতার মান দেয় — কোড ইংরেজির মতো পড়া উচিত। ম্যানুয়াল লুপের চেয়ে গণনাযোগ্য পদ্ধতি পছন্দ করুন, শনাক্তকারীর জন্য প্রতীক ব্যবহার করুন, এবং পুনরাবৃত্তি এবং সংস্থান পরিচালনার জন্য ব্লকগুলি আলিঙ্গন করুন।