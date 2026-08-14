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

# Cross-Language Comparison — Concurrency & Parallelism

## Concurrency Models Overview

| Language | Model | Key Mechanism | Shared Memory? |
|----------|-------|---------------|----------------|
| Python | GIL + threads | `threading`, `asyncio` | Yes (GIL limits parallelism) |
| JavaScript | Event loop | Promises, `async/await` | No (single-threaded) |
| Rust | Ownership + Send/Sync | `std::thread`, `async/await`, channels | Compile-time safety |
| Go | Goroutines | `go func()`, channels | No (message passing) |
| Java | OS threads | `Thread`, `ExecutorService`, `CompletableFuture` | Yes |
| TypeScript | Event loop | Promises, `async/await` | No (single-threaded) |
| C | POSIX threads | `pthread`, OpenMP | Yes (manual sync) |
| C++ | OS threads | `std::thread`, `std::async`, coroutines | Yes (manual sync) |
| C# | async/await | `Task`, `async/await`, `Parallel` | Yes |
| Ruby | GVL + fibers | `Thread`, `Fiber`, `Ractor` (3.0+) | Yes (GVL), Ractor: No |
| Swift | Actors | `async/await`, actors, `Sendable` | No (actor isolation) |
| Kotlin | Coroutines | `suspend`, `launch`, `async` | Depends on dispatcher |
| PHP | Process-based | `pcntl_fork`, fibers (8.1+) | No (separate processes) |
| Scala | JVM threads | `Future`, Akka actors, ZIO, Cats Effect | Yes (JVM) |
| Haskell | Green threads | `forkIO`, STM, `async` | Yes (STM for safety) |
| Lua | Coroutines | `coroutine.create/resume/yield` | No (cooperative) |
| R | Sequential + parallel | `parallel`, `future` | No (separate processes) |
| Julia | Tasks + threads | `@async`, `@threads`, `Distributed` | Yes (thread-safe types) |
| Dart | Isolates | `Isolate`, `async/await` | No (message passing) |
| Perl | Threads + fork | `threads`, `fork` | Yes (ithreads) |
| MATLAB | Parallel pool | `parfor`, `spmd`, `gpuArray` | No (workers) |
| SQL | N/A | Database handles concurrency (MVCC, locks) | N/A |
| Shell | Background processes | `&`, `wait`, `xargs -P` | No (separate processes) |
| Fortran | Coarrays + OpenMP | `coarray`, `do concurrent`, OpenMP | Yes (shared memory) |
| Ada | Tasks + protected | `task`, `protected object`, rendezvous | Yes (protected objects) |
| COBOL | N/A | Batch processing, no native concurrency | N/A |
| Prolog | N/A | Sequential (some implementations have threads) | N/A |
| Lisp/Clojure | STM + agents | `future`, `promise`, `core.async`, STM | Clojure: STM (refs, atoms) |
| Erlang/Elixir | Actor model | `spawn`, message passing, `receive` | No (message passing) |
| OCaml | Domain + Effect | `Domain.spawn`, effect handlers (5.0+) | No (domains) |
| Assembly | N/A | OS-dependent (interrupts, system calls) | N/A |
| Delphi | Threads | `TThread`, `TTask` | Yes (manual sync) |
| Scratch | Event-driven | `when green flag clicked`, broadcast | No (sprite isolation) |
| VB | async/await | `Async/Await`, `Task` | Yes |

## Thread Creation

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

## Key Concurrency Patterns

### Producer-Consumer

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

### Mutex / Locking

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

## Summary Table

| Paradigm | Languages |
|----------|-----------|
| **OS Threads + Shared Memory** | C, C++, Java, C#, Fortran, Delphi, VB |
| **GIL/Lock + Threads** | Python, Ruby, Perl |
| **Goroutines + Channels** | Go |
| **Actor Model** | Erlang, Elixir, Scala (Akka), Ruby (Ractor) |
| **async/await + Event Loop** | JavaScript, TypeScript, Rust, Swift, C#, Kotlin, Dart |
| **STM (Software Transactional Memory)** | Haskell, Clojure |
| **Coroutines (cooperative)** | Lua, Kotlin |
| **Isolates (no shared memory)** | Dart, JavaScript, TypeScript |
| **No native concurrency** | COBOL, Prolog, Scratch, SQL |
