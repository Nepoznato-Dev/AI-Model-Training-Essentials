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
# कोड गुणवत्ता संबंधी समस्याएं
यह दस्तावेज़ खराब चर नाम, खराब दस्तावेज़ीकरण, स्पेगेटी कोड, सर्कुलर निर्भरता और अन्य रखरखाव संबंधी मुद्दों सहित सामान्य कोड गुणवत्ता समस्याओं को समेकित करता है।
---

## खराब परिवर्तनीय नाम
खराब वेरिएबल नामकरण से कोड को पढ़ना, समझना और बनाए रखना कठिन हो जाता है। अच्छे नाम दस्तावेज़ीकरण के रूप में काम करते हैं और संज्ञानात्मक भार को कम करते हैं।
### एकल अक्षर नाम (लूप काउंटरों को छोड़कर)
**खराब उदाहरण:**```python
def p(d, r, t):
    a = d * ((1 + r / 12) ** (12 * t))
    i = a - d
    return i
```

**समस्याएँ:**
- कौन से पैरामीटर दर्शाते हैं इसका कोई संकेत नहीं
- दस्तावेज़ के बिना समझना असंभव है
- रखरखाव के दौरान त्रुटि-प्रवण
**बेहतर दृष्टिकोण:**```python
def calculate_compound_interest(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    months = 12 * years
    amount = principal * ((1 + monthly_rate) ** months)
    interest = amount - principal
    return interest
```

### अस्पष्ट या सामान्य नाम
**खराब उदाहरण:**```python
data = get_data()
result = process_data(data)
temp = transform(result)
final = finalize(temp)
```

**बेहतर दृष्टिकोण:**```python
user_records = fetch_user_records()
validated_users = validate_user_data(user_records)
enriched_users = add_user_preferences(validated_users)
user_profiles = build_user_profiles(enriched_users)
```

### भ्रामक नाम
**खराब उदाहरण:**```python
def get_users():
    # Actually modifies database, doesn't just "get"
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

**बेहतर दृष्टिकोण:**```python
def update_user_last_login_and_fetch():
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

### सर्वोत्तम प्रथाओं का नामकरण
1. **इरादे उजागर करने वाले नामों का उपयोग करें**: नामों से यह स्पष्ट होना चाहिए कि कोई चीज़ क्यों मौजूद है
2. **दुष्प्रचार से बचें**: ऐसे नामों का उपयोग न करें जो व्यवहार के बारे में गुमराह करते हों
3. **अर्थपूर्ण अंतर करें**: अनावश्यक या निरर्थक शब्दों से बचें
4. **उच्चारण योग्य नामों का उपयोग करें**: आपको इस कोड के बारे में बात करनी होगी
5. **खोजे जाने योग्य नामों का उपयोग करें**: एकल अक्षरों और जादुई संख्याओं से बचें
6. **खुद को कोड में समझाएं**: अच्छे नामकरण के माध्यम से टिप्पणियों की आवश्यकता कम करें
---

## स्पेगेटी कोड
स्पेगेटी कोड उलझे हुए नियंत्रण प्रवाह के साथ असंरचित, बनाए रखने में मुश्किल स्रोत कोड को संदर्भित करता है।
### अत्यधिक घोंसला बनाना
**खराब उदाहरण:**```python
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

**बेहतर दृष्टिकोण:**```python
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

### लंबे कार्य
**खराब उदाहरण:**```python
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

**बेहतर दृष्टिकोण:**```python
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

### गोटो जैसे पैटर्न
**खराब उदाहरण:**```python
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

**बेहतर दृष्टिकोण:**```python
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

## परिपत्र निर्भरताएँ
परिपत्र निर्भरता तब होती है जब मॉड्यूल चक्र बनाते हुए प्रत्यक्ष या अप्रत्यक्ष रूप से एक दूसरे पर निर्भर होते हैं।
### प्रत्यक्ष परिपत्र निर्भरताएँ
**खराब उदाहरण:**```python
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

**यह बुरा क्यों है:**
- रनटाइम पर आयात त्रुटियाँ
- किसी भी मॉड्यूल को स्वतंत्र रूप से आयात करना असंभव है
- कोड का अलग से परीक्षण नहीं किया जा सकता
**समाधान: साझा इंटरफ़ेस निकालें**```python
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

### अप्रत्यक्ष परिपत्र निर्भरताएँ
**खराब उदाहरण:**```
module_a -> module_b -> module_c -> module_a
```

**समाधान: निर्भरता व्युत्क्रम**```python
# Define interfaces/protocols that modules depend on
# Modules implement interfaces rather than depending on concrete implementations
```

---

## ख़राब दस्तावेज़ीकरण
खराब दस्तावेज़ीकरण से रखरखाव की लागत बढ़ जाती है, ऑनबोर्डिंग धीमी हो जाती है और ज्ञान भंडार का निर्माण होता है।
### गुम दस्तावेज़
**खराब उदाहरण:**```python
def calc(a, b, c):
    x = a * 2 + b
    y = x / c if c != 0 else 1
    return y * 1.15
```

**बेहतर दृष्टिकोण:**```python
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

### पुराना दस्तावेज़
**खराब उदाहरण:**```python
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

**समाधान:** दस्तावेज़ को कोड के पास रखें और कोड समीक्षा के दौरान इसे अपडेट करें।
### अति-दस्तावेज़ीकरण
**खराब उदाहरण:**```python
# Increment i by 1
i += 1

# Check if name equals John
if name == "John":
    # Print greeting
    print("Hello, John!")
```

**समाधान:** स्पष्ट कोड को स्वयं बोलने दें; दस्तावेज़ क्यों, क्या नहीं।
---

## कोड गंध
कोड गंध सॉफ़्टवेयर डिज़ाइन में गहरी समस्याओं के सतही-स्तरीय संकेत हैं।
### डुप्लिकेट कोड
**खराब उदाहरण:**```python
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

**बेहतर दृष्टिकोण:**```python
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

### लंबी पैरामीटर सूचियाँ
**खराब उदाहरण:**```python
def create_user(username, password, email, first_name, last_name, 
                phone, address, city, state, zip_code, country,
                birth_date, gender, occupation, company):
    # 15 parameters!
```

**बेहतर दृष्टिकोण:**```python
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

## संबंधित विषय
- **सुरक्षा कमजोरियाँ**: सुरक्षा संबंधी कोड समस्याओं के लिए`02_security_vulnerabilities.md`देखें
- **गिट इतिहास**: प्रतिबद्ध संदेश और संस्करण नियंत्रण सर्वोत्तम प्रथाओं के लिए`06_git_documentation.md`देखें
- **एपीआई डिज़ाइन**: इंटरफ़ेस डिज़ाइन सिद्धांतों के लिए`07_api_system_design.md`देखें