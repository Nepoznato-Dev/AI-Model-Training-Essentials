<!--
---
# Metadata
title: "Go — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Go ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [go, golang, ecosystem, tooling, testing, web, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "20 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Go - คู่มือระบบนิเวศและเครื่องมือ
คู่มือนี้ครอบคลุมถึงเครื่องมือ เฟรมเวิร์ก และโครงสร้างพื้นฐานที่จำเป็นในระบบนิเวศ Go
---

## Toolchain (ในตัว)
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **ไปสร้าง** | คอมไพล์แพ็คเกจและการขึ้นต่อกัน |
| **ไปทดสอบ** | รันการทดสอบ |
| **ไปหาสัตว์แพทย์** | การวิเคราะห์แบบคงที่ |
| **ไป fmt** | การจัดรูปแบบโค้ด |
| **ไปดัดแปลง** | การจัดการโมดูล |
| **ไปหมอ** | โปรแกรมดูเอกสาร |
| **ไปสร้าง** | การสร้างโค้ด |
| **ไปติดตั้ง** | คอมไพล์และติดตั้ง |
| **ไปวิ่ง** | คอมไพล์และรัน |
```bash
go mod init example.com/project  # initialize module
go get github.com/pkg/errors     # add dependency
go mod tidy                      # clean up dependencies
go build -o app ./cmd/app       # build binary
go test ./...                    # run all tests
go test -race ./...              # with race detector
go test -cover ./...             # with coverage
go vet ./...                     # static analysis
```

---

## เครื่องมือของบุคคลที่สาม
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **โกลังซี-ลินต์** | ตัวรวบรวมหลาย linter |
| **gofumpt** | ตัวจัดรูปแบบที่เข้มงวดยิ่งขึ้น |
| **การตรวจสอบคงที่** | การวิเคราะห์คงที่ขั้นสูง |
| **อากาศ** | โหลดซ้ำสดเพื่อการพัฒนา |
| **gomock / mockgen** | กรอบการเยาะเย้ย |
| **พวงหรีด** | เครื่องมือสร้างเอกสาร Swagger |
| **บัฟ** | เครื่องมือบัฟเฟอร์โปรโตคอล |
---

## กรอบงานเว็บ
| กรอบ | พิมพ์ | ดีที่สุดสำหรับ |
|----------|-|----------|
| **สุทธิ/http** | ไลบรารีมาตรฐาน | API แบบง่าย ไม่มีการพึ่งพา |
| **จิน** | ประสิทธิภาพ | HTTP ที่รวดเร็ว มิดเดิลแวร์ |
| **เอคโค่** | น้อยที่สุด | การออกแบบ API ที่สะอาดตา |
| **ไฟเบอร์** | ด่วนเหมือน | คุ้นเคยกับ Node.js devs |
| **ชิ** | เราเตอร์ | น้ำหนักเบา รองรับ stdlib |
| **ฮูมา** | OpenAPI | การออกแบบที่เน้น API เป็นหลัก |
---

## gRPC และ API
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **google.golang.org/grpc** | กรอบงาน gRPC |
| **เชื่อมต่อไป** | gRPC-เว็บ, gRPC, REST |
| **protoc-gen-go** | การสร้างโค้ด Protobuf |
| **grpc-เกตเวย์** | REST ไปยังพร็อกซี gRPC |
---

## ฐานข้อมูล
| แพ็คเกจ | ฐานข้อมูล |
|---------|----------|
| **ฐานข้อมูล/sql** | อินเตอร์เฟส SQL มาตรฐาน |
| **pgx** | ไดรเวอร์ PostgreSQL (เร็ว) |
| **กอร์ม** | ORM เต็ม |
| **sqlc** | สร้างประเภทที่ปลอดภัย Go จาก SQL |
| **เข้า** | กรอบงานเอนทิตี (Facebook) |
| **go-redis** | ลูกค้า Redis |
| **คนขับมองโกโก** | ไคลเอนต์ MongoDB |
---

## การทดสอบ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **ทดสอบ** | กรอบการทดสอบในตัว |
| **เป็นพยาน** | การยืนยันและการเยาะเย้ย |
| **go-cmp** | การเปรียบเทียบเชิงลึก |
| **httptest** | ยูทิลิตี้การทดสอบ HTTP |
| **ไป-ฝอย / คลุมเครือ** | การทดสอบฟัซซี |
| **เกณฑ์มาตรฐาน** | การเปรียบเทียบเกณฑ์มาตรฐาน |
```go
func TestAdd(t *testing.T) {
    got := Add(2, 3)
    if got != 5 {
        t.Errorf("Add(2, 3) = %d, want 5", got)
    }
}

// Table-driven tests
func TestAdd(t *testing.T) {
    tests := []struct{
        name string
        a, b, want int
    }{
        {"positive", 2, 3, 5},
        {"zero", 0, 0, 0},
        {"negative", -1, 1, 0},
    }
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got := Add(tt.a, tt.b)
            if got != tt.want {
                t.Errorf("got %d, want %d", got, tt.want)
            }
        })
    }
}
```

---

## เครื่องมือ CLI
| แพ็คเกจ | วัตถุประสงค์ |
|---------|---------|
| **งูเห่า** | กรอบงาน CLI (kubectl ใช้สิ่งนี้) |
| **urfave/cli** | ตัวสร้าง CLI อย่างง่าย |
| **ชานมไข่มุก** | Terminal UI (เสน่ห์) |
| **ลิปกลอส** | สไตล์เทอร์มินัล |
---

## IDE และบรรณาธิการ
| ไอดี | จุดแข็ง |
|-----|-----------|
| **VS Code + gopls** | Go LSP อย่างเป็นทางการ |
| **โกแลนด์** | JetBrains Go IDE เต็มรูปแบบ |
| **นีโอวิม + โกพลัส** | บนเทอร์มินัล |
---

## การปรับใช้
| วิธีการ | หมายเหตุ |
|--------|--------|
| **ไบนารีแบบคงที่** | `CGO_ENABLED=0 go build`|
| **ข้ามคอมไพล์** | `GOOS=linux GOARCH=amd64 go build`|
| **นักเทียบท่า** | การสร้างแบบหลายขั้นตอน ไร้ distroless |
| **ตู้คอนเทนเนอร์** | ภาพขนาดจิ๋ว (~10MB) |
---

## สรุป
ระบบนิเวศของ Go นั้นใช้งานได้จริงและน้อยที่สุด ไลบรารีมาตรฐานครอบคลุม HTTP, JSON, การทดสอบ และอื่นๆ ซึ่งมักจะขจัดความจำเป็นในการใช้เฟรมเวิร์ก สแต็กสมัยใหม่คือ: **go modules** สำหรับการขึ้นต่อกัน, **golangci-lint** สำหรับ linting, **Gin** หรือ **Chi** สำหรับเว็บ, **pgx** หรือ **sqlc** สำหรับฐานข้อมูล, **cobra** สำหรับ CLIs และ **static binaries** สำหรับการปรับใช้ จุดแข็งของ Go คือความเรียบง่าย: การคอมไพล์ที่รวดเร็ว ไบนารีขนาดเล็ก และโมเดลการปรับใช้ไบนารีเดี่ยว