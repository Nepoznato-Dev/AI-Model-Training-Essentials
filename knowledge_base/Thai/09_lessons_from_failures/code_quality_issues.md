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
# ปัญหาคุณภาพของโค้ด
เอกสารนี้รวบรวมปัญหาคุณภาพโค้ดทั่วไป รวมถึงชื่อตัวแปรที่ไม่ดี เอกสารประกอบที่ไม่ดี โค้ดสปาเก็ตตี้ การขึ้นต่อกันแบบวงกลม และปัญหาด้านการบำรุงรักษาอื่นๆ
---

## ชื่อตัวแปรไม่ถูกต้อง
การตั้งชื่อตัวแปรที่ไม่ดีทำให้โค้ดอ่าน เข้าใจ และบำรุงรักษาได้ยากขึ้น ชื่อที่ดีทำหน้าที่เป็นเอกสารและลดภาระทางการรับรู้
### ชื่อตัวอักษรเดี่ยว (ยกเว้นตัวนับลูป)
**ตัวอย่างที่ไม่ดี:**```python
def p(d, r, t):
    a = d * ((1 + r / 12) ** (12 * t))
    i = a - d
    return i
```

**ปัญหา:**
- ไม่มีข้อบ่งชี้ว่าพารามิเตอร์ใดเป็นตัวแทน
- ไม่สามารถเข้าใจได้หากไม่มีเอกสารประกอบ
- เกิดข้อผิดพลาดได้ง่ายระหว่างการบำรุงรักษา
**แนวทางที่ดีกว่า:**```python
def calculate_compound_interest(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    months = 12 * years
    amount = principal * ((1 + monthly_rate) ** months)
    interest = amount - principal
    return interest
```

### ชื่อคลุมเครือหรือชื่อทั่วไป
**ตัวอย่างที่ไม่ดี:**```python
data = get_data()
result = process_data(data)
temp = transform(result)
final = finalize(temp)
```

**แนวทางที่ดีกว่า:**```python
user_records = fetch_user_records()
validated_users = validate_user_data(user_records)
enriched_users = add_user_preferences(validated_users)
user_profiles = build_user_profiles(enriched_users)
```

### ชื่อที่ทำให้เข้าใจผิด
**ตัวอย่างที่ไม่ดี:**```python
def get_users():
    # Actually modifies database, doesn't just "get"
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

**แนวทางที่ดีกว่า:**```python
def update_user_last_login_and_fetch():
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

### แนวทางปฏิบัติที่ดีที่สุดในการตั้งชื่อ
1. **ใช้ชื่อที่เปิดเผยความตั้งใจ**: ชื่อควรอธิบายว่าเหตุใดจึงมีบางสิ่งอยู่
2. **หลีกเลี่ยงการบิดเบือนข้อมูล**: ห้ามใช้ชื่อที่ทำให้เข้าใจผิดเกี่ยวกับพฤติกรรม
3. **สร้างความแตกต่างที่มีความหมาย**: หลีกเลี่ยงคำที่ซ้ำซ้อนหรือไม่มีความหมาย
4. **ใช้ชื่อที่ออกเสียงได้**: คุณจะต้องพูดถึงรหัสนี้
5. **ใช้ชื่อที่ค้นหาได้**: หลีกเลี่ยงตัวอักษรตัวเดียวและตัวเลขมหัศจรรย์
6. **อธิบายตัวเองด้วยโค้ด**: ลดความจำเป็นในการแสดงความคิดเห็นด้วยการตั้งชื่อที่ดี
---

## สปาเก็ตตี้โค้ด
รหัสสปาเก็ตตี้หมายถึงซอร์สโค้ดที่ไม่มีโครงสร้างและยากต่อการบำรุงรักษาโดยมีโฟลว์การควบคุมที่พันกัน
### การทำรังมากเกินไป
**ตัวอย่างที่ไม่ดี:**```python
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

**แนวทางที่ดีกว่า:**```python
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

### ฟังก์ชั่นยาว
**ตัวอย่างที่ไม่ดี:**```python
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

**แนวทางที่ดีกว่า:**```python
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

### รูปแบบที่เหมือน Goto
**ตัวอย่างที่ไม่ดี:**```python
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

**แนวทางที่ดีกว่า:**```python
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

## การพึ่งพาแบบวงกลม
การพึ่งพาแบบวงกลมเกิดขึ้นเมื่อโมดูลพึ่งพาซึ่งกันและกันทั้งทางตรงและทางอ้อม ทำให้เกิดวงจรขึ้น
### การพึ่งพาแบบวงกลมโดยตรง
**ตัวอย่างที่ไม่ดี:**```python
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

**ทำไมมันแย่:**
- นำเข้าข้อผิดพลาดขณะรันไทม์
- ไม่สามารถนำเข้าโมดูลใดโมดูลหนึ่งได้อย่างอิสระ
- ไม่สามารถทดสอบรหัสแบบแยกส่วนได้
**แนวทางแก้ไข: แยกส่วนต่อประสานที่ใช้ร่วมกัน**```python
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

### การพึ่งพาแบบวงกลมทางอ้อม
**ตัวอย่างที่ไม่ดี:**```
module_a -> module_b -> module_c -> module_a
```

**วิธีแก้ปัญหา: การผกผันการพึ่งพา**```python
# Define interfaces/protocols that modules depend on
# Modules implement interfaces rather than depending on concrete implementations
```

---

## เอกสารไม่ดี
เอกสารที่ไม่ดีจะเพิ่มค่าใช้จ่ายในการบำรุงรักษา ทำให้การเริ่มต้นใช้งานช้าลง และสร้างคลังความรู้
### เอกสารขาดหายไป
**ตัวอย่างที่ไม่ดี:**```python
def calc(a, b, c):
    x = a * 2 + b
    y = x / c if c != 0 else 1
    return y * 1.15
```

**แนวทางที่ดีกว่า:**```python
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

### เอกสารที่ล้าสมัย
**ตัวอย่างที่ไม่ดี:**```python
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

**วิธีแก้ไข:** เก็บเอกสารให้ใกล้กับโค้ดและอัปเดตในระหว่างการตรวจสอบโค้ด
### เอกสารเกิน
**ตัวอย่างที่ไม่ดี:**```python
# Increment i by 1
i += 1

# Check if name equals John
if name == "John":
    # Print greeting
    print("Hello, John!")
```

**วิธีแก้ปัญหา:** ให้โค้ดที่ชัดเจนพูดเพื่อตัวมันเอง เอกสารว่าทำไม ไม่ใช่อะไร
---

## รหัสกลิ่น
กลิ่นโค้ดเป็นการบ่งชี้ระดับพื้นผิวของปัญหาที่ลึกซึ้งยิ่งขึ้นในการออกแบบซอฟต์แวร์
### รหัสซ้ำกัน
**ตัวอย่างที่ไม่ดี:**```python
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

**แนวทางที่ดีกว่า:**```python
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

### รายการพารามิเตอร์แบบยาว
**ตัวอย่างที่ไม่ดี:**```python
def create_user(username, password, email, first_name, last_name, 
                phone, address, city, state, zip_code, country,
                birth_date, gender, occupation, company):
    # 15 parameters!
```

**แนวทางที่ดีกว่า:**```python
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

## หัวข้อที่เกี่ยวข้อง
- **ช่องโหว่ด้านความปลอดภัย**: ดู`02_security_vulnerabilities.md`สำหรับปัญหารหัสที่เกี่ยวข้องกับความปลอดภัย
- **ประวัติ Git**: ดู`06_git_documentation.md`สำหรับแนวทางปฏิบัติที่ดีที่สุดในการส่งข้อความและการควบคุมเวอร์ชัน
- **การออกแบบ API**: ดู`07_api_system_design.md`สำหรับหลักการออกแบบอินเทอร์เฟซ