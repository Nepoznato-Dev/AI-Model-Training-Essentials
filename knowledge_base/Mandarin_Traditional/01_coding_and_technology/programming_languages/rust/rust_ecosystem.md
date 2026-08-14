<!--
---
# Metadata
title: "Rust — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Rust ecosystem including package management, build tools, testing, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# Rust — 生態系與工具指南
本指南涵蓋了 Rust 生態系統中的基本工具、框架和基礎設施。
---

## 套件管理與構建
|工具|目的|
|------|---------|
| **貨物** |包管理器、建置系統、測試運行器 |
| **crates.io** |官方包註冊表 |
| **生鏽** |工具鏈安裝程序與管理器 |
| **貨物編輯** |新增/刪除/升級依賴項 |
| **貨物監視** |文件更改後重建 |
| **貨物審核** |安全漏洞檢查器|
| **貨物夾** | Linter（內建）|
| **貨物快速運輸** |代碼格式化程序 (rustfmt) |
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

## 測試
|工具|目的|
|------|---------|
| **貨物測試** |內建單元+整合測試|
| **標準** |基準測試框架|
| **道具測試** |基於屬性的測試 |
| **模擬** |模擬框架 |
| **東京::測試** |非同步測試支援 |
| **insta** |快照測試|
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

## 網路框架
|框架|類型 |最適合 |
|------------|------|----------|
| **Actix-web** |效能|高通量 API |
| **阿克蘇姆** |東京人 |現代非同步網路 |
| **火箭** |符合人體工學 |開發者經驗|
| **扭曲** |功能性|可組合過濾器 |
| **潮汐** |簡單|最少的 API |
---

## 非同步運行時
|運行時 |特點|
|---------|----------|
| **東京** |霸氣、功能齊全|
| **非同步標準** |類似 std 的非同步 |
| **小摩爾** |輕量化|
---

## 資料庫
|板條箱 |資料庫|
|--------|----------|
| **柴油** | PostgreSQL、MySQL、SQLite (ORM) |
| **SQLx** | PostgreSQL、MySQL、SQLite（非同步、編譯時檢查）|
| **SeaORM** |非同步 ORM、動態查詢 |
| **紅布** |嵌入鍵值 |
| **雪橇** |嵌入鍵值 |
---

## 序列化
|板條箱 |目的|
|--------|---------|
| **塞尔德** |序列化框架|
| **serde_json** | JSON |
| **serde_yaml** | yaml |
| **湯姆** | TOML（貨物使用這個）|
| **二進位代碼** |二進位 |
| **前列腺** |协议缓冲区 |
---

## CLI 工具
|板條箱 |目的|
|--------|---------|
| **鼓掌** |參數解析 |
| **拉圖伊** |終端使用者介面 |
| **交叉項** |跨平台終端 |
| **指示** |進度條|
| **對話者** |使用者提示|
| **控制台** |終端樣式 |
---

## 嵌入式與系統
|板條箱 |目的|
|--------|---------|
| **嵌入式哈爾** |硬體抽象|
| **無標準** |裸機程式設計 |
| **wasm-bindgen** | WebAssembly 互通 |
| **補品** | gRPC |
---

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **VS Code + rust 分析器** |出色的LSP支援|
| **CLion + Rust 外掛程式** |完整的 JetBrains 體驗 |
| **Neovim + 銹分析儀** |基於終端 |
| **螺旋** | Rust 原生編輯器 |
---

## 部署
|方法|工具|
|--------|------|
| **靜態二進位** | `cargo build --release`（單一二進位！）|
| **交叉編譯** | `cross`（基於 Docker）|
| **容器** | Docker，無發行版 |
| **WebAssembly** |`wasm-pack`|
| **穆斯林** | Linux 的靜態連結 |
---

＃＃ 概括
Rust 的生態系統具有凝聚力和高品質，以 Cargo 為中心。標準堆疊是：**Cargo** 用於所有內容（建置、測試、發布），**Tokio** 用於非同步，**Axum** 或 **Actix-web** 用於 Web，**serde** 用於序列化，**SQLx** 用於資料庫，**clap** 用於 CLI。 Rust 的殺手級功能是部署為單一靜態二進位文件，沒有執行時間依賴性。該生態系統優先考慮正確性和性能而不是便利性。