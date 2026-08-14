<!--
---
# Metadata
title: "COBOL"
description: "Comprehensive reference for the COBOL programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cobol, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "34 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# ภาษาโคบอล
COBOL (Common Business-Oriented Language) เป็นหนึ่งในภาษาการเขียนโปรแกรมที่เก่าแก่ที่สุดที่ยังคงใช้อยู่ พัฒนาขึ้นครั้งแรกในปี 1959 มันถูกออกแบบมาสำหรับการประมวลผลข้อมูลทางธุรกิจ เช่น ระบบการเงิน บัญชีเงินเดือน การธนาคาร การประกันภัย และแอปพลิเคชันของรัฐบาล ไวยากรณ์ที่คล้ายกับภาษาอังกฤษของ COBOL ตั้งใจให้ผู้จัดการธุรกิจสามารถอ่านได้ ไม่ใช่แค่โปรแกรมเมอร์เท่านั้น
แม้จะมีอายุมาก แต่ COBOL ก็ประมวลผลประมาณ 30% ของธุรกรรมทางธุรกิจทั้งหมดทั่วโลก ธนาคารรายใหญ่ หน่วยงานรัฐบาล (รวมถึงสำนักงานประกันสังคมของสหรัฐอเมริกา) และบริษัทประกันภัยยังคงใช้ระบบเมนเฟรมของ COBOL ความหวาดกลัวข้อผิดพลาดของ Y2K ในปี 1999 ทำให้ภาษาโคบอลกลับมาเป็นที่รู้จักของสาธารณชนอีกครั้ง และภาษานี้ยังคงใช้งานโครงสร้างพื้นฐานที่สำคัญทั่วโลก
---

## ทำไมภาษาโคบอลถึงมีความสำคัญ
- **โครงสร้างพื้นฐานที่สำคัญต่อธุรกิจ**: ประมวลผลธุรกรรมมูลค่าหลายล้านล้านดอลลาร์ต่อวันทั่วทั้งธนาคารและรัฐบาล
- **ความเสถียร**: โปรแกรม COBOL ที่เขียนขึ้นในปี 1970 ยังคงทำงานได้อย่างน่าเชื่อถือในปัจจุบัน โดยจำเป็นต้องมีการเปลี่ยนแปลงเพียงเล็กน้อย
- **ความสามารถในการอ่าน**: ไวยากรณ์คล้ายภาษาอังกฤษทำให้ตรรกะทางธุรกิจสามารถเข้าใจได้สำหรับผู้ที่ไม่ใช่โปรแกรมเมอร์
- **เลขคณิตทศนิยม**: รองรับการคำนวณทางการเงินที่แม่นยำ (ไม่มีข้อผิดพลาดในการปัดเศษทศนิยม)
- **การประมวลผลเป็นชุด**: ออกแบบมาเพื่อการประมวลผลบันทึกจำนวนมากอย่างมีประสิทธิภาพ
- **ตลาดงาน**: การขาดแคลนนักพัฒนาภาษาโคบอลอย่างรุนแรงทำให้เกิดความต้องการสูง (และเงินเดือนสูง) สำหรับบทบาทการบำรุงรักษา
## การแลกเปลี่ยน
| ข้อจำกัด | รายละเอียด | วิธีแก้ปัญหาทั่วไป |
|----------|---------|-------------------|
| **ไวยากรณ์แบบละเอียด** | การดำเนินการอย่างง่ายต้องใช้หลายบรรทัด | ยอมรับเป็นส่วนหนึ่งของการออกแบบภาษา |
| **ไม่ทันสมัย** | ไม่มีคลาส, ไม่มีการเขียนโปรแกรมเชิงฟังก์ชัน, นามธรรมที่จำกัด | ใช้สำหรับการบำรุงรักษา สร้างระบบใหม่ในภาษาสมัยใหม่ |
| **การพึ่งพาเมนเฟรม** | โดยทั่วไปแล้วจะรันบนเมนเฟรมของ IBM (แพง) | ใช้คอมไพเลอร์ภาษาโคบอลบนระบบแบบกระจาย (GnuCOBOL) |
| **จำนวนพนักงานลดลง** | นักพัฒนาภาษา COBOL น้อยลงที่เข้าสู่สนาม | ความต้องการสูงสำหรับผู้ที่รู้ ช่องทางอาชีพที่ดี |
| **ไม่มีเว็บ/มือถือ** | ไม่สามารถสร้างแอปพลิเคชันสมัยใหม่ได้ | ใช้สำหรับการประมวลผลแบตช์แบ็กเอนด์ ส่วนหน้าที่ทันสมัย ​​|
---

## พื้นฐานไวยากรณ์
```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. HELLO-WORLD.
       
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-NAME        PIC A(20) VALUE 'Alice'.
       01 WS-AGE         PIC 99 VALUE 30.
       01 WS-SCORE       PIC 9V99 VALUE 9.50.
       01 WS-GREETING    PIC X(50).
       
       PROCEDURE DIVISION.
           STRING 'Hello, ' DELIMITED BY SIZE
                  WS-NAME DELIMITED BY SIZE
                  '!' DELIMITED BY SIZE
                  INTO WS-GREETING
           END-STRING
           
           DISPLAY WS-GREETING
           DISPLAY 'Age: ' WS-AGE
           DISPLAY 'Score: ' WS-SCORE
           
           STOP RUN.
```

### ตัวอย่างการประมวลผลไฟล์
```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROCESS-CUSTOMERS.
       
       DATA DIVISION.
       FILE SECTION.
       FD  CUSTOMER-FILE.
       01  CUSTOMER-RECORD.
           05 CUST-ID        PIC 9(6).
           05 CUST-NAME      PIC X(30).
           05 CUST-BALANCE   PIC 9(7)V99.
       
       WORKING-STORAGE SECTION.
       01  WS-EOF            PIC X VALUE 'N'.
       
       PROCEDURE DIVISION.
           OPEN INPUT CUSTOMER-FILE
           
           PERFORM UNTIL WS-EOF = 'Y'
               READ CUSTOMER-FILE
                   AT END MOVE 'Y' TO WS-EOF
                   NOT AT END
                       IF CUST-BALANCE > 1000.00
                           DISPLAY CUST-ID ' ' CUST-NAME 
                               ' Balance: ' CUST-BALANCE
                       END-IF
               END-READ
           END-PERFORM
           
           CLOSE CUSTOMER-FILE
           STOP RUN.
```

---

## ไวยากรณ์และรูปแบบขั้นสูง
### เจาะลึกแผนกข้อมูล
การแบ่งข้อมูลของ COBOL เป็นคุณลักษณะที่โดดเด่นที่สุดของภาษา ใช้ระบบลำดับชั้น (ระดับ 01–88) เพื่อกำหนดโครงสร้างข้อมูล
| ระดับ | วัตถุประสงค์ | ตัวอย่าง |
|-------|---------|---------|
| **01** | รายการระดับเรกคอร์ด (ตัวแปรระดับบนสุดหรือเรกคอร์ด) | `01 WS-EMPLOYEE.`|
| **02–49** | กลุ่มหรือรายการเบื้องต้น (ฟิลด์ย่อย) | `05 EMP-NAME PIC X(30).`|
| **66** | เปลี่ยนชื่อส่วนคำสั่ง (มุมมองข้อมูลทางเลือก) | `66 EMP-FULL-NAME RENAMES EMP-FIRST.`|
| **77** | รายการเบื้องต้นแบบสแตนด์อโลน (ไม่มีรายการย่อย) | `77 WS-COUNTER PIC 9(5).`|
| **88** | ชื่อเงื่อนไข (แฟล็กคล้ายบูลีน) | `88 WS-IS-SENIOR VALUE 'Y'.`|
```cobol
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       
       * Hierarchical data structure
       01  WS-EMPLOYEE.
           05  EMP-ID            PIC 9(6).
           05  EMP-NAME.
               10  EMP-FIRST     PIC X(15).
               10  EMP-LAST      PIC X(20).
           05  EMP-SALARY        PIC 9(7)V99.
           05  EMP-HIRE-DATE.
               10  EMP-YEAR      PIC 9(4).
               10  EMP-MONTH     PIC 9(2).
               10  EMP-DAY       PIC 9(2).
           05  EMP-STATUS        PIC X.
               88  EMP-ACTIVE    VALUE 'A'.
               88  EMP-INACTIVE  VALUE 'I'.
               88  EMP-ON-LEAVE  VALUE 'L'.
       
       * Packed decimal for precise financial calculations
       01  WS-TRANSACTION.
           05  TR-AMOUNT         PIC S9(9)V99 COMP-3.
           05  TR-TYPE           PIC XX.
               88  TR-DEBIT      VALUE 'DB'.
               88  TR-CREDIT     VALUE 'CR'.
       
       * Usage types
       01  WS-CALC-FIELD         COMP-2.      * Double precision float
       01  WS-BINARY-FIELD       COMP.         * Binary integer
       01  WS-INDEX-FIELD        POINTER.      * Memory address
```

### คำชี้แจง COPY (Copybooks)
Copybooks เป็นกลไกของ COBOL สำหรับการใช้โค้ดซ้ำ ซึ่งคล้ายกับ`#include`ในภาษา C ซึ่งจะถูกจัดเก็บเป็นสมาชิกแยกต่างหากและแทรกไว้ในเวลาคอมไพล์
```cobol
       * In the main program — copy in common data definitions
       IDENTIFICATION DIVISION.
       PROGRAM-ID. PAYROLL-MAIN.
       
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       
       * Copy in standard record layouts
       COPY EMPLOYEE-RECORD.
       COPY PAYROLL-CALC.
       COPY ERROR-HANDLER.
       
       PROCEDURE DIVISION.
           PERFORM 100-INITIALIZE
           PERFORM 200-PROCESS-EMPLOYEES
           PERFORM 900-CLEANUP
           STOP RUN.
```

```cobol
       * EMPLOYEE-RECORD copybook (stored as EMPLOYEE.cpy)
       01  WS-EMPLOYEE-RECORD.
           05  EMP-ID            PIC 9(6).
           05  EMP-NAME          PIC X(30).
           05  EMP-DEPT          PIC X(4).
           05  EMP-SALARY        PIC 9(7)V99.
           05  EMP-HOURS-WORKED  PIC 9(3).
```

### ดำเนินการรูปแบบต่างๆ
COBOL มีคำสั่ง PERFORM หลายรูปแบบสำหรับการเขียนโปรแกรมแบบมีโครงสร้าง
```cobol
       PROCEDURE DIVISION.
       
       * Simple paragraph call (like a function call)
           PERFORM 100-CALCULATE-TAX
       
       * PERFORM with inline code (like a block)
           PERFORM
               DISPLAY 'Processing...'
               ADD 1 TO WS-COUNTER
           END-PERFORM
       
       * PERFORM N TIMES (counted loop)
           PERFORM 200-PROCESS-RECORD 100 TIMES
       
       * PERFORM VARYING (for loop equivalent)
           PERFORM 300-PROCESS-EMPLOYEE
               VARYING WS-INDEX FROM 1 BY 1
               UNTIL WS-INDEX > WS-EMPLOYEE-COUNT
       
       * PERFORM UNTIL (while loop equivalent)
           PERFORM UNTIL WS-EOF = 'Y'
               READ INPUT-FILE
                   AT END MOVE 'Y' TO WS-EOF
                   NOT AT END PERFORM 400-HANDLE-RECORD
               END-READ
           END-PERFORM
       
       * PERFORM THRU (executes a range of paragraphs)
           PERFORM 100-START THRU 100-END
       
       100-CALCULATE-TAX.
           COMPUTE WS-TAX = WS-SALARY * 0.22
           .
       
       200-PROCESS-RECORD.
           DISPLAY 'Processing record' WS-COUNTER
           .
```

### การจัดการและตรวจสอบสตริง
```cobol
       WORKING-STORAGE SECTION.
       01  WS-SOURCE         PIC X(50) VALUE 'Hello World'.
       01  WS-TARGET         PIC X(50).
       01  WS-COUNT          PIC 9(3).
       
       PROCEDURE DIVISION.
       * INSPECT — count occurrences
           INSPECT WS-SOURCE TALLYING WS-COUNT
               FOR ALL 'o'
           DISPLAY 'Count of o: ' WS-COUNT
       
       * INSPECT — replace characters
           INSPECT WS-SOURCE REPLACING ALL 'o' BY '0'
           DISPLAY WS-SOURCE
       
       * STRING — concatenate
           STRING 'Mr. ' DELIMITED BY SIZE
                  WS-LAST-NAME DELIMITED BY SPACE
                  ', ' DELIMITED BY SIZE
                  WS-FIRST-NAME DELIMITED BY SPACE
                  INTO WS-FULL-NAME
           END-STRING
       
       * UNSTRING — split a string
           UNSTRING WS-FULL-NAME
               DELIMITED BY ',' OR SPACE
               INTO WS-PART1 WS-PART2 WS-PART3
           END-UNSTRING
       
       * REFERENCE MODIFICATION — substring
           MOVE WS-SOURCE(1:5) TO WS-TARGET
           DISPLAY WS-TARGET
```

---

## สถาปัตยกรรมและการออกแบบระบบ
### สี่ดิวิชั่น
โปรแกรม COBOL ทุกโปรแกรมมีโครงสร้างเป็นสี่แผนก แต่ละส่วนมีวัตถุประสงค์ที่แตกต่างกัน:
```
┌─────────────────────────────────────────────────┐
│ IDENTIFICATION DIVISION                          │
│   Program metadata (name, author, date, etc.)    │
├─────────────────────────────────────────────────┤
│ ENVIRONMENT DIVISION                             │
│   Hardware/software configuration                │
│   CONFIGURATION SECTION (computer, compiler)     │
│   INPUT-OUTPUT SECTION (file definitions)        │
├─────────────────────────────────────────────────┤
│ DATA DIVISION                                    │
│   FILE SECTION (file record layouts)             │
│   WORKING-STORAGE SECTION (variables)            │
│   LOCAL-STORAGE SECTION (procedure-local vars)   │
│   LINKAGE SECTION (parameters passed in)         │
├─────────────────────────────────────────────────┤
│ PROCEDURE DIVISION                               │
│   All business logic and control flow            │
│   Organized into paragraphs and sections         │
└─────────────────────────────────────────────────┘
```

### ลำดับชั้นของโปรแกรม
โดยทั่วไประบบ COBOL จะใช้ลำดับชั้นการเรียกกับโปรแกรมหลักที่เรียกโปรแกรมย่อย
```
MAINPGM (entry point)
├── INITPGM    (initialization, open files)
├── READPGM    (read input records)
├── CALCPGM    (business logic calculations)
├── WRITEPGM   (write output records)
└── CLEANPGM   (close files, cleanup)
```

```cobol
       * Main program calling subprograms
       IDENTIFICATION DIVISION.
       PROGRAM-ID. MAINPGM.
       
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT EMPLOYEE-FILE ASSIGN TO EMPLFILE
               FILE STATUS IS WS-FILE-STATUS.
       
       DATA DIVISION.
       FILE SECTION.
       FD  EMPLOYEE-FILE.
       01  EMP-RECORD          PIC X(200).
       
       WORKING-STORAGE SECTION.
       01  WS-FILE-STATUS      PIC XX.
       01  WS-EOF              PIC X VALUE 'N'.
       01  WS-RETURN-CODE      PIC 9(4).
       
       PROCEDURE DIVISION.
       000-MAIN.
           PERFORM 100-INITIALIZE
           PERFORM 200-PROCESS
               UNTIL WS-EOF = 'Y'
           PERFORM 900-CLEANUP
           GOBACK.
       
       100-INITIALIZE.
           OPEN INPUT EMPLOYEE-FILE
           IF WS-FILE-STATUS NOT = '00'
               DISPLAY 'ERROR OPENING FILE: ' WS-FILE-STATUS
               MOVE 'Y' TO WS-EOF
           END-IF.
       
       200-PROCESS.
           READ EMPLOYEE-FILE
               AT END MOVE 'Y' TO WS-EOF
               NOT AT END
                   CALL 'CALCPGM' USING EMP-RECORD
                       RETURNING WS-RETURN-CODE
                   IF WS-RETURN-CODE = 0
                       CALL 'WRITEPGM' USING EMP-RECORD
                   END-IF
           END-READ.
       
       900-CLEANUP.
           CLOSE EMPLOYEE-FILE.
```

### โครงสร้างไดเร็กทอรีโครงการทั่วไป
```
cobol-project/
├── src/
│   ├── mainpgm.cbl           * Main entry program
│   ├── calcpgm.cbl           * Calculation subprogram
│   ├── readpgm.cbl           * File reading subprogram
│   └── writepgm.cbl          * Output subprogram
├── copybooks/
│   ├── employee.cpy          * Employee record layout
│   ├── payroll-calc.cpy      * Payroll calculation copybook
│   └── error-handler.cpy     * Error handling copybook
├── jcl/
│   ├── compile.jcl           * Compilation JCL
│   └── run.jcl               * Execution JCL
├── data/
│   ├── input/                * Input data files
│   └── output/               * Output data files
├── Makefile                  * GnuCOBOL build (distributed)
└── README.md
```

---

## การกำหนดค่าโครงการ & ระบบการสร้าง
### GnuCOBOL (คอมไพเลอร์โคบอลโอเพ่นซอร์ส)
GnuCOBOL (เดิมเรียกว่า OpenCOBOL) คอมไพล์ COBOL เป็น C แล้วตามด้วยโค้ดเครื่องเนทีฟ ทำให้ COBOL สามารถทำงานบน Linux, Windows และ macOS
```makefile
# Makefile for GnuCOBOL project
COBC     = cobc
COBFLAGS = -free -O2 -std=cobol2014
LDFLAGS  = -L./lib

SRCDIR   = src
CPYDIR   = copybooks
OBJDIR   = obj

SRCS     = $(wildcard $(SRCDIR)/*.cbl)
OBJS     = $(SRCS:$(SRCDIR)/%.cbl=$(OBJDIR)/%.o)
TARGET   = payroll

all: $(TARGET)

$(OBJDIR)/%.o: $(SRCDIR)/%.cbl
	$(COBC) $(COBFLAGS) -I $(CPYDIR) -c $< -o $@

$(TARGET): $(OBJS)
	$(COBC) -x $(COBFLAGS) $(OBJS) $(LDFLAGS) -o $(TARGET)

clean:
	rm -f $(OBJDIR)/*.o $(OBJDIR)/*.c $(TARGET)

run: $(TARGET)
	./$(TARGET)

.PHONY: all clean run
```

### IBM Mainframe JCL (ภาษาควบคุมงาน)
บนเมนเฟรมของ IBM โปรแกรม COBOL จะถูกคอมไพล์และดำเนินการโดยใช้ JCL
```jcl
//COMPILE  JOB (ACCT),'COMPILE COBOL',
//             CLASS=A,MSGCLASS=X
//*
//COBOL    EXEC IGYWCG,
//             COBOL.SYSCBL='MYPROJ.SRC.COBOL(MAINPGM)',
//             COBOL.SYSCP='MYPROJ.SRC.CPY'
//*
//LINK     EXEC IGYWLK,
//             LKED.SYSLMOD='MYPROJ.LOAD(MAINPGM)'
//*
//RUN      EXEC PGM=MAINPGM
//STEPLIB  DD DSN=MYPROJ.LOAD,DISP=SHR
//EMPLFILE DD DSN=MYPROJ.DATA.EMPLOYEE,DISP=SHR
//OUTFILE  DD DSN=MYPROJ.DATA.OUTPUT,
//            DISP=(NEW,CATLG,DELETE),
//            SPACE=(CYL,(10,5))
//SYSOUT   DD SYSOUT=*
```

### การอ้างอิงตัวเลือกคอมไพเลอร์
| ตัวเลือก | คำอธิบาย | ตัวอย่าง |
|--------|-------------|---------|
| `-free`| แหล่งที่มารูปแบบอิสระ (ไม่มีข้อจำกัดคอลัมน์) | `cobc -free prog.cbl`|
| `-fixed`| รูปแบบคงที่ (คอลัมน์ดั้งเดิม 1-80) | `cobc -fixed prog.cbl`|
| `-O2`| การเพิ่มประสิทธิภาพระดับ 2 | `cobc -O2 prog.cbl`|
| `-g`| สร้างข้อมูลการดีบัก | `cobc -g prog.cbl`|
| `-std=cobol2014`| ใช้มาตรฐาน COBOL 2014 | `cobc -std=cobol2014 prog.cbl`|
| `-x`| สร้างปฏิบัติการได้ (ไม่ใช่แค่คอมไพล์) | `cobc -x prog.cbl`|
| `-I`| เส้นทางการค้นหาสมุดลอก | `cobc -I ./copybooks prog.cbl`|
| `-Wall`| เปิดใช้งานคำเตือนทั้งหมด | `cobc -Wall prog.cbl`|
---

## การทดสอบและการดีบัก
### เทคนิคดีบักเกอร์ภาษาโคบอล
```cobol
       * Debugging with DISPLAY statements
       PROCEDURE DIVISION.
       000-MAIN.
           DISPLAY '=== DEBUG: Program started ==='
           
           MOVE 1000 TO WS-SALARY
           DISPLAY 'DEBUG: Salary = ' WS-SALARY
           
           PERFORM 100-CALCULATE
           
           DISPLAY 'DEBUG: Tax = ' WS-TAX
           DISPLAY 'DEBUG: Net = ' WS-NET-PAY
           DISPLAY '=== DEBUG: Program complete ==='
           STOP RUN.
       
       * Using EVALUATE for conditional debugging
       100-CALCULATE.
           COMPUTE WS-TAX = WS-SALARY * 0.22
           COMPUTE WS-NET-PAY = WS-SALARY - WS-TAX
           
           * Conditional debug output
           IF WS-DEBUG-FLAG = 'Y'
               DISPLAY 'DEBUG: Tax rate applied: 22%'
               DISPLAY 'DEBUG: Gross=' WS-SALARY 
                       ' Tax=' WS-TAX ' Net=' WS-NET-PAY
           END-IF.
```

### GnuCOBOL การดีบักด้วย gdb
```bash
# Compile with debug symbols
cobc -free -g -o payroll src/mainpgm.cbl

# Debug with GDB
gdb ./payroll
```

```gdb
# GDB commands useful for COBOL debugging
(gdb) break MAINPGM             # Break at paragraph
(gdb) break calcpgm.cbl:42      # Break at source line
(gdb) print ws_salary           # Print COBOL variable
(gdb) display ws-employee-record # Auto-display on each step
(gdb) step                       # Step into CALL
(gdb) next                       # Step over
```

### รูปแบบการดีบักทั่วไป
| ปัญหา | อาการ | โซลูชั่น |
|---------|---------|----------|
| ข้อมูลที่ถูกตัดทอน | ฟิลด์ถูกตัดออก | ตรวจสอบขนาดคำสั่ง PIC ตรงกับเค้าโครงบันทึก |
| ตัวเลขล้น | การคำนวณผิด | ตรวจสอบว่า PIC 9(n) มีตัวเลขเพียงพอ |
| ข้อผิดพลาดสถานะไฟล์ | WS-FILE-STATUS ไม่ใช่ '00' | ตรวจสอบชื่อ DD ไฟล์ เส้นทาง และการอนุญาต |
| วนซ้ำไม่สิ้นสุด | ดำเนินการจนกว่าจะไม่สิ้นสุด | ตรวจสอบว่าตัวแปรลูปถูกแก้ไขภายในลูป |
| การโทรล้มเหลว | การส่งคืนที่ไม่ใช่ศูนย์ | ตรวจสอบ LINKAGE SECTION ตรงกับโปรแกรมการโทร |
---

## การทำงานร่วมกัน
### คำสั่ง CALL - การเรียกโปรแกรมย่อย
```cobol
       * Dynamic CALL — program resolved at runtime
       WORKING-STORAGE SECTION.
       01  WS-PROGRAM-NAME   PIC X(8) VALUE 'TAXCALC'.
       01  WS-SALARY         PIC 9(7)V99 VALUE 75000.00.
       01  WS-TAX            PIC 9(7)V99.
       01  WS-RETURN-CODE    PIC 9(4).
       
       PROCEDURE DIVISION.
           CALL WS-PROGRAM-NAME
               USING WS-SALARY
                     WS-TAX
               RETURNING WS-RETURN-CODE
           END-CALL
           
           IF WS-RETURN-CODE = 0
               DISPLAY 'Tax: ' WS-TAX
           ELSE
               DISPLAY 'Error: ' WS-RETURN-CODE
           END-IF
```

### การทำงานร่วมกันแบบ C (GnuCOBOL)
```cobol
       * Calling a C function from COBOL via GnuCOBOL
       IDENTIFICATION DIVISION.
       PROGRAM-ID. CALL-C-FUNC.
       
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-RESULT   PIC 9(9).
       
       PROCEDURE DIVISION.
           * Call C's strlen() function
           CALL "strlen" USING
               BY REFERENCE "Hello World"
               RETURNING WS-RESULT
           END-CALL
           DISPLAY "Length: " WS-RESULT
           STOP RUN.
```

### การเชื่อมต่อฐานข้อมูล (DB2/COBOL)
```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. DB2-QUERY.
       
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       
       EXEC SQL INCLUDE SQLCA END-EXEC.
       
       01  WS-EMPLOYEE.
           05  WS-EMP-ID     PIC 9(6).
           05  WS-EMP-NAME   PIC X(30).
           05  WS-EMP-SAL    PIC 9(7)V99.
       
       01  WS-SQL-STMT       PIC X(200).
       
       PROCEDURE DIVISION.
       * Embedded SQL — single row fetch
           EXEC SQL
               SELECT EMP_ID, EMP_NAME, EMP_SALARY
               INTO :WS-EMP-ID, :WS-EMP-NAME, :WS-EMP-SAL
               FROM EMPLOYEE
               WHERE EMP_ID = 1001
           END-EXEC
           
           IF SQLCODE = 0
               DISPLAY 'Found: ' WS-EMP-NAME ' Salary: ' WS-EMP-SAL
           ELSE
               DISPLAY 'SQL Error: ' SQLCODE
           END-IF
           
       * Embedded SQL — cursor for multiple rows
           EXEC SQL
               DECLARE EMP-CUR CURSOR FOR
               SELECT EMP_ID, EMP_NAME, EMP_SALARY
               FROM EMPLOYEE
               WHERE EMP_SALARY > 50000
               ORDER BY EMP_NAME
           END-EXEC
           
           EXEC SQL OPEN EMP-CUR END-EXEC
           
           PERFORM UNTIL SQLCODE NOT = 0
               EXEC SQL
                   FETCH EMP-CUR
                   INTO :WS-EMP-ID, :WS-EMP-NAME, :WS-EMP-SAL
               END-EXEC
               IF SQLCODE = 0
                   DISPLAY WS-EMP-ID ' ' WS-EMP-NAME
                       ' ' WS-EMP-SAL
               END-IF
           END-PERFORM
           
           EXEC SQL CLOSE EMP-CUR END-EXEC
           STOP RUN.
```

---

## รูปแบบการออกแบบ
### รูปแบบ 1: การประมวลผลเป็นชุดพร้อมตัวแบ่งการควบคุม
รูปแบบการแบ่งการควบคุมเป็นรูปแบบการออกแบบภาษาโคบอลขั้นพื้นฐานที่สุด — การประมวลผลบันทึกที่จัดกลุ่มตามฟิลด์หลักและสร้างผลรวมย่อย
```cobol
       PROCEDURE DIVISION.
       000-MAIN.
           OPEN INPUT ORDER-FILE
           PERFORM 100-READ-ORDER
           PERFORM 200-PROCESS-ORDERS
               UNTIL WS-EOF = 'Y'
           CLOSE ORDER-FILE
           STOP RUN.
       
       100-READ-ORDER.
           READ ORDER-FILE
               AT END MOVE 'Y' TO WS-EOF
           END-READ.
       
       200-PROCESS-ORDERS.
           MOVE DEPT-CODE TO WS-PREV-DEPT
           MOVE ZERO TO WS-DEPT-TOTAL
           
           PERFORM UNTIL WS-EOF = 'Y'
               OR DEPT-CODE NOT = WS-PREV-DEPT
               
               IF DEPT-CODE NOT = WS-PREV-DEPT
                   PERFORM 300-PRINT-DEPT-SUBTOTAL
                   MOVE ZERO TO WS-DEPT-TOTAL
                   MOVE DEPT-CODE TO WS-PREV-DEPT
               END-IF
               
               ADD ORDER-AMOUNT TO WS-DEPT-TOTAL
               PERFORM 400-PRINT-ORDER-LINE
               PERFORM 100-READ-ORDER
           END-PERFORM
           
           PERFORM 300-PRINT-DEPT-SUBTOTAL.
       
       300-PRINT-DEPT-SUBTOTAL.
           DISPLAY 'Department: ' WS-PREV-DEPT
                   ' Total: ' WS-DEPT-TOTAL.
       
       400-PRINT-ORDER-LINE.
           DISPLAY '  Order: ' ORDER-ID
                   ' Amount: ' ORDER-AMOUNT.
```

### รูปแบบ 2: แก้ไข/ตรวจสอบรูปแบบ
```cobol
       500-VALIDATE-RECORD.
           MOVE ZERO TO WS-ERROR-COUNT
           
           * Validate customer ID (must be 6 digits)
           IF CUST-ID IS NOT NUMERIC
               DISPLAY 'ERROR: Invalid Customer ID: ' CUST-ID
               ADD 1 TO WS-ERROR-COUNT
           END-IF
           
           * Validate amount (must be positive)
           IF ORDER-AMOUNT <= 0
               DISPLAY 'ERROR: Negative amount: ' ORDER-AMOUNT
               ADD 1 TO WS-ERROR-COUNT
           END-IF
           
           * Validate date fields
           IF ORDER-DATE NOT NUMERIC
               DISPLAY 'ERROR: Invalid date format'
               ADD 1 TO WS-ERROR-COUNT
           END-IF
           
           IF WS-ERROR-COUNT = 0
               MOVE 'Y' TO WS-RECORD-VALID
           ELSE
               MOVE 'N' TO WS-RECORD-VALID
           END-IF.
```

### รูปแบบ 3: การค้นหาตาราง (อาร์เรย์ในหน่วยความจำ)
```cobol
       WORKING-STORAGE SECTION.
       01  WS-TAX-TABLE.
           05  WS-TAX-RATE OCCURS 5 TIMES.
               10  TR-BRACKET    PIC 9(7).
               10  TR-RATE       PIC V999.
       
       01  WS-INDEX              PIC 9 VALUE 1.
       01  WS-TAX-AMOUNT         PIC 9(7)V99.
       
       PROCEDURE DIVISION.
       * Initialize tax brackets
           MOVE 10000 TO TR-BRACKET(1)
           MOVE 0.100 TO TR-RATE(1)
           MOVE 25000 TO TR-BRACKET(2)
           MOVE 0.150 TO TR-RATE(2)
           MOVE 50000 TO TR-BRACKET(3)
           MOVE 0.220 TO TR-RATE(3)
           MOVE 100000 TO TR-BRACKET(4)
           MOVE 0.240 TO TR-RATE(4)
           MOVE 9999999 TO TR-BRACKET(5)
           MOVE 0.320 TO TR-RATE(5)
       
       * Lookup tax rate
       600-CALCULATE-TAX.
           PERFORM VARYING WS-INDEX FROM 1 BY 1
               UNTIL WS-INDEX > 5
               OR WS-SALARY <= TR-BRACKET(WS-INDEX)
               CONTINUE
           END-PERFORM
           
           COMPUTE WS-TAX-AMOUNT =
               WS-SALARY * TR-RATE(WS-INDEX).
```

---

## ประสิทธิภาพและการเพิ่มประสิทธิภาพ
### การเพิ่มประสิทธิภาพไฟล์ I/O
```cobol
       * BAD: Reading one record at a time with no buffering
           PERFORM UNTIL WS-EOF = 'Y'
               READ CUSTOMER-FILE
                   AT END MOVE 'Y' TO WS-EOF
                   NOT AT END PERFORM PROCESS-RECORD
               END-READ
           END-PERFORM
       
       * GOOD: Using BLOCK CONTAINS for buffered I/O
       * In the DATA DIVISION:
       FD  CUSTOMER-FILE
           BLOCK CONTAINS 0 RECORDS
           RECORDING MODE IS F.
       01  CUSTOMER-RECORD PIC X(200).
       
       * GOOD: Using indexed files for random access
       FD  INDEXED-CUSTOMER.
       01  CUST-RECORD.
           05  CUST-KEY      PIC 9(6).
           05  CUST-DATA     PIC X(194).
       
       * In ENVIRONMENT DIVISION:
       SELECT INDEXED-CUSTOMER ASSIGN TO CUSTFILE
           ORGANIZATION IS INDEXED
           ACCESS MODE IS DYNAMIC
           RECORD KEY IS CUST-KEY
           FILE STATUS IS WS-FILE-STATUS.
       
       * Random access read
           MOVE 1234 TO CUST-KEY
           READ INDEXED-CUSTOMER
               INVALID KEY DISPLAY 'Not found'
           END-READ
```

### การเพิ่มประสิทธิภาพการประมวลผลแบบแบตช์
| เทคนิค | ผลกระทบ | คำอธิบาย |
|----------|--------|-------------|
| **บล็อก I/O** | สูง | ใช้ BLOCK CONTAINS เพื่อลดการดำเนินการ I/O ฟิสิคัล |
| **การเข้าถึงที่จัดทำดัชนี** | สูง | ใช้ INDEXED ORGANIZATION สำหรับการค้นหาการเข้าถึงแบบสุ่ม |
| **เรียงลำดับ/รวม** | ปานกลาง | ใช้กริยา SORT สำหรับการจัดลำดับชุดข้อมูลขนาดใหญ่ |
| **ย่อขนาดการแสดงผล** | ปานกลาง | จอแสดงผลช้าในชุด; เขียนลงไฟล์แทน |
| **คอมพ์/คอมพ์-3** | ปานกลาง | ฟิลด์ไบนารี/แพ็กจะเร็วกว่า DISPLAY ตัวเลข |
| **การปรับบัฟเฟอร์** | ปานกลาง | ปรับขนาดบัฟเฟอร์สำหรับการประมวลผลไฟล์ตามลำดับ |
---

## การปรับใช้และการใช้งานในโลกแห่งความเป็นจริง
### การปรับใช้เมนเฟรม (IBM z/OS)
โปรแกรม COBOL บนเมนเฟรมถูกปรับใช้เป็นโมดูลโหลดในชุดข้อมูลแบบแบ่งพาร์ติชัน (PDS) JCL ควบคุมการคอมไพล์ การเชื่อมโยง และการดำเนินการ
```
Deployment pipeline on z/OS:
  Source (PDS) → Compile (JCL) → Link Edit → Load Module (PDS) → Execute (JCL)
```

### การปรับใช้แบบกระจาย (GnuCOBOL)
```bash
# Build for Linux deployment
cobc -free -O2 -x src/payroll.cbl -o bin/payroll

# Deploy binary to target server
scp bin/payroll server:/opt/cobol/bin/

# Run as a cron job for batch processing
# 0 2 * * * /opt/cobol/bin/payroll --input /data/daily.dat
```

### อุตสาหกรรมในโลกแห่งความเป็นจริงโดยใช้ภาษาโคบอล
| อุตสาหกรรม | การใช้งาน | สเกล |
|----------|-------|-------|
| **การธนาคาร** | การประมวลผลธุรกรรม การจัดการบัญชี | ประมวลผล ~85% ของธุรกรรม ATM |
| **ประกันภัย** | การบริหารนโยบาย การประมวลผลการเรียกร้อง | บริษัทประกันรายใหญ่ใช้แบ็กเอนด์ภาษาโคบอล |
| **รัฐบาล** | ประกันสังคม, ดำเนินการภาษี, สวัสดิการ | US SSA ประมวลผลบันทึกนับพันล้านรายการ |
| **การดูแลสุขภาพ** | บันทึกคนไข้ ระบบวางบิล | ระบบข้อมูลโรงพยาบาลรุ่นเก่า |
| **ขายปลีก** | การจัดการสินค้าคงคลัง, แบ็กเอนด์ ณ จุดขาย | ผู้ค้าปลีกรายใหญ่ที่มีระบบเดิม |
| **โทรคมนาคม** | ระบบการเรียกเก็บเงิน, การประมวลผลบันทึกการโทร | การประมวลผลบันทึกรายละเอียดการโทร |
---

## เมื่อใดจึงควรใช้ภาษาโคบอล
| สถานการณ์ | ทำไมต้องภาษาโคบอล | ทางเลือกที่ดีกว่า |
|----------|----------|-------------------|
| การบำรุงรักษาเมนเฟรม | รหัสฐานที่มีอยู่ | — |
| การประมวลผลทางการเงินเป็นกลุ่ม | คณิตศาสตร์ทศนิยมที่ได้รับการพิสูจน์แล้ว เชื่อถือได้ และแม่นยำ | Java, Python สำหรับระบบใหม่ |
| ระบบมรดกของรัฐบาล | รหัสฐานที่มีอยู่ | — |
| การเรียนรู้ประวัติศาสตร์คอมพิวเตอร์ | ทำความเข้าใจกับวิวัฒนาการของการเขียนโปรแกรม | — |
| แอพพลิเคชั่นธุรกิจใหม่ | ไม่ใช่ทางเลือกที่ทันสมัย ​​| ชวา, C#, หลาม |
| การพัฒนาเว็บ/มือถือ | ไม่เหมาะ | JavaScript, Swift, Kotlin |
| วิทยาศาสตร์ข้อมูล / ML | ไม่เหมาะ | หลาม, อาร์ |
---

## คำถามและคำตอบสังเคราะห์
### คำถามที่ 1: เหตุใดภาษาโคบอลจึงยังคงใช้ในวงการธนาคารหลังจากผ่านไป 60 ปีขึ้นไป
**ตอบ:** COBOL ประมวลผลธุรกรรมธนาคารประมาณ 70-80% เหตุผล:
- ฐานรหัสขนาดใหญ่ (ล้านบรรทัด) ที่ทำงานได้อย่างถูกต้อง
- ความน่าเชื่อถือสูงสุด — ระบบเหล่านี้ได้รับการทดสอบในการผลิตมานานหลายทศวรรษ
- ต้นทุนและความเสี่ยงในการย้ายข้อมูลมีมากกว่าค่าบำรุงรักษา
- ไวยากรณ์ที่เหมือนภาษาอังกฤษของภาษาโคบอลนั้นมีการจัดทำเอกสารด้วยตนเอง
- เลขคณิตทศนิยมที่สร้างขึ้นในภาษา (ไม่มีข้อผิดพลาดในการปัดเศษทศนิยม)
### Q2: COBOL จัดการเลขคณิตทศนิยมโดยไม่มีข้อผิดพลาดจุดลอยตัวอย่างไร
**A:** COBOL มีประเภททศนิยมดั้งเดิมซึ่งมีความแม่นยำคงที่:
```cobol
       01  PRICE         PIC 9(5)V99.    *> 99999.99
       01  TAX-RATE      PIC 9V999.      *> 0.125
       01  TOTAL         PIC 9(7)V99.

           COMPUTE TOTAL = PRICE * (1 + TAX-RATE)
```

`V` เป็นจุดทศนิยมโดยนัย COBOL ไม่เคยใช้จุดลอยตัวแบบไบนารีเพื่อเงิน
### Q3: โครงสร้างของโปรแกรม COBOL คืออะไร?
**A:** โปรแกรม COBOL ทุกโปรแกรมมี 4 แผนก:
```cobol
       IDENTIFICATION DIVISION.
           PROGRAM-ID. HELLO.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
           WORKING-STORAGE SECTION.
       PROCEDURE DIVISION.
           DISPLAY "Hello, World!".
           STOP RUN.
```

### Q4: ฉันจะอ่านและประมวลผลไฟล์ตามลำดับในภาษา COBOL ได้อย่างไร
**A:** ภาษาโคบอลมีความเป็นเลิศในการประมวลผลไฟล์:
```cobol
       SELECT CUST-FILE ASSIGN TO 'customers.dat'
           ORGANIZATION IS LINE SEQUENTIAL.

       FD CUST-FILE.
       01 CUST-RECORD.
           05 CUST-NAME    PIC X(30).
           05 CUST-BALANCE PIC 9(7)V99.

       PROCEDURE DIVISION.
           OPEN INPUT CUST-FILE
           PERFORM UNTIL EOF
               READ CUST-FILE
                   AT END MOVE 'YES' TO EOF
                   NOT AT END
                       ADD CUST-BALANCE TO GRAND-TOTAL
               END-READ
           END-PERFORM
           CLOSE CUST-FILE.
```

### Q5: มีเครื่องมืออะไรบ้างสำหรับการพัฒนา COBOL ยุคใหม่?
**ตอบ:** ส่วนขยาย GnuCOBOL (โอเพ่นซอร์ส), IBM Enterprise COBOL, Micro Focus และ VS Code มอบสภาพแวดล้อมการพัฒนาที่ทันสมัย สร้างด้วย `cobc -x program.cob`
---

## การแก้ปัญหาลูกโซ่แห่งความคิด
### ปัญหาที่ 1: การสร้างรายงานลูกค้า
**ขั้นตอนที่ 1: ทำความเข้าใจปัญหา**
อ่านบันทึกของลูกค้า คำนวณผลรวม และสร้างรายงานที่จัดรูปแบบ
**ขั้นตอนที่ 2: ระบุแนวทาง**
ใช้ความสามารถในการจัดการไฟล์และการเขียนรายงานของ COBOL
**ขั้นตอนที่ 3: นำไปใช้**```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. CUSTREPORT.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  EOF-FLAG        PIC X VALUE 'N'.
       01  GRAND-TOTAL     PIC 9(9)V99 VALUE 0.
       01  CUST-COUNT      PIC 9(5) VALUE 0.

       PROCEDURE DIVISION.
       MAIN-PARA.
           PERFORM READ-LOOP
               UNTIL EOF-FLAG = 'Y'
           DISPLAY "Total Customers: " CUST-COUNT
           DISPLAY "Grand Total: " GRAND-TOTAL
           STOP RUN.

       READ-LOOP.
           READ CUST-FILE
               AT END MOVE 'Y' TO EOF-FLAG
               NOT AT END
                   ADD 1 TO CUST-COUNT
                   ADD CUST-BALANCE TO GRAND-TOTAL
                   IF CUST-BALANCE > 10000
                       DISPLAY "High Balance: " CUST-NAME
                           " $" CUST-BALANCE
                   END-IF
           END-READ.
```

**ขั้นตอนที่ 4: ยืนยัน**
ตรวจสอบผลรวมกับแหล่งข้อมูล ทดสอบกับ Edge Case (ไฟล์เปล่า ยอดคงเหลือเป็นศูนย์)
### ปัญหาที่ 2: การประมวลผลเป็นชุดพร้อมตัวหยุดการควบคุม
**ขั้นตอนที่ 1: ทำความเข้าใจปัญหา**
ดำเนินธุรกรรมแยกกลุ่มตามแผนก พิมพ์ผลรวมย่อย
**ขั้นตอนที่ 2: ระบุแนวทาง**
ใช้ตรรกะการแบ่งการควบคุม - ตรวจจับเมื่อคีย์กลุ่มเปลี่ยนแปลง
**ขั้นตอนที่ 3: นำไปใช้**```cobol
       PROCESS-TRANSACTIONS.
           MOVE SPACES TO PREV-DEPT
           PERFORM READ-RECORD
           PERFORM UNTIL EOF-FLAG = 'Y'
               IF DEPT NOT = PREV-DEPT
                   PERFORM PRINT-DEPT-TOTAL
                   MOVE DEPT TO PREV-DEPT
                   MOVE 0 TO DEPT-TOTAL
               END-IF
               ADD AMOUNT TO DEPT-TOTAL
               ADD AMOUNT TO GRAND-TOTAL
               PERFORM READ-RECORD
           END-PERFORM
           PERFORM PRINT-DEPT-TOTAL.
```

**ขั้นตอนที่ 4: ยืนยัน**
ตรวจสอบว่ามีการพิมพ์ผลรวมของกลุ่มสุดท้ายแล้ว ตรวจสอบผลรวมทั้งหมดเท่ากับผลรวมของผลรวมแผนก
---

## สรุป
ภาษาโคบอลเป็นมรดกตกทอดของทศวรรษแรกๆ ของการประมวลผลที่ยังคงมีการใช้งานอยู่เนื่องจากการทดแทนไม่สามารถทำได้ในวงกว้าง ระบบธนาคารและภาครัฐของโลกขึ้นอยู่กับโปรแกรม COBOL ที่ทำงานได้อย่างน่าเชื่อถือมานานหลายทศวรรษ แม้ว่าโดยทั่วไปภาษา COBOL จะไม่ได้รับเลือกสำหรับโครงการใหม่ในปัจจุบัน แต่ภาษายังคงมีความสำคัญต่อการรักษาโครงสร้างพื้นฐานที่สนับสนุนการเงินทั่วโลก การขาดแคลนนักพัฒนาภาษาโคบอลทำให้เป็นช่องทางที่ทำกำไรได้