<!--
---
# Metadata
title: "COBOL — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the COBOL ecosystem including compilers, tools, and modernization."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# COBOL - คู่มือระบบนิเวศและเครื่องมือ
คู่มือนี้ครอบคลุมถึงเครื่องมือสำคัญ คอมไพเลอร์ และโครงสร้างพื้นฐานในระบบนิเวศ COBOL
---

## คอมไพเลอร์และการนำไปใช้งาน
| คอมไพเลอร์ | พิมพ์ | หมายเหตุ |
|----------|-|-------|
| **GnuCOBOL (OpenCOBOL)** | โอเพ่นซอร์ส | คอมไพเลอร์ฟรีที่ใช้กันอย่างแพร่หลายที่สุด |
| **IBM Enterprise ภาษาโคบอล** | เชิงพาณิชย์ | มาตรฐานเมนเฟรม z/OS |
| **ไมโครโฟกัสโคบอล** | เชิงพาณิชย์ | ภาษาโคบอลระดับองค์กร |
| **ฟูจิตสึโคบอล** | เชิงพาณิชย์ | ยูนิกซ์โคบอล |
| **เอคูโคโบล-GT** | เชิงพาณิชย์ | ตอนนี้ไมโครโฟกัส |
| **โคบอล-ไอที** | เชิงพาณิชย์ | ที่ใช้ GnuCOBOL |
```bash
cobc --version              # GnuCOBOL version
cobc -x -o app program.cob  # compile to executable
cobc -m -o lib.so module.cob  # compile to shared library
cobc -free program.cob      # free-format source
```

---

## สร้างระบบ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **ทำ** | งานสร้างคลาสสิก |
| **คอมไพเลอร์ GnuCOBOL** | การรวบรวมโดยตรง |
| **Maven (ปลั๊กอินโคบอล)** | องค์กรสร้าง |
| **เจซีแอล** | การควบคุมงานเมนเฟรม |
| **ซีเมค** | ข้ามแพลตฟอร์ม (พร้อมรองรับ COBOL) |
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

## ฐานข้อมูลและระบบธุรกรรม
| เทคโนโลยี | วัตถุประสงค์ |
|------------|---------|
| **DB2** | ฐานข้อมูลเมนเฟรมของ IBM |
| **VSAM** | วิธีการเข้าถึงที่เก็บข้อมูลเสมือน |
| **ซีไอซีส** | การประมวลผลธุรกรรม |
| **IMS** | ระบบการจัดการข้อมูล |
| **SQL** | การเข้าถึงฐานข้อมูลมาตรฐาน |
| **GnuCOBOL + SQLite** | ฐานข้อมูลแบบฝัง |
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

## การทดสอบ
| กรอบ | วัตถุประสงค์ |
|----------|---------|
| **โคโบลยูนิต** | การทดสอบหน่วย (ไมโครโฟกัส) |
| **การทดสอบกนูโคบอล** | การทดสอบขั้นพื้นฐาน |
| **เครื่องมือทดสอบ z/OS** | การทดสอบไอบีเอ็ม |
| **สคริปต์ที่กำหนดเอง** | การทดสอบแบบเชลล์ |
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

## คุณภาพรหัส
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **OpenCobolCE** | การวิเคราะห์โค้ด |
| **การวิเคราะห์โค้ด IBM** | การวิเคราะห์ z/OS |
| **โซนาร์โคบอล** | ปลั๊กอิน SonarQube |
| **ลินเตอร์แบบกำหนดเอง** | การตรวจสอบตาม Regex |
---

## เครื่องมือปรับปรุงใหม่
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **ภาษาโคบอลภาพไมโครโฟกัส** | IDE สมัยใหม่ |
| **กนูโคบอล** | ความทันสมัยของโอเพ่นซอร์ส |
| **อายุ AWS Blu** | การรีแฟคเตอร์อัตโนมัติ |
| **การปรับแอปพลิเคชัน IBM z/OS ให้ทันสมัย** | การปรับปรุงเมนเฟรมให้ทันสมัย ​​|
| **ภาษาโคบอลตะวันออก** | การวิเคราะห์โค้ด |
| **OpenLegacy** | การเปิดใช้งาน API |
---

## ไลบรารีและรูปแบบที่สำคัญ
| รูปแบบ | วัตถุประสงค์ |
|---------|---------|
| **คัดลอกหนังสือ** | ข้อมูลโค้ดที่ใช้ซ้ำได้ |
| **โทร** | การเรียกโปรแกรมต่อโปรแกรม |
| **สำเนา** | รวมรหัสภายนอก |
| **EXEC SQL** | SQL แบบฝัง |
| **EXEC CICS** | คำสั่งธุรกรรม CICS |
| **เรียงลำดับ** | การเรียงลำดับไฟล์ |
| **STRING/ปลดสตริง** | การจัดการสตริง |
| **ตรวจสอบ** | การตรวจสอบสตริง |
| **ดำเนินการ** | การดำเนินการวนซ้ำ/ย่อหน้า |
---

## IDE และบรรณาธิการ
| ไอดี | จุดแข็ง |
|-----|-----------|
| **ภาษาโคบอลภาพไมโครโฟกัส** | IDE องค์กร |
| **รหัส VS + ภาษาโคบอล** | การแก้ไขที่ทันสมัย ​​|
| **IBM Z Open Editor** | การพัฒนา z/OS |
| **SPF/ISPF** | โปรแกรมแก้ไขเมนเฟรม |
| **GnuCOBOL + โปรแกรมแก้ไขใดๆ** | โอเพ่นซอร์ส |
---

## การปรับใช้
| วิธีการ | หมายเหตุ |
|--------|--------|
| **z/OS** | ไอบีเอ็มเมนเฟรม |
| **เซิร์ฟเวอร์ไมโครโฟกัส** | ภาษาโคบอลแบบกระจาย |
| **กนูโคบอล** | Linux/Unix/Windows |
| **นักเทียบท่า** | แบบบรรจุกล่อง (GnuCOBOL) |
| **ซีไอซีส** | การประมวลผลธุรกรรม |
| **ชุด** | การประมวลผลเป็นชุด |
---

## สรุป
ระบบนิเวศของ COBOL ถูกครอบงำโดยเมนเฟรมและการประมวลผลระดับองค์กร ห่วงโซ่เครื่องมือมาตรฐานคือ: **IBM Enterprise COBOL** บน z/OS (เมนเฟรม) หรือ **GnuCOBOL** (โอเพ่นซอร์ส ข้ามแพลตฟอร์ม), **Db2** และ **VSAM** สำหรับข้อมูล **CICS** สำหรับธุรกรรม และเครื่องมือ **Micro Focus** สำหรับการปรับปรุงให้ทันสมัย COBOL ประมวลผลธุรกรรมทางธุรกิจทั่วโลกประมาณ 70% — การธนาคาร การประกันภัย รัฐบาล และการดูแลสุขภาพ ยังคงพึ่งพา COBOL อย่างมาก ระบบนิเวศเป็นสิ่งจำเป็นสำหรับการรักษาระบบเดิมและปรับปรุงแอปพลิเคชันเมนเฟรมให้ทันสมัย GnuCOBOL มอบเส้นทางโอเพ่นซอร์สฟรีสำหรับการพัฒนาและการโยกย้ายภาษาโคบอล