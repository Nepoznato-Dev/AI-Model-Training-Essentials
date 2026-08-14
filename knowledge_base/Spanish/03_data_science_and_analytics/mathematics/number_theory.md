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

# Teoría de números
La teoría de números es el estudio de los números enteros: números enteros y sus propiedades. Gauss la llamó "la reina de las matemáticas". A pesar de estudiar los objetos más simples (1, 2, 3,...), la teoría de números produce algunos de los problemas más profundos y difíciles de todas las matemáticas. Hoy en día, sustenta la criptografía moderna, los algoritmos hash, los códigos de corrección de errores y la generación de números aleatorios.
---

## Divisibilidad y algoritmo de división
### Definiciones principales
| Término | Definición | Ejemplo |
|------|------------|---------|
| **Divide** | un \| b significa ∃k ∈ ℤ: b = ak | 3 \| 12 (ya que 12 = 3 × 4) |
| **Divisor** | Un número que divide a otro | Divisores de 12: 1, 2, 3, 4, 6, 12 |
| **Múltiples** | b es múltiplo de a si a \| segundo | 15 es múltiplo de 5 |
| **Cociente** | El resultado de la división | 17 ÷ 5 = cociente 3 |
| **Resto** | Lo que queda después de la división | 17 ÷ 5 = resto 2 |
### El algoritmo de división
Para cualquier número entero a y b con b > 0, existen números enteros únicos q (cociente) y r (resto) tales que:
a = bq + r, donde 0 ≤ r < b
**Ejemplo:** 23 = 5 × 4 + 3. Cociente q = 4, resto r = 3.
### Propiedades de la divisibilidad
| Propiedad | Declaración |
|----------|-----------|
| Transitividad | Si un \| b y b \| c, entonces a \| c |
| Linealidad | Si un \| b y a \| c, entonces a \| (bx + cy) para todos los números enteros x, y |
| Comparación | Si un \| b y b > 0, entonces a ≤ b |
| trivial | un \| 0 para todo a; 1 \| a para todos a; un \| a para todo a ≠ 0 |
---

## Máximo común divisor (MCD)
El **máximo común divisor** de a y b, denotado mcd(a, b), es el mayor entero positivo que divide a a y b.
### El algoritmo euclidiano
El algoritmo clásico más eficiente para calcular el MCD.
**Información clave:** mcd(a, b) = mcd(b, a mod b)
**Algoritmo:**```
function gcd(a, b):
    while b ≠ 0:
        t = b
        b = a mod b
        a = t
    return a
```

**Ejemplo resuelto:** gcd(252, 105)
- 252 = 105 × 2 + 42 → mcd(105, 42)
- 105 = 42 × 2 + 21 → mcd(42, 21)
- 42 = 21 × 2 + 0 → mcd(21, 0)
- Resultado: mcd(252, 105) = 21
| Propiedad | Valor |
|----------|-------|
| Complejidad del tiempo | O(log(mín(a, b))) |
| Complejidad espacial | O(1) iterativo |
### La identidad de Bézout
Para cualquier número entero a, b, existen números enteros x, y tales que:
hacha + por = mcd(a, b)
**Algoritmo euclidiano extendido** calcula mcd(a, b) y los coeficientes x, y simultáneamente.
**Ejemplo resuelto:** Encuentra x, y tal que 252x + 105y = 21.
- Sustitución hacia atrás del algoritmo euclidiano:
  - 21 = 105 - 42 × 2
  - 42 = 252 - 105 × 2
  - 21 = 105 − (252 − 105 × 2) × 2 = 105 × 5 − 252 × 2
- Entonces x = −2, y = 5. Comprueba: 252(−2) + 105(5) = −504 + 525 = 21.
### Propiedades clave de GCD
| Propiedad | Declaración |
|----------|-----------|
| mcd(a, 0) | = un |
| mcd(a, 1) | = 1 (a y 1 son siempre coprimos) |
| mcd(a, b) = mcd(b, a) | Conmutativo |
| mcd(a, b) = mcd(a, b + ka) | Agregar múltiplos no cambia GCD |
| mcd(ca,cb) | = c · mcd(a, b) |
| Coprime | mcd(a, b) = 1 significa que a y b no comparten factores comunes |
---

## Números primos
Un **primo** es un número entero mayor que 1 cuyos únicos divisores positivos son 1 y él mismo.
### Propiedades fundamentales
| Propiedad | Declaración |
|----------|-----------|
| **Teorema fundamental de la aritmética** | Todo número entero n > 1 tiene una factorización prima única |
| **Infinidad de números primos** | Hay infinitos números primos (Euclides, ~300 a.C.) |
| **Teorema de los números primos** | El número de primos ≤ n es aproximadamente n / ln(n) |
| **Postulado de Bertrand** | Para cada n > 1, existe un primo p con n < p < 2n |
### Los primeros números primos
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97...

### Factorización prima
Todo número entero n > 1 se puede escribir de forma única como:
n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ
donde p₁ < p₂ < ... < pₖ son primos y aᵢ ≥ 1.
**Ejemplos:**
- 60 = 2² × 3 × 5
- 360 = 2³ × 3² × 5
- 1001 = 7 × 11 × 13
**Uso de factorización para calcular MCD y MCM:**
- mcd(a, b) = producto de potencias mínimas de números primos compartidos
- mcm(a, b) = producto de las potencias máximas de todos los números primos
**Ejemplo:** a = 12 = 2² × 3, b = 18 = 2 × 3²
- mcd(12, 18) = 2¹ × 3¹ = 6
- mcm(12, 18) = 2² × 3² = 36
### Tamiz de Eratóstenes
El algoritmo clásico para encontrar todos los números primos hasta un límite N.
| Propiedad | Valor |
|----------|-------|
| Complejidad del tiempo | O(norte registro registro norte) |
| Complejidad espacial | O (norte) |
**Algoritmo:**
1. Enumere todos los números enteros del 2 al N.
2. Comience con p = 2. Tache todos los múltiplos de p (comenzando desde p²).
3. Encuentra el siguiente número sin cruzar > p. Establezca p en ese número.
4. Repita hasta que p² > N. Todos los números no cruzados son primos.
### Prueba de primalidad
| Método | Tipo | Hora | Caso de uso |
|--------|------|------|----------|
| División de prueba | Determinista | O(√norte) | Números pequeños |
| Prueba de Fermat | Probabilístico | O(k log² n) | Detección rápida |
| Miller-Rabin | Probabilístico | O(k log² n) | Propósito general |
| AKS | Determinista | O(log⁶ norte) | Importancia teórica |
**Prueba de primalidad de Fermat:** Si p es primo y mcd(a, p) = 1, entonces aᵖ⁻¹ ≡ 1 (mod p). Si esto falla para algún a, entonces p es definitivamente compuesto. Si pasa por muchos valores aleatorios de a, p probablemente sea primo.
**Advertencia:** Los números de Carmichael (p. ej., 561) pasan la prueba de Fermat para todas las bases coprimes, pero son compuestos. Miller-Rabin evita esta cuestión.
---

## Aritmética modular
La aritmética modular estudia números enteros bajo "aritmética envolvente": aritmética en la esfera de un reloj.
### Relaciones de congruencia
a ≡ b (mod n) significa n | (a − b), es decir, a y b dejan el mismo resto cuando se dividen por n.
### Propiedades aritméticas
| Operación | Regla |
|-----------|--------------|
| Adición | (a + b) mod n = ((a mod n) + (b mod n)) mod n |
| Multiplicación | (a × b) mod n = ((a mod n) × (b mod n)) mod n |
| Exponenciación | aᵇ mod n se puede calcular de manera eficiente elevando al cuadrado repetidamente |
| Negación | (−a) mod n = n − (a mod n) |
### Exponenciación modular
Calcular aᵇ mod n de manera eficiente usando **cuadrados repetidos**:
**Ejemplo resuelto:** 3¹³ mod 7
- 13 en binario: 1101
- 3¹ = 3 mod 7 = 3
- 3² = 9 mod 7 = 2
- 3⁴ = 4 mod 7 = 4
- 3⁸ = 16 mod 7 = 2
- 3¹³ = 3⁸ × 3⁴ × 3¹ = 2 × 4 × 3 = 24 mod 7 = 3
| Propiedad | Valor |
|----------|-------|
| Complejidad del tiempo | O(log b · log² n) |
| Complejidad espacial | O(1) |
### Función Totiente de Euler
φ(n) cuenta los números enteros del 1 al n que son coprimos de n.
| norte | φ(norte) | Enteros coprimos |
|---|------|------------------|
| 1 | 1 | {1} |
| 2 | 1 | {1} |
| 6 | 2 | {1, 5} |
| 7 | 6 | {1, 2, 3, 4, 5, 6} (7 es primo) |
| 10 | 4 | {1, 3, 7, 9} |
| 12 | 4 | {1, 5, 7, 11} |
**Fórmulas:**
- Si p es primo: φ(p) = p − 1
- Si p es primo: φ(pᵏ) = pᵏ − pᵏ⁻¹ = pᵏ⁻¹(p − 1)
- Si mcd(m, n) = 1: φ(mn) = φ(m) · φ(n) (multiplicatividad)
- General: φ(n) = n · Π_{p|n} (1 − 1/p) donde el producto es sobre distintos factores primos de n
---

## Teoremas clave
### El pequeño teorema de Fermat
Si p es primo y mcd(a, p) = 1, entonces:
aᵖ⁻¹ ≡ 1 (mod p)
**Corolario (para todo a):** aᵖ ≡ a (mod p)
**Uso:** Inverso modular rápido cuando el módulo es primo: a⁻¹ ≡ aᵖ⁻² (mod p)
**Ejemplo resuelto:** Encuentra 3⁻¹ mod 7.
- Por Fermat: 3⁻¹ ≡ 3⁵ (mod 7)
- 3² = 9 ≡ 2 (mod 7)
- 3⁴ = 4 (mod 7)
- 3⁵ = 3⁴ × 3 = 4 × 3 = 12 ≡ 5 (mod 7)
- Comprueba: 3 × 5 = 15 ≡ 1 (mod 7).
### Teorema de Euler (Generalización de Fermat)
Si mcd(a, n) = 1, entonces:
a^φ(n) ≡ 1 (mód n)
Esto generaliza el pequeño teorema de Fermat desde números primos hasta cualquier módulo.
### Teorema chino del resto (CRT)
Si m₁, m₂, ..., mₖ son coprimos por pares, el sistema:
x ≡ a₁ (mód m₁)
x ≡ a₂ (mód m₂)
...
x ≡ aₖ (mód mₖ)
tiene una solución única módulo M = m₁ · m₂ · ... · mₖ.
**Ejemplo resuelto:** Resuelve x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7).
- M = 3 × 5 × 7 = 105
- M₁ = 105/3 = 35; M₂ = 105/5 = 21; M₃ = 105/7 = 15
- Encuentra inversas: 35y₁ ≡ 1 (mod 3) → 2y₁ ≡ 1 → y₁ = 2
  21y₂ ≡ 1 (mod 5) → y₂ ≡ 1 (mod 5) → y₂ = 1
  15y₃ ≡ 1 (mod 7) → y₃ ≡ 1 (mod 7) → y₃ = 1
- x = 2·35·2 + 3·21·1 + 2·15·1 = 140 + 63 + 30 = 233
- x ≡ 233 mod 105 = 23
- Comprueba: 23 mod 3 = 2, 23 mod 5 = 3, 23 mod 7 = 2.
### Teorema de Wilson
(p-1)! ≡ −1 (mod p) si y sólo si p es primo.
Principalmente de interés teórico, no práctico para pruebas de primalidad ya que calcular factoriales es costoso.
### Residuos cuadráticos
Un número entero a es un **residuo cuadrático mod n** si x² ≡ a (mod n) tiene solución.
**Criterio de Euler:** a es un residuo cuadrático mod primo p sif a^((p−1)/2) ≡ 1 (mod p).
**Símbolo legendario:** (a/p) = a^((p−1)/2) mod p, lo que da +1, −1 o 0.
**Reciprocidad cuadrática** (Gauss): Para primos impares distintos p, q:
(p/q)(q/p) = (−1)^((p−1)/2 · (q−1)/2)
Este profundo teorema conecta residuos cuadráticos entre diferentes números primos y tiene ocho leyes suplementarias que manejan los casos p = 2.
---

## Aplicaciones a la criptografía
### Criptosistema RSA
El criptosistema de clave pública más utilizado, basado en la dificultad de factorizar números enteros grandes.
**Configuración:**
1. Elija dos números primos grandes p, q (normalmente de más de 1024 bits cada uno)
2. Calcule n = pq y φ(n) = (p−1)(q−1)
3. Elija e tal que 1 < e < φ(n) y mcd(e, φ(n)) = 1 (común: e = 65537)
4. Calcule d ≡ e⁻¹ (mod φ(n)) usando el algoritmo euclidiano extendido
5. **Clave pública:** (n, e). **Clave privada:** (n,d)
**Cifrado:** c = mᵉ mod n (donde m es el mensaje de texto sin formato)
**Descifrado:** m = cᵈ mod n
**Por qué funciona:** cᵈ = m^(ed) ≡ m (mod n) según el teorema de Euler, ya que ed ≡ 1 (mod φ(n)).
**Seguridad:** Factorizar n en p y q es computacionalmente inviable para n grande (más de 2048 bits). Sin p y q, un atacante no puede calcular φ(n) y por tanto no puede encontrar d.
### Intercambio de claves Diffie-Hellman
Permite que dos partes establezcan un secreto compartido a través de un canal inseguro.
**Configuración:** Acuerde un primo grande p y un generador g (mod p).
**Protocolo:**
1. Alice elige el secreto a, envía A = gᵃ mod p a Bob
2. Bob elige el secreto b, envía B = gᵇ mod p a Alice
3. Alice calcula s = Bᵃ mod p = gᵃᵇ mod p
4. Bob calcula s = Aᵇ mod p = gᵃᵇ mod p
5. Ambos comparten el secreto s = gᵃᵇ mod p
**Seguridad:** Basado en la dificultad del **problema de logaritmos discretos**: encontrar a de gᵃ mod p.
### Funciones hash y teoría de números
Las buenas funciones hash utilizan aritmética modular para distribuir claves de manera uniforme:
- **Hashing multiplicativo:** h(k) = (k · A) mod m, donde A ≈ m · (√5 − 1) / 2 (proporción áurea)
- **Hashing universal:** h(k) = ((ak + b) mod p) mod m, donde p es primo, a, b son aleatorios
---

## Relevancia para el aprendizaje automático y la ciencia de datos
| Concepto de teoría de números | Solicitud |
|----------------------|-------------|
| Aritmética modular | Hashing (tablas hash, mapas hash), generación de números aleatorios |
| Números primos | Tamaño de la tabla hash (use tamaños de tabla principales para reducir las colisiones) |
| GCD / Algoritmo euclidiano | Aritmética racional, simplificando fracciones en probabilidad |
| Exponenciación modular | Seguridad criptográfica para el modelo ML que se sirve a través de HTTPS |
| El paciente de Euler | Generación de claves RSA, comprensión de las garantías criptográficas |
| Teorema del resto chino | Computación distribuida, aritmética modular paralela |
| Pruebas de primalidad | Generando números primos para operaciones criptográficas |
| Residuos cuadráticos | Problema de residuosidad cuadrática en criptografía avanzada |
| Campos finitos (GF(p), GF(2ᵏ)) | Códigos de corrección de errores, códigos Reed-Solomon, cifrado AES |
---

## Resumen
| Tema | Idea central | Resultado clave |
|-------|-----------|------------|
| Divisibilidad | División con resto | Algoritmo de división: a = bq + r |
| MCD | Mayor factor compartido | Algoritmo euclidiano: O(log n) |
| Primos | Átomos de los números enteros | Teorema Fundamental de la Aritmética (factorización única) |
| Aritmética modular | Aritmética envolvente | Clases de congruencia, exponenciación modular |
| El paciente de Euler | Contando números enteros coprimos | φ(n) = n · Π(1 − 1/p) |
| El pequeño teorema de Fermat | Atajo del módulo principal | aᵖ⁻¹ ≡ 1 (mod p) |
| Teorema de Euler | Fermat generalizado | a^φ(n) ≡ 1 (mod n) |
| Teorema del resto chino | Combinando sistemas modulares | Producto mod de solución única de módulos coprime |
| Criptografía | Problemas difíciles de teoría de números | RSA (factoring), Diffie-Hellman (registro discreto) |
La teoría de números transforma preguntas simples sobre números enteros en matemáticas profundas con profundas aplicaciones prácticas. Cada conexión web segura, mensaje cifrado y firma digital se basa en resultados de la teoría de números descubiertos siglos antes de que existieran las computadoras. Para los científicos de datos y los ingenieros de ML, comprender la teoría de números proporciona información sobre el hash, la generación de números aleatorios y la infraestructura criptográfica que protege los datos en tránsito y en reposo.