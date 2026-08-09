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

# 代码质量问题
本文档整合了常见的代码质量问题，包括错误的变量名称、糟糕的文档、意大利面条式代码、循环依赖和其他可维护性问题。
---

## 错误的变量名
糟糕的变量命名会使代码更难阅读、理解和维护。好的名字可以作为文档并减少认知负担。
### 单字母名称（循环计数器除外）
**错误的例子：**```python
def p(d, r, t):
    a = d * ((1 + r / 12) ** (12 * t))
    i = a - d
    return i
```

**问题：**
- 没有说明参数代表什么
- 没有文档就无法理解
- 维护期间容易出错
**更好的方法：**```python
def calculate_compound_interest(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    months = 12 * years
    amount = principal * ((1 + monthly_rate) ** months)
    interest = amount - principal
    return interest
```

### 模糊或通用名称
**错误的例子：**```python
data = get_data()
result = process_data(data)
temp = transform(result)
final = finalize(temp)
```

**更好的方法：**```python
user_records = fetch_user_records()
validated_users = validate_user_data(user_records)
enriched_users = add_user_preferences(validated_users)
user_profiles = build_user_profiles(enriched_users)
```

### 误导性名称
**错误的例子：**```python
def get_users():
    # Actually modifies database, doesn't just "get"
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

**更好的方法：**```python
def update_user_last_login_and_fetch():
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

### 命名最佳实践
1. **使用揭示意图的名称**：名称应该解释某物存在的原因
2. **避免虚假信息**：不要使用误导行为的名称
3. **做出有意义的区分**：避免冗余或无意义的词语
4. **使用可发音的名称**：你需要谈论这段代码
5. **使用可搜索的名称**：避免使用单个字母和幻数
6. **用代码解释自己**：通过良好的命名减少对注释的需求
---

## 意大利面条代码
意大利面条式代码是指非结构化、难以维护且控制流错综复杂的源代码。
### 过度嵌套
**错误的例子：**```python
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

**更好的方法：**```python
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

### 长函数
**错误的例子：**```python
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

**更好的方法：**```python
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

### 类似 Goto 的模式
**错误的例子：**```python
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

**更好的方法：**```python
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

## 循环依赖
当模块直接或间接相互依赖并创建循环时，就会发生循环依赖。
### 直接循环依赖
**错误的例子：**```python
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

**为什么不好：**
- 运行时导入错误
- 无法独立导入任一模块
- 代码不能单独测试
**解决方案：提取共享接口**```python
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

### 间接循环依赖
**错误的例子：**```
module_a -> module_b -> module_c -> module_a
```

**解决方案：依赖倒置**```python
# Define interfaces/protocols that modules depend on
# Modules implement interfaces rather than depending on concrete implementations
```

---

## 糟糕的文档
糟糕的文档会增加维护成本、减慢入职速度并造成知识孤岛。
### 缺少文档
**错误的例子：**```python
def calc(a, b, c):
    x = a * 2 + b
    y = x / c if c != 0 else 1
    return y * 1.15
```

**更好的方法：**```python
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

### 过时的文档
**错误的例子：**```python
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

**解决方案：** 让文档靠近代码，并在代码审查期间更新它。
### 过多的文档
**错误的例子：**```python
# Increment i by 1
i += 1

# Check if name equals John
if name == "John":
    # Print greeting
    print("Hello, John!")
```

**解决方案：** 让清晰的代码说明一切；记录原因，而不是记录什么。
---

## 代码异味
代码异味是软件设计中更深层次问题的表面迹象。
### 重复的代码
**错误的例子：**```python
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

**更好的方法：**```python
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

### 长参数列表
**错误的例子：**```python
def create_user(username, password, email, first_name, last_name, 
                phone, address, city, state, zip_code, country,
                birth_date, gender, occupation, company):
    # 15 parameters!
```

**更好的方法：**```python
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

## 相关主题
- **安全漏洞**：有关安全相关的代码问题，请参阅 `02_security_vulnerabilities.md`
- **Git 历史记录**：请参阅`06_git_documentation.md`了解提交消息和版本控制最佳实践
- **API设计**：接口设计原则参见`07_api_system_design.md`