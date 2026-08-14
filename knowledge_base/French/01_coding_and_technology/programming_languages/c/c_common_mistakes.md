---
# Metadata
title: "C — Common Mistakes & Anti-Patterns"
description: "Comprehensive guide to common pitfalls, traps, and anti-patterns in C that catch even experienced developers, with explanations and corrections."
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
tags: [c, common-mistakes, anti-patterns, pitfalls, memory-safety, best-practices, coding-and-technology]
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
# C — Erreurs courantes et anti-modèles
Ce document répertorie les erreurs, pièges et anti-modèles les plus courants en C. Chaque entrée montre l'approche incorrecte, explique pourquoi elle échoue et fournit la solution correcte. C vous donne un contrôle total, ce qui signifie l'entière responsabilité de la sécurité de la mémoire, de la vérification des limites et du comportement non défini.
---

## 1. Débordement de tampon avec`gets()`/ `strcpy()`
```c
// ❌ WRONG — no bounds checking
char buffer[64];
gets(buffer);           // NEVER use gets() — removed in C11
strcpy(buffer, input);  // overflow if input > 63 chars

// ✅ CORRECT — use bounded functions
fgets(buffer, sizeof(buffer), stdin);
strncpy(buffer, input, sizeof(buffer) - 1);
buffer[sizeof(buffer) - 1] = '\0';  // ensure null termination

// ✅ BEST — use snprintf
snprintf(buffer, sizeof(buffer), "%s", input);
```

---

## 2. Pointeurs pendants
```c
// ❌ WRONG — pointer to freed memory
int *ptr = malloc(sizeof(int));
*ptr = 42;
free(ptr);
printf("%d", *ptr);  // undefined behavior!

// ✅ CORRECT — set pointer to NULL after free
free(ptr);
ptr = NULL;

// ❌ WRONG — returning pointer to local variable
int *get_value() {
    int x = 42;
    return &x;  // x is destroyed when function returns
}

// ✅ CORRECT — allocate on heap or use output parameter
int *get_value() {
    int *x = malloc(sizeof(int));
    *x = 42;
    return x;  // caller must free
}
```

---

## 3. Erreurs ponctuelles
```c
// ❌ WRONG — writing past array bounds
int arr[10];
for (int i = 0; i <= 10; i++) {  // i=10 is out of bounds!
    arr[i] = 0;
}

// ✅ CORRECT — use < not <=
for (int i = 0; i < 10; i++) {
    arr[i] = 0;
}

// ✅ CORRECT — use sizeof for array length
for (size_t i = 0; i < sizeof(arr) / sizeof(arr[0]); i++) {
    arr[i] = 0;
}
```

---

## 4. Variables non initialisées
```c
// ❌ WRONG — using uninitialized memory
int x;
if (condition) x = 42;
printf("%d", x);  // undefined if condition is false

// ✅ CORRECT — always initialize
int x = 0;
if (condition) x = 42;
printf("%d", x);
```

---

## 5.`scanf()`sans limites de largeur
```c
// ❌ WRONG — buffer overflow
char name[20];
scanf("%s", name);  // no limit on input length

// ✅ CORRECT — specify maximum width
scanf("%19s", name);  // leaves room for null terminator
```

---

## 6. Débordement d'entier
```c
// ❌ WRONG — no overflow check
int a = INT_MAX;
int b = a + 1;  // undefined behavior (signed overflow)

// ✅ CORRECT — check before operation
if (a > INT_MAX - 1) {
    fprintf(stderr, "Overflow detected\n");
    // handle error
}
int result = a + 1;

// ✅ CORRECT — use unsigned for wrapping behavior
unsigned int a = UINT_MAX;
unsigned int b = a + 1;  // well-defined: wraps to 0
```

---

## 7. Fuites de mémoire
```c
// ❌ WRONG — forgetting to free
void process() {
    int *data = malloc(1000 * sizeof(int));
    // ... use data ...
    return;  // memory leaked!
}

// ✅ CORRECT — free before every return
void process() {
    int *data = malloc(1000 * sizeof(int));
    if (!data) return;
    // ... use data ...
    free(data);
}

// ✅ CORRECT — use goto cleanup pattern
void process() {
    int *data = NULL;
    int *result = NULL;

    data = malloc(1000 * sizeof(int));
    if (!data) goto cleanup;

    result = malloc(500 * sizeof(int));
    if (!result) goto cleanup;

    // ... use data and result ...

cleanup:
    free(data);
    free(result);
}
```

---

## 8. Vulnérabilités de format de chaîne
```c
// ❌ WRONG — user input as format string
char *user_input = get_input();
printf(user_input);  // attacker can use %x, %n

// ✅ CORRECT — always use format string literal
printf("%s", user_input);
```

---

## 9. Confondre`=`et`==`dans les conditions
```c
// ❌ WRONG — assignment instead of comparison
if (x = 5) {  // always true, assigns 5 to x
    printf("x is 5");
}

// ✅ CORRECT — use comparison
if (x == 5) {
    printf("x is 5");
}

// ✅ DEFENSIVE — Yoda condition (compiler catches typo)
if (5 == x) {
    // if you write if (5 = x), compiler error
}
```

---

## 10. Ne pas comprendre l'arithmétique des pointeurs
```c
// ❌ WRONG — treating pointer arithmetic as byte arithmetic
int arr[5] = {1, 2, 3, 4, 5};
int *p = arr;
p = p + 1;  // advances by sizeof(int), not 1 byte!

// ❌ WRONG — arithmetic on void pointers
void *vp = arr;
vp = vp + 1;  // undefined behavior (void has no size)

// ✅ CORRECT — cast void pointer first
int *ip = (int *)vp;
ip = ip + 1;  // advances by sizeof(int)
```

---

## 11. Anti-modèle : les nombres magiques
```c
// ❌ WRONG — unexplained constants
if (status == 42) { ... }
char buffer[16384];

// ✅ CORRECT — use named constants or enums
#define MAX_BUFFER_SIZE 16384
#define STATUS_SUCCESS 42

enum { MAX_BUFFER_SIZE = 16384, STATUS_SUCCESS = 42 };
```

---

## 12.`break`manquant dans `switch`
```c
// ❌ WRONG — fall-through (often unintentional)
switch (grade) {
    case 'A': printf("Excellent");
    case 'B': printf("Good");     // falls through from A!
    case 'C': printf("Average");  // falls through from B!
    default:  printf("Fail");
}

// ✅ CORRECT — explicit break or fall-through comment
switch (grade) {
    case 'A': printf("Excellent"); break;
    case 'B': printf("Good");      break;
    case 'C': printf("Average");   break;
    default:  printf("Fail");      break;
}
```

---

## Résumé
Les dangers du C sont bien connus mais omniprésents : débordements de tampon, pointeurs suspendus, dépassement d'entier, attaques de chaînes de formatage et fuites de mémoire. La discipline est la suivante : vérifiez toujours les valeurs de retour, libérez toujours ce que vous allouez, utilisez toujours des fonctions limitées (`snprintf`,`strncpy`,`fgets`), n'utilisez jamais`gets()`, initialisez toutes les variables et utilisez des outils comme Valgrind et AddressSanitizer. C récompense les programmeurs prudents avec des performances et un contrôle inégalés, mais punit la négligence avec un comportement indéfini et des vulnérabilités de sécurité.