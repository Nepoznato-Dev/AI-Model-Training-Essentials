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

# Probleme mit der Codequalität
Dieses Dokument konsolidiert häufige Probleme mit der Codequalität, darunter fehlerhafte Variablennamen, schlechte Dokumentation, Spaghetti-Code, zirkuläre Abhängigkeiten und andere Probleme bei der Wartbarkeit.
---

## Ungültige Variablennamen
Eine schlechte Variablenbenennung erschwert das Lesen, Verstehen und Verwalten des Codes. Gute Namen dienen der Dokumentation und reduzieren die kognitive Belastung.
### Einzelbuchstabennamen (außer Schleifenzähler)
**Schlechtes Beispiel:**```python
def p(d, r, t):
    a = d * ((1 + r / 12) ** (12 * t))
    i = a - d
    return i
```

**Probleme:**
- Keine Angabe, welche Parameter dargestellt werden
- Ohne Dokumentation nicht verständlich
- Fehleranfällig bei der Wartung
**Besserer Ansatz:**```python
def calculate_compound_interest(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    months = 12 * years
    amount = principal * ((1 + monthly_rate) ** months)
    interest = amount - principal
    return interest
```

### Vage oder generische Namen
**Schlechtes Beispiel:**```python
data = get_data()
result = process_data(data)
temp = transform(result)
final = finalize(temp)
```

**Besserer Ansatz:**```python
user_records = fetch_user_records()
validated_users = validate_user_data(user_records)
enriched_users = add_user_preferences(validated_users)
user_profiles = build_user_profiles(enriched_users)
```

### Irreführende Namen
**Schlechtes Beispiel:**```python
def get_users():
    # Actually modifies database, doesn't just "get"
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

**Besserer Ansatz:**```python
def update_user_last_login_and_fetch():
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

### Best Practices benennen
1. **Verwenden Sie Namen, die Ihre Absicht offenbaren**: Namen sollten erklären, warum etwas existiert
2. **Desinformation vermeiden**: Verwenden Sie keine Namen, die über das Verhalten irreführen
3. **Machen Sie sinnvolle Unterscheidungen**: Vermeiden Sie überflüssige oder bedeutungslose Wörter
4. **Verwenden Sie aussprechbare Namen**: Sie müssen über diesen Code sprechen
5. **Suchbare Namen verwenden**: Vermeiden Sie einzelne Buchstaben und magische Zahlen
6. **Erklären Sie sich im Code**: Reduzieren Sie die Notwendigkeit von Kommentaren durch gute Benennung
---

## Spaghetti-Code
Unter Spaghetti-Code versteht man unstrukturierten, schwer zu wartenden Quellcode mit verworrenem Kontrollfluss.
### Übermäßige Verschachtelung
**Schlechtes Beispiel:**```python
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

**Besserer Ansatz:**```python
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

### Lange Funktionen
**Schlechtes Beispiel:**```python
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

**Besserer Ansatz:**```python
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

### Goto-ähnliche Muster
**Schlechtes Beispiel:**```python
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

**Besserer Ansatz:**```python
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

## Zirkuläre Abhängigkeiten
Zirkuläre Abhängigkeiten treten auf, wenn Module direkt oder indirekt voneinander abhängig sind und Zyklen entstehen.
### Direkte zirkuläre Abhängigkeiten
**Schlechtes Beispiel:**```python
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

**Warum es schlecht ist:**
- Fehler zur Laufzeit importieren
- Es ist nicht möglich, eines der beiden Module unabhängig voneinander zu importieren
- Code kann nicht isoliert getestet werden
**Lösung: Gemeinsam genutzte Schnittstelle extrahieren**```python
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

### Indirekte zirkuläre Abhängigkeiten
**Schlechtes Beispiel:**```
module_a -> module_b -> module_c -> module_a
```

**Lösung: Abhängigkeitsumkehr**```python
# Define interfaces/protocols that modules depend on
# Modules implement interfaces rather than depending on concrete implementations
```

---

## Schlechte Dokumentation
Eine schlechte Dokumentation erhöht die Wartungskosten, verlangsamt das Onboarding und schafft Wissenssilos.
### Fehlende Dokumentation
**Schlechtes Beispiel:**```python
def calc(a, b, c):
    x = a * 2 + b
    y = x / c if c != 0 else 1
    return y * 1.15
```

**Besserer Ansatz:**```python
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

### Veraltete Dokumentation
**Schlechtes Beispiel:**```python
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

**Lösung:** Halten Sie die Dokumentation nah am Code und aktualisieren Sie sie während der Codeüberprüfungen.
### Überdokumentation
**Schlechtes Beispiel:**```python
# Increment i by 1
i += 1

# Check if name equals John
if name == "John":
    # Print greeting
    print("Hello, John!")
```

**Lösung:** Lassen Sie klaren Code für sich selbst sprechen; Dokumentieren Sie, warum, nicht was.
---

## Code-Gerüche
Code-Gerüche sind oberflächliche Hinweise auf tiefere Probleme im Software-Design.
### Doppelter Code
**Schlechtes Beispiel:**```python
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

**Besserer Ansatz:**```python
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

### Lange Parameterlisten
**Schlechtes Beispiel:**```python
def create_user(username, password, email, first_name, last_name, 
                phone, address, city, state, zip_code, country,
                birth_date, gender, occupation, company):
    # 15 parameters!
```

**Besserer Ansatz:**```python
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

## Verwandte Themen
- **Sicherheitslücken**: Informationen zu sicherheitsrelevanten Codeproblemen finden Sie unter `02_security_vulnerabilities.md`
- **Git-Verlauf**: Best Practices für Commit-Nachrichten und Versionskontrolle finden Sie unter `06_git_documentation.md`
- **API-Design**: Siehe`07_api_system_design.md`für Schnittstellendesignprinzipien