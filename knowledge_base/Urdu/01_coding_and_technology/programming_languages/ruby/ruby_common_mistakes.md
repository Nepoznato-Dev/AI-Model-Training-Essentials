---
# Metadata
title: "Ruby — Common Mistakes & Anti-Patterns"
description: "Comprehensive guide to common pitfalls, traps, and anti-patterns in Ruby that catch even experienced developers, with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Initial common mistakes document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [ruby, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "20 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# روبی - عام غلطیاں اور اینٹی پیٹرن
یہ دستاویز روبی میں سب سے عام غلطیوں، ٹریپس، اور مخالف پیٹرن کی فہرست بناتی ہے۔ ہر اندراج غلط نقطہ نظر کو ظاہر کرتا ہے، یہ بتاتا ہے کہ یہ کیوں ناکام ہوتا ہے، اور صحیح حل فراہم کرتا ہے۔
---

## 1. تکرار کے دوران مجموعہ میں ترمیم کرنا
```ruby
# ❌ WRONG — skipping elements
numbers = [1, 2, 3, 4, 5]
numbers.each do |n|
  numbers.delete(n) if n.even?
end
# numbers = [1, 3, 5] — but 4 was skipped!

# ✅ CORRECT — use reject/select to create new array
numbers = numbers.reject(&:even?)
# => [1, 3, 5]
```

---

## 2.`nil`بمقابلہ`false`سچائی
```ruby
# ❌ WRONG — assuming nil is falsy like 0 in some languages
if 0
  puts "zero is truthy"  # this runs! Only nil and false are falsy
end

# ✅ CORRECT — explicit nil check
if value.nil?
  puts "value is nil"
end

# ✅ CORRECT — safe navigation
user&.address&.city  # returns nil if any part is nil
```

---

## 3. سٹرنگ انٹرپولیشن بمقابلہ کنکٹنیشن
```ruby
# ❌ WRONG — string concatenation (less readable)
greeting = "Hello, " + name + "! You are " + age.to_s + " years old."

# ✅ CORRECT — string interpolation
greeting = "Hello, #{name}! You are #{age} years old."
```

---

## 4. بلاکس/ شمار کنندگان کو محاوراتی طور پر استعمال نہ کرنا
```ruby
# ❌ WRONG — C-style loop
i = 0
while i < items.length
  puts items[i]
  i += 1
end

# ❌ WRONG — index-based iteration
(0...items.length).each do |i|
  puts items[i]
end

# ✅ CORRECT — idiomatic Ruby
items.each { |item| puts item }
items.each_with_index { |item, i| puts "#{i}: #{item}" }
```

---

## 5. عالمی متغیر زیادتی
```ruby
# ❌ WRONG — global variables create hidden coupling
$count = 0
def increment
  $count += 1
end

# ✅ CORRECT — use instance/class variables or dependency injection
class Counter
  attr_reader :count
  def initialize; @count = 0; end
  def increment; @count += 1; end
end
```

---

## 6. بندر پیچنگ کور کلاسز
```ruby
# ❌ WRONG — modifying built-in classes
class String
  def shout
    upcase + "!!!"
  end
end
# Can break other gems, hard to debug

# ✅ CORRECT — use refinements (Ruby 2.0+)
module StringExtensions
  refine String do
    def shout
      upcase + "!!!"
    end
  end
end

using StringExtensions
"hello".shout  # "HELLO!!!"
```

---

## 7. بلاکس میں`return`کو نہیں سمجھنا
```ruby
# ❌ WRONG — return exits the enclosing method, not just the block
def process(items)
  items.each do |item|
    return if item.nil?  # exits process(), not just the block!
  end
  "completed"
end

# ✅ CORRECT — use next to skip to next iteration
def process(items)
  items.each do |item|
    next if item.nil?  # skips to next item
    puts item
  end
  "completed"
end
```

---

## 8. اینٹی پیٹرن: موٹے ماڈل
```ruby
# ❌ WRONG — model doing too much
class User < ApplicationRecord
  def send_welcome_email; end
  def generate_invoice; end
  def resize_avatar; end
  def calculate_revenue; end
end

# ✅ CORRECT — service objects
class UserRegistration
  def initialize(user); @user = user; end
  def call
    @user.save
    WelcomeMailer.send(@user)
    InvoiceGenerator.create(@user)
  end
end
```

---

## 9. علامت بمقابلہ سٹرنگ کنفیوژن
```ruby
# ❌ WRONG — using strings as hash keys (pre-Ruby 1.9 style)
options = { "color" => "red", "size" => "large" }
options["color"]  # works but verbose

# ✅ CORRECT — use symbols (or keyword arguments)
options = { color: "red", size: "large" }
options[:color]

# ✅ CORRECT — keyword arguments (Ruby 2.0+)
def configure(color:, size: "medium")
  { color: color, size: size }
end
```

---

## 10. اسٹرنگ لٹریلز کو منجمد نہیں کرنا
```ruby
# ❌ WRONG — mutable strings by default
def format_name(name)
  name << " Jr."  # mutates the original string!
end

original = "John"
format_name(original)
original  # "John Jr." — surprise mutation!

# ✅ CORRECT — freeze or duplicate
# magic comment: # frozen_string_literal: true
def format_name(name)
  name + " Jr."  # creates new string
end
```

---

## خلاصہ
روبی کی اظہار خیال مخالف پیٹرن کا باعث بن سکتا ہے: تکرار کے دوران مجموعوں میں ترمیم کرنا، بندر کی پیچیدگی کور کلاسز، عالمی متغیرات، اور چربی کے ماڈل۔ روبی طریقہ یہ ہے: شمار کنندگان (`each`,`map`,`reject`) استعمال کریں، علامتوں اور مطلوبہ الفاظ کے دلائل کو ترجیح دیں، سٹرنگ لٹریلز کو منجمد کریں، ماڈلز سے سروس آبجیکٹ نکالیں، اور بندر پیچ کی بجائے اصلاح کا استعمال کریں۔ روبی ایسے ڈویلپرز کو انعام دیتا ہے جو بلاکس، بتھ ٹائپنگ، اور کم از کم حیرت کے اصول کو اپناتے ہیں۔