<!--
---
# Metadata
title: "C"
description: "Comprehensive reference for the C programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
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

-->
#C
C 是一種通用的過程式設計語言，由丹尼斯·里奇 (Dennis Ritchie) 在 1969 年至 1973 年間在貝爾實驗室創建。它旨在實現 Unix 作業系統，並且在 50 多年後仍然是使用最廣泛的程式語言之一。 C 提供低階記憶體存取、最小標準庫以及到機器指令的清晰映射——使其成為建立大多數現代運算的基礎。
C 是作業系統（Linux、Windows 核心、macOS）、嵌入式系統、資料庫引擎（SQLite、PostgreSQL）、編譯器（Python 的 CPython、Ruby 的 MRI）以及幾乎所有其他程式語言執行時期背後的語言。理解 C 就是理解计算机实际上是如何工作的。
---

## 為什麼 C 很重要
- **接近硬體**：C 與機器碼緊密對應。沒有垃圾收集器，沒有運行時開銷，沒有隱藏分配。
- **無所不在**：從微控制器到超級計算機，C 語言無所不在。
- **計算基礎**：Linux、Windows、macOS 核心、Python 解譯器、SQLite、Git－全部用 C 寫。
- **效能**：接近最佳的執行速度，完全控制記憶體佈局。
- **影響**：C 的語法和概念（指標、陣列、結構體、函數）塑造了 C++、Java、C#、JavaScript、Go、Rust 以及隨後的大多數語言。
## 權衡
|限制|詳情 |典型解決方法|
|------------|---------|--------------------|
| **手動記憶體管理** |沒有垃圾收集器－您自己分配和釋放記憶體|謹慎使用malloc/free; C++ 中的 RAII 模式 |
| **緩衝區溢位** |數組上沒有邊界檢查－很容易寫入超過緩衝區結束的內容 |使用strncpy代替strcpy；啟用編譯器警告 |
| **沒有內建的OOP** |僅限過程－無類別、繼承或方法 |使用結構體+函數指標；或切換到 C++ |
| **標準函式庫有限** |最少的內建功能 |第三方函式庫或自行寫 |
| **未定義的行為** |許多錯誤編譯正常但無法預料地崩潰 |使用消毒劑、靜電分析儀|
---

## 文法基礎知識
### 基本結構
每個 C 程式都從`main()`開始。語言是編譯的－原始碼透過編譯器（GCC、Clang、MSVC）變成機器碼。
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

### 變數和類型
C 是靜態型別的－每個變數都有一個在編譯時已知的固定型別。
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

### 指針
指標是 C 最強大也是最容易被誤解的功能。指標保存著記憶體位址。
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

### 控制流程
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

### 函數和堆疊
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

## 記憶體佈局
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

|地區 |那裡有什麼？終身|誰來管理？
|--------------------|----------------|----------|----------------|
| **堆疊** |局部變數、函數參數|直到函數返回 |編譯器（自動）|
| **堆** | malloc/calloc 分配 |直到你呼叫 free() |你（手冊）|
| **資料/BSS** |全域與靜態變數|整個程式生命週期|編譯器（自動）|
| **文字** |機器碼|整個程式生命週期|唯讀 |
---

## 標準庫
|標題|目的|常用功能|
|--------|---------|-----------------|
| `<stdio.h>`|输入/输出 | printf、scanf、fopen、fgets、fprintf | printf、scanf、fopen、fgets、fprintf |
| `<stdlib.h>`|一般公用事业| malloc、自由、退出、atoi、rand、qsort |
| `<string.h>`|字符串操作| strlen、strcpy、strncpy、strcmp、memcpy |
| `<math.h>`|数学| sin、cos、sqrt、pow、fabs、ceil、floor |
| `<ctype.h>`|人物分类| isalpha、isdigit、toupper、tolower | isalpha、isdigit、toupper、tolower |
| `<time.h>`|日期和时间 |时间、时钟、difftime、strftime |
| `<assert.h>`|调试断言|断言（条件）|
| `<errno.h>`|错误代码 | errno、perror、strerror |
---

## 進階語法和模式
### 預處理器宏
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

### 函數指標和回調
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

### 自訂錯誤處理模式
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

## 並發與平行
### POSIX 執行緒（pthreads）
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

### 互斥與共享狀態
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

### C11 原子和執行緒
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

## 專案配置與建置系統
### 專案結構
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

### 產生文件
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

### CI/CD 管道 (GitHub Actions)
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

## 測試
### 使用簡單框架進行單元測試
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

## 互通性
### 從 Python 呼叫 C (ctypes)
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

### 從其他語言呼叫 C
|語言 |機制|範例|
|----------|------------|---------|
|蟒蛇 | ctypes、cffi |`ctypes.CDLL("./lib.so")`|
|紅寶石 |小提琴|`Fiddle.dlopen("./lib.so")`|
| 爪哇 | JNI |`System.loadLibrary("mylib")`|
| C++ |外部「C」 |`extern "C" void my_func();`|
|鐵鏽|外部「C」+ FFI |`extern "C" { fn my_func(); }`|
---

## 設計模式
### 不透明指標（C 語言中的 Pimpl 慣用法）
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

### 虛擬表（C 中的 OOP）
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

## 效能與最佳化
### 分析工具
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

### 優化技術
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

## 部署
### 交叉編譯
```bash
# Cross-compile for ARM (embedded)
arm-none-eabi-gcc -mcpu=cortex-m4 -o firmware.elf main.c

# Cross-compile for Windows from Linux
x86_64-w64-mingw32-gcc -o my_app.exe main.c

# Static linking (no shared library dependencies)
gcc -static -o my_app main.c
```

### Docker 部署
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

## 常見模式和慣用語
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

## 編譯和工具
```bash
gcc -Wall -Wextra -o myprogram myprogram.c      # Basic compile
gcc -g -Wall -o myprogram myprogram.c            # With debug symbols
gcc -O2 -Wall -o myprogram myprogram.c           # With optimisation
gcc -std=c17 -Wall -o myprogram myprogram.c      # Specific standard
make          # Runs the Makefile
make clean    # Removes build artifacts
```

|工具|目的|
|------|---------|
| **海湾合作委员会/叮当** |编译器 |
| **制作/CMake** |构建系统|
| **GDB** |偵錯器|
| **瓦尔格林德** |内存错误检测器（泄漏、无效访问）|
| **地址消毒剂** |编译时内存检查|
| **cpp检查** |静态分析|
| **clang 格式** |代码格式化 |
---

## 何時使用 C
|場景|為什麼選擇 C |更好的選擇|
|----------|------|--------------------|
|作業系統 |直接硬體訪問，無運行時開銷 | --|
|嵌入式系統/微控制器|佔地面積最小，可在任何物體上運行 | Rust 用於安全關鍵型嵌入式 |
|資料庫引擎|最高效能，完全記憶體控制| --|
|編譯器與解釋器|快速、便攜、易於理解 |用於大型編譯器專案的 C++ |
|裝置驅動程式|大多數作業系統核心 API 都需要 | --|
|效能關鍵庫 |接近最佳速度 | Rust 保證記憶體安全 |
|通用應用開發 |太多的體力勞動 | Python、Java、Go、C# |
|網頁開發|完全錯誤的工具| JavaScript、Go、Python |
|資料科學/機器學習 |沒有適合這個的生態系統| Python、R、茱莉亞 |
---

## C 標準
|标准|年份|关键补充|
|----------|------|--------------|
| C89/C90 | 1989/1990 |最初的 ANSI C——仍然是基線 |
| C99 | C99 1999 | // 註解、bool 型別、變長數組、內聯、stdint.h |
| C11 | 2011 |原子操作、線程、匿名結構、_Generic |
| C17 | C17 2018 |錯誤修復與澄清（無新功能）|
| C23 | C23 2024 | 2024 nullptr、typeof、constexpr、改良的預處理器 |
大多數生產代碼都以 C11 或 C17 為目標。 C23 帶來了現代便利，但採用需要時間。
---

## 綜合問答
### Q1：C 中指標和陣列有什麼差別？
**答：** 陣列和指標相關但又不同。數組是一個連續的記憶體區塊，具有編譯時已知的固定大小。指標是保存記憶體位址的變數。當傳遞給函數時，數組會衰減為指針，但`sizeof(array)`給出總大小，而`sizeof(pointer)`僅給出指針大小（4 或 8 位元組）。陣列名稱是不可修改的左值 - 您不能執行`arr++`。
```c
int arr[5] = {1, 2, 3, 4, 5};
int *ptr = arr;       // Array decays to pointer to first element

printf("%zu\n", sizeof(arr));   // 20 (5 * sizeof(int))
printf("%zu\n", sizeof(ptr));   // 8 (on 64-bit system)

// arr++;        // Error: array is not a modifiable lvalue
ptr++;           // OK: pointer arithmetic

// They behave the same for indexing
printf("%d\n", arr[2]);   // 3
printf("%d\n", ptr[2]);   // 3
printf("%d\n", *(arr + 2)); // 3 — pointer arithmetic
```

### Q2：如何正確管理記憶體並避免洩漏？
**A:** 每個`malloc`/`calloc`必須有一個對應的`free`。常見錯誤：忘記釋放（洩漏）、釋放兩次（未定義行為）、釋放後使用記憶體（釋放後使用）以及不檢查`malloc`回傳值（失敗時為 NULL）。最佳實務：在相同模組中分配和釋放，使用「goto cleanup」模式進行錯誤處理，並始終將釋放的指標設為 NULL。
```c
// Proper allocation pattern with cleanup
char *load_file(const char *path) {
    FILE *f = fopen(path, "r");
    if (!f) return NULL;

    fseek(f, 0, SEEK_END);
    long size = ftell(f);
    rewind(f);

    char *buf = malloc(size + 1);
    if (!buf) {
        fclose(f);
        return NULL;
    }

    if (fread(buf, 1, size, f) != (size_t)size) {
        free(buf);
        buf = NULL;   // Prevent dangling pointer
        fclose(f);
        return NULL;
    }
    buf[size] = '\0';

    fclose(f);
    return buf;
}

// Usage
char *data = load_file("config.txt");
if (data) {
    process(data);
    free(data);
    data = NULL;  // Defensive: catch use-after-free
}
```

### Q3：C 中錯誤處理的最佳實務是什麼？
**A:** C 也不例外。錯誤處理使用傳回值（錯誤代碼、NULL 指標、負值）。標準模式：函數在失敗時傳回狀態碼或 NULL，並為系統呼叫設定 `errno`。使用“goto cleanup”模式來清除錯誤時的資源。請務必檢查`malloc`、`fopen`的回傳值以及其他可能失敗的函數。
```c
#include <errno.h>
#include <string.h>

// Error code pattern
typedef enum {
    OK = 0,
    ERR_NULL_PTR = -1,
    ERR_NOT_FOUND = -2,
    ERR_IO = -3,
} Status;

Status read_config(const char *path, Config *out) {
    if (!path || !out) return ERR_NULL_PTR;

    FILE *f = fopen(path, "r");
    if (!f) {
        fprintf(stderr, "Cannot open %s: %s\n", path, strerror(errno));
        return ERR_IO;
    }

    // ... parse config ...

    fclose(f);
    return OK;
}

// Usage
Config cfg;
Status s = read_config("app.conf", &cfg);
if (s != OK) {
    fprintf(stderr, "Config error: %d\n", s);
    exit(EXIT_FAILURE);
}
```

### Q4：結構體、聯合體和位元域在記憶體佈局上有何不同？
**A:** 結構按順序排列成員，並可能使用填充以進行對齊。聯合覆蓋同一記憶體位置的所有成員－大小等於最大成員。位域将多个值打包到一个整数中。結構用於異質數據，聯合用於類型雙關或僅在一個字段處於活動狀態時節省空間，而位元字段用於緊湊標誌存儲。
```c
// Struct — sequential layout with padding
struct Point {
    double x;  // offset 0, 8 bytes
    double y;  // offset 8, 8 bytes
};               // sizeof = 16

// Union — overlapping storage
union Value {
    int    i;
    float  f;
    char   s[8];
};               // sizeof = 8 (largest member)

// Tagged union — safe union usage
typedef enum { TYPE_INT, TYPE_FLOAT, TYPE_STRING } ValueType;

struct TaggedValue {
    ValueType type;
    union {
        int   i;
        float f;
        char  s[32];
    } data;
};

// Bitfields — pack flags into minimal space
struct Flags {
    unsigned int read    : 1;  // 1 bit
    unsigned int write   : 1;
    unsigned int execute : 1;
    unsigned int sticky  : 1;
    unsigned int reserved : 4;  // 4 bits padding
};  // Total: 1 byte instead of 4 ints
```

### Q5：什麼是函數指針，什麼時候應該使用它們？
**A:** 函數指標儲存函數的位址並啟用回呼、多型性和外掛架構。它們是 C 處理高階函數的方法的基礎（例如`qsort`、`bsearch`）。使用語法聲明它們：`return_type (*name)(parameter_types)`。
```c
// Function pointer declaration
int (*operation)(int, int);

int add(int a, int b) { return a + b; }
int mul(int a, int b) { return a * b; }

operation = add;
printf("%d\n", operation(3, 4));  // 7
operation = mul;
printf("%d\n", operation(3, 4));  // 12

// Callback pattern — qsort
int compare_ints(const void *a, const void *b) {
    int ia = *(const int *)a;
    int ib = *(const int *)b;
    return (ia > ib) - (ia < ib);
}

int arr[] = {5, 2, 8, 1, 9, 3};
qsort(arr, 6, sizeof(int), compare_ints);
// arr is now {1, 2, 3, 5, 8, 9}

// Strategy pattern
struct Strategy {
    void (*init)(void);
    void (*process)(const char *data);
    void (*cleanup)(void);
};

void run_pipeline(const struct Strategy *s, const char *data) {
    s->init();
    s->process(data);
    s->cleanup();
}
```

---

## 解決問題的思路
### 問題 1：實作動態陣列（向量）
**問題陳述：** 在 C 中實作動態數組，在新增元素時會自動增長，支援 O(1) 攤銷追加，並提供適當的清理。这是 C++`std::vector`的 C 等效项。
**第 1 步 — 了解問題：**
動態數組需要：(1) 堆分配的緩衝區，(2) 追蹤大小（已使用的元素）和容量（分配的槽），(3) 當大小達到容量時重新分配，(4) 適當的記憶體清理。 2x 的成長因子提供 O(1) 攤銷追加。
**第 2 步 — 確定方法：**
- 使用`malloc`進行初步分配，使用`realloc`進行成長。
- 將資料指標、大小和容量儲存在結構中。
-`size == capacity`時容量加倍。
- 提供`push`、`pop`、`get`、`set`和`free`操作。
**第 3 步 — 實施解決方案：**
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int    *data;
    size_t  size;
    size_t  capacity;
} IntVec;

// Initialize with default capacity
void vec_init(IntVec *v, size_t initial_capacity) {
    v->data = malloc(initial_capacity * sizeof(int));
    if (!v->data) { perror("malloc"); exit(EXIT_FAILURE); }
    v->size = 0;
    v->capacity = initial_capacity;
}

// Ensure capacity for at least one more element
static void vec_grow(IntVec *v) {
    if (v->size < v->capacity) return;
    size_t new_cap = v->capacity * 2;
    int *new_data = realloc(v->data, new_cap * sizeof(int));
    if (!new_data) { perror("realloc"); exit(EXIT_FAILURE); }
    v->data = new_data;
    v->capacity = new_cap;
}

// Append element — O(1) amortized
void vec_push(IntVec *v, int value) {
    vec_grow(v);
    v->data[v->size++] = value;
}

// Remove last element — O(1)
int vec_pop(IntVec *v) {
    if (v->size == 0) { fprintf(stderr, "pop from empty vector\n"); exit(EXIT_FAILURE); }
    return v->data[--v->size];
}

// Access element
int vec_get(const IntVec *v, size_t index) {
    if (index >= v->size) { fprintf(stderr, "index %zu out of bounds (size %zu)\n", index, v->size); exit(EXIT_FAILURE); }
    return v->data[index];
}

// Free all memory
void vec_free(IntVec *v) {
    free(v->data);
    v->data = NULL;
    v->size = v->capacity = 0;
}

// Usage
int main(void) {
    IntVec v;
    vec_init(&v, 4);

    for (int i = 0; i < 100; i++) {
        vec_push(&v, i * i);
    }

    printf("Size: %zu, Capacity: %zu\n", v.size, v.capacity);
    printf("Last: %d\n", vec_get(&v, v.size - 1));  // 9801

    vec_free(&v);
    return 0;
}
```

**第 4 步 — 驗證與最佳化：**
- 攤銷 O(1) 推送：加倍意味著每個元素總共最多複製 O(log n) 次。
-`vec_get`和`vec_pop`中的邊界檢查可以儘早捕獲錯誤 - 這在沒有運行時安全網的 C 語言中至關重要。
- 記憶體：從容量4開始推入100次後，容量達到128（4→8→16→32→64→128）。
- 生產：成長完成後使用 `shrink_to_fit`（重新分配到精確大小）以回收未使用的記憶體。
### 問題 2：建立一個簡單的雜湊表
**問題陳述：** 使用單獨的連結來實現具有字串鍵和整數值的雜湊表以解決衝突。支援插入、尋找、刪除操作。
**第 1 步 — 了解問題：**
哈希表透過哈希函數將鍵映射到數組索引。衝突（不同的鍵映射到相同的索引）透過單獨的連結來解決：每個儲存桶都是條目的連結列表。我們需要：雜湊函數、插入、尋找、刪除和清理。
**第 2 步 — 確定方法：**
- 使用 FNV-1a 雜湊來良好地指派字串鍵。
- 桶指針數組（鍊錶頭）。
- 負載係數追蹤；當負載因子超過閾值時調整大小。
- 所有操作平均為 O(1)，最壞情況為 O(n)。
**第 3 步 — 實施解決方案：**
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INITIAL_BUCKETS 64
#define LOAD_FACTOR_THRESHOLD 0.75

typedef struct Entry {
    char *key;
    int   value;
    struct Entry *next;
} Entry;

typedef struct {
    Entry  **buckets;
    size_t   num_buckets;
    size_t   size;
} HashMap;

// FNV-1a hash function
static unsigned long hash(const char *key) {
    unsigned long h = 14695981039346656037ULL;
    while (*key) {
        h ^= (unsigned char)*key++;
        h *= 1099511628211ULL;
    }
    return h;
}

void hashmap_init(HashMap *m) {
    m->num_buckets = INITIAL_BUCKETS;
    m->buckets = calloc(m->num_buckets, sizeof(Entry *));
    m->size = 0;
}

// Insert or update
void hashmap_put(HashMap *m, const char *key, int value) {
    size_t idx = hash(key) % m->num_buckets;

    // Check if key already exists
    for (Entry *e = m->buckets[idx]; e; e = e->next) {
        if (strcmp(e->key, key) == 0) {
            e->value = value;
            return;
        }
    }

    // New entry — prepend to bucket
    Entry *entry = malloc(sizeof(Entry));
    entry->key = strdup(key);
    entry->value = value;
    entry->next = m->buckets[idx];
    m->buckets[idx] = entry;
    m->size++;
}

// Lookup — returns 1 if found, 0 if not
int hashmap_get(const HashMap *m, const char *key, int *out_value) {
    size_t idx = hash(key) % m->num_buckets;
    for (Entry *e = m->buckets[idx]; e; e = e->next) {
        if (strcmp(e->key, key) == 0) {
            *out_value = e->value;
            return 1;
        }
    }
    return 0;
}

// Delete — returns 1 if removed, 0 if not found
int hashmap_remove(HashMap *m, const char *key) {
    size_t idx = hash(key) % m->num_buckets;
    Entry **pp = &m->buckets[idx];

    while (*pp) {
        if (strcmp((*pp)->key, key) == 0) {
            Entry *to_free = *pp;
            *pp = to_free->next;
            free(to_free->key);
            free(to_free);
            m->size--;
            return 1;
        }
        pp = &(*pp)->next;
    }
    return 0;
}

// Cleanup
void hashmap_free(HashMap *m) {
    for (size_t i = 0; i < m->num_buckets; i++) {
        Entry *e = m->buckets[i];
        while (e) {
            Entry *next = e->next;
            free(e->key);
            free(e);
            e = next;
        }
    }
    free(m->buckets);
    m->buckets = NULL;
    m->size = m->num_buckets = 0;
}

// Usage
int main(void) {
    HashMap m;
    hashmap_init(&m);

    hashmap_put(&m, "alice", 95);
    hashmap_put(&m, "bob", 87);
    hashmap_put(&m, "charlie", 92);

    int score;
    if (hashmap_get(&m, "alice", &score)) {
        printf("Alice: %d\n", score);  // Alice: 95
    }

    hashmap_remove(&m, "bob");
    hashmap_free(&m);
    return 0;
}
```

**第 4 步 — 驗證與最佳化：**
- 插入/尋找/刪除的平均 O(1)，具有良好的雜湊函數和合理的負載因子。
- FNV-1a 以最少的計算提供出色的字串鍵分佈。
-`hashmap_remove`中的指標到指標技術 (`Entry **pp`) 可以優雅地處理列表頭和中間列表刪除，無需特殊情況。
- 生產：當負載因子超過閾值時添加重新哈希。使用開放尋址（線性探測）以獲得更好的快取效能。
### 問題 3：為生產者-消費者實現環形緩衝區
**問題陳述：** 用C實現一個無鎖的單生產者單消費者環形緩衝區，用於高性能線程間通信，而無需在運行過程中動態分配。
**第 1 步 — 了解問題：**
環形緩衝區（循環緩衝區）使用具有讀取和寫入索引的固定大小數組。當緩衝區已滿時，寫入器會阻塞或覆寫。對於SPSC（單一生產者單一消費者），我們可以使用原子操作而不是鎖來獲得最大吞吐量。
**第 2 步 — 確定方法：**
- 初始化時分配一次固定大小的陣列。
- `head`（讀取位置）和 `tail`（寫入位置）作為原子索引。
- 製作人推進`tail`；消費者進步`head`。
-`head == tail`時緩衝區為空；當`(tail + 1) % capacity == head`已滿時。
- 使用具有適當記憶體排序的 C11 原子。
**第 3 步 — 實施解決方案：**
```c
#include <stdio.h>
#include <stdatomic.h>
#include <stdlib.h>
#include <string.h>
#include <threads.h>

typedef struct {
    int              *buffer;
    size_t            capacity;  // Must be power of 2
    atomic_size_t     head;      // Consumer reads from here
    atomic_size_t     tail;      // Producer writes to here
} RingBuffer;

void ring_init(RingBuffer *rb, size_t capacity) {
    // Round up to power of 2 for efficient modulo
    size_t cap = 1;
    while (cap < capacity) cap <<= 1;
    rb->buffer = malloc(cap * sizeof(int));
    rb->capacity = cap;
    atomic_store(&rb->head, 0);
    atomic_store(&rb->tail, 0);
}

// Producer: try to push an item. Returns 1 on success, 0 if full.
int ring_push(RingBuffer *rb, int value) {
    size_t tail = atomic_load_explicit(&rb->tail, memory_order_relaxed);
    size_t next_tail = (tail + 1) & (rb->capacity - 1);  // Fast modulo

    if (next_tail == atomic_load_explicit(&rb->head, memory_order_acquire)) {
        return 0;  // Buffer full
    }

    rb->buffer[tail] = value;
    atomic_store_explicit(&rb->tail, next_tail, memory_order_release);
    return 1;
}

// Consumer: try to pop an item. Returns 1 on success, 0 if empty.
int ring_pop(RingBuffer *rb, int *out) {
    size_t head = atomic_load_explicit(&rb->head, memory_order_relaxed);

    if (head == atomic_load_explicit(&rb->tail, memory_order_acquire)) {
        return 0;  // Buffer empty
    }

    *out = rb->buffer[head];
    atomic_store_explicit(&rb->head, (head + 1) & (rb->capacity - 1),
                          memory_order_release);
    return 1;
}

void ring_free(RingBuffer *rb) {
    free(rb->buffer);
    rb->buffer = NULL;
}

// Producer thread
int producer_thread(void *arg) {
    RingBuffer *rb = arg;
    for (int i = 0; i < 1000000; i++) {
        while (!ring_push(rb, i)) {
            // Spin — buffer full
            thrd_yield();
        }
    }
    return 0;
}

// Consumer thread
int consumer_thread(void *arg) {
    RingBuffer *rb = arg;
    long long sum = 0;
    int count = 0;
    int val;
    while (count < 1000000) {
        if (ring_pop(rb, &val)) {
            sum += val;
            count++;
        } else {
            thrd_yield();  // Spin — buffer empty
        }
    }
    printf("Consumed %d items, sum = %lld\n", count, sum);
    return 0;
}
```

**第 4 步 — 驗證與最佳化：**
- 無鎖：只有原子操作－沒有互斥體，沒有上下文切換。
- 記憶體排序：寫入時`release`確保資料在索引更新之前可見；讀取時的`acquire`確保我們在讀取索引後看到資料。
- 2 次方容量：啟用`& (capacity - 1)`而不是`% capacity`— 速度明顯更快。
- 吞吐量：在現代硬體上每秒數十億次操作。
- 生產：在`head`和`tail`之間添加填充，以防止錯誤共享（每個都在其自己的快取行上）。
---

＃＃ 概括
C 是現代計算的基石。它使您能夠以最小的抽象開銷最大程度地控制硬體。這種控制的成本就是責任——您自己管理記憶體、檢查邊界和處理錯誤。對於系統程式設計、嵌入式開發以及任何效能和資源限制很重要的地方，C 仍然是無與倫比的。對於其他一切，建立在 C 之上的高階語言通常是更有效率的選擇。