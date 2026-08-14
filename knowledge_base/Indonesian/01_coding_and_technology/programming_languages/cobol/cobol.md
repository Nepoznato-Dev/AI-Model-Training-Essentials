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
COBOL (Common Business-Oriented Language) adalah salah satu bahasa pemrograman tertua yang masih digunakan, pertama kali dikembangkan pada tahun 1959. COBOL dirancang untuk pemrosesan data bisnis — sistem keuangan, penggajian, perbankan, asuransi, dan aplikasi pemerintah. Sintaks COBOL yang mirip bahasa Inggris dimaksudkan agar dapat dibaca oleh manajer bisnis, bukan hanya pemrogram.
Meskipun usianya sudah tua, COBOL memproses sekitar 30% dari seluruh transaksi bisnis secara global. Bank-bank besar, lembaga pemerintah (termasuk Administrasi Jaminan Sosial AS), dan perusahaan asuransi masih mengandalkan sistem mainframe COBOL. Ketakutan akan bug Y2K pada tahun 1999 membawa COBOL kembali ke kesadaran publik, dan bahasa tersebut terus menjalankan infrastruktur penting di seluruh dunia.
---

## Mengapa COBOL Penting
- **Infrastruktur penting bagi bisnis**: Memproses transaksi senilai triliunan dolar setiap hari di perbankan dan pemerintahan.
- **Stabilitas**: Program COBOL yang ditulis pada tahun 1970-an masih berjalan dengan andal hingga saat ini — hanya diperlukan sedikit perubahan.
- **Keterbacaan**: Sintaks mirip bahasa Inggris membuat logika bisnis dapat dimengerti oleh non-pemrogram.
- **Aritmatika desimal**: Dukungan asli untuk perhitungan keuangan yang tepat (tidak ada kesalahan pembulatan floating-point).
- **Pemrosesan batch**: Dirancang untuk memproses rekaman dalam jumlah besar secara efisien.
- **Pasar kerja**: Kekurangan besar pengembang COBOL menciptakan permintaan yang tinggi (dan gaji yang tinggi) untuk peran pemeliharaan.
## Pengorbanan
| Batasan | Detail | Solusi Khas |
|-----------|---------|-------------------|
| **Sintaks verbose** | Membutuhkan banyak baris untuk pengoperasian sederhana | Terima sebagai bagian dari desain bahasa |
| **Tidak modern** | Tidak ada kelas, tidak ada pemrograman fungsional, abstraksi terbatas | Gunakan untuk pemeliharaan; membangun sistem baru dalam bahasa modern |
| **Ketergantungan mainframe** | Biasanya berjalan pada mainframe IBM (mahal) | Gunakan kompiler COBOL pada sistem terdistribusi (GnuCOBOL) |
| **Penurunan tenaga kerja** | Lebih sedikit pengembang COBOL yang memasuki bidang ini | Tingginya permintaan bagi yang mengetahuinya; ceruk karier yang bagus |
| **Tidak ada web/seluler** | Tidak dapat membangun aplikasi modern | Gunakan untuk pemrosesan batch backend; frontend modern |
---

## Dasar Sintaks
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

### Contoh Pemrosesan File
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

## Sintaks & Pola Tingkat Lanjut
### Divisi Data Menyelami Lebih Dalam
Pembagian data COBOL adalah ciri paling khas dari bahasa ini. Ia menggunakan sistem penomoran hierarki (level 01–88) untuk menentukan struktur data.
| Tingkat | Tujuan | Contoh |
|-------|---------|---------|
| **01** | Item tingkat rekaman (variabel atau catatan tingkat atas) | `01 WS-EMPLOYEE.`|
| **02–49** | Item grup atau elemen dasar (sub-bidang) | `05 EMP-NAME PIC X(30).`|
| **66** | Ganti nama klausa (tampilan data alternatif) | `66 EMP-FULL-NAME RENAMES EMP-FIRST.`|
| **77** | Item dasar yang berdiri sendiri (tanpa sub-item) | `77 WS-COUNTER PIC 9(5).`|
| **88** | Nama kondisi (bendera mirip boolean) | `88 WS-IS-SENIOR VALUE 'Y'.`|
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

### Pernyataan COPY (Copybook)
Copybook adalah mekanisme COBOL untuk penggunaan kembali kode — mirip dengan`#include`di C. Copybook disimpan sebagai anggota terpisah dan disisipkan pada waktu kompilasi.
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

### LAKUKAN Variasi
COBOL menyediakan beberapa bentuk pernyataan PERFORM untuk pemrograman terstruktur.
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

### Penanganan dan Inspeksi Senar
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

## Arsitektur & Desain Sistem
### Empat Divisi
Setiap program COBOL disusun menjadi empat divisi, masing-masing memiliki tujuan berbeda:
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

### Hierarki Program
Sistem COBOL biasanya menggunakan hierarki pemanggilan dengan program utama yang memanggil subprogram.
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

### Struktur Direktori Proyek Khas
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

## Konfigurasi Proyek & Sistem Pembangunan
### GnuCOBOL (Kompiler COBOL Sumber Terbuka)
GnuCOBOL (sebelumnya OpenCOBOL) mengkompilasi COBOL ke C dan kemudian ke kode mesin asli, memungkinkan COBOL berjalan di Linux, Windows, dan macOS.
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

### IBM Mainframe JCL (Bahasa Kontrol Pekerjaan)
Pada mainframe IBM, program COBOL dikompilasi dan dieksekusi menggunakan JCL.
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

### Referensi Opsi Kompiler
| Pilihan | Deskripsi | Contoh |
|--------|-------------|---------|
| `-free`| Sumber format bebas (tanpa batasan kolom) | `cobc -free prog.cbl`|
| `-fixed`| Format tetap (kolom tradisional 1-80) | `cobc -fixed prog.cbl`|
| `-O2`| Optimasi tingkat 2 | `cobc -O2 prog.cbl`|
| `-g`| Hasilkan informasi debug | `cobc -g prog.cbl`|
| `-std=cobol2014`| Gunakan standar COBOL 2014 | `cobc -std=cobol2014 prog.cbl`|
| `-x`| Bangun yang dapat dieksekusi (bukan hanya kompilasi) | `cobc -x prog.cbl`|
| `-I`| Jalur pencarian copybook | `cobc -I ./copybooks prog.cbl`|
| `-Wall`| Aktifkan semua peringatan | `cobc -Wall prog.cbl`|
---

## Pengujian & Debugging
### Teknik Debugger COBOL
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

### GnuCOBOL Men-debug dengan gdb
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

### Pola Debugging Umum
| Masalah | Gejala | Solusi |
|---------|---------|----------|
| Data terpotong | Ladang terpotong | Periksa ukuran klausa PIC sesuai dengan tata letak rekaman |
| Luapan numerik | Perhitungan salah | Pastikan PIC 9(n) memiliki cukup digit |
| Kesalahan status berkas | WS-FILE-STATUS bukan '00' | Periksa nama file DD, jalur, dan izin |
| Lingkaran tak terbatas | PERFORM SAMPAI tidak pernah berakhir | Verifikasi variabel loop diubah di dalam loop |
| Kegagalan PANGGILAN | MENGEMBALIKAN bukan nol | Periksa LINKAGE BAGIAN cocok dengan program panggilan |
---

## Interoperabilitas
### Pernyataan CALL — Memanggil Subprogram
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

### C Interoperabilitas (GnuCOBOL)
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

### Konektivitas Basis Data (DB2/COBOL)
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

## Pola Desain
### Pola 1: Pemrosesan Batch dengan Pemutusan Kontrol
Pola pemutusan kontrol adalah pola desain COBOL yang paling mendasar — ​​memproses catatan yang dikelompokkan berdasarkan bidang utama dan menghasilkan subtotal.
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

### Pola 2: Pola Edit/Validasi
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

### Pola 3: Pencarian Tabel (Array Dalam Memori)
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

## Kinerja & Optimasi
### Optimasi I/O Berkas
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

### Optimasi Pemrosesan Batch
| Teknik | Dampak | Deskripsi |
|-----------|--------|-------------|
| **Blokir I/O** | Tinggi | Gunakan BLOCK CONTAIN untuk mengurangi operasi I/O fisik |
| **Akses terindeks** | Tinggi | Gunakan ORGANISASI TERINDEKS untuk pencarian akses acak |
| **Urutkan/Gabungkan** | Sedang | Gunakan kata kerja SORT untuk pemesanan kumpulan data besar |
| **Minimalkan TAMPILAN** | Sedang | DISPLAY lambat dalam batch; tulis ke file sebagai gantinya |
| **COMP/COMP-3** | Sedang | Bidang biner/dikemas lebih cepat daripada DISPLAY numerik |
| **Penyetelan penyangga** | Sedang | Sesuaikan ukuran buffer untuk pemrosesan file berurutan |
---

## Penerapan & Penggunaan di Dunia Nyata
### Penerapan Mainframe (IBM z/OS)
Program COBOL pada mainframe disebarkan sebagai modul beban dalam kumpulan data yang dipartisi (PDS). JCL mengontrol kompilasi, penautan, dan eksekusi.
```
Deployment pipeline on z/OS:
  Source (PDS) → Compile (JCL) → Link Edit → Load Module (PDS) → Execute (JCL)
```

### Penerapan Terdistribusi (GnuCOBOL)
```bash
# Build for Linux deployment
cobc -free -O2 -x src/payroll.cbl -o bin/payroll

# Deploy binary to target server
scp bin/payroll server:/opt/cobol/bin/

# Run as a cron job for batch processing
# 0 2 * * * /opt/cobol/bin/payroll --input /data/daily.dat
```

### Industri Dunia Nyata Menggunakan COBOL
| Industri | Penggunaan | Skala |
|----------|-------|-------|
| **Perbankan** | Pemrosesan transaksi, manajemen akun | Memproses ~85% transaksi ATM |
| **Asuransi** | Administrasi polis, pemrosesan klaim | Perusahaan asuransi besar menjalankan backend COBOL |
| **Pemerintah** | Jaminan Sosial, pemrosesan pajak, tunjangan | SSA AS memproses miliaran catatan |
| **Perawatan Kesehatan** | Catatan pasien, sistem penagihan | Sistem informasi rumah sakit lama |
| **Eceran** | Manajemen inventaris, backend tempat penjualan | Pengecer besar dengan sistem lama |
| **Telekomunikasi** | Sistem penagihan, pemrosesan catatan panggilan | Pemrosesan catatan detail panggilan |
---

## Kapan Menggunakan COBOL
| Skenario | Mengapa COBOL | Alternatif Lebih Baik |
|----------|----------|-------------------|
| Pemeliharaan mainframe | Basis kode yang ada | — |
| Pemrosesan keuangan batch | Matematika desimal yang terbukti, andal, dan tepat | Java, Python untuk sistem baru |
| Sistem warisan pemerintah | Basis kode yang ada | — |
| Belajar sejarah komputasi | Memahami evolusi pemrograman | — |
| Aplikasi bisnis baru | Bukan pilihan modern | Jawa, C#, Python |
| Pengembangan web/seluler | Tidak cocok | JavaScript, Swift, Kotlin |
| Ilmu data / ML | Tidak cocok | Piton, R |
---

## Tanya Jawab Sintetis
### Q1: Mengapa COBOL masih digunakan di perbankan setelah 60+ tahun?
**A:** COBOL memproses sekitar 70-80% transaksi perbankan. Alasannya:
- Basis kode besar (jutaan baris) yang berfungsi dengan benar
- Keandalan yang ekstrim — sistem ini telah diuji dalam produksi selama beberapa dekade
- Biaya dan risiko migrasi melebihi biaya pemeliharaan
- Sintaks COBOL yang bertele-tele dan mirip bahasa Inggris dapat didokumentasikan sendiri
- Aritmatika desimal dibangun ke dalam bahasa (tidak ada kesalahan pembulatan floating-point)
### Q2: Bagaimana COBOL menangani aritmatika desimal tanpa kesalahan floating-point?
**A:** COBOL memiliki tipe desimal asli dengan presisi tetap:
```cobol
       01  PRICE         PIC 9(5)V99.    *> 99999.99
       01  TAX-RATE      PIC 9V999.      *> 0.125
       01  TOTAL         PIC 9(7)V99.

           COMPUTE TOTAL = PRICE * (1 + TAX-RATE)
```

`V` adalah titik desimal tersirat. COBOL tidak pernah menggunakan floating-point biner untuk uang.
### Q3: Apa struktur program COBOL?
**A:** Setiap program COBOL memiliki empat divisi:
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

### Q4: Bagaimana cara membaca dan memproses file berurutan di COBOL?
**A:** COBOL unggul dalam pemrosesan file:
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

### Q5: Alat apa saja yang tersedia untuk pengembangan COBOL modern?
**A:** GnuCOBOL (open source), IBM Enterprise COBOL, Micro Focus, dan ekstensi VS Code menyediakan lingkungan pengembangan modern. Bangun dengan`cobc -x program.cob`.
---

## Pemecahan Masalah Rantai Pemikiran
### Masalah 1: Membuat Laporan Pelanggan
**Langkah 1: Pahami Masalahnya**
Baca catatan pelanggan, hitung total, dan buat laporan berformat.
**Langkah 2: Identifikasi Pendekatannya**
Gunakan kemampuan penanganan file dan penulisan laporan COBOL.
**Langkah 3: Terapkan**```cobol
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

**Langkah 4: Verifikasi**
Periksa ulang total terhadap data sumber. Uji dengan kasus tepi (file kosong, saldo nol).
### Masalah 2: Pemrosesan Batch dengan Pemutusan Kontrol
**Langkah 1: Pahami Masalahnya**
Proses transaksi dikelompokkan berdasarkan departemen, mencetak subtotal.
**Langkah 2: Identifikasi Pendekatannya**
Gunakan logika pemutusan kontrol — mendeteksi kapan kunci grup berubah.
**Langkah 3: Terapkan**```cobol
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

**Langkah 4: Verifikasi**
Periksa apakah total grup terakhir sudah tercetak. Verifikasikan total keseluruhan sama dengan jumlah total departemen.
---

## Ringkasan
COBOL adalah warisan dekade awal komputasi yang masih digunakan secara aktif karena penggantian dalam skala besar tidak dapat dilakukan. Sistem perbankan dan pemerintahan dunia bergantung pada program COBOL yang telah berjalan dengan baik selama beberapa dekade. Meskipun COBOL biasanya tidak dipilih untuk proyek baru saat ini, bahasa tersebut tetap penting untuk menjaga infrastruktur yang mendukung keuangan global. Kurangnya pengembang COBOL menjadikannya ceruk yang menguntungkan.