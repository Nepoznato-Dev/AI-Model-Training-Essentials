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
- **高速コンパイル**: 大規模なプロジェクトであっても、数秒で直接マシンコードにコンパイルします。
- **組み込みの同時実行性**: ゴルーチンとチャネルにより、同時プログラミングがアクセスしやすく効率的になります。
- **優れた標準ライブラリ**: HTTP サーバー、JSON エンコード、テスト、暗号化 -- すべてが組み込まれています。
- **静的バイナリ**: 外部依存関係のない単一のバイナリにコンパイルします。導入は簡単です。
- **Google スケールの血統**: Unix、UTF-8、および Google のインフラストラクチャの多くを構築したエンジニアによって設計されています。
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

## 総合的な Q&A
### Q1: Go にはなぜ例外がないのですか?エラーはどのように処理すればよいでしょうか?
**A:** Go は、例外の代わりに明示的なエラーを返します。失敗する可能性のあるすべての関数は、最後の戻り値として`error`を返します。これにより、呼び出し元はエラーを明示的に処理する必要が生じます。サイレントエラーやキャッチブロックの忘れは発生しません。慣用的なパターンは`if err != nil`です。エラーのラップには`fmt.Errorf`を`%w`とともに使用し、エラー タイプのチェックには`errors.Is`/`errors.As`を使用します。回復不可能なエラー (プログラミングのバグ) の場合は、`panic`を使用します。
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

### Q2: ゴルーチンとは何ですか? OS スレッドとの違いは何ですか?
**A:** ゴルーチンは、Go ランタイムによって管理される軽量のユーザー空間スレッドです。これらは、最大 2 KB のスタック (OS スレッドの場合は最大 1 MB) で開始され、スケジューラによって OS スレッドに多重化され、一度に数百万個作成できます。ゴルーチン間の通信にはチャネル (または共有状態の`sync`プリミティブ) が使用されます。 goroutine リークを避けるために、常に`sync.WaitGroup`またはコンテキスト キャンセルを使用してください。
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

### Q3: 同時実行のためにチャネルとミューテックスのどちらを使用する必要があるのですか?
**A:** ゴルーチンがデータを通信する必要がある場合はチャネルを使用します。チャネルは「通信によるメモリの共有」の理念を強制します。ゴルーチンが共有状態 (キャッシュ、カウンター、接続プール) を保護する必要がある場合は、ミューテックス (`sync.Mutex`) を使用します。良いルール: データがゴルーチン間で受け渡される場合は、チャネルを使用します。データが複数のゴルーチンによってアクセスされている場合は、ミューテックスを使用します。単純なアトミック操作の場合は、`sync/atomic`を使用します。
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

### Q4:`nil`スライス/マップと空のスライス/マップの違いは何ですか?
**A:**`nil`スライス (`var s []int`) には基礎となる配列がなく、長さ 0、容量 0 です。空のスライス (`s := []int{}`または`make([]int, 0)`) には基礎となる配列がありますが、長さは 0 です。どちらも`append`、`len`、`cap`、および`range`。 JSON マーシャリングは異なります。 nil スライスは`null`になり、空のスライスは`[]`になります。ベスト プラクティス: 戻り値には nil スライスを使用し (「データなし」を示します)、JSON 出力が重要な場合は空のスライスを使用します。
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

### Q5: Go ではインターフェイスはどのように機能しますか? 空のインターフェイスとは何ですか?
**A:** Go インターフェイスは暗黙的に満たされます。型は、`implements` キーワードを使用せずにメソッドを実装することによってインターフェイスを実装します。これにより、デカップリングと合成が可能になります。空のインターフェイス`interface{}`(Go 1.18 以降では `any`) は、すべての型で満たされます。使用は慎重に行ってください (ジェネリックの方が優れていることがよくあります)。インターフェイス値はペアです:`(type, value)`。 nil インターフェースは両方とも nil になります。
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

## 思考連鎖による問題解決
### 問題 1: レート制限のある同時 Web スクレイパーを構築する
**問題ステートメント:** リストから URL を同時に取得し、ページ タイトルを抽出し、1 秒あたり 10 リクエストのレート制限を遵守し、データ競合なしで結果を収集する Go プログラムを構築します。
**ステップ 1 — 問題を理解する:**
(1) ゴルーチンによる同時 HTTP フェッチ、(2) サーバーの過負荷を避けるためのレート制限、(3) 競合のない結果収集、(4) 失敗したリクエストに対する適切なエラー処理が必要です。 Go の同時実行プリミティブ (ゴルーチン、チャネル、`errgroup`) はこれに最適です。
**ステップ 2 — アプローチを特定する:**
- トークンバケットのレート制限には`golang.org/x/time/rate`を使用します。
- ゴルーチンを管理するには、`sync.WaitGroup` または`errgroup.Group`を使用します。
- 結果チャネルを使用して出力を安全に収集します。
- キャンセルとタイムアウトには`context.Context`を使用します。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- データ競合なし: 各ゴルーチンは`results`内の独自のインデックスに書き込みます。ミューテックスは必要ありません。
-`errgroup.SetLimit`は、レート リミッターとは独立して同時実行を制限します。
-`io.LimitReader`は、過度に大きなページの読み取りを防ぎます。
-`http.NewRequestWithContext`は、コンテキストが完了したときにリクエストが確実にキャンセルされるようにします。
- 運用環境の場合: 指数バックオフを使用した再試行ロジック、接続プーリングの調整、およびメトリクスを追加します。
### 問題 2: 汎用 LRU キャッシュの実装
**問題ステートメント:** ジェネリックス (Go 1.18 以降) を使用して、Go にスレッドセーフなジェネリック LRU (最も最近使用されていない) キャッシュを実装します。 O(1) 時間計算量の`Get`、`Set`、および`Delete`をサポートする必要があります。
**ステップ 1 — 問題を理解する:**
LRU キャッシュには、O(1) のルックアップ (ハッシュ マップ) と O(1) の順序付け更新 (二重リンク リスト) が必要です。`Get`の場合: 項目を前に移動します。`Set`の場合: 前に挿入します。容量を超えた場合は後ろから追い出します。スレッド セーフティにはミューテックスが必要です。
**ステップ 2 — アプローチを特定する:**
- O(1) 前面への移動および背面からの削除には、`container/list` (二重リンク リスト) を使用します。
- O(1) ルックアップには`map[K]*list.Element`を使用します。
- スレッドセーフのために`sync.Mutex`を使用します。
- タイプ セーフティのためのジェネリックス (`[K comparable, V any]`)。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
-`Get`、`Set`、`Delete`の場合は O(1) : マップ ルックアップは平均 O(1) です。リスト操作 (`MoveToFront`、`PushFront`、`Remove`、`Back`) はすべて O(1) です。
- スレッド セーフ:`sync.Mutex`は、一度に 1 つの goroutine だけがキャッシュにアクセスすることを保証します。読み取り負荷の高いワークロードの場合は、`sync.RWMutex`を使用します。
- ジェネリック:`[K comparable, V any]`は、キーが`==`(マップ キーに必要) をサポートすることを保証しますが、値は任意の型にすることができます。
- 本番環境:`github.com/hashicorp/golang-lru/v2`を検討してください。TTL サポートとシャーディングにより、ロック競合が軽減され、十分なテストが行​​われています。
### 問題 3: TCP チャット サーバーを構築する
**問題点:** クライアントが接続し、接続されている他のすべてのクライアントにメッセージをブロードキャストし、正常に切断できる同時 TCP チャット サーバーを構築します。他のクライアントをブロックすることなく、遅いクライアントを処理します。
**ステップ 1 — 問題を理解する:**
(1) TCP 接続を受け入れる、(2) 読み取り用にクライアントごとに 1 つのゴルーチン、(3) すべてのクライアントにメッセージを送信するブロードキャスト メカニズム、(4) 切断と低速クライアントの処理が必要です。これは古典的なファンアウト パターンです。
**ステップ 2 — アプローチを特定する:**
- TCP 接続には`net.Listener`を使用します。
- クライアントの登録/登録解除/ブロードキャスト用のチャネルを持つ中央の`hub`ゴルーチンを使用します。
- 各クライアントはバッファリングされたチャネルを持つ専用の書き込みゴルーチンを取得します。遅いクライアントは他のクライアントをブロックしません。
- 正常なシャットダウンには`context.Context`を使用します。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- クライアント処理が遅い: ブロードキャストで`select`と`default`を併用すると、ブロックが防止されます。低速クライアントは、バッファがいっぱいになると切断されます。
- レースなし: ハブのゴルーチンは`clients`マップへの単一の書き込み者です。 `mu`はブロードキャスト中の読み取りを保護します。
- 正常なシャットダウン:`context.Context`とシグナル ハンドラーを追加して、リスナーを閉じて接続をドレインします。
- 運用: ブラウザ クライアントに`golang.org/x/net/websocket`の使用を検討し、認証、メッセージ履歴、ルームを追加します。
---

＃＃ まとめ
Go は、機能よりもシンプルさを意図的に選択した言語です。ほとんどの言語よりも構成要素が少なく、継承、メソッドのオーバーロード、例外、マクロはありませんが、これが強みです。その結果、読みやすく、書きやすく、保守しやすいコードが得られます。 Go の同時実行モデル (ゴルーチンとチャネル) は、あらゆる言語の中で最もよく設計されたモデルの 1 つです。クラウド インフラストラクチャ、マイクロサービス、CLI ツール、ネットワーク プログラミングには、Go が最適な選択肢です。