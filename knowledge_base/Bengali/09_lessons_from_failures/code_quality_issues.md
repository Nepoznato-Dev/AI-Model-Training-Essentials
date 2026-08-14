<!--
---
# Metadata
title: "Code Quality Issues"
description: "Common coding mistakes and anti-patterns"
category: "Lessons from Failures"
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [code, quality, issues, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "18 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# কোড মানের সমস্যা
এই নথিটি খারাপ পরিবর্তনশীল নাম, দুর্বল ডকুমেন্টেশন, স্প্যাগেটি কোড, সার্কুলার নির্ভরতা এবং অন্যান্য রক্ষণাবেক্ষণযোগ্যতা সমস্যা সহ সাধারণ কোড মানের সমস্যাগুলিকে একত্রিত করে।
---

## খারাপ পরিবর্তনশীল নাম
দুর্বল পরিবর্তনশীল নামকরণ কোড পড়া, বোঝা এবং বজায় রাখা কঠিন করে তোলে। ভালো নাম ডকুমেন্টেশন হিসেবে কাজ করে এবং জ্ঞানীয় লোড কমায়।
### একক অক্ষরের নাম (লুপ কাউন্টার ব্যতীত)
**খারাপ উদাহরণ:**```python
def p(d, r, t):
    a = d * ((1 + r / 12) ** (12 * t))
    i = a - d
    return i
```

**সমস্যা:**
- কি পরামিতি প্রতিনিধিত্ব কোন ইঙ্গিত
- ডকুমেন্টেশন ছাড়া বোঝা অসম্ভব
- রক্ষণাবেক্ষণের সময় ত্রুটি-প্রবণ
**উত্তম পদ্ধতি:**```python
def calculate_compound_interest(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    months = 12 * years
    amount = principal * ((1 + monthly_rate) ** months)
    interest = amount - principal
    return interest
```

### অস্পষ্ট বা সাধারণ নাম
**খারাপ উদাহরণ:**```python
data = get_data()
result = process_data(data)
temp = transform(result)
final = finalize(temp)
```

**উত্তম পদ্ধতি:**```python
user_records = fetch_user_records()
validated_users = validate_user_data(user_records)
enriched_users = add_user_preferences(validated_users)
user_profiles = build_user_profiles(enriched_users)
```

### বিভ্রান্তিকর নাম
**খারাপ উদাহরণ:**```python
def get_users():
    # Actually modifies database, doesn't just "get"
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

**উত্তম পদ্ধতি:**```python
def update_user_last_login_and_fetch():
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

### নামকরণের সর্বোত্তম অভ্যাস
1. **উদ্দেশ্য-প্রকাশক নাম ব্যবহার করুন**: নামগুলি কেন কিছু বিদ্যমান তা ব্যাখ্যা করা উচিত
2. **বিভ্রান্তি এড়িয়ে চলুন**: এমন নাম ব্যবহার করবেন না যা আচরণ সম্পর্কে বিভ্রান্ত করে
3. **অর্থপূর্ণ পার্থক্য করুন**: অপ্রয়োজনীয় বা অর্থহীন শব্দ এড়িয়ে চলুন
4. **উচ্চারণযোগ্য নাম ব্যবহার করুন**: আপনাকে এই কোড সম্পর্কে কথা বলতে হবে
5. **অনুসন্ধানযোগ্য নাম ব্যবহার করুন**: একক অক্ষর এবং জাদু সংখ্যা এড়িয়ে চলুন
6. **কোডের মধ্যে নিজেকে ব্যাখ্যা করুন**: ভাল নামকরণের মাধ্যমে মন্তব্যের প্রয়োজনীয়তা হ্রাস করুন
---

## স্প্যাগেটি কোড
স্প্যাগেটি কোড অসংগঠিত, জটিল নিয়ন্ত্রণ প্রবাহ সহ রক্ষণাবেক্ষণ করা কঠিন সোর্স কোডকে বোঝায়।
### অত্যধিক বাসা বাঁধা
**খারাপ উদাহরণ:**```python
def process_order(order):
    if order:
        if order.items:
            if len(order.items) > 0:
                for item in order.items:
                    if item.in_stock:
                        if item.price > 0:
                            if order.customer:
                                if order.customer.active:
                                    if order.customer.verified:
                                        process_item(item)
                                    else:
                                        return "Customer not verified"
                                else:
                                    return "Customer not active"
                            else:
                                return "No customer"
                        else:
                            return "Invalid price"
                    else:
                        return "Item out of stock"
                return "Success"
            else:
                return "No items"
        else:
            return "Empty order"
    else:
        return "Null order"
```

**উত্তম পদ্ধতি:**```python
def process_order(order):
    if not order:
        return "Null order"
    
    if not order.items:
        return "Empty order"
    
    if not order.customer:
        return "No customer"
    
    if not order.customer.active:
        return "Customer not active"
    
    if not order.customer.verified:
        return "Customer not verified"
    
    for item in order.items:
        if not item.in_stock:
            return "Item out of stock"
        
        if item.price <= 0:
            return "Invalid price"
        
        process_item(item)
    
    return "Success"
```

### দীর্ঘ ফাংশন
**খারাপ উদাহরণ:**```python
def handle_request(request):
    # 200 lines of code doing everything:
    # - Parse request
    # - Validate input
    # - Authenticate user
    # - Query database
    # - Process business logic
    # - Format response
    # - Log activity
    # - Send notifications
    # ... all in one function
```

**উত্তম পদ্ধতি:**```python
def handle_request(request):
    parsed = parse_request(request)
    validate_input(parsed)
    user = authenticate_user(parsed)
    data = query_database(user, parsed)
    result = process_business_logic(data)
    response = format_response(result)
    log_activity(user, request, response)
    send_notifications(user, result)
    return response
```

### গোটো-মতো প্যাটার্ন
**খারাপ উদাহরণ:**```python
def complex_workflow():
    step = 1
    while True:
        if step == 1:
            # do something
            step = 2
        elif step == 2:
            # do something else
            if condition:
                step = 5
            else:
                step = 3
        elif step == 3:
            # more logic
            step = 1  # Jump back!
        # ... continues for many steps
```

**উত্তম পদ্ধতি:**```python
def complex_workflow():
    result = step_one()
    if should_proceed(result):
        result = step_two(result)
        if needs_special_handling(result):
            return handle_special_case(result)
        result = step_three(result)
    return finalize(result)
```

---

## সার্কুলার নির্ভরতা
বৃত্তাকার নির্ভরতা ঘটে যখন মডিউলগুলি একে অপরের উপর প্রত্যক্ষ বা পরোক্ষভাবে নির্ভর করে, চক্র তৈরি করে।
### সরাসরি সার্কুলার নির্ভরতা
**খারাপ উদাহরণ:**```python
# module_a.py
from module_b import process_data

def handle_request(data):
    return process_data(data)

# module_b.py
from module_a import handle_request  # CIRCULAR!

def process_data(data):
    # Need to call back to module_a
    return handle_request(transform(data))
```

**কেন এটা খারাপ:**
- রানটাইমে ত্রুটি আমদানি করুন
- স্বাধীনভাবে মডিউল আমদানি করা অসম্ভব
- কোড বিচ্ছিন্নভাবে পরীক্ষা করা যাবে না
**সমাধান: শেয়ার্ড ইন্টারফেস বের করুন**```python
# interfaces.py
from abc import ABC, abstractmethod

class DataHandler(ABC):
    @abstractmethod
    def handle_request(self, data):
        pass

# module_a.py
from interfaces import DataHandler

class RequestHandler(DataHandler):
    def handle_request(self, data):
        from module_b import process_data
        return process_data(data)

# module_b.py
def process_data(data):
    # Process without calling back
    return transform(data)
```

### পরোক্ষ সার্কুলার নির্ভরতা
**খারাপ উদাহরণ:**```
module_a -> module_b -> module_c -> module_a
```

**সমাধান: নির্ভরতা বিপরীত**```python
# Define interfaces/protocols that modules depend on
# Modules implement interfaces rather than depending on concrete implementations
```

---

## দুর্বল ডকুমেন্টেশন
দুর্বল ডকুমেন্টেশন রক্ষণাবেক্ষণের খরচ বাড়ায়, অনবোর্ডিংকে ধীর করে দেয় এবং জ্ঞানের সাইলো তৈরি করে।
### নথিপত্র অনুপস্থিত
**খারাপ উদাহরণ:**```python
def calc(a, b, c):
    x = a * 2 + b
    y = x / c if c != 0 else 1
    return y * 1.15
```

**উত্তম পদ্ধতি:**```python
def calculate_final_price(base_price: float, tax_amount: float, discount_factor: float) -> float:
    """
    Calculate the final price after applying tax and discount.
    
    Args:
        base_price: The original price before adjustments
        tax_amount: Tax amount to add
        discount_factor: Multiplier for discount (e.g., 0.85 for 15% off)
    
    Returns:
        Final price rounded to 2 decimal places
    
    Raises:
        ValueError: If discount_factor is negative or greater than 1
    """
    if not 0 <= discount_factor <= 1:
        raise ValueError("discount_factor must be between 0 and 1")
    
    subtotal = base_price * 2 + tax_amount
    discounted = subtotal / discount_factor if discount_factor != 0 else subtotal
    return round(discounted * 1.15, 2)
```

### পুরানো ডকুমেন্টেশন
**খারাপ উদাহরণ:**```python
def process_items(items):
    """
    Process up to 100 items.
    Returns a list of processed items.
    """
    # Now handles unlimited items with pagination
    # Returns a generator instead of list
    # Added error handling and logging
    ...
```

**সমাধান:** ডকুমেন্টেশন কোডের কাছাকাছি রাখুন এবং কোড পর্যালোচনার সময় এটি আপডেট করুন।
### ওভার-ডকুমেন্টেশন
**খারাপ উদাহরণ:**```python
# Increment i by 1
i += 1

# Check if name equals John
if name == "John":
    # Print greeting
    print("Hello, John!")
```

**সমাধান:** পরিষ্কার কোড নিজের জন্য কথা বলতে দিন; নথি কেন, কি নয়।
---

## কোড গন্ধ
কোড গন্ধ হল সফ্টওয়্যার ডিজাইনে গভীর সমস্যাগুলির পৃষ্ঠ-স্তরের ইঙ্গিত।
### সদৃশ কোড
**খারাপ উদাহরণ:**```python
# File: user_service.py
def send_welcome_email(user):
    message = f"Welcome {user.name}!"
    smtp = SMTPServer("smtp.example.com")
    smtp.connect()
    smtp.send(user.email, message)
    smtp.disconnect()
    log_email_sent(user.id)

# File: order_service.py
def send_order_confirmation(user):
    message = f"Order confirmed, {user.name}!"
    smtp = SMTPServer("smtp.example.com")
    smtp.connect()
    smtp.send(user.email, message)
    smtp.disconnect()
    log_email_sent(user.id)
```

**উত্তম পদ্ধতি:**```python
# File: email_service.py
def send_email(user, message):
    smtp = SMTPServer("smtp.example.com")
    smtp.connect()
    smtp.send(user.email, message)
    smtp.disconnect()
    log_email_sent(user.id)

# File: user_service.py
def send_welcome_email(user):
    send_email(user, f"Welcome {user.name}!")

# File: order_service.py
def send_order_confirmation(user):
    send_email(user, f"Order confirmed, {user.name}!")
```

### দীর্ঘ পরামিতি তালিকা
**খারাপ উদাহরণ:**```python
def create_user(username, password, email, first_name, last_name, 
                phone, address, city, state, zip_code, country,
                birth_date, gender, occupation, company):
    # 15 parameters!
```

**উত্তম পদ্ধতি:**```python
@dataclass
class UserProfile:
    username: str
    password: str
    email: str
    first_name: str
    last_name: str
    phone: Optional[str] = None
    address: Optional[Address] = None
    birth_date: Optional[date] = None
    gender: Optional[str] = None
    occupation: Optional[str] = None
    company: Optional[str] = None

def create_user(profile: UserProfile):
    # Clean and extensible
```

---

## সম্পর্কিত বিষয়
- **নিরাপত্তা দুর্বলতা**: নিরাপত্তা-সম্পর্কিত কোড সমস্যাগুলির জন্য`02_security_vulnerabilities.md`দেখুন
- **গিট ইতিহাস**: কমিট বার্তা এবং সংস্করণ নিয়ন্ত্রণের সর্বোত্তম অনুশীলনের জন্য`06_git_documentation.md`দেখুন
- **API ডিজাইন**: ইন্টারফেস ডিজাইনের নীতির জন্য`07_api_system_design.md`দেখুন