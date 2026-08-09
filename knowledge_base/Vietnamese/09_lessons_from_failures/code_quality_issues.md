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
# Vấn đề về chất lượng mã
Tài liệu này tổng hợp các vấn đề về chất lượng mã phổ biến bao gồm tên biến không hợp lệ, tài liệu kém, mã spaghetti, phụ thuộc vòng tròn và các vấn đề về khả năng bảo trì khác.
---

## Tên biến xấu
Việc đặt tên biến kém khiến mã khó đọc, khó hiểu và bảo trì hơn. Những cái tên hay đóng vai trò là tài liệu và giảm tải nhận thức.
### Tên một chữ cái (Ngoại trừ Bộ đếm vòng lặp)
**Ví dụ tồi:**```python
def p(d, r, t):
    a = d * ((1 + r / 12) ** (12 * t))
    i = a - d
    return i
```

**Vấn đề:**
- Không có dấu hiệu cho biết thông số nào đại diện
- Không thể hiểu được nếu không có tài liệu
- Dễ xảy ra lỗi trong quá trình bảo trì
**Cách tiếp cận tốt hơn:**```python
def calculate_compound_interest(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    months = 12 * years
    amount = principal * ((1 + monthly_rate) ** months)
    interest = amount - principal
    return interest
```

### Tên mơ hồ hoặc chung chung
**Ví dụ tồi:**```python
data = get_data()
result = process_data(data)
temp = transform(result)
final = finalize(temp)
```

**Cách tiếp cận tốt hơn:**```python
user_records = fetch_user_records()
validated_users = validate_user_data(user_records)
enriched_users = add_user_preferences(validated_users)
user_profiles = build_user_profiles(enriched_users)
```

### Tên gây hiểu lầm
**Ví dụ tồi:**```python
def get_users():
    # Actually modifies database, doesn't just "get"
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

**Cách tiếp cận tốt hơn:**```python
def update_user_last_login_and_fetch():
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

### Cách đặt tên tốt nhất
1. **Sử dụng tên tiết lộ ý định**: Tên phải giải thích lý do tồn tại
2. **Tránh thông tin sai lệch**: Không sử dụng tên gây hiểu lầm về hành vi
3. **Tạo sự khác biệt có ý nghĩa**: Tránh dùng từ thừa hoặc vô nghĩa
4. **Sử dụng tên có thể phát âm**: Bạn sẽ cần nói về mã này
5. **Sử dụng tên có thể tìm kiếm**: Tránh các chữ cái đơn lẻ và các con số ma thuật
6. **Giải thích bằng mã**: Giảm nhu cầu nhận xét thông qua cách đặt tên hay
---

## Mã Spaghetti
Mã Spaghetti đề cập đến mã nguồn không có cấu trúc, khó bảo trì với luồng điều khiển rối rắm.
### Lồng ghép quá mức
**Ví dụ tồi:**```python
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

**Cách tiếp cận tốt hơn:**```python
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

### Hàm dài
**Ví dụ tồi:**```python
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

**Cách tiếp cận tốt hơn:**```python
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

### Mẫu giống Goto
**Ví dụ tồi:**```python
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

**Cách tiếp cận tốt hơn:**```python
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

## Phụ thuộc vòng tròn
Sự phụ thuộc vòng tròn xảy ra khi các mô-đun phụ thuộc trực tiếp hoặc gián tiếp vào nhau, tạo ra các chu kỳ.
### Phụ thuộc vòng tròn trực tiếp
**Ví dụ tồi:**```python
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

**Tại sao nó xấu:**
- Lỗi nhập khi chạy
- Không thể nhập mô-đun một cách độc lập
- Mã không thể được kiểm tra một cách cô lập
**Giải pháp: Trích xuất giao diện chia sẻ**```python
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

### Phụ thuộc vòng tròn gián tiếp
**Ví dụ tồi:**```
module_a -> module_b -> module_c -> module_a
```

**Giải pháp: Đảo ngược phụ thuộc**```python
# Define interfaces/protocols that modules depend on
# Modules implement interfaces rather than depending on concrete implementations
```

---

## Tài liệu kém
Tài liệu kém làm tăng chi phí bảo trì, làm chậm quá trình triển khai và tạo ra các kho chứa kiến ​​thức.
### Thiếu tài liệu
**Ví dụ tồi:**```python
def calc(a, b, c):
    x = a * 2 + b
    y = x / c if c != 0 else 1
    return y * 1.15
```

**Cách tiếp cận tốt hơn:**```python
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

### Tài liệu lỗi thời
**Ví dụ tồi:**```python
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

**Giải pháp:** Giữ tài liệu gần với mã và cập nhật nó trong quá trình đánh giá mã.
### Thừa tài liệu
**Ví dụ tồi:**```python
# Increment i by 1
i += 1

# Check if name equals John
if name == "John":
    # Print greeting
    print("Hello, John!")
```

**Giải pháp:** Hãy để mã rõ ràng tự nói lên điều đó; ghi lại lý do tại sao, không phải cái gì.
---

## Mùi mã
Mùi mã là dấu hiệu ở mức độ bề mặt của các vấn đề sâu hơn trong thiết kế phần mềm.
### Mã trùng lặp
**Ví dụ tồi:**```python
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

**Cách tiếp cận tốt hơn:**```python
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

### Danh sách tham số dài
**Ví dụ tồi:**```python
def create_user(username, password, email, first_name, last_name, 
                phone, address, city, state, zip_code, country,
                birth_date, gender, occupation, company):
    # 15 parameters!
```

**Cách tiếp cận tốt hơn:**```python
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

## Chủ đề liên quan
- **Lỗ hổng bảo mật**: Xem`02_security_vulnerabilities.md`để biết các vấn đề về mã liên quan đến bảo mật
- **Lịch sử Git**: Xem`06_git_documentation.md`để biết các phương pháp hay nhất về thông báo cam kết và kiểm soát phiên bản
- **Thiết kế API**: Xem`07_api_system_design.md`để biết nguyên tắc thiết kế giao diện