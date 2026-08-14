---
# Metadata
title: "Perl"
description: "Comprehensive reference for the Perl programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [perl, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "24 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# পার্ল
পার্ল ল্যারি ওয়াল দ্বারা 1987 সালে একটি ব্যবহারিক পাঠ্য-প্রক্রিয়াকরণ সরঞ্জাম হিসাবে তৈরি করা হয়েছিল। এটি প্রারম্ভিক ওয়েব ডেভেলপমেন্ট (CGI স্ক্রিপ্ট), সিস্টেম অ্যাডমিনিস্ট্রেশন, বায়োইনফরমেটিক্স এবং নেটওয়ার্ক প্রোগ্রামিং এর মেরুদণ্ড হয়ে ওঠে। পার্লের দর্শন হল "দেয়ার ইজ মোর ওয়ান ওয়ে টু ডু ইট" (TMTOWTDI) — ভাষা আপনাকে প্রতিটি সমস্যার একাধিক পন্থা দেয়, অভিন্নতার চেয়ে অভিব্যক্তির পক্ষে।
আধুনিক প্রোগ্রামিং-এ পার্লের প্রভাব প্রচুর কিন্তু প্রায়শই অদৃশ্য: পার্লের প্যাটার্ন ম্যাচিং দ্বারা প্রভাবিত রেগুলার এক্সপ্রেশনগুলি এখন পাইথন, জাভাস্ক্রিপ্ট, জাভা এবং অন্যান্য বেশিরভাগ ভাষায় আদর্শ। CPAN (কমপ্রিহেনসিভ পার্ল আর্কাইভ নেটওয়ার্ক) ছিল প্রথম সফ্টওয়্যার প্যাকেজ সংগ্রহস্থলগুলির মধ্যে একটি এবং পাইথনের PyPI এবং নোডের npm-এর মতো পরবর্তী সিস্টেমগুলিকে অনুপ্রাণিত করেছিল।
যদিও পার্লের জনপ্রিয়তা 2000 এর দশকের গোড়ার দিকে তার শিখর থেকে হ্রাস পেয়েছে, এটি লিগ্যাসি সিস্টেম, পাঠ্য প্রক্রিয়াকরণ পাইপলাইন এবং সিস্টেম প্রশাসনে ব্যাপকভাবে ব্যবহৃত হয়। পার্ল 6 (বর্তমানে **রাকু** বলা হয়) হল একটি পৃথক ভাষা যা পার্লের অনেক ধারণাকে নতুন করে কল্পনা করেছে।
---

## কেন পার্ল ব্যাপার
- **টেক্সট প্রসেসিং**: পার্লের রেগুলার এক্সপ্রেশন যে কোনো মূলধারার ভাষার সবচেয়ে শক্তিশালী।
- **CPAN**: 200,000-এর বেশি মডিউল — বৃহত্তম এবং প্রাচীনতম প্যাকেজ সংগ্রহস্থলগুলির মধ্যে একটি।
- **ওয়ান-লাইনার**: পার্ল দ্রুত কমান্ড-লাইন টেক্সট রূপান্তরে পারদর্শী।
- **আঠালো ভাষা**: সিস্টেম সংযোগ করে, লগ পার্স করে, ডেটা ফাইল প্রসেস করে, কাজগুলি স্বয়ংক্রিয় করে।
- **উৎপাদনে প্রমাণিত**: PHP এর অস্তিত্বের আগে থেকেই ওয়েবকে শক্তিশালী করা। এখনও গুরুত্বপূর্ণ অবকাঠামো চলছে।
- **রাকু (পার্ল 6): ব্যাকরণ, জংশন এবং একাধিক প্রেরণ সহ একটি আধুনিক পুনঃডিজাইন।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **পঠনযোগ্যতা** | "পার্ল হল একটি শুধুমাত্র লেখার ভাষা" — ঘন, ক্রিপ্টিক সিনট্যাক্স | কঠোর/সতর্কতা ব্যবহার করুন; মডুলার কোড লিখুন; আধুনিক পার্ল ব্যবহার করুন (5.36+) |
| **পতনশীল সম্প্রদায়** | পার্ল বেছে নেওয়া কম নতুন প্রকল্প বড় বিদ্যমান কোডবেসের রক্ষণাবেক্ষণ প্রয়োজন; সক্রিয় সম্প্রদায় |
| **দুটি প্রধান সংস্করণ** | পার্ল 5 এবং রাকু (পার্ল 6) ভিন্ন ভাষা | বিদ্যমান কাজের জন্য পার্ল 5 ব্যবহার করুন; নতুন প্রকল্পের জন্য রাকু |
| **চলমান নয়** | খুব কমই বুটক্যাম্প বা বিশ্ববিদ্যালয়ে পড়ানো হয় | বিস্তৃত ডকুমেন্টেশন এবং CPAN মডিউল |
| **ভেরিয়েবল সিগিলস** | `$`,`@`,`%`উপসর্গ নতুনদের বিভ্রান্ত করতে পারে | প্যাটার্ন শিখুন:`$scalar`,`@array`,`%hash`|
| **পারফরম্যান্স** | কম্পিউট-ভারী কাজের জন্য কম্পাইল করা ভাষার চেয়ে ধীর | সি এক্সটেনশন ব্যবহার করুন; HPC এর জন্য সঠিক টুল নয়
---

## সিনট্যাক্স মৌলিক
```perl
#!/usr/bin/env perl
use strict;
use warnings;
use feature 'say';  # Modern Perl

# Variables
my $name = "Alice";          # Scalar (single value)
my @colors = ("red", "green", "blue");  # Array
my %user = (                  # Hash (key-value pairs)
    name  => "Alice",
    age   => 30,
    email => "alice@example.com",
);

# Access
say $name;                    # Alice
say $colors[0];               # red
say $user{name};              # Alice

# String operations
my $greeting = "Hello, $name!";
my $upper = uc($name);        # "ALICE"
my $length = length($name);   # 5

# Regular expressions (Perl's superpower)
my $text = "Error 404: Page not found on 2024-01-15";

if ($text =~ /Error (\d+): (.+)/) {
    say "Code: $1";    # 404
    say "Message: $2"; # Page not found on 2024-01-15
}

# Substitution
$text =~ s/not found/missing/;
# "Error 404: Page missing on 2024-01-15"

# Global replacement
my $data = "foo bar foo baz foo";
$data =~ s/foo/qux/g;    # "qux bar qux baz qux"

# Extracting with regex
my @numbers = $text =~ /(\d+)/g;  # Extract all numbers

# Conditionals
if ($name eq "Alice") {
    say "Welcome back!";
} elsif ($name eq "Bob") {
    say "Hello Bob!";
} else {
    say "Who are you?";
}

# Loops
for my $color (@colors) {
    say "Color: $color";
}

foreach my $key (keys %user) {
    say "$key => $user{$key}";
}

# While loop (read file line by line)
open my $fh, '<', 'data.txt' or die "Cannot open: $!";
while (my $line = <$fh>) {
    chomp $line;
    say "Line: $line";
}
close $fh;

# Subroutines (functions)
sub greet {
    my ($name, $greeting) = @_;
    $greeting //= "Hello";  # Default value
    return "$greeting, $name!";
}

say greet("Alice", "Hi");   # Hi, Alice!
say greet("Bob");            # Hello, Bob!

# List processing (Perl's other strength)
my @numbers = (1..100);
my @evens = grep { $_ % 2 == 0 } @numbers;
my @doubled = map { $_ * 2 } @evens;
my $sum = reduce { $a + $b } @numbers;

# Hash references (complex data structures)
my $team = {
    name    => "Engineering",
    members => [
        { name => "Alice", role => "Lead" },
        { name => "Bob",   role => "Dev" },
    ],
};

say $team->{members}[0]{name};  # Alice

# Error handling
eval {
    die "Something went wrong";
};
if ($@) {
    say "Caught error: $@";
}

# Perl one-liners (command line)
# perl -ne 'print if /ERROR/' access.log
# perl -pe 's/old/new/g' file.txt
# perl -lane 'print $F[0]' data.csv  # Print first column
```

---

## অন্যান্য ভাষার উপর পার্লের প্রভাব
| বৈশিষ্ট্য | ভাষা যে এটি গ্রহণ করেছে |
|---------|----------------------------|
| নিয়মিত অভিব্যক্তি | পাইথন, জাভাস্ক্রিপ্ট, জাভা, রুবি, সি#, পিএইচপি |
| প্যাকেজ রিপোজিটরি (CPAN) | PyPI, npm, RubyGems, crates.io |
| Herdocs | পাইথন, রুবি, পিএইচপি, শেল, জাভাস্ক্রিপ্ট |
| `$_`ডিফল্ট পরিবর্তনশীল | রুবির`$_`, PowerShell এর`$_`|
| `map`/`grep`/`reduce`| পাইথন, রুবি, জাভাস্ক্রিপ্ট, মরিচা |
| `use strict`/ লিন্টিং | টাইপস্ক্রিপ্ট, পাইথনের টাইপ ইঙ্গিত |
---

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### তথ্যসূত্র এবং জটিল ডেটা স্ট্রাকচার
```perl
use strict;
use warnings;
use feature 'say';
use Data::Dumper;

# References — pointers to variables
my $scalar_ref = \42;
my $array_ref  = [1, 2, 3];       # Anonymous array reference
my $hash_ref   = { name => "Alice" };  # Anonymous hash reference

# Dereferencing
say $$scalar_ref;        # 42
say $array_ref->[0];     # 1
say $hash_ref->{name};   # Alice

# Complex nested structures
my $company = {
    name => "TechCorp",
    departments => [
        {
            name    => "Engineering",
            members => [
                { name => "Alice", skills => ["Perl", "Python"] },
                { name => "Bob",   skills => ["Perl", "Go"] },
            ],
        },
        {
            name    => "Marketing",
            members => [
                { name => "Charlie", skills => ["SEO", "Analytics"] },
            ],
        },
    ],
};

say $company->{departments}[0]{members}[0]{name};  # Alice
say $company->{departments}[0]{members}[0]{skills}[1];  # Python
```

### বন্ধ এবং উচ্চ ক্রম ফাংশন
```perl
# Closures — subroutines that capture their lexical environment
sub make_counter {
    my $count = 0;
    return sub {
        $count++;
        return $count;
    };
}

my $counter = make_counter();
say $counter->();  # 1
say $counter->();  # 2
say $counter->();  # 3

# Higher-order functions
sub apply {
    my ($func, $value) = @_;
    return $func->($value);
}

my $double = sub { $_[0] * 2 };
say apply($double, 21);  # 42

# Sort with custom comparators
my @users = (
    { name => "Charlie", age => 25 },
    { name => "Alice",   age => 30 },
    { name => "Bob",     age => 20 },
);

my @sorted_by_name = sort { $a->{name} cmp $b->{name} } @users;
my @sorted_by_age    = sort { $a->{age} <=> $b->{age} } @users;
```

### উন্নত রেগুলার এক্সপ্রেশন
```perl
# Named captures
my $log = "2024-01-15 ERROR: Connection timeout on server-01";
if ($log =~ /(?<date>\d{4}-\d{2}-\d{2})\s+(?<level>\w+):\s+(?<msg>.+)/) {
    say "Date:  $+{date}";   # 2024-01-15
    say "Level: $+{level}";  # ERROR
    say "Msg:   $+{msg}";    # Connection timeout on server-01
}

# Lookahead and lookbehind
my $text = "price: $100, cost: $50";
my @prices = $text =~ /(?<=\$)\d+/g;  # (100, 50) — match digits after $

# Recursive patterns for nested structures
my $nested = "a(b(c)d)e";
if ($nested =~ /(\w+(??{(?1)?)\w*)/) {
    say "Matched: $&";
}

# /x modifier — readable regex with comments
my $email_re = qr{
    ^
    [a-zA-Z0-9._%+-]+   # local part
    @
    [a-zA-Z0-9.-]+       # domain
    \.
    [a-zA-Z]{2,}         # TLD
    $
}x;

say "test@example.com" =~ $email_re ? "Valid" : "Invalid";
```

### অবজেক্ট-ওরিয়েন্টেড পার্ল (মুজ/মু)
```perl
# Modern Perl OOP with Moose
package Animal;
use Moose;

has 'name' => (is => 'ro', isa => 'Str', required => 1);
has 'age'  => (is => 'rw', isa => 'Int', default => 0);

sub speak { return "$_[0]->name makes a sound" }

__PACKAGE__->meta->make_immutable;
no Moose;

package Dog;
use Moose;
extends 'Animal';

override 'speak' => sub {
    return super() . " — woof!";
};

__PACKAGE__->meta->make_immutable;
no Moose;

# Usage
my $rex = Dog->new(name => "Rex", age => 3);
say $rex->speak();  # Rex makes a sound — woof!
```

---

## সামঞ্জস্য এবং সমান্তরালতা
### সমান্তরাল::ফর্ক ম্যানেজার দিয়ে ফর্কিং
```perl
use Parallel::ForkManager;

my $pm = Parallel::ForkManager->new(4);  # 4 parallel workers

my @urls = ("http://example.com/1", "http://example.com/2",
            "http://example.com/3", "http://example.com/4");

foreach my $url (@urls) {
    $pm->start and next;  # Parent continues
    # Child process
    my $result = `curl -s $url`;
    $pm->finish(0, { url => $url, result => $result });
}

$pm->wait_all_children;
```

### কোরো — কোঅপারেটিভ কোরোটিন
```perl
use Coro;

my $ready = new Coro::Channel;

async {
    while (my $item = $ready->get) {
        say "Processing: $item";
        schedule;  # Yield to other coroutines
    }
};

$ready->put("item1");
$ready->put("item2");
$ready->put("item3");
```

### IO::Async — ইভেন্ট-চালিত প্রোগ্রামিং
```perl
use IO::Async;

my $loop = IO::Async::Loop->new;
my $http = IO::Async::HTTP->new;

foreach my $url (@urls) {
    $http->do_request(
        uri => $url,
        on_response => sub {
            my ($response) = @_;
            say "$url: " . $response->code;
        },
    );
}

$loop->run;
```

---

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### প্রকল্পের কাঠামো
```
my-perl-project/
├── lib/
│   └── MyApp/
│       ├── Controller/
│       ├── Model/
│       └── View/
├── t/
│   ├── 00-load.t
│   ├── basic.t
│   └── controller/
├── bin/
│   └── myapp.pl
├── cpanfile
├── Makefile.PL
├── dist.ini        # If using Dist::Zilla
└── README.md
```

### cpanfile — নির্ভরতা ব্যবস্থাপনা
```perl
# cpanfile
requires 'perl', '5.036';
requires 'Mojolicious', '>= 9.0';
requires 'DBIx::Class', '>= 0.08';
requires 'JSON::XS';
requires 'Log::Log4perl';

on 'test' => sub {
    requires 'Test::More', '>= 1.3';
    requires 'Test::Deep';
    requires 'Mock::Sub';
};

on 'develop' => sub {
    requires 'Perl::Critic';
    requires 'Perl::Tidy';
};
```

### নির্ভরতা কমান্ড
```bash
cpanm --installdeps .       # Install from cpanfile
cpanm Mojolicious           # Install specific module
cpanm --notest Mojolicious  # Skip tests for speed
carton install              # Bundler-like dependency pinning
carton exec -- perl app.pl  # Run with pinned deps
```

### CI/CD পাইপলাইন (GitHub অ্যাকশন)
```yaml
name: Perl CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    strategy:
      matrix:
        perl: ['5.36', '5.38']
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: shogo82148/actions-setup-perl@v1
        with:
          perl-version: ${{ matrix.perl }}
      - run: cpanm --installdeps --with-develop .
      - run: perl Makefile.PL && make test
      - run: perlcritic lib/
```
---

## পরীক্ষা
### পরীক্ষা::আরো
```perl
use Test::More;
ok(1, 'basic test');
is(2+2, 4, 'math works');
done_testing();
```

### টেস্ট কমান্ড
```bash
prove -lrv t/
prove -l t/user_service.t
```

---

## ইন্টারঅপারেবিলিটি
### FFI::প্ল্যাটিপাস
```perl
use FFI::Platypus;
my $ffi = FFI::Platypus->new(api => 2);
$ffi->lib(undef);  # libc
$ffi->attach(sqrt => ['double'] => 'double');
say sqrt(144.0);  # 12.0
```

### XS — C ইন্টিগ্রেশন
```perl
# XS allows Perl to call C functions directly
# Build with: perl Makefile.PL && make && make install
use MyModule;
say MyModule::fast_factorial(10);  # 3628800
```

---

## ডিজাইন প্যাটার্ন
### সিঙ্গেলটন
```perl
package Database;
use Moose;
has 'connection' => (is => 'ro', lazy => 1, builder => '_build_conn');
sub _build_conn { return "db_handle"; }
my $instance;
sub instance { $instance //= Database->new }
__PACKAGE__->meta->make_immutable;
no Moose;
```

### দায়িত্বের চেইন
```perl
package Middleware::Pipeline;
sub new { bless { handlers => [] }, shift }
sub add { my ($s, $h) = @_; push @{$s->{handlers}}, $h; $s }
sub execute {
    my ($self, $req) = @_;
    my $i = 0;
    my $n; $n = sub {
        $i < @{$self->{handlers}} ? $self->{handlers}[$i++]->($req, $n) : $req
    };
    $n->();
}
```
---

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
```bash
# Devel::NYTProf profiler
perl -d:NYTProf script.pl && nytprofhtml --open
```

```perl
# Hash lookups instead of array scans
my %lookup = map { $_->{id} => $_ } @users;
my $user = $lookup{42};  # O(1) instead of O(n)

# Precompile regexes
my $pattern = qr/\b[A-Z]{2,}\b/;
```

---

## স্থাপনা
```bash
# FatPacker — self-contained scripts
fatpack pack script.pl > fatpacked.pl

# Starman production server
starman --workers 8 --port 5000 bin/app.pl
```

```dockerfile
FROM perl:5.38-slim
WORKDIR /app
COPY cpanfile* ./
RUN cpanm --installdeps --notest .
COPY . .
CMD ["perl", "bin/myapp.pl"]
```

---

## কখন পার্ল ব্যবহার করবেন
| দৃশ্যকল্প | কেন পার্ল | ভাল বিকল্প |
|------------|---------|---------|
| পাঠ্য প্রক্রিয়াকরণ / পার্সিং | বেস্ট-ইন-ক্লাস রেজেক্স ইঞ্জিন | স্ট্রাকচার্ড ডেটার জন্য পাইথন |
| লগ ফাইল বিশ্লেষণ | দ্রুত এক-লাইনার, প্রমাণিত সরঞ্জাম |  সাধারণ ক্ষেত্রে`awk`/ `sed`; জটিল জন্য পাইথন |
| সিস্টেম প্রশাসন | ঐতিহাসিকভাবে প্রভাবশালী | সাধারণ কাজের জন্য ব্যাশ/পাওয়ারশেল; জটিল জন্য পাইথন |
| উত্তরাধিকার সিস্টেম রক্ষণাবেক্ষণ | উৎপাদনে পার্লের লক্ষ লক্ষ লাইন | — |
| বায়োইনফরমেটিক্স | শক্তিশালী ঐতিহাসিক উপস্থিতি (BioPerl) | পাইথন (বায়োপাইথন), আর |
| দ্রুত তথ্য রূপান্তর | ওয়ান-লাইনার অপরাজেয় | `jq`,`awk`কাঠামোবদ্ধ বিন্যাসের জন্য |
| ওয়েব ডেভেলপমেন্ট | CGI যুগ শেষ | Python, Node.js, Go, PHP |
| নতুন বড় মাপের প্রকল্প | সম্প্রদায় এগিয়ে গেছে | যান, মরিচা, পাইথন |
| ডেটা সায়েন্স / এমএল | বাস্তুতন্ত্র নয় | পাইথন, আর |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: `my`,`our`এবং`local`এর মধ্যে পার্থক্য কী?
**A:** এই কীওয়ার্ডগুলি পরিবর্তনশীল স্কোপিং নিয়ন্ত্রণ করে:
```perl
# my — lexical scope (preferred)
my $x = 10;  # visible only in current block

# our — package global with lexical alias
our $VERSION = '1.0';  # package variable, accessible as $main::VERSION

# local — temporarily change a global
local $/ = undef;  # temporarily undefine input record separator
# original value restored when block exits
```

### প্রশ্ন 2: আমি কীভাবে পার্লে দক্ষতার সাথে টেক্সট ফাইলগুলি প্রক্রিয়া করব?
**A:** পার্ল টেক্সট প্রসেসিং এ এক্সেল। ডায়মন্ড অপারেটর এবং রেজেক্স ব্যবহার করুন:
```perl
# Line-by-line processing
while (my $line = <STDIN>) {
    chomp $line;
    $line =~ s/old/new/g;
    print "$line\n";
}

# One-liner (the classic Perl superpower)
# perl -pe 's/foo/bar/g' file.txt
# perl -ne 'print if /error/i' logfile.txt
# perl -lane 'print $F[0]' file.txt  # split on whitespace

# Slurp entire file
local $/;
my $content = <FILE>;
```

### প্রশ্ন 3: আমি কীভাবে রেফারেন্স এবং জটিল ডেটা স্ট্রাকচার ব্যবহার করব?
**A:** রেফারেন্সগুলি নেস্টেড কাঠামো তৈরি করার জন্য পার্লের উপায়:
```perl
# Array reference
my $aref = [1, 2, 3];
print $aref->[0];  # 1

# Hash reference
my $href = { name => 'Alice', age => 30 };
print $href->{name};  # Alice

# Nested structures
my $data = {
    users => [
        { name => 'Alice', scores => [95, 87, 92] },
        { name => 'Bob',   scores => [78, 88, 91] },
    ],
};
print $data->{users}[0]{scores}[2];  # 92
```

### প্রশ্ন 4: পার্লের বিশেষ ভেরিয়েবল কি কি আমার জানা উচিত?
**A:** পার্লের অনেকগুলি বিশেষ ভেরিয়েবল রয়েছে। সবচেয়ে গুরুত্বপূর্ণ:
```perl
$_     # default variable (topic)
$!     # system error message
$@     # eval error
$$     # process ID
$.     # current line number in last filehandle
$/     # input record separator (\n by default)
$\     # output record separator
$|     # autoflush (1 = on)
@ARGV  # command-line arguments
%ENV   # environment variables
```

### প্রশ্ন 5: আমি কীভাবে আধুনিক, রক্ষণাবেক্ষণযোগ্য পার্ল লিখব?
**A:** আধুনিক পার্লের জন্য সর্বোত্তম অনুশীলন:
- সর্বদা`strict`এবং`warnings`ব্যবহার করুন 
- সমস্ত ভেরিয়েবলের জন্য`my`ব্যবহার করুন
- আভিধানিক ফাইলহ্যান্ডেল ব্যবহার করুন:`open my $fh, '<', $file`
- CPAN থেকে মডিউল ব্যবহার করুন (OOP এর জন্য Moo/Moose, চেষ্টা করুন::ত্রুটির জন্য ক্ষুদ্র)
-`print`এর পরিবর্তে`say`ব্যবহার করুন (`feature 'say'` সহ)
-`perltidy`দিয়ে ফরম্যাট করুন
---

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: লগ ফাইল বিশ্লেষণ
**ধাপ 1: সমস্যাটি বুঝুন**
একটি Apache অ্যাক্সেস লগ পার্স করুন এবং IP ঠিকানা প্রতি অনুরোধ গণনা করুন।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
আইপি ঠিকানা বের করতে regex ব্যবহার করুন, ঘটনা গণনা করতে হ্যাশ করুন।
**ধাপ 3: প্রয়োগ করুন**```perl
use strict;
use warnings;

my %counts;
while (my $line = <>) {
    if ($line =~ /^(\S+)/) {
        $counts{$1}++;
    }
}

# Sort by count (descending)
for my $ip (sort { $counts{$b} <=> $counts{$a} } keys %counts) {
    printf "%-15s %d\n", $ip, $counts{$ip};
}
```

**ধাপ 4: প্রসারিত করুন**
CSV হিসাবে তারিখ ফিল্টারিং, স্থিতি কোড বিশ্লেষণ এবং আউটপুট যোগ করুন।
### সমস্যা 2: Regex এর সাথে ব্যাচ ফাইলের নামকরণ
**ধাপ 1: সমস্যাটি বুঝুন**
একটি প্যাটার্নের সাথে মিলে যাওয়া ফাইলগুলির নাম পরিবর্তন করুন, ফাইলের নামগুলি regex এর সাথে রূপান্তর করুন৷
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
ফাইলগুলি খুঁজতে`glob`বা`opendir`ব্যবহার করুন, নাম রূপান্তর করতে regex ব্যবহার করুন৷
**ধাপ 3: প্রয়োগ করুন**```perl
use strict;
use warnings;
use File::Copy;

my $dir = shift @ARGV || '.';
opendir my $dh, $dir or die "Cannot open $dir: $!";

for my $file (sort readdir $dh) {
    next unless $file =~ /^(\d{4})-(\d{2})-(\d{2})_(.+)$/;
    my $new_name = "$3-$2-$1_$4";  # Rearrange date format
    my $old = "$dir/$file";
    my $new = "$dir/$new_name";
    print "Renaming: $file -> $new_name\n";
    move($old, $new) or warn "Failed: $!";
}
closedir $dh;
```

**পদক্ষেপ 4: যাচাই করুন**
প্রথমে`--dry-run`পতাকা দিয়ে চালান (শুধু মুদ্রণ করুন, সরবেন না)।
### সমস্যা 3: একটি সাধারণ ওয়েব স্ক্র্যাপার তৈরি করা
**ধাপ 1: সমস্যাটি বুঝুন**
একটি ওয়েব পেজ আনুন এবং সমস্ত লিঙ্ক বের করুন.
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
আনার জন্য`LWP::Simple`ব্যবহার করুন এবং regex বা পার্স করার জন্য`HTML::LinkExtor`ব্যবহার করুন৷
**ধাপ 3: প্রয়োগ করুন**```perl
use strict;
use warnings;
use LWP::Simple;
use HTML::LinkExtor;

my $url = 'https://example.com';
my $html = get($url) or die "Cannot fetch $url";

my $parser = HTML::LinkExtor->new;
$parser->parse($html);

for my $link ($parser->links) {
    my ($tag, %attrs) = @$link;
    print "$attrs{href}\n" if $attrs{href};
}
```

**ধাপ 4: প্রসারিত করুন**
আপেক্ষিক URL গুলি পরিচালনা করুন, ডোমেন দ্বারা ফিল্টার করুন এবং পৃষ্ঠা সংখ্যা অনুসরণ করুন৷
---

## সারাংশ
পার্লের সোনালী যুগ চলে গেছে, কিন্তু এর প্রভাব সর্বত্র। রেগুলার এক্সপ্রেশন সহ প্রতিটি ভাষা, প্রতিটি প্যাকেজ ম্যানেজার সিপিএএন এর আদলে তৈরি, এবং`map`/`grep`/`reduce`সহ প্রতিটি সিস্টেম পার্লের ডিএনএ বহন করে। নতুন প্রজেক্টের জন্য, বেশিরভাগ ডেভেলপাররা পাইথন বা গো-তে পৌঁছান। কিন্তু পার্ল টেক্সট প্রসেসিং, দ্রুত অটোমেশন এবং বিশ্বব্যাপী গুরুত্বপূর্ণ পরিকাঠামো চলমান পার্ল কোডের বিশাল পরিমাণ বজায় রাখার জন্য একটি শক্তিশালী হাতিয়ার হিসেবে রয়ে গেছে। পার্ল বোঝার অর্থ আধুনিক প্রোগ্রামিং কোথা থেকে এসেছে তা বোঝাও — এটি আজকে আমরা যে সরঞ্জামগুলি এবং নিদর্শনগুলি ব্যবহার করি সেগুলিকে আকার দিয়েছে৷