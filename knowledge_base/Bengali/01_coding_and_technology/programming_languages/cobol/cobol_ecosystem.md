---
# Metadata
title: "COBOL — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the COBOL ecosystem including compilers, tools, and modernization."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [cobol, ecosystem, tooling, compilers, mainframe, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "11 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# COBOL — ইকোসিস্টেম এবং টুলিং গাইড
এই নির্দেশিকাটি COBOL ইকোসিস্টেমের প্রয়োজনীয় সরঞ্জাম, কম্পাইলার এবং অবকাঠামো কভার করে।
---

## কম্পাইলার এবং বাস্তবায়ন
| কম্পাইলার | প্রকার | নোট |
|----------|------|-------|
| **GnuCOBOL (OpenCOBOL)** | ওপেন সোর্স | সর্বাধিক ব্যবহৃত ফ্রি কম্পাইলার |
| **আইবিএম এন্টারপ্রাইজ কোবল** | বাণিজ্যিক | z/OS মেইনফ্রেম স্ট্যান্ডার্ড |
| **মাইক্রো ফোকাস COBOL** | বাণিজ্যিক | এন্টারপ্রাইজ COBOL |
| **ফুজিৎসু কোবল** | বাণিজ্যিক | ইউনিক্স COBOL |
| **ACUCOBOL-GT** | বাণিজ্যিক | এখন মাইক্রো ফোকাস |
| **COBOL-IT** | বাণিজ্যিক | GnuCOBOL-ভিত্তিক |
```bash
cobc --version              # GnuCOBOL version
cobc -x -o app program.cob  # compile to executable
cobc -m -o lib.so module.cob  # compile to shared library
cobc -free program.cob      # free-format source
```

---

## সিস্টেম তৈরি করুন
| টুল | উদ্দেশ্য |
|------|---------|
| **বানান** | ক্লাসিক নির্মাণ |
| **GnuCOBOL কম্পাইলার** | সরাসরি সংকলন |
| **মাভেন (কোবোল প্লাগইন)** | এন্টারপ্রাইজ তৈরি করে |
| **JCL** | মেইনফ্রেম কাজ নিয়ন্ত্রণ |
| **সিমেক** | ক্রস-প্ল্যাটফর্ম (COBOL সমর্থন সহ) |
```makefile
# Makefile for COBOL project
COBOL = cobc
FLAGS = -free -O2 -Wall

SRCS = $(wildcard src/*.cob)
OBJS = $(SRCS:.cob=.o)

all: myapp

myapp: $(OBJS)
	$(COBOL) -x -o $@ $^

%.o: %.cob
	$(COBOL) $(FLAGS) -c $<

clean:
	rm -f $(OBJS) myapp
```

---

## ডাটাবেস এবং লেনদেন সিস্টেম
| প্রযুক্তি | উদ্দেশ্য |
|------------|---------|
| **Db2** | আইবিএম মেইনফ্রেম ডাটাবেস |
| **ভিএসএএম** | ভার্চুয়াল স্টোরেজ অ্যাক্সেস পদ্ধতি |
| **CICS** | লেনদেন প্রক্রিয়াকরণ |
| **আইএমএস** | তথ্য ব্যবস্থাপনা সিস্টেম |
| **SQL** | স্ট্যান্ডার্ড ডাটাবেস অ্যাক্সেস |
| **GnuCOBOL + SQLite** | এমবেডেড ডাটাবেস |
```cobol
       *> SQL example in COBOL
       EXEC SQL
           SELECT NAME, SALARY
           INTO :WS-NAME, :WS-SALARY
           FROM EMPLOYEES
           WHERE EMP_ID = :WS-EMP-ID
       END-EXEC.
       
       IF SQLCODE = 0
           DISPLAY "Name: " WS-NAME
           DISPLAY "Salary: " WS-SALARY
       ELSE
           DISPLAY "Error: " SQLCODE
       END-IF.
```

---

## পরীক্ষা
| ফ্রেমওয়ার্ক | উদ্দেশ্য |
|------------|---------|
| **কোবল ইউনিট** | ইউনিট পরীক্ষা (মাইক্রো ফোকাস) |
| **GnuCOBOL পরীক্ষা** | মৌলিক পরীক্ষা |
| **z/OS পরীক্ষার সরঞ্জাম** | IBM টেস্টিং |
| **কাস্টম স্ক্রিপ্ট** | শেল ভিত্তিক পরীক্ষা |
```cobol
       *> Simple test in COBOL
       IDENTIFICATION DIVISION.
       PROGRAM-ID. TEST-ADD.
       
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-A    PIC 9(3) VALUE 5.
       01 WS-B    PIC 9(3) VALUE 3.
       01 WS-RESULT PIC 9(3).
       
       PROCEDURE DIVISION.
           COMPUTE WS-RESULT = WS-A + WS-B
           
           IF WS-RESULT = 8
               DISPLAY "PASS: 5 + 3 = 8"
           ELSE
               DISPLAY "FAIL: Expected 8, got " WS-RESULT
           END-IF
           
           STOP RUN.
```

---

## কোড কোয়ালিটি
| টুল | উদ্দেশ্য |
|------|---------|
| **OpenCobolCE** | কোড বিশ্লেষণ |
| **আইবিএম কোড বিশ্লেষণ** | z/OS বিশ্লেষণ |
| **সোনারকোবল** | সোনারকিউব প্লাগইন |
| **কাস্টম লিন্টার** | Regex-ভিত্তিক চেক |
---

## আধুনিকীকরণের সরঞ্জাম
| টুল | উদ্দেশ্য |
|------|---------|
| **মাইক্রো ফোকাস ভিজ্যুয়াল COBOL** | আধুনিক IDE |
| **গ্নুকোবোল** | ওপেন সোর্স আধুনিকীকরণ |
| **AWS ব্লু এজ** | স্বয়ংক্রিয় রিফ্যাক্টরিং |
| **IBM z/OS অ্যাপ্লিকেশন আধুনিকীকরণ** | মেইনফ্রেম আধুনিকীকরণ |
| **AST COBOL** | কোড বিশ্লেষণ |
| **ওপেন লিগ্যাসি** | API সক্ষমতা |
---

## মূল লাইব্রেরি এবং প্যাটার্ন
| প্যাটার্ন | উদ্দেশ্য |
|---------|---------|
| **কপি বই** | পুনঃব্যবহারযোগ্য কোড স্নিপেট |
| **কল** | প্রোগ্রাম থেকে প্রোগ্রাম কল |
| **কপি** | বাহ্যিক কোড অন্তর্ভুক্ত করুন |
| **EXEC SQL** | এমবেডেড এসকিউএল |
| **EXEC CICS** | CICS লেনদেন আদেশ |
| **বাছাই** | ফাইল বাছাই |
| **STRING/UNSTRING** | স্ট্রিং ম্যানিপুলেশন |
| **পরিদর্শন** | স্ট্রিং পরীক্ষা |
| **পারফর্ম** | লুপ/অনুচ্ছেদ নির্বাহ |
---

## আইডিই এবং সম্পাদক
| IDE | শক্তি |
|------|------------|
| **মাইক্রো ফোকাস ভিজ্যুয়াল COBOL** | এন্টারপ্রাইজ আইডিই |
| **VS কোড + COBOL** | আধুনিক সম্পাদনা |
| **আইবিএম জেড ওপেন এডিটর** | z/OS বিকাশ |
| **SPF/ISPF** | মেইনফ্রেম সম্পাদক |
| **GnuCOBOL + যেকোনো সম্পাদক** | ওপেন সোর্স |
---

## স্থাপনা
| পদ্ধতি | নোট |
|---------|-------|
| **z/OS** | IBM মেইনফ্রেম |
| **মাইক্রো ফোকাস সার্ভার** | বিতরণ করা COBOL |
| **গ্নুকোবোল** | লিনাক্স/ইউনিক্স/উইন্ডোজ |
| **ডকার** | কন্টেইনারাইজড (GnuCOBOL) |
| **CICS** | লেনদেন প্রক্রিয়াকরণ |
| **ব্যাচ** | ব্যাচ প্রক্রিয়াকরণ |
---

## সারাংশ
COBOL এর ইকোসিস্টেম মেইনফ্রেম এবং এন্টারপ্রাইজ কম্পিউটিং দ্বারা প্রভাবিত। স্ট্যান্ডার্ড টুলচেন হল: **IBM Enterprise COBOL** z/OS (মেনফ্রেম) বা **GnuCOBOL** (ওপেন-সোর্স, ক্রস-প্ল্যাটফর্ম), **Db2** এবং **VSAM** ডেটার জন্য, লেনদেনের জন্য **CICS** এবং আধুনিকীকরণের জন্য **মাইক্রো ফোকাস** টুল। COBOL বিশ্বের ব্যবসায়িক লেনদেনের আনুমানিক 70% প্রক্রিয়া করে — ব্যাঙ্কিং, বীমা, সরকার, এবং স্বাস্থ্যসেবা এখনও COBOL-এর উপর অনেক বেশি নির্ভর করে৷ লিগ্যাসি সিস্টেম রক্ষণাবেক্ষণ এবং মেইনফ্রেম অ্যাপ্লিকেশন আধুনিকীকরণের জন্য ইকোসিস্টেম অপরিহার্য। GnuCOBOL COBOL ডেভেলপমেন্ট এবং মাইগ্রেশনের জন্য একটি বিনামূল্যে, ওপেন সোর্স পাথ প্রদান করে।