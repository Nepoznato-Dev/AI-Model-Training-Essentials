<!--
---
# Metadata
title: "Cognitive Biases and Logical Fallacies"
description: "Reasoning errors and cognitive biases"
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
tags: [cognitive, logical, issues, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "27 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# علمی تعصبات اور منطقی غلطیاں
یہ دستاویز علمی تعصبات، منطقی غلط فہمیوں، اور استدلال کی غلطیوں کو مضبوط کرتی ہے جو انسانی فیصلہ سازی اور AI نظام کے نتائج دونوں کو متاثر کرتی ہے۔
---

## علمی تعصبات
علمی تعصبات فیصلے اور فیصلہ سازی میں عقلیت سے انحراف کے منظم نمونے ہیں۔ سافٹ ویئر ڈویلپمنٹ اور اے آئی سسٹمز میں، یہ ناقص ڈیزائن کے فیصلے، ناقص تقاضوں اور متعصب ماڈل رویے کا باعث بن سکتے ہیں۔
### تصدیقی تعصب
**یہ کیا ہے:** معلومات کو اس انداز میں تلاش کرنے، اس کی تشریح کرنے اور یاد کرنے کا رجحان جو پہلے سے موجود عقائد کی تصدیق کرتا ہے۔
**ترقی میں بری مثال:**```python
# Developer believes their algorithm is O(n log n)
def analyze_complexity(code):
    # Only looks for evidence supporting O(n log n)
    sees_divide_and_conquer = True
    sees_recursion = True
    
    # Ignores contradictory evidence
    nested_loop_present = True  # Actually makes it O(n²)
    redundant_computation = True  # Adds extra factor
    
    return "O(n log n)"  # Wrong conclusion
```

**کوڈ کے جائزوں میں:**```markdown
Developer A (senior): "This looks good, nice work!"
Developer B (junior): "This has several potential issues..."

Team accepts Developer A's review without scrutiny but questions Developer B's feedback excessively.
```

**تخفیف:**
- فعال طور پر غیر تصدیق شدہ ثبوت تلاش کریں۔
- بلائنڈ کوڈ کے جائزے استعمال کریں۔
- اختلاف رائے کی حوصلہ افزائی کریں۔
- دستاویزی مفروضے واضح طور پر
### اینکرنگ تعصب
**یہ کیا ہے:** معلومات کے پہلے حصے پر بہت زیادہ انحصار کرنا۔
**بری مثال:**```markdown
Project Manager: "This feature should take about 2 days."
Developer: (Anchored to 2 days, even though realistic estimate is 5 days)
"Okay, I'll try to finish in 2 days."

Result: Rushed work, technical debt, missed deadlines anyway.
```

**تخفیف:**
- متعدد آزاد تخمینے حاصل کریں۔
- تخمینہ لگانے کے لیے پلاننگ پوکر کا استعمال کریں۔
- نقطہ تخمینوں کے بجائے حدود پر غور کریں۔
- تاریخی ڈیٹا کا حوالہ دیں۔
### ڈوبی لاگت کی غلطی
**یہ کیا ہے:** پہلے سے لگائے گئے وسائل (وقت، پیسہ، کوشش) کی وجہ سے کوشش جاری رکھنا، یہاں تک کہ ترک کرنا بہتر ہوگا۔
**بری مثال:**```markdown
"We've already spent 6 months building this custom framework. 
We can't switch to the industry standard now, even though 
it would save us time in the long run."
```

**تخفیف:**
- مستقبل کی قیمت کی بنیاد پر فیصلوں کا اندازہ کریں، ماضی کی سرمایہ کاری کی نہیں۔
- باقاعدگی سے پروجیکٹ کی قابل عملیت کا دوبارہ جائزہ لیں۔
- محور کے لیے نفسیاتی حفاظت بنائیں
- جاری رکھنے / روکنے کے فیصلوں کے لیے معروضی معیار استعمال کریں۔
### دستیابی ہیورسٹک
**یہ کیا ہے:** آسانی سے دستیاب یا حالیہ معلومات کی اہمیت کو بڑھانا۔
**بری مثال:**```markdown
"I just read about a SQL injection attack, so we should 
prioritize SQL injection prevention over XSS, even though 
our security audit shows XSS is our bigger risk."
```

**تخفیف:**
- ڈیٹا پر مبنی فیصلہ سازی کا استعمال کریں۔
- جامع خطرے کے ماڈلز سے مشورہ کریں۔
- بنیادی شرحوں اور اعدادوشمار کو دیکھیں
- ترجیحات میں رجعت پسندی سے پرہیز کریں۔
### ڈننگ-کروگر اثر
**یہ کیا ہے:** کسی کام میں کم صلاحیت والے لوگ اپنی قابلیت کا زیادہ اندازہ لگاتے ہیں۔ ماہرین ان کو کم کر سکتے ہیں۔
**بری مثال:**```markdown
Junior Developer: "I've completed a Python tutorial. 
I'm ready to architect our entire microservices platform."

Senior Developer: "I've been building distributed systems for 10 years. 
I'm probably missing something important in this design."
```

**تخفیف:**
- مسلسل سیکھنے کی حوصلہ افزائی کریں۔
- ہم مرتبہ جائزہ کے عمل کو لاگو کریں۔
- رہنمائی کے پروگرام بنائیں
- عاجزی اور تجسس کو فروغ دیں۔
---

## منطقی غلطیاں
منطقی غلطیاں استدلال میں غلطیاں ہیں جو دلیل کی صداقت کو کمزور کرتی ہیں۔ AI ماڈل ان غلط فہمیوں پر مشتمل آؤٹ پٹ تیار کر سکتے ہیں۔
### Ad Hominem (شخص کے خلاف حملہ)
**یہ کیا ہے:** خود دلیل کی بجائے دلیل دینے والے شخص پر حملہ کرنا۔
**بری مثال:**```markdown
"This code review is wrong because the reviewer is a junior developer."
```

**یہ برا کیوں ہے:** تاثرات کی درستگی کا انحصار اس کے مواد پر ہے، جائزہ لینے والے کی سنیارٹی پر نہیں۔
### اتھارٹی سے اپیل
**یہ کیا ہے:** کسی چیز کا دعویٰ کرنا درست ہے کیونکہ ایک اتھارٹی شخصیت بغیر ثبوت کے ایسا کہتی ہے۔
**بری مثال:**```markdown
"This architecture must be correct because Google uses it."
```

**یہ برا کیوں ہے:** گوگل کے لیے ان کے پیمانے پر جو کام کرتا ہے وہ آپ کے استعمال کے معاملے میں کام نہیں کر سکتا۔
### جھوٹی تفریق (سیاہ و سفید سوچ)
**یہ کیا ہے:** جب زیادہ موجود ہوں تو صرف دو اختیارات پیش کرنا۔
**بری مثال:**```markdown
"We either rewrite everything in Rust or accept that our 
codebase will always be slow and buggy."
```

**حقیقت:** ان انتہاؤں کے درمیان بہت سے اختیارات موجود ہیں (ہاٹ پاتھ کو بہتر بنائیں، مخصوص اجزاء کے لیے رسٹ کا استعمال کریں، ازگر کوڈ کو بہتر بنائیں، وغیرہ)
### پھسلن والی ڈھلوان
**یہ کیا ہے:** یہ بحث کرنا کہ ایک واقعہ لامحالہ منفی نتائج کی ایک زنجیر کا باعث بنے گا۔
**بری مثال:**```markdown
"If we allow this small technical debt, soon our entire 
codebase will be unmaintainable and the company will fail."
```

**یہ برا کیوں ہے:** بغیر ثبوت کے ناگزیر ترقی کو فرض کرتا ہے۔ کم کرنے والے عوامل کو نظر انداز کرتا ہے۔
### سرکلر ریزننگ
**یہ کیا ہے:** اختتام کو ایک بنیاد کے طور پر استعمال کرنا۔
**بری مثال:**```markdown
"Our code is high quality because we write good code."
```

### Post Hoc Ergo Propter Hoc (غلط وجہ)
**یہ کیا ہے:** یہ فرض کرتے ہوئے کہ B نے A کی پیروی کی، A کی وجہ سے B۔
**بری مثال:**```markdown
"We deployed the new feature and then saw increased latency. 
The new feature must be causing the latency."
```

**حقیقت:** ارتباط کا مطلب وجہ نہیں ہے۔ دیگر عوامل ذمہ دار ہو سکتے ہیں۔
### اسٹرا مین
**یہ کیا ہے:** حملہ کرنا آسان بنانے کے لیے کسی کی دلیل کو غلط انداز میں پیش کرنا۔
**بری مثال:**```markdown
Developer A: "We should add more tests for edge cases."
Developer B: "So you want us to spend all our time writing tests 
and never ship features?"
```

### بینڈ ویگن کی غلط فہمی۔
**یہ کیا ہے:** کسی چیز پر بحث کرنا درست ہے کیونکہ بہت سے لوگ اس پر یقین رکھتے ہیں۔
**بری مثال:**```markdown
"Everyone is using Kubernetes, so we should too."
```

**یہ برا کیوں ہے:** مقبولیت آپ کی مخصوص ضروریات کے لیے موزوں ہونے کی ضمانت نہیں دیتی۔
---

## AI میں استدلال کی ناکامیاں
### ملٹی سٹیپ لاجک کی خرابیاں
**بری مثال:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Yes, Alice must be a programmer.
```

**یہ برا کیوں ہے:**
- نتیجے کی تصدیق کرنے کی غلطی کا ارتکاب کرتا ہے۔
- ایلس بغیر پروگرامر کے کوڈ لکھ سکتی تھی۔
- منطقی ساخت: (P→Q, Q) ⊬ P
**صحیح استدلال:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Not necessarily. While all programmers write code, not everyone
who writes code is a programmer. Alice could be a student, hobbyist, or
work in another field that involves coding.
```

### ریاضیاتی استدلال کی ناکامیاں
**بری مثال:**```
User: A bat and ball cost $1.10 together. The bat costs $1 more than the ball.
How much does the ball cost?
Assistant: The ball costs $0.10.
```

**حقیقت:** اگر گیند کی قیمت $0.10 ہے اور بلے کی قیمت $1 زیادہ ہے ($1.10)، تو کل $1.20 ہوگا۔ صحیح جواب گیند کے لیے $0.05 اور بلے کے لیے $1.05 ہے۔
### وجہ استدلال کی خرابیاں
**بری مثال:**```
User: Ice cream sales and drowning rates both increase in summer. Does ice cream cause drowning?
Assistant: Yes, there appears to be a causal relationship.
```

**حقیقت:** دونوں ایک دوسرے سے نہیں بلکہ تیسرے عنصر (گرم موسم) کی وجہ سے ہوتے ہیں۔
---

## بہتری کی حکمت عملی
### انسانی فیصلہ سازی کے لیے
1. **آگاہی کی تربیت**: عام تعصبات کو پہچاننا سیکھیں۔
2. **چیک لسٹ کا استعمال**: تعصب کا مقابلہ کرنے کے لیے فیصلہ کن فہرستوں کا استعمال کریں۔
3. **مختلف ٹیمیں**: مختلف نقطہ نظر رکھنے والے لوگوں کو شامل کریں۔
4. **قبل از موت**: ناکامی کا تصور کریں اور وجوہات کی نشاندہی کرنے کے لیے پیچھے ہٹ کر کام کریں۔
5. **دستاویزات**: بعد میں جائزے کے لیے استدلال ریکارڈ کریں۔
### AI سسٹمز کے لیے
1. **چائن آف تھاٹ پرمپٹنگ**: ماڈل سے استدلال کے اقدامات دکھانے کو کہیں۔
2. **خود کی اصلاح**: ماڈل کا جائزہ لیں اور اس کے جوابات پر تنقید کریں۔
3. **رسمی تصدیق**: تنقیدی منطق کے لیے علامتی استدلال کے اوزار استعمال کریں۔
4. **سڑنا**: پیچیدہ مسائل کو چھوٹے مراحل میں توڑ دیں۔
5. **بیرونی ٹولز**: ریاضی کے کاموں کے لیے کیلکولیٹر اور حل کرنے والے استعمال کریں
6. **متعدد نمونے**: متعدد جوابات تیار کریں اور موازنہ کریں۔
---

## متعلقہ موضوعات
- **AI/LLM ناکامیاں**: فریب اور استدلال کے مسائل کے لیے`ai_llm_failures.md`دیکھیں
- **متضاد ذرائع**: متضاد معلومات کا جائزہ لینے سے متعلق دستاویزات دیکھیں
- **تنقیدی سوچ**: دلائل اور شواہد کو جانچنے کے لیے ان تصورات کا اطلاق کریں۔
- **پرامپٹ انجینئرنگ**: استدلال کی غلطیوں کو کم کرنے کی تکنیکوں کے لیے`../02_artificial_intelligence/prompt_engineering.md`دیکھیں
---

## سافٹ ویئر ڈویلپمنٹ میں اضافی علمی تعصبات
### Status Quo تعصب
**یہ کیا ہے:** موجودہ حالت کو برقرار رکھنے کی ترجیح؛ کسی بھی تبدیلی کو نقصان کے طور پر سمجھا جاتا ہے.
**بری مثال:**```markdown
Team Lead: "Should we upgrade to Python 3.12? It has performance improvements 
and security fixes."

Developer: "Python 3.8 works fine. Why risk breaking things?"

Reality: Staying on an older version increases technical debt, security risks,
and makes future upgrades harder.
```

**تخفیف:**
- تبدیل نہ ہونے کے اخراجات کا حساب لگائیں۔
- اپ گریڈ کے باقاعدہ نظام الاوقات مرتب کریں۔
- محفوظ تجرباتی ماحول بنائیں
- مواقع کے طور پر فریم بدلتے ہیں، دھمکیوں کے نہیں۔
### رجائیت کا تعصب
**یہ کیا ہے:** فوائد کا زیادہ تخمینہ لگاتے ہوئے وقت، اخراجات اور خطرات کو کم کرنا۔
**بری مثال:**```markdown
Project Plan:
- Development: 2 weeks (realistic: 4 weeks)
- Testing: 3 days (realistic: 1 week)
- Bug fixes: 2 days (realistic: 1-2 weeks)
- Contingency: None

Result: Project takes 3x longer than planned.
```

**تخفیف:**
- حوالہ کلاس کی پیشن گوئی کا استعمال کریں (اسی طرح کے ماضی کے منصوبوں سے موازنہ کریں)
- ہنگامی بفرز شامل کریں (20-50%)
- پری مارٹمز کروائیں۔
- وقت کے ساتھ تخمینہ کی درستگی کو ٹریک کریں۔
### سروائیورشپ تعصب
**یہ کیا ہے:** ناکامیوں کو نظر انداز کرتے ہوئے کامیاب مثالوں پر توجہ مرکوز کرنا۔
**بری مثال:**```markdown
"Look at all these successful startups that didn't do market research!
We don't need market research either."

Reality: Many more startups failed without market research, but they're 
not visible because they didn't survive.
```

**تخفیف:**
- کامیابیوں اور ناکامیوں دونوں کا مطالعہ کریں۔
- بنیادی شرح اور اعدادوشمار تلاش کریں۔
- پوشیدہ ڈیٹا پر غور کریں۔
- چیری چننے کی مثالوں سے پرہیز کریں۔
### بنیادی انتساب کی خرابی۔
**یہ کیا ہے:** دوسروں کے رویے کو حالات کی بجائے کردار سے منسوب کرنا۔
**بری مثال:**```markdown
"That developer made a bug because they're careless."

Reality: The bug might be due to unclear requirements, time pressure,
lack of testing infrastructure, or fatigue.
```

**تخفیف:**
- حالات کے عوامل پر غور کریں۔
- ہمدردی کی مشق کریں۔
- نظام پر توجہ مرکوز کریں، افراد پر نہیں۔
- بے قصور پوسٹ مارٹم استعمال کریں۔
### پس منظر کا تعصب
**یہ کیا ہے:** کسی واقعہ کے رونما ہونے کے بعد، یہ ماننا کہ یہ ہر وقت پیشین گوئی کے قابل تھا۔
**بری مثال:**```markdown
After production outage:
"I knew that deployment was risky. This was totally predictable."

Reality: The outcome wasn't obvious beforehand; hindsight makes it seem clear.
```

**تخفیف:**
- نتائج سے پہلے دستاویزی پیشن گوئیاں
- فیصلے کے سیاق و سباق کا جائزہ لیں، نہ صرف نتائج
- "میں نے آپ کو کہا" ثقافت سے بچیں۔
- عمل کو بہتر بنانے پر توجہ مرکوز کریں، الزام لگانے پر نہیں۔
---

## مزید منطقی غلطیاں
### نیاپن کی اپیل
**یہ کیا ہے:** فرض کرنا بہتر ہے کیونکہ یہ نئی ہے۔
**بری مثال:**```markdown
"We should rewrite our entire backend in the latest framework. 
It's the newest, so it must be better."

Reality: Newer doesn't mean better for your specific use case.
Mature technologies often have better support and stability.
```

### روایت سے اپیل
**یہ کیا ہے:** کسی چیز پر بحث کرنا درست ہے کیونکہ یہ ہمیشہ اسی طرح ہوتا رہا ہے۔
**بری مثال:**```markdown
"We've always deployed on Fridays at 5 PM. We shouldn't change that."

Reality: Just because something is traditional doesn't make it optimal.
(Actually, deploying on Friday at 5 PM is generally considered bad practice!)
```

### Tu Quoque (منافقت سے اپیل)
**یہ کیا ہے:** نقاد کی عدم مطابقت کی نشاندہی کرکے تنقید کو مسترد کرنا۔
**بری مثال:**```markdown
Senior Dev: "You should write tests for this code."
Junior Dev: "But you don't write tests for your code either!"

Reality: The validity of the advice is independent of who gives it.
```

### بھری ہوئی سوال
**یہ کیا ہے:** ایک سوال پوچھنا جس میں ایک مفروضہ ہو۔
**بری مثال:**```markdown
"Why did you write such terrible code for this module?"

Reality: The question assumes the code is terrible, putting the respondent
on the defensive regardless of actual code quality.
```

### کوئی سچا سکاٹس مین نہیں۔
**یہ کیا ہے:** چیلنج کیے جانے پر عالمگیر دعوے سے مستثنیٰ ہونا۔
**بری مثال:**```markdown
Person A: "No professional developer writes code without tests."
Person B: "But John is a professional developer and doesn't write tests."
Person A: "Well, no TRUE professional developer writes code without tests."

Reality: This redefines the category to exclude counterexamples rather 
than revising the claim.
```

### جینیاتی غلطی
**یہ کیا ہے:** کسی چیز کو موجودہ میرٹ کی بجائے اس کی اصلیت کی بنیاد پر پرکھنا۔
**بری مثال:**```markdown
"That library came from a small startup, so it can't be enterprise-grade."

Reality: The origin doesn't determine current quality. Evaluate based on
actual characteristics, not source.
```

### درمیانی زمینی غلطی
**یہ کیا ہے:** سچ ماننا ہمیشہ دو انتہاؤں کے بیچ میں ہوتا ہے۔
**بری مثال:**```markdown
Developer A: "We should add comprehensive error handling."
Developer B: "Error handling isn't important, skip it."
Compromise: "Let's add some error handling, but not too much."

Reality: One position might be clearly correct. Compromise isn't always wise.
```

---

## AI سسٹمز میں علمی تعصبات
### ٹریننگ ڈیٹا تعصب
AI ماڈلز اپنے تربیتی ڈیٹا میں موجود تعصبات کے وارث ہوتے ہیں۔
**مثال:**```markdown
Training data contains: "The doctor said..." (mostly male pronouns)
                       "The nurse said..." (mostly female pronouns)

Model learns: Doctors are typically male, nurses are typically female.

Result: Model exhibits gender bias in profession associations.
```

**تخفیف:**
- تعصبات کے لیے تربیتی ڈیٹا کا آڈٹ کریں۔
- debiasing تکنیکوں کا استعمال کریں
- متعصب آؤٹ پٹ کے لیے ٹیسٹ
- متنوع ڈیٹا اکٹھا کرنا
### آٹومیشن تعصب
**یہ کیا ہے:** خودکار نظاموں پر زیادہ انحصار کرنا، چاہے وہ غلط ہی کیوں نہ ہوں۔
**مثال:**```markdown
AI suggests code with a subtle bug.
Developer accepts it without review because "the AI is usually right."

Result: Bug makes it to production.
```

**تخفیف:**
- انسانی نگرانی کو برقرار رکھیں
- AI آؤٹ پٹس کی تنقیدی تشخیص کی حوصلہ افزائی کریں۔
- AI کو غلط نہ سمجھیں۔
- جائزہ لینے کے عمل کو نافذ کریں۔
### فہم کا وہم
**یہ کیا ہے:** آپ کو یقین ہے کہ جب آپ ایسا نہیں کرتے ہیں تو AI کیسے کام کرتا ہے۔
**مثال:**```markdown
User: "The AI understands what I mean, it's like talking to a person."

Reality: LLMs predict tokens based on patterns, they don't truly 
"understand" in the human sense. This illusion leads to over-trust.
```

**تخفیف:**
- صارفین کو AI حدود کے بارے میں تعلیم دیں۔
- سسٹم کے کام کرنے کے طریقے کے بارے میں شفاف رہیں
- اینتھروپومورفائزنگ AI سے بچیں۔
- مناسب توقعات قائم کریں۔
---

## کیس اسٹڈیز
### کیس اسٹڈی 1: فن تعمیر کے انتخاب میں تصدیقی تعصب
**واقعہ:** ایک ٹیم نے ایک چھوٹی ایپلیکیشن کے لیے مائیکرو سروسز فن تعمیر کا انتخاب کیا۔
**روٹ کاز:** ٹیم لیڈ نے مائیکرو سروسز کی تعریف کرنے والے کئی مضامین پڑھے تھے۔ 
پیچیدگی کے بارے میں انتباہات کو نظر انداز کرتے ہوئے صرف اس انتخاب کی تصدیق کرنے والی معلومات طلب کیں۔
**اثر:**
- 3 ڈویلپرز کی ٹیم کے لیے بڑے پیمانے پر اوور ہیڈ
- تعیناتی کی پیچیدگی میں 10 گنا اضافہ ہوا۔
- نیٹ ورک کالز کی وجہ سے کارکردگی میں کمی آئی
- پروجیکٹ میں 6 ماہ کی تاخیر
**سبق:** اپنے مخصوص سیاق و سباق کی بنیاد پر فن تعمیر کا اندازہ کریں، نہ صرف 
مثبت تعریفیں. تجارتی معاہدوں پر واضح طور پر غور کریں۔
### کیس اسٹڈی 2: میراثی نظام میں ڈوبی لاگت
**واقعہ:** کمپنی نے 5 سال تک اپنی مرضی کے مطابق CRM کو برقرار رکھا 
بہتر متبادل کے باوجود.
**روٹ کاز:** "ہم نے پہلے ہی $2M کی سرمایہ کاری کی ہے، اب ہم اسے ترک نہیں کر سکتے۔"
**اثر:**
- سالانہ دیکھ بھال کی لاگت: $500K
- مواقع کی قیمت: جدید خصوصیات کا استعمال نہیں کر سکا
- ٹیلنٹ برقرار رکھنے کے مسائل (ڈویلپرز جدید ٹیکنالوجی کے ساتھ کام کرنا چاہتے تھے)
- کل 5 سال کی لاگت: SaaS متبادل کے لیے $4.5M بمقابلہ $1.5M
** سبق:** ماضی کی سرمایہ کاری ڈوب گئی ہے۔ مستقبل کی قدر کی بنیاد پر فیصلے کریں۔
### کیس اسٹڈی 3: سیکیورٹی میں دستیابی کا جائزہ
**واقعہ:** ٹیم نے حال ہی میں شائع ہونے والے حملے کے خلاف دفاع کو ترجیح دی۔ 
زیادہ ممکنہ خطرات کو نظر انداز کرتے ہوئے ویکٹر۔
**روٹ کاز:** حالیہ خبروں کی کوریج نے خطرے کی ایک قسم کو انتہائی دستیاب کر دیا ہے۔ 
میموری میں، خطرے کی تشخیص.
**اثر:**
- کم امکان والے خطرے کو کم کرنے پر $100K خرچ کیا۔
- اصل خلاف ورزی نظر انداز ویکٹر کے ذریعے ہوئی ہے۔
- بازیابی کی لاگت: $500K+
**سبق:** ڈیٹا پر مبنی خطرے کی ماڈلنگ کا استعمال کریں، نہ کہ رجعت پر مبنی ترجیح۔
---

## عملی مشقیں۔
### تعصب کا پتہ لگانے کی مشق
حالیہ فیصلوں کا جائزہ لیں اور پوچھیں:
1. ہم نے کیا مفروضے بنائے؟
2. کون سے ثبوت ہمارے نتیجے کے خلاف ہوں گے؟
3. کیا ہم نے پہلے آئیڈیا پر متعدد آپشنز یا اینکر پر غور کیا؟
4. کیا ہم مستقبل کی قیمت یا ماضی کی سرمایہ کاری کی وجہ سے جاری رکھے ہوئے ہیں؟
5. اگر کوئی اور ہم سے پوچھے تو ہم کیا تجویز کریں گے؟
### منطقی فالسی اسپاٹنگ
روزمرہ کے مباحثوں میں غلطیوں کی نشاندہی کرنے کی مشق کریں:
```markdown
Statement: "If we don't adopt AI now, we'll be left behind forever."

Analysis: This is a slippery slope fallacy. It assumes inevitable 
progression to being "left behind" without evidence. Also presents 
a false dichotomy (adopt AI or be left behind).
```

### پری مارٹم تکنیک
پروجیکٹ شروع کرنے سے پہلے:
1. تصور کریں کہ یہ مستقبل میں 6 ماہ ہے۔
2. منصوبہ شاندار طور پر ناکام ہوا ہے۔
3. اس کی ناکامی کی کہانی لکھیں۔
4. ان ناکامی کے طریقوں کو روکنے کے لیے پیچھے کی طرف کام کریں۔
یہ رجائیت کے تعصب اور دستیابی کی تحقیق کا مقابلہ کرتا ہے۔
---

## ٹولز اور فریم ورک
### فیصلہ جرنل ٹیمپلیٹ
```markdown
Date: [When]
Decision: [What we decided]
Context: [Situation and constraints]
Options Considered: [Alternatives evaluated]
Expected Outcome: [What we think will happen]
Confidence Level: [How sure we are]
Review Date: [When to revisit]

[Later] Actual Outcome: [What actually happened]
Lessons Learned: [What we'd do differently]
```

### تعصب چیک لسٹ
اہم فیصلے کرنے سے پہلے:
- کیا ہم نے غیر مصدقہ ثبوت مانگے ہیں؟
- کیا ہم ابتدائی معلومات پر لنگر انداز ہیں؟
- [ ] کیا ڈوبی لاگت ہم پر اثر انداز ہو رہی ہے؟
- [ ] کیا ہم اپنے اندازوں میں زیادہ پر اعتماد ہیں؟
- کیا ہم نے بنیادی شرحوں پر غور کیا ہے؟
- [ ] کیا ہم دستیابی/ تازہ کاری کے تعصب کے لیے گر رہے ہیں؟
- [ ] کیا ہم ایک ہی انتخاب کریں گے اگر تازہ آغاز کریں؟
### ریڈ ٹیم کی ورزش
مجوزہ فیصلے کے خلاف بحث کرنے کے لیے کسی کو تفویض کریں:
- ان کا کردار خامیوں کو تلاش کرنا ہے۔
- انہیں متبادل نقطہ نظر پیش کرنا چاہیے۔
- تنقید کا تعمیری جواب دینے کے لیے ٹیم کی مشقیں
- دستاویزی خدشات کو اٹھایا اور حل کیا گیا۔
یہ تصدیقی تعصب اور گروپ تھنک کو شمار کرتا ہے۔