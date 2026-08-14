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
# مشکلات کیفیت کد
این سند مشکلات رایج کیفیت کد از جمله نام‌های بد متغیرها، اسناد ضعیف، کد اسپاگتی، وابستگی‌های دایره‌ای و سایر مسائل مربوط به قابلیت نگهداری را ادغام می‌کند.
---

## نام متغیر بد
نام‌گذاری ضعیف متغیرها، خواندن، درک و نگهداری کد را سخت‌تر می‌کند. نام های خوب به عنوان سند عمل می کنند و بار شناختی را کاهش می دهند.
### نام های تک حرفی (به جز شمارنده های حلقه)
**مثال بد:**```python
def p(d, r, t):
    a = d * ((1 + r / 12) ** (12 * t))
    i = a - d
    return i
```

**مشکلات:**
- هیچ نشانی از چه پارامترهایی نشان نمی دهد
- درک بدون مستندات غیر ممکن است
- مستعد خطا در حین تعمیر و نگهداری
**رویکرد بهتر:**```python
def calculate_compound_interest(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    months = 12 * years
    amount = principal * ((1 + monthly_rate) ** months)
    interest = amount - principal
    return interest
```

### نام های مبهم یا عمومی
**مثال بد:**```python
data = get_data()
result = process_data(data)
temp = transform(result)
final = finalize(temp)
```

**رویکرد بهتر:**```python
user_records = fetch_user_records()
validated_users = validate_user_data(user_records)
enriched_users = add_user_preferences(validated_users)
user_profiles = build_user_profiles(enriched_users)
```

### نام های گمراه کننده
**مثال بد:**```python
def get_users():
    # Actually modifies database, doesn't just "get"
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

**رویکرد بهتر:**```python
def update_user_last_login_and_fetch():
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

### نام‌گذاری بهترین روش‌ها
1. **از نام های آشکار کننده قصد استفاده کنید**: نام ها باید دلیل وجود چیزی را توضیح دهند
2. **اجتناب از اطلاعات نادرست**: از نام هایی که رفتار را گمراه می کند استفاده نکنید
3. **تمایزهای معنادار **: از کلمات زائد یا بی معنی اجتناب کنید
4. **از اسامی قابل تلفظ** استفاده کنید: باید در مورد این کد صحبت کنید
5. **از نام های قابل جستجو استفاده کنید**: از تک حروف و اعداد جادویی خودداری کنید
6. **خود را با کد توضیح دهید**: از طریق نامگذاری خوب نیاز به نظرات را کاهش دهید
---

## کد اسپاگتی
کد اسپاگتی به کد منبع غیرساختارمند و دشوار برای نگهداری با جریان کنترل درهم اشاره دارد.
### تودرتو بیش از حد
**مثال بد:**```python
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

**رویکرد بهتر:**```python
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

### توابع طولانی
**مثال بد:**```python
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

**رویکرد بهتر:**```python
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

### الگوهای شبیه به Goto
**مثال بد:**```python
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

**رویکرد بهتر:**```python
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

## وابستگی های دایره ای
وابستگی های دایره ای زمانی رخ می دهند که ماژول ها به طور مستقیم یا غیرمستقیم به یکدیگر وابسته باشند و چرخه هایی را ایجاد کنند.
### وابستگی های دایره ای مستقیم
**مثال بد:**```python
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

**چرا بد است:**
- خطاهای وارد کردن در زمان اجرا
- وارد کردن هر یک از ماژول ها به طور مستقل غیرممکن است
- کد را نمی توان به صورت مجزا آزمایش کرد
**راه حل: استخراج رابط مشترک**```python
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

### وابستگی های دایره ای غیر مستقیم
**مثال بد:**```
module_a -> module_b -> module_c -> module_a
```

**راه حل: وارونگی وابستگی**```python
# Define interfaces/protocols that modules depend on
# Modules implement interfaces rather than depending on concrete implementations
```

---

## مستندات ضعیف
مستندات ضعیف هزینه های نگهداری را افزایش می دهد، سوار شدن را کند می کند و سیلوهای دانش را ایجاد می کند.
### اسناد موجود نیست
**مثال بد:**```python
def calc(a, b, c):
    x = a * 2 + b
    y = x / c if c != 0 else 1
    return y * 1.15
```

**رویکرد بهتر:**```python
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

### اسناد قدیمی
**مثال بد:**```python
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

**راه حل:** اسناد را نزدیک به کد نگه دارید و در طول بررسی کد آن را به روز کنید.
### بیش از حد اسناد
**مثال بد:**```python
# Increment i by 1
i += 1

# Check if name equals John
if name == "John":
    # Print greeting
    print("Hello, John!")
```

**راه حل:** بگذارید کد واضح خودش صحبت کند. مستند چرا، نه چی.
---

## کد بو می دهد
بوهای کد نشانه های سطحی مشکلات عمیق تر در طراحی نرم افزار هستند.
### کد تکراری
**مثال بد:**```python
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

**رویکرد بهتر:**```python
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

### لیست های طولانی پارامتر
**مثال بد:**```python
def create_user(username, password, email, first_name, last_name, 
                phone, address, city, state, zip_code, country,
                birth_date, gender, occupation, company):
    # 15 parameters!
```

**رویکرد بهتر:**```python
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

## موضوعات مرتبط
- **آسیب پذیری های امنیتی**: برای مسائل مربوط به کد مربوط به امنیت به`02_security_vulnerabilities.md`مراجعه کنید
- **تاریخچه Git**: برای اطلاع از بهترین شیوه های commit پیام و کنترل نسخه به`06_git_documentation.md`مراجعه کنید
- **طراحی API**: برای اصول طراحی رابط به`07_api_system_design.md`مراجعه کنید