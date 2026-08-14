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
# জ্ঞানীয় পক্ষপাত এবং যৌক্তিক ভুল
এই নথিটি জ্ঞানীয় পক্ষপাতিত্ব, যৌক্তিক ভুল এবং যুক্তির ত্রুটিগুলিকে একীভূত করে যা মানুষের সিদ্ধান্ত গ্রহণ এবং এআই সিস্টেম আউটপুট উভয়কেই প্রভাবিত করে।
---

## জ্ঞানীয় পক্ষপাত
জ্ঞানীয় পক্ষপাত হল বিচার এবং সিদ্ধান্ত গ্রহণের ক্ষেত্রে যৌক্তিকতা থেকে বিচ্যুতির পদ্ধতিগত নিদর্শন। সফ্টওয়্যার ডেভেলপমেন্ট এবং এআই সিস্টেমে, এগুলি দুর্বল ডিজাইনের সিদ্ধান্ত, ত্রুটিপূর্ণ প্রয়োজনীয়তা এবং পক্ষপাতদুষ্ট মডেল আচরণের দিকে নিয়ে যেতে পারে।
### নিশ্চিতকরণ পক্ষপাতিত্ব
**এটি কী:** এমনভাবে তথ্য অনুসন্ধান, ব্যাখ্যা এবং স্মরণ করার প্রবণতা যা পূর্বে বিদ্যমান বিশ্বাসকে নিশ্চিত করে।
**বিকাশের ক্ষেত্রে খারাপ উদাহরণ:**```python
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

**কোড পর্যালোচনায়:**```markdown
Developer A (senior): "This looks good, nice work!"
Developer B (junior): "This has several potential issues..."

Team accepts Developer A's review without scrutiny but questions Developer B's feedback excessively.
```

**প্রশমন:**
- সক্রিয়ভাবে অস্বীকৃতি প্রমাণের সন্ধান করুন
- অন্ধ কোড পর্যালোচনা ব্যবহার করুন
- ভিন্নমত পোষণ করতে উত্সাহিত করুন
- নথির অনুমান স্পষ্টভাবে
### অ্যাঙ্করিং বায়াস
**এটি কী:** প্রথম যে তথ্যের সম্মুখীন হয়েছে তার উপর খুব বেশি নির্ভর করা।
**খারাপ উদাহরণ:**```markdown
Project Manager: "This feature should take about 2 days."
Developer: (Anchored to 2 days, even though realistic estimate is 5 days)
"Okay, I'll try to finish in 2 days."

Result: Rushed work, technical debt, missed deadlines anyway.
```

**প্রশমন:**
- একাধিক স্বাধীন অনুমান পান
- অনুমানের জন্য পরিকল্পনা পোকার ব্যবহার করুন
- পয়েন্ট অনুমানের পরিবর্তে রেঞ্জ বিবেচনা করুন
- ঐতিহাসিক তথ্য উল্লেখ করুন
### নিমজ্জিত খরচ ফ্যালাসি
**এটি কী:** পূর্বে বিনিয়োগ করা সম্পদের (সময়, অর্থ, প্রচেষ্টা) কারণে একটি প্রচেষ্টা চালিয়ে যাওয়া, এমনকি যখন পরিত্যাগ করা ভাল হবে।
**খারাপ উদাহরণ:**```markdown
"We've already spent 6 months building this custom framework. 
We can't switch to the industry standard now, even though 
it would save us time in the long run."
```

**প্রশমন:**
- অতীত বিনিয়োগ নয়, ভবিষ্যতের মূল্যের উপর ভিত্তি করে সিদ্ধান্তগুলি মূল্যায়ন করুন
- নিয়মিতভাবে প্রকল্পের কার্যকারিতা পুনর্মূল্যায়ন করুন
- পিভটিংয়ের জন্য মনস্তাত্ত্বিক নিরাপত্তা তৈরি করুন
- অবিরত/বন্ধ সিদ্ধান্তের জন্য উদ্দেশ্যমূলক মানদণ্ড ব্যবহার করুন
### প্রাপ্যতা হিউরিস্টিক
**এটি কী:** সহজলভ্য বা সাম্প্রতিক তথ্যের গুরুত্বকে অতিমূল্যায়ন করা।
**খারাপ উদাহরণ:**```markdown
"I just read about a SQL injection attack, so we should 
prioritize SQL injection prevention over XSS, even though 
our security audit shows XSS is our bigger risk."
```

**প্রশমন:**
- ডেটা-চালিত সিদ্ধান্ত গ্রহণ ব্যবহার করুন
- ব্যাপক হুমকি মডেলের সাথে পরামর্শ করুন
- বেস রেট এবং পরিসংখ্যান দেখুন
- অগ্রাধিকারের ক্ষেত্রে নতুনত্বের পক্ষপাত এড়িয়ে চলুন
### ডানিং-ক্রুগার প্রভাব
**এটা কী বিশেষজ্ঞরা তাদের অবমূল্যায়ন করতে পারে।
**খারাপ উদাহরণ:**```markdown
Junior Developer: "I've completed a Python tutorial. 
I'm ready to architect our entire microservices platform."

Senior Developer: "I've been building distributed systems for 10 years. 
I'm probably missing something important in this design."
```

**প্রশমন:**
- ক্রমাগত শেখার উত্সাহ দিন
- পিয়ার রিভিউ প্রক্রিয়া বাস্তবায়ন করুন
- মেন্টরশিপ প্রোগ্রাম তৈরি করুন
- নম্রতা এবং কৌতূহল বৃদ্ধি করুন
---

## যৌক্তিক ভুল
যৌক্তিক ভ্রান্তি হল যুক্তিতে ত্রুটি যা যুক্তির বৈধতাকে দুর্বল করে। এআই মডেলগুলি এই ভুলগুলি ধারণকারী আউটপুট তৈরি করতে পারে।
### অ্যাড হোমিনেম (ব্যক্তির বিরুদ্ধে আক্রমণ)
**এটি কী:** যুক্তির পরিবর্তে যুক্তি প্রদানকারী ব্যক্তিকে আক্রমণ করা।
**খারাপ উদাহরণ:**```markdown
"This code review is wrong because the reviewer is a junior developer."
```

**এটি কেন খারাপ:** প্রতিক্রিয়ার বৈধতা তার বিষয়বস্তুর উপর নির্ভর করে, পর্যালোচনাকারীর জ্যেষ্ঠতার উপর নয়।
### কর্তৃপক্ষের কাছে আবেদন
**এটি কী:** কোনো কিছু দাবি করা সত্য কারণ কোনো কর্তৃপক্ষের ব্যক্তি প্রমাণ ছাড়াই তা বলে।
**খারাপ উদাহরণ:**```markdown
"This architecture must be correct because Google uses it."
```

**কেন এটা খারাপ:** Google এর স্কেলে যা কাজ করে তা আপনার ব্যবহারের ক্ষেত্রে কাজ নাও করতে পারে।
### মিথ্যা দ্বিধাবিভক্তি (কালো-সাদা চিন্তা)
**এটি কী:** আরও উপস্থিত থাকলে শুধুমাত্র দুটি বিকল্প উপস্থাপন করা হচ্ছে।
**খারাপ উদাহরণ:**```markdown
"We either rewrite everything in Rust or accept that our 
codebase will always be slow and buggy."
```

**বাস্তবতা:** এই চরমগুলির মধ্যে অনেকগুলি বিকল্প বিদ্যমান (হট পাথ অপ্টিমাইজ করুন, নির্দিষ্ট উপাদানগুলির জন্য মরিচা ব্যবহার করুন, পাইথন কোড উন্নত করুন, ইত্যাদি)
### পিচ্ছিল ঢাল
**এটি কী:** যুক্তি দেওয়া যে একটি ঘটনা অনিবার্যভাবে নেতিবাচক পরিণতির একটি শৃঙ্খলের দিকে নিয়ে যাবে।
**খারাপ উদাহরণ:**```markdown
"If we allow this small technical debt, soon our entire 
codebase will be unmaintainable and the company will fail."
```

**কেন এটা খারাপ:** প্রমাণ ছাড়াই অনিবার্য অগ্রগতি অনুমান করে; প্রশমিত কারণ উপেক্ষা করে।
### সার্কুলার রিজনিং
**এটা কি:** উপসংহারকে ভিত্তি হিসেবে ব্যবহার করা।
**খারাপ উদাহরণ:**```markdown
"Our code is high quality because we write good code."
```

### Post Hoc Ergo Propter Hoc (মিথ্যা কারণ)
**এটা কি:** ধরে নিচ্ছি যে B A এর অনুসরণ করেছে, A এর ফলে B হয়েছে।
**খারাপ উদাহরণ:**```markdown
"We deployed the new feature and then saw increased latency. 
The new feature must be causing the latency."
```

**বাস্তবতা:** পারস্পরিক সম্পর্ক কার্যকারণকে বোঝায় না। অন্যান্য কারণ দায়ী হতে পারে।
### খড়ের মানুষ
**এটি কী:** আক্রমণ করা সহজ করার জন্য কারও যুক্তিকে ভুলভাবে উপস্থাপন করা।
**খারাপ উদাহরণ:**```markdown
Developer A: "We should add more tests for edge cases."
Developer B: "So you want us to spend all our time writing tests 
and never ship features?"
```

### ব্যান্ডওয়াগন ফ্যালাসি
**এটা কি:** কিছু তর্ক করা সঠিক কারণ অনেক মানুষ এটা বিশ্বাস করে।
**খারাপ উদাহরণ:**```markdown
"Everyone is using Kubernetes, so we should too."
```

**কেন এটা খারাপ:** জনপ্রিয়তা আপনার নির্দিষ্ট প্রয়োজনের জন্য উপযুক্ততার নিশ্চয়তা দেয় না।
---

## AI-তে যুক্তির ব্যর্থতা
### মাল্টি-স্টেপ লজিক ত্রুটি
**খারাপ উদাহরণ:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Yes, Alice must be a programmer.
```

**কেন এটা খারাপ:**
- ফলাফল নিশ্চিত করার ভ্রান্তি প্রতিশ্রুতিবদ্ধ
- অ্যালিস প্রোগ্রামার না হয়েও কোড লিখতে পারত
- যৌক্তিক গঠন: (P→Q, Q) ⊬ P
**সঠিক যুক্তি:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Not necessarily. While all programmers write code, not everyone
who writes code is a programmer. Alice could be a student, hobbyist, or
work in another field that involves coding.
```

### গাণিতিক যুক্তিতে ব্যর্থতা
**খারাপ উদাহরণ:**```
User: A bat and ball cost $1.10 together. The bat costs $1 more than the ball.
How much does the ball cost?
Assistant: The ball costs $0.10.
```

**বাস্তবতা:** যদি বলের দাম $0.10 হয় এবং ব্যাটের দাম $1 বেশি ($1.10), তাহলে মোট $1.20 হবে। সঠিক উত্তর হল বলের জন্য $0.05 এবং ব্যাটের জন্য $1.05।
### কারণগত যুক্তি ত্রুটি
**খারাপ উদাহরণ:**```
User: Ice cream sales and drowning rates both increase in summer. Does ice cream cause drowning?
Assistant: Yes, there appears to be a causal relationship.
```

**বাস্তবতা:** উভয়ই একটি তৃতীয় কারণ (গরম আবহাওয়া) দ্বারা সৃষ্ট, একে অপরের দ্বারা নয়।
---

## উন্নতির জন্য কৌশল
### মানুষের সিদ্ধান্ত গ্রহণের জন্য
1. **সচেতনতা প্রশিক্ষণ**: সাধারণ পক্ষপাতগুলি চিনতে শিখুন
2. **চেকলিস্টের ব্যবহার**: পক্ষপাতিত্ব প্রতিরোধ করতে সিদ্ধান্তের চেকলিস্ট ব্যবহার করুন
3. **বিভিন্ন দল**: বিভিন্ন দৃষ্টিভঙ্গি সহ লোকেদের অন্তর্ভুক্ত করুন
4. **প্রি-মর্টেম**: ব্যর্থতার কথা কল্পনা করুন এবং কারণগুলি চিহ্নিত করতে পিছনের দিকে কাজ করুন
5. **ডকুমেন্টেশন**: পরবর্তী পর্যালোচনার জন্য যুক্তি রেকর্ড করুন
### এআই সিস্টেমের জন্য
1. **চেইন-অফ-থট প্রম্পটিং**: মডেলটিকে যুক্তির পদক্ষেপগুলি দেখাতে বলুন
2. **আত্ম-সংশোধন**: মডেলটির পর্যালোচনা করুন এবং এর উত্তরগুলির সমালোচনা করুন৷
3. **আনুষ্ঠানিক যাচাই**: সমালোচনামূলক যুক্তির জন্য প্রতীকী যুক্তি সরঞ্জাম ব্যবহার করুন
4. **পচন**: জটিল সমস্যাগুলিকে ছোট ধাপে ভাগ করুন
5. **বাহ্যিক সরঞ্জাম**: গাণিতিক কাজের জন্য ক্যালকুলেটর এবং সমাধানকারী ব্যবহার করুন
6. **একাধিক নমুনা**: একাধিক প্রতিক্রিয়া তৈরি করুন এবং তুলনা করুন
---

## সম্পর্কিত বিষয়
- **AI/LLM ব্যর্থতা**: হ্যালুসিনেশন এবং যুক্তি সংক্রান্ত সমস্যার জন্য`ai_llm_failures.md`দেখুন
- **পরস্পরবিরোধী সূত্র**: পরস্পরবিরোধী তথ্য মূল্যায়নের ডকুমেন্টেশন দেখুন
- **সমালোচনামূলক চিন্তা**: যুক্তি এবং প্রমাণ মূল্যায়ন করতে এই ধারণাগুলি প্রয়োগ করুন
- **প্রম্পট ইঞ্জিনিয়ারিং**: যুক্তি ত্রুটি কমানোর কৌশলগুলির জন্য`../02_artificial_intelligence/prompt_engineering.md`দেখুন
---

## সফ্টওয়্যার উন্নয়নে অতিরিক্ত জ্ঞানীয় পক্ষপাত
### স্থিতাবস্থার পক্ষপাতিত্ব
**এটি কি:** বর্তমান অবস্থা বজায় রাখার জন্য অগ্রাধিকার; কোন পরিবর্তন ক্ষতি হিসাবে বিবেচিত হয়।
**খারাপ উদাহরণ:**```markdown
Team Lead: "Should we upgrade to Python 3.12? It has performance improvements 
and security fixes."

Developer: "Python 3.8 works fine. Why risk breaking things?"

Reality: Staying on an older version increases technical debt, security risks,
and makes future upgrades harder.
```

**প্রশমন:**
- পরিবর্তিত না হওয়ার খরচ পরিমাপ করুন
- নিয়মিত আপগ্রেড সময়সূচী সেট করুন
- নিরাপদ পরীক্ষার পরিবেশ তৈরি করুন
- সুযোগ হিসাবে ফ্রেম পরিবর্তন, হুমকি নয়
### আশাবাদ পক্ষপাতিত্ব
**এটি কী:** সুবিধার অত্যধিক মূল্যায়ন করার সময় সময়, খরচ এবং ঝুঁকিকে অবমূল্যায়ন করা।
**খারাপ উদাহরণ:**```markdown
Project Plan:
- Development: 2 weeks (realistic: 4 weeks)
- Testing: 3 days (realistic: 1 week)
- Bug fixes: 2 days (realistic: 1-2 weeks)
- Contingency: None

Result: Project takes 3x longer than planned.
```

**প্রশমন:**
- রেফারেন্স ক্লাস পূর্বাভাস ব্যবহার করুন (অতীতের অনুরূপ প্রকল্পের সাথে তুলনা করুন)
- আকস্মিক বাফার যোগ করুন (20-50%)
- প্রি-মর্টেম করা
- সময়ের সাথে অনুমান নির্ভুলতা ট্র্যাক করুন
### সারভাইভারশিপ বায়াস
**এটি কী:** ব্যর্থতা উপেক্ষা করে সফল উদাহরণগুলিতে মনোনিবেশ করা।
**খারাপ উদাহরণ:**```markdown
"Look at all these successful startups that didn't do market research!
We don't need market research either."

Reality: Many more startups failed without market research, but they're 
not visible because they didn't survive.
```

**প্রশমন:**
- সাফল্য এবং ব্যর্থতা উভয়ই অধ্যয়ন করুন
- বেস রেট এবং পরিসংখ্যান দেখুন
- অদৃশ্য তথ্য বিবেচনা করুন
- চেরি বাছাই উদাহরণ এড়িয়ে চলুন
### মৌলিক বৈশিষ্ট্য ত্রুটি
**এটি কী:** পরিস্থিতির পরিবর্তে চরিত্রের প্রতি অন্যের আচরণকে দায়ী করা।
**খারাপ উদাহরণ:**```markdown
"That developer made a bug because they're careless."

Reality: The bug might be due to unclear requirements, time pressure,
lack of testing infrastructure, or fatigue.
```

**প্রশমন:**
- পরিস্থিতিগত কারণ বিবেচনা করুন
- সহানুভূতি অনুশীলন করুন
- সিস্টেমে ফোকাস করুন, ব্যক্তি নয়
- নির্দোষ পোস্ট-মর্টেম ব্যবহার করুন
### হিন্ডসাইট বায়াস
**এটি কী:** একটি ঘটনা ঘটার পরে, বিশ্বাস করা যে এটি সর্বদা পূর্বাভাসযোগ্য ছিল।
**খারাপ উদাহরণ:**```markdown
After production outage:
"I knew that deployment was risky. This was totally predictable."

Reality: The outcome wasn't obvious beforehand; hindsight makes it seem clear.
```

**প্রশমন:**
- ফলাফলের আগে নথির পূর্বাভাস
- সিদ্ধান্তের প্রেক্ষাপট পর্যালোচনা করুন, শুধু ফলাফল নয়
- "আমি তোমাকে তাই বলেছি" সংস্কৃতি এড়িয়ে চলুন
- প্রক্রিয়ার উন্নতিতে ফোকাস করুন, দোষারোপ না করে
---

## আরও যৌক্তিক ভুল
### নতুনত্বের আবেদন
**এটি কী:** কিছু অনুমান করা ভাল কারণ এটি নতুন।
**খারাপ উদাহরণ:**```markdown
"We should rewrite our entire backend in the latest framework. 
It's the newest, so it must be better."

Reality: Newer doesn't mean better for your specific use case.
Mature technologies often have better support and stability.
```

### ঐতিহ্যের প্রতি আবেদন
**এটা কি:** কোনো কিছুর তর্ক করা সঠিক কারণ এটা সবসময়ই সেভাবে করা হয়েছে।
**খারাপ উদাহরণ:**```markdown
"We've always deployed on Fridays at 5 PM. We shouldn't change that."

Reality: Just because something is traditional doesn't make it optimal.
(Actually, deploying on Friday at 5 PM is generally considered bad practice!)
```

### Tu Quoque (কপটতার প্রতি আবেদন)
**এটি কী:** সমালোচকের অসঙ্গতি নির্দেশ করে সমালোচনাকে খারিজ করা।
**খারাপ উদাহরণ:**```markdown
Senior Dev: "You should write tests for this code."
Junior Dev: "But you don't write tests for your code either!"

Reality: The validity of the advice is independent of who gives it.
```

### লোড করা প্রশ্ন
**এটি কী:** এমন একটি প্রশ্ন জিজ্ঞাসা করা যাতে একটি অনুমান রয়েছে।
**খারাপ উদাহরণ:**```markdown
"Why did you write such terrible code for this module?"

Reality: The question assumes the code is terrible, putting the respondent
on the defensive regardless of actual code quality.
```

### সত্যিকারের স্কটসম্যান নেই
**এটি কী:** চ্যালেঞ্জ করা হলে একটি সর্বজনীন দাবির ব্যতিক্রম করা।
**খারাপ উদাহরণ:**```markdown
Person A: "No professional developer writes code without tests."
Person B: "But John is a professional developer and doesn't write tests."
Person A: "Well, no TRUE professional developer writes code without tests."

Reality: This redefines the category to exclude counterexamples rather 
than revising the claim.
```

### জেনেটিক ফ্যালাসি
**এটি কী:** বর্তমান যোগ্যতার পরিবর্তে তার উত্সের ভিত্তিতে কিছু বিচার করা।
**খারাপ উদাহরণ:**```markdown
"That library came from a small startup, so it can't be enterprise-grade."

Reality: The origin doesn't determine current quality. Evaluate based on
actual characteristics, not source.
```

### মিডল গ্রাউন্ড ফ্যালাসি
**এটি কী:** সত্যকে ধরে নেওয়া সর্বদা দুটি চরমের মাঝখানে থাকে।
**খারাপ উদাহরণ:**```markdown
Developer A: "We should add comprehensive error handling."
Developer B: "Error handling isn't important, skip it."
Compromise: "Let's add some error handling, but not too much."

Reality: One position might be clearly correct. Compromise isn't always wise.
```

---

## এআই সিস্টেমে জ্ঞানীয় পক্ষপাত
### প্রশিক্ষণ ডেটা বায়াস
এআই মডেলগুলি তাদের প্রশিক্ষণের ডেটাতে উপস্থিত পক্ষপাতের উত্তরাধিকারী হয়।
**উদাহরণ:**```markdown
Training data contains: "The doctor said..." (mostly male pronouns)
                       "The nurse said..." (mostly female pronouns)

Model learns: Doctors are typically male, nurses are typically female.

Result: Model exhibits gender bias in profession associations.
```

**প্রশমন:**
- পক্ষপাতের জন্য অডিট প্রশিক্ষণ ডেটা
- debiasing কৌশল ব্যবহার করুন
- পক্ষপাতদুষ্ট আউটপুট জন্য পরীক্ষা
- বিভিন্ন তথ্য সংগ্রহ
### অটোমেশন বায়াস
**এটি কী:** স্বয়ংক্রিয় সিস্টেমের উপর অতিরিক্ত নির্ভর করা, এমনকি তারা ভুল হলেও।
**উদাহরণ:**```markdown
AI suggests code with a subtle bug.
Developer accepts it without review because "the AI is usually right."

Result: Bug makes it to production.
```

**প্রশমন:**
- মানুষের তদারকি বজায় রাখুন
- এআই আউটপুটগুলির সমালোচনামূলক মূল্যায়নকে উত্সাহিত করুন
- এআইকে ভুল বলে মনে করবেন না
- পর্যালোচনা প্রক্রিয়া বাস্তবায়ন
### বোঝার মায়া
**এটা কি:** বিশ্বাস করলে আপনি বুঝতে পারবেন কিভাবে একটি AI কাজ করে যখন আপনি না করেন।
**উদাহরণ:**```markdown
User: "The AI understands what I mean, it's like talking to a person."

Reality: LLMs predict tokens based on patterns, they don't truly 
"understand" in the human sense. This illusion leads to over-trust.
```

**প্রশমন:**
- এআই সীমাবদ্ধতা সম্পর্কে ব্যবহারকারীদের শিক্ষিত করুন
- সিস্টেমগুলি কীভাবে কাজ করে সে সম্পর্কে স্বচ্ছ হন৷
- নৃতাত্ত্বিক এআই এড়িয়ে চলুন
- উপযুক্ত প্রত্যাশা সেট করুন
---

## কেস স্টাডিজ
### কেস স্টাডি 1: আর্কিটেকচার নির্বাচনে নিশ্চিতকরণ পক্ষপাত
**ঘটনা:** একটি দল একটি ছোট অ্যাপ্লিকেশনের জন্য একটি মাইক্রোসার্ভিসেস আর্কিটেকচার বেছে নিয়েছে৷
**মূল কারণ:** টিম লিড মাইক্রোসার্ভিসের প্রশংসা করে বেশ কয়েকটি নিবন্ধ পড়েছিল এবং 
জটিলতা সম্পর্কে সতর্কতা উপেক্ষা করে শুধুমাত্র এই পছন্দ নিশ্চিত করার তথ্য চেয়েছে।
**প্রভাব:**
- 3 ডেভেলপারদের একটি দলের জন্য বিশাল ওভারহেড
- স্থাপনার জটিলতা 10x বৃদ্ধি পেয়েছে
- নেটওয়ার্ক কলের কারণে কর্মক্ষমতা হ্রাস পেয়েছে
- প্রকল্প 6 মাস বিলম্বিত
**পাঠ:** আপনার নির্দিষ্ট প্রসঙ্গের উপর ভিত্তি করে আর্কিটেকচারের মূল্যায়ন করুন, শুধু নয় 
ইতিবাচক প্রশংসাপত্র। সুস্পষ্টভাবে ট্রেড-অফ বিবেচনা করুন.
### কেস স্টাডি 2: লিগ্যাসি সিস্টেমে খরচ কমে গেছে
**ঘটনা:** কোম্পানি 5 বছর ধরে একটি কাস্টম-নির্মিত CRM বজায় রেখেছে 
ভাল বিকল্প সত্ত্বেও।
**মূল কারণ:** "আমরা ইতিমধ্যেই $2M বিনিয়োগ করেছি, আমরা এখন এটি ত্যাগ করতে পারি না।"
**প্রভাব:**
- বার্ষিক রক্ষণাবেক্ষণ খরচ: $500K
- সুযোগ খরচ: আধুনিক বৈশিষ্ট্য ব্যবহার করা যায়নি
- প্রতিভা ধরে রাখার সমস্যা (বিকাশকারীরা আধুনিক প্রযুক্তির সাথে কাজ করতে চেয়েছিলেন)
- মোট 5 বছরের খরচ: SaaS বিকল্পের জন্য $4.5M বনাম $1.5M
**পাঠ:** অতীত বিনিয়োগ ডুবে গেছে। ভবিষ্যতের মূল্যের উপর ভিত্তি করে সিদ্ধান্ত নিন।
### কেস স্টাডি 3: নিরাপত্তায় উপলব্ধতা হিউরিস্টিক
**ঘটনা:** টিম সম্প্রতি প্রচারিত আক্রমণের বিরুদ্ধে রক্ষা করাকে অগ্রাধিকার দিয়েছে 
আরও সম্ভাব্য হুমকি উপেক্ষা করার সময় ভেক্টর।
**মূল কারণ:** সাম্প্রতিক সংবাদ কভারেজ একটি হুমকি টাইপ অত্যন্ত উপলব্ধ করা হয়েছে 
মেমরি, ঝুঁকি মূল্যায়ন skewing.
**প্রভাব:**
- কম-সম্ভাব্যতার হুমকি প্রশমিত করতে $100K খরচ করেছে
- অবহেলিত ভেক্টরের মাধ্যমে প্রকৃত লঙ্ঘন ঘটেছে
- পুনরুদ্ধারের খরচ: $500K+
**পাঠ:** ডেটা-চালিত হুমকি মডেলিং ব্যবহার করুন, নতুনত্ব-ভিত্তিক অগ্রাধিকার নয়।
---

## ব্যবহারিক ব্যায়াম
### পক্ষপাত সনাক্তকরণ অনুশীলন
সাম্প্রতিক সিদ্ধান্তগুলি পর্যালোচনা করুন এবং জিজ্ঞাসা করুন:
1. আমরা কি অনুমান করেছি?
2. কোন প্রমাণ আমাদের উপসংহারের বিরোধিতা করবে?
3. আমরা কি একাধিক বিকল্প বিবেচনা করেছি বা প্রথম ধারণাটিতে অ্যাঙ্কর করেছি?
4. আমরা কি ভবিষ্যতের মূল্য বা অতীত বিনিয়োগের কারণে চালিয়ে যাচ্ছি?
5. অন্য কেউ আমাদের জিজ্ঞাসা করলে আমরা কী সুপারিশ করব?
### লজিক্যাল ফ্যালাসি স্পটিং
দৈনন্দিন আলোচনায় ভুলত্রুটি চিহ্নিত করার অভ্যাস করুন:
```markdown
Statement: "If we don't adopt AI now, we'll be left behind forever."

Analysis: This is a slippery slope fallacy. It assumes inevitable 
progression to being "left behind" without evidence. Also presents 
a false dichotomy (adopt AI or be left behind).
```

### প্রি-মর্টেম টেকনিক
একটি প্রকল্প শুরু করার আগে:
1. কল্পনা করুন এটি ভবিষ্যতে 6 মাস
2. প্রকল্পটি দর্শনীয়ভাবে ব্যর্থ হয়েছে
3. কেন ব্যর্থ হয়েছে তার গল্প লিখুন
4. সেই ব্যর্থতা মোড প্রতিরোধ করতে পিছনে কাজ করুন
এটি আশাবাদের পক্ষপাতিত্ব এবং প্রাপ্যতা হিউরিস্টিককে কাউন্টার করে।
---

## টুলস এবং ফ্রেমওয়ার্ক
### সিদ্ধান্ত জার্নাল টেমপ্লেট
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

### বায়াস চেকলিস্ট
গুরুত্বপূর্ণ সিদ্ধান্ত নেওয়ার আগে:
- [ ] আমরা কি অপ্রমাণিত প্রমাণ চেয়েছি?
- [ ] আমরা কি প্রাথমিক তথ্যে নোঙর করেছি?
- [ ] ডুবে যাওয়া খরচ কি আমাদের প্রভাবিত করছে?
- [ ] আমরা কি আমাদের অনুমানে অতিরিক্ত আত্মবিশ্বাসী?
- [ ] আমরা কি বেস রেট বিবেচনা করেছি?
- [ ] আমরা কি প্রাপ্যতা/সম্পর্কিত পক্ষপাতের জন্য পড়ে যাচ্ছি?
- [ ] নতুন করে শুরু করলে আমরা কি একই পছন্দ করব?
### লাল দলের ব্যায়াম
প্রস্তাবিত সিদ্ধান্তের বিরুদ্ধে তর্ক করার জন্য কাউকে বরাদ্দ করুন:
- তাদের ভূমিকা ত্রুটি খুঁজে বের করা হয়
- তাদের অবশ্যই বিকল্প দৃষ্টিভঙ্গি উপস্থাপন করতে হবে
- সমালোচনাকে গঠনমূলকভাবে সাড়া দিয়ে দলের অনুশীলন
- নথি উদ্বেগ উত্থাপিত এবং সুরাহা
এটি নিশ্চিতকরণ পক্ষপাতিত্ব এবং গ্রুপথিঙ্ককে কাউন্টার করে।