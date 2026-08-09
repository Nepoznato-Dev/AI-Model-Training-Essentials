---
# Metadata
title: "Go"
description: "Comprehensive reference for the Go programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
tags: [go, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# ไป
Go (มักเรียกว่า "Golang" ตามชื่อโดเมนเดิม) เป็นภาษาโปรแกรมคอมไพล์ที่พิมพ์คงที่ ออกแบบโดย Google โดย Robert Griesemer, Rob Pike และ Ken Thompson เปิดตัวครั้งแรกในปี 2555 โดยมีเป้าหมายที่ชัดเจนในการเป็นภาษาที่ดีกว่าสำหรับการเขียนโปรแกรมระบบ ซึ่งเป็นการผสมผสานประสิทธิภาพของภาษา C เข้ากับประสิทธิภาพของภาษาไดนามิกเช่น Python Go ขึ้นชื่อเรื่องความเรียบง่าย การคอมไพล์ที่รวดเร็ว การทำงานพร้อมกันในตัว (กอร์รูทีนและแชนเนล) และเครื่องมือที่ยอดเยี่ยม
Go ขับเคลื่อนระบบนิเวศโครงสร้างพื้นฐานคลาวด์ส่วนใหญ่: Docker, Kubernetes, Terraform, Prometheus ฯลฯ และเซิร์ฟเวอร์ HTTP ของไลบรารีมาตรฐาน Go ล้วนเขียนด้วยภาษา Go โดยได้กลายเป็นภาษาเริ่มต้นสำหรับการพัฒนาบนคลาวด์ ไมโครเซอร์วิส และเครื่องมือ CLI
---

## ทำไมต้องไปเรื่อง
- **เรียบง่ายด้วยการออกแบบ**: Go มีคำหลักเพียง 25 คำเท่านั้น ภาษามีขนาดเล็กและง่ายต่อการเรียนรู้
- **การคอมไพล์อย่างรวดเร็ว**: คอมไพล์โดยตรงไปยังรหัสเครื่องภายในไม่กี่วินาที แม้สำหรับโปรเจ็กต์ขนาดใหญ่
- **การทำงานพร้อมกันในตัว**: Goroutines และช่องสัญญาณทำให้การเขียนโปรแกรมพร้อมกันสามารถเข้าถึงได้และมีประสิทธิภาพ
- **ไลบรารี่มาตรฐานที่ยอดเยี่ยม**: เซิร์ฟเวอร์ HTTP, การเข้ารหัส JSON, การทดสอบ, การเข้ารหัส -- ทั้งหมดนี้รวมอยู่ในตัว
- **ไบนารีแบบคงที่**: คอมไพล์เป็นไบนารีเดียวโดยไม่มีการอ้างอิงภายนอก การปรับใช้เป็นเรื่องเล็กน้อย
- **สายเลือดระดับ Google**: ออกแบบโดยวิศวกรที่สร้าง Unix, UTF-8 และโครงสร้างพื้นฐานส่วนใหญ่ของ Google
## การแลกเปลี่ยน
| ข้อจำกัด | รายละเอียด | วิธีแก้ปัญหาทั่วไป |
|----------|---------|-------------------|
| **ไม่มีประเภทผลรวม/การจับคู่รูปแบบ** | ไม่มีการแจงนับที่มีข้อมูลที่เกี่ยวข้อง ไม่มีประเภทพีชคณิต | ใช้อินเทอร์เฟซและสวิตช์ประเภท |
| **เกิดข้อผิดพลาดในการจัดการคำฟุ่มเฟือย** | ชัดเจนถ้าผิดพลาด != ไม่มีการตรวจสอบทุกที่ | ยอมรับรูปแบบ; มันทำให้มองเห็นการจัดการข้อผิดพลาด |
| **ระบบนิเวศเล็กลง** | ไลบรารีน้อยกว่า Python, Java หรือ JavaScript | ไลบรารีมาตรฐานครอบคลุมความต้องการส่วนใหญ่ แพ็คเกจชุมชนที่กำลังเติบโต |
| **ไม่มีกรอบ GUI** | ไม่เหมาะกับ UI ของเดสก์ท็อปหรืออุปกรณ์เคลื่อนที่ | ใช้ UI บนเว็บ (WASM) หรือภาษาอื่น |
| **คนเก็บขยะ** | มี GC -- การหยุดชั่วคราวมีขนาดเล็กแต่ไม่เป็นศูนย์ | ปรับแต่ง GC สำหรับปริมาณงานที่ไวต่อความหน่วง ใช้ sync.Pool |
---

## พื้นฐานไวยากรณ์
### โครงสร้างพื้นฐาน
```go
package main

import (
    "fmt"
    "strings"
)

func main() {
    name := "World"
    fmt.Printf("Hello, %s!\n", name)

    age := 30
    score := 9.5
    active := true
    message := "Hello"

    upper := strings.ToUpper(message)
    fmt.Println(upper)
}
```

### ฟังก์ชั่น
```go
// Multiple return values
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, fmt.Errorf("division by zero")
    }
    return a / b, nil
}

result, err := divide(10, 3)
if err != nil {
    fmt.Println("Error:", err)
    return
}

// Named return values
func split(sum int) (x, y int) {
    x = sum * 4 / 9
    y = sum - x
    return
}

// Variadic functions
func sum(nums ...int) int {
    total := 0
    for _, n := range nums {
        total += n
    }
    return total
}
```

### โครงสร้างและอินเทอร์เฟซ
```go
type Animal struct {
    Name string
    Age  int
}

func (a Animal) Speak() string {
    return a.Name + " makes a sound"
}

// Embedding (composition, not inheritance)
type Dog struct {
    Animal
    Breed string
}

func (d Dog) Speak() string {
    return d.Name + " says woof"
}

// Interface -- implicitly satisfied
type Speaker interface {
    Speak() string
}

func announce(s Speaker) {
    fmt.Println(s.Speak())
}

dog := Dog{Animal: Animal{Name: "Rex"}, Breed: "Labrador"}
announce(dog)
```

### การจัดการข้อผิดพลาด
```go
type InsufficientFundsError struct {
    Balance float64
    Amount  float64
}

func (e *InsufficientFundsError) Error() string {
    return fmt.Sprintf("cannot withdraw $%.2f from $%.2f", e.Amount, e.Balance)
}

func withdraw(balance, amount float64) (float64, error) {
    if amount > balance {
        return balance, &InsufficientFundsError{Balance: balance, Amount: amount}
    }
    return balance - amount, nil
}

newBalance, err := withdraw(100, 150)
if err != nil {
    var fundsErr *InsufficientFundsError
    if errors.As(err, &fundsErr) {
        fmt.Printf("Need $%.2f more\n", fundsErr.Amount-fundsErr.Balance)
    }
}
```

### การทำงานพร้อมกัน -- รูทีนและช่องทาง
```go
// Goroutine
go func() {
    fmt.Println("Running concurrently")
}()

// Channels
func producer(ch chan<- int) {
    for i := 0; i < 5; i++ { ch <- i }
    close(ch)
}

func consumer(ch <-chan int) {
    for value := range ch {
        fmt.Println("Received:", value)
    }
}

ch := make(chan int)
go producer(ch)
consumer(ch)

// WaitGroup
var wg sync.WaitGroup
for i := 0; i < 5; i++ {
    wg.Add(1)
    go func(id int) {
        defer wg.Done()
        fmt.Printf("Worker %d done\n", id)
    }(i)
}
wg.Wait()
```

---

## ไวยากรณ์และรูปแบบขั้นสูง
### ทั่วไป (ไป 1.18+)
```go
// Generic function
func Map[T any, U any](s []T, f func(T) U) []U {
    result := make([]U, len(s))
    for i, v := range s {
        result[i] = f(v)
    }
    return result
}

// Type constraints
type Number interface {
    ~int | ~float64 | ~float32
}

func Sum[T Number](nums []T) T {
    var total T
    for _, n := range nums {
        total += n
    }
    return total
}

// Generic struct
type Set[T comparable] struct {
    items map[T]struct{}
}

func NewSet[T comparable]() *Set[T] {
    return &Set[T]{items: make(map[T]struct{})}
}

func (s *Set[T]) Add(item T)  { s.items[item] = struct{}{} }
func (s *Set[T]) Has(item T) bool {
    _, ok := s.items[item]
    return ok
}
```

### การจับคู่รูปแบบขั้นสูง (สวิตช์ประเภท)
```go
func describe(i interface{}) string {
    switch v := i.(type) {
    case int:
        return fmt.Sprintf("Integer: %d", v)
    case string:
        return fmt.Sprintf("String: %q", v)
    case bool:
        return fmt.Sprintf("Bool: %t", v)
    case []int:
        return fmt.Sprintf("Int slice of length %d", len(v))
    default:
        return fmt.Sprintf("Unknown type: %T", v)
    }
}

// Comma-ok idiom
var i interface{} = "hello"
s, ok := i.(string)
if ok {
    fmt.Println("String:", s)
}
```

### การตัดข้อผิดพลาดแบบกำหนดเอง
```go
import "errors"

var (
    ErrNotFound    = errors.New("not found")
    ErrUnauthorized = errors.New("unauthorized")
)

type ValidationError struct {
    Field   string
    Message string
    Err     error
}

func (e *ValidationError) Error() string {
    return fmt.Sprintf("validation: %s: %s", e.Field, e.Message)
}

func (e *ValidationError) Unwrap() error { return e.Err }

func validateAge(age int) error {
    if age < 0 {
        return &ValidationError{
            Field: "age", Message: "must be non-negative",
        }
    }
    return nil
}

// Error wrapping and checking
func getUser(id int) (*User, error) {
    user, err := db.Find(id)
    if err != nil {
        return nil, fmt.Errorf("getUser(%d): %w", id, ErrNotFound)
    }
    return user, nil
}

// Usage
_, err := getUser(42)
if errors.Is(err, ErrNotFound) {
    fmt.Println("User not found")
}
```

---

## ความสอดคล้องและความเท่าเทียม (เจาะลึก)
### รูปแบบสระคนงาน
```go
func workerPool(jobs <-chan int, results chan<- int, workerCount int) {
    var wg sync.WaitGroup
    for w := 0; w < workerCount; w++ {
        wg.Add(1)
        go func(id int) {
            defer wg.Done()
            for j := range jobs {
                results <- j * 2  // Process job
            }
        }(w)
    }
    wg.Wait()
    close(results)
}

func main() {
    jobs := make(chan int, 100)
    results := make(chan int, 100)

    go workerPool(jobs, results, 5)

    for j := 1; j <= 20; j++ {
        jobs <- j
    }
    close(jobs)

    for r := range results {
        fmt.Println("Result:", r)
    }
}
```

### บริบทสำหรับการยกเลิก
```go
func fetchWithTimeout(ctx context.Context, url string) ([]byte, error) {
    ctx, cancel := context.WithTimeout(ctx, 5*time.Second)
    defer cancel()

    req, err := http.NewRequestWithContext(ctx, "GET", url, nil)
    if err != nil {
        return nil, err
    }

    resp, err := http.DefaultClient.Do(req)
    if err != nil {
        return nil, err
    }
    defer resp.Body.Close()
    return io.ReadAll(resp.Body)
}
```

### เลือกสำหรับมัลติเพล็กซ์
```go
func fanIn(ch1, ch2 <-chan string) <-chan string {
    merged := make(chan string)
    go func() {
        for {
            select {
            case v := <-ch1:
                merged <- v
            case v := <-ch2:
                merged <- v
            }
        }
    }()
    return merged
}
```

---

## การกำหนดค่าโครงการ & ระบบการสร้าง
### โครงสร้างโครงการ
```
my_project/
+-- go.mod
+-- go.sum
+-- main.go
+-- internal/
|   +-- handlers/
|   |   +-- api.go
|   +-- models/
|   |   +-- user.go
|   +-- service/
|       +-- user_service.go
+-- pkg/
|   +-- utils/
|       +-- helpers.go
+-- cmd/
|   +-- server/
|       +-- main.go
|   +-- cli/
|       +-- main.go
+-- api/
|   +-- openapi.yaml
+-- configs/
|   +-- config.yaml
+-- deployments/
|   +-- Dockerfile
+-- .golangci.yml
```

### go.mod
```
module github.com/example/my_project

go 1.22

require (
    github.com/gin-gonic/gin v1.10.0
    github.com/go-sql-driver/mysql v1.8.0
    go.uber.org/zap v1.27.0
)
```

### คำสั่งที่จำเป็น
```bash
go mod init myproject         # Initialise module
go mod tidy                   # Download and clean dependencies
go build -o myapp             # Build binary
go run main.go                # Run without building
go test ./...                 # Run all tests
go vet ./...                  # Static analysis
gofmt -w .                    # Format code
go generate ./...             # Run code generators
```

### ไปป์ไลน์ CI/CD (การดำเนินการ GitHub)
```yaml
name: Go CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v5
        with:
          go-version: '1.22'
      - run: go vet ./...
      - run: go test -race -coverprofile=coverage.out ./...
      - run: go build ./...
```

---

## การทดสอบ
### การทดสอบหน่วย
```go
// math_test.go
package math

import "testing"

func TestAdd(t *testing.T) {
    tests := []struct {
        name     string
        a, b     int
        expected int
    }{
        {"positive", 2, 3, 5},
        {"negative", -1, -2, -3},
        {"zero", 0, 0, 0},
        {"mixed", -1, 1, 0},
    }
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            result := Add(tt.a, tt.b)
            if result != tt.expected {
                t.Errorf("Add(%d, %d) = %d; want %d", tt.a, tt.b, result, tt.expected)
            }
        })
    }
}

func BenchmarkAdd(b *testing.B) {
    for i := 0; i < b.N; i++ {
        Add(2, 3)
    }
}
```

### การทดสอบ HTTP ที่ขับเคลื่อนด้วยตาราง
```go
func TestHandler(t *testing.T) {
    req := httptest.NewRequest("GET", "/health", nil)
    w := httptest.NewRecorder()
    healthHandler(w, req)

    if w.Code != http.StatusOK {
        t.Errorf("expected 200, got %d", w.Code)
    }
}
```

```bash
go test ./...                    # All tests
go test -v ./...                 # Verbose
go test -race ./...              # Race detector
go test -cover ./...             # Coverage
go test -bench=. ./...           # Benchmarks
go test -fuzz=Fuzz ./...         # Fuzz testing
```

---

## การทำงานร่วมกัน
### CGo (เรียก C จาก Go)
```go
package main

// #include <stdio.h>
// #include <stdlib.h>
//
// void print_hello() {
//     printf("Hello from C!\n");
// }
import "C"
import "unsafe"

func main() {
    C.print_hello()

    // Passing strings to C
    cs := C.CString("Hello from Go")
    defer C.free(unsafe.Pointer(cs))
    // Use cs in C function calls
}
```

### FFI พร้อมภาษาอื่น
| ทิศทาง | กลไก |
|----------|-----------|
| ไปโทรหา C | cgo (`import "C"`) |
| ไปโทร C ++ | ฟังก์ชั่น cgo + C wrapper |
| C โทรไป | ส่งออกฟังก์ชัน Go ด้วย`//export`|
| ไปเรียก Python | ใช้ gopy หรือกระบวนการย่อย |
---

## รูปแบบการออกแบบ
### รูปแบบมิดเดิลแวร์ (HTTP)
```go
type Middleware func(http.Handler) http.Handler

func Logging(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        start := time.Now()
        next.ServeHTTP(w, r)
        log.Printf("%s %s %v", r.Method, r.URL.Path, time.Since(start))
    })
}

func Auth(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        token := r.Header.Get("Authorization")
        if token == "" {
            http.Error(w, "Unauthorized", http.StatusUnauthorized)
            return
        }
        next.ServeHTTP(w, r)
    })
}

func Chain(h http.Handler, middlewares ...Middleware) http.Handler {
    for i := len(middlewares) - 1; i >= 0; i-- {
        h = middlewares[i](h)
    }
    return h
}
```

### รูปแบบตัวเลือก
```go
type Server struct {
    host    string
    port    int
    timeout time.Duration
}

type Option func(*Server)

func WithHost(host string) Option    { return func(s *Server) { s.host = host } }
func WithPort(port int) Option       { return func(s *Server) { s.port = port } }
func WithTimeout(d time.Duration) Option { return func(s *Server) { s.timeout = d } }

func NewServer(opts ...Option) *Server {
    s := &Server{host: "localhost", port: 8080, timeout: 30 * time.Second}
    for _, opt := range opts { opt(s) }
    return s
}

srv := NewServer(WithHost("0.0.0.0"), WithPort(3000))
```

---

## ประสิทธิภาพและการเพิ่มประสิทธิภาพ
### การทำโปรไฟล์
```bash
go test -cpuprofile=cpu.prof -bench=. ./...
go tool pprof cpu.prof
go test -memprofile=mem.prof -bench=. ./...
go tool pprof mem.prof
```

### เคล็ดลับการเพิ่มประสิทธิภาพ
```go
// Pre-allocate slices when size is known
result := make([]int, 0, 1000)

// Use sync.Pool for frequently allocated objects
var bufPool = sync.Pool{
    New: func() interface{} { return new(bytes.Buffer) },
}

// Avoid string concatenation in loops
var b strings.Builder
for i := 0; i < 1000; i++ {
    b.WriteString("hello")
}
result := b.String()
```

---

## การปรับใช้
### การรวบรวมข้าม
```bash
GOOS=linux GOARCH=amd64 go build -o myapp-linux
GOOS=windows GOARCH=amd64 go build -o myapp.exe
GOOS=darwin GOARCH=arm64 go build -o myapp-mac
```

### การปรับใช้นักเทียบท่า
```dockerfile
FROM golang:1.22-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY src/ ./
RUN CGO_ENABLED=0 go build -o myapp .

FROM alpine:latest
COPY --from=builder /app/myapp /usr/local/bin/myapp
CMD ["myapp"]
```

---

## ห้องสมุดมาตรฐาน
| แพ็คเกจ | วัตถุประสงค์ |
|---------|---------|
| เอฟเอ็มที | I/O ที่จัดรูปแบบแล้ว |
| สุทธิ/http | ไคลเอนต์ HTTP และเซิร์ฟเวอร์ |
| การเข้ารหัส/json | การเข้ารหัส / ถอดรหัส JSON |
| ระบบปฏิบัติการ | การดำเนินงานระดับระบบปฏิบัติการ |
| ไอโอ | I/O ดั้งเดิม |
| สตริง / strconv | การจัดการสตริง |
| ซิงค์ | Mutex, WaitGroup, ครั้งเดียว |
| บริบท | กำหนดเวลาการยกเลิก |
| การทดสอบ | กรอบการทดสอบในตัว |
| บันทึก / บันทึก / สล็อก | การบันทึก |
| เวลา | เวลาและระยะเวลา |
| การเข้ารหัสลับ | การเข้ารหัส (TLS, การแฮช) |
| ฐานข้อมูล/sql | นามธรรมฐานข้อมูล |
---

## เครื่องมือ
```bash
go mod init myproject
go run main.go
go build -o myapp
go test ./...
gofmt -w .
go vet ./...
go mod tidy
```

---

## เมื่อใดควรใช้ Go
| สถานการณ์ | ไปทำไม | ทางเลือกที่ดีกว่า |
|----------|--------|-------------------|
| บริการคลาวด์เนทีฟ / ไมโครเซอร์วิส | ไบนารี่ที่รวดเร็วและเล็ก HTTP | ที่ยอดเยี่ยม สนิมเพื่อประสิทธิภาพสูงสุด |
| เครื่องมือ CLI | การรวบรวมที่รวดเร็ว ไบนารี่เดียว | สนิมสำหรับ CLI ที่ซับซ้อน |
| เว็บเซิร์ฟเวอร์ / API | HTTP ในตัว รวดเร็ว เรียบง่าย | Node.js/Express สำหรับการสร้างต้นแบบอย่างรวดเร็ว |
| เครื่องมือ DevOps | Docker, Kubernetes, Terraform เป็น Go | Python สำหรับการเขียนสคริปต์ |
| ระบบพร้อมกัน | Goroutines มีน้ำหนักเบาและสง่างาม | Erlang/Elixir สำหรับการทำงานพร้อมกันที่ทนต่อข้อผิดพลาด |
| การเขียนโปรแกรมเครือข่าย | แพ็คเกจเน็ตสุดคุ้ม | C/C++ สำหรับการควบคุมระดับต่ำสุด |
| วิทยาศาสตร์ข้อมูล / ML | ไม่ใช่ระบบนิเวศที่เหมาะสม | หลาม, อาร์ |
| GUI บนเดสก์ท็อป/มือถือ | ไม่มีกรอบงาน GUI | ใช้ส่วนหน้าของเว็บหรือภาษาพื้นเมือง |
| ระบบสมองกลฝังตัว | หนักเกินไป (GC, รันไทม์) | C, สนิม |
---

## สรุป
Go เป็นภาษาที่จงใจเลือกความเรียบง่ายเหนือฟีเจอร์ต่างๆ มีโครงสร้างน้อยกว่าภาษาส่วนใหญ่ ไม่มีการสืบทอด ไม่มีวิธีการโอเวอร์โหลด ไม่มีข้อยกเว้น ไม่มีมาโคร และนี่คือจุดแข็ง ผลลัพธ์ที่ได้คือโค้ดที่อ่านง่าย เขียนง่าย และดูแลรักษาง่าย โมเดลการทำงานพร้อมกันของ Go (โกรูทีนและแชนเนล) เป็นหนึ่งในโมเดลที่ได้รับการออกแบบอย่างดีที่สุดในทุกภาษา สำหรับโครงสร้างพื้นฐานคลาวด์ ไมโครเซอร์วิส เครื่องมือ CLI และการเขียนโปรแกรมเครือข่าย Go เป็นตัวเลือกที่ยอดเยี่ยม