<!--
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

-->
# So sánh đa ngôn ngữ - Đồng thời & Song song
## Tổng quan về mô hình đồng thời
| Ngôn ngữ | Người mẫu | Cơ chế chính | Bộ nhớ chia sẻ? |
|----------|-------|---------------|-------|
| Python | GIL + chủ đề | `threading`,`asyncio`| Có (GIL giới hạn tính song song) |
| JavaScript | Vòng lặp sự kiện | Lời hứa,`async/await`| Không (đơn luồng) |
| rỉ sét | Quyền sở hữu + Gửi/Đồng bộ hóa | `std::thread`,`async/await`, kênh | An toàn thời gian biên dịch |
| Đi | Goroutine | `go func()`, kênh | Không (chuyển tin nhắn) |
| Java | Chủ đề hệ điều hành | `Thread`,`ExecutorService`,`CompletableFuture`| Có |
| TypeScript | Vòng lặp sự kiện | Lời hứa,`async/await`| Không (đơn luồng) |
| C | Chủ đề POSIX | `pthread`, OpenMP | Có (đồng bộ thủ công) |
| C++ | Chủ đề hệ điều hành | `std::thread`,`std::async`, coroutine | Có (đồng bộ thủ công) |
| C# | không đồng bộ/đang chờ | `Task`,`async/await`,`Parallel`| Có |
| Ruby | GVL + sợi | `Thread`,`Fiber`,`Ractor`(3.0+) | Có (GVL), Ractor: Không |
| Nhanh | Diễn viên | `async/await`, diễn viên,`Sendable`| Không (cách ly diễn viên) |
| Kotlin | Coroutine | `suspend`,`launch`,`async`| Phụ thuộc vào người điều phối |
| PHP | Dựa trên quy trình | `pcntl_fork`, sợi (8.1+) | Không (các quy trình riêng biệt) |
| Scala | Chủ đề JVM | `Future`, diễn viên Akka, ZIO, Hiệu ứng mèo | Có (JVM) |
| Haskell | Chủ đề xanh | `forkIO`, STM,`async`| Có (STM để đảm bảo an toàn) |
| Lua | Coroutine | `coroutine.create/resume/yield`| Không (hợp tác) |
| R | Tuần tự + song song | `parallel`,`future`| Không (các quy trình riêng biệt) |
| Julia | Nhiệm vụ + chủ đề | `@async`,`@threads`,`Distributed`| Có (loại an toàn theo luồng) |
| Phi tiêu | Cô lập | `Isolate`,`async/await`| Không (chuyển tin nhắn) |
| Perl | Chủ đề + nĩa | `threads`,`fork`| Có (ithreads) |
| MATLAB | Bể song song | `parfor`,`spmd`,`gpuArray`| Không (công nhân) |
| SQL | Không áp dụng | Cơ sở dữ liệu xử lý đồng thời (MVCC, khóa) | Không áp dụng |
| Vỏ | Quá trình nền | `&`,`wait`,`xargs -P`| Không (các quy trình riêng biệt) |
| Fortran | Coarrays + OpenMP | `coarray`,`do concurrent`, OpenMP | Có (bộ nhớ dùng chung) |
| Ada | Nhiệm vụ + được bảo vệ | `task`,`protected object`, điểm hẹn | Có (đối tượng được bảo vệ) |
| COBOL | Không áp dụng | Xử lý hàng loạt, không có đồng thời | Không áp dụng |
| Prolog | Không áp dụng | Tuần tự (một số triển khai có chủ đề) | Không áp dụng |
| Lisp/Clojure | STM + đại lý | `future`,`promise`,`core.async`, STM | Clojure: STM (refs, nguyên tử) |
| Erlang/Thuốc tiên | Người mẫu diễn viên | `spawn`, truyền tin nhắn,`receive`| Không (chuyển tin nhắn) |
| OCaml | Tên miền + Hiệu ứng | `Domain.spawn`, trình xử lý hiệu ứng (5.0+) | Không (tên miền) |
| Hội | Không áp dụng | Phụ thuộc vào hệ điều hành (ngắt, cuộc gọi hệ thống) | Không áp dụng |
| Delphi | Chủ đề | `TThread`,`TTask`| Có (đồng bộ thủ công) |
| Cào | Hướng sự kiện | `when green flag clicked`, phát sóng | Không (cách ly sprite) |
| VB | không đồng bộ/đang chờ | `Async/Await`,`Task`| Có |
## Tạo chủ đề
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

## Các mẫu đồng thời chính
### Nhà sản xuất-Người tiêu dùng
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

### Mutex / Khóa
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

## Bảng tóm tắt
| Mô hình | Ngôn ngữ |
|----------|----------|
| **Chủ đề hệ điều hành + Bộ nhớ dùng chung** | C, C++, Java, C#, Fortran, Delphi, VB |
| **GIL/Khóa + Chủ đề** | Python, Ruby, Perl |
| **Goutines + Kênh** | Đi |
| **Người mẫu diễn viên** | Erlang, Elixir, Scala (Akka), Ruby (Ractor) |
| **async/await + Vòng lặp sự kiện** | JavaScript, TypeScript, Rust, Swift, C#, Kotlin, Dart |
| **STM (Bộ nhớ giao dịch phần mềm)** | Haskell, Clojure |
| **Coroutines (hợp tác)** | Lua, Kotlin |
| **Cách ly (không có bộ nhớ dùng chung)** | Phi tiêu, JavaScript, TypeScript |
| **Không có tính đồng thời gốc** | COBOL, Prolog, Scratch, SQL |