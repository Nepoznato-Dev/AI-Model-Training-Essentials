---
# Metadata
title: "COBOL"
description: "Comprehensive reference for the COBOL programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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

#कोबोल
COBOL (कॉमन बिजनेस-ओरिएंटेड लैंग्वेज) अभी भी उपयोग में आने वाली सबसे पुरानी प्रोग्रामिंग भाषाओं में से एक है, जिसे पहली बार 1959 में विकसित किया गया था। इसे बिजनेस डेटा प्रोसेसिंग - वित्तीय प्रणाली, पेरोल, बैंकिंग, बीमा और सरकारी अनुप्रयोगों के लिए डिज़ाइन किया गया था। COBOL के अंग्रेजी जैसे सिंटैक्स का उद्देश्य केवल प्रोग्रामर ही नहीं, बल्कि व्यवसाय प्रबंधकों द्वारा भी पढ़ने योग्य होना था।
अपनी उम्र के बावजूद, COBOL वैश्विक स्तर पर सभी व्यावसायिक लेनदेन का अनुमानित 30% संसाधित करता है। प्रमुख बैंक, सरकारी एजेंसियां ​​(अमेरिकी सामाजिक सुरक्षा प्रशासन सहित) और बीमा कंपनियां अभी भी COBOL मेनफ्रेम सिस्टम पर निर्भर हैं। 1999 में Y2K बग के डर ने COBOL को सार्वजनिक जागरूकता में वापस ला दिया, और यह भाषा दुनिया भर में महत्वपूर्ण बुनियादी ढांचे को चला रही है।
---

## COBOL क्यों मायने रखता है
- **व्यापार-महत्वपूर्ण बुनियादी ढाँचा**: बैंकिंग और सरकार में प्रतिदिन खरबों डॉलर के लेन-देन की प्रक्रिया करता है।
- **स्थिरता**: 1970 के दशक में लिखे गए COBOL कार्यक्रम आज भी विश्वसनीय रूप से चलते हैं - न्यूनतम परिवर्तनों की आवश्यकता है।
- **पठनीयता**: अंग्रेजी जैसा वाक्यविन्यास व्यावसायिक तर्क को गैर-प्रोग्रामर के लिए समझने योग्य बनाता है।
- **दशमलव अंकगणित**: सटीक वित्तीय गणना के लिए मूल समर्थन (कोई फ़्लोटिंग-पॉइंट राउंडिंग त्रुटियां नहीं)।
- **बैच प्रोसेसिंग**: बड़ी मात्रा में रिकॉर्ड को कुशलतापूर्वक संसाधित करने के लिए डिज़ाइन किया गया।
- **नौकरी बाजार**: COBOL डेवलपर्स की गंभीर कमी रखरखाव भूमिकाओं के लिए उच्च मांग (और उच्च वेतन) पैदा करती है।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **वर्बोज़ सिंटैक्स** | सरल संचालन के लिए कई पंक्तियों की आवश्यकता होती है | भाषा डिज़ाइन के भाग के रूप में स्वीकार करें |
| **आधुनिक नहीं** | कोई कक्षा नहीं, कोई कार्यात्मक प्रोग्रामिंग नहीं, सीमित सार | रखरखाव के लिए उपयोग करें; आधुनिक भाषाओं में नई प्रणालियाँ बनाएँ |
| **मेनफ्रेम निर्भरता** | आमतौर पर आईबीएम मेनफ्रेम (महंगा) पर चलता है | वितरित सिस्टम (GnuCOBOL) पर COBOL कंपाइलर्स का उपयोग करें |
| **घटती कार्यबल** | कम COBOL डेवलपर क्षेत्र में प्रवेश कर रहे हैं | जो लोग इसे जानते हैं उनके लिए उच्च मांग; अच्छा करियर क्षेत्र |
| **कोई वेब/मोबाइल नहीं** | आधुनिक अनुप्रयोग नहीं बना सकते | बैकएंड बैच प्रोसेसिंग के लिए उपयोग करें; आधुनिक अग्रभाग |
---

## सिंटेक्स बुनियादी बातें
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

### फ़ाइल प्रोसेसिंग उदाहरण
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

## उन्नत सिंटैक्स और पैटर्न
### डेटा डिवीजन डीप डाइव
COBOL का डेटा प्रभाग भाषा की सबसे विशिष्ट विशेषता है। यह डेटा संरचनाओं को परिभाषित करने के लिए एक पदानुक्रमित क्रमांकन प्रणाली (स्तर 01-88) का उपयोग करता है।
| स्तर | उद्देश्य | उदाहरण |
|------|------|------|
| **01** | रिकॉर्ड-स्तरीय आइटम (शीर्ष-स्तरीय चर या रिकॉर्ड) | `01 WS-EMPLOYEE.`|
| **02–49** | समूह या प्राथमिक आइटम (उप-क्षेत्र) | `05 EMP-NAME PIC X(30).`|
| **66** | खंड का नाम बदलें (डेटा का वैकल्पिक दृश्य) | `66 EMP-FULL-NAME RENAMES EMP-FIRST.`|
| **77** | स्टैंडअलोन प्रारंभिक आइटम (कोई उप-आइटम नहीं) | `77 WS-COUNTER PIC 9(5).`|
| **88** | स्थिति के नाम (बूलियन-जैसे झंडे) | `88 WS-IS-SENIOR VALUE 'Y'.`|
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

### कॉपी स्टेटमेंट (कॉपीबुक)
कॉपीबुक कोड के पुन: उपयोग के लिए COBOL का तंत्र है - C में`#include`के समान। उन्हें अलग-अलग सदस्यों के रूप में संग्रहीत किया जाता है और संकलन समय पर डाला जाता है।
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

### विविधताएँ प्रदर्शित करें
COBOL संरचित प्रोग्रामिंग के लिए PERFORM स्टेटमेंट के कई फ्लेवर प्रदान करता है।
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

### स्ट्रिंग हैंडलिंग और निरीक्षण
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

## वास्तुकला एवं सिस्टम डिज़ाइन
### चार प्रभाग
प्रत्येक COBOL कार्यक्रम को चार प्रभागों में संरचित किया गया है, प्रत्येक का एक अलग उद्देश्य है:
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

### कार्यक्रम पदानुक्रम
COBOL सिस्टम आम तौर पर एक मुख्य प्रोग्राम के साथ कॉलिंग पदानुक्रम का उपयोग करते हैं जो उपप्रोग्राम को कॉल करता है।
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

### विशिष्ट परियोजना निर्देशिका संरचना
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### GnuCOBOL (ओपन-सोर्स COBOL कंपाइलर)
GnuCOBOL (पूर्व में OpenCOBOL) COBOL को C और फिर मूल मशीन कोड में संकलित करता है, जिससे COBOL Linux, Windows और macOS पर चलने में सक्षम होता है।
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

### आईबीएम मेनफ्रेम जेसीएल (जॉब कंट्रोल लैंग्वेज)
IBM मेनफ्रेम पर, COBOL प्रोग्राम को JCL का उपयोग करके संकलित और निष्पादित किया जाता है।
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

### कंपाइलर विकल्प संदर्भ
| विकल्प | विवरण | उदाहरण |
|--------|---|----|
| `-free`| फ्री-फॉर्मेट स्रोत (कोई कॉलम प्रतिबंध नहीं) | `cobc -free prog.cbl`|
| `-fixed`| निश्चित-प्रारूप (पारंपरिक कॉलम 1-80) | `cobc -fixed prog.cbl`|
| `-O2`| अनुकूलन स्तर 2 | `cobc -O2 prog.cbl`|
| `-g`| डिबग जानकारी उत्पन्न करें | `cobc -g prog.cbl`|
| `-std=cobol2014`| COBOL 2014 मानक का उपयोग करें | `cobc -std=cobol2014 prog.cbl`|
| `-x`| निष्पादन योग्य बनाएं (सिर्फ संकलन नहीं) | `cobc -x prog.cbl`|
| `-I`| कॉपीबुक खोज पथ | `cobc -I ./copybooks prog.cbl`|
| `-Wall`| सभी चेतावनियाँ सक्षम करें | `cobc -Wall prog.cbl`|
---

## परीक्षण एवं डिबगिंग
### COBOL डिबगर तकनीकें
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

### जीडीबी के साथ GnuCOBOL डिबगिंग
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

### सामान्य डिबगिंग पैटर्न
| समस्या | लक्षण | समाधान |
|---------|---------|----------|
| काटा गया डेटा | खेत कट गए | रिकॉर्ड लेआउट से मेल खाते पीआईसी क्लॉज आकार की जांच करें |
| संख्यात्मक अतिप्रवाह | गलत गणना | सत्यापित करें कि PIC 9(n) में पर्याप्त अंक हैं |
| फ़ाइल स्थिति त्रुटियाँ | WS-फ़ाइल-स्थिति '00' नहीं | फ़ाइल डीडी नाम, पथ और अनुमतियाँ जाँचें |
| अनंत पाश | तब तक प्रदर्शन करें जब तक यह कभी समाप्त न हो जाए | सत्यापित करें कि लूप वेरिएबल को लूप के अंदर संशोधित किया गया है |
| कॉल विफलताएँ | गैर-शून्य लौटना | कॉलिंग प्रोग्राम से मेल खाने वाले लिंकेज सेक्शन की जांच करें |
---

## अंतरसंचालनीयता
### कॉल स्टेटमेंट - सबप्रोग्राम्स को कॉल करना
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

### सी इंटरऑपरेबिलिटी (GnuCOBOL)
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

### डेटाबेस कनेक्टिविटी (DB2/COBOL)
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

## डिज़ाइन पैटर्न
### पैटर्न 1: कंट्रोल ब्रेक के साथ बैच प्रोसेसिंग
कंट्रोल ब्रेक पैटर्न सबसे मौलिक COBOL डिज़ाइन पैटर्न है - एक प्रमुख फ़ील्ड द्वारा समूहीकृत रिकॉर्ड को संसाधित करना और उप-योग तैयार करना।
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

### पैटर्न 2: संपादन/सत्यापन पैटर्न
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

### पैटर्न 3: टेबल लुकअप (इन-मेमोरी ऐरे)
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

## प्रदर्शन एवं अनुकूलन
### फ़ाइल I/O अनुकूलन
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

### बैच प्रोसेसिंग अनुकूलन
| तकनीक | प्रभाव | विवरण |
|----|-------|----|
| **ब्लॉक I/O** | उच्च | भौतिक I/O संचालन को कम करने के लिए ब्लॉक कंटेनर का उपयोग करें |
| **अनुक्रमित पहुंच** | उच्च | रैंडम-एक्सेस लुकअप के लिए अनुक्रमित संगठन का उपयोग करें |
| **सॉर्ट करें/मर्ज करें** | मध्यम | बड़े डेटासेट ऑर्डर के लिए SORT क्रिया का उपयोग करें |
| **प्रदर्शन न्यूनतम करें** | मध्यम | बैच में प्रदर्शन धीमा है; इसके बजाय फ़ाइलों को लिखें |
| **COMP/COMP-3** | मध्यम | बाइनरी/पैक्ड फ़ील्ड्स डिस्प्ले न्यूमेरिक | से तेज़ हैं
| **बफर ट्यूनिंग** | मध्यम | अनुक्रमिक फ़ाइल प्रसंस्करण के लिए बफर आकार ट्यून करें |
---

## परिनियोजन और वास्तविक दुनिया में उपयोग
### मेनफ़्रेम परिनियोजन (IBM z/OS)
मेनफ्रेम पर COBOL प्रोग्राम को विभाजित डेटासेट (पीडीएस) में लोड मॉड्यूल के रूप में तैनात किया जाता है। जेसीएल संकलन, लिंकिंग और निष्पादन को नियंत्रित करता है।
```
Deployment pipeline on z/OS:
  Source (PDS) → Compile (JCL) → Link Edit → Load Module (PDS) → Execute (JCL)
```

### वितरित परिनियोजन (GnuCOBOL)
```bash
# Build for Linux deployment
cobc -free -O2 -x src/payroll.cbl -o bin/payroll

# Deploy binary to target server
scp bin/payroll server:/opt/cobol/bin/

# Run as a cron job for batch processing
# 0 2 * * * /opt/cobol/bin/payroll --input /data/daily.dat
```

### वास्तविक दुनिया के उद्योग COBOL का उपयोग कर रहे हैं
| उद्योग | उपयोग | स्केल |
|---|-------|-------|
| **बैंकिंग** | लेनदेन प्रसंस्करण, खाता प्रबंधन | ~85% एटीएम लेनदेन प्रक्रियाएँ |
| **बीमा** | नीति प्रशासन, दावा प्रसंस्करण | प्रमुख बीमाकर्ता COBOL बैकएंड चलाते हैं |
| **सरकार** | सामाजिक सुरक्षा, कर प्रसंस्करण, लाभ | यूएस एसएसए अरबों रिकॉर्ड संसाधित करता है |
| **स्वास्थ्य सेवा** | रोगी रिकॉर्ड, बिलिंग प्रणाली | विरासत अस्पताल सूचना प्रणाली |
| **खुदरा** | इन्वेंटरी प्रबंधन, पॉइंट-ऑफ-सेल बैकएंड | पुराने सिस्टम वाले बड़े खुदरा विक्रेता |
| **टेलीकॉम** | बिलिंग सिस्टम, कॉल रिकॉर्ड प्रोसेसिंग | कॉल डिटेल रिकॉर्ड प्रोसेसिंग |
---

## COBOL का उपयोग कब करें
| परिदृश्य | कोबोल क्यों | बेहतर विकल्प |
|---|---|-----|
| मेनफ्रेम रखरखाव | मौजूदा कोडबेस | — |
| बैच वित्तीय प्रसंस्करण | सिद्ध, विश्वसनीय, सटीक दशमलव गणित | नए सिस्टम के लिए जावा, पायथन |
| सरकारी विरासत प्रणाली | मौजूदा कोडबेस | — |
| कंप्यूटिंग इतिहास सीखना | प्रोग्रामिंग के विकास को समझना | — |
| नए व्यावसायिक अनुप्रयोग | आधुनिक विकल्प नहीं | जावा, सी#, पायथन |
| वेब/मोबाइल विकास | अनुकूल नहीं | जावास्क्रिप्ट, स्विफ्ट, कोटलिन |
| डेटा साइंस/एमएल | अनुकूल नहीं | पायथन, आर |
---

## सिंथेटिक प्रश्नोत्तर
### Q1: 60+ वर्षों के बाद भी बैंकिंग में COBOL का उपयोग क्यों किया जाता है?
**ए:** COBOL अनुमानित 70-80% बैंकिंग लेनदेन संसाधित करता है। कारण:
- विशाल कोडबेस (लाखों लाइनें) जो सही ढंग से काम करते हैं
- अत्यधिक विश्वसनीयता - इन प्रणालियों का उत्पादन में दशकों से परीक्षण किया गया है
- प्रवासन की लागत और जोखिम रखरखाव लागत से अधिक है
- COBOL का वर्बोज़, अंग्रेजी जैसा वाक्य-विन्यास स्व-दस्तावेजीकरण है
- दशमलव अंकगणित भाषा में निर्मित (कोई फ़्लोटिंग-पॉइंट राउंडिंग त्रुटियां नहीं)
### Q2: COBOL फ़्लोटिंग-पॉइंट त्रुटियों के बिना दशमलव अंकगणित को कैसे संभालता है?
**ए:** COBOL में निश्चित परिशुद्धता के साथ मूल दशमलव प्रकार होते हैं:
```cobol
       01  PRICE         PIC 9(5)V99.    *> 99999.99
       01  TAX-RATE      PIC 9V999.      *> 0.125
       01  TOTAL         PIC 9(7)V99.

           COMPUTE TOTAL = PRICE * (1 + TAX-RATE)
```

`V` एक निहित दशमलव बिंदु है। COBOL पैसे के लिए कभी भी बाइनरी फ़्लोटिंग-पॉइंट का उपयोग नहीं करता है।
### Q3: COBOL प्रोग्राम की संरचना क्या है?
**ए:** प्रत्येक COBOL कार्यक्रम के चार प्रभाग होते हैं:
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

### Q4: मैं COBOL में अनुक्रमिक फ़ाइलों को कैसे पढ़ूं और संसाधित करूं?
**ए:** COBOL फ़ाइल प्रोसेसिंग में उत्कृष्ट है:
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

### Q5: आधुनिक COBOL विकास के लिए कौन से उपकरण उपलब्ध हैं?
**ए:** GnuCOBOL (खुला स्रोत), IBM एंटरप्राइज COBOL, माइक्रो फोकस और VS कोड एक्सटेंशन आधुनिक विकास वातावरण प्रदान करते हैं।`cobc -x program.cob`के साथ बनाएं।
---

## चेन-ऑफ़-थॉट समस्या का समाधान
### समस्या 1: ग्राहक रिपोर्ट तैयार करना
**चरण 1: समस्या को समझें**
ग्राहक रिकॉर्ड पढ़ें, कुल की गणना करें और एक स्वरूपित रिपोर्ट तैयार करें।
**चरण 2: दृष्टिकोण को पहचानें**
COBOL की फ़ाइल प्रबंधन और रिपोर्ट लेखन क्षमताओं का उपयोग करें।
**चरण 3: कार्यान्वयन**```cobol
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

**चरण 4: सत्यापित करें**
स्रोत डेटा के विरुद्ध कुल योग की क्रॉस-चेक करें। किनारे के मामलों (खाली फ़ाइल, शून्य शेष) के साथ परीक्षण करें।
### समस्या 2: कंट्रोल ब्रेक के साथ बैच प्रोसेसिंग
**चरण 1: समस्या को समझें**
विभाग द्वारा समूहीकृत प्रक्रिया लेनदेन, उप-योग मुद्रण।
**चरण 2: दृष्टिकोण को पहचानें**
कंट्रोल ब्रेक लॉजिक का उपयोग करें - पता लगाएं कि समूह कुंजी कब बदलती है।
**चरण 3: कार्यान्वयन**```cobol
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

**चरण 4: सत्यापित करें**
जांचें कि अंतिम समूह का कुल योग मुद्रित है। सत्यापित करें कि कुल योग विभाग के कुल योग के बराबर है।
---

## सारांश
COBOL कंप्यूटिंग के शुरुआती दशकों की एक विरासत है जो सक्रिय उपयोग में बनी हुई है क्योंकि बड़े पैमाने पर प्रतिस्थापन संभव नहीं है। दुनिया की बैंकिंग और सरकारी प्रणालियाँ COBOL कार्यक्रमों पर निर्भर हैं जो दशकों से विश्वसनीय रूप से चल रहे हैं। हालाँकि COBOL को आम तौर पर आज किसी नई परियोजना के लिए नहीं चुना जाएगा, लेकिन वैश्विक वित्त का समर्थन करने वाले बुनियादी ढांचे को बनाए रखने के लिए भाषा महत्वपूर्ण बनी हुई है। COBOL डेवलपर्स की कमी इसे एक आकर्षक स्थान बनाती है।