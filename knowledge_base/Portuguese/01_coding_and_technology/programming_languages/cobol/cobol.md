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

# COBOL
COBOL (Common Business-Oriented Language) é uma das linguagens de programação mais antigas ainda em uso, desenvolvida pela primeira vez em 1959. Ela foi projetada para processamento de dados comerciais – sistemas financeiros, folha de pagamento, bancos, seguros e aplicações governamentais. A sintaxe semelhante ao inglês do COBOL foi projetada para ser legível por gerentes de negócios, não apenas por programadores.
Apesar de sua idade, o COBOL processa cerca de 30% de todas as transações comerciais em todo o mundo. Os principais bancos, agências governamentais (incluindo a Administração da Segurança Social dos EUA) e companhias de seguros ainda dependem de sistemas mainframe COBOL. O susto do bug Y2K em 1999 trouxe o COBOL de volta à consciência pública, e a linguagem continua a operar infraestruturas críticas em todo o mundo.
---

## Por que o COBOL é importante
- **Infraestrutura crítica para os negócios**: processa diariamente trilhões de dólares em transações bancárias e governamentais.
- **Estabilidade**: os programas COBOL escritos na década de 1970 ainda são executados de maneira confiável hoje — são necessárias alterações mínimas.
- **Legibilidade**: a sintaxe semelhante ao inglês torna a lógica de negócios compreensível para não programadores.
- **Aritmética decimal**: suporte nativo para cálculos financeiros precisos (sem erros de arredondamento de ponto flutuante).
- **Processamento em lote**: projetado para processar grandes volumes de registros com eficiência.
- **Mercado de trabalho**: A grave escassez de desenvolvedores COBOL cria alta demanda (e altos salários) para funções de manutenção.
## As compensações
| Limitação | Detalhes | Solução alternativa típica |
|-------|---------|-------------------|
| **Sintaxe detalhada** | Requer muitas linhas para operações simples | Aceitar como parte do design da linguagem |
| **Não é moderno** | Sem classes, sem programação funcional, abstrações limitadas | Uso para manutenção; construir novos sistemas em linguagens modernas |
| **Dependência de mainframe** | Normalmente roda em mainframes IBM (caro) | Use compiladores COBOL em sistemas distribuídos (GnuCOBOL) |
| **Força de trabalho em declínio** | Menos desenvolvedores COBOL entrando no campo | Alta demanda por quem conhece; bom nicho de carreira |
| **Sem web/dispositivo móvel** | Não é possível construir aplicativos modernos | Use para processamento em lote de back-end; front-ends modernos |
---

## Fundamentos de sintaxe
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

### Exemplo de processamento de arquivo
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

## Sintaxe e padrões avançados
### Aprofundamento da Divisão de Dados
A divisão de dados do COBOL é a característica mais distintiva da linguagem. Ele usa um sistema de numeração hierárquica (níveis 01 a 88) para definir estruturas de dados.
| Nível | Finalidade | Exemplo |
|-------|---------|-----|
| **01** | Item ao nível do registo (variável ou registo de nível superior) | `01 WS-EMPLOYEE.`|
| **02–49** | Itens agrupados ou elementares (subcampos) | `05 EMP-NAME PIC X(30).`|
| **66** | Cláusula de renomeação (visão alternativa dos dados) | `66 EMP-FULL-NAME RENAMES EMP-FIRST.`|
| **77** | Item elementar independente (sem subitens) | `77 WS-COUNTER PIC 9(5).`|
| **88** | Nomes de condições (sinalizadores do tipo booleano) | `88 WS-IS-SENIOR VALUE 'Y'.`|
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

### A declaração COPY (Copybooks)
Copybooks são o mecanismo COBOL para reutilização de código - semelhante a`#include`em C. Eles são armazenados como membros separados e inseridos em tempo de compilação.
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

### PERFORM Variações
COBOL fornece vários tipos de instrução PERFORM para programação estruturada.
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

### Manuseio e inspeção de strings
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

## Arquitetura e Design de Sistema
### As Quatro Divisões
Cada programa COBOL é estruturado em quatro divisões, cada uma servindo a um propósito distinto:
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

### Hierarquia do Programa
Os sistemas COBOL normalmente usam uma hierarquia de chamada com um programa principal que chama subprogramas.
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

### Estrutura típica de diretório de projeto
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

## Configuração do projeto e sistema de construção
### GnuCOBOL (compilador COBOL de código aberto)
GnuCOBOL (anteriormente OpenCOBOL) compila COBOL em C e depois em código de máquina nativo, permitindo que o COBOL seja executado em Linux, Windows e macOS.
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

### IBM Mainframe JCL (linguagem de controle de trabalho)
Nos mainframes IBM, os programas COBOL são compilados e executados usando JCL.
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

### Referência de opções do compilador
| Opção | Descrição | Exemplo |
|--------|-------------|---------|
| `-free`| Fonte em formato livre (sem restrições de coluna) | `cobc -free prog.cbl`|
| `-fixed`| Formato fixo (colunas tradicionais 1-80) | `cobc -fixed prog.cbl`|
| `-O2`| Nível de otimização 2 | `cobc -O2 prog.cbl`|
| `-g`| Gerar informações de depuração | `cobc -g prog.cbl`|
| `-std=cobol2014`| Usar o padrão COBOL 2014 | `cobc -std=cobol2014 prog.cbl`|
| `-x`| Construir executável (não apenas compilar) | `cobc -x prog.cbl`|
| `-I`| Caminho de pesquisa do caderno | `cobc -I ./copybooks prog.cbl`|
| `-Wall`| Habilite todos os avisos | `cobc -Wall prog.cbl`|
---

## Teste e depuração
### Técnicas de depurador COBOL
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

### Depuração GnuCOBOL com gdb
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

### Padrões comuns de depuração
| Problema | Sintoma | Solução |
|--------|---------|----------|
| Dados truncados | Campos cortados | Verifique se os tamanhos das cláusulas PIC correspondem ao layout do registro |
| Estouro numérico | Cálculos errados | Verifique se o PIC 9(n) possui dígitos suficientes |
| Erros de status de arquivo | WS-FILE-STATUS não é '00' | Verifique nomes, caminhos e permissões de DD de arquivo |
| Laço infinito | PERFORM ATÉ nunca termina | Verifique se a variável do loop foi modificada dentro do loop |
| Falhas de CHAMADA | RETORNANDO diferente de zero | Verifique se LINKAGE SECTION corresponde ao programa de chamada |
---

## Interoperabilidade
### Instrução CALL — Chamando Subprogramas
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

### Interoperabilidade C (GnuCOBOL)
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

### Conectividade de banco de dados (DB2/COBOL)
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

## Padrões de Projeto
### Padrão 1: Processamento em lote com quebras de controle
O padrão de quebra de controle é o padrão de design COBOL mais fundamental – processando registros agrupados por um campo-chave e produzindo subtotais.
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

### Padrão 2: Padrão de edição/validação
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

### Padrão 3: Pesquisa de tabela (matriz na memória)
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

## Desempenho e otimização
### Otimização de E/S de arquivos
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

### Otimização de processamento em lote
| Técnica | Impacto | Descrição |
|-----------|--------|-------------|
| **Bloquear E/S** | Alto | Use BLOCK CONTAINS para reduzir operações físicas de E/S |
| **Acesso indexado** | Alto | Use INDEXED ORGANIZATION para pesquisas de acesso aleatório |
| **Classificar/Mesclar** | Médio | Use o verbo SORT para ordenação de grandes conjuntos de dados |
| **Minimizar EXIBIÇÃO** | Médio | DISPLAY é lento em lote; escreva em arquivos |
| **COMP/COMP-3** | Médio | Campos binários/compactados são mais rápidos que DISPLAY numérico |
| **Ajuste de buffer** | Médio | Ajustar tamanhos de buffer para processamento sequencial de arquivos |
---

## Implantação e uso no mundo real
### Implantação de mainframe (IBM z/OS)
Os programas COBOL em mainframes são implementados como módulos de carregamento em conjuntos de dados particionados (PDS). JCL controla compilação, vinculação e execução.
```
Deployment pipeline on z/OS:
  Source (PDS) → Compile (JCL) → Link Edit → Load Module (PDS) → Execute (JCL)
```

### Implantação Distribuída (GnuCOBOL)
```bash
# Build for Linux deployment
cobc -free -O2 -x src/payroll.cbl -o bin/payroll

# Deploy binary to target server
scp bin/payroll server:/opt/cobol/bin/

# Run as a cron job for batch processing
# 0 2 * * * /opt/cobol/bin/payroll --input /data/daily.dat
```

### Indústrias do mundo real usando COBOL
| Indústria | Uso | Escala |
|----------|-------|-------|
| **Banco** | Processamento de transações, gerenciamento de contas | Processa aproximadamente 85% das transações em caixas eletrônicos |
| **Seguros** | Administração de apólices, processamento de sinistros | Grandes seguradoras executam backends COBOL |
| **Governo** | Segurança Social, processamento fiscal, benefícios | SSA dos EUA processa bilhões de registros |
| **Saúde** | Registros de pacientes, sistemas de faturamento | Sistemas de informação hospitalar legados |
| **Varejo** | Gestão de estoques, backends de ponto de venda | Grandes varejistas com sistemas legados |
| **Telecomunicações** | Sistemas de facturação, processamento de registos de chamadas | Processamento de registro de detalhes de chamadas |
---

## Quando usar COBOL
| Cenário | Por que COBOL | Melhor Alternativa |
|----------|----------|-------------------|
| Manutenção de mainframes | Base de código existente | — |
| Processamento financeiro em lote | Matemática decimal comprovada, confiável e precisa | Java, Python para novos sistemas |
| Sistemas legados governamentais | Base de código existente | — |
| Aprendendo a história da computação | Compreendendo a evolução da programação | — |
| Novas aplicações de negócios | Não é a escolha moderna | Java, C#, Python |
| Desenvolvimento web/móvel | Não adequado | JavaScript, Swift, Kotlin |
| Ciência de dados / ML | Não adequado | Pitão, R |
---

## Resumo
COBOL é uma relíquia dos primórdios da computação que se recusa a morrer — porque não tem condições de fazê-lo. Os sistemas bancários e governamentais do mundo dependem de programas COBOL que funcionam de forma confiável há décadas. Embora hoje ninguém escolha COBOL para um novo projeto, a linguagem continua extremamente importante para manter a infraestrutura que sustenta as finanças globais. A escassez de desenvolvedores COBOL torna esse nicho surpreendentemente lucrativo.