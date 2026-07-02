# गणित और तर्कशास्त्र

## गणित क्या है?

गणित संख्याओं, आकृतियों, पैटर्नों और तार्किक संबंधों का अध्ययन है। यह एक विज्ञान भी है और एक भाषा भी, जिसका उपयोग ब्रह्मांड का वर्णन करने के लिए किया जाता है। गणित को arithmetic, algebra, geometry, calculus, statistics और logic जैसी शाखाओं में विभाजित किया जाता है। गणित physics, engineering, computer science, economics और कई अन्य क्षेत्रों की नींव है।

## अंकगणित

अंकगणित गणित की वह शाखा है जो संख्याओं पर मूलभूत क्रियाओं से संबंधित है। चार मौलिक क्रियाएँ हैं addition (+), subtraction (−), multiplication (×), और division (÷)। Order of operations यह निर्धारित करता है कि गणनाएँ किस क्रम में की जानी चाहिए: Parentheses, Exponents, Multiplication and Division (left to right), Addition and Subtraction (left to right)। इसे अक्सर **PEMDAS** या **BODMAS** के रूप में याद रखा जाता है। Prime number वह पूर्ण संख्या है जो 1 से बड़ी हो और जिसका 1 तथा स्वयं के अलावा कोई भाजक न हो। प्रारंभिक prime numbers हैं 2, 3, 5, 7, 11, 13, 17, 19, 23, और 29।

**उदाहरण:**
- Prime factorization: 84 = 2² × 3 × 7
- 24 और 36 का Greatest Common Divisor (GCD): 12
- 4 और 6 का Least Common Multiple (LCM): 12

## बीजगणित

बीजगणित equations और formulas में संख्याओं तथा राशियों को दर्शाने के लिए letters और symbols का उपयोग करता है। **Variable** एक symbol (आमतौर पर कोई letter) है जो किसी अज्ञात या बदलती हुई मात्रा का प्रतिनिधित्व करता है। **Equation** यह बताती है कि दो expressions बराबर हैं। किसी equation को solve करने का अर्थ है variable(s) के वे मान खोजना जो equation को सत्य बनाते हैं।

**Quadratic formula** ax² + bx + c = 0 के रूप की equations को हल करती है: x = (−b ± √(b²−4ac)) / (2a)


**Function** प्रत्येक input को ठीक एक output से map करती है। सामान्य functions में शामिल हैं:
- Linear: y = mx + b (सीधी रेखा, परिवर्तन की स्थिर दर)
- Quadratic: y = ax² + bx + c (parabola, वक्राकार)
- Exponential: y = a × bˣ (growth या decay, तीव्र परिवर्तन)
- Logarithmic: y = log_b(x) (exponential का inverse)

**मुख्य अवधारणाएँ:**
- Domain: सभी संभावित input values का समुच्चय
- Range: सभी संभावित output values का समुच्चय
- Slope: परिवर्तन की दर (y = mx + b में m)
- Intercept: जहाँ function y-axis को काटती है (y = mx + b में b)

## ज्यामिति

ज्यामिति गणित की वह शाखा है जो आकृतियों, आकारों, स्थितियों और आकृतियों के गुणों का अध्ययन करती है। Point का कोई आकार नहीं होता; यह केवल एक स्थान दर्शाता है। Line दोनों दिशाओं में अनंत तक फैली होती है। Line segment के दो endpoints होते हैं। Angle दो rays से बनता है जो एक endpoint साझा करती हैं।

**मुख्य नियम:**
- Triangle में कोणों का योग हमेशा 180 degrees होता है।
- Quadrilateral में कोणों का योग हमेशा 360 degrees होता है।
- Pythagorean theorem: समकोण triangle में a² + b² = c² (जहाँ c hypotenuse है)।
- Circle circumference: 2πr
- Circle area: πr²
- Sphere volume: (4/3)πr³

**π (pi)** लगभग 3.14159 है और यह circle की circumference तथा diameter का अनुपात है।

**सामान्य ज्यामितीय आकृतियाँ:**
- Triangle: 3 sides, कोणों का योग 180°
- Square: 4 बराबर sides, 4 right angles
- Rectangle: 4 sides, विपरीत sides बराबर, 4 right angles
- Circle: कोई side नहीं, निरंतर curved boundary
- Pentagon: 5 sides, कोणों का योग 540°
- Hexagon: 6 sides, कोणों का योग 720°

## सांख्यिकी और प्रायिकता

सांख्यिकी डेटा को एकत्रित करने, उसका विश्लेषण करने, उसकी व्याख्या करने और उसे प्रस्तुत करने का विज्ञान है।

**केंद्रीय प्रवृत्ति के माप:**
- **Mean** (average): सभी values का योग, values की संख्या से विभाजित
- **Median**: जब डेटा क्रमबद्ध हो तो बीच की value (outliers के प्रति कम संवेदनशील)
- **Mode**: सबसे अधिक बार आने वाली value (एक से अधिक modes हो सकते हैं)

**प्रसार के माप:**
- **Range**: maximum - minimum
- **Variance**: mean से squared deviations का औसत
- **Standard deviation**: variance का square root (डेटा की वही units)

Probability किसी घटना के होने की संभावना को मापती है, जो 0 (असंभव) से 1 (निश्चित) तक होती है। दो independent घटनाओं के दोनों होने की probability उनकी व्यक्तिगत probabilities के गुणनफल के बराबर होती है।

**उदाहरण:** किसी निष्पक्ष die पर 6 आने की probability: 1/6. लगातार दो बार 6 आने की probability: (1/6) × (1/6) = 1/36.

## Computing और ML के लिए Probability

**Random variable** वह variable है जिसका मान किसी random process के परिणाम पर निर्भर करता है। **Probability distribution** यह वर्णन करती है कि प्रत्येक outcome कितना संभावित है।

**सामान्य distributions:**
- **Bernoulli**: दो outcomes वाला एक trial (उदा., coin flip)
- **Binomial**: n independent Bernoulli trials में successes की संख्या
- **Normal (Gaussian)**: bell curve, mean के चारों ओर symmetric (प्राकृतिक घटनाओं में सामान्य)
- **Poisson**: निश्चित interval में events की संख्या (उदा., प्रति घंटा emails)

**Expected value** random variable का long-run average outcome है। **Variance** उस expectation के आसपास के प्रसार को मापता है।

**Conditional probability** किसी घटना की probability का वर्णन करती है, यह मानते हुए कि दूसरी घटना घट चुकी है: P(A|B) = P(A ∩ B) / P(B) [यदि P(B) > 0]।

**Bayes' theorem** साक्ष्य के आधार पर विश्वासों को अद्यतन करती है: P(A|B) = P(B|A) × P(A) / P(B).


Machine learning में probability classification confidence, uncertainty estimation, Bayesian methods और कई loss functions (जैसे cross-entropy) की आधारशिला है।

## कलन

कलन गणित की वह शाखा है जो continuous change का अध्ययन करती है।

**Differential calculus** परिवर्तन की दरों और curves के slopes से संबंधित है, और इसके लिए **derivatives** का उपयोग करती है। किसी function f(x) का derivative किसी बिंदु पर x के सापेक्ष f के परिवर्तन की दर दर्शाता है। Notation: f'(x) या df/dx.

**सामान्य derivatives:**
- d/dx [x^n] = n·x^(n−1)
- d/dx [e^x] = e^x
- d/dx [ln(x)] = 1/x
- d/dx [sin(x)] = cos(x)

**Integral calculus** मात्राओं के संचय और curves के नीचे के area से संबंधित है, और **integrals** का उपयोग करती है। Integral दो बिंदुओं के बीच curve के नीचे का area दर्शाता है।

**Fundamental theorem of calculus** differentiation और integration को जोड़ती है: differentiation और integration परस्पर inverse operations हैं।

Calculus का स्वतंत्र रूप से विकास Isaac Newton और Gottfried Wilhelm Leibniz ने 17वीं शताब्दी में किया था।

## संख्या प्रणालियाँ

- **Natural numbers**: 1, 2, 3, 4, ... (गिनने वाली संख्याएँ)
- **Whole numbers**: 0, 1, 2, 3, ... (natural numbers plus zero)
- **Integers**: ..., −2, −1, 0, 1, 2, ... (सभी whole numbers और उनके negatives)
- **Rational numbers**: वे संख्याएँ जिन्हें p/q के रूप में व्यक्त किया जा सकता है, जहाँ p और q integers हैं और q ≠ 0 (उदा., 1/2, 3/4, −5/3)
- **Irrational numbers**: fraction के रूप में व्यक्त नहीं की जा सकतीं (उदा., √2, π, e)
- **Real numbers**: सभी rational और irrational numbers (number line)
- **Imaginary numbers**: negative numbers के square root को शामिल करती हैं; i = √(−1)
- **Complex numbers**: real और imaginary भागों का संयोजन (a + bi)

## तर्क और विवेचना

Logic वैध reasoning का अध्ययन है।

**Deductive reasoning** सामान्य premises से विशिष्ट conclusions निकालती है। यदि premises सत्य हैं और argument वैध है, तो conclusion अनिवार्य रूप से सत्य होगी।
- **उदाहरण:** सभी मनुष्य नश्वर हैं। Socrates मनुष्य है। अतः Socrates नश्वर है।

**Inductive reasoning** विशिष्ट observations से सामान्य conclusions निकालती है। यह conclusion के सत्य होने की गारंटी नहीं देती, लेकिन उसे संभावित बनाती है।
- **उदाहरण:** मैंने जितने भी swans देखे हैं वे सफ़ेद हैं। अतः सभी swans सफ़ेद हैं। (ध्यान दें: यह गलत है; black swans भी होते हैं!)

**सामान्य logical fallacies (reasoning में त्रुटियाँ):**
- **Ad hominem**: तर्क के बजाय व्यक्ति पर आक्रमण करना
- **Straw man**: तर्क को गलत रूप में प्रस्तुत करना ताकि उस पर हमला करना आसान हो जाए
- **False dichotomy**: जब अधिक विकल्प हों तब केवल दो विकल्प प्रस्तुत करना
- **Circular reasoning**: conclusion को ही premise के रूप में उपयोग करना
- **Appeal to authority**: यह दावा करना कि कोई बात इसलिए सत्य है क्योंकि किसी authority ने ऐसा कहा है
- **Post hoc fallacy**: यह मान लेना कि क्योंकि A, B से पहले हुआ, इसलिए A ने B का कारण बना

## समुच्चय

**Set** विशिष्ट वस्तुओं का एक collection है।
- **Union** (A ∪ B): दोनों sets के सभी elements
- **Intersection** (A ∩ B): केवल वे elements जो दोनों में सामान्य हों
- **Empty set** (∅ or {}): इसमें कोई elements नहीं होते
- **Subset** (A ⊆ B): A के सभी elements, B में भी हैं
- **Venn diagrams**: sets के बीच संबंधों का दृश्य निरूपण

Set theory आधुनिक गणित और logic की आधारशिला है।

## Binary और Number Bases

Computers डेटा को **binary** (base 2) में दर्शाते हैं, जिसमें केवल 0 और 1 digits का उपयोग होता है। प्रत्येक binary digit को **bit** कहा जाता है। आठ bits मिलकर एक **byte** बनाते हैं।

**Decimal** वह base-10 number system है जिसका मनुष्य सामान्यतः उपयोग करते हैं।

**Hexadecimal** base 16 है, जिसमें 0–9 digits और A–F letters का उपयोग होता है, और computing में binary data को संक्षिप्त रूप में दर्शाने के लिए इसका अक्सर उपयोग किया जाता है।

**Conversions:**
- Binary 1011 = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11 (decimal)
- Hex A3 = 10×16¹ + 3×16⁰ = 160 + 3 = 163 (decimal)

Number bases के बीच conversion computer science की एक मौलिक अवधारणा है।

## Developers और ML के लिए Linear Algebra

Linear algebra vectors, matrices और linear transformations का अध्ययन करती है।

**Vector** संख्याओं की क्रमबद्ध सूची है (उदा., किसी ML sample की features)।
- उदाहरण: [23, 1.8, 175] किसी व्यक्ति की age, height और weight को दर्शाता है

**Matrix** संख्याओं की 2D array है (उदा., model weights या dataset batches)।
- उदाहरण: [[1, 2], [3, 4]] एक 2×2 matrix है

**Matrix multiplication** linear transformations को संयोजित करती है और graphics, simulation तथा neural networks में एक मुख्य operation है।

**Dot product** vectors के बीच similarity और projection को मापता है:
- a·b = Σ(a_i × b_i)
- **Cosine similarity** = (a·b) / (||a|| × ||b||)
- Cosine similarity -1 (विपरीत) से 1 (एक ही दिशा) तक होती है

**Eigenvalues and eigenvectors** उन दिशाओं का वर्णन करते हैं जिन्हें कोई matrix scale करती है (rotate नहीं), और इनका उपयोग PCA (Principal Component Analysis) जैसी विधियों में होता है।

**Rank** यह दर्शाता है कि किसी matrix में कितनी independent information है। Low-rank approximations compression और dimensionality reduction के लिए उपयोगी हैं।

अधिकांश आधुनिक ML workloads optimised linear algebra libraries और hardware acceleration पर बहुत अधिक निर्भर करते हैं।
