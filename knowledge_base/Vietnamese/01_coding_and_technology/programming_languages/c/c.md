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
# C
C là ngôn ngữ lập trình thủ tục, có mục đích chung được tạo bởi Dennis Ritchie tại Bell Labs từ năm 1969 đến năm 1973. Nó được thiết kế để triển khai hệ điều hành Unix và nó vẫn là một trong những ngôn ngữ lập trình được sử dụng rộng rãi nhất trong hơn 50 năm sau. C cung cấp khả năng truy cập bộ nhớ cấp thấp, một thư viện tiêu chuẩn tối thiểu và ánh xạ rõ ràng tới các lệnh máy -- khiến nó trở thành nền tảng cho hầu hết các máy tính hiện đại được xây dựng.
C là ngôn ngữ đằng sau các hệ điều hành (Linux, nhân Windows, macOS), hệ thống nhúng, công cụ cơ sở dữ liệu (SQLite, PostgreSQL), trình biên dịch (CPython của Python, MRI của Ruby) và hầu như mọi thời gian chạy ngôn ngữ lập trình khác. Hiểu C là hiểu cách máy tính thực sự hoạt động.
---

## Tại sao C lại quan trọng
- **Gần với phần cứng**: C ánh xạ gần với mã máy. Không có trình thu gom rác, không có chi phí thời gian chạy, không có phân bổ ẩn.
- **Tính phổ biến**: Từ bộ vi điều khiển đến siêu máy tính, C chạy khắp mọi nơi.
- **Nền tảng điện toán**: Linux, Windows, nhân macOS, trình thông dịch Python, SQLite, Git -- tất cả đều được viết bằng C.
- **Hiệu suất**: Tốc độ thực thi gần như tối ưu với toàn quyền kiểm soát bố cục bộ nhớ.
- **Ảnh hưởng**: Cú pháp và khái niệm của C (con trỏ, mảng, cấu trúc, hàm) đã định hình C++, Java, C#, JavaScript, Go, Rust và hầu hết các ngôn ngữ tiếp theo.
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Quản lý bộ nhớ thủ công** | Không có trình thu gom rác - bạn tự phân bổ và giải phóng bộ nhớ | Sử dụng cẩn thận malloc/free; Các mẫu RAII trong C++ |
| **Tràn bộ đệm** | Không có giới hạn kiểm tra trên mảng -- dễ dàng ghi vào cuối bộ đệm | Sử dụng strncpy thay vì strcpy; kích hoạt cảnh báo trình biên dịch |
| **Không có OOP tích hợp** | Chỉ thủ tục - không có lớp, kế thừa hoặc phương thức | Sử dụng cấu trúc + con trỏ hàm; hoặc chuyển sang C++ |
| **Thư viện tiêu chuẩn có giới hạn** | Chức năng tích hợp tối thiểu | Thư viện của bên thứ ba hoặc viết của riêng bạn |
| **Hành vi không xác định** | Nhiều lỗi biên dịch tốt nhưng bị lỗi khó lường | Sử dụng chất khử trùng, máy phân tích tĩnh điện |
---

##Cơ bản về cú pháp
###Cấu trúc cơ bản
Mọi chương trình C đều bắt đầu tại`main()`. Ngôn ngữ được biên dịch - mã nguồn trở thành mã máy thông qua trình biên dịch (GCC, Clang, MSVC).
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

### Biến và kiểu
C được gõ tĩnh - mọi biến đều có kiểu cố định được biết tại thời điểm biên dịch.
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

### Con trỏ
Con trỏ là tính năng mạnh mẽ nhất và dễ bị hiểu lầm nhất của C. Một con trỏ chứa một địa chỉ bộ nhớ.
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

### Luồng điều khiển
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

### Hàm và ngăn xếp
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

## Bố cục bộ nhớ
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

| Vùng | Có Gì Ở Đó | Trọn đời | Ai quản lý nó |
|--------|-------|----------|----------------|
| **Chồng** | Biến cục bộ, tham số hàm | Cho đến khi hàm trả về | Trình biên dịch (tự động) |
| **Đống** | phân bổ malloc/calloc | Cho đến khi bạn gọi free() | Bạn (thủ công) |
| **Dữ liệu/BSS** | Biến toàn cục và tĩnh | Toàn bộ thời gian sử dụng chương trình | Trình biên dịch (tự động) |
| **Văn bản** | Mã máy | Toàn bộ thời gian sử dụng chương trình | Chỉ đọc |
---

## Thư viện chuẩn
| Tiêu đề | Mục đích | Chức năng chung |
|--------|----------|--------|
|  __BẢO VỆ_0__ | Đầu vào/đầu ra | printf, scanf, fopen, fgets, fprintf |
|  __BẢO VỆ_1__ | Tiện ích chung | malloc, miễn phí, thoát, atoi, rand, qsort |
|  __BẢO VỆ_2__ | Hoạt động chuỗi | strlen, strcpy, strncpy, strcmp, memcpy |
|  __BẢO VỆ_3__ | Toán học | sin, cos, sqrt, pow, fabs, trần, sàn |
|  __BẢO VỆ_4__ | Phân loại nhân vật | isalpha, isdigit, toupper, tower |
|  __BẢO VỆ_5__ | Ngày giờ | thời gian, đồng hồ, chênh lệch thời gian, strftime |
|  __BẢO VỆ_6__ | Xác nhận gỡ lỗi | khẳng định(điều kiện) |
|  __BẢO VỆ_7__ | Mã lỗi | errno, perror, strerror |
---

## Cú pháp & Mẫu nâng cao
### Macro tiền xử lý
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

### Con trỏ hàm và lệnh gọi lại
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

### Mẫu xử lý lỗi tùy chỉnh
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

## Đồng thời & Song song
### Chủ đề POSIX (pthread)
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

### Mutex và trạng thái chia sẻ
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

### C11 Nguyên tử và Chủ đề
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

## Cấu hình dự án & xây dựng hệ thống
### Cấu trúc dự án
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

###Tập tin tạo
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

### Đường dẫn CI/CD (Hành động trên GitHub)
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

##Thử nghiệm
### Kiểm tra đơn vị với một khung đơn giản
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

## Khả năng tương tác
### Gọi C từ Python (ctypes)
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

### Gọi C từ các ngôn ngữ khác
| Ngôn ngữ | Cơ chế | Ví dụ |
|----------|-------------|----------|
| Python | ctypes, cffi |  __BẢO VỆ_0__ |
| Ruby | Fiddle |  __BẢO VỆ_1__ |
| Java | JNI |  __BẢO VỆ_2__ |
| C++ | bên ngoài "C" |  __BẢO VỆ_3__ |
| rỉ sét | bên ngoài "C" + FFI |  __BẢO VỆ_4__ |
---

## Mẫu thiết kế
### Con trỏ mờ (Thành ngữ Pimpl trong C)
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

### Bảng ảo (OOP trong C)
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

## Hiệu suất & Tối ưu hóa
### Công cụ lập hồ sơ
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

### Kỹ thuật tối ưu hóa
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

## Triển khai
### Biên dịch chéo
```bash
# Cross-compile for ARM (embedded)
arm-none-eabi-gcc -mcpu=cortex-m4 -o firmware.elf main.c

# Cross-compile for Windows from Linux
x86_64-w64-mingw32-gcc -o my_app.exe main.c

# Static linking (no shared library dependencies)
gcc -static -o my_app main.c
```

### Triển khai Docker
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

## Các mẫu và thành ngữ phổ biến
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

## Biên dịch và tạo công cụ
```bash
gcc -Wall -Wextra -o myprogram myprogram.c      # Basic compile
gcc -g -Wall -o myprogram myprogram.c            # With debug symbols
gcc -O2 -Wall -o myprogram myprogram.c           # With optimisation
gcc -std=c17 -Wall -o myprogram myprogram.c      # Specific standard
make          # Runs the Makefile
make clean    # Removes build artifacts
```

| Công cụ | Mục đích |
|------|----------|
| **GCC / Clang** | Trình biên dịch |
| **Tạo / CMake** | Xây dựng hệ thống |
| **GDB** | Trình gỡ lỗi |
| **Valgrind** | Trình phát hiện lỗi bộ nhớ (rò rỉ, truy cập không hợp lệ) |
| **Khử trùng địa chỉ** | Kiểm tra bộ nhớ thời gian biên dịch |
| **cppcheck** | Phân tích tĩnh |
| **định dạng clang** | Định dạng mã |
---

## Khi nào nên sử dụng C
| Kịch bản | Tại sao C | Thay thế tốt hơn |
|----------|-------|-------------------|
| Hệ điều hành | Truy cập phần cứng trực tiếp, không tốn phí thời gian chạy | -- |
| Hệ thống nhúng / vi điều khiển | Dấu chân tối thiểu, chạy trên mọi thứ | Rust dành cho nhúng quan trọng về an toàn |
| Công cụ cơ sở dữ liệu | Hiệu suất tối đa, kiểm soát toàn bộ bộ nhớ | -- |
| Trình biên dịch và phiên dịch | Nhanh chóng, di động, hiểu rõ | C++ cho các dự án biên dịch lớn hơn |
| Trình điều khiển thiết bị | Được yêu cầu bởi hầu hết các API nhân hệ điều hành | -- |
| Thư viện quan trọng về hiệu suất | Tốc độ gần tối ưu | Rust để đảm bảo an toàn cho bộ nhớ |
| Phát triển ứng dụng chung | Quá nhiều công việc thủ công | Python, Java, Go, C# |
| Phát triển web | Công cụ sai hoàn toàn | JavaScript, Đi, Python |
| Khoa học dữ liệu / ML | Không có hệ sinh thái cho việc này | Python, R, Julia |
---

##C Tiêu chuẩn
| Tiêu chuẩn | Năm | Bổ sung chính |
|----------|------|--------------|
| C89/C90 | 1989/1990 | ANSI C ban đầu -- vẫn là đường cơ sở |
| C99 | 1999 | // nhận xét, kiểu bool, mảng có độ dài thay đổi, nội tuyến, stdint.h |
| C11 | 2011 | Hoạt động nguyên tử, chủ đề, cấu trúc ẩn danh, _Generic |
| C17 | 2018 | Sửa lỗi và làm rõ (không có tính năng mới) |
| C23 | 2024 | nullptr, typeof, constexpr, bộ tiền xử lý cải tiến |
Hầu hết mã sản xuất đều nhắm đến C11 hoặc C17. C23 mang lại tiện ích hiện đại nhưng việc áp dụng cần có thời gian.
---

## Bản tóm tắt
C là nền tảng của điện toán hiện đại. Nó cho phép bạn kiểm soát tối đa phần cứng với chi phí trừu tượng tối thiểu. Cái giá của việc kiểm soát đó là trách nhiệm -- bạn quản lý bộ nhớ, kiểm tra giới hạn và tự mình xử lý lỗi. Đối với lập trình hệ thống, phát triển nhúng và bất kỳ nơi nào có vấn đề về hiệu suất và hạn chế về tài nguyên, C vẫn không thể so sánh được. Đối với mọi thứ khác, các ngôn ngữ cấp cao hơn được xây dựng dựa trên C thường là những lựa chọn hiệu quả hơn.