---
# Metadata
title: "C — Syntax Reference"
description: "Detailed syntax reference for C covering operators, control flow, functions, pointers, memory management, preprocessor, structs, and advanced features."
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
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [c, syntax-reference, operators, control-flow, pointers, memory, preprocessor, coding-and-technology]
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
# C — Référence de syntaxe
Ce document fournit une référence de syntaxe complète et structurée pour C (C11/C17 avec notes C23). Il complète la référence principale du C en se concentrant sur les modèles de syntaxe exhaustifs, les tables d'opérateurs, la mécanique des pointeurs et la gestion de la mémoire.
---

## Opérateurs et expressions
### Opérateurs arithmétiques
| Opérateur | Nom | Exemple | Résultat | Remarques |
|--------------|------|---------|--------|-------|
| `+`| Ajout | `3 + 2`| `5`| |
| `-`| Soustraction | `3 - 2`| `1`| Aussi négation unaire |
| `*`| Multiplications | `3 * 2`| `6`| |
| `/`| Division | `7 / 2`| `3`| Troncature entière pour les types int |
| `%`| Module | `7 % 2`| `1`| Uniquement pour les types entiers |
| `++`| Incrément | `i++`/`++i`| | Post- et pré-incrémentation |
| `--`| Décrémentation | `i--`/`--i`| | Post- et pré-décrémentation |
### Comparaison et opérateurs logiques
| Opérateur | Nom | Exemple | Remarques |
|--------------|------|---------|-------|
| `==`| Égalité | `x == y`| |
| `!=`| Pas égal | `x != y`| |
| `<`,`>`,`<=`,`>=`| Relationnel | `x >= y`| |
| `&&`| ET logique | `a && b`| Court-circuit |
| `\|\|`| OU logique | `a \|\| b`| Court-circuit |
| `!`| NON logique | `!x`| |
### Opérateurs au niveau du bit
| Opérateur | Nom | Exemple | Remarques |
|--------------|------|---------|-------|
| `&`| ET | `5 & 3`| `1`|
| `\|`| OU | `5 \| 3`| `7`|
| `^`| XOR | `5 ^ 3`| `6`|
| `~`| Complément | `~0`| Tous les bits inversés |
| `<<`| Maj gauche | `1 << 3`| `8`|
| `>>`| Maj droite | `8 >> 3`| `1`(défini par l'implémentation pour signé) |
### Opérateurs de pointeur et d'adresse
| Opérateur | Nom | Exemple | Remarques |
|--------------|------|---------|-------|
| `&`| Adresse de | `&x`| Renvoie le pointeur vers x |
| `*`| Déréférencement | `*ptr`| Accéder à la valeur au pointeur |
| `->`| Accès des membres via un pointeur | `p->x`| Équivalent à`(*p).x`|
| `.`| Accès membres | `s.field`| Accès direct aux membres de la structure |
| `[]`| Indice du tableau | `arr[i]`| Équivalent à`*(arr + i)`|
### Priorité des opérateurs (de la plus élevée à la plus basse)
| Priorité | Opérateurs | Associativité |
|------------|-----------|--------------|
| 1 (le plus élevé) | `()``[]``->``.` | De gauche à droite |
| 2 | `!``~``+``-` (unaire)`*``&``sizeof``(type)` | De droite à gauche |
| 3 | `*``/``%`| De gauche à droite |
| 4 | `+``-` | De gauche à droite |
| 5 | `<<``>>` | De gauche à droite |
| 6 | `<``<=``>``>=` | De gauche à droite |
| 7 | `==``!=` | De gauche à droite |
| 8 | `&`(ET au niveau du bit) | De gauche à droite |
| 9 | `^`| De gauche à droite |
| 10 | `\|`| De gauche à droite |
| 11 | `&&`| De gauche à droite |
| 12 | `\|\|`| De gauche à droite |
| 13 | `? :`(ternaire) | De droite à gauche |
| 14 | `=`|`+=`| De droite à gauche |
| 15 (le plus bas) | `,`(virgule) | De gauche à droite |
---

## Types de données
### Types fondamentaux
```c
// Integer types — exact sizes from <stdint.h>
int8_t    a = -128;       // Exactly 8 bits signed
uint8_t   b = 255;        // Exactly 8 bits unsigned
int16_t   c = -32768;
uint16_t  d = 65535;
int32_t   e = -2147483648;
uint32_t  f = 4294967295U;
int64_t   g = -9223372036854775807LL;
uint64_t  h = 18446744073709551615ULL;

// Platform-dependent sizes
char      ch = 'A';       // At least 8 bits
short     s = 32767;      // At least 16 bits
int       i = 0;          // At least 16 bits (usually 32)
long      l = 0L;         // At least 32 bits
long long ll = 0LL;       // At least 64 bits

// Floating-point types
float     f1 = 3.14f;     // IEEE 754 single precision (~7 digits)
double    f2 = 3.14;      // IEEE 754 double precision (~15 digits)
long double f3 = 3.14L;   // Extended precision (platform-dependent)

// Boolean (C99+)
#include <stdbool.h>
bool flag = true;         // Actually an int (0 or 1)

// Size type — result of sizeof
size_t len = sizeof(int);  // Unsigned, guaranteed to hold any object size
```

### Qualificateurs de type
```c
const int MAX = 100;          // Cannot be modified
volatile int sensor;          // May change externally (hardware, ISR)
static int count = 0;         // File scope or function persistence
register int fast_var;        // Hint for register storage (mostly ignored by modern compilers)

// const pointer vs pointer to const
const int *p1;       // Pointer to const int — can't modify *p1, can change p1
int *const p2 = &x;  // Const pointer to int — can modify *p2, can't change p2
const int *const p3; // Both pointer and pointee are const
```

---

## Flux de contrôle
### Déclarations conditionnelles
```c
// if / else if / else
if (score >= 90) {
    grade = 'A';
} else if (score >= 80) {
    grade = 'B';
} else {
    grade = 'F';
}

// Ternary operator
int max = (a > b) ? a : b;

// switch
switch (command) {
    case CMD_START:
        start_engine();
        break;
    case CMD_STOP:
        stop_engine();
        break;
    case CMD_PAUSE:
    case CMD_HOLD:            // Fall-through (intentional)
        pause_engine();
        break;
    default:
        fprintf(stderr, "Unknown command: %d\n", command);
        break;
}
```

### Boucles
```c
// for loop
for (int i = 0; i < 10; i++) {
    printf("%d ", i);
}

// while loop
int n = 100;
while (n > 1) {
    n = (n % 2 == 0) ? n / 2 : 3 * n + 1;
}

// do-while loop (executes at least once)
do {
    printf("Enter a positive number: ");
    scanf("%d", &n);
} while (n <= 0);

// Loop control
for (int i = 0; i < 100; i++) {
    if (i % 2 == 0) continue;   // Skip to next iteration
    if (i > 50) break;           // Exit loop
    process(i);
}
```

---

## Fonctions
### Syntaxe de la fonction
```c
// Basic function
int add(int a, int b) {
    return a + b;
}

// Void function (no return value)
void greet(const char *name) {
    printf("Hello, %s!\n", name);
}

// Function with pointer output parameter
int divide(int a, int b, int *remainder) {
    if (b == 0) return -1;  // Error code
    *remainder = a % b;
    return a / b;
}

int rem;
int quotient = divide(17, 5, &rem);  // quotient=3, rem=2

// Variadic functions
#include <stdarg.h>
int sum(int count, ...) {
    va_list args;
    va_start(args, count);
    int total = 0;
    for (int i = 0; i < count; i++) {
        total += va_arg(args, int);
    }
    va_end(args);
    return total;
}
int s = sum(4, 10, 20, 30, 40);  // 100

// Inline function (C99+)
static inline int max(int a, int b) {
    return (a > b) ? a : b;
}

// Function pointers
typedef int (*Comparator)(const void *, const void *);

int compare_ints(const void *a, const void *b) {
    return (*(const int *)a - *(const int *)b);
}

int arr[] = {5, 2, 8, 1, 9};
qsort(arr, 5, sizeof(int), compare_ints);
```

---

## Pointeurs et mémoire
### Mécanique du pointeur
```c
int x = 42;
int *p = &x;        // p holds the address of x

printf("%d\n", *p);  // Dereference: 42
printf("%p\n", p);   // Print address
printf("%p\n", &x);  // Same address

// Pointer arithmetic
int arr[] = {10, 20, 30, 40, 50};
int *start = arr;     // Points to arr[0]
int *end = arr + 5;   // Points past arr[4]

printf("%d\n", *(start + 2));  // 30 — same as arr[2]
printf("%td\n", end - start);   // 5 — difference in elements

// Pointer casting
void *generic = &x;
int *back = (int *)generic;
printf("%d\n", *back);  // 42

// Double pointers (pointer to pointer)
void allocate_int(int **pp, int value) {
    *pp = malloc(sizeof(int));
    **pp = value;
}
int *result;
allocate_int(&result, 99);
printf("%d\n", *result);  // 99
```

### Gestion dynamique de la mémoire
```c
#include <stdlib.h>
#include <string.h>

// malloc — allocate uninitialized memory
int *arr = malloc(10 * sizeof(int));
if (!arr) { /* handle allocation failure */ }

// calloc — allocate zeroed memory
int *zeros = calloc(10, sizeof(int));  // 10 ints, all zero

// realloc — resize allocation
arr = realloc(arr, 20 * sizeof(int));  // May move to new location
if (!arr) { /* original still valid, but leaked */ }

// Safe realloc pattern
int *new_arr = realloc(arr, 20 * sizeof(int));
if (new_arr) {
    arr = new_arr;
} else {
    // Handle failure — arr is still valid
    free(arr);
}

// free — release memory
free(arr);
arr = NULL;  // Prevent use-after-free

// memcpy, memmove, memset
char src[] = "Hello, World!";
char dst[20];
memcpy(dst, src, strlen(src) + 1);   // Copy including null terminator
memmove(dst + 7, dst, 5);            // Safe for overlapping regions
memset(dst, 0, sizeof(dst));          // Zero-fill
```

---

## Structures, unions et énumérations
```c
// Struct
struct Point {
    double x;
    double y;
};

struct Point p = {3.0, 4.0};
struct Point *pp = &p;
printf("%.1f\n", pp->x);  // 3.0

// Typedef for convenience
typedef struct {
    char name[64];
    int age;
} Person;

Person alice = {"Alice", 30};

// Struct with self-referential pointer (linked list)
typedef struct Node {
    int data;
    struct Node *next;
} Node;

// Union — overlapping storage
typedef union {
    int    i;
    float  f;
    char   bytes[4];
} DataUnion;

DataUnion u;
u.f = 3.14f;
printf("%d\n", u.i);       // Reinterpret same bytes as int

// Enum
typedef enum {
    STATUS_OK = 0,
    STATUS_ERROR = -1,
    STATUS_PENDING = 1,
} Status;

Status s = STATUS_OK;

// Bitfield
struct Flags {
    unsigned int readable   : 1;
    unsigned int writable   : 1;
    unsigned int executable : 1;
};

struct Flags f = {1, 1, 0};
```

---

## Préprocesseur
```c
// Object-like macros
#define PI 3.14159265358979
#define MAX_SIZE 1024

// Function-like macros (use parentheses!)
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define SQUARE(x) ((x) * (x))

// Stringification and concatenation
#define STR(x) #x
#define CONCAT(a, b) a ## b

const char *s = STR(hello);   // "hello"
int CONCAT(my, Var) = 42;     // int myVar = 42;

// Conditional compilation
#ifdef DEBUG
    #define LOG(fmt, ...) fprintf(stderr, fmt "\n", ##__VA_ARGS__)
#else
    #define LOG(fmt, ...) ((void)0)
#endif

// Include guards
#ifndef MY_HEADER_H
#define MY_HEADER_H
// ... header contents ...
#endif

// Predefined macros
__FILE__      // Current filename
__LINE__      // Current line number
__func__      // Current function name (C99+)
__DATE__      // Compilation date
__STDC_VERSION__  // C standard version

// Static assert (C11+)
_Static_assert(sizeof(int) >= 4, "int must be at least 32 bits");
```

---

## Éléments essentiels de la bibliothèque standard
```c
#include <stdio.h>    // I/O: printf, fprintf, fopen, fread
#include <stdlib.h>   // General: malloc, free, atoi, exit, qsort, rand
#include <string.h>   // Strings: strlen, strcpy, strcmp, memcpy, memset
#include <stdint.h>   // Fixed-width types: int32_t, uint64_t
#include <stdbool.h>  // Boolean: bool, true, false
#include <errno.h>    // Error codes: errno, strerror
#include <math.h>     // Math: sqrt, pow, sin, cos, fabs
#include <assert.h>   // Assertions: assert()
#include <time.h>     // Time: clock, time, difftime, CLOCKS_PER_SEC

// File I/O
FILE *f = fopen("data.txt", "r");
if (f) {
    char line[256];
    while (fgets(line, sizeof(line), f)) {
        printf("%s", line);
    }
    fclose(f);
}

// String to number conversions
int n = atoi("42");
long l = strtol("0xFF", NULL, 16);
double d = strtod("3.14", NULL);

// Random numbers
srand((unsigned)time(NULL));
int r = rand() % 100;  // 0 to 99
```

---

## Résumé
La syntaxe du C est minimale et proche du matériel : pointeurs, gestion manuelle de la mémoire et fine couche d'abstraction sur les instructions machine. La puissance du langage vient de cette simplicité : il n'y a presque aucun coût caché, aucune surcharge d'exécution et un contrôle total sur la disposition de la mémoire. Le préprocesseur, bien que puissant, nécessite de la discipline pour être utilisé en toute sécurité. Modern C (C11/C17/C23) a ajouté des fonctionnalités de sécurité importantes telles que`_Static_assert`,`_Generic`,`nullptr`et`typeof`, rendant le langage progressivement plus sûr tout en conservant sa philosophie fondamentale de confiance dans le programmeur.