---
# Metadata
title: "C — Cheat Sheet"
description: "Quick-reference cheat sheet for C syntax, memory management, and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [c, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# C — Hoja de referencia
## Conceptos básicos
```c
// Variables
int x = 42;
float pi = 3.14f;
double d = 3.14159;
char c = 'A';
char name[] = "Alice";
const int MAX = 100;

// Sizes (platform-dependent)
sizeof(int)       // typically 4
sizeof(long)      // 4 or 8
sizeof(char)      // always 1
sizeof(void*)     // 4 or 8

// Fixed-width types (stdint.h)
#include <stdint.h>
int32_t n = -42;
uint64_t big = 100ULL;
int8_t byte = 127;

// Format specifiers
printf("%d\n", x);       // int
printf("%ld\n", longval); // long
printf("%f\n", pi);      // float/double
printf("%.2f\n", pi);    // 2 decimal places
printf("%s\n", name);    // string
printf("%p\n", ptr);     // pointer
printf("%zu\n", size);   // size_t
printf("%x\n", hex);     // hex
```

## Punteros y memoria
```c
// Pointer basics
int x = 42;
int *p = &x;    // p points to x
*p = 100;       // x is now 100

// Dynamic allocation
int *arr = (int*)malloc(10 * sizeof(int));
if (arr == NULL) { /* handle error */ }
arr[0] = 42;
free(arr);       // always free!
arr = NULL;      // avoid dangling pointer

// calloc (zero-initialized)
int *zeros = (int*)calloc(10, sizeof(int));

// realloc
arr = (int*)realloc(arr, 20 * sizeof(int));

// Struct pointer
struct Point { int x, y; };
struct Point p = {1, 2};
struct Point *pp = &p;
pp->x;   // same as (*pp).x
```

## Matrices y cadenas
```c
// Arrays
int arr[5] = {1, 2, 3, 4, 5};
int matrix[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
int len = sizeof(arr) / sizeof(arr[0]);

// Strings (null-terminated char arrays)
char s[] = "Hello";
char buf[256];
strcpy(buf, "Hello");     // copy
strcat(buf, " World");    // concatenate
strlen(buf);              // length
strcmp("abc", "def");     // compare
strncpy(buf, src, sizeof(buf) - 1); // safe copy
buf[sizeof(buf) - 1] = '\0';        // ensure null term

// String from stdio
fgets(buf, sizeof(buf), stdin);
```

## Controlar el flujo
```c
if (condition) {
    // ...
} else if (other) {
    // ...
} else {
    // ...
}

// Ternary
int max = (a > b) ? a : b;

// Switch
switch (op) {
    case '+': result = a + b; break;
    case '-': result = a - b; break;
    default:  printf("unknown\n"); break;
}

// Loops
for (int i = 0; i < 10; i++) { ... }
while (condition) { ... }
do { ... } while (condition);

// Goto (use sparingly)
goto cleanup;
cleanup:
    free(ptr);
    return;
```

## Funciones
```c
// Declaration (prototype)
int add(int a, int b);

// Definition
int add(int a, int b) {
    return a + b;
}

// Pointers as parameters (pass by reference)
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Function pointers
int (*op)(int, int) = add;
int result = op(3, 4);  // 7

// Variadic functions
#include <stdarg.h>
int sum(int count, ...) {
    va_list args;
    va_start(args, count);
    int total = 0;
    for (int i = 0; i < count; i++)
        total += va_arg(args, int);
    va_end(args);
    return total;
}
```

## Estructuras y sindicatos
```c
// Struct
struct Point {
    int x;
    int y;
};
struct Point p = {.x = 1, .y = 2};  // designated init

// Typedef
typedef struct {
    char name[64];
    int age;
} Person;
Person alice = {"Alice", 30};

// Union (shared memory)
union Value {
    int i;
    float f;
    char s[4];
};
union Value v;
v.i = 42;  // now v.f and v.s are reinterpreted

// Bit fields
struct Flags {
    unsigned int read  : 1;
    unsigned int write : 1;
    unsigned int exec  : 1;
};
```

## Preprocesador
```c
#define MAX_SIZE 1024
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define SQUARE(x) ((x) * (x))

// Conditional compilation
#ifdef DEBUG
    printf("Debug: x = %d\n", x);
#endif

#ifndef HEADER_H
#define HEADER_H
// header content
#endif

// Include
#include <stdio.h>      // system header
#include "myheader.h"   // local header
```

## Manejo de errores
```c
#include <errno.h>
#include <string.h>

FILE *f = fopen("data.txt", "r");
if (f == NULL) {
    fprintf(stderr, "Error: %s\n", strerror(errno));
    return 1;
}

// setjmp/longjmp (non-local jumps)
#include <setjmp.h>
static jmp_buf env;
if (setjmp(env) == 0) {
    // normal path
    longjmp(env, 1);  // jump back
} else {
    // error path
}
```
