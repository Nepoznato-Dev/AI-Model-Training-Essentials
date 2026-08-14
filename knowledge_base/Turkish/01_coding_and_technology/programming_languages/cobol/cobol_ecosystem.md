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
# COBOL — Ekosistem ve Takımlama Kılavuzu
Bu kılavuz COBOL ekosistemindeki temel araçları, derleyicileri ve altyapıyı kapsar.
---

## Derleyiciler ve Uygulamalar
| Derleyici | Tür | Notlar |
|----------|------|----------|
| **GnuCOBOL (OpenCOBOL)** | Açık kaynak | En yaygın kullanılan ücretsiz derleyici |
| **IBM Kurumsal COBOL** | Ticari | z/OS ana bilgisayar standardı |
| **Mikro Odaklı COBOL** | Ticari | Kurumsal COBOL |
| **Fujitsu COBOL** | Ticari | Unix COBOL |
| **ACUCOBOL-GT** | Ticari | Şimdi Mikro Odaklanma |
| **COBOL-IT** | Ticari | GnuCOBOL tabanlı |
```bash
cobc --version              # GnuCOBOL version
cobc -x -o app program.cob  # compile to executable
cobc -m -o lib.so module.cob  # compile to shared library
cobc -free program.cob      # free-format source
```

---

## Sistem Oluştur
| Araç | Amaç |
|------|------------|
| **Yap** | Klasik yapılar |
| **GnuCOBOL derleyicisi** | Doğrudan derleme |
| **Maven (cobol eklentisi)** | Kurumsal yapılar |
| **JCL** | Ana bilgisayar iş kontrolü |
| **CMake** | Çapraz platform (COBOL desteğiyle) |
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

## Veritabanı ve İşlem Sistemleri
| Teknoloji | Amaç |
|---------------|-----------|
| **Db2** | IBM ana bilgisayar veritabanı |
| **VSAM** | Sanal depolama erişim yöntemi |
| **CICS** | İşlem işleme |
| **IMS** | Bilgi Yönetim Sistemi |
| **SQL** | Standart veritabanı erişimi |
| **GnuCOBOL + SQLite** | Gömülü veritabanı |
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

## Test etme
| Çerçeve | Amaç |
|-----------|------------|
| **CobolBirimi** | Birim testi (Mikro Odak) |
| **GnuCOBOL testi** | Temel testler |
| **z/OS test araçları** | IBM testleri |
| **Özel komut dosyaları** | Kabuk tabanlı testler |
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

## Kod Kalitesi
| Araç | Amaç |
|------|------------|
| **OpenCobolCE** | Kod analizi |
| **IBM Kod Analizi** | z/OS analizi |
| **SonarCOBOL** | SonarQube eklentisi |
| **Özel linterler** | Regex tabanlı kontroller |
---

## Modernizasyon Araçları
| Araç | Amaç |
|------|------------|
| **Mikro Odaklı Görsel COBOL** | Modern IDE |
| **GnuCOBOL** | Açık kaynak modernizasyonu |
| **AWS Blu Çağı** | Otomatik yeniden düzenleme |
| **IBM z/OS Uygulama Modernizasyonu** | Ana bilgisayar modernizasyonu |
| **AST COBOL** | Kod analizi |
| **OpenLegacy** | API etkinleştirme |
---

## Anahtar Kitaplıklar ve Desenler
| Desen | Amaç |
|-----------|-----------|
| **Kitapları KOPYALA** | Yeniden kullanılabilir kod parçacıkları |
| **ARAYIN** | Programdan programa aramalar |
| **KOPYALA** | Harici kodu ekle |
| **EXEC SQL** | Gömülü SQL |
| **EXEC CICS** | CICS işlem komutları |
| **SIRALA** | Dosya sıralama |
| **STRING/UNSTRING** | Dize manipülasyonu |
| **İNCELEME** | Dize incelemesi |
| **PERFORM** | Döngü/paragraf yürütme |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **Mikro Odaklı Görsel COBOL** | Kurumsal IDE |
| **VS Kodu + COBOL** | Modern düzenleme |
| **IBM Z Açık Editör** | z/OS geliştirme |
| **SPF/ISPF** | Ana bilgisayar düzenleyicisi |
| **GnuCOBOL + herhangi bir düzenleyici** | Açık kaynak |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **z/OS** | IBM ana bilgisayarı |
| **Mikro Odak Sunucusu** | Dağıtılmış COBOL |
| **GnuCOBOL** | Linux/Unix/Windows |
| **Docker** | Konteynerleştirilmiş (GnuCOBOL) |
| **CICS** | İşlem işleme |
| **Toplu** | Toplu işleme |
---

## Özet
COBOL'un ekosistemine ana bilgisayar ve kurumsal bilgi işlem hakimdir. Standart araç zinciri şudur: z/OS (ana bilgisayar) üzerinde **IBM Enterprise COBOL** veya **GnuCOBOL** (açık kaynak, çapraz platform), veriler için **Db2** ve **VSAM**, işlemler için **CICS** ve modernizasyon için **Micro Focus** araçları. COBOL dünyadaki ticari işlemlerin tahmini %70'ini gerçekleştirmektedir; bankacılık, sigorta, hükümet ve sağlık hizmetleri hala büyük ölçüde COBOL'a bağımlıdır. Ekosistem, eski sistemleri korumak ve ana bilgisayar uygulamalarını modernleştirmek için gereklidir. GnuCOBOL, COBOL geliştirme ve geçişi için ücretsiz, açık kaynaklı bir yol sağlar.