---
# Metadata
title: "C"
description: "Comprehensive reference for the C programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
tags: [c, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "35 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
#C
C는 1969년부터 1973년까지 Bell Labs의 Dennis Ritchie가 만든 범용, 절차적 프로그래밍 언어입니다. C는 Unix 운영 체제를 구현하도록 설계되었으며 50년이 지난 후에도 가장 널리 사용되는 프로그래밍 언어 중 하나로 남아 있습니다. C는 낮은 수준의 메모리 액세스, 최소한의 표준 라이브러리 및 기계 명령어에 대한 깔끔한 매핑을 제공하여 대부분의 최신 컴퓨팅이 구축되는 기반이 됩니다.
C는 운영 체제(Linux, Windows 커널, macOS), 임베디드 시스템, 데이터베이스 엔진(SQLite, PostgreSQL), 컴파일러(Python의 CPython, Ruby의 MRI) 및 기타 거의 모든 프로그래밍 언어 런타임의 기반이 되는 언어입니다. C를 이해하는 것은 컴퓨터가 실제로 어떻게 작동하는지 이해하는 것입니다.
---

## C가 중요한 이유
- **하드웨어에 대한 근접성**: C는 기계어 코드와 밀접하게 매핑됩니다. 가비지 수집기, 런타임 오버헤드, 숨겨진 할당이 없습니다.
- **유비쿼터스**: 마이크로컨트롤러부터 슈퍼컴퓨터까지 C는 어디에서나 실행됩니다.
- **컴퓨팅의 기초**: Linux, Windows, macOS 커널, Python 인터프리터, SQLite, Git - 모두 C로 작성되었습니다.
- **성능**: 메모리 레이아웃을 완벽하게 제어할 수 있어 최적에 가까운 실행 속도입니다.
- **영향**: C의 구문과 개념(포인터, 배열, 구조체, 함수)은 C++, Java, C#, JavaScript, Go, Rust 및 그 이후의 대부분의 언어를 형성했습니다.
## 절충안
| 제한사항 | 세부정보 | 일반적인 해결 방법 |
|------------|---------|------|
| **수동 메모리 관리** | 가비지 수집기 없음 - 메모리를 직접 할당하고 해제합니다 | malloc/free를 주의 깊게 사용하세요. C++의 RAII 패턴 |
| **버퍼 오버플로** | 배열에 대한 경계 검사가 없음 - 과거 버퍼 끝을 쓰기 쉬움 | strcpy 대신 strncpy를 사용하십시오. 컴파일러 경고 활성화 |
| **내장 OOP 없음** | 절차적 전용 - 클래스, 상속 또는 메소드 없음 | 구조체 + 함수 포인터를 사용하세요. 또는 C++로 전환 |
| **제한된 표준 라이브러리** | 최소한의 내장 기능 | 타사 라이브러리 또는 직접 작성 |
| **정의되지 않은 동작** | 많은 실수가 잘 컴파일되지만 예기치 않게 충돌이 발생함 | 살균제, 정적 분석기 사용 |
---

## 구문 기본 사항
### 기본 구조
모든 C 프로그램은`main()`에서 시작됩니다. 언어는 컴파일됩니다. 소스 코드는 컴파일러(GCC, Clang, MSVC)를 통해 기계어 코드가 됩니다.
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int add(int a, int b) {
    return a + b;
}

int main(void) {
    int result = add(3, 5);
    printf("Result: %d\n", result);
    return 0;
}
```

### 변수 및 유형
C는 정적으로 유형이 지정됩니다. 모든 변수에는 컴파일 타임에 알려진 고정 유형이 있습니다.
```c
int count = 42;              // 4 bytes (typically)
float pi = 3.14159f;         // 4 bytes
double precise = 3.14159;    // 8 bytes
char letter = 'A';           // 1 byte
long big = 1000000L;         // 4 or 8 bytes depending on platform

#define MAX_SIZE 1024
const float GRAVITY = 9.81f;

int numbers[5] = {1, 2, 3, 4, 5};
char name[] = "Hello";       // Size inferred: 6 bytes (includes \0)

struct Point {
    float x;
    float y;
};
struct Point p;
p.x = 3.0f;
p.y = 4.0f;
```

### 포인터
포인터는 C의 가장 강력하면서도 가장 오해를 많이 받는 기능입니다. 포인터는 메모리 주소를 보유합니다.
```c
int value = 42;
int *ptr = &value;     // ptr holds the address of value

printf("%d\n", *ptr);  // Dereference: prints 42
printf("%p\n", ptr);   // Prints the memory address

// Pointers and arrays are closely related
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;          // p points to arr[0]
printf("%d\n", *(p+2)); // prints 30 (arr[2])

// Dynamic memory allocation
int *dynamic = (int *)malloc(10 * sizeof(int));
if (dynamic == NULL) {
    fprintf(stderr, "Memory allocation failed\n");
    exit(1);
}
dynamic[0] = 100;
free(dynamic);   // Always free what you malloc!
dynamic = NULL;  // Prevent use-after-free
```

### 제어 흐름
```c
if (score >= 90) {
    grade = 'A';
} else if (score >= 80) {
    grade = 'B';
} else {
    grade = 'C';
}

for (int i = 0; i < 10; i++) {
    printf("%d ", i);
}

while (running) {
    process_input();
}

do {
    check_status();
} while (status == PENDING);

switch (command) {
    case START:   run();     break;
    case STOP:    halt();    break;
    case PAUSE:   suspend(); break;
    default:      printf("Unknown command\n");
}
```

### 함수와 스택
```c
// Pass by value (default)
void increment(int x) {
    x++;  // Only modifies the local copy
}

// Pass by pointer -- function can modify the original
void increment_ptr(int *x) {
    (*x)++;
}

// Variadic functions (like printf)
#include <stdarg.h>
double average(int count, ...) {
    va_list args;
    va_start(args, count);
    double sum = 0;
    for (int i = 0; i < count; i++) {
        sum += va_arg(args, double);
    }
    va_end(args);
    return sum / count;
}
```

---

## 메모리 레이아웃
```
+---------------------+ High addresses
|     Stack           | <- Local variables, function call frames
|       | grows       |   (automatically cleaned up when function returns)
+---------------------+
|       | grows       |
|      Heap           | <- malloc/calloc allocations
|                     |   (you must free() these manually)
+---------------------+
|  BSS segment        | <- Uninitialised global/static variables
+---------------------+
|  Data segment       | <- Initialised global/static variables
+---------------------+
|  Text segment       | <- Compiled machine code (read-only)
+---------------------+ Low addresses
```

| 지역 | 무엇이 거기에 가는가 | 평생 | 누가 관리하나요?
|---------|---|----------|---|
| **스택** | 지역 변수, 함수 매개변수 | 함수가 반환될 때까지 | 컴파일러(자동) |
| **힙** | malloc/calloc 할당 | free()를 호출할 때까지 | 당신(수동) |
| **데이터/BSS** | 전역 및 정적 변수 | 전체 프로그램 수명 | 컴파일러(자동) |
| **텍스트** | 기계코드 | 전체 프로그램 수명 | 읽기 전용 |
---

## 표준 라이브러리
| 헤더 | 목적 | 공통 기능 |
|---------|---------|----|
|  __보호됨_0__ | 입력/출력 | printf, scanf, fopen, fgets, fprintf |
|  __보호됨_1__ | 일반 유틸리티 | malloc, 무료, 종료, atoi, rand, qsort |
|  __보호됨_2__ | 문자열 작업 | strlen, strcpy, strncpy, strcmp, memcpy |
|  __보호됨_3__ | 수학 | 죄, cos, sqrt, pow, 팹, ceil, 바닥 |
|  __보호됨_4__ | 문자 분류 | isalpha, isdigit, toupper, tolower |
|  __보호됨_5__ | 날짜 및 시간 | 시간, 시계, difftime, strftime |
|  __보호_6__ | 어설션 디버깅 | 주장(조건) |
|  __보호_7__ | 오류 코드 | 오류, 오류, strerror |
---

## 고급 구문 및 패턴
### 전처리기 매크로
```c
// Safe macro with do-while wrapper
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ARRAY_LEN(arr) (sizeof(arr) / sizeof((arr)[0]))

#define SAFE_COPY(dst, src, size) do { \
    if ((size) > 0) {                  \
        strncpy((dst), (src), (size)-1); \
        (dst)[(size)-1] = '\0';        \
    }                                  \
} while(0)

// Conditional compilation
#ifdef DEBUG
    #define LOG(fmt, ...) fprintf(stderr, fmt "\n", ##__VA_ARGS__)
#else
    #define LOG(fmt, ...) ((void)0)
#endif

// Stringify and concatenation
#define STR(x) #x
#define CONCAT(a, b) a##b
```

### 함수 포인터 및 콜백
```c
#include <stdio.h>

// Function pointer type
typedef int (*Comparator)(const void *, const void *);

// Using function pointers for callbacks
int ascending(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int descending(const void *a, const void *b) {
    return (*(int*)b - *(int*)a);
}

void print_array(int *arr, int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main(void) {
    int data[] = {5, 2, 8, 1, 9, 3};
    int n = ARRAY_LEN(data);

    // qsort uses function pointers for custom comparison
    qsort(data, n, sizeof(int), ascending);
    print_array(data, n);  // 1 2 3 5 8 9

    qsort(data, n, sizeof(int), descending);
    print_array(data, n);  // 9 8 5 3 2 1

    return 0;
}
```

### 사용자 정의 오류 처리 패턴
```c
#include <stdio.h>
#include <stdlib.h>

// Error code enum
typedef enum {
    ERR_OK = 0,
    ERR_NULL_PTR = -1,
    ERR_ALLOC = -2,
    ERR_IO = -3,
    ERR_INVALID_ARG = -4,
} ErrorCode;

// Error string lookup
const char *error_string(ErrorCode code) {
    switch (code) {
        case ERR_OK:           return "Success";
        case ERR_NULL_PTR:     return "Null pointer";
        case ERR_ALLOC:        return "Allocation failed";
        case ERR_IO:           return "IO error";
        case ERR_INVALID_ARG:  return "Invalid argument";
        default:               return "Unknown error";
    }
}

// Error propagation pattern (goto cleanup)
ErrorCode process_file(const char *path) {
    FILE *fp = NULL;
    char *buffer = NULL;
    ErrorCode err = ERR_OK;

    if (path == NULL) { err = ERR_NULL_PTR; goto cleanup; }

    fp = fopen(path, "r");
    if (!fp) { err = ERR_IO; goto cleanup; }

    buffer = (char *)malloc(4096);
    if (!buffer) { err = ERR_ALLOC; goto cleanup; }

    // ... process file ...

cleanup:
    free(buffer);
    if (fp) fclose(fp);
    if (err != ERR_OK)
        fprintf(stderr, "Error: %s\n", error_string(err));
    return err;
}
```

---

## 동시성 및 병렬성
### POSIX 스레드(pthread)
```c
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

// Thread function
void *worker(void *arg) {
    int id = *(int *)arg;
    printf("Thread %d running\n", id);
    return NULL;
}

int main(void) {
    pthread_t threads[5];
    int ids[5];

    for (int i = 0; i < 5; i++) {
        ids[i] = i;
        pthread_create(&threads[i], NULL, worker, &ids[i]);
    }

    for (int i = 0; i < 5; i++) {
        pthread_join(threads[i], NULL);
    }
    return 0;
}
```

### 뮤텍스 및 공유 상태
```c
#include <pthread.h>

typedef struct {
    int count;
    pthread_mutex_t lock;
} Counter;

void *increment(void *arg) {
    Counter *c = (Counter *)arg;
    for (int i = 0; i < 100000; i++) {
        pthread_mutex_lock(&c->lock);
        c->count++;
        pthread_mutex_unlock(&c->lock);
    }
    return NULL;
}

int main(void) {
    Counter counter = {0, PTHREAD_MUTEX_INITIALIZER};
    pthread_t t1, t2;

    pthread_create(&t1, NULL, increment, &counter);
    pthread_create(&t2, NULL, increment, &counter);
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    printf("Final count: %d\n", counter.count);
    pthread_mutex_destroy(&counter.lock);
    return 0;
}
```

### C11 원자학과 스레드
```c
#include <stdatomic.h>
#include <threads.h>

atomic_int shared_count = 0;

int worker(void *arg) {
    for (int i = 0; i < 1000; i++) {
        atomic_fetch_add(&shared_count, 1);
    }
    return 0;
}

int main(void) {
    thrd_t t1, t2;
    thrd_create(&t1, worker, NULL);
    thrd_create(&t2, worker, NULL);
    thrd_join(t1, NULL);
    thrd_join(t2, NULL);
    printf("Count: %d\n", atomic_load(&shared_count));
    return 0;
}
```

---

## 프로젝트 구성 및 빌드 시스템
### 프로젝트 구조
```
my_project/
+-- CMakeLists.txt        # CMake build configuration
+-- Makefile              # Alternative: Make build
+-- src/
|   +-- main.c
|   +-- utils.c
|   +-- utils.h
|   +-- parser.c
|   +-- parser.h
+-- include/
|   +-- config.h
|   +-- types.h
+-- tests/
|   +-- test_utils.c
|   +-- test_parser.c
+-- lib/                  # Third-party libraries
+-- build/                # Build output (gitignored)
+-- .clang-format         # Code style configuration
+-- .clang-tidy           # Linter configuration
```

### CMakeLists.txt
```cmake
cmake_minimum_required(VERSION 3.20)
project(my_project VERSION 1.0.0 LANGUAGES C)

set(CMAKE_C_STANDARD 17)
set(CMAKE_C_STANDARD_REQUIRED ON)

# Compiler warnings
add_compile_options(-Wall -Wextra -Wpedantic)

# Source files
set(SOURCES
    src/main.c
    src/utils.c
    src/parser.c
)

# Main executable
add_executable(my_app ${SOURCES})
target_include_directories(my_app PRIVATE include)

# Link math library on Unix
if(UNIX)
    target_link_libraries(my_app m pthread)
endif()

# Release build optimisation
if(CMAKE_BUILD_TYPE STREQUAL "Release")
    target_compile_options(my_app PRIVATE -O2)
endif()

# Testing
enable_testing()
add_executable(test_utils tests/test_utils.c src/utils.c)
target_include_directories(test_utils PRIVATE include)
add_test(NAME UtilsTest COMMAND test_utils)
```

### 메이크파일
```makefile
CC = gcc
CFLAGS = -Wall -Wextra -std=c17 -Iinclude
LDFLAGS = -lm -lpthread

SRCS = src/main.c src/utils.c src/parser.c
OBJS = $(SRCS:.c=.o)
TARGET = my_app

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	find . -name "*.o" -delete
	find . -name "$(TARGET)" -delete

debug: CFLAGS += -g -DDEBUG -fsanitize=address
debug: clean all

.PHONY: all clean debug
```

### CI/CD 파이프라인(GitHub 작업)
```yaml
name: C CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  build:
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - run: cmake -B build -DCMAKE_BUILD_TYPE=Debug
      - run: cmake --build build
      - run: ctest --test-dir build --output-on-failure
```

---

## 테스트
### 간단한 프레임워크를 사용한 단위 테스트
```c
#include <stdio.h>
#include <assert.h>
#include "utils.h"

// Simple test macros
#define TEST(name) void name(void)
#define ASSERT_EQ(a, b) do { \
    if ((a) != (b)) { \
        fprintf(stderr, "FAIL: %s:%d: %d != %d\n", __FILE__, __LINE__, (a), (b)); \
        exit(1); \
    } \
} while(0)

#define ASSERT_STR_EQ(a, b) do { \
    if (strcmp((a), (b)) != 0) { \
        fprintf(stderr, "FAIL: %s:%d: \"%s\" != \"%s\"\n", __FILE__, __LINE__, (a), (b)); \
        exit(1); \
    } \
} while(0)

TEST(test_add) {
    ASSERT_EQ(add(2, 3), 5);
    ASSERT_EQ(add(-1, 1), 0);
    ASSERT_EQ(add(0, 0), 0);
}

TEST(test_string_trim) {
    char buf[64];
    strcpy(buf, "  hello  ");
    trim(buf);
    ASSERT_STR_EQ(buf, "hello");
}

int main(void) {
    test_add();
    printf("test_add passed\n");
    test_string_trim();
    printf("test_string_trim passed\n");
    printf("All tests passed!\n");
    return 0;
}
```

```bash
# Compile and run tests
gcc -Wall -o test_utils tests/test_utils.c src/utils.c -Iinclude
./test_utils

# Run with AddressSanitizer
gcc -fsanitize=address -g -o test_utils tests/test_utils.c src/utils.c -Iinclude
./test_utils
```

---

## 상호 운용성
### Python에서 C 호출(ctypes)
```c
// mathlib.c -- compile to shared library
// gcc -shared -fPIC -o libmathlib.so mathlib.c
int c_add(int a, int b) { return a + b; }
double c_sqrt(double x) {
    if (x < 0) return -1.0;
    // Newton's method
    double guess = x / 2.0;
    for (int i = 0; i < 100; i++)
        guess = (guess + x / guess) / 2.0;
    return guess;
}
```

```python
# Python side
import ctypes
lib = ctypes.CDLL("./libmathlib.so")
lib.c_add.argtypes = [ctypes.c_int, ctypes.c_int]
lib.c_add.restype = ctypes.c_int
print(lib.c_add(3, 5))  # 8
```

### 다른 언어에서 C 호출하기
| 언어 | 메커니즘 | 예 |
|----------|------------|---------|
| 파이썬 | ctypes, cffi |  __보호됨_0__ |
| 루비 | 바이올린 |  __보호됨_1__ |
| 자바 | JNI |  __보호됨_2__ |
| C++ | 외부 "C" |  __보호됨_3__ |
| 녹 | 외부 "C" + FFI |  __보호됨_4__ |
---

## 디자인 패턴
### 불투명 포인터(C의 Pimpl 관용구)
```c
// stack.h -- public interface (implementation hidden)
typedef struct Stack Stack;

Stack *stack_create(void);
void stack_destroy(Stack *s);
void stack_push(Stack *s, int value);
int stack_pop(Stack *s);
int stack_is_empty(const Stack *s);

// stack.c -- private implementation
struct Stack {
    int *data;
    int top;
    int capacity;
};

Stack *stack_create(void) {
    Stack *s = malloc(sizeof(Stack));
    s->data = malloc(16 * sizeof(int));
    s->top = -1;
    s->capacity = 16;
    return s;
}

void stack_push(Stack *s, int value) {
    if (++s->top == s->capacity) {
        s->capacity *= 2;
        s->data = realloc(s->data, s->capacity * sizeof(int));
    }
    s->data[s->top] = value;
}
```

### 가상 테이블(C의 OOP)
```c
typedef struct {
    void (*speak)(const void *self);
    void (*destroy)(void *self);
} AnimalVTable;

typedef struct {
    const AnimalVTable *vtable;
    char name[64];
} Animal;

void animal_speak(const Animal *a) { a->vtable->speak(a); }

// Dog implementation
typedef struct { Animal base; int trick_count; } Dog;
void dog_speak(const void *self) { printf("Woof!\n"); }
void dog_destroy(void *self) { free(self); }

static const AnimalVTable dog_vtable = { dog_speak, dog_destroy };
Animal *dog_create(const char *name) {
    Dog *d = calloc(1, sizeof(Dog));
    d->base.vtable = &dog_vtable;
    strncpy(d->base.name, name, 63);
    return (Animal *)d;
}
```

---

## 성능 및 최적화
### 프로파일링 도구
```bash
# GCC profiling with gprof
gcc -pg -O2 -o my_app main.c
./my_app
gprof my_app gmon.out > profile.txt

# perf (Linux)
perf record -g ./my_app
perf report

# Valgrind for cache profiling
valgrind --tool=cachegrind ./my_app

# Memory leak detection
valgrind --tool=memcheck --leak-check=full ./my_app

# AddressSanitizer (compile-time)
gcc -fsanitize=address,undefined -g -o my_app main.c
```

### 최적화 기술
```c
// Struct packing to reduce memory
#pragma pack(push, 1)
typedef struct {
    uint8_t type;
    uint32_t id;
    uint16_t value;
} PackedRecord;  // 7 bytes instead of 12 (with padding)
#pragma pack(pop)

// Cache-friendly access patterns (row-major order)
for (int i = 0; i < rows; i++)
    for (int j = 0; j < cols; j++)
        matrix[i][j] = 0;  // Sequential memory access

// Branch prediction hints
#define LIKELY(x)   __builtin_expect(!!(x), 1)
#define UNLIKELY(x) __builtin_expect(!!(x), 0)

if (LIKELY(ptr != NULL)) {
    // Fast path
}
```

---

## 배포
### 크로스 컴파일
```bash
# Cross-compile for ARM (embedded)
arm-none-eabi-gcc -mcpu=cortex-m4 -o firmware.elf main.c

# Cross-compile for Windows from Linux
x86_64-w64-mingw32-gcc -o my_app.exe main.c

# Static linking (no shared library dependencies)
gcc -static -o my_app main.c
```

### 도커 배포
```dockerfile
FROM gcc:13 AS builder
WORKDIR /app
COPY src/ ./
RUN gcc -O2 -Wall -o my_app main.c utils.c

FROM debian:bookworm-slim
COPY --from=builder /app/my_app /usr/local/bin/my_app
CMD ["my_app"]
```

---

## 일반적인 패턴 및 관용어
```c
// Safe string copy (prevents buffer overflow)
#define SAFE_COPY(dst, src, size) do { \
    if ((size) > 0) {                  \
        strncpy((dst), (src), (size)-1); \
        (dst)[(size)-1] = '\0';        \
    }                                  \
} while(0)

// Macro for array length
#define ARRAY_LEN(arr) (sizeof(arr) / sizeof((arr)[0]))

// Typedef for cleaner struct usage
typedef struct {
    float x, y, z;
} Vec3;

// Linked list node
typedef struct Node {
    int data;
    struct Node *next;
} Node;
```

---

## 컴파일 및 도구
```bash
gcc -Wall -Wextra -o myprogram myprogram.c      # Basic compile
gcc -g -Wall -o myprogram myprogram.c            # With debug symbols
gcc -O2 -Wall -o myprogram myprogram.c           # With optimisation
gcc -std=c17 -Wall -o myprogram myprogram.c      # Specific standard
make          # Runs the Makefile
make clean    # Removes build artifacts
```

| 도구 | 목적 |
|------|---------|
| **GCC / 클랭** | 컴파일러 |
| **만들기 / CMake** | 시스템 구축 |
| **GDB** | 디버거 |
| **발그린드** | 메모리 오류 감지기(누수, 잘못된 액세스) |
| **AddressSanitizer** | 컴파일 타임 메모리 검사 |
| **cpp체크** | 정적 분석 |
| ** 소리 형식 ** | 코드 서식 |
---

## C를 사용해야 하는 경우
| 시나리오 | 왜 C인가 | 더 나은 대안 |
|----------|-------|------|
| 운영 체제 | 직접 하드웨어 액세스, 런타임 오버헤드 없음 | -- |
| 임베디드 시스템/마이크로컨트롤러 | 최소한의 설치 공간, 무엇이든 실행 가능 | 안전이 중요한 임베디드용 Rust |
| 데이터베이스 엔진 | 최대 성능, 전체 메모리 제어 | -- |
| 컴파일러와 통역사 | 빠르고, 휴대 가능하며, 이해하기 쉽습니다 | 대규모 컴파일러 프로젝트를 위한 C++ |
| 장치 드라이버 | 대부분의 OS 커널 API에 필요 | -- |
| 성능이 중요한 라이브러리 | 최적에 가까운 속도 | 메모리 안전성을 보장하는 Rust |
| 일반 애플리케이션 개발 | 수작업이 너무 많음 | 파이썬, 자바, Go, C# |
| 웹 개발 | 완전히 잘못된 도구 | 자바스크립트, 바둑, Python |
| 데이터 과학 / ML | 이에 대한 생태계는 없습니다 | 파이썬, R, 줄리아 |
---

## C 표준
| 표준 | 연도 | 주요 추가사항 |
|------------|------|---------------|
| C89/C90 | 1989/1990 | 원본 ANSI C - 여전히 기준 |
| C99 | 1999 | // 주석, 부울 유형, 가변 길이 배열, 인라인, stdint.h |
| C11 | 2011 | 원자적 연산, 스레드, 익명 구조체, _Generic |
| C17 | 2018 | 버그 수정 및 설명(새로운 기능 없음) |
| C23 | 2024년 | nullptr, typeof, constexpr, 향상된 전처리기 |
대부분의 프로덕션 코드는 C11 또는 C17을 대상으로 합니다. C23은 현대적인 편리함을 제공하지만 채택에는 시간이 걸립니다.
---

## 요약
C는 현대 컴퓨팅의 기반이다. 최소한의 추상화 오버헤드로 하드웨어를 최대한 제어할 수 있습니다. 해당 제어 비용은 책임입니다. 메모리를 관리하고, 범위를 확인하고, 오류를 직접 처리합니다. 시스템 프로그래밍, 임베디드 개발, 성능 및 리소스 제약이 중요한 모든 곳에서 C는 타의 추종을 불허합니다. 그 밖의 모든 경우에는 일반적으로 C를 기반으로 구축된 고급 언어가 더 생산적인 선택입니다.