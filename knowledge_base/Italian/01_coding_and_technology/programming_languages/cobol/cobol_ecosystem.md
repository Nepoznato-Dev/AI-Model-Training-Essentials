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
# COBOL: Guida all'ecosistema e agli strumenti
Questa guida copre gli strumenti, i compilatori e l'infrastruttura essenziali nell'ecosistema COBOL.
---

## Compilatori e implementazioni
| Compilatore | Digitare | Note |
|----------|------|-------|
| **GnuCOBOL (OpenCOBOL)** | Open source | Compilatore gratuito più utilizzato |
| **IBM Enterprise COBOL** | Commerciale | Standard mainframe z/OS |
| **Microfuoco COBOL** | Commerciale | Impresa COBOL |
| **Fujitsu COBOL** | Commerciale | Unix COBOL |
| **ACUCOBOL-GT** | Commerciale | Ora Micro Focus |
| **COBOL-IT** | Commerciale | Basato su GnuCOBOL |
```bash
cobc --version              # GnuCOBOL version
cobc -x -o app program.cob  # compile to executable
cobc -m -o lib.so module.cob  # compile to shared library
cobc -free program.cob      # free-format source
```

---

## Costruisci sistemi
| Strumento | Scopo |
|------|---------|
| **Fai** | Costruzioni classiche |
| **Compilatore GnuCOBOL** | Compilazione diretta |
| **Maven (plugin Cobol)** | L'impresa costruisce |
| **JCL** | Controllo del lavoro del mainframe |
| **CMake** | Multipiattaforma (con supporto COBOL) |
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

## Database e sistemi di transazione
| Tecnologia | Scopo |
|------------|---------|
| **Db2** | Database mainframe IBM |
| **VSAM** | Metodo di accesso all'archiviazione virtuale |
| **CICS** | Elaborazione delle transazioni |
| **IMS** | Sistema di gestione delle informazioni |
| **SQL** | Accesso al database standard |
| **GnuCOBOL + SQLite** | Database incorporato |
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

## Test
| Quadro | Scopo |
|-----------|---------|
| **CobolUnit** | Test unitari (Micro Focus) |
| **Test GnuCOBOL** | Test di base |
| **Strumenti di test z/OS** | Test IBM |
| **Script personalizzati** | Test basati su shell |
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

## Qualità del codice
| Strumento | Scopo |
|------|---------|
| **OpenCobolCE** | Analisi del codice |
| **Analisi del codice IBM** | Analisi z/OS |
| **SonarCOBOL** | Plug-in SonarQube |
| **Linter personalizzati** | Controlli basati su Regex |
---

## Strumenti di modernizzazione
| Strumento | Scopo |
|------|---------|
| **Micro Focus visivo COBOL** | IDE moderno |
| **GnuCOBOL** | Modernizzazione open source |
| **AWS Blu Età** | Refactoring automatizzato |
| **Modernizzazione delle applicazioni IBM z/OS** | Modernizzazione del mainframe |
| **AST COBOL** | Analisi del codice |
| **OpenLegacy** | Abilitazione API |
---

## Librerie e modelli chiave
| Modello | Scopo |
|---------|---------|
| **COPIA libri** | Frammenti di codice riutilizzabili |
| **CHIAMA** | Chiamate da programma a programma |
| **COPIA** | Includi codice esterno |
| **EXECSQL** | SQL incorporato |
| **EXEC CICS** | Comandi di transazione CICS |
| **ORDINA** | Ordinamento dei file |
| **STRINGA/UNSTRING** | Manipolazione delle stringhe |
| **ISPEZIONARE** | Esame della stringa |
| **ESEGUIRE** | Esecuzione di loop/paragrafi |
---

## IDE ed editor
| IDE | Punti di forza |
|-----|-----------|
| **Micro Focus visivo COBOL** | IDE aziendale |
| **Codice VS + COBOL** | Modifica moderna |
| **Editor IBM Z Open** | Sviluppo z/OS |
| **SPF/ISPF** | Editor del mainframe |
| **GnuCOBOL + qualsiasi editor** | Open source |
---

## Distribuzione
| Metodo | Note |
|--------|-------|
| **z/OS** | Mainframe IBM |
| **Server Micro Focus** | COBOL distribuito |
| **GnuCOBOL** | Linux/Unix/Windows |
| **Docker** | Containerizzato (GnuCOBOL) |
| **CICS** | Elaborazione delle transazioni |
| **Lotto** | Elaborazione batch |
---

## Riepilogo
L'ecosistema COBOL è dominato dal mainframe e dall'informatica aziendale. La toolchain standard è: **IBM Enterprise COBOL** su z/OS (mainframe) o **GnuCOBOL** (open source, multipiattaforma), **Db2** e **VSAM** per i dati, **CICS** per le transazioni e strumenti **Micro Focus** per la modernizzazione. COBOL elabora circa il 70% delle transazioni commerciali mondiali: banche, assicurazioni, governo e sanità fanno ancora molto affidamento su COBOL. L'ecosistema è essenziale per mantenere i sistemi legacy e modernizzare le applicazioni mainframe. GnuCOBOL fornisce un percorso open source gratuito per lo sviluppo e la migrazione di COBOL.