---
# Metadata
title: "Perl — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, modern Perl code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [perl, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# পার্ল — ইডিওম্যাটিক প্যাটার্নস এবং সেরা অভ্যাস
এই নির্দেশিকাটি পরিচ্ছন্ন, আধুনিক পার্ল (5.38+) কোড লেখার জন্য ইডিওম্যাটিক প্যাটার্ন এবং সর্বোত্তম অনুশীলনগুলি কভার করে।
---

## আধুনিক পার্ল
```perl
# ✅ Always use strict and warnings
use v5.38;
use strict;
use warnings;
use feature 'signatures';
no warnings 'experimental::signatures';

# ✅ Signatures (Perl 5.36+)
sub greet ($name, $greeting = "Hello") {
    return "$greeting, $name!";
}

# ✅ say instead of print
say "Hello, World!";

# ✅ postderef (Perl 5.20+)
my @items = $array_ref->@*;
my %hash  = $hash_ref->%*;
my $name  = $user->{name};
```

---

## ডেটা স্ট্রাকচার
```perl
# ✅ Hash references for structured data
my $user = {
    name  => "Alice",
    email => "alice@example.com",
    age   => 30,
};

# ✅ Array references
my $items = [1, 2, 3, 4, 5];

# ✅ Slicing
my @names = map { $_->{name} } @$users;
my @values = @{$hash}{qw/key1 key2 key3/};

# ✅ Defined-or
my $name = $input // "Anonymous";
```

---

## রেগুলার এক্সপ্রেশন
```perl
# ✅ Named captures
if ($text =~ /(?<name>\w+)\s*@\s*(?<email>[\w.]+)/) {
    say "Name: $+{name}, Email: $+{email}";
}

# ✅ /x for readable regexes
my $email_re = qr{
    (?<user>   [\w.]+)
    \@
    (?<domain> [\w.]+\.\w+)
}x;

# ✅ Non-destructive substitution
my $cleaned = $dirty =~ s/\s+/_/gr;
```

---

## ত্রুটি হ্যান্ডলিং
```perl
# ✅ eval for exception handling
my $result = eval {
    risky_operation();
    1;
} or do {
    warn "Failed: $@";
    fallback();
};

# ✅ Try::Tiny (cleaner)
use Try::Tiny;
try {
    risky_operation();
} catch {
    warn "Error: $_";
};

# ✅ die with context
die "Cannot open file '$file': $!" unless -f $file;
```

---

## মডিউল এবং ওওপি
```perl
# ✅ Modern OOP (Perl 5.38+ class)
class User {
    field $name :param;
    field $email :param;
    
    method greet() {
        return "Hello, I'm $name";
    }
}

# ✅ Moose/Moo for complex OOP
package User;
use Moose;
has name  => (is => 'ro', isa => 'Str', required => 1);
has email => (is => 'ro', isa => 'Str', required => 1);
__PACKAGE__->meta->make_immutable;
```

---

## সারাংশ
আধুনিক পার্ল ইডিয়মগুলি জোর দেয়:`use strict; use warnings;`, স্বাক্ষর, বলুন, পোস্টডেরেফ এবং আধুনিক OOP (5.38+ এ ক্লাস কীওয়ার্ড)। linting এর জন্য perlcritic এবং ফরম্যাটিং এর জন্য perltidy অনুসরণ করুন। পার্ল TMTOWTDI (এটি করার একেরও বেশি উপায় আছে) মূল্যায়ন করে — কিন্তু আধুনিক পার্ল ক্লিনার, আরও রক্ষণাবেক্ষণযোগ্য প্যাটার্নে একত্রিত হয়।