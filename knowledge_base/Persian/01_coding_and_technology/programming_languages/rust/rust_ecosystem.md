---
# Metadata
title: "Rust — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Rust ecosystem including package management, build tools, testing, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [rust, ecosystem, tooling, cargo, testing, web, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "20 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# زنگ - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، چارچوب‌ها و زیرساخت‌های ضروری در اکوسیستم Rust را پوشش می‌دهد.
---

## مدیریت بسته و ساخت
| ابزار | هدف |
|------|---------|
| **محموله** | Package Manager, build system, test runner |
| **crates.io** | رجیستری پکیج رسمی |
| **rustup** | نصب کننده و مدیر Toolchain |
| **محموله-ویرایش** | افزودن/حذف/ارتقای وابستگی |
| **محموله-ساعت** | بازسازی بر روی تغییرات فایل |
| **ممیزی محموله** | بررسی کننده آسیب پذیری امنیتی |
| **محموله-کلیپی** | لینتر (توکار) |
| **cargo-fmt** | فرمت کننده کد (rustfmt) |
```bash
cargo new project               # new binary project
cargo new --lib project         # new library
cargo build                     # debug build
cargo build --release           # optimized build
cargo run                       # build and run
cargo test                      # run tests
cargo clippy                    # lint
cargo fmt                       # format
cargo doc --open                # generate and view docs
```

---

## تست
| ابزار | هدف |
|------|---------|
| **تست محموله** | واحد داخلی + تست های یکپارچه سازی |
| **معیار** | چارچوب معیار |
| **اعتراض** | تست مبتنی بر اموال |
| **مسخره** | چارچوب تمسخر آمیز |
| **tokio::test** | پشتیبانی از تست Async |
| **اینستا** | تست عکس فوری |
```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_addition() {
        assert_eq!(2 + 2, 4);
    }

    #[test]
    #[should_panic(expected = "overflow")]
    fn test_overflow() {
        panic!("overflow!");
    }
}
```

---

## چارچوب های وب
| چارچوب | نوع | بهترین برای |
|-----------|------|----------|
| **Actix-web** | عملکرد | APIهای پرتوان |
| **Axum** | بومی توکیو | وب مدرن همگام |
| **راکت** | ارگونومیک | تجربه توسعه دهنده |
| **Warp** | عملکردی | فیلترهای قابل ترکیب |
| ** جزر و مد ** | ساده | حداقل API |
---

## زمان اجرا ناهمگام
| زمان اجرا | ویژگی ها |
|---------|----------|
| **توکیو** | غالب، با امکانات کامل |
| **async-std** | std-like async |
| **اسمول** | سبک |
---

## پایگاه داده
| جعبه | پایگاه داده |
|-------|----------|
| **دیزل** | PostgreSQL، MySQL، SQLite (ORM) |
| **SQLx** | PostgreSQL، MySQL، SQLite (ناهمگام، زمان کامپایل بررسی شده) |
| **SeaORM** | ORM غیر همگام، پرس و جوهای پویا |
| **قرمز** | کلید-مقدار جاسازی شده |
| **سورتمه** | کلید-مقدار جاسازی شده |
---

## سریال سازی
| جعبه | هدف |
|-------|---------|
| **سرد** | چارچوب سریال سازی |
| **serde_json** | JSON |
| **serde_yaml** | YAML |
| **تومل** | TOML (محموله از این استفاده می کند) |
| **bincode** | باینری |
| **پروست** | بافرهای پروتکل |
---

## ابزارهای CLI
| جعبه | هدف |
|-------|---------|
| **کف زدن** | تجزیه آرگومان |
| **راتاتوی** | رابط کاربری ترمینال |
| **کراسترم** | ترمینال کراس پلت فرم |
| **نشانگر** | نوارهای پیشرفت |
| **گفتگو** | درخواست های کاربر |
| **کنسول** | یک ظاهر طراحی ترمینال |
---

## جاسازی شده و سیستم ها
| جعبه | هدف |
|-------|---------|
| **embedded-hal** | انتزاع سخت افزار |
| **no_std** | برنامه نویسی بره متال |
| **wasm-bindgen** | WebAssembly interop |
| **تونیک** | gRPC |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **VS Code + زنگ زدگی** | پشتیبانی عالی LSP |
| **پلاگین CLion + Rust** | تجربه کامل JetBrains |
| **Neovim + زنگ زدگی** | مبتنی بر ترمینال |
| **مارپیچ** | ویرایشگر Rust-native |
---

## استقرار
| روش | ابزار |
|--------|------|
| **باینری استاتیک** | `cargo build --release`(تک باینری!) |
| **تقاطع کامپایل** | `cross`(مبتنی بر داکر) |
| **ظروف** | داکر، بدون توزیع |
| **WebAssembly** | `wasm-pack`|
| **مسل** | پیوند استاتیک برای لینوکس |
---

## خلاصه
اکوسیستم Rust منسجم و باکیفیت است که حول محور Cargo متمرکز شده است. پشته استاندارد عبارت است از: **Cargo** برای همه چیز (ساخت، آزمایش، انتشار)، **Tokio** برای async، **Axum** یا **Actix-web** برای وب، **serde** برای سریال سازی، **SQLx** برای پایگاه داده، و **clap** برای CLI ها. ویژگی قاتل Rust استقرار به عنوان یک باینری استاتیک واحد بدون وابستگی زمان اجرا است. اکوسیستم صحت و عملکرد را به راحتی اولویت می دهد.