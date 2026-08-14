---
# Metadata
title: "Number Theory"
description: "Divisibility, primes, modular arithmetic, Euler's theorem, Fermat's little theorem, Chinese Remainder Theorem, and applications to cryptography"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial deep-dive into number theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [number-theory, primes, divisibility, modular-arithmetic, cryptography, euler-theorem, fermat, chinese-remainder-theorem]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Teoria dos Números
A teoria dos números é o estudo dos inteiros – números inteiros e suas propriedades. Gauss a chamou de "a rainha da matemática". Apesar de estudar os objetos mais simples (1, 2, 3, ...), a teoria dos números produz alguns dos problemas mais profundos e difíceis de toda a matemática. Hoje, ele sustenta a criptografia moderna, algoritmos de hash, códigos de correção de erros e geração de números aleatórios.
---

## Divisibilidade e o Algoritmo de Divisão
### Definições Básicas
| Prazo | Definição | Exemplo |
|------|------------|--------|
| **Divide** | uma\| b significa ∃k ∈ ℤ: b = ak | 3\| 12 (já que 12 = 3 × 4) |
| **Divisor** | Um número que divide outro | Divisores de 12: 1, 2, 3, 4, 6, 12 |
| **Múltiplos** | b é um múltiplo de a se a \| b | 15 é um múltiplo de 5 |
| **Quociente** | O resultado da divisão | 17 ÷ 5 = quociente 3 |
| **Restante** | O que resta após a divisão | 17 ÷ 5 = resto 2 |
### O Algoritmo de Divisão
Para quaisquer inteiros a e b com b > 0, existem inteiros únicos q (quociente) e r (resto) tais que:
a = bq + r, onde 0 ≤ r <b
**Exemplo:** 23 = 5 × 4 + 3. Quociente q = 4, resto r = 3.
### Propriedades de Divisibilidade
| Propriedade | Declaração |
|----------|-----------|
| Transitividade | Se um \| b e b \| c, então um \| c |
| Linearidade | Se um \| b e uma \| c, então um \| (bx + cy) para todos os inteiros x, y |
| Comparação | Se um \| b e b > 0, então a ≤ b |
| Trivial | uma\| 0 para todo a; 1\| um para todos; uma\| a para todo a ≠ 0 |
---

## Maior Divisor Comum (GCD)
O **maior divisor comum** de a e b, denotado mdc(a, b), é o maior número inteiro positivo que divide a e b.
### O Algoritmo Euclidiano
O algoritmo clássico mais eficiente para calcular o GCD.
**Informação principal:** mdc(a, b) = mdc(b, a mod b)
**Algoritmo:**```
function gcd(a, b):
    while b ≠ 0:
        t = b
        b = a mod b
        a = t
    return a
```

**Exemplo resolvido:** gcd(252, 105)
- 252 = 105 × 2 + 42 → mdc(105, 42)
- 105 = 42 × 2 + 21 → mdc(42, 21)
- 42 = 21 × 2 + 0 → mdc(21, 0)
- Resultado: mdc(252, 105) = 21
| Propriedade | Valor |
|----------|-------|
| Complexidade de tempo | O(log(min(a, b))) |
| Complexidade espacial | O(1) iterativo |
### Identidade de Bézout
Para quaisquer inteiros a, b, existem inteiros x, y tais que:
machado + por = mdc (a, b)
**Algoritmo Euclidiano Estendido** calcula mdc(a, b) e os coeficientes x, y simultaneamente.
**Exemplo resolvido:** Encontre x, y tal que 252x + 105y = 21.
- Substituição reversa do algoritmo euclidiano:
  - 21 = 105 − 42 × 2
  - 42 = 252 − 105 × 2
  - 21 = 105 − (252 − 105 × 2) × 2 = 105 × 5 − 252 × 2
- Então x = −2, y = 5. Verifique: 252(−2) + 105(5) = −504 + 525 = 21.
### Principais propriedades do GCD
| Propriedade | Declaração |
|----------|-----------|
| mdc(a, 0) | = uma |
| mdc(a, 1) | = 1 (a e 1 são sempre primos) |
| mdc(a, b) = mdc(b, a) | Comutativo |
| mdc(a, b) = mdc(a, b + ka) | Adicionar múltiplos não altera o GCD |
| mdc(ca,cb) | = c · mdc(a, b) |
| Coprime | mdc(a, b) = 1 significa que a e b não compartilham fatores comuns |
---

## Números Primos
Um **prime** é um número inteiro maior que 1 cujos únicos divisores positivos são 1 e ele mesmo.
### Propriedades Fundamentais
| Propriedade | Declaração |
|----------|-----------|
| **Teorema Fundamental da Aritmética** | Todo número inteiro n > 1 possui uma fatoração primária única |
| **Infinitude de primos** | Existem infinitos números primos (Euclides, ~300 AC) |
| **Teorema dos números primos** | O número de primos ≤ n é aproximadamente n / ln(n) |
| ** Postulado de Bertrand ** | Para cada n > 1, existe um primo p com n < p < 2n |
### Os primeiros primos
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97...

### Fatoração Primária
Todo número inteiro n > 1 pode ser escrito exclusivamente como:
n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ
onde p₁ < p₂ < ... < pₖ são primos e aᵢ ≥ 1.
**Exemplos:**
- 60 = 2² × 3 × 5
- 360 = 2³ × 3² × 5
- 1001 = 7 × 11 × 13
**Usando fatoração para calcular GCD e LCM:**
- mdc(a, b) = produto de potências mínimas de números primos compartilhados
- lcm(a, b) = produto das potências máximas de todos os números primos
**Exemplo:** a = 12 = 2² × 3, b = 18 = 2 × 3²
- mdc(12, 18) = 2¹ × 3¹ = 6
- lcm(12, 18) = 2² × 3² = 36
### Peneira de Eratóstenes
O algoritmo clássico para encontrar todos os primos até um limite N.
| Propriedade | Valor |
|----------|-------|
| Complexidade de tempo | SOBRE log log N) |
| Complexidade espacial | SOBRE(N) |
**Algoritmo:**
1. Liste todos os inteiros de 2 a N.
2. Comece com p = 2. Risque todos os múltiplos de p (começando em p²).
3. Encontre o próximo número não cruzado> p. Defina p para esse número.
4. Repita até p² > N. Todos os números não cruzados são primos.
### Teste de Primalidade
| Método | Tipo | Tempo | Caso de uso |
|--------|------|------|----------|
| Divisão experimental | Determinístico | O(√n) | Números pequenos |
| Teste Fermat | Probabilístico | OK(klog²n) | Triagem rápida |
| Miller-Rabin | Probabilístico | OK(klog²n) | Finalidade geral |
| AKS | Determinístico | O(log⁶n) | Importância teórica |
**Teste de primalidade de Fermat:** Se p é primo e mdc(a, p) = 1, então aᵖ⁻¹ ≡ 1 (mod p). Se isso falhar para algum a, então p é definitivamente composto. Se passar por muitos valores aleatórios de a, p provavelmente é primo.
**Advertência:** Os números de Carmichael (por exemplo, 561) passam no teste de Fermat para todas as bases coprimas, mas são compostos. Miller-Rabin evita esse problema.
---

## Aritmética Modular
A aritmética modular estuda números inteiros em "wraparound" - aritmética em um mostrador de relógio.
### Relações de Congruência
a ≡ b (mod n) significa n | (a - b), ou seja, aeb deixam o mesmo resto quando divididos por n.
### Propriedades Aritméticas
| Operação | Regra |
|-----------|------|
| Adição | (a + b) mod n = ((a mod n) + (b mod n)) mod n |
| Multiplicação | (a × b) mod n = ((a mod n) × (b mod n)) mod n |
| Exponenciação | aᵇ mod n pode ser calculado eficientemente por quadraturas repetidas |
| Negação | (−a) mod n = n − (a mod n) |
### Exponenciação Modular
Calculando um mod n eficientemente usando **quadratura repetida**:
**Exemplo resolvido:** 3¹³ mod 7
- 13 em binário: 1101
- 3¹ = 3 mod 7 = 3
- 3² = 9 módulo 7 = 2
- 3⁴ = 4 mod 7 = 4
- 3⁸ = 16 módulo 7 = 2
- 3¹³ = 3⁸ × 3⁴ × 3¹ = 2 × 4 × 3 = 24 mod 7 = 3
| Propriedade | Valor |
|----------|-------|
| Complexidade de tempo | O(log b · log² n) |
| Complexidade espacial | O(1) |
### Função Tociente de Euler
φ(n) conta os inteiros de 1 a n que são coprimos com n.
| n | φ(n) | Inteiros coprimos |
|---|------|---|
| 1 | 1 | {1} |
| 2 | 1 | {1} |
| 6 | 2 | {1, 5} |
| 7 | 6 | {1, 2, 3, 4, 5, 6} (7 é primo) |
| 10 | 4 | {1, 3, 7, 9} |
| 12 | 4 | {1, 5, 7, 11} |
**Fórmulas:**
- Se p for primo: φ(p) = p − 1
- Se p for primo: φ(pᵏ) = pᵏ − pᵏ⁻¹ = pᵏ⁻¹(p − 1)
- Se mdc(m, n) = 1: φ(mn) = φ(m) · φ(n) (multiplicatividade)
- Geral: φ(n) = n · Π_{p|n} (1 − 1/p) onde o produto é sobre fatores primos distintos de n
---

## Teoremas Chave
### Pequeno Teorema de Fermat
Se p é primo e mdc(a, p) = 1, então:
aᵖ⁻¹ ≡ 1 (mod p)
**Corolário (para todo a):** aᵖ ≡ a (mod p)
**Usar:** Inverso modular rápido quando o módulo é primo: a⁻¹ ≡ aᵖ⁻² (mod p)
**Exemplo resolvido:** Encontre 3⁻¹ mod 7.
- Por Fermat: 3⁻¹ ≡ 3⁵ (mod 7)
- 3² = 9 ≡ 2 (mod 7)
- 3⁴ = 4 (modificação 7)
- 3⁵ = 3⁴ × 3 = 4 × 3 = 12 ≡ 5 (mod 7)
- Verifique: 3 × 5 = 15 ≡ 1 (mod 7).
### Teorema de Euler (Generalização de Fermat)
Se mdc(a, n) = 1, então:
uma^φ(n) ≡ 1 (mod n)
Isso generaliza o Pequeno Teorema de Fermat de números primos para qualquer módulo.
### Teorema do Resto Chinês (CRT)
Se m₁, m₂, ..., mₖ são primos entre pares, o sistema:
x ≡ a₁ (mod m₁)
x ≡ a₂ (mod m₂)
...
x ≡ aₖ (mod mₖ)
tem uma solução única módulo M = m₁ · m₂ · ... · mₖ.
**Exemplo resolvido:** Resolva x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7).
- M = 3 × 5 × 7 = 105
- M₁ = 105/3 = 35; M₂ = 105/5 = 21; M₃ = 105/7 = 15
- Encontre inversos: 35y₁ ≡ 1 (mod 3) → 2y₁ ≡ 1 → y₁ = 2
  21y₂ ≡ 1 (mod 5) → y₂ ≡ 1 (mod 5) → y₂ = 1
  15y₃ ≡ 1 (mod 7) → y₃ ≡ 1 (mod 7) → y₃ = 1
- x = 2·35·2 + 3·21·1 + 2·15·1 = 140 + 63 + 30 = 233
-x ≡ 233 mod 105 = 23
- Verifique: 23 mod 3 = 2, 23 mod 5 = 3, 23 mod 7 = 2.
### Teorema de Wilson
(p − 1)! ≡ −1 (mod p) se e somente se p for primo.
Principalmente de interesse teórico - não é prático para testes de primalidade, uma vez que calcular fatoriais é caro.
### Resíduos Quadráticos
Um inteiro a é um **resíduo quadrático mod n** se x² ≡ a (mod n) tem uma solução.
**Critério de Euler:** a é um resíduo quadrático mod prime p iff a^((p−1)/2) ≡ 1 (mod p).
**Símbolo da legenda:** (a/p) = a^((p−1)/2) mod p, dando +1, −1 ou 0.
**Reciprocidade quadrática** (Gauss): Para primos ímpares distintos p, q:
(p/q)(q/p) = (−1)^((p−1)/2 · (q−1)/2)
Este teorema profundo conecta resíduos quadráticos entre diferentes primos e tem oito leis suplementares que tratam dos casos p = 2.
---

## Aplicações para criptografia
### Criptosistema RSA
O sistema criptográfico de chave pública mais amplamente utilizado, baseado na dificuldade de fatorar números inteiros grandes.
**Configuração:**
1. Escolha dois números primos grandes p, q (normalmente com mais de 1024 bits cada)
2. Calcule n = pq e φ(n) = (p−1)(q−1)
3. Escolha e tal que 1 < e < φ(n) e mdc(e, φ(n)) = 1 (comum: e = 65537)
4. Calcule d ≡ e⁻¹ (mod φ(n)) usando o Algoritmo Euclidiano Estendido
5. **Chave pública:** (n, e). **Chave privada:** (n, d)
**Criptografia:** c = mᵉ mod n (onde m é a mensagem de texto simples)
**Descriptografia:** m = cᵈ mod n
**Por que funciona:** cᵈ = m^(ed) ≡ m (mod n) pelo teorema de Euler, já que ed ≡ 1 (mod φ(n)).
**Segurança:** Fatorar n em peq é computacionalmente inviável para n grandes (mais de 2.048 bits). Sem p e q, um invasor não pode calcular φ(n) e, portanto, não pode encontrar d.
### Troca de chaves Diffie-Hellman
Permite que duas partes estabeleçam um segredo compartilhado em um canal inseguro.
**Configuração:** Combine um número primo grande p e um gerador g (mod p).
**Protocolo:**
1. Alice escolhe o segredo a e envia A = gᵃ mod p para Bob
2. Bob escolhe o segredo b, envia B = gᵇ mod p para Alice
3. Alice calcula s = Bᵃ mod p = gᵃᵇ mod p
4. Bob calcula s = Aᵇ mod p = gᵃᵇ mod p
5. Ambos compartilham o segredo s = gᵃᵇ mod p
**Segurança:** Com base na dificuldade do **problema do logaritmo discreto** — encontrar a de gᵃ mod p.
### Funções Hash e Teoria dos Números
Boas funções hash usam aritmética modular para distribuir chaves uniformemente:
- **Hashing multiplicativo:** h(k) = (k · A) mod m, onde A ≈ m · (√5 − 1) / 2 (proporção áurea)
- **Hashing universal:** h(k) = ((ak + b) mod p) mod m, onde p é primo, a, b são aleatórios
---

## Relevância para aprendizado de máquina e ciência de dados
| Conceito de Teoria dos Números | Aplicação |
|----------------------|------------|
| Aritmética modular | Hashing (tabelas hash, mapas hash), geração de números aleatórios |
| Números primos | Dimensionamento de tabelas hash (use tamanhos de tabelas principais para reduzir colisões) |
| Algoritmo GCD/Euclidiano | Aritmética racional, simplificando frações em probabilidade |
| Exponenciação modular | Segurança criptográfica para modelo de ML veiculado em HTTPS |
| Tociente de Euler | Geração de chave RSA, entendendo garantias criptográficas |
| Teorema do Resto Chinês | Computação distribuída, aritmética modular paralela |
| Teste de primalidade | Gerando números primos para operações criptográficas |
| Resíduos quadráticos | Problema de residuosidade quadrática em criptografia avançada |
| Campos finitos (GF(p), GF(2ᵏ)) | Códigos de correção de erros, códigos Reed-Solomon, criptografia AES |
---

## Resumo
| Tópico | Ideia Central | Resultado chave |
|-------|-----------|-----------|
| Divisibilidade | Divisão com resto | Algoritmo de divisão: a = bq + r |
| GCD | Maior fator compartilhado | Algoritmo euclidiano: O(log n) |
| Primos | Átomos dos inteiros | Teorema Fundamental da Aritmética (fatoração única) |
| Aritmética Modular | Aritmética envolvente | Classes de congruência, exponenciação modular |
| Tociente de Euler | Contando inteiros coprimos | φ(n) = n · Π(1 − 1/p) |
| Pequeno Teorema de Fermat | Atalho do módulo principal | aᵖ⁻¹ ≡ 1 (mod p) |
| Teorema de Euler | Fermat generalizado | uma^φ(n) ≡ 1 (mod n) |
| Teorema do Resto Chinês | Combinando sistemas modulares | Produto mod de solução exclusiva de módulos coprime |
| Criptografia | Problemas difíceis de teoria dos números | RSA (factoring), Diffie-Hellman (log discreto) |
A teoria dos números transforma questões simples sobre números inteiros em matemática profunda com aplicações práticas profundas. Cada conexão segura da web, mensagem criptografada e assinatura digital depende de resultados da teoria dos números descobertos séculos antes da existência dos computadores. Para cientistas de dados e engenheiros de ML, a compreensão da teoria dos números fornece informações sobre hashing, geração de números aleatórios e a infraestrutura criptográfica que protege os dados em trânsito e em repouso.