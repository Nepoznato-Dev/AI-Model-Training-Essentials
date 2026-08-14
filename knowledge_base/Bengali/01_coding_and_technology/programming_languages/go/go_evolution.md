---
# Metadata
title: "Go — Version History & Evolution"
description: "Comprehensive version history and evolution of Go from 1.0 to modern Go."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [go, golang, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# যান — সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | মুক্তির তারিখ | মূল থিম |
|---------|---------------|------------|
| 1.0 | মার্চ 2012 | প্রথম স্থিতিশীল মুক্তি |
| 1.1 | মে 2013 | কর্মক্ষমতা, রেস ডিটেক্টর |
| 1.3 | জুন 2014 | নেটওয়ার্ক পোলিং, ক্রিপ্টো/টিএলএস |
| 1.4 | ডিসেম্বর 2014 | Go এর সাথে বুটস্ট্র্যাপ (স্ব-হোস্টিং) |
| 1.5 | আগস্ট 2015 | **সমসাময়িক GC**, বাধা লিখুন |
| 1.7 | আগস্ট 2016 | `context`প্যাকেজ,`testing`সাবটেস্ট |
| 1.8 | ফেব্রুয়ারী 2017 | `http.Server.Shutdown`, প্লাগইন |
| 1.9 | আগস্ট 2017 | টাইপ উপনাম, সমান্তরাল`make`|
| 1.10 | ফেব্রুয়ারী 2018 | `database/sql`সংযোগ পুল |
| 1.11 | আগস্ট 2018 | **মডিউলে যান**,`go mod`|
| 1.12 | ফেব্রুয়ারী 2019 | TLS 1.3, মডিউল সংস্করণ |
| 1.13 | সেপ্টেম্বর 2019 | `errors.Is/As`, সংখ্যার আক্ষরিক`0b`,`0o`|
| 1.14 | ফেব্রুয়ারী 2020 | **উইন্ডোজে ওভারল্যাপড I/O**, গোরুটিন প্রিম্পশন |
| 1.15 | আগস্ট 2020 | `time.Ticker`/`Timer`রিসেট, মডিউল প্রক্সি |
| 1.16 | ফেব্রুয়ারী 2021 | `embed`প্যাকেজ,`io/fs`, ডিফল্টরূপে মডিউল-সচেতন |
| 1.17 | আগস্ট 2021 | স্লাইস-টু-অ্যারে রূপান্তর,`unsafe.Slice`|
| 1.18 | মার্চ 2022 | **জেনারিকস**, ফাজিং, ওয়ার্কস্পেস |
| 1.19 | আগস্ট 2022 | ডক মন্তব্য, মেমরি মডেল সংশোধন |
| 1.20 | ফেব্রুয়ারী 2023 | `errors.Join`, প্রোফাইল-নির্দেশিত অপ্টিমাইজেশান |
| 1.21 | আগস্ট 2023 | **`slog`**,`min/max`বিল্টইন,`maps/slices`|
| 1.22 | ফেব্রুয়ারী 2024 | পূর্ণসংখ্যার উপর পরিসীমা, বর্ধিত রাউটিং |
| 1.23 | আগস্ট 2024 | ইটারেটর (`iter`) প্যাকেজ, টাইমার পরিবর্তন |
| 1.24 | ফেব্রুয়ারী 2025 | `weak`প্যাকেজ, উন্নত মানচিত্র |
## প্রধান মাইলফলক
### দ্য বিগিনিং (2009-2012)
- **2009**: গুগল দ্বারা ঘোষণা করা হয়েছে (রবার্ট গ্রিজেমার, রব পাইক, কেন থম্পসন)
- **2012**: **Go 1.0** — "The Go 1 সামঞ্জস্যের প্রতিশ্রুতি"
### কর্মক্ষমতা এবং টুলিং (2012-2018)
- **1.1**: 30%+ কর্মক্ষমতা উন্নতি; রেস ডিটেক্টর
- **1.5**: সমসাময়িক আবর্জনা সংগ্রহকারী (GC পজ মিলিসেকেন্ড থেকে মাইক্রোসেকেন্ডে নেমে আসে)
- **1.5**: Go কম্পাইলার বুটস্ট্র্যাপড — Go-তে লেখা (আর কোন C)
- **1.7**:`context`প্যাকেজ স্ট্যান্ডার্ড হয়ে যায়
### মডিউল এবং ইকোসিস্টেম (2018-2021)
- **1.11**: **গো মডিউল** — অফিসিয়াল নির্ভরতা ব্যবস্থাপনা
- **1.13**:`errors.Is/As`— ত্রুটি মোড়ানো মূর্খ হয়ে ওঠে
- **1.16**:`embed`প্যাকেজ — কম্পাইলের সময় ফাইল এম্বেড করুন
### মডার্ন গো (2022-বর্তমান)
- **1.18**: **জেনারিক** — সীমাবদ্ধতা সহ প্যারামিটার টাইপ করুন
- **1.21**:`slog`— stdlib-এ কাঠামোবদ্ধ লগিং; `min/max`বিল্টইন
- **1.22**: পূর্ণসংখ্যার উপর পরিসীমা (`for i := range 10`)
- **1.23**: ইটারেটর প্যাকেজ — stdlib-এ অলস মূল্যায়ন
## জেনেরিক জার্নি
```
2010: "Go doesn't need generics" (early stance)
2016: Go generics proposal discussions begin
2018: Type parameters design draft published
2020: Go 2 generics proposal (draft designs)
2022: Go 1.18 — generics land! Type parameters, constraints
2023: Generic code patterns emerge (slices, maps packages)
2024: Community adapts — generic data structures, algorithms
```

## ত্রুটি হ্যান্ডলিং দর্শন
```
1.0:     Explicit error returns — "errors are values"
1.13:    Error wrapping with %w — "inspect and unwrap"
1.20:    errors.Join — multiple errors
Future:  go2 proposal for try/handle (not yet adopted)
```

## কনকারেন্সি বিবর্তন
```
1.0:  Goroutines + channels — CSP-inspired
1.1:  Race detector
1.4:  Non-blocking syscalls (net poller)
1.5:  Concurrent GC
1.7:  context package for cancellation
1.14: Cooperative goroutine preemption (signals)
1.21: Synchronization improvements
1.23: iter package — iterator pattern
```

## যান সামঞ্জস্যতার প্রতিশ্রুতি
```
Go 1.0 (2012): "Go 1 will be available for a long time.
  Compatibility is important. Programs that work at Go 1
  will continue to work at every subsequent Go 1 release."

This means:
- No breaking changes to the language spec
- No breaking changes to the standard library
- Only additive changes
- Forward compatibility guaranteed
```

## ইকোসিস্টেম বৃদ্ধি
```
2012: Go 1.0 — basic stdlib, no package manager
2014: dep (early dependency management experiments)
2018: Go modules — official solution
2019: Go used by Uber, Twitch, Dropbox, Cloudflare
2022: Generics — opens new library design patterns
2023: Go in Kubernetes, Docker, Terraform, Hugo
2025: Top 10 most used language; cloud-native standard
```

## কর্মক্ষমতা বিবর্তন
```
Go 1.0:  Baseline
Go 1.1:  ~30% faster (register-based calling prep)
Go 1.5:  Concurrent GC (pause time: ms → μs)
Go 1.7:  SSA backend (15-30% faster)
Go 1.11: PGO experiments
Go 1.13: Faster map operations
Go 1.18: Generics (initial overhead, optimized in 1.19+)
Go 1.20: Profile-guided optimization
Go 1.22: Faster crypto, improved compiler
```
