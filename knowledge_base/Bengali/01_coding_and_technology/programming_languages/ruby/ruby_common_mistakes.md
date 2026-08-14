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

# রুবি — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্নস
এই নথিটি রুবিতে সবচেয়ে সাধারণ ভুল, ফাঁদ এবং অ্যান্টি-প্যাটার্নের ক্যাটালগ করে। প্রতিটি এন্ট্রি ভুল পদ্ধতি দেখায়, ব্যাখ্যা করে কেন এটি ব্যর্থ হয় এবং সঠিক সমাধান প্রদান করে।
---

## 1. পুনরাবৃত্তির সময় একটি সংগ্রহ পরিবর্তন করা
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

## 2.`nil`বনাম`false`সত্যতা
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

## 3. স্ট্রিং ইন্টারপোলেশন বনাম কনক্যাটেনেশন
```ruby
# ❌ WRONG — string concatenation (less readable)
greeting = "Hello, " + name + "! You are " + age.to_s + " years old."

# ✅ CORRECT — string interpolation
greeting = "Hello, #{name}! You are #{age} years old."
```

---

## 4. শব্দগতভাবে ব্লক/গণনাকারী ব্যবহার না করা
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

## 5. বৈশ্বিক পরিবর্তনশীল অপব্যবহার
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

## 6. বানর প্যাচিং কোর ক্লাস
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

## 7. ব্লকে`return`বোঝা যাচ্ছে না
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

## 8. অ্যান্টি-প্যাটার্ন: ফ্যাট মডেল
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

## 9. প্রতীক বনাম স্ট্রিং বিভ্রান্তি
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

## 10. ফ্রিজিং স্ট্রিং লিটারেল নয়
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

## সারাংশ
রুবির অভিব্যক্তি অ্যান্টি-প্যাটার্নের দিকে নিয়ে যেতে পারে: পুনরাবৃত্তির সময় সংগ্রহ পরিবর্তন করা, মাঙ্কি প্যাচিং কোর ক্লাস, গ্লোবাল ভেরিয়েবল এবং ফ্যাট মডেল। রুবি উপায় হল: গণনাকারী ব্যবহার করুন (`each`,`map`,`reject`), প্রতীক এবং কীওয়ার্ড আর্গুমেন্ট পছন্দ করুন, স্ট্রিং লিটারেল ফ্রিজ করুন, মডেল থেকে পরিষেবা বস্তু বের করুন এবং বানর প্যাচের পরিবর্তে পরিমার্জন ব্যবহার করুন। রুবি ডেভেলপারদের পুরস্কৃত করে যারা ব্লক, হাঁস টাইপিং এবং সর্বনিম্ন অবাক করার নীতি গ্রহণ করে।