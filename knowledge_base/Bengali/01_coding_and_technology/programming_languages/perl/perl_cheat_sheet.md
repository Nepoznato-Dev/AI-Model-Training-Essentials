---
# Metadata
title: "Perl — Cheat Sheet"
description: "Quick-reference cheat sheet for Perl syntax, regex, and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [perl, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# পার্ল — চিট শীট
## মৌলিক
```perl
use strict;
use warnings;
use feature 'say';

# Variables
my $name = "Alice";       # scalar
my $age = 30;
my $pi = 3.14159;
my $active = 1;           # true (any non-zero, non-empty)

# Special variables
$_    # default variable
$.    # current line number
$!    # OS error
$@    # eval error
$$    # process ID
$0    # program name

# String interpolation
"Hello, $name!"
"Age: ${age}"
'No $interpolation here'  # single quotes — literal

# String operations
length($name)
uc($name)                  # uppercase
lc($name)                  # lowercase
substr($name, 0, 3)       # "Ali"
index($name, "lic")        # position
$name =~ s/Alice/Bob/r    # substitute (non-destructive)
$name =~ tr/a-z/A-Z/      # transliterate
reverse($name)
split(/,/, "a,b,c")
join(", ", @items)
sprintf("Hello, %s!", $name)
chomp($line)               # remove trailing newline
```

## অ্যারে এবং হ্যাশ
```perl
# Array
my @arr = (1, 2, 3, 4, 5);
$arr[0];                   # 1
$arr[-1];                  # 5 (last element)
$arr[1..3];                # slice
push @arr, 6;
pop @arr;
shift @arr;
unshift @arr, 0;
scalar @arr;               # length
@arr[2..4];                # slice
grep { $_ > 2 } @arr;
map { $_ * 2 } @arr;
sort @arr;
reverse @arr;
join(", ", @arr);

# Hash
my %user = (name => "Alice", age => 30);
$user{name};
$user{email} = "a\@b.com";
keys %user;
values %user;
exists $user{name};
delete $user{age};
scalar keys %user;         # count

# Hash slice
my @vals = @user{qw(name age)};

# References
my $arr_ref = \@arr;
my $hash_ref = \%user;
$arr_ref->[0];
$hash_ref->{name};

# Dereference
@$arr_ref;
%$hash_ref;
```

## নিয়ন্ত্রণ প্রবাহ
```perl
if ($condition) {
    # ...
} elsif ($other) {
    # ...
} else {
    # ...
}

# Postfix (statement modifier)
print "yes" if $condition;
next unless $valid;
last if $done;

# Ternary
my $result = $condition ? "yes" : "no";

# given/when (experimental)
use feature 'switch';
given ($value) {
    when (0)     { say "zero" }
    when (/^\d/) { say "number" }
    default      { say "other" }
}

# Loops
for my $item (@arr) { say $item; }
for my $i (0 .. $#arr) { say "$i: $arr[$i]"; }
foreach my $k (keys %hash) { say "$k: $hash{$k}"; }
for (1..10) { say $_; }

while ($condition) { ... }
until ($condition) { ... }

# C-style for
for (my $i = 0; $i < 10; $i++) { ... }
```

## রেগুলার এক্সপ্রেশন
```perl
# Match
if ($str =~ /pattern/) { ... }
if ($str =~ /^hello/i) { ... }  # case insensitive

# Capture
my ($first, $last) = $name =~ /(\w+)\s+(\w+)/;

# Substitute
$str =~ s/old/new/g;       # global replace
$str =~ s/\s+/ /g;         # collapse whitespace
$str =~ s/^\s+|\s+$//g;    # trim

# Split
my @parts = split /,/, $csv_line;
my @words = split /\s+/, $text;

# Common patterns
/^\d+$/                    # integer
/^\d+\.\d+$/               # decimal
/^[\w.-]+@[\w.-]+\.\w+$/  # email (simplified)
/^(https?:\/\/)/           # URL start
```

## ফাংশন এবং সাবরুটিন
```perl
# Subroutine
sub add {
    my ($a, $b) = @_;
    return $a + $b;
}
my $result = add(3, 4);

# Signatures (Perl 5.20+)
use feature 'signatures';
sub greet($name, $greeting = "Hello") {
    say "$greeting, $name!";
}

# Variadic
sub flexible {
    my @args = @_;
    # ...
}

# Closures
sub make_counter {
    my $n = 0;
    return sub { ++$n };
}
my $counter = make_counter();
$counter->();  # 1
$counter->();  # 2
```

## ফাইল I/O
```perl
# Open file
open my $fh, '<', 'input.txt' or die "Cannot open: $!";
while (my $line = <$fh>) {
    chomp $line;
    process($line);
}
close $fh;

# Write file
open my $out, '>', 'output.txt' or die "Cannot write: $!";
print $out "Hello, World!\n";
close $out;

# Slurp
my $content = do { local $/; open my $fh, '<', 'file.txt'; <$fh> };

# Diamond operator (read from files or STDIN)
while (<>) {
    chomp;
    say "Got: $_";
}
```

## ত্রুটি হ্যান্ডলিং
```perl
# eval (catch exceptions)
eval {
    risky_operation();
};
if ($@) {
    warn "Error: $@";
}

# die / warn
die "Fatal error: $!";
warn "Something suspicious";

# Try::Tiny
use Try::Tiny;
try {
    risky_operation();
} catch {
    warn "Error: $_";
} finally {
    cleanup();
};
```

## সাধারণ নিদর্শন
```perl
# Defined-or
my $value = $input // "default";

# Schwartzian transform (sort by computed key)
my @sorted = map  { $_->[0] }
             sort { $a->[1] <=> $b->[1] }
             map  { [$_, compute_key($_)] }
             @items;

# List::Util
use List::Util qw(first max min sum shuffle);
my $found = first { $_ > 5 } @arr;
my $total = sum @arr;

# say (Perl 5.10+)
use feature 'say';
say "Hello!";
```
