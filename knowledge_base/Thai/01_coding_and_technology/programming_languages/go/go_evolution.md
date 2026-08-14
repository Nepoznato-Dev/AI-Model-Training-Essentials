<!--
---
# Metadata
title: "Go — Version History & Evolution"
description: "Comprehensive version history and evolution of Go from 1.0 to modern Go."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [go, golang, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Go - ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | วันที่วางจำหน่าย | ธีมหลัก |
|---------|-------------|-----------|
| 1.0 | มี.ค. 2555 | การเปิดตัวที่เสถียรครั้งแรก |
| 1.1 | พฤษภาคม 2556 | ประสิทธิภาพเครื่องตรวจจับการแข่งขัน |
| 1.3 | มิ.ย. 2557 | การโพลเครือข่าย, crypto/tls |
| 1.4 | ธ.ค. 2557 | Bootstrap with Go (โฮสต์เอง) |
| 1.5 | ส.ค. 2558 | **GC พร้อมกัน** เขียนอุปสรรค |
| 1.7 | ส.ค. 2559 |  แพ็คเกจ`context`การทดสอบย่อย `testing`
| 1.8 | ก.พ. 2560 | `http.Server.Shutdown`, ปลั๊กอิน |
| 1.9 | ส.ค. 2560 | พิมพ์นามแฝง ขนาน`make`|
| 1.10 | ก.พ. 2561 |  พูลการเชื่อมต่อ`database/sql`|
| 1.11 | ส.ค. 2561 | **ไปที่โมดูล**,`go mod`|
| 1.12 | ก.พ. 2562 | TLS 1.3 การกำหนดเวอร์ชันโมดูล |
| 1.13 | ก.ย. 2562 | `errors.Is/As`, ตัวอักษรตัวเลข`0b`,`0o`|
| 1.14 | ก.พ. 2563 | **I/O ที่ทับซ้อนกันบน Windows** การจองรูทีน |
| 1.15 | ส.ค. 2563 | `time.Ticker`/`Timer`รีเซ็ต, พร็อกซีโมดูล |
| 1.16 | ก.พ. 2564 |  แพ็คเกจ `embed`,`io/fs`, รับรู้โมดูลโดยค่าเริ่มต้น |
| 1.17 | ส.ค. 2564 | การแปลงแบบแบ่งส่วนเป็นอาร์เรย์`unsafe.Slice`|
| 1.18 | มี.ค. 2565 | **ทั่วไป**, fuzzing, พื้นที่ทำงาน |
| 1.19 | ส.ค. 2565 | ความคิดเห็นของหมอ การแก้ไขโมเดลหน่วยความจำ |
| 1.20 | ก.พ. 2566 | `errors.Join`การเพิ่มประสิทธิภาพตามโปรไฟล์ |
| 1.21 | ส.ค. 2566 | **`slog`**,`min/max`บิวด์อิน,`maps/slices`|
| 1.22 | ก.พ. 2567 | ช่วงเหนือจำนวนเต็ม การกำหนดเส้นทางที่ปรับปรุง |
| 1.23 | ส.ค. 2567 | แพ็คเกจ Iterator (`iter`) การเปลี่ยนแปลงตัวจับเวลา |
| 1.24 | ก.พ. 2568 |  แพ็คเกจ`weak`แผนที่ที่ปรับปรุงแล้ว |
## เหตุการณ์สำคัญที่สำคัญ
### จุดเริ่มต้น (2552–2555)
- **2009**: Go ประกาศโดย Google (Robert Griesemer, Rob Pike, Ken Thompson)
- **2012**: **Go 1.0** — "สัญญาความเข้ากันได้ของ Go 1"
### ประสิทธิภาพและเครื่องมือ (2012–2018)
- **1.1**: ปรับปรุงประสิทธิภาพ 30%+; เครื่องตรวจจับการแข่งขัน
- **1.5**: ตัวรวบรวมขยะพร้อมกัน (GC หยุดชั่วคราวลดลงจากมิลลิวินาทีเป็นไมโครวินาที)
- **1.5**: Go คอมไพเลอร์บูตสแตรป — เขียนด้วยภาษา Go (ไม่มี C อีกต่อไป)
- **1.7**: แพ็คเกจ`context`กลายเป็นแพ็คเกจมาตรฐาน
### โมดูลและระบบนิเวศ (2018–2021)
- **1.11**: **Go modules** — การจัดการการพึ่งพาอย่างเป็นทางการ
- **1.13**:`errors.Is/As`— การตัดข้อผิดพลาดกลายเป็นสำนวน
- **1.16**: แพ็คเกจ`embed`— ฝังไฟล์ ณ เวลาคอมไพล์
### โมเดิร์นโก (2565–ปัจจุบัน)
- **1.18**: **ทั่วไป** — พิมพ์พารามิเตอร์ที่มีข้อจำกัด
- **1.21**:`slog`— การบันทึกแบบมีโครงสร้างใน stdlib; `min/max`บิวด์อิน
- **1.22**: ช่วงจำนวนเต็ม (`for i := range 10`)
- **1.23**: แพ็คเกจ Iterator — การประเมินแบบ Lazy ใน stdlib
## การเดินทางทั่วไป
```
2010: "Go doesn't need generics" (early stance)
2016: Go generics proposal discussions begin
2018: Type parameters design draft published
2020: Go 2 generics proposal (draft designs)
2022: Go 1.18 — generics land! Type parameters, constraints
2023: Generic code patterns emerge (slices, maps packages)
2024: Community adapts — generic data structures, algorithms
```

## ปรัชญาการจัดการข้อผิดพลาด
```
1.0:     Explicit error returns — "errors are values"
1.13:    Error wrapping with %w — "inspect and unwrap"
1.20:    errors.Join — multiple errors
Future:  go2 proposal for try/handle (not yet adopted)
```

## วิวัฒนาการพร้อมกัน
```
1.0:  Goroutines + channels — CSP-inspired
1.1:  Race detector
1.4:  Non-blocking syscalls (net poller)
1.5:  Concurrent GC
1.7:  context package for cancellation
1.14: Cooperative goroutine preemption (signals)
1.21: Synchronization improvements
1.23: iter package — iterator pattern
```

## Go สัญญาความเข้ากันได้
```
Go 1.0 (2012): "Go 1 will be available for a long time.
  Compatibility is important. Programs that work at Go 1
  will continue to work at every subsequent Go 1 release."

This means:
- No breaking changes to the language spec
- No breaking changes to the standard library
- Only additive changes
- Forward compatibility guaranteed
```

## การเติบโตของระบบนิเวศ
```
2012: Go 1.0 — basic stdlib, no package manager
2014: dep (early dependency management experiments)
2018: Go modules — official solution
2019: Go used by Uber, Twitch, Dropbox, Cloudflare
2022: Generics — opens new library design patterns
2023: Go in Kubernetes, Docker, Terraform, Hugo
2025: Top 10 most used language; cloud-native standard
```

## วิวัฒนาการด้านประสิทธิภาพ
```
Go 1.0:  Baseline
Go 1.1:  ~30% faster (register-based calling prep)
Go 1.5:  Concurrent GC (pause time: ms → μs)
Go 1.7:  SSA backend (15-30% faster)
Go 1.11: PGO experiments
Go 1.13: Faster map operations
Go 1.18: Generics (initial overhead, optimized in 1.19+)
Go 1.20: Profile-guided optimization
Go 1.22: Faster crypto, improved compiler
```
