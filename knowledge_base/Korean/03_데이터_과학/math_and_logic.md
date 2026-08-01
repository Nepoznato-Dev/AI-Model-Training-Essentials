<!-- 
This file was automatically translated from English to Korean.
Source: math_and_logic.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 수학과 논리

## 수학이란 무엇인가?

수학은 수, 도형, 패턴, 그리고 논리적 관계를 연구하는 학문입니다. 우주를 설명하는 데 쓰이는 과학이자 언어이기도 합니다. 수학은 산술, 대수, 기하학, 미적분, 통계, 논리 같은 여러 분야로 나뉘며, 물리학, 공학, computer science, economics를 비롯한 많은 분야의 기초를 이룹니다.

## 산술

산술은 수에 대한 기본 연산을 다루는 수학의 한 분야입니다. 네 가지 기본 연산은 덧셈 (+), 뺄셈 (−), 곱셈 (×), 나눗셈 (÷)입니다. 연산 순서는 계산을 어떤 순서로 해야 하는지 정해 주며, 일반적으로 괄호, 지수, 곱셈과 나눗셈(왼쪽에서 오른쪽), 덧셈과 뺄셈(왼쪽에서 오른쪽) 순으로 진행합니다. 이는 **PEMDAS** 또는 **BODMAS**로 기억하는 경우가 많습니다. 소수(prime number)는 1보다 큰 자연수 가운데 1과 자기 자신 외에는 약수가 없는 수입니다. 처음 몇 개의 소수는 2, 3, 5, 7, 11, 13, 17, 19, 23, 29입니다.

**예시:**
- 84의 소인수분해: 84 = 2² × 3 × 7
- 24와 36의 최대공약수 (GCD): 12
- 4와 6의 최소공배수 (LCM): 12

## 대수

대수는 문자와 기호를 사용해 방정식과 공식 속의 수와 양을 표현합니다. **Variable**은 알 수 없거나 변하는 양을 나타내는 기호로, 보통 문자를 사용합니다. **Equation**은 두 식이 같음을 나타냅니다. 방정식을 푼다는 것은 그 식을 참으로 만드는 **variable**의 값을 찾는다는 뜻입니다.

**Quadratic formula**는 ax² + bx + c = 0 꼴의 방정식을 푸는 공식입니다: x = (−b ± √(b²−4ac)) / (2a)

함수(function)는 각 입력값을 정확히 하나의 출력값에 대응시킵니다. 대표적인 함수는 다음과 같습니다:
- Linear: y = mx + b (직선, 일정한 변화율)
- Quadratic: y = ax² + bx + c (포물선, 곡선 형태)
- Exponential: y = a × bˣ (급격한 성장 또는 감소)
- Logarithmic: y = log_b(x) (exponential의 역함수)

**핵심 개념:**
- Domain: 가능한 모든 입력값의 집합
- Range: 가능한 모든 출력값의 집합
- Slope: 변화율 (y = mx + b에서 m)
- Intercept: 함수가 y축과 만나는 값 (y = mx + b에서 b)

## 기하학

기하학은 도형의 모양, 크기, 위치, 성질을 연구하는 수학의 한 분야입니다. 점은 크기가 없고 위치만 나타냅니다. 직선은 양방향으로 무한히 뻗어 있습니다. 선분은 두 끝점을 가집니다. 각은 하나의 끝점을 공유하는 두 반직선으로 이루어집니다.

**주요 규칙:**
- 삼각형의 내각의 합은 항상 180도입니다.
- 사각형의 내각의 합은 항상 360도입니다.
- 피타고라스 정리: 직각삼각형에서 a² + b² = c² (c는 빗변)
- 원의 둘레: 2πr
- 원의 넓이: πr²
- 구의 부피: (4/3)πr³

**π (pi)**는 약 3.14159이며, 원의 둘레와 지름의 비율입니다.

**대표적인 도형:**
- Triangle: 변 3개, 내각의 합 180°
- Square: 네 변의 길이가 같고 직각 4개
- Rectangle: 마주 보는 변의 길이가 같고 직각 4개
- Circle: 변이 없고 연속된 곡선 경계를 가짐
- Pentagon: 변 5개, 내각의 합 540°
- Hexagon: 변 6개, 내각의 합 720°

## 통계와 확률

통계는 데이터를 수집하고, 분석하고, 해석하고, 제시하는 과학입니다.

**중심 경향 측도:**
- **Mean** (average): 모든 값을 더한 뒤 값의 개수로 나눈 것
- **Median**: 데이터를 정렬했을 때 가운데 오는 값 (이상치의 영향을 덜 받음)
- **Mode**: 가장 자주 나타나는 값 (여러 개일 수 있음)

**산포 측도:**
- **Range**: 최댓값 - 최솟값
- **Variance**: 평균으로부터의 제곱 편차 평균
- **Standard deviation**: variance의 제곱근 (데이터와 같은 단위)

확률은 어떤 사건이 일어날 가능성을 0(불가능)부터 1(확실) 사이 값으로 나타냅니다. 서로 독립인 두 사건이 모두 일어날 확률은 각 사건 확률의 곱입니다.

**예시:** 공정한 주사위에서 6이 나올 확률은 1/6입니다. 6이 두 번 연속 나올 확률은 (1/6) × (1/6) = 1/36입니다.

## 컴퓨팅과 ML을 위한 확률

**Random variable**은 무작위 과정의 결과에 따라 값이 정해지는 변수입니다. **Probability distribution**은 각 결과가 얼마나 일어날 가능성이 있는지를 설명합니다.

**자주 쓰이는 분포:**
- **Bernoulli**: 두 가지 결과만 있는 단일 시행 (예: 동전 던지기)
- **Binomial**: n번의 독립적인 Bernoulli 시행에서 성공한 횟수
- **Normal (Gaussian)**: 평균을 중심으로 대칭인 종 모양 분포 (자연현상에서 흔함)
- **Poisson**: 일정 구간 안에서 발생하는 사건 수 (예: 시간당 이메일 수)

**Expected value**는 random variable의 장기적인 평균 결과를 뜻합니다. **Variance**는 그 기대값 주변으로 얼마나 퍼져 있는지를 나타냅니다.

**Conditional probability**는 다른 사건이 이미 일어났다는 조건 아래에서의 확률을 뜻합니다: P(A|B) = P(A ∩ B) / P(B) [if P(B) > 0].

**Bayes' theorem**은 증거를 바탕으로 믿음을 갱신하는 방법을 설명합니다: P(A|B) = P(B|A) × P(A) / P(B).

기계 학습에서는 확률이 분류 신뢰도, 불확실성 추정, Bayesian 방법론, 그리고 cross-entropy 같은 여러 loss function의 기반이 됩니다.

## 미적분

미적분은 연속적인 변화를 연구하는 수학의 한 분야입니다.

**Differential calculus**는 **derivative**를 사용해 변화율과 곡선의 기울기를 다룹니다. 함수 f(x)의 derivative는 어떤 점에서 x에 대한 f의 변화율을 나타냅니다. 표기법은 f'(x) 또는 df/dx입니다.

**Common derivatives:**
- d/dx [x^n] = n·x^(n−1)
- d/dx [e^x] = e^x
- d/dx [ln(x)] = 1/x
- d/dx [sin(x)] = cos(x)

**Integral calculus**는 **integral**을 사용해 양의 누적과 곡선 아래 넓이를 다룹니다. 적분은 두 점 사이에서 곡선 아래의 넓이를 나타냅니다.

**Fundamental theorem of calculus**는 미분과 적분을 연결합니다. 즉, 미분과 적분은 서로 역연산 관계입니다.

미적분은 17세기에 Isaac Newton과 Gottfried Wilhelm Leibniz가 각각 독립적으로 발전시켰습니다.

## 수 체계

- **Natural numbers**: 1, 2, 3, 4, ... (자연수)
- **Whole numbers**: 0, 1, 2, 3, ... (0을 포함한 자연수)
- **Integers**: ..., −2, −1, 0, 1, 2, ... (정수)
- **Rational numbers**: p/q 꼴로 나타낼 수 있는 수. p와 q는 정수이고 q ≠ 0입니다 (예: 1/2, 3/4, −5/3).
- **Irrational numbers**: 분수로 정확히 나타낼 수 없는 수 (예: √2, π, e)
- **Real numbers**: 유리수와 무리수를 모두 포함하는 수 체계 (수직선 위의 수)
- **Imaginary numbers**: 음수의 제곱근을 포함하는 수. i = √(−1)
- **Complex numbers**: 실수부와 허수부를 함께 가지는 수 (a + bi)

## 논리와 추론

논리는 타당한 추론을 연구하는 분야입니다.

**Deductive reasoning**은 일반적인 전제로부터 구체적인 결론을 이끌어 냅니다. 전제가 참이고 논증이 타당하다면 결론도 반드시 참입니다.
- **예시:** 모든 인간은 죽습니다. 소크라테스는 인간입니다. 따라서 소크라테스는 죽습니다.

**Inductive reasoning**은 개별 관찰에서 일반적인 결론을 도출합니다. 결론이 반드시 참이라고 보장하지는 않지만, 그럴 가능성을 높여 줍니다.
- **예시:** 내가 본 모든 백조는 흰색이었습니다. 따라서 모든 백조는 흰색이라고 결론내릴 수 있습니다. (하지만 이는 틀린 결론입니다. 검은 백조도 존재합니다!)

**흔한 논리적 오류 (추론의 실수):**
- **Ad hominem**: 주장 대신 사람을 공격하는 오류
- **Straw man**: 상대 주장을 왜곡해 더 공격하기 쉽게 만드는 오류
- **False dichotomy**: 실제로는 더 많은 선택지가 있는데 둘만 제시하는 오류
- **Circular reasoning**: 결론을 전제로 다시 사용하는 오류
- **Appeal to authority**: 권위자가 말했으니 참이라고 주장하는 오류
- **Post hoc fallacy**: A가 B보다 먼저 일어났다는 이유만으로 A가 B의 원인이라고 보는 오류

## 집합

**Set**은 서로 구별되는 대상들의 모임입니다.
- **Union** (A ∪ B): 두 집합의 모든 원소
- **Intersection** (A ∩ B): 두 집합에 공통으로 들어 있는 원소
- **Empty set** (∅ or {}): 원소가 하나도 없는 집합
- **Subset** (A ⊆ B): A의 모든 원소가 B에도 포함되는 관계
- **Venn diagrams**: 집합 간 관계를 시각적으로 나타내는 그림

집합론은 현대 수학과 논리학의 기초를 이룹니다.

## 이진수와 진법

컴퓨터는 데이터를 **binary** (base 2)로 표현하며, 0과 1 두 숫자만 사용합니다. 각 binary digit를 **bit**라고 하고, 8bit를 **byte**라고 합니다.

**Decimal**은 사람이 일반적으로 사용하는 10진법입니다.

**Hexadecimal**은 16진법으로, 0–9와 A–F를 사용하며 컴퓨팅에서 binary 데이터를 더 간결하게 표현할 때 자주 쓰입니다.

**변환 예시:**
- Binary 1011 = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11 (decimal)
- Hex A3 = 10×16¹ + 3×16⁰ = 160 + 3 = 163 (decimal)

진법 변환은 computer science의 기본 개념 가운데 하나입니다.

## 개발자와 ML을 위한 선형대수

Linear algebra는 벡터, 행렬, 선형 변환을 연구합니다.

**Vector**는 순서가 있는 수의 목록입니다 (예: ML 샘플의 feature들).
- 예를 들어 [23, 1.8, 175]는 어떤 사람의 나이, 키, 몸무게를 나타낼 수 있습니다.

**Matrix**는 숫자로 이루어진 2차원 배열입니다 (예: 모델 가중치나 데이터셋 batch).
- 예를 들어 [[1, 2], [3, 4]]는 2×2 행렬입니다.

**Matrix multiplication**은 선형 변환을 결합하는 연산으로, graphics, simulation, neural network에서 핵심적으로 사용됩니다.

**Dot product**는 벡터 사이의 유사성과 투영을 측정합니다.
- a·b = Σ(a_i × b_i)
- **Cosine similarity** = (a·b) / (||a|| × ||b||)
- Cosine similarity는 -1(정반대 방향)에서 1(같은 방향) 사이 값을 가집니다.

**Eigenvalues**와 **eigenvectors**는 행렬에 의해 크기만 바뀌고 방향은 유지되는 축을 설명하며, PCA (Principal Component Analysis) 같은 방법에 활용됩니다.

**Rank**는 행렬이 담고 있는 독립적인 정보의 양을 나타냅니다. 저랭크 근사는 압축과 차원 축소에 유용합니다.

현대의 대부분의 ML 워크로드는 최적화된 선형대수 라이브러리와 하드웨어 가속에 크게 의존합니다.
