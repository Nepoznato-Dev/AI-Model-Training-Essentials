---
# Metadata
title: "Perl — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, modern Perl code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Perl — идиоматические шаблоны и лучшие практики
В этом руководстве рассматриваются идиоматические шаблоны и лучшие практики написания чистого современного кода на Perl (5.38+).
---

## Современный Perl
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

## Структуры данных
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

## Регулярные выражения
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

## Обработка ошибок
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

## Модули и ООП
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

## Краткое содержание
Современные идиомы Perl подчеркивают:`use strict; use warnings;`, подписи, скажем, postderef и современное ООП (ключевое слово class в версии 5.38+). Следуйте perlcritic для проверки и perltidy для форматирования. Perl ценит TMTOWTDI (есть более чем один способ сделать это), но современный Perl ориентирован на более чистые и удобные в обслуживании шаблоны.