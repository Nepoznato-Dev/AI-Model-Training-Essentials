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

# Problemas de qualidade de código
Este documento consolida problemas comuns de qualidade de código, incluindo nomes de variáveis ​​incorretos, documentação deficiente, código espaguete, dependências circulares e outros problemas de manutenção.
---

## Nomes de variáveis ​​ruins
A má nomenclatura de variáveis ​​torna o código mais difícil de ler, entender e manter. Bons nomes servem como documentação e reduzem a carga cognitiva.
### Nomes de uma única letra (exceto contadores de loop)
**Mau exemplo:**```python
def p(d, r, t):
    a = d * ((1 + r / 12) ** (12 * t))
    i = a - d
    return i
```

**Problemas:**
- Nenhuma indicação de quais parâmetros representam
- Impossível entender sem documentação
- Propenso a erros durante a manutenção
**Melhor abordagem:**```python
def calculate_compound_interest(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    months = 12 * years
    amount = principal * ((1 + monthly_rate) ** months)
    interest = amount - principal
    return interest
```

### Nomes vagos ou genéricos
**Mau exemplo:**```python
data = get_data()
result = process_data(data)
temp = transform(result)
final = finalize(temp)
```

**Melhor abordagem:**```python
user_records = fetch_user_records()
validated_users = validate_user_data(user_records)
enriched_users = add_user_preferences(validated_users)
user_profiles = build_user_profiles(enriched_users)
```

### Nomes enganosos
**Mau exemplo:**```python
def get_users():
    # Actually modifies database, doesn't just "get"
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

**Melhor abordagem:**```python
def update_user_last_login_and_fetch():
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

### Melhores práticas de nomenclatura
1. **Use nomes que revelem intenções**: os nomes devem explicar por que algo existe
2. **Evite desinformação**: não use nomes que enganem o comportamento
3. **Faça distinções significativas**: Evite palavras redundantes ou sem sentido
4. **Use nomes pronunciáveis**: você precisará falar sobre este código
5. **Use nomes pesquisáveis**: Evite letras únicas e números mágicos
6. **Explique-se em código**: Reduza a necessidade de comentários por meio de uma boa nomenclatura
---

## Código Espaguete
Código espaguete refere-se a código-fonte não estruturado e de difícil manutenção, com fluxo de controle emaranhado.
### Aninhamento excessivo
**Mau exemplo:**```python
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

**Melhor abordagem:**```python
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

### Funções longas
**Mau exemplo:**```python
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

**Melhor abordagem:**```python
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

### Padrões semelhantes a Goto
**Mau exemplo:**```python
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

**Melhor abordagem:**```python
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

## Dependências Circulares
As dependências circulares ocorrem quando os módulos dependem uns dos outros direta ou indiretamente, criando ciclos.
### Dependências Circulares Diretas
**Mau exemplo:**```python
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

**Por que é ruim:**
- Erros de importação em tempo de execução
- Impossível importar qualquer módulo de forma independente
- O código não pode ser testado isoladamente
**Solução: extrair interface compartilhada**```python
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

### Dependências Circulares Indiretas
**Mau exemplo:**```
module_a -> module_b -> module_c -> module_a
```

**Solução: Inversão de Dependência**```python
# Define interfaces/protocols that modules depend on
# Modules implement interfaces rather than depending on concrete implementations
```

---

## Documentação deficiente
A documentação deficiente aumenta os custos de manutenção, retarda a integração e cria silos de conhecimento.
### Documentação ausente
**Mau exemplo:**```python
def calc(a, b, c):
    x = a * 2 + b
    y = x / c if c != 0 else 1
    return y * 1.15
```

**Melhor abordagem:**```python
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

### Documentação desatualizada
**Mau exemplo:**```python
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

**Solução:** mantenha a documentação próxima do código e atualize-a durante as revisões de código.
### Excesso de documentação
**Mau exemplo:**```python
# Increment i by 1
i += 1

# Check if name equals John
if name == "John":
    # Print greeting
    print("Hello, John!")
```

**Solução:** Deixe o código claro falar por si; documentar por que, não o quê.
---

## Código cheira
Os cheiros de código são indicações superficiais de problemas mais profundos no design de software.
### Código Duplicado
**Mau exemplo:**```python
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

**Melhor abordagem:**```python
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

### Longas listas de parâmetros
**Mau exemplo:**```python
def create_user(username, password, email, first_name, last_name, 
                phone, address, city, state, zip_code, country,
                birth_date, gender, occupation, company):
    # 15 parameters!
```

**Melhor abordagem:**```python
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

## Tópicos Relacionados
- **Vulnerabilidades de segurança**: consulte`02_security_vulnerabilities.md`para problemas de código relacionados à segurança
- **Histórico do Git**: consulte`06_git_documentation.md`para mensagens de commit e práticas recomendadas de controle de versão
- **Design de API**: consulte`07_api_system_design.md`para princípios de design de interface