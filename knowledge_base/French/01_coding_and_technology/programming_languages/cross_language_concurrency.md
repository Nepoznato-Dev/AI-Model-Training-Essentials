---
# Metadata
title: "Cross-Language Comparison — Concurrency & Parallelism"
description: "Side-by-side comparison of concurrency models across 34 programming languages."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cross-language comparison"
tags: [concurrency, parallelism, cross-language, comparison, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Comparaison multilingue — Concurrence et parallélisme
## Présentation des modèles de concurrence
| Langue | Modèle | Mécanisme clé | Mémoire partagée ? |
|--------------|-------|---------------|----------------|
| Python | GIL + fils de discussion | `threading`,`asyncio`| Oui (GIL limite le parallélisme) |
| JavaScript | Boucle d'événement | Promesses,`async/await`| Non (monothread) |
| Rouille | Propriété + Envoyer/Sync | `std::thread`,`async/await`, canaux | Sécurité au moment de la compilation |
| Aller | Goroutines | `go func()`, canaux | Non (passage de message) |
| Java | Fils de discussion du système d'exploitation | `Thread`,`ExecutorService`,`CompletableFuture`| Oui |
| Tapuscrit | Boucle d'événement | Promesses,`async/await`| Non (monothread) |
| C | Fils POSIX | `pthread`, OpenMP | Oui (synchronisation manuelle) |
| C++ | Fils de discussion du système d'exploitation | `std::thread`,`std::async`, coroutines | Oui (synchronisation manuelle) |
| C# | asynchrone/attendre | `Task`,`async/await`,`Parallel`| Oui |
| Rubis | GVL + fibres | `Thread`,`Fiber`,`Ractor`(3.0+) | Oui (GVL), Ractor : Non |
| Rapide | Acteurs | `async/await`, acteurs,`Sendable`| Non (isolement des acteurs) |
| Kotlin | Coroutines | `suspend`,`launch`,`async`| Dépend du répartiteur |
| PHP | Basé sur les processus | `pcntl_fork`, fibres (8.1+) | Non (processus distincts) |
| Échelle | Fils de discussion JVM | `Future`, Acteurs Akka, ZIO, Effet Chats | Oui (JVM) |
| Haskell | Fils verts |  `forkIO`, STM,`async`| Oui (STM pour la sécurité) |
| Lua | Coroutines | `coroutine.create/resume/yield`| Non (coopérative) |
| R | Séquentiel + parallèle | `parallel`,`future`| Non (processus distincts) |
| Julie | Tâches + fils de discussion | `@async`,`@threads`,`Distributed`| Oui (types thread-safe) |
| Fléchette | Isole | `Isolate`,`async/await`| Non (passage de message) |
| Perl | Fils + fourchette | `threads`,`fork`| Oui (threads) |
| MATLAB | Piscine parallèle | `parfor`,`spmd`,`gpuArray`| Non (travailleurs) |
| SQL | N/A | La base de données gère la concurrence (MVCC, verrous) | N/A |
| Coquille | Processus d'arrière-plan | `&`,`wait`,`xargs -P`| Non (processus distincts) |
| Fortran | Coarrays + OpenMP | `coarray`,`do concurrent`, OpenMP | Oui (mémoire partagée) |
| Ada | Tâches + protégé | `task`,`protected object`, rendez-vous | Oui (objets protégés) |
| COBOL | N/A | Traitement par lots, pas de concurrence native | N/A |
| Prologue | N/A | Séquentiel (certaines implémentations ont des threads) | N/A |
| Lisp/Clojure | Agents STM + | `future`,`promise`,`core.async`, STM | Clojure : STM (réfs, atomes) |
| Erlang/Élixir | Modèle d'acteur | `spawn`, transmission de messages,`receive`| Non (passage de message) |
| OCaml | Domaine + Effet | `Domain.spawn`, gestionnaires d'effets (5.0+) | Non (domaines) |
| Assemblée | N/A | Dépend du système d'exploitation (interruptions, appels système) | N/A |
| Delphes | Fils | `TThread`,`TTask`| Oui (synchronisation manuelle) |
| Gratter | Piloté par les événements | `when green flag clicked`, diffusion | Non (isolation des sprites) |
| VB | asynchrone/attendre | `Async/Await`,`Task`| Oui |
## Création de fil de discussion
```python
# Python: threading
import threading
t = threading.Thread(target=worker, args=(data,))
t.start()
t.join()

# Python: asyncio
import asyncio
async def main():
    await asyncio.gather(task1(), task2())
asyncio.run(main())
```

```javascript
// JavaScript: Promises
const result = await Promise.all([task1(), task2()]);

// JavaScript: Web Workers
const worker = new Worker('worker.js');
worker.postMessage(data);
worker.onmessage = (e) => console.log(e.data);
```

```rust
// Rust: threads
use std::thread;
let handle = thread::spawn(|| {
    println!("Hello from thread!");
});
handle.join().unwrap();

// Rust: async (tokio)
#[tokio::main]
async fn main() {
    let task = tokio::spawn(async { /* work */ });
    task.await.unwrap();
}
```

```go
// Go: goroutines
go func() {
    fmt.Println("Hello from goroutine!")
}()

// Go: channels
ch := make(chan int)
go func() { ch <- 42 }()
value := <-ch
```

```java
// Java: threads
Thread t = new Thread(() -> System.out.println("Hello!"));
t.start();
t.join();

// Java: CompletableFuture
CompletableFuture.supplyAsync(() -> compute())
    .thenAccept(System.out::println);
```

```c
// C: POSIX threads
#include <pthread.h>
void* worker(void* arg) {
    printf("Hello from thread!\n");
    return NULL;
}
pthread_t t;
pthread_create(&t, NULL, worker, NULL);
pthread_join(t, NULL);
```

```go
// Go: worker pool pattern
func worker(id int, jobs <-chan int, results chan<- int) {
    for j := range jobs {
        results <- j * 2
    }
}
jobs := make(chan int, 100)
results := make(chan int, 100)
for w := 0; w < 3; w++ {
    go worker(w, jobs, results)
}
```

```erlang
% Erlang: spawn + message passing
Pid = spawn(fun() ->
    receive
        {From, Msg} -> From ! {response, Msg}
    end
end),
Pid ! {self(), hello},
receive
    {Pid, Response} -> io:format("~p~n", [Response])
end.
```

```elixir
# Elixir: Task (built on Erlang processes)
task = Task.async(fn -> compute() end)
result = Task.await(task)

# Elixir: GenServer (OTP behavior)
defmodule Worker do
  use GenServer
  def start_link(args), do: GenServer.start_link(__MODULE__, args)
  def handle_call(:work, _from, state), do: {:reply, result, state}
end
```

```swift
// Swift: async/await + actors
actor Counter {
    var count = 0
    func increment() { count += 1 }
}

let counter = Counter()
Task {
    await counter.increment()
}

// Swift: TaskGroup
await withTaskGroup(of: Int.self) { group in
    for i in 0..<10 {
        group.addTask { return i * i }
    }
}
```

```kotlin
// Kotlin: coroutines
import kotlinx.coroutines.*

runBlocking {
    val deferred = async { computeAsync() }
    println(deferred.await())
}

// Kotlin: coroutine scope
CoroutineScope(Dispatchers.Default).launch {
    val result = withContext(Dispatchers.IO) { fetchData() }
}
```

## Modèles de concurrence clés
### Producteur-Consommateur
```go
// Go: channels
func producer(ch chan<- int) {
    for i := 0; i < 10; i++ { ch <- i }
    close(ch)
}
func consumer(ch <-chan int) {
    for v := range ch { fmt.Println(v) }
}
ch := make(chan int)
go producer(ch)
consumer(ch)
```

```rust
// Rust: channels (mpsc)
use std::sync::mpsc;
use std::thread;
let (tx, rx) = mpsc::channel();
thread::spawn(move || {
    for i in 0..10 { tx.send(i).unwrap(); }
});
for val in rx { println!("{}", val); }
```

```erlang
% Erlang: message passing
producer(Pid, 0) -> Pid ! done;
producer(Pid, N) -> Pid ! {data, N}, producer(Pid, N-1).

consumer() ->
    receive
        done -> ok;
        {data, N} -> io:format("~p~n", [N]), consumer()
    end.
```

### Mutex / Verrouillage
```java
// Java: synchronized
synchronized (lock) {
    sharedResource++;
}

// Java: ReentrantLock
ReentrantLock lock = new ReentrantLock();
lock.lock();
try { sharedResource++; }
finally { lock.unlock(); }
```

```python
# Python: threading.Lock
import threading
lock = threading.Lock()
with lock:
    shared_resource += 1
```

```rust
// Rust: Mutex (compile-time safety)
use std::sync::{Arc, Mutex};
let counter = Arc::new(Mutex::new(0));
let c = counter.clone();
thread::spawn(move || {
    let mut num = c.lock().unwrap();
    *num += 1;
});
```

```csharp
// C#: lock
lock (lockObj) {
    sharedResource++;
}

// C#: SemaphoreSlim
await semaphoreSlim.WaitAsync();
try { /* critical section */ }
finally { semaphoreSlim.Release(); }
```

## Tableau récapitulatif
| Paradigme | Langues |
|--------------|---------------|
| **Threads du système d'exploitation + mémoire partagée** | C, C++, Java, C#, Fortran, Delphi, VB |
| **GIL/Verrouillage + Discussions** | Python, Rubis, Perl |
| **Goroutines + Chaînes** | Aller |
| **Modèle d'acteur** | Erlang, Elixir, Scala (Akka), Ruby (Ractor) |
| **async/wait + Boucle d'événement** | JavaScript, TypeScript, Rust, Swift, C#, Kotlin, Dart |
| **STM (mémoire transactionnelle logicielle)** | Haskell, Clojure |
| **Coroutines (coopérative)** | Lua, Kotlin |
| **Isole (pas de mémoire partagée)** | Fléchette, JavaScript, TypeScript |
| **Pas de concurrence native** | COBOL, Prologue, Scratch, SQL |