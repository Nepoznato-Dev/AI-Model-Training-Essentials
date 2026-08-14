---
# Metadata
title: "C — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, safe C code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [c, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "14 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# C — 惯用模式和最佳实践
本指南涵盖了编写干净、安全的 C 代码的惯用模式和最佳实践。
---

## 标头防护和包含
```c
// ✅ Include guard (pragma once or traditional)
#pragma once
// or:
#ifndef MYMODULE_H
#define MYMODULE_H

// ... declarations

#endif // MYMODULE_H

// ✅ Include order: own header, C stdlib, system, project
#include "mymodule.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "project/common.h"
```

---

## 命名约定
```c
// ✅ snake_case for functions and variables
int calculate_total(int count);
size_t buffer_size;

// ✅ UPPER_CASE for macros and constants
#define MAX_BUFFER_SIZE 4096
#define PI 3.14159265358979

// ✅ Typedef for structs
typedef struct {
    char name[64];
    int age;
} Person;

// ✅ Prefix for module namespacing
typedef struct {
    int x, y;
} Vec2;

Vec2 vec2_create(int x, int y);
void vec2_add(Vec2 *a, const Vec2 *b);
```

---

## 内存管理
```c
// ✅ Always check malloc
int *arr = malloc(count * sizeof(int));
if (!arr) {
    fprintf(stderr, "allocation failed\n");
    return -1;
}

// ✅ calloc for zeroed memory
int *arr = calloc(count, sizeof(int));

// ✅ Free in reverse order of allocation
// ✅ Set pointer to NULL after free
free(ptr);
ptr = NULL;

// ✅ Single exit point for cleanup
int process(const char *filename) {
    int result = -1;
    FILE *fp = NULL;
    char *buffer = NULL;
    
    fp = fopen(filename, "r");
    if (!fp) goto cleanup;
    
    buffer = malloc(1024);
    if (!buffer) goto cleanup;
    
    // ... work ...
    result = 0;
    
cleanup:
    free(buffer);
    if (fp) fclose(fp);
    return result;
}
```

---

## 错误处理
```c
// ✅ Return error codes
int read_config(const char *path, Config *out) {
    if (!path || !out) return -1;
    // ...
    return 0;  // success
}

// ✅ errno for standard functions
if (fopen(path, "r") == NULL) {
    perror("fopen failed");
    return -1;
}

// ✅ Assert for invariants (debug only)
#include <assert.h>
assert(index < array_size);

// ✅ Static assert for compile-time checks
_Static_assert(sizeof(int) == 4, "int must be 32 bits");
```

---

## 宏和内联
```c
// ✅ Macro with do-while for statements
#define SWAP(a, b) do { \
    typeof(a) tmp = (a); \
    (a) = (b); \
    (b) = tmp; \
} while (0)

// ✅ Macro with parentheses for expressions
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define ARRAY_SIZE(arr) (sizeof(arr) / sizeof((arr)[0]))

// ✅ Prefer inline functions over macros
static inline int max_int(int a, int b) {
    return a > b ? a : b;
}

// ✅ Compiler attributes
__attribute__((unused))
__attribute__((noreturn))
__attribute__((warn_unused_result))
```

---

## 结构模式
```c
// ✅ Opaque struct (hide implementation)
// header:
typedef struct Connection Connection;
Connection *conn_create(const char *host);
void conn_destroy(Connection *conn);

// source:
struct Connection {
    int socket;
    char host[256];
};

// ✅ Flexible array member (C99)
typedef struct {
    size_t length;
    char data[];
} Buffer;

Buffer *buf = malloc(sizeof(Buffer) + data_len);
buf->length = data_len;

// ✅ Designated initializers (C99)
Config cfg = {
    .host = "localhost",
    .port = 8080,
    .debug = true,
};
```

---

## 防御性编程
```c
// ✅ Validate all inputs
int process(const char *input, size_t len) {
    if (!input || len == 0 || len > MAX_INPUT) return -1;
    // ...
}

// ✅ Use size_t for sizes and counts
void copy(char *dst, const char *src, size_t n);

// ✅ Use const for read-only parameters
int strlen_custom(const char *str);

// ✅ Bounds checking
snprintf(buf, sizeof(buf), "Hello, %s!", name);
```

---

## 现代 C (C11/C17/C23)
```c
// ✅ _Generic for type-generic macros (C11)
#define print(x) _Generic((x), \
    int: print_int, \
    double: print_double, \
    char*: print_string \
)(x)

// ✅ Atomic operations (C11)
#include <stdatomic.h>
atomic_int counter = 0;
atomic_fetch_add(&counter, 1);

// ✅ Threads (C11)
#include <threads.h>
thrd_t thread;
thrd_create(&thread, worker_func, arg);

// ✅ Static assertions
static_assert(sizeof(void*) == 8, "64-bit required");
```

---

＃＃ 概括
C 惯用语强调：仔细的内存管理、防御性编程、封装的不透明结构、带有 do-while 的宏、带有 goto 清理的单一退出点以及现代 C11/C23 功能。按照`clang-format`进行格式化，按照`clang-tidy`进行 linting，并始终使用`-Wall -Wextra -Werror`进行编译。测试期间使用消毒剂（ASan、UBSan）。 C 社区重视简单性、性能和显式控制——“信任程序员”。