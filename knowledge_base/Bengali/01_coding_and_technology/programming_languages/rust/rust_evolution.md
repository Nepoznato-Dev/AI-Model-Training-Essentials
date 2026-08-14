---
# Metadata
title: "Rust — Version History & Evolution"
description: "Comprehensive version history and evolution of Rust from early development to modern Rust."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [rust, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# মরিচা — সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | মুক্তির তারিখ | মূল থিম |
|---------|---------------|------------|
| 0.1 | জানুয়ারী 2012 | প্রথম কম্পাইলার (rustc), টাস্ক-ভিত্তিক সঙ্গতি |
| 0.5 | 2012 | বৈশিষ্ট্য-ভিত্তিক টাইপ সিস্টেম আকার নেয় |
| 0.6 | 2012 |`@`পরিচালিত বাক্স অপসারণ |
| 0.7 | 2013 | `@`সরানো হয়েছে, মালিকানাধীন বাক্সগুলির জন্য`~`|
| 0.8 | 2013 | লাইফটাইম টীকা,`&mut`|
| 0.9 | জানুয়ারী 2014 | চূড়ান্ত প্রি-1.0 পরিষ্কার |
| 0.10 | ফেব্রুয়ারী 2014 | সর্বশেষ প্রি-1.0 রিলিজ |
| 0.11 | এপ্রিল 2014 | `Box<T>``~T` প্রতিস্থাপন করে |
| 0.12 | মে 2014 | `io`মডিউল পুনর্লিখন শুরু হয় |
| 1.0 | মে 15, 2015 | **স্থিতিশীল প্রকাশ** — "মরিচা 1.0" |
| 1.10 | আগস্ট 2016 | `?`ত্রুটি প্রচার (`try!` →`?`হিসাবে) |
| 1.15 | ফেব্রুয়ারী 2017 |`impl Trait`প্রস্তুতির সাথে স্থিতিশীল অবস্থায় প্রথম মরিচা |
| 1.18 | জুন 2017 | `pub(crate)`, ক্রমবর্ধমান সংকলন |
| 1.20 | অক্টোবর 2017 | যুক্ত ধ্রুবক |
| 1.26 | মে 2018 | `impl Trait`যুক্তি/রিটার্ন পজিশনে |
| 1.28 | সেপ্টেম্বর 2018 | গ্লোবাল বরাদ্দকারী |
| 1.31 | ডিসেম্বর 2018 | **মরিচা 2018 সংস্করণ** — মডিউল,`dyn Trait`|
| 1.34 | এপ্রিল 2019 | বিকল্প রেজিস্ট্রি |
| 1.39 | নভেম্বর 2019 | `async/await`স্থিতিশীল |
| 1.44 | জুলাই 2020 | ডায়াগনস্টিক উন্নতি |
| 1.51 | এপ্রিল 2021 | `const`জেনেরিক (MVP) |
| 1.56 | অক্টোবর 2021 | **মরিচা 2021 সংস্করণ** — বন্ধ, IntoIterator |
| 1.59 | ফেব্রুয়ারী 2022 | ইনলাইন সমাবেশ |
| 1.62 | জুন 2022 |  enums জন্য`#[default]`|
| 1.65 | ডিসেম্বর 2022 | `let else`|
| 1.68 | মার্চ 2023 | `#[ffi_pure]`, প্রোফাইল-নির্দেশিত অপ্টিমাইজেশান |
| 1.70 | জুন 2023 | বিচ্ছিন্ন`crates.io`নির্ভরতা |
| 1.74 | নভেম্বর 2023 | কার্গো অফলাইন মোড |
| 1.76 | ফেব্রুয়ারী 2024 | **মরিচা 2024 সংস্করণ** —`gen`ব্লক,`unsafe extern`|
| 1.79 | জুন 2024 | `LazyCell`,`LazyLock`|
| 1.82 | অক্টোবর 2024 | `extern`ব্লকে`unsafe`প্রয়োজন |
| 1.85 | ফেব্রুয়ারী 2025 | মরিচা 2024 সংস্করণ স্থিতিশীল |
## প্রধান মাইলফলক
### প্রাক-1.0 (2010-2015)
- **2010**: মজিলার গ্রেডন হোয়ারের সাইড প্রজেক্ট ট্র্যাকশন লাভ করেছে
- **2012**: প্রথম পাবলিক কম্পাইলার; টাইপ সিস্টেম বড় নতুন ডিজাইনের মধ্য দিয়ে যায়
- **2013**: মালিকানা মডেল স্ফটিক; `@`বাক্সগুলি সরানো হয়েছে৷
- **2014**: মরিচা আরএফসি প্রক্রিয়া আনুষ্ঠানিক; সম্প্রদায় বৃদ্ধি পায়
- **2015**: **1.0** — স্থিতিশীলতার গ্যারান্টি; "শূন্য খরচের বিমূর্ততা"
### বৃদ্ধির বছর (2015-2019)
- **2015**: কার্গো স্ট্যান্ডার্ড প্যাকেজ ম্যানেজার হয়ে ওঠে
- **2018**: **মরিচা 2018 সংস্করণ** — মডিউল সিস্টেম ওভারহল,`dyn Trait`,`impl Trait`
- **2019**:`async/await`স্থিতিশীল - অ্যাসিঙ্ক ইকোসিস্টেম শুরু হয়
### পরিপক্কতা (2020-বর্তমান)
- **2021**: **মরিচা 2021 সংস্করণ** — ক্লোজারে ক্ষেত্রগুলিকে দ্ব্যর্থিত করুন, অ্যারেগুলির জন্য `IntoIterator`
- **2024**: **মরিচা 2024 সংস্করণ** —`gen`ব্লক,`unsafe extern`প্রয়োজনীয়তা
- **2025**: লিনাক্স কার্নেল, অ্যান্ড্রয়েড, উইন্ডোজ, AWS অবকাঠামোতে মরিচা
## সংস্করণ সিস্টেম
```
Rust 2015:  The baseline (1.0)
Rust 2018:  Module system, async/await prep, dyn Trait
Rust 2021:  Closure changes, IntoIterator, panic macros
Rust 2024:  gen blocks, unsafe extern, tail expressions

Key principle: Editions are opt-in, never break existing code.
Old editions always compile. New editions add features.
```

## মালিকানার বিবর্তন
```
2010: GC-based, like Erlang
2011: Region-based lifetimes proposed
2012: Ownership model emerges (unique, shared, owned)
2013: Simplified to &T / &mut T / Box<T>
2014: Box<T> replaces ~T; Rc<T> for shared ownership
2015: 1.0 — ownership model finalized
2018: Non-Lexical Lifetimes (NLL) in Rust 2018
2021: IntoIterator for arrays (was blocked by edition concerns)
2024: Further NLL improvements
```

## অ্যাসিঙ্ক বিবর্তন
```
2018: futures 0.1 — early async with manual polling
2019: async/await syntax (Rust 1.39)
2019: tokio 0.2 — async runtime
2020: async-std — std-like async API
2021: tokio 1.0 — stable async runtime
2023: async fn in traits (Rust 1.75)
2024: async closures, improved Send bounds
```

## ইকোসিস্টেম বৃদ্ধি
```
2015: crates.io launches (~2,000 crates)
2018: Rust most loved language (Stack Overflow survey)
2019: 30,000 crates on crates.io
2021: Most admired language (6th consecutive year)
2023: 130,000+ crates
2025: Used in Linux kernel, Android, Windows, Chromium, AWS, Cloudflare, Discord, Dropbox
```

## মূল RFC
| RFC | বছর | বৈশিষ্ট্য |
|------|------|---------|
| 25 | 2013 | প্যাটার্ন ম্যাচিং |
| 153 | 2014 | `Result`প্রকার |
| 217 | 2014 | `?`(চেষ্টা) অপারেটর |
| 460 | 2016 | `?``try!` প্রতিস্থাপন করে |
| 1210 | 2015 | `impl Trait`|
| 1414 | 2016 | মরিচা 2018 সংস্করণ |
| 2394 | 2018 | `async/await`|
| 2515 | 2018 | `const`জেনেরিক |
| 3013 | 2020 | শর্তাধীন সংকলন পরীক্ষা করা হচ্ছে |
| 3517 | 2023 | `gen`ব্লক |