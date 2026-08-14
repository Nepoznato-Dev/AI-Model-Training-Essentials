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
# Problemi di qualità del codice
Questo documento consolida i problemi comuni di qualità del codice, inclusi nomi di variabili errati, scarsa documentazione, spaghetti code, dipendenze circolari e altri problemi di manutenibilità.
---

## Nomi di variabili errati
Una denominazione inadeguata delle variabili rende il codice più difficile da leggere, comprendere e mantenere. I buoni nomi servono da documentazione e riducono il carico cognitivo.
### Nomi con una sola lettera (tranne i contatori di loop)
**Cattivo esempio:**```python
def p(d, r, t):
    a = d * ((1 + r / 12) ** (12 * t))
    i = a - d
    return i
```

**Problemi:**
- Nessuna indicazione su quali parametri rappresentano
- Impossibile da comprendere senza documentazione
- Soggetto a errori durante la manutenzione
**Approccio migliore:**```python
def calculate_compound_interest(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    months = 12 * years
    amount = principal * ((1 + monthly_rate) ** months)
    interest = amount - principal
    return interest
```

### Nomi vaghi o generici
**Cattivo esempio:**```python
data = get_data()
result = process_data(data)
temp = transform(result)
final = finalize(temp)
```

**Approccio migliore:**```python
user_records = fetch_user_records()
validated_users = validate_user_data(user_records)
enriched_users = add_user_preferences(validated_users)
user_profiles = build_user_profiles(enriched_users)
```

### Nomi fuorvianti
**Cattivo esempio:**```python
def get_users():
    # Actually modifies database, doesn't just "get"
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

**Approccio migliore:**```python
def update_user_last_login_and_fetch():
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

### Denominazione delle migliori pratiche
1. **Utilizza nomi che rivelino intenzioni**: i nomi dovrebbero spiegare perché qualcosa esiste
2. **Evita la disinformazione**: non utilizzare nomi che possano fuorviare il comportamento
3. **Fai distinzioni significative**: evita parole ridondanti o prive di significato
4. **Usa nomi pronunciabili**: dovrai parlare di questo codice
5. **Utilizza nomi ricercabili**: evita singole lettere e numeri magici
6. **Spiegati nel codice**: riduci la necessità di commenti attraverso una buona denominazione
---

##Codice Spaghetti
Il codice spaghetti si riferisce a codice sorgente non strutturato e difficile da mantenere con un flusso di controllo intricato.
### Nidificazione eccessiva
**Cattivo esempio:**```python
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

**Approccio migliore:**```python
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

### Funzioni lunghe
**Cattivo esempio:**```python
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

**Approccio migliore:**```python
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

### Modelli simili a Goto
**Cattivo esempio:**```python
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

**Approccio migliore:**```python
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

## Dipendenze circolari
Le dipendenze circolari si verificano quando i moduli dipendono l'uno dall'altro direttamente o indirettamente, creando cicli.
### Dipendenze circolari dirette
**Cattivo esempio:**```python
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

**Perché non va bene:**
- Importa errori in fase di esecuzione
- Impossibile importare entrambi i moduli in modo indipendente
- Il codice non può essere testato isolatamente
**Soluzione: estrarre l'interfaccia condivisa**```python
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

### Dipendenze circolari indirette
**Cattivo esempio:**```
module_a -> module_b -> module_c -> module_a
```

**Soluzione: inversione delle dipendenze**```python
# Define interfaces/protocols that modules depend on
# Modules implement interfaces rather than depending on concrete implementations
```

---

## Documentazione scarsa
Una documentazione scarsa aumenta i costi di manutenzione, rallenta l’onboarding e crea silos di conoscenza.
### Documentazione mancante
**Cattivo esempio:**```python
def calc(a, b, c):
    x = a * 2 + b
    y = x / c if c != 0 else 1
    return y * 1.15
```

**Approccio migliore:**```python
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

### Documentazione obsoleta
**Cattivo esempio:**```python
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

**Soluzione:** conserva la documentazione vicino al codice e aggiornala durante le revisioni del codice.
### Eccessiva documentazione
**Cattivo esempio:**```python
# Increment i by 1
i += 1

# Check if name equals John
if name == "John":
    # Print greeting
    print("Hello, John!")
```

**Soluzione:** lascia che il codice chiaro parli da solo; documentare perché, non cosa.
---

## Il codice odora
Gli odori di codice sono indicazioni superficiali di problemi più profondi nella progettazione del software.
### Codice duplicato
**Cattivo esempio:**```python
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

**Approccio migliore:**```python
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

### Elenchi di parametri lunghi
**Cattivo esempio:**```python
def create_user(username, password, email, first_name, last_name, 
                phone, address, city, state, zip_code, country,
                birth_date, gender, occupation, company):
    # 15 parameters!
```

**Approccio migliore:**```python
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

## Argomenti correlati
- **Vulnerabilità della sicurezza**: consulta`02_security_vulnerabilities.md`per problemi di codice relativi alla sicurezza
- **Cronologia Git**: consulta`06_git_documentation.md`per le best practice sui messaggi di commit e sul controllo della versione
- **Progettazione API**: consulta`07_api_system_design.md`per i principi di progettazione dell'interfaccia