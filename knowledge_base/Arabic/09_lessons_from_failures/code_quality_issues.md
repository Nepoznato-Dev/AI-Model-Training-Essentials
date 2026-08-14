---
# Metadata
title: "Code Quality Issues"
description: "Common coding mistakes and anti-patterns"
category: "Lessons from Failures"
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
    date: "2026-08-05"
    author: "AI Model Training Team"
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

# مشكلات جودة الكود
يقوم هذا المستند بدمج مشاكل جودة التعليمات البرمجية الشائعة بما في ذلك أسماء المتغيرات السيئة، والوثائق الرديئة، والتعليمات البرمجية السباغيتي، والتبعيات الدائرية، ومشكلات الصيانة الأخرى.
---

## أسماء المتغيرات سيئة
إن تسمية المتغيرات السيئة تجعل من الصعب قراءة التعليمات البرمجية وفهمها وصيانتها. تعمل الأسماء الجيدة بمثابة توثيق وتقلل من الحمل المعرفي.
### أسماء الحروف المفردة (باستثناء عدادات الحلقات)
**مثال سيء:**```python
def p(d, r, t):
    a = d * ((1 + r / 12) ** (12 * t))
    i = a - d
    return i
```

**المشاكل:**
- لا توجد إشارة إلى ما تمثله المعلمات
- من المستحيل أن نفهم دون توثيق
- عرضة للخطأ أثناء الصيانة
** نهج أفضل: **```python
def calculate_compound_interest(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    months = 12 * years
    amount = principal * ((1 + monthly_rate) ** months)
    interest = amount - principal
    return interest
```

### أسماء غامضة أو عامة
**مثال سيء:**```python
data = get_data()
result = process_data(data)
temp = transform(result)
final = finalize(temp)
```

** نهج أفضل: **```python
user_records = fetch_user_records()
validated_users = validate_user_data(user_records)
enriched_users = add_user_preferences(validated_users)
user_profiles = build_user_profiles(enriched_users)
```

### الأسماء المضللة
**مثال سيء:**```python
def get_users():
    # Actually modifies database, doesn't just "get"
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

** نهج أفضل: **```python
def update_user_last_login_and_fetch():
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

### أفضل ممارسات التسمية
1. **استخدم الأسماء التي تكشف النية**: يجب أن توضح الأسماء سبب وجود شيء ما
2. **تجنب المعلومات المضللة**: لا تستخدم أسماء مضللة بشأن السلوك
3. **ميز بين الكلمات ذات المعنى**: تجنب الكلمات الزائدة أو التي لا معنى لها
4. **استخدم أسماء قابلة للنطق**: ستحتاج إلى التحدث عن هذا الرمز
5. **استخدم أسماء قابلة للبحث**: تجنب الحروف المفردة والأرقام السحرية
6. **اشرح نفسك في الكود**: قلل الحاجة إلى التعليقات من خلال التسمية الجيدة
---

## كود السباغيتي
يشير رمز السباغيتي إلى كود مصدر غير منظم ويصعب الحفاظ عليه مع تدفق تحكم متشابك.
### التداخل المفرط
**مثال سيء:**```python
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

** نهج أفضل: **```python
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

### وظائف طويلة
**مثال سيء:**```python
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

** نهج أفضل: **```python
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

### أنماط تشبه Goto
**مثال سيء:**```python
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

** نهج أفضل: **```python
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

## التبعيات الدائرية
تحدث التبعيات الدائرية عندما تعتمد الوحدات على بعضها البعض بشكل مباشر أو غير مباشر، مما يؤدي إلى إنشاء دورات.
### التبعيات الدائرية المباشرة
**مثال سيء:**```python
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

**لماذا هو سيء:**
- أخطاء الاستيراد في وقت التشغيل
- من المستحيل استيراد أي وحدة بشكل مستقل
- لا يمكن اختبار الكود بشكل منفصل
** الحل: استخراج الواجهة المشتركة **```python
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

### التبعيات الدائرية غير المباشرة
**مثال سيء:**```
module_a -> module_b -> module_c -> module_a
```

**الحل: عكس التبعية**```python
# Define interfaces/protocols that modules depend on
# Modules implement interfaces rather than depending on concrete implementations
```

---

## توثيق ضعيف
يؤدي التوثيق السيئ إلى زيادة تكاليف الصيانة، وإبطاء عملية الإعداد، وإنشاء صوامع المعرفة.
### الوثائق المفقودة
**مثال سيء:**```python
def calc(a, b, c):
    x = a * 2 + b
    y = x / c if c != 0 else 1
    return y * 1.15
```

** نهج أفضل: **```python
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

### الوثائق القديمة
**مثال سيء:**```python
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

**الحل:** احتفظ بالوثائق قريبة من التعليمات البرمجية وقم بتحديثها أثناء مراجعة التعليمات البرمجية.
### الإفراط في التوثيق
**مثال سيء:**```python
# Increment i by 1
i += 1

# Check if name equals John
if name == "John":
    # Print greeting
    print("Hello, John!")
```

**الحل:** دع الكود الواضح يتحدث عن نفسه؛ وثيقة لماذا، وليس ماذا.
---

## كود الروائح
تعد روائح التعليمات البرمجية بمثابة مؤشرات على المستوى السطحي لمشاكل أعمق في تصميم البرامج.
### رمز مكرر
**مثال سيء:**```python
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

** نهج أفضل: **```python
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

### قوائم المعلمات الطويلة
**مثال سيء:**```python
def create_user(username, password, email, first_name, last_name, 
                phone, address, city, state, zip_code, country,
                birth_date, gender, occupation, company):
    # 15 parameters!
```

** نهج أفضل: **```python
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

## موضوعات ذات صلة
- **الثغرات الأمنية**: راجع`02_security_vulnerabilities.md`للتعرف على مشكلات التعليمات البرمجية المتعلقة بالأمان
- **سجل Git**: راجع`06_git_documentation.md`للتعرف على أفضل الممارسات الخاصة برسالة الالتزام والتحكم في الإصدار
- **تصميم واجهة برمجة التطبيقات**: راجع`07_api_system_design.md`للتعرف على مبادئ تصميم الواجهة