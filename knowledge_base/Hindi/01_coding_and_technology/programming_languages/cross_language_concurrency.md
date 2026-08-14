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
# क्रॉस-लैंग्वेज तुलना - समवर्ती और समानांतरवाद
## समवर्ती मॉडल अवलोकन
| भाषा | मॉडल | मुख्य तंत्र | शारेड मेमोरी? |
|---|-------|------------|----------------|
| पायथन | जीआईएल + धागे | `threading`,`asyncio`| हाँ (जीआईएल समानता को सीमित करता है) |
| जावास्क्रिप्ट | इवेंट लूप | वादे,`async/await`| नहीं (एकल-थ्रेडेड) |
| जंग | स्वामित्व + भेजें/सिंक करें | `std::thread`,`async/await`, चैनल | संकलन-समय सुरक्षा |
| जाओ | गोरौटाइन्स |  `go func()`, चैनल | नहीं (संदेश पास करना) |
| जावा | ओएस थ्रेड्स | `Thread`,`ExecutorService`,`CompletableFuture`| हाँ |
| टाइपस्क्रिप्ट | इवेंट लूप | वादे,`async/await`| नहीं (एकल-थ्रेडेड) |
| सी | पॉज़िक्स थ्रेड्स |  `pthread`, ओपनएमपी | हाँ (मैन्युअल सिंक) |
| सी++ | ओएस थ्रेड्स | `std::thread`,`std::async`, कोरटाइन्स | हाँ (मैन्युअल सिंक) |
| सी# | एसिंक/प्रतीक्षा | `Task`,`async/await`,`Parallel`| हाँ |
| रूबी | जीवीएल + फाइबर | `Thread`,`Fiber`,`Ractor`(3.0+) | हाँ (जीवीएल), ट्रैक्टर: नहीं |
| स्विफ्ट | अभिनेता |  `async/await`, अभिनेता,`Sendable`| नहीं (अभिनेता अलगाव) |
| कोटलिन | कोरटाइन्स | `suspend`,`launch`,`async`| डिस्पैचर पर निर्भर करता है |
| पीएचपी | प्रक्रिया आधारित |  `pcntl_fork`, फाइबर (8.1+) | नहीं (अलग-अलग प्रक्रियाएं) |
| स्काला | जेवीएम धागे |  `Future`, अक्का अभिनेता, ZIO, कैट्स इफेक्ट | हाँ (जेवीएम) |
| हास्केल | हरे धागे | `forkIO`, एसटीएम,`async`| हाँ (सुरक्षा के लिए एसटीएम) |
| लुआ | कोरटाइन्स | `coroutine.create/resume/yield`| नहीं (सहयोगी) |
| आर | अनुक्रमिक + समानांतर | `parallel`,`future`| नहीं (अलग-अलग प्रक्रियाएं) |
| जूलिया | कार्य + सूत्र | `@async`,`@threads`,`Distributed`| हाँ (थ्रेड-सुरक्षित प्रकार) |
| डार्ट | आइसोलेट्स | `Isolate`,`async/await`| नहीं (संदेश पास करना) |
| पर्ल | धागे + कांटा | `threads`,`fork`| हाँ (थ्रेड्स) |
| मतलब | समानांतर पूल | `parfor`,`spmd`,`gpuArray`| नहीं (कर्मचारी) |
| एसक्यूएल | एन/ए | डेटाबेस समवर्ती (एमवीसीसी, लॉक) संभालता है | एन/ए |
| शैल | पृष्ठभूमि प्रक्रियाएं | `&`,`wait`,`xargs -P`| नहीं (अलग-अलग प्रक्रियाएं) |
| फोरट्रान | कॉरेरेस + ओपनएमपी | `coarray`,`do concurrent`, ओपनएमपी | हाँ (साझा स्मृति) |
| अदा | कार्य + सुरक्षित | `task`,`protected object`, मुलाकात | हाँ (संरक्षित वस्तुएं) |
| कोबोल | एन/ए | बैच प्रोसेसिंग, कोई मूल संगामिति नहीं | एन/ए |
| प्रोलॉग | एन/ए | अनुक्रमिक (कुछ कार्यान्वयन में सूत्र हैं) | एन/ए |
| लिस्प/क्लोजर | एसटीएम + एजेंट | `future`,`promise`,`core.async`, STM | क्लोजर: एसटीएम (रेफ्स, परमाणु) |
| एरलांग/अमृत | अभिनेता मॉडल | `spawn`, संदेश भेजना,`receive`| नहीं (संदेश पास करना) |
| ओकैमल | डोमेन + प्रभाव |  `Domain.spawn`, प्रभाव संचालक (5.0+) | नहीं (डोमेन) |
| सभा | एन/ए | ओएस-निर्भर (व्यवधान, सिस्टम कॉल) | एन/ए |
| डेल्फ़ी | धागे | `TThread`,`TTask`| हाँ (मैन्युअल सिंक) |
| स्क्रैच | घटना-संचालित |  `when green flag clicked`, प्रसारण | नहीं (स्प्राइट आइसोलेशन) |
| वीबी | एसिंक/प्रतीक्षा | `Async/Await`,`Task`| हाँ |
## धागा निर्माण
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

## प्रमुख समवर्ती पैटर्न
### निर्माता-उपभोक्ता
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

### म्यूटेक्स/लॉकिंग
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

## सार तालिका
| प्रतिमान | भाषाएँ |
|---|----|
| **ओएस थ्रेड्स + साझा मेमोरी** | सी, सी++, जावा, सी#, फोरट्रान, डेल्फ़ी, वीबी |
| **जीआईएल/लॉक + थ्रेड्स** | पायथन, रूबी, पर्ल |
| **गोरोइन्स + चैनल** | जाओ |
| **अभिनेता मॉडल** | एरलांग, एलिक्सिर, स्काला (अक्का), रूबी (रैक्टर) |
| **async/प्रतीक्षा + इवेंट लूप** | जावास्क्रिप्ट, टाइपस्क्रिप्ट, रस्ट, स्विफ्ट, सी#, कोटलिन, डार्ट |
| **एसटीएम (सॉफ्टवेयर ट्रांजेक्शनल मेमोरी)** | हास्केल, क्लोजर |
| **कोरआउटिंस (सहकारी)** | लुआ, कोटलिन |
| **पृथक (कोई साझा स्मृति नहीं)** | डार्ट, जावास्क्रिप्ट, टाइपस्क्रिप्ट |
| **कोई मूल संगामिति नहीं** | कोबोल, प्रोलॉग, स्क्रैच, एसक्यूएल |