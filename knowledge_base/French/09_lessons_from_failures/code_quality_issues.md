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
# Problèmes de qualité du code
Ce document consolide les problèmes courants de qualité du code, notamment les mauvais noms de variables, la mauvaise documentation, le code spaghetti, les dépendances circulaires et d'autres problèmes de maintenabilité.
---

## Mauvais noms de variables
Une mauvaise dénomination des variables rend le code plus difficile à lire, à comprendre et à maintenir. Les bons noms servent de documentation et réduisent la charge cognitive.
### Noms d'une seule lettre (sauf les compteurs de boucles)
**Mauvais exemple :**```python
def p(d, r, t):
    a = d * ((1 + r / 12) ** (12 * t))
    i = a - d
    return i
```

**Problèmes :**
- Aucune indication sur ce que représentent les paramètres
- Impossible à comprendre sans documentation
- Sujet aux erreurs pendant la maintenance
**Meilleure approche :**```python
def calculate_compound_interest(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    months = 12 * years
    amount = principal * ((1 + monthly_rate) ** months)
    interest = amount - principal
    return interest
```

### Noms vagues ou génériques
**Mauvais exemple :**```python
data = get_data()
result = process_data(data)
temp = transform(result)
final = finalize(temp)
```

**Meilleure approche :**```python
user_records = fetch_user_records()
validated_users = validate_user_data(user_records)
enriched_users = add_user_preferences(validated_users)
user_profiles = build_user_profiles(enriched_users)
```

### Noms trompeurs
**Mauvais exemple :**```python
def get_users():
    # Actually modifies database, doesn't just "get"
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

**Meilleure approche :**```python
def update_user_last_login_and_fetch():
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

### Nommer les meilleures pratiques
1. **Utilisez des noms révélateurs d'intention** : les noms doivent expliquer pourquoi quelque chose existe
2. **Évitez la désinformation** : n'utilisez pas de noms qui induisent en erreur sur le comportement
3. **Faites des distinctions significatives** : évitez les mots redondants ou dénués de sens
4. **Utilisez des noms prononçables** : vous devrez parler de ce code
5. **Utilisez des noms consultables** : évitez les lettres simples et les chiffres magiques
6. **Expliquez-vous dans le code** : réduisez le besoin de commentaires grâce à une bonne dénomination
---

## Code Spaghetti
Le code spaghetti fait référence à un code source non structuré et difficile à maintenir avec un flux de contrôle enchevêtré.
### Nidification excessive
**Mauvais exemple :**```python
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

**Meilleure approche :**```python
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

### Fonctions longues
**Mauvais exemple :**```python
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

**Meilleure approche :**```python
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

### Modèles de type Goto
**Mauvais exemple :**```python
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

**Meilleure approche :**```python
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

## Dépendances circulaires
Les dépendances circulaires se produisent lorsque les modules dépendent les uns des autres directement ou indirectement, créant des cycles.
### Dépendances circulaires directes
**Mauvais exemple :**```python
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

**Pourquoi c'est mauvais :**
- Erreurs d'importation au moment de l'exécution
- Impossible d'importer l'un ou l'autre module indépendamment
- Le code ne peut pas être testé isolément
**Solution : Extraire l'interface partagée**```python
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

### Dépendances circulaires indirectes
**Mauvais exemple :**```
module_a -> module_b -> module_c -> module_a
```

**Solution : Inversion des dépendances**```python
# Define interfaces/protocols that modules depend on
# Modules implement interfaces rather than depending on concrete implementations
```

---

## Mauvaise documentation
Une mauvaise documentation augmente les coûts de maintenance, ralentit l’intégration et crée des silos de connaissances.
### Documentation manquante
**Mauvais exemple :**```python
def calc(a, b, c):
    x = a * 2 + b
    y = x / c if c != 0 else 1
    return y * 1.15
```

**Meilleure approche :**```python
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

### Documentation obsolète
**Mauvais exemple :**```python
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

**Solution :** Conservez la documentation à proximité du code et mettez-la à jour lors des révisions de code.
### Sur-documentation
**Mauvais exemple :**```python
# Increment i by 1
i += 1

# Check if name equals John
if name == "John":
    # Print greeting
    print("Hello, John!")
```

**Solution :** Laissez le code clair parler de lui-même ; documentez pourquoi, pas quoi.
---

## Odeurs de code
Les odeurs de code sont des indications superficielles de problèmes plus profonds dans la conception de logiciels.
### Code dupliqué
**Mauvais exemple :**```python
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

**Meilleure approche :**```python
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

### Longues listes de paramètres
**Mauvais exemple :**```python
def create_user(username, password, email, first_name, last_name, 
                phone, address, city, state, zip_code, country,
                birth_date, gender, occupation, company):
    # 15 parameters!
```

**Meilleure approche :**```python
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

## Sujets connexes
- **Fulnérabilités de sécurité** : voir`02_security_vulnerabilities.md`pour les problèmes de code liés à la sécurité
- **Historique Git** : voir`06_git_documentation.md`pour les messages de validation et les meilleures pratiques en matière de contrôle de version
- **Conception API** : voir`07_api_system_design.md`pour les principes de conception d'interface.