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
# سوگیری های شناختی و مغالطه های منطقی
این سند سوگیری‌های شناختی، مغالطه‌های منطقی و خطاهای استدلالی را که هم بر تصمیم‌گیری انسانی و هم بر خروجی‌های سیستم هوش مصنوعی تأثیر می‌گذارند، ادغام می‌کند.
---

## سوگیری های شناختی
سوگیری های شناختی الگوهای سیستماتیک انحراف از عقلانیت در قضاوت و تصمیم گیری هستند. در توسعه نرم‌افزار و سیستم‌های هوش مصنوعی، این موارد می‌تواند منجر به تصمیم‌های طراحی ضعیف، الزامات معیوب و رفتار مدل مغرضانه شود.
### سوگیری تایید
**چیست:** تمایل به جستجو، تفسیر و یادآوری اطلاعات به گونه ای که باورهای قبلی را تأیید کند.
**نمونه بد در توسعه:**```python
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

**در بررسی کد:**```markdown
Developer A (senior): "This looks good, nice work!"
Developer B (junior): "This has several potential issues..."

Team accepts Developer A's review without scrutiny but questions Developer B's feedback excessively.
```

**تخفیف:**
- به طور فعال به دنبال شواهد نادرست باشید
- از بررسی کدهای کور استفاده کنید
- نظرات مخالف را تشویق کنید
- مفروضات را به صراحت مستند کنید
### تعصب لنگر انداختن
**چیست:** تکیه بیش از حد به اولین اطلاعاتی که با آن مواجه شدیم.
**مثال بد:**```markdown
Project Manager: "This feature should take about 2 days."
Developer: (Anchored to 2 days, even though realistic estimate is 5 days)
"Okay, I'll try to finish in 2 days."

Result: Rushed work, technical debt, missed deadlines anyway.
```

**تخفیف:**
- چندین تخمین مستقل دریافت کنید
- از پوکر برنامه ریزی برای تخمین استفاده کنید
- به جای تخمین نقطه ای محدوده ها را در نظر بگیرید
- ارجاع داده های تاریخی
### اشتباه هزینه غرق شده
**چیست:** ادامه تلاش به دلیل منابع سرمایه گذاری شده قبلی (زمان، پول، تلاش)، حتی زمانی که رها کردن آن بهتر است.
**مثال بد:**```markdown
"We've already spent 6 months building this custom framework. 
We can't switch to the industry standard now, even though 
it would save us time in the long run."
```

**تخفیف:**
- ارزیابی تصمیمات بر اساس ارزش آینده، نه سرمایه گذاری گذشته
- به طور منظم قابلیت اجرای پروژه را مورد ارزیابی مجدد قرار دهید
-ایمنی روانی برای پیوتینگ ایجاد کنید
- از معیارهای عینی برای تصمیمات ادامه/توقف استفاده کنید
### اکتشافی در دسترس بودن
**چیست:** بیش از حد اهمیت دادن به اطلاعاتی که به آسانی در دسترس یا جدید هستند.
**مثال بد:**```markdown
"I just read about a SQL injection attack, so we should 
prioritize SQL injection prevention over XSS, even though 
our security audit shows XSS is our bigger risk."
```

**تخفیف:**
- از تصمیم گیری مبتنی بر داده استفاده کنید
- با مدل های تهدید جامع مشورت کنید
- به نرخ های پایه و آمار نگاه کنید
- از تعصبات اخیر در اولویت بندی خودداری کنید
### اثر دانینگ-کروگر
**چیست:** افراد با توانایی پایین در یک کار، توانایی خود را بیش از حد ارزیابی می کنند. کارشناسان ممکن است نظرات خود را دست کم بگیرند.
**مثال بد:**```markdown
Junior Developer: "I've completed a Python tutorial. 
I'm ready to architect our entire microservices platform."

Senior Developer: "I've been building distributed systems for 10 years. 
I'm probably missing something important in this design."
```

**تخفیف:**
- تشویق به یادگیری مستمر
- اجرای فرآیندهای بررسی همتایان
- ایجاد برنامه های مربیگری
- فروتنی و کنجکاوی را پرورش دهید
---

## اشتباهات منطقی
مغالطات منطقی خطاهایی در استدلال هستند که اعتبار استدلال را تضعیف می کنند. مدل‌های هوش مصنوعی می‌توانند خروجی‌هایی حاوی این اشتباهات تولید کنند.
### Ad Hominem (حمله علیه شخص)
**چیست:** حمله به فردی که بحث می کند نه خود بحث.
**مثال بد:**```markdown
"This code review is wrong because the reviewer is a junior developer."
```

**چرا بد است:** اعتبار بازخورد به محتوای آن بستگی دارد، نه به ارشدیت داور.
### درخواست تجدید نظر از مقامات
**چیست:** ادعای چیزی درست است زیرا یک مرجع این را بدون مدرک می گوید.
**مثال بد:**```markdown
"This architecture must be correct because Google uses it."
```

**چرا بد است:** آنچه برای Google در مقیاس خود کار می کند ممکن است برای مورد استفاده شما کارایی نداشته باشد.
### دوگانگی کاذب (تفکر سیاه و سفید)
**چیست:** ارائه تنها دو گزینه در صورت وجود بیشتر.
**مثال بد:**```markdown
"We either rewrite everything in Rust or accept that our 
codebase will always be slow and buggy."
```

**واقعیت:** گزینه های زیادی بین این افراط وجود دارد (بهینه سازی مسیرهای داغ، استفاده از Rust برای اجزای خاص، بهبود کد پایتون و غیره)
### شیب لغزنده
**چیست:** استدلال اینکه یک رویداد به ناچار منجر به زنجیره ای از پیامدهای منفی می شود.
**مثال بد:**```markdown
"If we allow this small technical debt, soon our entire 
codebase will be unmaintainable and the company will fail."
```

**چرا بد است:** پیشرفت اجتناب ناپذیر بدون شواهد را فرض می کند. عوامل کاهش دهنده را نادیده می گیرد
### استدلال دایره ای
**چیست:** استفاده از نتیجه گیری به عنوان مقدمه.
**مثال بد:**```markdown
"Our code is high quality because we write good code."
```

### Post Hoc Ergo Propter Hoc (علت نادرست)
**چیست:** با فرض اینکه چون B از A پیروی می کند، A باعث B شده است.
**مثال بد:**```markdown
"We deployed the new feature and then saw increased latency. 
The new feature must be causing the latency."
```

**واقعیت:** همبستگی دلالت بر علیت ندارد. عوامل دیگری نیز می تواند مسئول باشد.
### مرد نی
**چیست:** ارائه نادرست استدلال کسی برای آسانتر کردن حمله.
**مثال بد:**```markdown
Developer A: "We should add more tests for edge cases."
Developer B: "So you want us to spend all our time writing tests 
and never ship features?"
```

### مغالطه باند واگن
**چیست:** بحث کردن درباره چیزی درست است زیرا بسیاری از مردم آن را باور دارند.
**مثال بد:**```markdown
"Everyone is using Kubernetes, so we should too."
```

**چرا بد است:** محبوبیت مناسب بودن برای نیازهای خاص شما را تضمین نمی کند.
---

## دلیل شکست در هوش مصنوعی
### خطاهای منطقی چند مرحله ای
**مثال بد:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Yes, Alice must be a programmer.
```

**چرا بد است:**
- مرتکب مغالطه تأیید نتیجه می شود
- آلیس می توانست بدون برنامه نویسی کد بنویسد
- ساختار منطقی: (P→Q، Q) ⊬ P
**دلیل صحیح:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Not necessarily. While all programmers write code, not everyone
who writes code is a programmer. Alice could be a student, hobbyist, or
work in another field that involves coding.
```

### شکست های استدلال ریاضی
**مثال بد:**```
User: A bat and ball cost $1.10 together. The bat costs $1 more than the ball.
How much does the ball cost?
Assistant: The ball costs $0.10.
```

**واقعیت:** اگر قیمت توپ 0.10 دلار و خفاش 1 دلار بیشتر (1.10 دلار) قیمت داشته باشد، مجموع آن 1.20 دلار خواهد بود. پاسخ صحیح 0.05 دلار برای توپ و 1.05 دلار برای خفاش است.
### خطاهای استدلال علّی
**مثال بد:**```
User: Ice cream sales and drowning rates both increase in summer. Does ice cream cause drowning?
Assistant: Yes, there appears to be a causal relationship.
```

**واقعیت:** هر دو ناشی از یک عامل سوم (هوای گرم) هستند، نه توسط یکدیگر.
---

## استراتژی برای بهبود
### برای تصمیم گیری انسانی
1. **آموزش آگاهی**: یاد بگیرید که سوگیری های رایج را تشخیص دهید
2. **استفاده از چک لیست**: از چک لیست های تصمیم گیری برای مقابله با سوگیری ها استفاده کنید
3. **تیم های متنوع**: افرادی با دیدگاه های مختلف را شامل شود
4. **قبل از مرگ**: شکست را تصور کنید و برای شناسایی علل به عقب کار کنید
5. **مستندات**: استدلال را برای بررسی بعدی ثبت کنید
### برای سیستم های هوش مصنوعی
1. **تشویق زنجیره ای از فکر**: از مدل بخواهید مراحل استدلال را نشان دهد.
2. **خود اصلاحی**: مدل را بررسی و پاسخ های آن را نقد کنید
3. **تأیید رسمی **: از ابزارهای استدلال نمادین برای منطق انتقادی استفاده کنید
4. **تجزیه**: مسائل پیچیده را به مراحل کوچکتر تقسیم کنید
5. **ابزارهای خارجی**: استفاده از ماشین حساب و حل کننده برای کارهای ریاضی
6. **نمونه های چندگانه**: پاسخ های متعدد ایجاد کنید و مقایسه کنید
---

## موضوعات مرتبط
- **شکست های AI/LLM**: برای توهمات و مسائل استدلالی به`ai_llm_failures.md`مراجعه کنید
- **منابع متناقض**: به مستندات ارزیابی اطلاعات متناقض مراجعه کنید
- **تفکر انتقادی**: از این مفاهیم برای ارزیابی استدلال ها و شواهد استفاده کنید
- **مهندسی سریع**: برای تکنیک های کاهش خطاهای استدلالی به`../02_artificial_intelligence/prompt_engineering.md`مراجعه کنید
---

## سوگیری های شناختی اضافی در توسعه نرم افزار
### تعصب وضعیت موجود
**چیست:** ترجیح برای حفظ وضعیت فعلی. هر تغییری به عنوان ضرر تلقی می شود.
**مثال بد:**```markdown
Team Lead: "Should we upgrade to Python 3.12? It has performance improvements 
and security fixes."

Developer: "Python 3.8 works fine. Why risk breaking things?"

Reality: Staying on an older version increases technical debt, security risks,
and makes future upgrades harder.
```

**تخفیف:**
- هزینه های عدم تغییر را کمی کنید
- برنامه های مرتب ارتقاء را تنظیم کنید
- محیط های آزمایشی ایمن ایجاد کنید
- تغییر چارچوب به عنوان فرصت، نه تهدید
### تعصب خوش بینی
**چیست:** دست کم گرفتن زمان، هزینه ها و خطرات در حالی که مزایا را بیش از حد برآورد می کند.
**مثال بد:**```markdown
Project Plan:
- Development: 2 weeks (realistic: 4 weeks)
- Testing: 3 days (realistic: 1 week)
- Bug fixes: 2 days (realistic: 1-2 weeks)
- Contingency: None

Result: Project takes 3x longer than planned.
```

**تخفیف:**
- استفاده از پیش بینی کلاس مرجع (مقایسه با پروژه های مشابه قبلی)
- اضافه کردن بافرهای احتمالی (20-50٪)
- انجام پیش از مرگ
- دقت برآورد را در طول زمان پیگیری کنید
### تعصب بقا
**چیست:** تمرکز بر نمونه های موفق و در عین حال نادیده گرفتن شکست ها.
**مثال بد:**```markdown
"Look at all these successful startups that didn't do market research!
We don't need market research either."

Reality: Many more startups failed without market research, but they're 
not visible because they didn't survive.
```

**تخفیف:**
- هم موفقیت ها و هم شکست ها را مطالعه کنید
- به دنبال نرخ های پایه و آمار باشید
- داده های نامرئی را در نظر بگیرید
- از نمونه های چیدن گیلاس خودداری کنید
### خطای اسناد اساسی
**چیست:** نسبت دادن رفتار دیگران به شخصیت و نه شرایط.
**مثال بد:**```markdown
"That developer made a bug because they're careless."

Reality: The bug might be due to unclear requirements, time pressure,
lack of testing infrastructure, or fatigue.
```

**تخفیف:**
- عوامل موقعیتی را در نظر بگیرید
- همدلی را تمرین کنید
- روی سیستم ها تمرکز کنید نه افراد
- از پس از مرگ بی تقصیر استفاده کنید
### تعصب پسینی
**چیست:** پس از وقوع یک رویداد، با این باور که همیشه قابل پیش بینی بوده است.
**مثال بد:**```markdown
After production outage:
"I knew that deployment was risky. This was totally predictable."

Reality: The outcome wasn't obvious beforehand; hindsight makes it seem clear.
```

**تخفیف:**
- پیش‌بینی‌ها را قبل از نتایج مستند کنید
- بررسی زمینه تصمیم گیری، نه فقط نتایج
- از فرهنگ "من به شما گفتم" بپرهیزید
- بر بهبود فرآیندها تمرکز کنید، نه سرزنش کردن
---

## مغالطه های منطقی بیشتر
### توسل به تازگی
**چیست:** با فرض اینکه چیزی بهتر است زیرا جدیدتر است.
**مثال بد:**```markdown
"We should rewrite our entire backend in the latest framework. 
It's the newest, so it must be better."

Reality: Newer doesn't mean better for your specific use case.
Mature technologies often have better support and stability.
```

### توسل به سنت
**چیست:** بحث کردن درباره چیزی درست است، زیرا همیشه اینطور انجام می شده است.
**مثال بد:**```markdown
"We've always deployed on Fridays at 5 PM. We shouldn't change that."

Reality: Just because something is traditional doesn't make it optimal.
(Actually, deploying on Friday at 5 PM is generally considered bad practice!)
```

### Tu Quoque (توسل به ریاکاری)
**چیست:** رد انتقاد با اشاره به ناهماهنگی منتقد.
**مثال بد:**```markdown
Senior Dev: "You should write tests for this code."
Junior Dev: "But you don't write tests for your code either!"

Reality: The validity of the advice is independent of who gives it.
```

### سوال بارگذاری شده
**چیست:** پرسیدن سوالی که حاوی یک فرض است.
**مثال بد:**```markdown
"Why did you write such terrible code for this module?"

Reality: The question assumes the code is terrible, putting the respondent
on the defensive regardless of actual code quality.
```

### هیچ اسکاتلندی واقعی
**چیست:** ایجاد استثنا در یک ادعای جهانی در صورت اعتراض.
**مثال بد:**```markdown
Person A: "No professional developer writes code without tests."
Person B: "But John is a professional developer and doesn't write tests."
Person A: "Well, no TRUE professional developer writes code without tests."

Reality: This redefines the category to exclude counterexamples rather 
than revising the claim.
```

### مغالطه ژنتیکی
**چیست:** قضاوت در مورد چیزی بر اساس منشأ آن به جای شایستگی فعلی.
**مثال بد:**```markdown
"That library came from a small startup, so it can't be enterprise-grade."

Reality: The origin doesn't determine current quality. Evaluate based on
actual characteristics, not source.
```

### مغالطه میانی
**چیست:** با فرض اینکه حقیقت همیشه در میانه دو افراط است.
**مثال بد:**```markdown
Developer A: "We should add comprehensive error handling."
Developer B: "Error handling isn't important, skip it."
Compromise: "Let's add some error handling, but not too much."

Reality: One position might be clearly correct. Compromise isn't always wise.
```

---

## سوگیری های شناختی در سیستم های هوش مصنوعی
### تعصب داده های آموزشی
مدل‌های هوش مصنوعی سوگیری‌های موجود در داده‌های آموزشی خود را به ارث می‌برند.
**مثال:**```markdown
Training data contains: "The doctor said..." (mostly male pronouns)
                       "The nurse said..." (mostly female pronouns)

Model learns: Doctors are typically male, nurses are typically female.

Result: Model exhibits gender bias in profession associations.
```

**تخفیف:**
- داده های آموزشی حسابرسی برای سوگیری ها
- از تکنیک های انحرافی استفاده کنید
- برای خروجی های مغرضانه تست کنید
- جمع آوری داده های متنوع
### تعصب اتوماسیون
**چیست:** تکیه بیش از حد به سیستم های خودکار، حتی زمانی که آنها اشتباه می کنند.
**مثال:**```markdown
AI suggests code with a subtle bug.
Developer accepts it without review because "the AI is usually right."

Result: Bug makes it to production.
```

**تخفیف:**
- نظارت انسانی را حفظ کنید
- تشویق ارزیابی انتقادی خروجی های هوش مصنوعی
- با هوش مصنوعی به عنوان خطاناپذیر رفتار نکنید
- اجرای فرآیندهای بازبینی
### توهم درک
**چیست:** باور داشته باشید که می‌دانید هوش مصنوعی چگونه کار می‌کند در حالی که این کار را نمی‌کنید.
**مثال:**```markdown
User: "The AI understands what I mean, it's like talking to a person."

Reality: LLMs predict tokens based on patterns, they don't truly 
"understand" in the human sense. This illusion leads to over-trust.
```

**تخفیف:**
- آموزش کاربران در مورد محدودیت های هوش مصنوعی
- در مورد نحوه عملکرد سیستم ها شفاف باشید
- از انسان‌سازی هوش مصنوعی اجتناب کنید
- انتظارات مناسب را تعیین کنید
---

## مطالعات موردی
### مطالعه موردی 1: سوگیری تایید در انتخاب معماری
**حادثه:** یک تیم یک معماری میکروسرویس را برای یک برنامه کوچک انتخاب کردند.
**علت اصلی:** سرپرست تیم مقالات متعددی را در تمجید از میکروسرویس ها خوانده بود 
فقط به دنبال اطلاعاتی بود که این انتخاب را تأیید کرد، بدون توجه به هشدارها در مورد پیچیدگی.
**تاثیر:**
- سربار هنگفت برای تیمی متشکل از 3 توسعه دهنده
- پیچیدگی استقرار 10 برابر افزایش یافته است
- کاهش عملکرد به دلیل تماس های شبکه
- پروژه با 6 ماه تاخیر
**درس:** معماری ها را بر اساس زمینه خاص خود ارزیابی کنید، نه فقط 
شواهد مثبت مبادلات را به صراحت در نظر بگیرید.
### مطالعه موردی 2: کاهش هزینه در سیستم قدیمی
**حادثه:** شرکت به مدت 5 سال به حفظ CRM سفارشی خود ادامه داد 
با وجود جایگزین های بهتر
**علت اصلی: ** "ما قبلاً 2 میلیون دلار سرمایه گذاری کرده ایم، اکنون نمی توانیم آن را رها کنیم."
**تاثیر:**
- هزینه نگهداری سالانه: 500 هزار دلار
- هزینه فرصت: نمی توان از ویژگی های مدرن استفاده کرد
- مشکلات حفظ استعداد (توسعه دهندگان می خواستند با فناوری مدرن کار کنند)
- هزینه کل 5 ساله: 4.5 میلیون دلار در مقابل 1.5 میلیون دلار برای جایگزین SaaS
**درس:** سرمایه گذاری گذشته غرق شده است. بر اساس ارزش آینده تصمیم بگیرید.
### مطالعه موردی 3: اکتشافی در دسترس بودن در امنیت
**حادثه:** تیم دفاع در برابر حمله اخیراً منتشر شده را در اولویت قرار داد 
بردار در حالی که تهدیدهای محتمل تر را نادیده می گیرند.
**علت اصلی:** پوشش خبری اخیر یک نوع تهدید را بسیار در دسترس قرار داد 
در حافظه، ارزیابی ریسک انحرافی
**تاثیر:**
- 100 هزار دلار برای کاهش تهدید با احتمال کم هزینه کرد
- نقض واقعی از طریق بردار نادیده گرفته شده رخ داده است
- هزینه بازیابی: 500 هزار دلار +
**درس:** از مدل‌سازی تهدید مبتنی بر داده استفاده کنید، نه اولویت‌بندی مبتنی بر تازگی.
---

## تمرینات عملی
### تمرین تشخیص تعصب
تصمیمات اخیر را مرور کنید و بپرسید:
1. چه فرضیاتی داشتیم؟
2. چه شواهدی با نتیجه گیری ما در تضاد است؟
3. آیا چندین گزینه را در نظر گرفتیم یا روی ایده اول لنگر انداختیم؟
4. آیا ما به دلیل ارزش آتی یا سرمایه گذاری گذشته ادامه می دهیم؟
5. اگر شخص دیگری از ما بپرسد چه چیزی را توصیه می کنیم؟
### تشخیص مغالطه منطقی
تشخیص اشتباهات در بحث های روزمره را تمرین کنید:
```markdown
Statement: "If we don't adopt AI now, we'll be left behind forever."

Analysis: This is a slippery slope fallacy. It assumes inevitable 
progression to being "left behind" without evidence. Also presents 
a false dichotomy (adopt AI or be left behind).
```

### تکنیک قبل از مرگ
قبل از شروع پروژه:
1. تصور کنید 6 ماه آینده است
2. پروژه به طرز چشمگیری شکست خورده است
3. داستان چرایی شکست را بنویسید
4. برای جلوگیری از این حالت های شکست، به عقب کار کنید
این با تعصب خوش بینی و اکتشافی در دسترس مقابله می کند.
---

## ابزارها و چارچوب ها
### قالب مجله تصمیم
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

### چک لیست تعصب
قبل از تصمیم گیری مهم:
- [ ] آیا ما به دنبال شواهد نادرست بوده ایم؟
- [ ] آیا ما بر روی اطلاعات اولیه متکی هستیم؟
- [ ] آیا هزینه غرق شده بر ما تأثیر می گذارد؟
- [ ] آیا ما بیش از حد به برآوردهای خود اطمینان داریم؟
- [ ] آیا نرخ های پایه را در نظر گرفته ایم؟
- [ ] آیا ما به دنبال سوگیری در دسترس بودن/تأخر هستیم؟
- [ ] آیا اگر تازه شروع کنیم همین انتخاب را خواهیم داشت؟
### تمرین تیم قرمز
شخصی را مأمور کنید تا علیه تصمیم پیشنهادی استدلال کند:
- نقش آنها یافتن عیوب است
- آنها باید دیدگاه های جایگزین ارائه دهند
- تیم پاسخ سازنده به انتقاد را تمرین می کند
- نگرانی های مستند مطرح شده و رسیدگی شده است
این با سوگیری تایید و تفکر گروهی مقابله می کند.