---
# Metadata
title: "Cross-Language Comparison — Concurrency & Parallelism"
description: "Side-by-side comparison of concurrency models across 34 programming languages."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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
# Porównanie międzyjęzykowe — współbieżność i równoległość
## Przegląd modeli współbieżności
| Język | Modelka | Kluczowy mechanizm | Wspólna pamięć? |
|---------|-------|--------------|----------------|
| Pythona | GIL + wątki | `threading`,`asyncio`| Tak (GIL ogranicza równoległość) |
| JavaScript | Pętla zdarzeń | Obietnice,`async/await`| Nie (jednowątkowy) |
| Rdza | Własność + Wyślij/Synchronizuj | `std::thread`,`async/await`, kanały | Bezpieczeństwo w czasie kompilacji |
| Idź | Gorutyny | `go func()`, kanały | Nie (przekazywanie wiadomości) |
| Jawa | Wątki dotyczące systemu operacyjnego | `Thread`,`ExecutorService`,`CompletableFuture`| Tak |
| TypeScript | Pętla zdarzeń | Obietnice,`async/await`| Nie (jednowątkowy) |
| C | wątki POSIX |  `pthread`, OpenMP | Tak (synchronizacja ręczna) |
| C++ | Wątki dotyczące systemu operacyjnego | `std::thread`,`std::async`, współprogramy | Tak (synchronizacja ręczna) |
| C# | async/czekaj | `Task`,`async/await`,`Parallel`| Tak |
| Rubin | GVL + włókna |  `Thread`, `Fiber`,`Ractor`(3.0+) | Tak (GVL), Ractor: Nie |
| Szybki | Aktorzy | `async/await`, aktorzy,`Sendable`| Nie (izolacja aktora) |
| Kotlina | Współprogramy | `suspend`,`launch`,`async`| Zależy od dyspozytora |
| PHP | Oparte na procesie | `pcntl_fork`, włókna (8.1+) | Nie (oddzielne procesy) |
| Scala | Wątki JVM | `Future`, aktorzy Akka, ZIO, Efekt kota | Tak (JVM) |
| Haskell | Zielone nici | `forkIO`, STM,`async`| Tak (STM dla bezpieczeństwa) |
| Lua | Współprogramy | `coroutine.create/resume/yield`| Nie (spółdzielnia) |
| R | Sekwencyjny + równoległy | `parallel`,`future`| Nie (oddzielne procesy) |
| Julia | Zadania + wątki | `@async`,`@threads`,`Distributed`| Tak (typy bezpieczne dla wątków) |
| Dart | Izoluje | `Isolate`,`async/await`| Nie (przekazywanie wiadomości) |
| Perł | Nici + widelec | `threads`,`fork`| Tak (i ​​wątki) |
| MATLAB | Basen równoległy | `parfor`,`spmd`,`gpuArray`| Nie (pracownicy) |
| SQL | Nie dotyczy | Baza danych obsługuje współbieżność (MVCC, blokady) | Nie dotyczy |
| Powłoka | Procesy w tle | `&`,`wait`,`xargs -P`| Nie (oddzielne procesy) |
| Fortran | Coarrays + OpenMP | `coarray`,`do concurrent`, OpenMP | Tak (pamięć współdzielona) |
| Ada | Zadania + chronione | `task`,`protected object`, spotkanie | Tak (obiekty chronione) |
| COBOL | Nie dotyczy | Przetwarzanie wsadowe, brak natywnej współbieżności | Nie dotyczy |
| Prolog | Nie dotyczy | Sekwencyjne (niektóre implementacje mają wątki) | Nie dotyczy |
| Lisp/Clojure | STM + agenci | `future`,`promise`,`core.async`, STM | Clojure: STM (ref., atomy) |
| Erlang/Eliksir | Model aktora | `spawn`, przekazywanie wiadomości,`receive`| Nie (przekazywanie wiadomości) |
| OCaml | Domena + Efekt | `Domain.spawn`, obsługa efektów (5.0+) | Nie (domeny) |
| Montaż | Nie dotyczy | Zależne od systemu operacyjnego (przerwania, wywołania systemowe) | Nie dotyczy |
| Delfy | Wątki | `TThread`,`TTask`| Tak (synchronizacja ręczna) |
| Zadrapanie | Oparte na zdarzeniach | `when green flag clicked`, transmisja | Nie (izolacja duszka) |
| VB | async/czekaj | `Async/Await`,`Task`| Tak |
## Tworzenie wątku
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

## Kluczowe wzorce współbieżności
### Producent-konsument
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

### Muteks / Blokowanie
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

## Tabela podsumowująca
| Paradygmat | Języki |
|---------|-----------|
| **Wątki systemu operacyjnego + pamięć współdzielona** | C, C++, Java, C#, Fortran, Delphi, VB |
| **GIL/blokada + wątki** | Python, Ruby, Perl |
| **Gorutyny + kanały** | Idź |
| **Model aktora** | Erlang, Elixir, Scala (Akka), Ruby (Ractor) |
| **asynchronizacja/oczekiwanie + pętla zdarzeń** | JavaScript, TypeScript, Rust, Swift, C#, Kotlin, Dart |
| **STM (programowa pamięć transakcyjna)** | Haskell, Clojure |
| **Współprace (spółdzielcze)** | Lua, Kotlin |
| **Izoluje (bez pamięci współdzielonej)** | Dart, JavaScript, TypeScript |
| **Brak natywnej współbieżności** | COBOL, Prolog, Scratch, SQL |