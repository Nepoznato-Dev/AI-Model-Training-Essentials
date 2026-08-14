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
# COBOL
COBOL (Ngôn ngữ định hướng kinh doanh chung) là một trong những ngôn ngữ lập trình lâu đời nhất vẫn được sử dụng, được phát triển lần đầu tiên vào năm 1959. Nó được thiết kế để xử lý dữ liệu kinh doanh - hệ thống tài chính, bảng lương, ngân hàng, bảo hiểm và các ứng dụng chính phủ. Cú pháp giống tiếng Anh của COBOL nhằm mục đích giúp các nhà quản lý doanh nghiệp có thể đọc được chứ không chỉ các lập trình viên.
Bất chấp tuổi đời của nó, COBOL xử lý khoảng 30% tổng số giao dịch kinh doanh trên toàn cầu. Các ngân hàng lớn, cơ quan chính phủ (bao gồm cả Cơ quan An sinh Xã hội Hoa Kỳ) và các công ty bảo hiểm vẫn dựa vào hệ thống máy tính lớn COBOL. Lỗi Y2K năm 1999 đã đưa COBOL trở lại với nhận thức của công chúng và ngôn ngữ này tiếp tục vận hành cơ sở hạ tầng quan trọng trên toàn thế giới.
---

## Tại sao COBOL lại quan trọng
- **Cơ sở hạ tầng quan trọng cho doanh nghiệp**: Xử lý hàng nghìn tỷ đô la giao dịch hàng ngày giữa các ngân hàng và chính phủ.
- **Tính ổn định**: Các chương trình COBOL được viết vào những năm 1970 vẫn chạy đáng tin cậy cho đến ngày nay — chỉ cần thay đổi tối thiểu.
- **Dễ đọc**: Cú pháp giống tiếng Anh giúp logic nghiệp vụ dễ hiểu đối với những người không phải là lập trình viên.
- **Số học thập phân**: Hỗ trợ nguyên bản cho các phép tính tài chính chính xác (không có lỗi làm tròn dấu phẩy động).
- **Xử lý hàng loạt**: Được thiết kế để xử lý khối lượng lớn hồ sơ một cách hiệu quả.
- **Thị trường việc làm**: Sự thiếu hụt trầm trọng các nhà phát triển COBOL tạo ra nhu cầu cao (và mức lương cao) cho vai trò bảo trì.
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Cú pháp dài dòng** | Yêu cầu nhiều dòng cho các thao tác đơn giản | Chấp nhận như một phần của thiết kế ngôn ngữ |
| **Không hiện đại** | Không có lớp học, không có lập trình chức năng, có giới hạn trừu tượng | Sử dụng để bảo trì; xây dựng hệ thống mới bằng các ngôn ngữ hiện đại |
| **Phụ thuộc vào máy tính lớn** | Thường chạy trên máy tính lớn của IBM (đắt tiền) | Sử dụng trình biên dịch COBOL trên hệ thống phân tán (GnuCOBOL) |
| **Lực lượng lao động suy giảm** | Ít nhà phát triển COBOL tham gia vào lĩnh vực này | Nhu cầu cao đối với những người biết điều đó; niche nghề nghiệp tốt |
| **Không có web/di động** | Không thể xây dựng các ứng dụng hiện đại | Sử dụng để xử lý hàng loạt phụ trợ; mặt trận hiện đại |
---

##Cơ bản về cú pháp
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

### Ví dụ về xử lý tệp
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

## Cú pháp & Mẫu nâng cao
### Phân tích sâu về phân chia dữ liệu
Phân chia dữ liệu của COBOL là tính năng đặc biệt nhất của ngôn ngữ. Nó sử dụng hệ thống đánh số phân cấp (cấp 01–88) để xác định cấu trúc dữ liệu.
| Cấp độ | Mục đích | Ví dụ |
|-------|----------|---------|
| **01** | Mục cấp bản ghi (biến hoặc bản ghi cấp cao nhất) | `01 WS-EMPLOYEE.`|
| **02–49** | Nhóm hoặc mục cơ bản (trường con) | `05 EMP-NAME PIC X(30).`|
| **66** | Mệnh đề đổi tên (chế độ xem dữ liệu thay thế) | `66 EMP-FULL-NAME RENAMES EMP-FIRST.`|
| **77** | Mục cơ bản độc lập (không có mục phụ) | `77 WS-COUNTER PIC 9(5).`|
| **88** | Tên điều kiện (cờ giống boolean) | `88 WS-IS-SENIOR VALUE 'Y'.`|
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

### Tuyên bố SAO CHÉP (Bản sao)
Sách sao chép là cơ chế tái sử dụng mã của COBOL — tương tự như`#include`trong C. Chúng được lưu trữ dưới dạng thành viên riêng biệt và được chèn vào thời gian biên dịch.
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

### THỰC HIỆN các biến thể
COBOL cung cấp một số dạng của câu lệnh PERFORM cho lập trình có cấu trúc.
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

### Xử lý và kiểm tra chuỗi
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

## Thiết kế kiến ​​trúc & hệ thống
### Tứ Phần
Mỗi chương trình COBOL được cấu trúc thành bốn phần, mỗi phần phục vụ một mục đích riêng biệt:
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

### Hệ thống phân cấp chương trình
Các hệ thống COBOL thường sử dụng hệ thống phân cấp cuộc gọi với chương trình chính gọi các chương trình con.
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

### Cấu trúc thư mục dự án điển hình
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

## Cấu hình dự án & xây dựng hệ thống
### GnuCOBOL (Trình biên dịch COBOL mã nguồn mở)
GnuCOBOL (trước đây là OpenCOBOL) biên dịch COBOL thành C rồi thành mã máy gốc, cho phép COBOL chạy trên Linux, Windows và macOS.
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

### IBM Mainframe JCL (Ngôn ngữ kiểm soát công việc)
Trên các máy tính lớn của IBM, các chương trình COBOL được biên dịch và thực thi bằng JCL.
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

### Tham khảo các tùy chọn trình biên dịch
| Tùy chọn | Mô tả | Ví dụ |
|--------|-------------|----------|
| `-free`| Nguồn định dạng tự do (không hạn chế cột) | `cobc -free prog.cbl`|
| `-fixed`| Định dạng cố định (cột truyền thống 1-80) | `cobc -fixed prog.cbl`|
| `-O2`| Tối ưu hóa cấp độ 2 | `cobc -O2 prog.cbl`|
| `-g`| Tạo thông tin gỡ lỗi | `cobc -g prog.cbl`|
| `-std=cobol2014`| Sử dụng tiêu chuẩn COBOL 2014 | `cobc -std=cobol2014 prog.cbl`|
| `-x`| Xây dựng tệp thực thi (không chỉ biên dịch) | `cobc -x prog.cbl`|
| `-I`| Đường dẫn tìm kiếm sách sao chép | `cobc -I ./copybooks prog.cbl`|
| `-Wall`| Bật tất cả cảnh báo | `cobc -Wall prog.cbl`|
---

## Kiểm tra & gỡ lỗi
### Kỹ thuật gỡ lỗi COBOL
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

### Gỡ lỗi GnuCOBOL bằng gdb
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

### Các mẫu gỡ lỗi phổ biến
| Vấn đề | Triệu chứng | Giải pháp |
|----------|----------|----------|
| Dữ liệu bị cắt bớt | Cánh đồng bị cắt | Kiểm tra kích thước mệnh đề PIC khớp với bố cục bản ghi |
| Tràn số | Tính toán sai | Xác minh PIC 9(n) có đủ chữ số |
| Lỗi trạng thái tệp | WS-FILE-STATUS không phải '00' | Kiểm tra tên, đường dẫn và quyền của tệp DD |
| Vòng lặp vô hạn | THỰC HIỆN ĐẾN ĐẾN không bao giờ chấm dứt | Xác minh biến vòng lặp được sửa đổi bên trong vòng lặp |
| GỌI thất bại | TRỞ LẠI khác không | Kiểm tra LIÊN KẾT PHẦN phù hợp với chương trình gọi điện |
---

## Khả năng tương tác
### Câu lệnh CALL — Gọi các chương trình con
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

### Khả năng tương tác C (GnuCOBOL)
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

### Kết nối cơ sở dữ liệu (DB2/COBOL)
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

## Mẫu thiết kế
### Mẫu 1: Xử lý hàng loạt với các ngắt kiểm soát
Mẫu ngắt điều khiển là mẫu thiết kế COBOL cơ bản nhất — xử lý các bản ghi được nhóm theo một trường khóa và tạo ra các tổng phụ.
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

### Mẫu 2: Mẫu chỉnh sửa/xác thực
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

### Mẫu 3: Tra cứu bảng (Mảng trong bộ nhớ)
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

## Hiệu suất & Tối ưu hóa
### Tối ưu hóa I/O tệp
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

### Tối ưu hóa xử lý hàng loạt
| Kỹ thuật | Tác động | Mô tả |
|----------|----------|-------------|
| **Chặn I/O** | Cao | Sử dụng BLOCK CONTAINS để giảm các thao tác I/O vật lý |
| **Quyền truy cập được lập chỉ mục** | Cao | Sử dụng TỔ CHỨC CHỈ SỐ để tra cứu truy cập ngẫu nhiên |
| **Sắp xếp/Hợp nhất** | Trung bình | Sử dụng động từ SORT để sắp xếp tập dữ liệu lớn |
| **Giảm thiểu HIỂN THỊ** | Trung bình | HIỂN THỊ chậm theo từng đợt; thay vào đó ghi vào tập tin |
| **COMP/COMP-3** | Trung bình | Các trường nhị phân/đóng gói nhanh hơn số HIỂN THỊ |
| **Điều chỉnh bộ đệm** | Trung bình | Điều chỉnh kích thước bộ đệm để xử lý tệp tuần tự |
---

## Triển khai & Sử dụng trong Thế giới Thực
### Triển khai máy tính lớn (IBM z/OS)
Các chương trình COBOL trên máy tính lớn được triển khai dưới dạng mô-đun tải trong bộ dữ liệu được phân vùng (PDS). JCL kiểm soát việc biên dịch, liên kết và thực thi.
```
Deployment pipeline on z/OS:
  Source (PDS) → Compile (JCL) → Link Edit → Load Module (PDS) → Execute (JCL)
```

### Triển khai phân tán (GnuCOBOL)
```bash
# Build for Linux deployment
cobc -free -O2 -x src/payroll.cbl -o bin/payroll

# Deploy binary to target server
scp bin/payroll server:/opt/cobol/bin/

# Run as a cron job for batch processing
# 0 2 * * * /opt/cobol/bin/payroll --input /data/daily.dat
```

### Các ngành công nghiệp trong thế giới thực sử dụng COBOL
| Công nghiệp | Cách sử dụng | Quy mô |
|----------|-------|-------|
| **Ngân hàng** | Xử lý giao dịch, quản lý tài khoản | Xử lý ~85% giao dịch ATM |
| **Bảo hiểm** | Quản lý chính sách, xử lý khiếu nại | Các công ty bảo hiểm lớn chạy chương trình phụ trợ COBOL |
| **Chính phủ** | An sinh xã hội, xử lý thuế, phúc lợi | SSA Hoa Kỳ xử lý hàng tỷ hồ sơ |
| **Chăm sóc sức khỏe** | Hồ sơ bệnh nhân, hệ thống thanh toán | Hệ thống thông tin bệnh viện cũ |
| **Bán lẻ** | Quản lý hàng tồn kho, phụ trợ điểm bán hàng | Các nhà bán lẻ lớn với hệ thống kế thừa |
| **Viễn thông** | Hệ thống thanh toán, xử lý hồ sơ cuộc gọi | Xử lý bản ghi chi tiết cuộc gọi |
---

## Khi nào nên sử dụng COBOL
| Kịch bản | Tại sao COBOL | Thay thế tốt hơn |
|----------|----------|-------------------|
| Bảo trì máy tính lớn | Cơ sở mã hiện có | — |
| Xử lý tài chính hàng loạt | Toán thập phân đã được chứng minh, đáng tin cậy, chính xác | Java, Python cho hệ thống mới |
| Hệ thống di sản của chính phủ | Cơ sở mã hiện có | — |
| Học lịch sử điện toán | Hiểu sự phát triển của lập trình | — |
| Ứng dụng kinh doanh mới | Không phải sự lựa chọn hiện đại | Java, C#, Python |
| Phát triển web/di động | Không phù hợp | JavaScript, Swift, Kotlin |
| Khoa học dữ liệu / ML | Không phù hợp | Python, R |
---

## Hỏi đáp tổng hợp
### Q1: Tại sao COBOL vẫn được sử dụng trong ngân hàng sau hơn 60 năm?
**Đáp:** COBOL xử lý khoảng 70-80% giao dịch ngân hàng. Những lý do:
- Cơ sở mã khổng lồ (hàng triệu dòng) hoạt động chính xác
- Độ tin cậy cực cao — các hệ thống này đã được thử nghiệm trong sản xuất trong nhiều thập kỷ
- Chi phí và rủi ro di chuyển lớn hơn chi phí bảo trì
- Cú pháp dài dòng, giống tiếng Anh của COBOL tự ghi lại
- Số học thập phân được tích hợp trong ngôn ngữ (không có lỗi làm tròn dấu phẩy động)
### Câu 2: COBOL xử lý số học thập phân như thế nào mà không mắc lỗi dấu phẩy động?
**A:** COBOL có các loại thập phân gốc với độ chính xác cố định:
```cobol
       01  PRICE         PIC 9(5)V99.    *> 99999.99
       01  TAX-RATE      PIC 9V999.      *> 0.125
       01  TOTAL         PIC 9(7)V99.

           COMPUTE TOTAL = PRICE * (1 + TAX-RATE)
```

`V` là dấu thập phân ngụ ý. COBOL không bao giờ sử dụng dấu phẩy động nhị phân để kiếm tiền.
### Câu 3: Cấu trúc của chương trình COBOL là gì?
**A:** Mỗi chương trình COBOL đều có bốn phần:
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

### Q4: Làm cách nào để đọc và xử lý các tệp tuần tự trong COBOL?
**A:** COBOL vượt trội trong việc xử lý tệp:
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

### Câu 5: Có những công cụ nào để phát triển COBOL hiện đại?
**A:** GnuCOBOL (mã nguồn mở), các tiện ích mở rộng IBM Enterprise COBOL, Micro Focus và VS Code cung cấp môi trường phát triển hiện đại. Xây dựng với `cobc -x program.cob`.
---

## Giải quyết vấn đề theo chuỗi suy nghĩ
### Vấn đề 1: Tạo Báo cáo khách hàng
**Bước 1: Tìm hiểu vấn đề**
Đọc hồ sơ khách hàng, tính tổng và tạo báo cáo được định dạng.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng khả năng xử lý tệp và viết báo cáo của COBOL.
**Bước 3: Thực hiện**```cobol
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

**Bước 4: Xác minh**
Kiểm tra chéo tổng số so với dữ liệu nguồn. Kiểm tra với các trường hợp đặc biệt (tệp trống, số dư bằng 0).
### Vấn đề 2: Xử lý hàng loạt có ngắt kiểm soát
**Bước 1: Tìm hiểu vấn đề**
Xử lý các giao dịch được nhóm theo bộ phận, in tổng phụ.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng logic ngắt điều khiển - phát hiện khi khóa nhóm thay đổi.
**Bước 3: Thực hiện**```cobol
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

**Bước 4: Xác minh**
Kiểm tra xem tổng số của nhóm cuối cùng đã được in chưa. Xác minh tổng cộng bằng tổng của tổng số bộ phận.
---

## Bản tóm tắt
COBOL là di sản của những thập kỷ đầu của điện toán vẫn được sử dụng tích cực vì việc thay thế là không khả thi trên quy mô lớn. Hệ thống ngân hàng và chính phủ trên thế giới phụ thuộc vào các chương trình COBOL đã hoạt động đáng tin cậy trong nhiều thập kỷ. Mặc dù COBOL thường không được chọn cho một dự án mới ngày nay nhưng ngôn ngữ này vẫn quan trọng để duy trì cơ sở hạ tầng hỗ trợ tài chính toàn cầu. Sự thiếu hụt các nhà phát triển COBOL khiến nó trở thành một lĩnh vực sinh lợi.