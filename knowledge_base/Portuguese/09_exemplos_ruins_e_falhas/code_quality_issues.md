# Problemas de Qualidade de Código

Este documento consolida problemas comuns de qualidade de código, incluindo nomes ruins, documentação fraca, spaghetti code, dependências circulares e outros problemas de manutenção.

---

## Nomes de variáveis ruins

Nomes ruins tornam o código mais difícil de ler, entender e manter. Bons nomes funcionam como documentação e reduzem a carga cognitiva.

### Nomes de uma letra (exceto contadores de laço)

**Exemplo ruim:**
```python
def p(d, r, t):
    a = d * ((1 + r / 12) ** (12 * t))
    i = a - d
    return i
```

**Problemas:**
- não indica o que os parâmetros representam
- impossível entender sem documentação
- propenso a erros durante a manutenção

**Abordagem melhor:**
```python
def calculate_compound_interest(principal, annual_rate, years):
    monthly_rate = annual_rate / 12
    months = 12 * years
    amount = principal * ((1 + monthly_rate) ** months)
    interest = amount - principal
    return interest
```

### Nomes vagos ou genéricos

**Exemplo ruim:**
```python
data = get_data()
result = process_data(data)
temp = transform(result)
final = finalize(temp)
```

**Abordagem melhor:**
```python
user_records = fetch_user_records()
validated_users = validate_user_data(user_records)
enriched_users = add_user_preferences(validated_users)
user_profiles = build_user_profiles(enriched_users)
```

### Nomes enganosos

**Exemplo ruim:**
```python
def get_users():
    # Na verdade altera o banco, não apenas "obtém"
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

**Abordagem melhor:**
```python
def update_user_last_login_and_fetch():
    users = db.query("SELECT * FROM users")
    for user in users:
        user.last_login = now()
        user.save()
    return users
```

### Boas práticas de nomenclatura
1. **Use nomes que revelem a intenção**
2. **Evite desinformação**
3. **Faça distinções significativas**
4. **Use nomes pronunciáveis**
5. **Use nomes pesquisáveis**
6. **Explique no código**: reduza a necessidade de comentários com bons nomes

---

## Spaghetti code

Spaghetti code é um código desestruturado e difícil de manter, com fluxo de controle emaranhado.

### Aninhamento excessivo

**Exemplo ruim:**
```python
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

**Abordagem melhor:**
```python
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

**Exemplo ruim:**
```python
def handle_request(request):
    # 200 linhas de código fazendo tudo:
    # - analisar a requisição
    # - validar entrada
    # - autenticar usuário
    # - consultar banco
    # - processar lógica de negócio
    # - formatar resposta
    # - registrar atividade
    # - enviar notificações
    # ... tudo em uma função
```

**Abordagem melhor:**
```python
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

### Padrões semelhantes a goto

**Exemplo ruim:**
```python
def complex_workflow():
    step = 1
    while True:
        if step == 1:
            # faz algo
            step = 2
        elif step == 2:
            # faz outra coisa
            if condition:
                step = 5
            else:
                step = 3
        elif step == 3:
            # mais lógica
            step = 1  # volta!
        # ... continua por muitos passos
```

**Abordagem melhor:**
```python
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

## Dependências circulares

Dependências circulares ocorrem quando módulos dependem uns dos outros direta ou indiretamente, criando ciclos.

### Dependências circulares diretas

**Exemplo ruim:**
```python
# module_a.py
from module_b import process_data

def handle_request(data):
    return process_data(data)

# module_b.py
from module_a import handle_request  # CIRCULAR!

def process_data(data):
    # precisa chamar de volta module_a
    return handle_request(transform(data))
```

**Por que é ruim:**
- erros de importação em tempo de execução
- impossível importar qualquer módulo de forma independente
- não dá para testar isoladamente

**Solução: extrair interface compartilhada**
```python
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
    # processa sem chamar de volta
    return transform(data)
```

### Dependências circulares indiretas

**Exemplo ruim:**
```
module_a -> module_b -> module_c -> module_a
```

**Solução: inversão de dependência**
```python
# Defina interfaces/protocolos dos quais os módulos dependem
# Os módulos implementam interfaces em vez de depender de implementações concretas
```

---

## Documentação ruim

Documentação ruim aumenta custos de manutenção, atrasa o onboarding e cria silos de conhecimento.

### Documentação ausente

**Exemplo ruim:**
```python
def calc(a, b, c):
    x = a * 2 + b
    y = x / c if c != 0 else 1
    return y * 1.15
```

**Abordagem melhor:**
```python
def calculate_final_price(base_price: float, tax_amount: float, discount_factor: float) -> float:
    """
    Calcula o preço final após aplicar imposto e desconto.

    Args:
        base_price: preço original antes dos ajustes
        tax_amount: valor do imposto a adicionar
        discount_factor: multiplicador do desconto (ex.: 0.85 para 15% de desconto)

    Returns:
        Preço final arredondado para 2 casas decimais

    Raises:
        ValueError: se discount_factor for negativo ou maior que 1
    """
    if not 0 <= discount_factor <= 1:
        raise ValueError("discount_factor must be between 0 and 1")

    subtotal = base_price * 2 + tax_amount
    discounted = subtotal / discount_factor if discount_factor != 0 else subtotal
    return round(discounted * 1.15, 2)
```

### Documentação desatualizada

**Exemplo ruim:**
```python
def process_items(items):
    """
    Processa até 100 itens.
    Retorna uma lista de itens processados.
    """
    # Agora lida com itens ilimitados com paginação
    # Retorna um generator em vez de lista
    # Adicionou tratamento de erros e logging
    ...
```

**Solução:** mantenha a documentação próxima ao código e atualize-a durante revisões.

### Sobre-documentação

**Exemplo ruim:**
```python
# Incrementa i em 1
i += 1

# Verifica se o nome é John
if name == "John":
    # Imprime saudação
    print("Hello, John!")
```

**Solução:** deixe o código claro falar por si; documente o porquê, não o quê.

---

## Code smells

Code smells são indícios superficiais de problemas mais profundos de design de software.

### Código duplicado

**Exemplo ruim:**
```python
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

**Abordagem melhor:**
```python
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

### Listas longas de parâmetros

**Exemplo ruim:**
```python
def create_user(username, password, email, first_name, last_name, 
                phone, address, city, state, zip_code, country,
                birth_date, gender, occupation, company):
    # 15 parâmetros!
```

**Abordagem melhor:**
```python
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
    # Limpo e extensível
```

## Tópicos relacionados
- **Vulnerabilidades de segurança**: veja `02_security_vulnerabilities.md` para problemas de código relacionados à segurança
- **Histórico Git**: veja `06_git_documentation.md` para boas práticas de commit e controle de versão
- **Design de API**: veja `07_api_system_design.md` para princípios de design de interface
