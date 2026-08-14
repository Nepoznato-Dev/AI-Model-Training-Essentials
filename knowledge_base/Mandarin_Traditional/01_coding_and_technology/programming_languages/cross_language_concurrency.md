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
# 跨語言比較－並發與平行
## 並發模型概述
|語言 |型號|關鍵機制|共享記憶體？ |
|----------|------|----------------|----------------|
|蟒蛇 | GIL + 線程 |`threading`,`asyncio`|是（GIL 限制並行性）|
| JavaScript |事件循環|承諾，`async/await` |否（單線程）|
|鐵鏽|所有權+發送/同步| `std::thread`、`async/await`、通道 |編譯時安全 |
|去 | Goroutines | `go func()`，頻道 |否（訊息傳遞）|
| 爪哇 |作業系統線程 | `Thread`、`ExecutorService`、`CompletableFuture` |是的 |
|打字稿 |事件循環|承諾，`async/await` |否（單線程）|
| C | POSIX 線程 | `pthread`，OpenMP |是（手動同步）|
| C++ |作業系統執行緒 |`std::thread`、`std::async`、協程 |是（手動同步）|
| C# |非同步/等待 | `Task`、`async/await`、`Parallel` |是的 |
|紅寶石 | GVL + 纖維 | `Thread`、`Fiber`、`Ractor` (3.0+) |是（GVL），Ractor：否 |
|斯威夫特 |演員 |`async/await`, 演員,`Sendable`|否（演員隔離）|
|科特林 |協程 | `suspend`、`launch`、`async` |取決於調度員 |
| PHP |基於流程| `pcntl_fork`，纖維（8.1+）|否（單獨的進程）|
|斯卡拉 | JVM 線程 | `Future`、Akka 演員、ZIO、貓效果 |是（JVM）|
|哈斯克爾 |綠色線程| `forkIO`、STM、`async` |是（STM 為了安全）|
|盧阿 |協程 |`coroutine.create/resume/yield`|否（合作）|
|右 |順序+並行| `parallel`、`future` |否（單獨的進程）|
|茱莉亞 |任務+執行緒| `@async`、`@threads`、`Distributed` |是（執行緒安全型別）|
|飛鏢 |隔離 | `Isolate`、`async/await` |否（訊息傳遞）|
|珀爾|線程+叉| `threads`、`fork` |是（ithreads）|
| MATLAB |平行池| `parfor`、`spmd`、`gpuArray` |否（工人）|
| SQL |不適用 |資料庫處理並發（MVCC、鎖）|不適用 |
|殼牌|後台進程| `&`、`wait`、`xargs -P` |否（單獨的進程）|
|語言 | Coarrays + OpenMP | `coarray`、`do concurrent`、OpenMP |是（共享記憶體）|
|艾達 |任務+受保護|`task`,`protected object`, 會合 |是（受保護物件）|
|科博爾 |不適用 |批處理，無原生並發 |不適用 |
|序言|不適用 |順序（某些實作有線程）|不適用 |
| Lisp/Clojure | STM+代理商| `future`、`promise`、`core.async`、STM | Clojure：STM（引用、原子）|
| Erlang/Elixir |演員模型|`spawn`，訊息傳遞，`receive` |否（訊息傳遞）|
| OCaml |領域+效果|`Domain.spawn`，效果處理程序 (5.0+) |否（域）|
|組裝|不適用 |依賴作業系統（中斷、系統呼叫）|不適用 |
|德爾福|主題 | `TThread`、`TTask` |是（手動同步）|
|刮刮|事件驅動程式| `when green flag clicked`，廣播|否（精靈隔離）|
| VB |非同步/等待 | `Async/Await`、`Task` |是的 |
## 線程創建
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

## 關鍵並發模式
### 生產者-消費者
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

### 互斥/鎖定
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

## 總結表
|范式|语言 |
|----------|------------|
| **作業系統執行緒 + 共享記憶體** | C、C++、Java、C#、Fortran、Delphi、VB |
| **GIL/鎖 + 線程** | Python、Ruby、Perl |
| **Goroutine + 頻道** |去 |
| **演員模特兒** | Erlang、Elixir、Scala (Akka)、Ruby (Ractor) |
| **非同步/等待+事件循環** | JavaScript、TypeScript、Rust、Swift、C#、Kotlin、Dart |
| **STM（軟體事務記憶體）** | Haskell、Clojure |
| **協程（合作）** | Lua、Kotlin |
| **隔離（無共享記憶體）** | Dart、JavaScript、TypeScript |
| **沒有本機並發** | COBOL、Prolog、Scratch、SQL |