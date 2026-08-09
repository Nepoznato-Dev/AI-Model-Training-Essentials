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
C 是一种通用的过程式编程语言，由丹尼斯·里奇 (Dennis Ritchie) 在 1969 年至 1973 年间在贝尔实验室创建。它旨在实现 Unix 操作系统，并且在 50 多年后仍然是使用最广泛的编程语言之一。 C 提供低级内存访问、最小标准库以及到机器指令的清晰映射——使其成为构建大多数现代计算的基础。
C 是操作系统（Linux、Windows 内核、macOS）、嵌入式系统、数据库引擎（SQLite、PostgreSQL）、编译器（Python 的 CPython、Ruby 的 MRI）以及几乎所有其他编程语言运行时背后的语言。理解 C 就是理解计算机实际上是如何工作的。
---

## 为什么 C 很重要
- **接近硬件**：C 与机器代码紧密对应。没有垃圾收集器，没有运行时开销，没有隐藏分配。
- **无处不在**：从微控制器到超级计算机，C 语言无处不在。
- **计算基础**：Linux、Windows、macOS 内核、Python 解释器、SQLite、Git——全部用 C 编写。
- **性能**：接近最佳的执行速度，完全控制内存布局。
- **影响**：C 的语法和概念（指针、数组、结构体、函数）塑造了 C++、Java、C#、JavaScript、Go、Rust 以及随后的大多数语言。
## 权衡
|限制|详情 |典型解决方法|
|------------|---------|--------------------|
| **手动内存管理** |没有垃圾收集器——您自己分配和释放内存|谨慎使用malloc/free； C++ 中的 RAII 模式 |
| **缓冲区溢出** |数组上没有边界检查——很容易写入超过缓冲区结束的内容 |使用strncpy代替strcpy；启用编译器警告 |
| **没有内置的OOP** |仅限过程——无类、继承或方法 |使用结构体+函数指针；或切换到 C++ |
| **标准库有限** |最少的内置功能 |第三方库或自己编写|
| **未定义的行为** |许多错误编译正常但崩溃不可预知使用消毒剂、静电分析仪|
---

## 语法基础知识
### 基本结构
每个 C 程序都从`main()`开始。该语言是编译的——源代码通过编译器（GCC、Clang、MSVC）变成机器代码。
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

### 变量和类型
C 是静态类型的——每个变量都有一个在编译时已知的固定类型。
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

### 指针
指针是 C 最强大也是最容易被误解的功能。指针保存着内存地址。
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

### 函数和堆栈
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

## 内存布局
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

|地区 |那里有什么？终身|谁来管理？
|--------------------|----------------|----------|----------------|
| **堆栈** |局部变量、函数参数|直到函数返回 |编译器（自动）|
| **堆** | malloc/calloc 分配 |直到你调用 free() |你（手册）|
| **数据/BSS** |全局和静态变量|整个程序生命周期 |编译器（自动）|
| **文字** |机器码|整个程序生命周期 |只读|
---

## 标准库
|标题 |目的|常用功能|
|--------|---------|-----------------|
|  __受保护_0__ |输入/输出| printf、scanf、fopen、fgets、fprintf | printf、scanf、fopen、fgets、fprintf |
|  __受保护_1__ |一般公用事业| malloc、自由、退出、atoi、rand、qsort |
|  __受保护_2__ |字符串操作 | strlen、strcpy、strncpy、strcmp、memcpy |
|  __受保护_3__ |数学| sin、cos、sqrt、pow、fabs、ceil、floor |
|  __受保护_4__ |人物分类| isalpha、isdigit、toupper、tolower | isalpha、isdigit、toupper、tolower |
|  __受保护_5__ |日期和时间 |时间、时钟、difftime、strftime |
|  __受保护_6__ |调试断言|断言（条件）|
|  __受保护_7__ |错误代码 | errno、perror、strerror |
---

## 高级语法和模式
### 预处理器宏
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

### 函数指针和回调
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

### 自定义错误处理模式
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

## 并发与并行
### POSIX 线程（pthreads）
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

### 互斥和共享状态
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

### C11 原子和线程
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

## 项目配置和构建系统
### 项目结构
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

### 生成文件
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

## 测试
### 使用简单框架进行单元测试
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

## 互操作性
### 从 Python 调用 C (ctypes)
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

### 从其他语言调用 C
|语言 |机制|示例|
|----------|------------|---------|
|蟒蛇 | ctypes、cffi |  __受保护_0__ |
|红宝石 |小提琴|  __受保护_1__ |
|爪哇 | JNI |  __受保护_2__ |
| C++ |外部“C” |  __受保护_3__ |
|铁锈|外部“C”+ FFI |  __受保护_4__ |
---

## 设计模式
### 不透明指针（C 语言中的 Pimpl 惯用法）
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

### 虚拟表（C 中的 OOP）
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

## 性能与优化
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

### 优化技术
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
### 交叉编译
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

## 常见模式和习语
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

## 编译和工具
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
| **GDB** |调试器|
| **瓦尔格林德** |内存错误检测器（泄漏、无效访问）|
| **地址消毒剂** |编译时内存检查|
| **cpp检查** |静态分析|
| **clang 格式** |代码格式化 |
---

## 何时使用 C
|场景 |为什么选择 C ​​|更好的选择|
|----------|------|--------------------|
|操作系统 |直接硬件访问，无运行时开销 | --|
|嵌入式系统/微控制器|占地面积最小，可在任何物体上运行 | Rust 用于安全关键型嵌入式 |
|数据库引擎|最高性能，完全内存控制| --|
|编译器和解释器|快速、便携、易于理解 |用于大型编译器项目的 C++ |
|设备驱动程序|大多数操作系统内核 API 都需要 | --|
|性能关键库 |接近最佳速度 | Rust 保证内存安全 |
|通用应用开发|太多的体力劳动 | Python、Java、Go、C# |
|网页开发|完全错误的工具| JavaScript、Go、Python |
|数据科学/机器学习 |没有适合这个的生态系统| Python、R、朱莉娅 |
---

## C 标准
|标准|年份|关键补充|
|----------|------|--------------|
| C89/C90 | 1989/1990 |最初的 ANSI C——仍然是基线 |
| C99 | C99 1999 | // 注释、bool 类型、变长数组、内联、stdint.h |
| C11 | 2011 |原子操作、线程、匿名结构、_Generic |
| C17 | C17 2018 |错误修复和澄清（无新功能）|
| C23 | C23 2024 | 2024 nullptr、typeof、constexpr、改进的预处理器 |
大多数生产代码都以 C11 或 C17 为目标。 C23 带来了现代便利，但采用需要时间。
---

＃＃ 概括
C 是现代计算的基石。它使您能够以最小的抽象开销最大程度地控制硬件。这种控制的成本就是责任——您自己管理内存、检查边界和处理错误。对于系统编程、嵌入式开发以及任何性能和资源限制很重要的地方，C 仍然是无与伦比的。对于其他一切，构建在 C 之上的高级语言通常是更高效的选择。