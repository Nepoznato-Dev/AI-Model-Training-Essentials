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

＃ 去
Go（通常以其原始網域命名為「Golang」）是一種靜態類型、編譯型程式語言，由 Google 的 Robert Griesemer、Rob Pike 和 Ken Thompson 設計。它於 2012 年首次發布，其明確目標是成為更好的系統程式語言——一種將 C 的性能與 Python 等動態語言的生產力結合起來的語言。 Go 以其簡單、快速編譯、內建並發（goroutines 和通道）和優秀的工具而聞名。
Go 為大部分雲端基礎架構生態系統提供支援：Docker、Kubernetes、Terraform、Prometheus、etcd 以及 Go 標準函式庫的 HTTP 伺服器都是用 Go 編寫的。它已成為雲端原生開發、微服務和 CLI 工具的預設語言。
---

## 為什麼 Go 很重要
- **設計簡單**：Go 只有 25 個關鍵字。該語言故意很小且易於學習。
- **快速編譯**：即使對於大型項目，也能在幾秒鐘內直接編譯為機器碼。
- **內建並發**：Goroutines 和通道使並發程式設計變得易於存取和高效。
- **優秀的標準函式庫**：HTTP 伺服器、JSON 編碼、測試、加密－全部內建。
- **靜態二進位檔案**：編譯為沒有外部相依性的單一二進位。部署很簡單。
- **Google 規模的血統**：由建造 Unix、UTF-8 和大部分 Google 基礎設施的工程師設計。
## 權衡
|限制|詳情 |典型解決方法|
|------------|---------|--------------------|
| **無總和類型/模式匹配** |沒有帶有關聯資料的枚舉，沒有代數類型 |使用介面和類型開關|
| **錯誤處理冗長** |明確 if err != nil 檢查各處 |接受圖案；它使錯誤處理可見 |
| **較小的生態系統** |比 Python、Java 或 JavaScript 更少的庫 |標準庫滿足大部分需求；社區套餐不斷增長|
| **無 GUI 框架** |不適合桌面或行動使用者介面 |使用基於 Web 的 UI (WASM) 或其他語言 |
| **垃圾收集器** |有 GC —— 暫停很小但非零 |針對延遲敏感的工作負載調整 GC；使用sync.Pool |
---

## 文法基礎知識
### 基本結構
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

### 函數
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

### 結構和接口
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

### 錯誤處理
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

### 並發－Goroutines 和 Channels
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

## 進階語法和模式
### 泛型（Go 1.18+）
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

### 進階模式匹配（類型開關）
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

### 自訂錯誤包裝
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

## 並發與並行（深入探討）
### 工作池模式
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

### 取消的上下文
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

### 選擇復用
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

## 專案配置與建置系統
### 專案結構
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

### 去.mod
```
module github.com/example/my_project

go 1.22

require (
    github.com/gin-gonic/gin v1.10.0
    github.com/go-sql-driver/mysql v1.8.0
    go.uber.org/zap v1.27.0
)
```

### 基本指令
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

### CI/CD 管道 (GitHub Actions)
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

## 測試
### 單元測試
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

### 表驅動的 HTTP 測試
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

## 互通性
### CGo（從 Go 呼叫 C）
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

### FFI 與其他語言
|方向 |機制|
|------------|------------|
|去打電話給C | cgo (`import "C"`) |
|去呼叫C++ | cgo + C 包裝函數 |
| C 呼叫 Go |使用`//export`匯出 Go 函數 |
|去呼叫Python |使用 gopy 或子程序 |
---

## 設計模式
### 中介軟體模式（HTTP）
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

### 選項模式
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

## 效能與最佳化
### 分析
```bash
go test -cpuprofile=cpu.prof -bench=. ./...
go tool pprof cpu.prof
go test -memprofile=mem.prof -bench=. ./...
go tool pprof mem.prof
```

### 最佳化技巧
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

## 部署
### 交叉編譯
```bash
GOOS=linux GOARCH=amd64 go build -o myapp-linux
GOOS=windows GOARCH=amd64 go build -o myapp.exe
GOOS=darwin GOARCH=arm64 go build -o myapp-mac
```

### Docker 部署
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

## 標準庫
|套餐 |目的|
|---------|---------|
| FMMT |格式化 I/O |
|網路/http | HTTP 用戶端與伺服器 |
|編碼/json | JSON 編碼/解碼 |
|作業系統 |作業系統層級操作 |
| io | I/O 原語 |
|字串/strconv |字串運算 |
|同步|互斥鎖、等待群組、一次 |
|背景 |截止日期、取消 |
|測試|內建測試框架 |
|日誌/日誌/slog |記錄 |
|時間 |時間與持續時間|
|加密 |密碼學（TLS、雜湊）|
|資料庫/sql |資料庫抽象|
---

## 工具
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

## 何時使用 Go
|場景|為什麼要去 |更好的選擇|
|----------|--------|--------------------|
|雲端原生服務/微服務 |快速、小型二進位、出色的 HTTP | Rust 實現最佳效能 |
| CLI 工具 |快速編譯，單一二進位檔案 | Rust 用於複雜的 CLI |
| Web 伺服器/API |內建HTTP，快速，簡單|用於快速原型設計的 Node.js/Express |
| DevOps 工具 | Docker、Kubernetes、Terraform 都是 Go |用於腳本編寫的 Python |
|並發系統| Goroutine 輕巧且優雅 | Erlang/Elixir 用於容錯並發 |
|網路程式設計|優網包|用於最低等級控制的 C/C++ |
|資料科學/機器學習 |沒有正確的生態系統| Python、R |
|桌面/行動 GUI |沒有GUI框架|使用網路前端或母語 |
|嵌入式系統|太重（GC、運行時）| C、鐵鏽|
---

## 綜合問答
### Q1：為什麼Go沒有異常？我該如何處理錯誤？
**A:** Go 使用明確錯誤返回而不是異常。每個可能失敗的函數都會傳回`error`作為其最後的回傳值。這迫使呼叫者明確地處理錯誤——沒有靜默的失敗或忘記的 catch 區塊。慣用模式是`if err != nil`。使用`fmt.Errorf`和`%w`來包裝錯誤，使用`errors.Is`/`errors.As`檢查錯誤類型。對於不可恢復的錯誤（程式錯誤），請使用`panic`。
```go
func readConfig(path string) (Config, error) {
    data, err := os.ReadFile(path)
    if err != nil {
        return Config{}, fmt.Errorf("reading config %s: %w", path, err)
    }
    var cfg Config
    if err := json.Unmarshal(data, &cfg); err != nil {
        return Config{}, fmt.Errorf("parsing config %s: %w", path, err)
    }
    return cfg, nil
}
```

### Q2：什麼是 goroutine，它們與作業系統執行緒有何不同？
**A:** Goroutines 是由 Go 執行時期管理的輕量級使用者空間執行緒。它們以約 2KB 的堆疊開始（作業系統執行緒約 1MB），由調度程式多路復用到作業系統執行緒上，並且一次可以創建數百萬個。 goroutine 之間的通訊使用通道（或用於共用狀態的`sync`原語）。始終使用`sync.WaitGroup`或上下文取消來避免 goroutine 洩漏。
```go
// Launch thousands of goroutines — perfectly fine
var wg sync.WaitGroup
for i := 0; i < 10000; i++ {
    wg.Add(1)
    go func(id int) {
        defer wg.Done()
        process(id)
    }(i)
}
wg.Wait()
```

### Q3：什麼時候應該使用通道和互斥體來實現並發？
**A：** 當 goroutine 需要通訊資料時使用通道－它們強制執行「透過通訊共享記憶體」的概念。當 goroutine 需要保護共用狀態（快取、計數器、連線池）時，請使用互斥體 (`sync.Mutex`)。一個好的規則：如果數據在 goroutine 之間傳遞，則使用通道；如果多個 goroutine 存取數據，請使用互斥體。對於簡單的原子操作，請使用`sync/atomic`。
```go
// Channel pattern — pipeline
func producer(nums chan<- int) {
    for i := 0; i < 10; i++ { nums <- i }
    close(nums)
}
func consumer(nums <-chan int, results chan<- int) {
    for n := range nums { results <- n * n }
    close(results)
}

// Mutex pattern — shared cache
type SafeCache struct {
    mu    sync.RWMutex
    items map[string]string
}
func (c *SafeCache) Get(key string) (string, bool) {
    c.mu.RLock()
    defer c.mu.RUnlock()
    v, ok := c.items[key]
    return v, ok
}
```

### Q4：`nil` 切片/貼圖和空切片/貼圖有什麼不同？
**A:**`nil`切片 (`var s []int`) 沒有底層數組，長度為 0，容量為 0。空切片（`s := []int{}`或`make([]int, 0)`）有底層數組，但長度為 0。兩者與`append`、`len`、`cap`的工作方式相同，和`range`。 JSON 封送不同： nil 切片變成`null`，空切片變成`[]`。最佳實務：首選 nil 切片作為傳回值（它們表示「無資料」），當 JSON 輸出很重要時使用空切片。
```go
var nilSlice []int          // nil, len=0, cap=0
emptySlice := []int{}       // not nil, len=0, cap=0

// Both work with append
nilSlice = append(nilSlice, 1)   // Now len=1
emptySlice = append(emptySlice, 1) // Now len=1

// JSON difference
json.Marshal(nilSlice)     // "null"
json.Marshal(emptySlice)   // "[]"
```

### Q5：Go 中的介面是如何運作的，什麼是空介面？
**A:** Go 接口是隱式滿足的——類型通過實現其方法來實現接口，沒有`implements`關鍵字。這使得解耦和組合成為可能。每種類型都滿足空介面`interface{}`（或 Go 1.18+ 中的`any`）——謹慎使用它（泛型通常更好）。介面值是對：`(type, value)`。 nil 介面兩者皆為 nil。
```go
// Implicit interface satisfaction
type Writer interface {
    Write(p []byte) (n int, err error)
}

// MyWriter implements Writer without declaring it
type MyWriter struct { buf *bytes.Buffer }
func (w *MyWriter) Write(p []byte) (int, error) { return w.buf.Write(p) }

// Type assertion and type switch
func describe(i interface{}) string {
    switch v := i.(type) {
    case int:
        return fmt.Sprintf("integer: %d", v)
    case string:
        return fmt.Sprintf("string: %q", v)
    default:
        return fmt.Sprintf("unknown: %T", v)
    }
}
```

---

## 解決問題的思路
### 問題 1：建立具有速率限制的並發 Web 爬蟲
**問題陳述：** 建立一個 Go 程序，同時從清單中取得 URL、提取頁面標題、遵守每秒 10 個請求的速率限制，並在沒有資料競爭的情況下收集結果。
**第 1 步 — 了解問題：**
我們需要：(1) 使用 goroutine 進行並發 HTTP 獲取，(2) 速率限制以避免伺服器不堪重負，(3) 無競爭的結果收集，(4) 對失敗請求進行正確的錯誤處理。 Go 的並發原語（goroutines、channels、`errgroup`）非常適合此目的。
**第 2 步 — 確定方法：**
- 使用`golang.org/x/time/rate`進行令牌桶速率限制。
- 使用`sync.WaitGroup`或`errgroup.Group`來管理 goroutine。
- 使用結果通道安全地收集輸出。
- 使用`context.Context`進行取消和逾時。
**第 3 步 — 實施解決方案：**
```go
package main

import (
    "context"
    "fmt"
    "io"
    "net/http"
    "regexp"
    "sync"
    "time"

    "golang.org/x/sync/errgroup"
    "golang.org/x/time/rate"
)

type Result struct {
    URL   string
    Title string
    Error error
}

var titleRegex = regexp.MustCompile(`<title[^>]*>(.*?)</title>`)

func fetchTitle(ctx context.Context, client *http.Client, url string) Result {
    req, err := http.NewRequestWithContext(ctx, "GET", url, nil)
    if err != nil {
        return Result{URL: url, Error: err}
    }
    resp, err := client.Do(req)
    if err != nil {
        return Result{URL: url, Error: err}
    }
    defer resp.Body.Close()

    body, err := io.ReadAll(io.LimitReader(resp.Body, 1<<20)) // 1MB limit
    if err != nil {
        return Result{URL: url, Error: err}
    }

    matches := titleRegex.FindSubmatch(body)
    if matches == nil {
        return Result{URL: url, Title: "(no title)"}
    }
    return Result{URL: url, Title: string(matches[1])}
}

func scrapeAll(ctx context.Context, urls []string, rps int) []Result {
    limiter := rate.NewLimiter(rate.Limit(rps), rps)
    client := &http.Client{Timeout: 10 * time.Second}
    results := make([]Result, len(urls))

    g, ctx := errgroup.WithContext(ctx)
    g.SetLimit(20) // Max 20 concurrent goroutines

    for i, url := range urls {
        i, url := i, url // Capture loop variables
        g.Go(func() error {
            if err := limiter.Wait(ctx); err != nil {
                return err
            }
            results[i] = fetchTitle(ctx, client, url)
            return nil
        })
    }

    if err := g.Wait(); err != nil {
        fmt.Fprintf(os.Stderr, "Error: %v\n", err)
    }
    return results
}
```

**第 4 步 — 驗證與最佳化：**
- 無資料競爭：每個 goroutine 寫入`results`中自己的索引 - 不需要互斥體。
-`errgroup.SetLimit`獨立於速率限制器限制並發性。
-`io.LimitReader`防止讀取過大的頁面。
-`http.NewRequestWithContext`確保上下文完成時取消請求。
- 對於生產：增加具有指數退避、連接池調整和指標的重試邏輯。
### 問題 2：實作通用 LRU 緩存
**問題陳述：** 使用泛型（Go 1.18+）在 Go 中實現線程安全的通用 LRU（最近最少使用）快取。它應該支援`Get`、`Set`和`Delete`，時間複雜度為 O(1)。
**第 1 步 — 了解問題：**
LRU 快取需要 O(1) 來尋找（雜湊映射）和 O(1) 排序更新（雙向鍊錶）。在`Get`上：將專案移到前面。在`Set`上：插入在前面；如果超出容量，則從後面驅逐。線程安全需要互斥鎖。
**第 2 步 — 確定方法：**
- 使用 `container/list`（雙向鍊錶）進行 O(1) 移至前面和從後面移除。
- 使用`map[K]*list.Element`進行 O(1) 尋找。
- 使用`sync.Mutex`實現線程安全。
- 用於型別安全的泛型 (`[K comparable, V any]`)。
**第 3 步 — 實施解決方案：**
```go
type entry[K comparable, V any] struct {
    key   K
    value V
}

type LRUCache[K comparable, V any] struct {
    capacity int
    items    map[K]*list.Element
    order    *list.List
    mu       sync.Mutex
}

func NewLRU[K comparable, V any](capacity int) *LRUCache[K, V] {
    return &LRUCache[K, V]{
        capacity: capacity,
        items:    make(map[K]*list.Element),
        order:    list.New(),
    }
}

func (c *LRUCache[K, V]) Get(key K) (V, bool) {
    c.mu.Lock()
    defer c.mu.Unlock()

    if elem, ok := c.items[key]; ok {
        c.order.MoveToFront(elem)
        return elem.Value.(*entry[K, V]).value, true
    }
    var zero V
    return zero, false
}

func (c *LRUCache[K, V]) Set(key K, value V) {
    c.mu.Lock()
    defer c.mu.Unlock()

    if elem, ok := c.items[key]; ok {
        c.order.MoveToFront(elem)
        elem.Value.(*entry[K, V]).value = value
        return
    }

    if c.order.Len() >= c.capacity {
        oldest := c.order.Back()
        if oldest != nil {
            c.order.Remove(oldest)
            delete(c.items, oldest.Value.(*entry[K, V]).key)
        }
    }

    e := &entry[K, V]{key: key, value: value}
    elem := c.order.PushFront(e)
    c.items[key] = elem
}

func (c *LRUCache[K, V]) Delete(key K) bool {
    c.mu.Lock()
    defer c.mu.Unlock()

    if elem, ok := c.items[key]; ok {
        c.order.Remove(elem)
        delete(c.items, key)
        return true
    }
    return false
}

func (c *LRUCache[K, V]) Len() int {
    c.mu.Lock()
    defer c.mu.Unlock()
    return c.order.Len()
}
```

**第 4 步 — 驗證與最佳化：**
- O(1) 對於`Get`、`Set`、`Delete`：地圖查找平均為 O(1) ；列表操作（`MoveToFront`、`PushFront`、 `Remove`、XQZKER OXQZ、XQZ）都是
- 線程安全：`sync.Mutex` 確保一次只有一個 goroutine 存取快取。對於讀取繁重的工作負載，請使用`sync.RWMutex`。
- 泛型：`[K comparable, V any]` 確保鍵支援 `==`（映射鍵必需），而值可以是任何類型。
- 生產：考慮`github.com/hashicorp/golang-lru/v2`— 經過了 TTL 支援和分片以減少鎖爭用的實戰測試。
### 問題 3：建立 TCP 聊天伺服器
**問題陳述：** 建立一個並發 TCP 聊天伺服器，客戶端可以在其中連接、向所有其他連接的客戶端廣播訊息，並正常斷開連接。處理緩慢的客戶端而不阻塞其他客戶端。
**第 1 步 — 了解問題：**
我們需要：（1）接受 TCP 連接，（2）每個客戶端一個用於讀取的 goroutine，（3）一種向所有客戶端發送訊息的廣播機制，（4）處理斷開連接和緩慢的客戶端。這是經典的扇出模式。
**第 2 步 — 確定方法：**
- 使用`net.Listener`進行 TCP 連線。
- 使用中央`hub`goroutine 和用戶端註冊/登出/廣播通道。
- 每個客戶端都有一個帶有緩衝通道的專用寫入 goroutine - 慢速客戶端不會阻塞其他客戶端。
- 使用`context.Context`正常關閉。
**第 3 步 — 實施解決方案：**
```go
package main

import (
    "bufio"
    "fmt"
    "log"
    "net"
    "sync"
)

type Client struct {
    conn net.Conn
    name string
    send chan string
}

type Hub struct {
    clients    map[*Client]bool
    broadcast  chan string
    register   chan *Client
    unregister chan *Client
    mu         sync.RWMutex
}

func NewHub() *Hub {
    return &Hub{
        clients:    make(map[*Client]bool),
        broadcast:  make(chan string, 256),
        register:   make(chan *Client),
        unregister: make(chan *Client),
    }
}

func (h *Hub) Run() {
    for {
        select {
        case client := <-h.register:
            h.mu.Lock()
            h.clients[client] = true
            h.mu.Unlock()
            h.broadcast <- fmt.Sprintf("[system] %s joined", client.name)

        case client := <-h.unregister:
            h.mu.Lock()
            if _, ok := h.clients[client]; ok {
                delete(h.clients, client)
                close(client.send)
            }
            h.mu.Unlock()
            h.broadcast <- fmt.Sprintf("[system] %s left", client.name)

        case msg := <-h.broadcast:
            h.mu.RLock()
            for client := range h.clients {
                select {
                case client.send <- msg:
                default:
                    // Slow client — disconnect
                    go func(c *Client) {
                        h.unregister <- c
                        c.conn.Close()
                    }(client)
                }
            }
            h.mu.RUnlock()
        }
    }
}

func handleClient(hub *Hub, conn net.Conn) {
    defer conn.Close()
    scanner := bufio.NewScanner(conn)

    // Read first line as name
    if !scanner.Scan() { return }
    name := scanner.Text()

    client := &Client{
        conn: conn,
        name: name,
        send: make(chan string, 64),
    }
    hub.register <- client
    defer func() { hub.unregister <- client }()

    // Write goroutine
    go func() {
        for msg := range client.send {
            fmt.Fprintf(conn, "%s\n", msg)
        }
    }()

    // Read loop
    for scanner.Scan() {
        text := scanner.Text()
        hub.broadcast <- fmt.Sprintf("[%s] %s", name, text)
    }
}

func main() {
    hub := NewHub()
    go hub.Run()

    listener, err := net.Listen("tcp", ":8080")
    if err != nil { log.Fatal(err) }
    log.Println("Chat server listening on :8080")

    for {
        conn, err := listener.Accept()
        if err != nil { log.Println(err); continue }
        go handleClient(hub, conn)
    }
}
```

**第 4 步 — 驗證與最佳化：**
- 客戶端處理速度慢：廣播中帶有`default`的`select`可防止阻塞。如果緩衝區已滿，慢速客戶端就會中斷連線。
- 無競賽：hub goroutine 是`clients`地圖的單一寫入者；`mu`保護廣播期間的讀取。
- 正常關閉：新增`context.Context`和訊號處理程序以關閉偵聽器和漏極連線。
- 生產：考慮將`golang.org/x/net/websocket`用於瀏覽器用戶端，並新增身份驗證、訊息歷史記錄和房間。
---

＃＃ 概括
Go 是一種刻意選擇簡單性而非功能的語言。它比大多數語言具有更少的構造——沒有繼承、沒有方法重載、沒有異常、沒有宏——這是一個優勢。結果是程式碼易於閱讀、易於編寫且易於維護。 Go 的並發模型（goroutine 和通道）是所有語言中設計最好的之一。對於雲端基礎架構、微服務、CLI 工具和網路編程，Go 是一個絕佳的選擇。