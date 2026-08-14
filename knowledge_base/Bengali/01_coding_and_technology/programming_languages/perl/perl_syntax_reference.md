<!--
---
# Metadata
title: "Perl — Syntax Reference"
description: "Detailed syntax reference for Perl covering regex, references, CPAN, object-oriented Perl, and text processing patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [perl, syntax-reference, regex, references, cpan, oop, text-processing, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# পার্ল — সিনট্যাক্স রেফারেন্স
এই নথিটি পার্লের (5.38+) জন্য একটি ব্যাপক, কাঠামোগত সিনট্যাক্স রেফারেন্স প্রদান করে। এটি সম্পূর্ণ সিনট্যাক্স প্যাটার্ন, রেগুলার এক্সপ্রেশন, রেফারেন্স এবং পার্লের টেক্সট প্রসেসিং ক্ষমতার উপর ফোকাস করে প্রধান পার্ল রেফারেন্সের পরিপূরক।
---

## অপারেটর এবং এক্সপ্রেশন
### মূল অপারেটর
| অপারেটর | নাম | উদাহরণ | নোট |
|----------|------|---------|-------|
| `+``-``*``/``%``**` | পাটিগণিত | `2 ** 10`| `**`হল সূচক |
| `.`| স্ট্রিং সংযোগ | `$a . $b`| |
| `x`| স্ট্রিং পুনরাবৃত্তি | `"ab" x 3`| `"ababab"`|
| `==``!=``<``>``<=``>=` | সংখ্যাগত তুলনা | `$a == $b`| |
| `eq``ne``lt``gt``le``ge` | স্ট্রিং তুলনা | `$a eq $b`| |
| `<=>`| সংখ্যাসূচক মহাকাশযান | `$a <=> $b`| রিটার্ন-1, 0, 1 |
| `cmp`| স্ট্রিং স্পেসশিপ | `$a cmp $b`| |
| `&&``\|\|``!`| যৌক্তিক | `$a && $b`| |
| `and``or``not`| যৌক্তিক (নিম্ন prec.) | `$a and $b`| এড়িয়ে চলুন —`&&`/`\|\|`ব্যবহার করুন |
| `=~``!~` | Regex ম্যাচ | `$str =~ /pattern/`| |
| `..``...` | রেঞ্জ / ফ্লিপ-ফ্লপ | `1..10`| |
| `?:`| টারনারি | `$a ? $b : $c`| |
| `//`| সংজ্ঞায়িত-বা | `$a // $b`| `$b`যদি`$a`undef হয় |
| `=>`| মোটা কমা | `key => 'value'`| স্বতঃ-উদ্ধৃতি বেয়ারওয়ার্ড |
### সিগিলস — পরিবর্তনশীল প্রকার
```perl
# Sigils indicate the type of access, not the variable type
my $scalar = "hello";     # scalar
my @array  = (1, 2, 3);   # array
my %hash   = (a => 1, b => 2);  # hash

# Accessing elements keeps the sigil of the result
my $first = $array[0];    # scalar context — $
my @slice = @array[0, 2]; # array slice — @
my $value = $hash{key};   # scalar from hash — $
my @vals  = @hash{'a','b'}; # hash slice — @
```

---

## নিয়ন্ত্রণ প্রবাহ
```perl
# if / elsif / else
if ($score >= 90) {
    $grade = 'A';
} elsif ($score >= 80) {
    $grade = 'B';
} else {
    $grade = 'F';
}

# Statement modifiers (postfix)
print "hello\n" if $debug;
die "error" unless $valid;

# unless (inverse if)
unless ($done) {
    process();
}

# while / until
while (my $line = <STDIN>) {
    chomp $line;
    process($line);
}

until ($done) {
    work();
}

# for (C-style)
for (my $i = 0; $i < 10; $i++) {
    print "$i\n";
}

# foreach (iterate over list)
foreach my $item (@items) {
    print "$item\n";
}

# Implicit $_ variable
foreach (@items) {      # $_ is each item
    print "$_\n";
}

# Given/when (switch — experimental in older Perls)
use feature 'switch';
given ($value) {
    when (1)     { say "one" }
    when (2)     { say "two" }
    default      { say "other" }
}

# Loop control
for my $n (1..100) {
    next if $n % 2 == 0;   # skip even
    last if $n > 50;        # stop at 50
    redo if restart_needed; # restart iteration
    print "$n\n";
}
```

---

## রেগুলার এক্সপ্রেশন
```perl
# Basic matching
if ($str =~ /hello/) { print "found!\n"; }
if ($str =~ /hello/i) { print "case-insensitive!\n"; }

# Capturing groups
my ($first, $last) = $name =~ /(\w+)\s+(\w+)/;

# Substitution
$str =~ s/old/new/g;        # global replace
$str =~ s/\s+/ /g;          # collapse whitespace
$str =~ s/^\s+|\s+$//g;     # trim

# Match modifiers
# /i  case-insensitive
# /g  global (all matches)
# /m  multiline (^ and $ match line boundaries)
# /s  single-line (. matches \n)
# /x  extended (ignore whitespace, allow comments)

# Extended regex with comments
if ($str =~ m{
    ^               # start of string
    (\d{4})         # year
    -               # dash
    (\d{2})         # month
    -               # dash
    (\d{2})         # day
    $               # end of string
}x) {
    print "Date: $1-$2-$3\n";
}

# Character classes
# \d  digit        \D  non-digit
# \w  word char    \W  non-word
# \s  whitespace   \S  non-whitespace

# Lookahead / lookbehind
$str =~ /foo(?=bar)/;    # foo followed by bar (not consumed)
$str =~ /(?<!not )foo/;  # foo not preceded by "not "

# Named captures
if ($str =~ /(?<year>\d{4})-(?<month>\d{2})/) {
    print "Year: $+{year}, Month: $+{month}\n";
}

# quotemeta — escape regex special characters
my $literal = quotemeta($user_input);
```

---

## রেফারেন্স এবং ডেটা স্ট্রাকচার
```perl
# Array reference
my $aref = [1, 2, 3];
push @$aref, 4;
print $aref->[0];  # 1

# Hash reference
my $href = { name => 'Alice', age => 30 };
$href->{email} = 'alice@example.com';
print $href->{name};

# Nested structures
my $data = {
    users => [
        { name => 'Alice', scores => [95, 87, 92] },
        { name => 'Bob',   scores => [78, 88, 91] },
    ],
};
print $data->{users}[0]{scores}[2];  # 92

# Dereferencing
my @array = @$aref;       # array from array ref
my %hash  = %$href;       # hash from hash ref

# Anonymous subroutines
my $greet = sub {
    my ($name) = @_;
    return "Hello, $name!";
};
print $greet->('World');

# Closures
sub make_counter {
    my $count = 0;
    return sub { ++$count };
}
my $counter = make_counter();
print $counter->();  # 1
print $counter->();  # 2
```

---

## ফাইল হ্যান্ডলিং
```perl
# Lexical filehandles (modern Perl)
open my $fh, '<', 'file.txt' or die "Cannot open: $!";
while (my $line = <$fh>) {
    chomp $line;
    process($line);
}
close $fh;

# Write to file
open my $out, '>', 'output.txt' or die "Cannot write: $!";
print $out "Hello, World!\n";
close $out;

# Slurp entire file
local $/;
open my $fh, '<', 'file.txt' or die $!;
my $content = <$fh>;

# Read directory
opendir my $dh, '.' or die $!;
while (my $file = readdir $dh) {
    next if $file =~ /^\./;
    print "$file\n";
}
closedir $dh;

# File tests
-e $file    # exists
-f $file    # is a file
-d $dir     # is a directory
-r $file    # readable
-w $file    # writable
```

---

## অবজেক্ট-ওরিয়েন্টেড পার্ল (Moo/Moose)
```perl
# Modern OOP with Moo
package User;
use Moo;

has name => (is => 'ro', required => 1);
has email => (is => 'rw');
has age => (is => 'rw', default => 0);

sub greet {
    my ($self) = @_;
    return "Hello, I'm " . $self->name;
}

1;

# Usage
my $user = User->new(name => 'Alice', email => 'alice@example.com');
print $user->greet;

# Roles (like interfaces/mixins)
package Printable;
use Moo::Role;

sub print_details {
    my ($self) = @_;
    print "Name: " . $self->name . "\n";
}

# Consume role
package Employee;
use Moo;
extends 'User';
with 'Printable';

has department => (is => 'rw');
1;
```

---

## সারাংশ
পার্লের সিনট্যাক্সটি প্রসঙ্গ, সিগিলস এবং "এটি করার জন্য একাধিক উপায় আছে" নীতির চারপাশে নির্মিত। নিয়মিত অভিব্যক্তিগুলি ভাষায় তৈরি করা হয়, যা পাঠ্য প্রক্রিয়াকরণকে সংক্ষিপ্ততায় অতুলনীয় করে তোলে। রেফারেন্স জটিল ডেটা স্ট্রাকচার সক্ষম করে। CPAN সবকিছুর জন্য মডিউল প্রদান করে। আধুনিক পার্ল (`strict` ,`warnings`, এবং আভিধানিক ভেরিয়েবল সহ) পরিষ্কার এবং রক্ষণাবেক্ষণযোগ্য। পার্লের উত্তরাধিকার প্রতিটি আধুনিক ভাষা গৃহীত নিদর্শন এবং সরঞ্জামগুলিতে বেঁচে থাকে।