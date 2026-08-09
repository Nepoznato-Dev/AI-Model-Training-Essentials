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
# КОБОЛ
COBOL (Common Business-Oriented Language) — один из старейших языков программирования, который до сих пор используется. Впервые он был разработан в 1959 году. Он был разработан для обработки бизнес-данных — финансовых систем, расчетов заработной платы, банковского дела, страхования и государственных приложений. Англоподобный синтаксис COBOL был предназначен для чтения бизнес-менеджерами, а не только программистами.
Несмотря на свой возраст, COBOL обрабатывает около 30% всех бизнес-транзакций в мире. Крупные банки, правительственные учреждения (включая Администрацию социального обеспечения США) и страховые компании по-прежнему полагаются на мейнфреймы COBOL. Опасения по поводу ошибки 2000 года в 1999 году вернули COBOL в известность общественности, и этот язык продолжает управлять критически важной инфраструктурой по всему миру.
---

## Почему COBOL важен
- **Критически важная для бизнеса инфраструктура**: ежедневно обрабатывает транзакции на триллионы долларов в банковских и государственных учреждениях.
- **Стабильность**: программы на языке COBOL, написанные в 1970-х годах, по-прежнему надежно работают и сегодня — требуются минимальные изменения.
- **Читаемость**: синтаксис, подобный английскому, делает бизнес-логику понятной непрограммистам.
- **Десятичная арифметика**: встроенная поддержка точных финансовых расчетов (без ошибок округления с плавающей запятой).
- **Пакетная обработка**: предназначена для эффективной обработки больших объемов записей.
- **Рынок труда**: острая нехватка разработчиков COBOL создает высокий спрос (и высокие зарплаты) на должности технического обслуживания.
## Компромиссы
| Ограничение | Подробности | Типичный обходной путь |
|-----------|---------|-------------------|
| **Подробный синтаксис** | Требуется много строк для простых операций | Принять как часть языкового дизайна |
| **Не современно** | Никаких классов, никакого функционального программирования, ограниченных абстракций | Использование для технического обслуживания; создавать новые системы на современных языках |
| **Зависимость от мейнфрейма** | Обычно работает на мэйнфреймах IBM (дорого) | Использование компиляторов COBOL в распределенных системах (GnuCOBOL) |
| **Сокращение рабочей силы** | Меньше разработчиков COBOL выходит на поле | Высокий спрос на тех, кто это знает; хорошая карьерная ниша |
| **Нет веб-версии или мобильного устройства** | Не могу создавать современные приложения | Используйте для серверной пакетной обработки; современные интерфейсы |
---

## Основы синтаксиса
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

### Пример обработки файла
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

## Расширенный синтаксис и шаблоны
### Подробный обзор отдела данных
Разделение данных COBOL — наиболее отличительная особенность языка. Он использует иерархическую систему нумерации (уровни 01–88) для определения структур данных.
| Уровень | Цель | Пример |
|-------|---------|---------|
| **01** | Элемент уровня записи (переменная или запись верхнего уровня) | `01 WS-EMPLOYEE.`|
| **02–49** | Группа или элементарные элементы (подполя) | `05 EMP-NAME PIC X(30).`|
| **66** | Предложение переименования (альтернативный вид данных) | `66 EMP-FULL-NAME RENAMES EMP-FIRST.`|
| **77** | Отдельный элементарный элемент (без подпунктов) |  __ЗАЩИЩЕНО_3__ |
| **88** | Имена условий (логические флаги) | `88 WS-IS-SENIOR VALUE 'Y'.`|
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

### Заявление COPY (тетради)
Тетради — это механизм COBOL для повторного использования кода, аналогичный`#include`в C. Они хранятся как отдельные члены и вставляются во время компиляции.
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

### ИСПОЛНИТЕЛЬНЫЕ Вариации
COBOL предоставляет несколько разновидностей оператора PERFORM для структурного программирования.
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

### Обработка и проверка строк
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

## Архитектура и системный дизайн
### Четыре дивизии
Каждая программа COBOL разделена на четыре раздела, каждый из которых служит определенной цели:
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

### Иерархия программ
Системы COBOL обычно используют иерархию вызовов, в которой основная программа вызывает подпрограммы.
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

### Типичная структура каталога проекта
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

## Конфигурация проекта и система сборки
### GnuCOBOL (компилятор COBOL с открытым исходным кодом)
GnuCOBOL (ранее OpenCOBOL) компилирует COBOL в C, а затем в собственный машинный код, позволяя COBOL работать в Linux, Windows и macOS.
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

### IBM Mainframe JCL (язык управления заданиями)
На мэйнфреймах IBM программы COBOL компилируются и выполняются с использованием JCL.
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

### Справочник по параметрам компилятора
| Вариант | Описание | Пример |
|--------|-------------|---------|
| `-free`| Источник в свободном формате (без ограничений по столбцам) | `cobc -free prog.cbl`|
| `-fixed`| Фиксированный формат (традиционные столбцы 1–80) |  __ЗАЩИЩЕНО_3__ |
| `-O2`| Уровень оптимизации 2 | `cobc -O2 prog.cbl`|
| `-g`| Создание отладочной информации | `cobc -g prog.cbl`|
| `-std=cobol2014`| Используйте стандарт COBOL 2014 | `cobc -std=cobol2014 prog.cbl`|
| `-x`| Сборка исполняемого файла (а не просто компиляция) | `cobc -x prog.cbl`|
| `-I`| Путь поиска тетради | `cobc -I ./copybooks prog.cbl`|
| `-Wall`| Включить все предупреждения | `cobc -Wall prog.cbl`|
---

## Тестирование и отладка
### Методы отладки COBOL
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

### GnuCOBOL Отладка с помощью GDB
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

### Общие шаблоны отладки
| Проблема | Симптом | Решение |
|---------|---------|----------|
| Сокращенные данные | Поля отрезаны | Проверьте, соответствуют ли размеры пунктов PIC макету записи |
| Числовое переполнение | Неправильные расчеты | Убедитесь, что в PIC 9(n) достаточно цифр |
| Ошибки статуса файла | WS-FILE-STATUS не '00' | Проверьте имена, пути и разрешения файлов DD |
| Бесконечный цикл | PERFORM UNTIL никогда не завершается | Убедитесь, что переменная цикла изменена внутри цикла |
| Ошибки вызова | ВОЗВРАЩАЕТСЯ ненулевое | Проверьте, соответствует ли РАЗДЕЛ СВЯЗИ вызывающей программе |
---

## Совместимость
### Оператор CALL — вызов подпрограмм
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

### Совместимость с C (GnuCOBOL)
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

### Подключение к базе данных (DB2/COBOL)
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

## Шаблоны проектирования
### Шаблон 1. Пакетная обработка с перерывами в управлении
Шаблон разрыва управления — это наиболее фундаментальный шаблон проектирования COBOL, который обрабатывает записи, сгруппированные по ключевому полю, и выдает промежуточные итоги.
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

### Шаблон 2: Шаблон редактирования/проверки
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

### Шаблон 3: поиск в таблице (массив в памяти)
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

## Производительность и оптимизация
### Оптимизация файлового ввода-вывода
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

### Оптимизация пакетной обработки
| Техника | Воздействие | Описание |
|-----------|--------|-------------|
| **Блокировать ввод-вывод** | Высокий | Используйте BLOCK CONTAINS для сокращения физических операций ввода-вывода |
| **Индексированный доступ** | Высокий | Используйте ИНДЕКСИРОВАННУЮ ОРГАНИЗАЦИЮ для поиска с произвольным доступом |
| **Сортировать/Объединить** | Средний | Используйте команду SORT для упорядочивания больших наборов данных |
| **Свернуть ОТОБРАЖЕНИЕ** | Средний | DISPLAY работает медленно в пакетном режиме; вместо этого записывайте в файлы |
| **КОМП/КОМП-3** | Средний | Двоичные/упакованные поля работают быстрее, чем числовые поля DISPLAY |
| **Настройка буфера** | Средний | Настройте размеры буфера для последовательной обработки файлов |
---

## Развертывание и использование в реальных условиях
### Развертывание мэйнфрейма (IBM z/OS)
Программы COBOL на мэйнфреймах развертываются как загрузочные модули в секционированных наборах данных (PDS). JCL управляет компиляцией, компоновкой и выполнением.
```
Deployment pipeline on z/OS:
  Source (PDS) → Compile (JCL) → Link Edit → Load Module (PDS) → Execute (JCL)
```

### Распределенное развертывание (GnuCOBOL)
```bash
# Build for Linux deployment
cobc -free -O2 -x src/payroll.cbl -o bin/payroll

# Deploy binary to target server
scp bin/payroll server:/opt/cobol/bin/

# Run as a cron job for batch processing
# 0 2 * * * /opt/cobol/bin/payroll --input /data/daily.dat
```

### Реальные отрасли, использующие COBOL
| Промышленность | Использование | Масштаб |
|----------|-------|-------|
| **Банковское дело** | Обработка транзакций, управление счетами | Обрабатывает ~85% транзакций через банкоматы |
| **Страхование** | Администрирование политик, обработка претензий | Крупнейшие страховщики используют серверную часть COBOL |
| **Правительство** | Социальное обеспечение, обработка налогов, льготы | Служба безопасности США обрабатывает миллиарды записей |
| **Здравоохранение** | Карты пациентов, биллинговые системы | Устаревшие больничные информационные системы |
| **Розничная торговля** | Управление запасами, серверная часть торговых точек | Крупные ритейлеры с устаревшими системами |
| **Телеком** | Биллинговые системы, обработка записей звонков | Обработка подробной записи звонков |
---

## Когда использовать COBOL
| Сценарий | Почему КОБОЛ | Лучшая альтернатива |
|----------|----------|-------------------|
| Обслуживание мейнфреймов | Существующая кодовая база | — |
| Пакетная финансовая обработка | Проверенная, надежная и точная десятичная математика | Java, Python для новых систем |
| Государственные устаревшие системы | Существующая кодовая база | — |
| Изучение истории вычислений | Понимание эволюции программирования | — |
| Новые бизнес-приложения | Не современный выбор | Java, C#, Python |
| Веб/мобильная разработка | Не подходит | JavaScript, Swift, Котлин |
| Наука о данных / ML | Не подходит | Питон, Р |
---

## Краткое содержание
COBOL — это пережиток первых дней компьютерной индустрии, который отказывается умирать, потому что не может себе этого позволить. Мировые банковские и правительственные системы зависят от программ COBOL, которые надежно работают на протяжении десятилетий. Хотя сегодня никто не выбрал бы COBOL для нового проекта, этот язык остается критически важным для поддержания инфраструктуры, лежащей в основе глобальных финансов. Нехватка разработчиков COBOL делает эту нишу удивительно прибыльной.