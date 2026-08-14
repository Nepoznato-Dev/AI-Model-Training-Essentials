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
# पर्ल - सिंटैक्स संदर्भ
यह दस्तावेज़ पर्ल (5.38+) के लिए एक व्यापक, संरचित वाक्यविन्यास संदर्भ प्रदान करता है। यह संपूर्ण सिंटैक्स पैटर्न, नियमित अभिव्यक्ति, संदर्भ और पर्ल की टेक्स्ट प्रोसेसिंग शक्ति पर ध्यान केंद्रित करके मुख्य पर्ल संदर्भ को पूरक करता है।
---

## ऑपरेटर्स और अभिव्यक्तियाँ
### कोर ऑपरेटर्स
| ऑपरेटर | नाम | उदाहरण | नोट्स |
|-------|------|------|-------|
| `+``-``*``/``%``**` | अंकगणित | `2 ** 10`| `**`घातांक है |
| `.`| स्ट्रिंग संयोजन | `$a . $b`| |
| `x`| स्ट्रिंग पुनरावृत्ति | `"ab" x 3`| `"ababab"`|
| `==``!=``<``>``<=``>=` | संख्यात्मक तुलना | `$a == $b`| |
| `eq``ne``lt``gt``le``ge` | स्ट्रिंग तुलना | `$a eq $b`| |
| `<=>`| संख्यात्मक अंतरिक्ष यान | `$a <=> $b`| रिटर्न -1, 0, 1 |
| `cmp`| स्ट्रिंग अंतरिक्ष यान | `$a cmp $b`| |
| `&&``\|\|``!`| तार्किक | `$a && $b`| |
| `and``or``not`| तार्किक (कम सटीक) | `$a and $b`| बचें -`&&`/`\|\|`| का उपयोग करें
| `=~``!~` | रेगेक्स मैच | `$str =~ /pattern/`| |
| `..``...` | रेंज/फ्लिप-फ्लॉप | `1..10`| |
| `?:`| टर्नरी | `$a ? $b : $c`| |
| `//`| परिभाषित-या | `$a // $b`| `$b`यदि`$a`अपरिभाषित है |
| `=>`| मोटा अल्पविराम | `key => 'value'`| ऑटो-उद्धरण नंगे शब्द |
### सिगिल्स - परिवर्तनशील प्रकार
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

## प्रवाह को नियंत्रित करें
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

## नियमित अभिव्यक्तियाँ
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

## संदर्भ एवं डेटा संरचनाएँ
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

## फ़ाइल रखरखाव
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

## ऑब्जेक्ट-ओरिएंटेड पर्ल (मू/मूस)
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

## सारांश
पर्ल का वाक्यविन्यास संदर्भ, सिगिल्स और "इसे करने के एक से अधिक तरीके हैं" के सिद्धांत के आसपास बनाया गया है। नियमित अभिव्यक्तियाँ भाषा में निर्मित होती हैं, जिससे पाठ प्रसंस्करण संक्षिप्तता में बेजोड़ हो जाता है। संदर्भ जटिल डेटा संरचनाओं को सक्षम करते हैं। सीपीएएन हर चीज के लिए मॉड्यूल प्रदान करता है। आधुनिक पर्ल (`strict` ,`warnings`और शाब्दिक चर के साथ) साफ और रखरखाव योग्य है। पर्ल की विरासत उन पैटर्न और उपकरणों में जीवित है जिन्हें हर आधुनिक भाषा ने अपनाया है।