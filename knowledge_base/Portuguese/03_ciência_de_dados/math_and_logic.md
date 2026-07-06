# Matemática e Lógica

## O que é Matemática?

Matemática é o estudo dos números, das formas, dos padrões e das relações lógicas. É ao mesmo tempo uma ciência e uma linguagem usada para descrever o universo. A matemática é dividida em ramos, incluindo aritmética, álgebra, geometria, cálculo, estatística e lógica. Ela é a base da física, da engenharia, da ciência da computação, da economia e de muitas outras áreas.

## Aritmética

A aritmética é o ramo da matemática que lida com operações básicas com números. As quatro operações fundamentais são adição (+), subtração (−), multiplicação (×) e divisão (÷). A ordem das operações especifica a sequência em que os cálculos devem ser realizados: Parênteses, Expoentes, Multiplicação e Divisão (da esquerda para a direita), Adição e Subtração (da esquerda para a direita). Isso costuma ser lembrado como **PEMDAS** ou **BODMAS**. Um número primo é um número inteiro maior que 1 que não tem divisores além de 1 e dele mesmo. Os primeiros números primos são 2, 3, 5, 7, 11, 13, 17, 19, 23 e 29.

**Exemplos:**
- Fatoração prima: 84 = 2² × 3 × 7
- Máximo Divisor Comum (MDC) de 24 e 36: 12
- Mínimo Múltiplo Comum (MMC) de 4 e 6: 12

## Álgebra

A álgebra usa letras e símbolos para representar números e quantidades em equações e fórmulas. Uma **variável** é um símbolo (geralmente uma letra) que representa uma quantidade desconhecida ou variável. Uma **equação** afirma que duas expressões são iguais. Resolver uma equação significa encontrar o(s) valor(es) da(s) variável(is) que tornam a equação verdadeira.

A **fórmula quadrática** resolve equações na forma ax² + bx + c = 0: x = (−b ± √(b²−4ac)) / (2a)


Uma **função** associa cada entrada a exatamente uma saída. Funções comuns incluem:
- Linear: y = mx + b (reta, taxa de variação constante)
- Quadrática: y = ax² + bx + c (parábola, curva)
- Exponencial: y = a × bˣ (crescimento ou decaimento, mudança rápida)
- Logarítmica: y = log_b(x) (inversa da exponencial)

**Conceitos-chave:**
- Domínio: o conjunto de todos os valores de entrada possíveis
- Imagem: o conjunto de todos os valores de saída possíveis
- Inclinação: taxa de variação (m em y = mx + b)
- Intercepto: onde a função cruza o eixo y (b em y = mx + b)

## Geometria

Geometria é o ramo da matemática que estuda formas, tamanhos, posições e propriedades das figuras. Um ponto não tem tamanho; ele representa uma localização. Uma reta se estende infinitamente em ambas as direções. Um segmento de reta tem dois pontos extremos. Um ângulo é formado por duas semirretas que compartilham um ponto extremo.

**Regras-chave:**
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
- Círculo: sem lados, contorno curvo contínuo
- Pentágono: 5 lados, soma dos ângulos igual a 540°
- Hexágono: 6 lados, soma dos ângulos igual a 720°

## Estatística e Probabilidade

Estatística é a ciência de coletar, analisar, interpretar e apresentar dados.

**Medidas de tendência central:**
- **Média**: soma de todos os valores dividida pelo número de valores
- **Mediana**: valor central quando os dados estão ordenados (menos sensível a valores extremos)
- **Moda**: valor que ocorre com mais frequência (pode haver múltiplas modas)

**Medidas de dispersão:**
- **Amplitude**: máximo - mínimo
- **Variância**: média dos desvios quadráticos em relação à média
- **Desvio padrão**: raiz quadrada da variância (nas mesmas unidades dos dados)

Probabilidade mede a chance de um evento ocorrer, variando de 0 (impossível) a 1 (certo). A probabilidade de dois eventos independentes ocorrerem ambos é o produto de suas probabilidades individuais.

**Exemplo:** Probabilidade de tirar um 6 em um dado justo: 1/6. Probabilidade de tirar dois 6 seguidos: (1/6) × (1/6) = 1/36.

## Probabilidade para Computação e ML

Uma **variável aleatória** é uma variável cujo valor depende do resultado de um processo aleatório. Uma **distribuição de probabilidade** descreve a probabilidade de cada resultado.

**Distribuições comuns:**
- **Bernoulli**: uma única tentativa com dois resultados (por exemplo, lançamento de moeda)
- **Binomial**: número de sucessos em n tentativas de Bernoulli independentes
- **Normal (Gaussiana)**: curva em sino, simétrica em torno da média (comum em fenômenos naturais)
- **Poisson**: número de eventos em um intervalo fixo (por exemplo, e-mails por hora)

**Valor esperado** é o resultado médio de longo prazo de uma variável aleatória. **Variância** mede a dispersão em torno dessa expectativa.

**Probabilidade condicional** descreve a probabilidade de um evento dado que outro evento ocorreu: P(A|B) = P(A ∩ B) / P(B) [se P(B) > 0].

O **teorema de Bayes** atualiza crenças com base em evidências: P(A|B) = P(B|A) × P(A) / P(B).


Em aprendizado de máquina, a probabilidade sustenta a confiança da classificação, a estimativa de incerteza, os métodos bayesianos e muitas funções de perda (como a entropia cruzada).

## Cálculo

Cálculo é o ramo da matemática que estuda a mudança contínua.

O **cálculo diferencial** trata das taxas de variação e das inclinações de curvas, usando **derivadas**. A derivada de uma função f(x) representa a taxa de variação de f em relação a x em um ponto. Notação: f'(x) ou df/dx.

**Derivadas comuns:**
- d/dx [x^n] = n·x^(n−1)
- d/dx [e^x] = e^x
- d/dx [ln(x)] = 1/x
- d/dx [sin(x)] = cos(x)

O **cálculo integral** trata da acumulação de quantidades e das áreas sob curvas, usando **integrais**. A integral representa a área sob a curva entre dois pontos.

O **teorema fundamental do cálculo** conecta diferenciação e integração: diferenciação e integração são operações inversas.

O cálculo foi desenvolvido independentemente por Isaac Newton e Gottfried Wilhelm Leibniz no século XVII.

## Sistemas Numéricos

- **Números naturais**: 1, 2, 3, 4, ... (números de contagem)
- **Números inteiros não negativos**: 0, 1, 2, 3, ... (números naturais mais zero)
- **Números inteiros**: ..., −2, −1, 0, 1, 2, ... (todos os inteiros não negativos e seus negativos)
- **Números racionais**: números que podem ser expressos como p/q, onde p e q são inteiros e q ≠ 0 (por exemplo, 1/2, 3/4, −5/3)
- **Números irracionais**: não podem ser expressos como fração (por exemplo, √2, π, e)
- **Números reais**: todos os números racionais e irracionais (a reta numérica)
- **Números imaginários**: envolvem a raiz quadrada de números negativos; i = √(−1)
- **Números complexos**: combinam partes reais e imaginárias (a + bi)

## Lógica e Raciocínio

Lógica é o estudo do raciocínio válido.

**Raciocínio dedutivo** tira conclusões específicas a partir de premissas gerais. Se as premissas forem verdadeiras e o argumento for válido, a conclusão deve ser verdadeira.
- **Exemplo:** Todos os humanos são mortais. Sócrates é humano. Portanto, Sócrates é mortal.

**Raciocínio indutivo** tira conclusões gerais a partir de observações específicas. Ele não garante que a conclusão seja verdadeira, mas a torna provável.
- **Exemplo:** Todo cisne que eu vi é branco. Portanto, todos os cisnes são brancos. (Observação: isso é falso; cisnes negros existem!)

**Falácias lógicas comuns (erros de raciocínio):**
- **Ad hominem**: atacar a pessoa em vez do argumento
- **Espantalho**: deturpar um argumento para torná-lo mais fácil de atacar
- **Falsa dicotomia**: apresentar apenas duas opções quando existem mais
- **Raciocínio circular**: usar a conclusão como premissa
- **Apelo à autoridade**: afirmar que algo é verdadeiro porque uma autoridade assim diz
- **Falácia post hoc**: supor que, porque A aconteceu antes de B, A causou B

## Conjuntos

Um **conjunto** é uma coleção de objetos distintos.
- **União** (A ∪ B): todos os elementos de ambos os conjuntos
- **Interseção** (A ∩ B): apenas os elementos comuns aos dois
- **Conjunto vazio** (∅ ou {}): não contém elementos
- **Subconjunto** (A ⊆ B): todos os elementos de A também estão em B
- **Diagramas de Venn**: representam visualmente relações entre conjuntos

A teoria dos conjuntos é a base da matemática e da lógica modernas.

## Binário e Bases Numéricas

Computadores representam dados em **binário** (base 2), usando apenas os dígitos 0 e 1. Cada dígito binário é chamado de **bit**. Oito bits formam um **byte**.

**Decimal** é o sistema numérico de base 10 que os humanos normalmente usam.

**Hexadecimal** é base 16, usando os dígitos 0–9 e as letras A–F, frequentemente usado em computação para representar dados binários de forma compacta.

**Conversões:**
- Binário 1011 = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11 (decimal)
- Hex A3 = 10×16¹ + 3×16⁰ = 160 + 3 = 163 (decimal)

Converter entre bases numéricas é um conceito fundamental na ciência da computação.

## Álgebra Linear para Desenvolvedores e ML

Álgebra linear estuda vetores, matrizes e transformações lineares.

Um **vetor** é uma lista ordenada de números (por exemplo, características em uma amostra de ML).
- Exemplo: [23, 1.8, 175] representa a idade, a altura e o peso de uma pessoa

Uma **matriz** é um arranjo bidimensional de números (por exemplo, pesos do modelo ou lotes de dados).
- Exemplo: [[1, 2], [3, 4]] é uma matriz 2×2

A **multiplicação de matrizes** combina transformações lineares e é uma operação central em gráficos, simulação e redes neurais.

**Produto escalar** mede similaridade e projeção entre vetores:
- a·b = Σ(a_i × b_i)
- **Similaridade do cosseno** = (a·b) / (||a|| × ||b||)
- A similaridade do cosseno varia de -1 (opostos) a 1 (mesma direção)

**Autovalores e autovetores** descrevem direções que são escaladas (não rotacionadas) por uma matriz e são usados em métodos como PCA (Análise de Componentes Principais).

**Posto** indica quanta informação independente uma matriz contém. Aproximações de baixo posto são úteis para compressão e redução de dimensionalidade.

A maioria das cargas de trabalho modernas de ML depende fortemente de bibliotecas otimizadas de álgebra linear e de aceleração por hardware.
