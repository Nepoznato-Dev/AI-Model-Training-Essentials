<!--
---
# Metadata
title: "Perl — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Perl ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [perl, ecosystem, tooling, cpan, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "13 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Perl — Hướng dẫn về hệ sinh thái và công cụ
Hướng dẫn này bao gồm các công cụ, khung và cơ sở hạ tầng thiết yếu trong hệ sinh thái Perl.
---

## Phiên bản Perl
| Phiên bản | Ghi chú |
|----------|-------|
| **Perl 5.38+** | Hiện tại ổn định |
| **Perl 5,40** | Mới nhất với các tính năng mới |
| **Raku (Perl 6)** | Thiết kế lại hiện đại (ngôn ngữ riêng) |
| **Con nai sừng tấm** | Hệ thống OO hiện đại |
| **Moo** | Nai sừng tấm nhẹ |
```bash
perl -v                   # check version
perl script.pl            # run script
perl -e 'print "Hello\n"' # inline execution
perlbrew list             # manage Perl versions
perlbrew install 5.40.0   # install version
```

---

## Quản lý gói
| Công cụ | Mục đích |
|------|----------|
| **CPAN** | Mạng lưu trữ Perl toàn diện (hơn 200.000 mô-đun) |
| **cpanm** | Trình cài đặt CPAN nhẹ |
| **cpanfile** | Khai báo phụ thuộc |
| **Thùng** | Gói phụ thuộc (như Bundler) |
| **Quận::Zilla** | Nhà xây dựng phân phối |
| **Ứng dụng::cpanminus** | Máy khách CPAN tối thiểu |
```bash
cpanm Module::Name          # install module
cpanm --installdeps .       # install from cpanfile
cpanm --self-upgrade        # upgrade cpanm
carton install              # install from cpanfile (Carton)
carton exec perl script.pl  # run with bundled deps
```

```perl
# cpanfile
requires 'perl', '5.038';
requires 'Mojolicious', '>= 9.0';
requires 'DBI', '>= 1.643';
requires 'JSON::XS';

on 'test' => sub {
    requires 'Test::More', '>= 1.302';
    requires 'Test::Fatal';
    requires 'Test::MockModule';
};
```

---

## Khung web
| Khung | Loại | Tốt nhất cho |
|----------|------|----------|
| **Vui vẻ** | Toàn ngăn xếp | Hiện đại, sạch sẽ, có kèm pin |
| **Vũ công2** | Vi mô | Giống Sinatra, nhẹ |
| **Chất xúc tác** | Toàn ngăn xếp | Doanh nghiệp, MVC |
| **Pck** | Bộ công cụ PSGI | Giao diện web cấp thấp |
| **Người ngôi sao** | Máy chủ HTTP | Máy chủ PSGI |
```perl
# Mojolicious::Lite example
use Mojolicious::Lite -signatures;

get '/hello' => sub ($c) {
    $c->render(text => 'Hello, World!');
};

get '/users/:id' => sub ($c) {
    my $id = $c->param('id');
    my $user = $c->users->find($id);
    $c->render(json => $user);
};

post '/users' => sub ($c) {
    my $data = $c->req->json;
    my $user = $c->users->create($data);
    $c->render(json => $user, status => 201);
};

app->start;
```

```perl
# Dancer2 example
use Dancer2;

get '/hello' => sub {
    return "Hello, World!";
};

get '/users/:id' => sub {
    my $id = route_parameters->get('id');
    my $user = schema->resultset('User')->find($id);
    return to_json($user);
};

dance;
```

---

## Cơ sở dữ liệu
| Công nghệ | Loại |
|----------||------|
| **DBI** | Chuẩn giao diện cơ sở dữ liệu |
| **DBD::SQLite** | Trình điều khiển SQLite |
| **DBD::Trang** | Trình điều khiển PostgreSQL |
| **DBD::mysql** | Trình điều khiển MySQL |
| **DBIx::Lớp** | ORM đầy đủ |
| **Mojo::Pg** | PostgreSQL (Mojolicious) |
| **Làm lại** | Khách hàng Redis |
```perl
# DBI example
use DBI;

my $dbh = DBI->connect("dbi:SQLite:dbname=mydb.sqlite", "", "", {
    RaiseError => 1,
    PrintError => 0,
});

my $sth = $dbh->prepare("SELECT * FROM users WHERE age > ?");
$sth->execute(18);

while (my $row = $sth->fetchrow_hashref) {
    print "$row->{name} ($row->{email})\n";
}
```

```perl
# DBIx::Class example
package MyApp::Schema::Result::User;
use base 'DBIx::Class::Core';
__PACKAGE__->table('users');
__PACKAGE__->add_columns(qw/id name email age/);
__PACKAGE__->set_primary_key('id');

# Usage
my @adults = $schema->resultset('User')->search(
    { age => { '>' => 18 } },
    { order_by => 'name' }
);
```

---

##Thử nghiệm
| Khung | Mục đích |
|----------||----------|
| **Kiểm tra::Thêm** | Khung kiểm tra tiêu chuẩn |
| **Test2::Suite** | Thử nghiệm hiện đại (được khuyến nghị) |
| **Kiểm tra::Chết người** | Kiểm tra ngoại lệ |
| **Kiểm tra::MockModule** | Chế giễu |
| **Kiểm tra::Sâu** | So sánh dữ liệu phức tạp |
| **Kiểm tra::Đầu ra** | Chụp STDOUT/STDERR |
| **chứng minh** | Người chạy thử |
```perl
# Test2::V0 example
use Test2::V0;
use MyApp::UserService;

my $service = MyApp::UserService->new();

subtest 'find user' => sub {
    my $user = $service->find(1);
    is($user->name, 'Alice', 'found user by id');
    ok(defined $user, 'user is defined');
};

subtest 'not found' => sub {
    my $user = $service->find(999);
    is($user, undef, 'returns undef for missing user');
};

done_testing();
```

```bash
prove -lrv t/             # run tests (verbose)
prove -j4 t/              # parallel testing
```

---

## Chất lượng mã
| Công cụ | Mục đích |
|------|----------|
| ** phê bình ** | Mã linting và phong cách |
| **nguy hiểm** | Định dạng mã |
| **Phát::Bìa** | Bảo hiểm mã |
| **Perl::Nhà phê bình** | Thực thi chính sách |
| **Kiểm tra::Perl::Critic** | Phê bình trong các bài kiểm tra |
```perl
# .perlcriticrc
severity = 3
[Variables::ProhibitPunctuationVars]
severity = 4
```

```bash
perlcritic --brutal lib/  # lint
perltidy -b lib/          # format
```

---

## Thư viện chính
| Thư viện | Mục đích |
|----------|----------|
| **Moose / Moo** | Hệ thống đối tượng hiện đại |
| **Vui vẻ** | Khung web |
| **DBI** | Giao diện cơ sở dữ liệu |
| **DBIx::Lớp** | ORM |
| **JSON::XS / Cpanel::JSON::XS** | Phân tích cú pháp JSON |
| **YAML::XS** | Phân tích cú pháp YAML |
| **LWP::Tác nhân người dùng** | Máy khách HTTP |
| **HTTP::Tiny** | Máy khách HTTP tối thiểu |
| **IO::Socket::SSL** | SSL/TLS |
| **Song song::ForkManager** | Xử lý song song |
| **MCE** | Động cơ nhiều lõi |
| **Hãy thử::Tiny** | Xử lý ngoại lệ |
| **Đường dẫn::Tiny** | Đường dẫn tệp |
| **Danh sách::Sử dụng** | Liệt kê tiện ích |
| **Vô hướng::Sử dụng** | Tiện ích vô hướng |
| **Ngày giờ** | Xử lý ngày/giờ |
| **Nhật ký::Bất kỳ** | Mặt tiền khai thác gỗ |
| **Cấu hình::Bất kỳ** | Cấu hình |
---

## Xử lý văn bản
| Công cụ | Mục đích |
|----------|----------|
| **Biểu thức chính quy** | Tích hợp, mạnh mẽ |
| **Mẫu::Bộ công cụ** | Công cụ tạo mẫu |
| **Văn bản::CSV** | Phân tích cú pháp CSV |
| **XML::LibXML** | Xử lý XML |
| **Mojo::DOM** | Phân tích cú pháp HTML/XML |
---

## IDE & Trình chỉnh sửa
| IDE | Điểm mạnh |
|------|-------------|
| **Mã VS + Perl** | Hỗ trợ ngôn ngữ Perl |
| **vim-Perl** | Hỗ trợ Vim Perl |
| **Emacs + chế độ cperl** | Môi trường Perl cổ điển |
| **Komodo** | IDE Perl ActiveState |
---

## Triển khai
| Phương pháp | Ghi chú |
|--------|-------|
| **Người ngôi sao** | Máy chủ web PSGI |
| ** thôi miên** | Máy chủ vui vẻ |
| **Docker** | Được đóng gói |
| **PAR::Người đóng gói** | Tệp thực thi độc lập |
| **Thùng** | Gói phụ thuộc |
| **cpanfile + Thùng carton** | Triển khai có thể lặp lại |
---

## Bản tóm tắt
Hệ sinh thái của Perl rất rộng lớn và trưởng thành, với CPAN lưu trữ hơn 200.000 mô-đun. Ngăn xếp tiêu chuẩn là: **Perl 5.38+** làm thời gian chạy, **cpanm** cho các gói, **Mojolicious** cho web, **DBI** + **DBIx::Class** cho cơ sở dữ liệu, **Test2::Suite** cho thử nghiệm, **perlcritic** cho linting và **perltidy** cho định dạng. Perl vượt trội về xử lý văn bản, quản trị hệ thống, tin sinh học và các ứng dụng web truyền thống. Perl hiện đại (5.38+) với chữ ký, tham chiếu hậu tố và thử/bắt rõ ràng hơn đáng kể so với danh tiếng của nó. Hệ sinh thái này lý tưởng cho việc viết kịch bản quản trị hệ thống, xử lý dữ liệu và tạo mẫu nhanh.