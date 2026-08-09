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

# 코드 품질 문제
이 문서는 잘못된 변수 이름, 잘못된 문서화, 스파게티 코드, 순환 종속성 및 기타 유지 관리 문제를 포함한 일반적인 코드 품질 문제를 통합합니다.
---

## 잘못된 변수 이름
잘못된 변수 이름 지정으로 인해 코드를 읽고, 이해하고, 유지 관리하기가 더 어려워집니다. 좋은 이름은 문서화 역할을 하며 인지 부하를 줄여줍니다.
### 단일 문자 이름(루프 카운터 제외)
**나쁜 예:**```python
def p(d, r, t):
    a = d * ((1 + r / 12) ** (12 * t))
    i = a - d
    return i
```

**문제:**
- 어떤 매개변수가 나타내는지 표시하지 않음
- 문서 없이는 이해가 불가능합니다.
- 유지보수 시 오류가 발생하기 쉬움
**더 나은 접근 방식:**```python
def calculate_compound_interest(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    months = 12 * years
    amount = principal * ((1 + monthly_rate) ** months)
    interest = amount - principal
    return interest
```

### 모호하거나 일반적인 이름
**나쁜 예:**```python
data = get_data()
result = process_data(data)
temp = transform(result)
final = finalize(temp)
```

**더 나은 접근 방식:**```python
user_records = fetch_user_records()
validated_users = validate_user_data(user_records)
enriched_users = add_user_preferences(validated_users)
user_profiles = build_user_profiles(enriched_users)
```

### 오해의 소지가 있는 이름
**나쁜 예:**```python
def get_users():
    # Actually modifies database, doesn't just "get"
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

**더 나은 접근 방식:**```python
def update_user_last_login_and_fetch():
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

### 이름 지정 모범 사례
1. **의도를 드러내는 이름 사용**: 이름은 무언가가 존재하는 이유를 설명해야 합니다.
2. **허위 정보 방지**: 행동에 대해 오해를 불러일으키는 이름을 사용하지 마세요.
3. **의미 있는 구분**: 중복되거나 의미 없는 단어는 피하세요.
4. **발음하기 쉬운 이름을 사용하세요**: 이 코드에 대해 이야기해야 합니다.
5. **검색 가능한 이름 사용**: 단일 문자와 마법 숫자를 사용하지 마세요.
6. **코드로 자신을 설명하세요**: 좋은 이름 지정을 통해 주석의 필요성을 줄입니다.
---

## 스파게티 코드
스파게티 코드는 제어 흐름이 얽혀 있어 구조화되지 않고 유지 관리가 어려운 소스 코드를 말합니다.
### 과도한 중첩
**나쁜 예:**```python
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

**더 나은 접근 방식:**```python
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

### 긴 함수
**나쁜 예:**```python
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

**더 나은 접근 방식:**```python
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

### Goto와 유사한 패턴
**나쁜 예:**```python
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

**더 나은 접근 방식:**```python
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

## 순환 종속성
순환 종속성은 모듈이 서로 직접 또는 간접적으로 의존하여 순환을 생성할 때 발생합니다.
### 직접 순환 종속성
**나쁜 예:**```python
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

**나쁜 이유:**
- 런타임 시 가져오기 오류
- 두 모듈 중 하나를 독립적으로 가져올 수 없습니다.
- 코드는 단독으로 테스트할 수 없습니다.
**해결책: 공유 인터페이스 추출**```python
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

### 간접 순환 종속성
**나쁜 예:**```
module_a -> module_b -> module_c -> module_a
```

**해결책: 종속성 반전**```python
# Define interfaces/protocols that modules depend on
# Modules implement interfaces rather than depending on concrete implementations
```

---

## 잘못된 문서
문서화가 제대로 이루어지지 않으면 유지 관리 비용이 증가하고 온보딩 속도가 느려지며 지식 사일로가 생성됩니다.
### 문서 누락
**나쁜 예:**```python
def calc(a, b, c):
    x = a * 2 + b
    y = x / c if c != 0 else 1
    return y * 1.15
```

**더 나은 접근 방식:**```python
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

### 오래된 문서
**나쁜 예:**```python
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

**해결책:** 문서를 코드 가까이에 보관하고 코드 검토 중에 업데이트하세요.
### 과도한 문서화
**나쁜 예:**```python
# Increment i by 1
i += 1

# Check if name equals John
if name == "John":
    # Print greeting
    print("Hello, John!")
```

**해결책:** 명확한 코드가 그 자체로 말하도록 하십시오. 무엇이 아니라 왜인지 문서화하세요.
---

## 코드 냄새
코드 냄새는 소프트웨어 설계의 더 깊은 문제를 표면적으로 나타냅니다.
### 중복된 코드
**나쁜 예:**```python
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

**더 나은 접근 방식:**```python
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

### 긴 매개변수 목록
**나쁜 예:**```python
def create_user(username, password, email, first_name, last_name, 
                phone, address, city, state, zip_code, country,
                birth_date, gender, occupation, company):
    # 15 parameters!
```

**더 나은 접근 방식:**```python
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

## 관련 주제
- **보안 취약점**: 보안 관련 코드 문제는 `02_security_vulnerabilities.md`를 참조하세요.
- **Git 기록**: 커밋 메시지 및 버전 제어 모범 사례는 `06_git_documentation.md`를 참조하세요.
- **API 디자인**: 인터페이스 디자인 원칙은 `07_api_system_design.md`를 참조하세요.