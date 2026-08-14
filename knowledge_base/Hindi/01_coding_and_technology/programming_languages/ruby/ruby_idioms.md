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
# रूबी - मुहावरेदार पैटर्न और सर्वोत्तम अभ्यास
यह मार्गदर्शिका स्वच्छ, रूबीश कोड लिखने के लिए मुहावरेदार पैटर्न और सर्वोत्तम प्रथाओं को शामिल करती है।
---

## रूबी शैली
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

## ब्लॉक और इटरेटर
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

## पैटर्न मिलान (रूबी 3+)
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

## बत्तख टाइपिंग और प्रोटोकॉल
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

## त्रुटि प्रबंधन
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

## मेटाप्रोग्रामिंग
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

## सारांश
रूबी मुहावरे जोर देते हैं: डेवलपर खुशी, कॉन्फ़िगरेशन पर कन्वेंशन, ब्लॉक और इटरेटर, डक टाइपिंग, और अभिव्यंजक वाक्यविन्यास। रूबी स्टाइल गाइड का पालन करें, लिंटिंग के लिए रूबोकॉप का उपयोग करें, और रायबद्ध प्रारूपण के लिए स्टैंडर्डआरबी का उपयोग करें। रूबी पठनीयता को महत्व देती है - कोड को अंग्रेजी की तरह पढ़ना चाहिए। मैन्युअल लूप की तुलना में गणना योग्य तरीकों को प्राथमिकता दें, पहचानकर्ताओं के लिए प्रतीकों का उपयोग करें, और पुनरावृत्ति और संसाधन प्रबंधन के लिए ब्लॉक को अपनाएं।