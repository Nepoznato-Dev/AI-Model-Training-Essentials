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

＃ 行く
Go (元のドメイン名にちなんで「Golang」と呼ばれることが多い) は、Robert Griesemer、Rob Pike、Ken Thompson によって Google で設計された、静的に型指定され、コンパイルされたプログラミング言語です。この言語は、C のパフォーマンスと Python などの動的言語の生産性を組み合わせた、システム プログラミングにより優れた言語になるという明確な目標を掲げて 2012 年に初めてリリースされました。 Go は、そのシンプルさ、高速なコンパイル、組み込みの同時実行性 (ゴルーチンとチャネル)、および優れたツールで知られています。
Go はクラウド インフラストラクチャ エコシステムの多くを支えています。Docker、Kubernetes、Terraform、Prometheus など、および Go 標準ライブラリの HTTP サーバーはすべて Go で書かれています。これは、クラウドネイティブ開発、マイクロサービス、および CLI ツールのデフォルト言語となっています。
---

## Go が重要な理由
- **設計によるシンプルさ**: Go には 25 個のキーワードしかありません。この言語は意図的に小さくなっており、習得が簡単です。
- **高速コンパイル**: 大規模なプロジェクトであっても、数秒でマシンコードに直接コンパイルします。
- **組み込みの同時実行性**: ゴルーチンとチャネルにより、同時プログラミングがアクセスしやすく効率的になります。
- **優れた標準ライブラリ**: HTTP サーバー、JSON エンコード、テスト、暗号化 -- すべてが組み込まれています。
- **静的バイナリ**: 外部依存関係のない単一のバイナリにコンパイルします。導入は簡単です。
- **Google スケールの系譜**: Unix、UTF-8、および Google のインフラストラクチャの多くを構築したエンジニアによって設計されています。
## トレードオフ
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **合計タイプ/パターン マッチングはありません** |関連するデータを持つ列挙型や代数型はありません。インターフェイスとタイプ スイッチを使用する |
| **冗長性を処理するエラー** | if err != nil はどこでも明示的にチェックします。パターンを受け入れます。エラー処理を可視化します。
| **小規模なエコシステム** | Python、Java、または JavaScript よりもライブラリが少ない |標準ライブラリはほとんどのニーズをカバーします。成長するコミュニティ パッケージ |
| **GUI フレームワークなし** |デスクトップまたはモバイル UI には適していません。 Web ベースの UI (WASM) または別の言語を使用する |
| **ガベージコレクター** | GC あり -- 一時停止は小さいですが、ゼロではありません。レイテンシの影響を受けやすいワークロードに合わせて GC を調整します。同期プールを使用する |
---

## 構文の基礎
### 基本構造
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

### 関数
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

### 構造体とインターフェイス
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

### エラー処理
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

### 同時実行 -- ゴルーチンとチャネル
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

## 高度な構文とパターン
### ジェネリック (Go 1.18 以降)
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

### 高度なパターン マッチング (タイプ スイッチ)
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

### カスタムエラーラッピング
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

## 同時実行性と並列処理 (詳細)
### ワーカープールパターン
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

### キャンセルのコンテキスト
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

### 多重化の選択
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

## プロジェクトの構成とシステムの構築
### プロジェクトの構造
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

### 必須コマンド
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

### CI/CD パイプライン (GitHub アクション)
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

## テスト
### 単体テスト
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

### テーブル駆動の HTTP テスト
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

## 相互運用性
### CGo (Go から C を呼び出す)
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

### 他の言語による FFI
|方向 |メカニズム |
|----------|----------|
| C | に電話してみます。 cgo (`import "C"`) |
| C++ を呼び出す | cgo + C ラッパー関数 |
| C が Go を呼び出す |`//export`を使用して Go 関数をエクスポートする |
| Python を呼び出します | gopy またはサブプロセスを使用する |
---

## デザインパターン
### ミドルウェア パターン (HTTP)
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

### オプション パターン
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

## パフォーマンスと最適化
### プロファイリング
```bash
go test -cpuprofile=cpu.prof -bench=. ./...
go tool pprof cpu.prof
go test -memprofile=mem.prof -bench=. ./...
go tool pprof mem.prof
```

### 最適化のヒント
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

## デプロイメント
### クロスコンパイル
```bash
GOOS=linux GOARCH=amd64 go build -o myapp-linux
GOOS=windows GOARCH=amd64 go build -o myapp.exe
GOOS=darwin GOARCH=arm64 go build -o myapp-mac
```

### Docker のデプロイメント
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

## 標準ライブラリ
|パッケージ |目的 |
|----------|----------|
| fmt |フォーマットされた I/O |
|ネット/http | HTTP クライアントとサーバー |
|エンコーディング/json | JSON エンコード/デコード |
| OS | OS レベルの操作 |
|イオ | I/O プリミティブ |
|文字列 / strconv |文字列操作 |
|同期 |ミューテックス、WaitGroup、1 回 |
|コンテキスト |締め切り、キャンセル |
|テスト |組み込みのテスト フレームワーク |
|ログ / ログ / スログ |ロギング |
|時間 |時間と期間 |
|暗号 |暗号化 (TLS、ハッシュ) |
|データベース/SQL |データベースの抽象化 |
---

## ツーリング
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

## Go を使用する場合
|シナリオ |なぜ行くのか |より良い代替案 |
|----------|----------|--------|
|クラウドネイティブ サービス / マイクロサービス |高速、小さいバイナリ、優れた HTTP | Rust で最大限のパフォーマンスを実現 |
| CLI ツール |高速コンパイル、単一バイナリ |複雑な CLI 用の Rust |
| Webサーバー/API |内蔵 HTTP、高速、シンプル |ラピッドプロトタイピングのための Node.js/Express |
| DevOps ツール | Docker、Kubernetes、Terraform が登場 |スクリプト作成のための Python |
|同時システム | goroutine は軽量でエレガントです |フォールトトレラントな同時実行のための Erlang/Elixir |
|ネットワークプログラミング |優れたネットパッケージ |最下位レベルの制御用の C/C++ |
|データ サイエンス / ML |適切なエコシステムではない |パイソン、R |
|デスクトップ/モバイル GUI | GUI フレームワークなし | Web フロントエンドまたは母国語を使用する |
|組み込みシステム |重すぎる (GC、ランタイム) | C、錆 |
---

＃＃ まとめ
Go は、機能よりもシンプルさを意図的に選択した言語です。ほとんどの言語よりも構成要素が少なく、継承、メソッドのオーバーロード、例外、マクロはありませんが、これが強みです。その結果、読みやすく、書きやすく、保守しやすいコードが得られます。 Go の同時実行モデル (ゴルーチンとチャネル) は、あらゆる言語の中で最もよく設計されたモデルの 1 つです。クラウド インフラストラクチャ、マイクロサービス、CLI ツール、ネットワーク プログラミングには、Go が最適な選択肢です。