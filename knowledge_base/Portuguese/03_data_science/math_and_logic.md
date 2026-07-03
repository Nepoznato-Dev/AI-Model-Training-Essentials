# Matemática e Lógica

## O que é Matemática?

Matemática é o estudo de números, formas, padrões e relações lógicas. Ela é ao mesmo tempo uma ciência e uma linguagem usada para descrever o universo. A matemática se divide em ramos como aritmética, álgebra, geometria, cálculo, estatística e lógica. A matemática é a base da física, da engenharia, da ciência da computação, da economia e de muitas outras áreas.

## Aritmética

A aritmética é o ramo da matemática que lida com operações básicas sobre números. As quatro operações fundamentais são adição (+), subtração (−), multiplicação (×) e divisão (÷). A ordem das operações especifica a sequência em que os cálculos devem ser realizados: Parênteses, Expoentes, Multiplicação e Divisão (da esquerda para a direita), Adição e Subtração (da esquerda para a direita). Isso costuma ser lembrado como **PEMDAS** ou **BODMAS**. Um número primo é um número inteiro maior que 1 que não tem divisores além de 1 e dele mesmo. Os primeiros números primos são 2, 3, 5, 7, 11, 13, 17, 19, 23 e 29.

**Exemplos:**
- Fatoração prima: 84 = 2² × 3 × 7
- Greatest Common Divisor (GCD) de 24 e 36: 12
- Least Common Multiple (LCM) de 4 e 6: 12

## Álgebra

A álgebra usa letras e símbolos para representar números e quantidades em equações e fórmulas. Uma **variável** é um símbolo (geralmente uma letra) que representa uma quantidade desconhecida ou mutável. Uma **equação** afirma que duas expressões são iguais. Resolver uma equação significa encontrar o(s) valor(es) da(s) variável(eis) que tornam a equação verdadeira.

A **fórmula quadrática** resolve equações da forma ax² + bx + c = 0: x = (−b ± √(b²−4ac)) / (2a)


Uma **função** associa cada entrada a exatamente uma saída. Funções comuns incluem:
- Linear: y = mx + b (reta, taxa de variação constante)
- Quadrática: y = ax² + bx + c (parábola, curva)
- Exponencial: y = a × bˣ (crescimento ou decaimento, mudança rápida)
- Logarítmica: y = log_b(x) (inversa da exponencial)

**Conceitos-chave:**
- Domínio: o conjunto de todos os valores de entrada possíveis
- Imagem: o conjunto de todos os valores de saída possíveis
- Inclinação: taxa de variação (m em y = mx + b)
- Intercepto: ponto em que a função cruza o eixo y (b em y = mx + b)

## Geometria

Geometria é o ramo da matemática que estuda formas, tamanhos, posições e propriedades das figuras. Um ponto não tem tamanho; ele representa uma localização. Uma reta se estende infinitamente em ambas as direções. Um segmento de reta tem duas extremidades. Um ângulo é formado por duas semirretas que compartilham um ponto final.

**Regras principais:**
- A soma dos ângulos de um triângulo é sempre 180 graus.
- A soma dos ângulos de um quadrilátero é sempre 360 graus.
- O teorema de Pitágoras: em um triângulo retângulo, a² + b² = c² (onde c é a hipotenusa).
- Circunferência do círculo: 2πr
- Área do círculo: πr²
- Volume da esfera: (4/3)πr³

**π (pi)** é aproximadamente 3,14159 e é a razão entre a circunferência de um círculo e seu diâmetro.

**Formas geométricas comuns:**
- Triângulo: 3 lados, soma dos ângulos igual a 180°
- Quadrado: 4 lados iguais, 4 ângulos retos
- Retângulo: 4 lados, lados opostos iguais, 4 ângulos retos
- Círculo: sem lados, borda curva contínua
- Pentágono: 5 lados, soma dos ângulos igual a 540°
- Hexágono: 6 lados, soma dos ângulos igual a 720°

## Estatística e Probabilidade

Estatística é a ciência de coletar, analisar, interpretar e apresentar dados.

**Medidas de tendência central:**
- **Média** (average): soma de todos os valores dividida pelo número de valores
- **Mediana**: valor central quando os dados estão ordenados (menos sensível a outliers)
- **Moda**: valor que ocorre com maior frequência (pode haver múltiplas modas)

**Medidas de dispersão:**
- **Amplitude**: máximo - mínimo
- **Variância**: média dos desvios quadráticos em relação à média
- **Desvio padrão**: raiz quadrada da variância (nas mesmas unidades dos dados)

Probabilidade mede a chance de um evento ocorrer, variando de 0 (impossível) a 1 (certo). A probabilidade de dois eventos independentes ocorrerem ambos é o produto de suas probabilidades individuais.

**Exemplo:** Probabilidade de sair 6 em um dado justo: 1/6. Probabilidade de sair dois 6 seguidos: (1/6) × (1/6) = 1/36.

## Probabilidade para Computação e ML

Uma **variável aleatória** é uma variável cujo valor depende do resultado de um processo aleatório. Uma **distribuição de probabilidade** descreve a probabilidade de cada resultado.

**Distribuições comuns:**
- **Bernoulli**: único experimento com dois resultados (ex.: cara ou coroa)
- **Binomial**: número de sucessos em n tentativas independentes de Bernoulli
- **Normal (Gaussiana)**: curva em sino, simétrica em torno da média (comum em fenômenos naturais)
- **Poisson**: número de eventos em um intervalo fixo (ex.: emails por hora)

**Valor esperado** é o resultado médio de longo prazo de uma variável aleatória. **Variância** mede a dispersão em torno dessa expectativa.

**Probabilidade condicional** descreve a probabilidade de um evento dado que outro evento ocorreu: P(A|B) = P(A ∩ B) / P(B) [se P(B) > 0].

**Teorema de Bayes** atualiza crenças usando evidências: P(A|B) = P(B|A) × P(A) / P(B).


Em machine learning, a probabilidade sustenta a confiança em classificação, a estimativa de incerteza, métodos bayesianos e muitas funções de perda (como cross-entropy).

## Cálculo

Cálculo é o ramo da matemática que estuda a mudança contínua.

**Cálculo diferencial** lida com taxas de variação e inclinações de curvas, usando **derivadas**. A derivada de uma função f(x) representa a taxa de variação de f em relação a x em um ponto. Notação: f'(x) ou df/dx.

**Derivadas comuns:**
- d/dx [x^n] = n·x^(n−1)
- d/dx [e^x] = e^x
- d/dx [ln(x)] = 1/x
- d/dx [sin(x)] = cos(x)

**Cálculo integral** lida com acúmulo de quantidades e áreas sob curvas, usando **integrais**. A integral representa a área sob a curva entre dois pontos.

O **teorema fundamental do cálculo** conecta diferenciação e integração: diferenciação e integração são operações inversas.

O cálculo foi desenvolvido de forma independente por Isaac Newton e Gottfried Wilhelm Leibniz no século XVII.

## Sistemas Numéricos

- **Números naturais**: 1, 2, 3, 4, ... (números de contagem)
- **Números inteiros não negativos**: 0, 1, 2, 3, ... (números naturais mais zero)
- **Inteiros**: ..., −2, −1, 0, 1, 2, ... (todos os inteiros não negativos e seus negativos)
- **Números racionais**: números expressáveis como p/q, onde p e q são inteiros e q ≠ 0 (ex.: 1/2, 3/4, −5/3)
- **Números irracionais**: não podem ser expressos como fração (ex.: √2, π, e)
- **Números reais**: todos os números racionais e irracionais (a reta numérica)
- **Números imaginários**: envolvem a raiz quadrada de números negativos; i = √(−1)
- **Números complexos**: combinam partes reais e imaginárias (a + bi)

## Lógica e Raciocínio

Lógica é o estudo do raciocínio válido.

**Raciocínio dedutivo** tira conclusões específicas a partir de premissas gerais. Se as premissas forem verdadeiras e o argumento for válido, a conclusão deve ser verdadeira.
- **Exemplo:** Todos os seres humanos são mortais. Sócrates é humano. Logo, Sócrates é mortal.

**Raciocínio indutivo** tira conclusões gerais a partir de observações específicas. Não garante que a conclusão seja verdadeira, mas a torna provável.
- **Exemplo:** Todo cisne que eu vi é branco. Portanto, todos os cisnes são brancos. (Observação: isso é falso; cisnes negros existem!)

**Falácias lógicas comuns (erros de raciocínio):**
- **Ad hominem**: atacar a pessoa em vez do argumento
- **Espantalho**: distorcer um argumento para torná-lo mais fácil de atacar
- **Falsa dicotomia**: apresentar apenas duas opções quando há mais possibilidades
- **Raciocínio circular**: usar a conclusão como premissa
- **Apelo à autoridade**: afirmar que algo é verdadeiro porque uma autoridade disse
- **Falácia post hoc**: presumir que, porque A aconteceu antes de B, A causou B

## Conjuntos

Um **conjunto** é uma coleção de objetos distintos.
- **União** (A ∪ B): todos os elementos de ambos os conjuntos
- **Interseção** (A ∩ B): apenas os elementos comuns aos dois
- **Conjunto vazio** (∅ or {}): não contém elementos
- **Subconjunto** (A ⊆ B): todos os elementos de A também estão em B
- **Diagramas de Venn**: representam visualmente as relações entre conjuntos

A teoria dos conjuntos é a base da matemática e da lógica modernas.

## Binário e Bases Numéricas

Computadores representam dados em **binário** (base 2), usando apenas os dígitos 0 e 1. Cada dígito binário é chamado de **bit**. Oito bits formam um **byte**.

**Decimal** é o sistema numérico de base 10 que os seres humanos normalmente usam.

**Hexadecimal** é base 16, usando os dígitos 0–9 e as letras A–F, frequentemente usado em computação para representar dados binários de forma compacta.

**Conversões:**
- Binary 1011 = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11 (decimal)
- Hex A3 = 10×16¹ + 3×16⁰ = 160 + 3 = 163 (decimal)

Converter entre bases numéricas é um conceito fundamental em ciência da computação.

## Álgebra Linear para Desenvolvedores e ML

Álgebra linear estuda vetores, matrizes e transformações lineares.

Um **vetor** é uma lista ordenada de números (ex.: features em uma amostra de ML).
- Exemplo: [23, 1.8, 175] representa a idade, a altura e o peso de uma pessoa

Uma **matriz** é um array bidimensional de números (ex.: pesos de um modelo ou batches de um dataset).
- Exemplo: [[1, 2], [3, 4]] é uma matriz 2×2

**Multiplicação de matrizes** combina transformações lineares e é uma operação central em gráficos, simulação e redes neurais.

**Produto escalar** mede similaridade e projeção entre vetores:
- a·b = Σ(a_i × b_i)
- **Cosine similarity** = (a·b) / (||a|| × ||b||)
- Cosine similarity varia de -1 (direções opostas) a 1 (mesma direção)

**Autovalores e autovetores** descrevem direções que são escaladas (e não rotacionadas) por uma matriz e são usados em métodos como PCA (Principal Component Analysis).

**Posto** indica quanta informação independente uma matriz contém. Aproximações de baixo posto são úteis para compressão e redução de dimensionalidade.

A maioria das cargas de trabalho modernas de ML depende fortemente de bibliotecas otimizadas de álgebra linear e de aceleração por hardware.
