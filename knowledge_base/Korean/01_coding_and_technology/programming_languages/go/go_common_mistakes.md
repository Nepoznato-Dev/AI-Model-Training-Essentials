<!--
---
# Metadata
title: "Go — Common Mistakes & Anti-Patterns"
description: "Comprehensive guide to common pitfalls, traps, and anti-patterns in Go that catch even experienced developers, with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial common mistakes document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [go, golang, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Go — 일반적인 실수 및 안티 패턴
이 문서는 Go에서 가장 흔히 발생하는 실수, 함정, 안티패턴을 나열합니다. 각 항목은 잘못된 접근 방식을 보여주고, 실패 이유를 설명하며, 올바른 솔루션을 제공합니다.
---

## 1. 고루틴의 루프 변수 캡처
```go
// ❌ WRONG — all goroutines share the same variable (pre-Go 1.22)
for i := 0; i < 5; i++ {
    go func() {
        fmt.Println(i)  // may print 5, 5, 5, 5, 5
    }()
}

// ✅ CORRECT — pass as argument
for i := 0; i < 5; i++ {
    go func(n int) {
        fmt.Println(n)
    }(i)
}

// ✅ CORRECT — Go 1.22+ creates new variable per iteration
for i := 0; i < 5; i++ {
    go func() {
        fmt.Println(i)  // works correctly in Go 1.22+
    }()
}
```

---

## 2. 오류 반환 무시
```go
// ❌ WRONG — ignoring errors
result, _ := riskyOperation()

// ❌ WRONG — blank identifier for error
data, _ := os.ReadFile("config.json")

// ✅ CORRECT — always handle errors
result, err := riskyOperation()
if err != nil {
    return fmt.Errorf("operation failed: %w", err)
}

// ✅ CORRECT — at minimum, log the error
data, err := os.ReadFile("config.json")
if err != nil {
    log.Printf("Warning: could not read config: %v", err)
    data = defaultConfig
}
```

---

## 3. 슬라이스 추가 문제
```go
// ❌ WRONG — append may not modify the original slice
func addItems(s []int) {
    s = append(s, 4, 5, 6)  // original slice unchanged if capacity exceeded!
}

// ✅ CORRECT — return the new slice
func addItems(s []int) []int {
    return append(s, 4, 5, 6)
}

// ✅ CORRECT — pre-allocate with known capacity
s := make([]int, 0, 10)
s = append(s, 1, 2, 3)
```

---

## 4. 고루틴 누출
```go
// ❌ WRONG — goroutine blocks forever if channel is never read
func process() {
    ch := make(chan int)
    go func() {
        result := compute()
        ch <- result  // blocks forever if caller returns early
    }()
    // if we return here without reading ch, goroutine leaks
}

// ✅ CORRECT — use context for cancellation
func process(ctx context.Context) (int, error) {
    ch := make(chan int, 1)  // buffered channel
    go func() {
        result, err := compute()
        if err != nil {
            return
        }
        select {
        case ch <- result:
        case <-ctx.Done():
            return  // exit if context cancelled
        }
    }()

    select {
    case result := <-ch:
        return result, nil
    case <-ctx.Done():
        return 0, ctx.Err()
    }
}
```

---

## 5. 구조체 메소드에 대한 Nil 포인터 역참조
```go
// ❌ WRONG — calling method on nil pointer
var user *User
user.GetName()  // panic if GetName doesn't handle nil

// ✅ CORRECT — check for nil or use value receiver
func (u *User) GetName() string {
    if u == nil {
        return ""
    }
    return u.Name
}
```

---

## 6. 루프에서`defer`사용하기
```go
// ❌ WRONG — files accumulate until function returns
func processFiles(paths []string) error {
    for _, path := range paths {
        f, err := os.Open(path)
        if err != nil {
            return err
        }
        defer f.Close()  // all Close() calls deferred to function exit!
        process(f)
    }
    return nil
}

// ✅ CORRECT — extract to helper function
func processFiles(paths []string) error {
    for _, path := range paths {
        if err := processOne(path); err != nil {
            return err
        }
    }
    return nil
}

func processOne(path string) error {
    f, err := os.Open(path)
    if err != nil {
        return err
    }
    defer f.Close()
    return process(f)
}
```

---

## 7. 안티 패턴: 명명된 변수를 조기에 반환
```go
// ❌ WRONG — named returns can cause subtle bugs with defer
func process() (result int, err error) {
    defer func() {
        if r := recover(); r != nil {
            err = fmt.Errorf("panic: %v", r)
            // result is zero value — may not be what you want
        }
    }()
    result = compute()
    return
}

// ✅ CORRECT — use explicit returns unless defer needs them
func process() (int, error) {
    result := compute()
    return result, nil
}
```

---

## 8. 지도 반복 순서는 무작위입니다.
```go
// ❌ WRONG — expecting consistent map iteration order
for key, value := range myMap {
    fmt.Printf("%s: %d\n", key, value)
}
// Order changes every run!

// ✅ CORRECT — sort keys first if order matters
keys := make([]string, 0, len(myMap))
for k := range myMap {
    keys = append(keys, k)
}
sort.Strings(keys)
for _, k := range keys {
    fmt.Printf("%s: %d\n", k, myMap[k])
}
```

---

## 9. 루프의 문자열 연결
```go
// ❌ WRONG — creates new string each iteration (O(n²))
var result string
for _, s := range parts {
    result += s
}

// ✅ CORRECT — use strings.Builder
var builder strings.Builder
for _, s := range parts {
    builder.WriteString(s)
}
result := builder.String()

// ✅ CORRECT — use strings.Join
result := strings.Join(parts, "")
```

---

## 10. 안티 패턴: 인터페이스 오염
```go
// ❌ WRONG — creating interfaces before they're needed
type UserRepository interface {
    FindByID(id int) (*User, error)
    Save(user *User) error
    Delete(id int) error
}

type userRepository struct{}  // only one implementation

// ✅ CORRECT — accept interfaces, return structs
// Create interfaces when you need them (for testing, mocking)
// "Accept interfaces, return structs" — Go proverb
```

---

## 11. 초기화에 `sync.Once`를 사용하지 않음
```go
// ❌ WRONG — race condition on initialization
var config *Config
var configOnce sync.Once

func GetConfig() *Config {
    if config == nil {  // race condition!
        config = loadConfig()
    }
    return config
}

// ✅ CORRECT — use sync.Once
var config *Config
var configOnce sync.Once

func GetConfig() *Config {
    configOnce.Do(func() {
        config = loadConfig()
    })
    return config
}
```

---

## 12.`sync`유형 복사
```go
// ❌ WRONG — copying a Mutex breaks it
type Counter struct {
    mu    sync.Mutex
    count int
}

func (c Counter) Increment() {  // value receiver — copies the mutex!
    c.mu.Lock()
    c.count++
    c.mu.Unlock()
}

// ✅ CORRECT — use pointer receiver
func (c *Counter) Increment() {
    c.mu.Lock()
    c.count++
    c.mu.Unlock()
}
```

---

## 요약
Go의 단순성은 강점이지만 버퍼링되지 않은 채널에서 고루틴 누출, 원본을 수정하지 않는 슬라이스 추가 의미 체계, 루프에 누적되는 지연된 호출, 의도적으로 무작위로 지정되는 맵 반복 등 미묘한 함정이 있습니다. Go 속담이 길을 안내합니다. 모든 오류를 처리하고, 인터페이스를 허용하지만 구조체를 반환하고, 뮤텍스 유형에 포인터 수신기를 사용하고, 수동 고루틴 관리보다 동시성 기본 요소(`sync.Once`,`errgroup`, 컨텍스트 취소)를 선호합니다. 간단한 코드를 먼저 작성하세요. Go는 영리함보다 명확성을 보상합니다.