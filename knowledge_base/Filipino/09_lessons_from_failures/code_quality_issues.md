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
# Mga Isyu sa Kalidad ng Code
Pinagsasama-sama ng dokumentong ito ang mga karaniwang problema sa kalidad ng code kabilang ang mga hindi magandang variable na pangalan, hindi magandang dokumentasyon, spaghetti code, circular dependencies, at iba pang isyu sa maintainability.
---

## Masamang Mga Pangalan ng Variable
Ang mahinang pagpapangalan sa variable ay nagpapahirap sa code na basahin, maunawaan, at mapanatili. Ang magagandang pangalan ay nagsisilbing dokumentasyon at nagpapababa ng cognitive load.
### Mga Pangalan ng Isang Letra (Maliban sa Mga Loop Counter)
**Masama Halimbawa:**```python
def p(d, r, t):
    a = d * ((1 + r / 12) ** (12 * t))
    i = a - d
    return i
```

**Mga Problema:**
- Walang indikasyon kung anong mga parameter ang kinakatawan
- Imposibleng maunawaan nang walang dokumentasyon
- Malamang na mali sa panahon ng pagpapanatili
**Mas mahusay na Diskarte:**```python
def calculate_compound_interest(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    months = 12 * years
    amount = principal * ((1 + monthly_rate) ** months)
    interest = amount - principal
    return interest
```

### Malabo o Generic na Pangalan
**Masama Halimbawa:**```python
data = get_data()
result = process_data(data)
temp = transform(result)
final = finalize(temp)
```

**Mas mahusay na Diskarte:**```python
user_records = fetch_user_records()
validated_users = validate_user_data(user_records)
enriched_users = add_user_preferences(validated_users)
user_profiles = build_user_profiles(enriched_users)
```

### Mga Mapanlinlang na Pangalan
**Masama Halimbawa:**```python
def get_users():
    # Actually modifies database, doesn't just "get"
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

**Mas mahusay na Diskarte:**```python
def update_user_last_login_and_fetch():
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

### Mga Pinakamahuhusay na Kasanayan sa Pangalan
1. **Gumamit ng mga pangalang naghahayag ng intensyon**: Dapat ipaliwanag ng mga pangalan kung bakit umiiral ang isang bagay
2. **Iwasan ang disinformation**: Huwag gumamit ng mga pangalan na nanlilinlang tungkol sa pag-uugali
3. **Gumawa ng makabuluhang pagkakaiba**: Iwasan ang mga kalabisan o walang kahulugan na mga salita
4. **Gumamit ng mga binibigkas na pangalan**: Kakailanganin mong pag-usapan ang code na ito
5. **Gumamit ng mga mahahanap na pangalan**: Iwasan ang mga solong titik at magic number
6. **Ipaliwanag ang iyong sarili sa code**: Bawasan ang pangangailangan para sa mga komento sa pamamagitan ng mabuting pagpapangalan
---

## Spaghetti Code
Ang spaghetti code ay tumutukoy sa hindi nakaayos, mahirap panatilihing source code na may gusot na daloy ng kontrol.
### Labis na Pugad
**Masama Halimbawa:**```python
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

**Mas mahusay na Diskarte:**```python
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

### Mahabang Pag-andar
**Masama Halimbawa:**```python
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

**Mas mahusay na Diskarte:**```python
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

### Mga Pattern na parang Goto
**Masama Halimbawa:**```python
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

**Mas mahusay na Diskarte:**```python
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

## Circular Dependencies
Nagaganap ang mga circular dependency kapag ang mga module ay nakadepende sa isa't isa nang direkta o hindi direkta, na lumilikha ng mga cycle.
### Direktang Circular Dependencies
**Masama Halimbawa:**```python
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

**Bakit Masama:**
- Mag-import ng mga error sa runtime
- Imposibleng mag-import ng alinman sa module nang nakapag-iisa
- Hindi masusuri ang code nang hiwalay
**Solusyon: I-extract ang Nakabahaging Interface**```python
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

### Hindi Direktang Circular Dependencies
**Masama Halimbawa:**```
module_a -> module_b -> module_c -> module_a
```

**Solusyon: Dependency Inversion**```python
# Define interfaces/protocols that modules depend on
# Modules implement interfaces rather than depending on concrete implementations
```

---

## Mahina Documentation
Ang hindi magandang dokumentasyon ay nagpapataas ng mga gastos sa pagpapanatili, nagpapabagal sa onboarding, at lumilikha ng mga silo ng kaalaman.
### Nawawalang Dokumentasyon
**Masama Halimbawa:**```python
def calc(a, b, c):
    x = a * 2 + b
    y = x / c if c != 0 else 1
    return y * 1.15
```

**Mas mahusay na Diskarte:**```python
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

### Lumang Dokumentasyon
**Masama Halimbawa:**```python
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

**Solusyon:** Panatilihing malapit sa code ang dokumentasyon at i-update ito habang sinusuri ang code.
### Over-Documentation
**Masama Halimbawa:**```python
# Increment i by 1
i += 1

# Check if name equals John
if name == "John":
    # Print greeting
    print("Hello, John!")
```

**Solusyon:** Hayaang malinaw na code ang magsalita para sa sarili nito; dokumento kung bakit, hindi ano.
---

## Mga amoy ng Code
Ang mga amoy ng code ay mga indikasyon sa antas ng ibabaw ng mas malalalim na problema sa disenyo ng software.
### Dobleng Code
**Masama Halimbawa:**```python
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

**Mas mahusay na Diskarte:**```python
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

### Mahabang Listahan ng Parameter
**Masama Halimbawa:**```python
def create_user(username, password, email, first_name, last_name, 
                phone, address, city, state, zip_code, country,
                birth_date, gender, occupation, company):
    # 15 parameters!
```

**Mas mahusay na Diskarte:**```python
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

## Mga Kaugnay na Paksa
- **Mga Kahinaan sa Seguridad**: Tingnan ang`02_security_vulnerabilities.md`para sa mga isyu sa code na nauugnay sa seguridad
- **Kasaysayan ng Git**: Tingnan ang`06_git_documentation.md`para sa commit message at mga pinakamahuhusay na kagawian sa pagkontrol ng bersyon
- **API Design**: Tingnan ang`07_api_system_design.md`para sa mga prinsipyo ng disenyo ng interface