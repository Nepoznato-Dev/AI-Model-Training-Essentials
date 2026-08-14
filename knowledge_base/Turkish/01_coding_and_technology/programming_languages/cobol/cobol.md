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
#COBOL
COBOL (Ortak İş Odaklı Dil), halen kullanımda olan en eski programlama dillerinden biridir ve ilk olarak 1959'da geliştirilmiştir. Finansal sistemler, bordro, bankacılık, sigorta ve hükümet uygulamaları gibi ticari veri işleme için tasarlanmıştır. COBOL'un İngilizce benzeri sözdiziminin yalnızca programcılar tarafından değil, işletme yöneticileri tarafından da okunabilmesi amaçlandı.
COBOL, yaşına rağmen dünya genelindeki tüm ticari işlemlerin tahmini %30'unu gerçekleştiriyor. Büyük bankalar, devlet kurumları (ABD Sosyal Güvenlik İdaresi dahil) ve sigorta şirketleri hâlâ COBOL ana bilgisayar sistemlerine güveniyor. 1999'daki Y2K hata korkusu, COBOL'u kamuoyunun farkındalığına geri getirdi ve dil, dünya çapında kritik altyapıyı çalıştırmaya devam ediyor.
---

## COBOL Neden Önemlidir
- **İş açısından kritik altyapı**: Bankacılık ve devlet genelinde günlük olarak trilyonlarca dolarlık işlem gerçekleştirir.
- **Kararlılık**: 1970'lerde yazılan COBOL programları bugün hala güvenilir bir şekilde çalışıyor; minimum düzeyde değişiklik gerekiyor.
- **Okunabilirlik**: İngilizce benzeri sözdizimi, iş mantığını programcı olmayanlar için de anlaşılır kılar.
- **Ondalık aritmetik**: Hassas finansal hesaplamalar için yerel destek (kayan nokta yuvarlama hatası yok).
- **Toplu işleme**: Büyük hacimli kayıtları verimli bir şekilde işlemek için tasarlanmıştır.
- **İş piyasası**: COBOL geliştiricilerindeki ciddi eksiklik, bakım rolleri için yüksek talep (ve yüksek maaşlar) yaratıyor.
## Takaslar
| Sınırlama | Ayrıntılar | Tipik Geçici Çözüm |
|-----------|------------|-----------|
| **Ayrıntılı söz dizimi** | Basit işlemler için çok sayıda satır gerekir | Dil tasarımının bir parçası olarak kabul edin |
| **Modern değil** | Sınıf yok, işlevsel programlama yok, sınırlı soyutlamalar | Bakım için kullanın; modern dillerde yeni sistemler kurmak |
| **Ana bilgisayar bağımlılığı** | Genellikle IBM ana bilgisayarlarında çalışır (pahalı) | Dağıtılmış sistemlerde COBOL derleyicilerini kullanın (GnuCOBOL) |
| **İş gücünde azalma** | Daha az COBOL geliştiricisi sahaya giriyor | Bilenler için yoğun talep; iyi kariyer nişi |
| **Web/mobil yok** | Modern uygulamalar oluşturulamıyor | Arka uç toplu işleme için kullanın; modern arayüzler |
---

## Söz Diziminin Temelleri
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

### Dosya İşleme Örneği
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

## Gelişmiş Sözdizimi ve Desenler
### Veri Bölümü Derin İncelemesi
COBOL'un veri bölümü dilin en ayırt edici özelliğidir. Veri yapılarını tanımlamak için hiyerarşik bir numaralandırma sistemi (01-88 arası düzeyler) kullanır.
| Seviye | Amaç | Örnek |
|----------|------------|---------|
| **01** | Kayıt düzeyi öğesi (üst düzey değişken veya kayıt) | `01 WS-EMPLOYEE.`|
| **02–49** | Grup veya temel öğeler (alt alanlar) | `05 EMP-NAME PIC X(30).`|
| **66** | Cümleyi yeniden adlandırın (verilerin alternatif görünümü) | `66 EMP-FULL-NAME RENAMES EMP-FIRST.`|
| **77** | Bağımsız temel öğe (alt öğe yok) | `77 WS-COUNTER PIC 9(5).`|
| **88** | Koşul adları (boolean benzeri işaretler) | `88 WS-IS-SENIOR VALUE 'Y'.`|
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

### KOPYALAMA Bildirimi (Kopyalama Defterleri)
Kopyalama defterleri, COBOL'un kodun yeniden kullanımına yönelik mekanizmasıdır; C'deki `#include`'ye benzer. Ayrı üyeler olarak depolanırlar ve derleme zamanında eklenirler.
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

### Varyasyonları GERÇEKLEŞTİRİN
COBOL, yapılandırılmış programlama için PERFORM ifadesinin çeşitli biçimlerini sağlar.
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

### Dizi İşleme ve Denetim
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

## Mimari ve Sistem Tasarımı
### Dört Bölüm
Her COBOL programı, her biri farklı bir amaca hizmet eden dört bölümden oluşmaktadır:
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

### Program Hiyerarşisi
COBOL sistemleri genellikle alt programları çağıran bir ana programla bir çağrı hiyerarşisi kullanır.
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

### Tipik Proje Dizin Yapısı
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

## Proje Yapılandırması ve Oluşturma Sistemi
### GnuCOBOL (Açık Kaynak COBOL Derleyicisi)
GnuCOBOL (eski adıyla OpenCOBOL), COBOL'u C'ye ve ardından yerel makine koduna derleyerek COBOL'un Linux, Windows ve macOS'ta çalışmasını sağlar.
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

### IBM Mainframe JCL (İş Kontrol Dili)
IBM ana bilgisayarlarında COBOL programları JCL kullanılarak derlenir ve yürütülür.
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

### Derleyici Seçenekleri Referansı
| Seçenek | Açıklama | Örnek |
|----------|----------------|------------|
| `-free`| Serbest biçimli kaynak (sütun kısıtlaması yok) | `cobc -free prog.cbl`|
| `-fixed`| Sabit format (geleneksel sütunlar 1-80) | `cobc -fixed prog.cbl`|
| `-O2`| Optimizasyon düzeyi 2 | `cobc -O2 prog.cbl`|
| `-g`| Hata ayıklama bilgileri oluştur | `cobc -g prog.cbl`|
| `-std=cobol2014`| COBOL 2014 standardını kullanın | `cobc -std=cobol2014 prog.cbl`|
| `-x`| Yürütülebilir dosya oluştur (yalnızca derleme değil) | `cobc -x prog.cbl`|
| `-I`| Defterin arama yolu | `cobc -I ./copybooks prog.cbl`|
| `-Wall`| Tüm uyarıları etkinleştir | `cobc -Wall prog.cbl`|
---

## Test Etme ve Hata Ayıklama
### COBOL Hata Ayıklayıcı Teknikleri
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

### GnuCOBOL gdb ile hata ayıklama
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

### Yaygın Hata Ayıklama Modelleri
| Sorun | Belirti | Çözüm |
|-----------|-----------|----------|
| Kesilmiş veriler | Alanlar kesildi | PIC yan tümcesi boyutlarının kayıt düzeniyle eşleştiğini kontrol edin |
| Sayısal taşma | Yanlış hesaplamalar | PIC 9(n)'nin yeterli rakama sahip olduğunu doğrulayın |
| Dosya durumu hataları | WS-DOSYA-DURUMU '00' değil | Dosya DD adlarını, yollarını ve izinlerini kontrol edin |
| Sonsuz döngü | PERFORM KADAR hiçbir zaman sona ermez | Döngü değişkeninin döngü içinde değiştirildiğini doğrulayın |
| ÇAĞRI hataları | Sıfırdan farklı bir yere DÖNÜŞ | LINKAGE SECTION'ın çağıran programla eşleştiğini kontrol edin |
---

## Birlikte Çalışabilirlik
### CALL İfadesi — Alt Programların Çağrılması
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

### C Birlikte Çalışabilirliği (GnuCOBOL)
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

### Veritabanı Bağlantısı (DB2/COBOL)
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

## Tasarım Desenleri
### Model 1: Kontrol Kesintileriyle Toplu İşleme
Kontrol kesme modeli, en temel COBOL tasarım modelidir; anahtar alana göre gruplandırılmış kayıtları işler ve alt toplamlar üretir.
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

### Desen 2: Düzenleme/Doğrulama Modeli
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

### Desen 3: Tablo Arama (Bellek İçi Dizi)
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

## Performans ve Optimizasyon
### Dosya G/Ç Optimizasyonu
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

### Toplu İşleme Optimizasyonu
| Tekniği | Etki | Açıklama |
|-----------|-----------|------------|
| **G/Ç'yi engelle** | Yüksek | Fiziksel G/Ç işlemlerini azaltmak için BLOCK CONTAINS kullanın |
| **Dizine alınmış erişim** | Yüksek | Rastgele erişimli aramalar için DİZİNLİ ORGANİZASYONU kullanın |
| **Sırala/Birleştir** | Orta | Büyük veri kümesi sıralaması için SORT fiilini kullanın |
| **EKRANI simge durumuna küçült** | Orta | DISPLAY toplu olarak yavaş; bunun yerine dosyalara yaz |
| **COMP/COMP-3** | Orta | İkili/paketlenmiş alanlar DISPLAY sayısaldan daha hızlıdır |
| **Arabellek ayarlama** | Orta | Sıralı dosya işleme için arabellek boyutlarını ayarlayın |
---

## Dağıtım ve Gerçek Dünya Kullanımı
### Ana Bilgisayar Dağıtımı (IBM z/OS)
Ana bilgisayarlardaki COBOL programları, bölümlenmiş veri kümelerinde (PDS) yük modülleri olarak dağıtılır. JCL derlemeyi, bağlamayı ve yürütmeyi kontrol eder.
```
Deployment pipeline on z/OS:
  Source (PDS) → Compile (JCL) → Link Edit → Load Module (PDS) → Execute (JCL)
```

### Dağıtılmış Dağıtım (GnuCOBOL)
```bash
# Build for Linux deployment
cobc -free -O2 -x src/payroll.cbl -o bin/payroll

# Deploy binary to target server
scp bin/payroll server:/opt/cobol/bin/

# Run as a cron job for batch processing
# 0 2 * * * /opt/cobol/bin/payroll --input /data/daily.dat
```

### COBOL Kullanan Gerçek Dünya Endüstrileri
| Sanayi | Kullanım | Ölçek |
|----------|-------|-------|
| **Bankacılık** | İşlem gerçekleştirme, hesap yönetimi | ATM işlemlerinin ~%85'ini gerçekleştirir |
| **Sigorta** | Poliçe yönetimi, taleplerin işlenmesi | Büyük sigorta şirketleri COBOL arka uçlarını çalıştırıyor |
| **Hükümet** | Sosyal Güvenlik, vergi işlemleri, sosyal yardımlar | ABD SSA milyarlarca kaydı işliyor |
| **Sağlık Hizmetleri** | Hasta kayıtları, faturalandırma sistemleri | Eski hastane bilgi sistemleri |
| **Perakende** | Envanter yönetimi, satış noktası arka uçları | Eski sistemlere sahip büyük perakendeciler |
| **Telekom** | Faturalandırma sistemleri, çağrı kaydı işleme | Arama detayı kayıt işleme |
---

## COBOL Ne Zaman Kullanılmalı?
| Senaryo | Neden COBOL | Daha İyi Alternatif |
|----------|----------|----------|
| Ana bilgisayar bakımı | Mevcut kod tabanı | — |
| Toplu finansal işlemler | Kanıtlanmış, güvenilir, hassas ondalık matematik | Yeni sistemler için Java, Python |
| Devletin eski sistemleri | Mevcut kod tabanı | — |
| Bilgisayar tarihini öğrenme | Programlamanın evrimini anlamak | — |
| Yeni iş uygulamaları | Modern seçim değil | Java, C#, Python |
| Web/mobil geliştirme | Uygun değil | JavaScript, Swift, Kotlin |
| Veri bilimi / ML | Uygun değil | Python, R |
---

## Sentetik Soru-Cevap
### S1: COBOL neden 60 yıldan fazla bir süre sonra bankacılıkta hala kullanılıyor?
**C:** COBOL, bankacılık işlemlerinin tahmini olarak %70-80'ini gerçekleştirmektedir. Sebepler:
- Doğru çalışan devasa kod tabanları (milyonlarca satır)
- Olağanüstü güvenilirlik — bu sistemler onlarca yıldır üretimde test edilmektedir
- Geçişin maliyeti ve riski bakım maliyetlerinden daha ağır basmaktadır
- COBOL'un ayrıntılı, İngilizce benzeri sözdizimi kendi kendini belgelemektedir
- Dilde yerleşik ondalık aritmetik (kayan nokta yuvarlama hatası yok)
### S2: COBOL, kayan nokta hataları olmadan ondalık aritmetiği nasıl işler?
**C:** COBOL'de sabit duyarlıklı yerel ondalık sayı türleri bulunur:
```cobol
       01  PRICE         PIC 9(5)V99.    *> 99999.99
       01  TAX-RATE      PIC 9V999.      *> 0.125
       01  TOTAL         PIC 9(7)V99.

           COMPUTE TOTAL = PRICE * (1 + TAX-RATE)
```

`V` örtülü bir ondalık sayıdır. COBOL para için asla ikili kayan nokta kullanmaz.
### S3: COBOL programının yapısı nedir?
**C:** Her COBOL programının dört bölümü vardır:
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

### S4: COBOL'da sıralı dosyaları nasıl okuyup işleyebilirim?
**C:** COBOL dosya işlemede üstündür:
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

### S5: Modern COBOL geliştirme için hangi araçlar mevcut?
**C:** GnuCOBOL (açık kaynak), IBM Enterprise COBOL, Micro Focus ve VS Code uzantıları modern geliştirme ortamları sağlar.`cobc -x program.cob`ile oluşturun.
---

## Düşünce Zinciri Problem Çözme
### Sorun 1: Müşteri Raporu Oluşturma
**1. Adım: Sorunu Anlayın**
Müşteri kayıtlarını okuyun, toplamları hesaplayın ve biçimlendirilmiş bir rapor oluşturun.
**2. Adım: Yaklaşımı Belirleyin**
COBOL'un dosya işleme ve rapor yazma yeteneklerini kullanın.
**3. Adım: Uygulama**```cobol
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

**4. Adım: Doğrulayın**
Toplamları kaynak verilere göre çapraz kontrol edin. Uç durumlarla test edin (boş dosya, sıfır bakiye).
### Sorun 2: Kontrol Kesintileriyle Toplu İşleme
**1. Adım: Sorunu Anlayın**
Departmanlara göre gruplandırılmış işlemleri işleyin, alt toplamları yazdırın.
**2. Adım: Yaklaşımı Belirleyin**
Kontrol kesme mantığını kullanın — grup anahtarının ne zaman değiştiğini tespit edin.
**3. Adım: Uygulama**```cobol
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

**4. Adım: Doğrulayın**
Son grubun toplamının yazdırılıp yazdırılmadığını kontrol edin. Genel toplamın bölüm toplamlarının toplamına eşit olduğunu doğrulayın.
---

## Özet
COBOL, bilgi işlemin ilk on yıllarından kalma bir mirastır ve büyük ölçekte değiştirilmesi mümkün olmadığından aktif kullanımda kalır. Dünyanın bankacılık ve hükümet sistemleri onlarca yıldır güvenilir bir şekilde çalışan COBOL programlarına bağlıdır. COBOL bugün yeni bir proje için genellikle seçilmezken, dil, küresel finansı destekleyen altyapının sürdürülmesi açısından önemini koruyor. COBOL geliştiricilerinin eksikliği onu kazançlı bir niş haline getiriyor.