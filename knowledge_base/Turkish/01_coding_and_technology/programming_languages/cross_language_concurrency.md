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

# Diller Arası Karşılaştırma - Eşzamanlılık ve Paralellik
## Eşzamanlılık Modellerine Genel Bakış
| Dil | Modeli | Anahtar Mekanizması | Paylaşılan Bellek? |
|----------|----------|---------------|-----|
| Python | GIL + konuları | `threading`,`asyncio`| Evet (GIL paralelliği sınırlıyor) |
| JavaScript | Olay döngüsü | Sözler,`async/await`| Hayır (tek iş parçacıklı) |
| Pas | Sahiplik + Gönder/Senkronizasyon | `std::thread`,`async/await`, kanallar | Derleme zamanı güvenliği |
| Git | Goroutinler |  `go func()`, kanallar | Hayır (mesaj geçiyor) |
| Java | işletim sistemi konuları | `Thread`,`ExecutorService`,`CompletableFuture`| Evet |
| TypeScript | Olay döngüsü | Sözler,`async/await`| Hayır (tek iş parçacıklı) |
| C | POSIX konuları |  `pthread`, OpenMP | Evet (manuel senkronizasyon) |
| C++ | işletim sistemi konuları | `std::thread`,`std::async`, eşyordamlar | Evet (manuel senkronizasyon) |
| C# | eşzamansız/beklemede | `Task`,`async/await`,`Parallel`| Evet |
| Yakut | GVL + elyaflar | `Thread`,`Fiber`,`Ractor`(3,0+) | Evet (GVL), Raktör: Hayır |
| Hızlı | Aktörler | `async/await`, aktörler,`Sendable`| Hayır (aktör izolasyonu) |
| Kotlin | Eşyordamlar | `suspend`,`launch`,`async`| Göndericiye bağlıdır |
| PHP | Süreç bazlı | `pcntl_fork`, elyaflar (8.1+) | Hayır (ayrı işlemler) |
| Ölçek | JVM konuları | `Future`, Akka aktörleri, ZIO, Kedi Etkisi | Evet (JVM) |
| Haskell | Yeşil iplikler | `forkIO`, STM,`async`| Evet (güvenlik için STM) |
| Lua | Eşyordamlar | `coroutine.create/resume/yield`| Hayır (kooperatif) |
| R | Sıralı + paralel | `parallel`,`future`| Hayır (ayrı işlemler) |
| Julia | Görevler + ileti dizileri | `@async`,`@threads`,`Distributed`| Evet (iş parçacığı güvenli türler) |
| Dart | İzolatlar | `Isolate`,`async/await`| Hayır (mesaj geçiyor) |
| Perl | Konular + çatal | `threads`,`fork`| Evet (konular) |
| MATLAB | Paralel havuz | `parfor`,`spmd`,`gpuArray`| Hayır (işçiler) |
| SQL | Yok | Veritabanı eşzamanlılığı yönetir (MVCC, kilitler) | Yok |
| Kabuk | Arka plan süreçleri | `&`,`wait`,`xargs -P`| Hayır (ayrı işlemler) |
| Fortran | Coarray'ler + OpenMP | `coarray`,`do concurrent`, OpenMP | Evet (paylaşılan hafıza) |
| Ada | Görevler + korumalı | `task`,`protected object`, randevu | Evet (korunan nesneler) |
| KOBOL | Yok | Toplu işleme, yerel eşzamanlılık yok | Yok |
| Giriş | Yok | Sıralı (bazı uygulamaların iş parçacıkları vardır) | Yok |
| Lisp/Clojure | STM + acenteleri | `future`,`promise`,`core.async`, STM | Clojure: STM (referanslar, atomlar) |
| Erlang/İksir | Aktör modeli |  `spawn`, mesaj aktarma,`receive`| Hayır (mesaj geçiyor) |
| OCaml | Etki Alanı + Efekt | `Domain.spawn`, efekt işleyiciler (5.0+) | Hayır (alan adları) |
| Montaj | Yok | İşletim sistemine bağımlı (kesintiler, sistem çağrıları) | Yok |
| Delfi | Konular | `TThread`,`TTask`| Evet (manuel senkronizasyon) |
| Çizik | Olay odaklı |  `when green flag clicked`, yayın | Hayır (sprite izolasyonu) |
| VB | eşzamansız/beklemede | `Async/Await`,`Task`| Evet |
## Konu Oluşturma
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

## Anahtar Eşzamanlılık Modelleri
### Üretici-Tüketici
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

### Mutex / Kilitleme
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

## Özet Tablosu
| Paradigma | Diller |
|----------|---------------|
| **İşletim Sistemi Konuları + Paylaşılan Bellek** | C, C++, Java, C#, Fortran, Delphi, VB |
| **GIL/Kilit + Konular** | Python, Yakut, Perl |
| **Goroutinler + Kanallar** | Git |
| **Oyuncu Modeli** | Erlang, İksir, Scala (Akka), Yakut (Raktör) |
| **eşzamansız/beklemede + Olay Döngüsü** | JavaScript, TypeScript, Rust, Swift, C#, Kotlin, Dart |
| **STM (Yazılım İşlemsel Belleği)** | Haskell, Clojure |
| **Ortak rutinler (işbirlikçi)** | Lua, Kotlin |
| **İzolatlar (paylaşılan bellek yok)** | Dart, JavaScript, TypeScript |
| **Yerel eşzamanlılık yok** | COBOL, Prolog, Scratch, SQL |