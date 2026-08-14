---
# Metadata
title: "Perl — Version History & Evolution"
description: "Comprehensive version history and evolution of Perl from 1.0 to modern Perl."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [perl, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# পার্ল — সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| 1.0 | 1987 | প্রাথমিক প্রকাশ (ল্যারি ওয়াল) |
| 2.0 | 1988 | `study`ফাংশন, আরও ভাল রেজেক্স |
| 3.0 | 1989 | `my`ভেরিয়েবল (লেক্সিক্যাল স্কোপিং) |
| 4.0 | 1991 | `O'Reilly`"প্রোগ্রামিং পার্ল" (উট বই) |
| 5.0 | 1994 | **মেজর**: মডিউল, রেফারেন্স, ক্লোজার,`use strict`|
| 5.6 | 2000 | `our`,`state`(পরে),`v-strings`,`y2k`সংশোধন |
| 5.8 | 2002 | **ইউনিকোড সমর্থন**,`ithreads`,`open`প্রাগমা |
| 5.10 | 2007 | `say`,`//`সংজ্ঞায়িত-বা,`given`/`when`,`~~`স্মার্টম্যাচ |
| 5.12 | 2010 | `package NAME VERSION`,`...`(ইয়াদা-ইয়াদা), ইউনিকোড 5.2 |
| 5.14 | 2011 | `s///r`(অ-ধ্বংসাত্মক প্রতিস্থাপন),`package`উন্নতি |
| 5.16 | 2012 | `__SUB__`,`unicode_eval`|
| 5.18 | 2013 | আভিধানিক`$_`, হ্যাশ র্যান্ডমাইজেশন,`my`শর্তসাপেক্ষে |
| 5.20 | 2014 | **সাবরুটিন স্বাক্ষর** (পরীক্ষামূলক),`%hash`স্লাইসিং |
| 5.22 | 2015 | `&`ডিরেফারেন্সিং,`<<>>`(নিরাপদ খোলা) |
| 5.24 | 2016 | পোস্টফিক্স ডিরেফারেন্সিং স্থিতিশীল |
| 5.26 | 2017 | **`while` এ লেক্সিকাল`$_`**,`@INC`এ`.`সরানো হয়েছে (নিরাপত্তা) |
| 5.28 | 2018 | ইউনিকোড 10.0,`delete`কী/মান স্লাইসে |
| 5.30 | 2019 | `for`/`while`শর্তে`my`|
| 5.32 | 2020 | `isa`অপারেটর, ইউনিকোড 13.0 |
| 5.34 | 2021 | `try`/`catch`(পরীক্ষামূলক),`defer`ব্লক |
| 5.36 | 2022 | **`use v5.36`**: স্বাক্ষর সক্রিয়,`$_`ডিফল্ট,`defer`|
| 5.38 | 2023 | `class`কীওয়ার্ড (পরীক্ষামূলক),`try`/`catch`স্থিতিশীল |
| 5.40 | 2024 | `^`বিটওয়াইজ অপারেটর,`for`তালিকার উন্নতি |
| 5.42 | 2025 | চলমান উন্নয়ন |
## প্রধান মাইলফলক
### পার্ল 1-4: স্ক্রিপ্টিং যুগ (1987-1993)
- **1987**: ল্যারি ওয়াল পার্ল প্রকাশ করেছে - "ব্যবহারিক নিষ্কাশন এবং রিপোর্ট ভাষা"
- **লক্ষ্য**: একটি শক্তিশালী স্ক্রিপ্টিং টুলে sed, awk, grep, শেল একত্রিত করুন
- **3.0**: লেক্সিকাল স্কোপিং (`my`)
- **4.0**: দ্য ক্যামেল বুক — পার্ল সিসাডমিন কাজের জন্য ব্যাপকভাবে গৃহীত হয়
### পার্ল 5: দ্য গোল্ডেন এজ (1994-2019)
- **5.0 (1994)**: সম্পূর্ণ পুনর্লিখন — **মডিউল**, **রেফারেন্স**, **ক্লোজার**, **বস্তু**
- **5.6 (2000):`our`, v-স্ট্রিং
- **5.8 (2002): **ইউনিকোড সমর্থন**, ইন্টারপ্রেটার থ্রেড (`ithreads`)
- **5.10 (2007):`say`,`//`(সংজ্ঞায়িত-বা),`given`/`when`(সুইচ), স্মার্টম্যাচ
- **5.12–5.28**: ক্রমবর্ধমান উন্নতি, ইউনিকোড আপগ্রেড
### আধুনিক পার্ল (2020-বর্তমান)
- **5.32 (2020):`isa`অপারেটর (ক্লিনার টাইপ চেকিং)
- **5.34 (2021):`try`/`catch`(পরীক্ষামূলক),`defer`ব্লক
- **5.36 (2022): **`use v5.36`** — স্বাক্ষরগুলি ডিফল্টরূপে সক্রিয়,`$_`ডিফল্ট,`defer`
- **5.38 (2023):`class`কীওয়ার্ড (পরীক্ষামূলক — অন্তর্নির্মিত OOP),`try`/`catch`স্থিতিশীল
- **5.40 (2024): Bitwise অপারেটর উন্নতি
## সিনট্যাক্স বিবর্তন
```perl
# Perl 1-4: Basic scripting
#!/usr/bin/perl
$name = "World";
print "Hello, $name\n";

# Perl 5.0: References, closures, modules
use strict;
use warnings;
my $greeting = sub { "Hello, $_[0]" };
print $greeting->("World");

# Perl 5.8: Unicode
use utf8;
my $text = "café";

# Perl 5.10: say, defined-or
use v5.10;
say "Hello!";
my $value = $input // 'default';

# Perl 5.20: Subroutine signatures (experimental)
use experimental 'signatures';
sub greet ($name, $greeting = "Hello") {
    say "$greeting, $name!";
}

# Perl 5.36: Modern Perl
use v5.36;
sub greet ($name, $greeting = "Hello") {
    say "$greeting, $name!";
}

# Perl 5.38: class keyword (experimental)
use experimental 'class';
class Dog {
    field $name :param;
    field $breed :param;
    method bark { say "$name says Woof!" }
}
my $dog = Dog->new(name => "Rex", breed => "Lab");
```

## CPAN ইকোসিস্টেম
```
1995: CPAN (Comprehensive Perl Archive Network) launched
2000: Module::Build — alternative to MakeMaker
2008: CPANPLUS — enhanced CPAN client
2010: Dist::Zilla — release builder
2012: Carton — dependency pinning (like Bundler)
2013: cpanminus — zero-config CPAN client
2025: CPAN hosts 200,000+ modules from 14,000+ authors
```

## মূল ডিজাইনের নীতি
```
1. "TMTOWTDI" — There's More Than One Way To Do It
2. "Practical, not pure" — solve real problems
3. "Text processing king" — regex built into the language
4. "Glue language" — connect systems, protocols, formats
5. "Backward compatible" — old Perl code keeps running
6. "Community-driven" — CPAN, Perl Mongers, YAPC conferences
```

## ইকোসিস্টেম বৃদ্ধি
```
1987: Perl 1.0 — sysadmin scripting
1994: Perl 5.0 — modules, OOP, the web CGI era
1995: CPAN launched — module ecosystem
2000: Perl powers the early web (CGI scripts)
2002: Perl 5.8 — Unicode, ithreads
2005: Catalyst, Dancer — web frameworks
2007: Perl 5.10 — modern syntax additions
2010: Moose — modern OOP (meta-object protocol)
2022: Perl 5.36 — modern defaults
2025: Perl still powers sysadmin, bioinformatics, legacy web apps
       CPAN: 200,000+ modules; used by cPanel, DuckDuckGo
```
