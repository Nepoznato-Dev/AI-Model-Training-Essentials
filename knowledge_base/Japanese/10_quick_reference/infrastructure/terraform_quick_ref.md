---
# Metadata
title: "Terraform and Infrastructure as Code"
description: "IaC concepts, Terraform commands, state management, modules"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [terraform, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Terraform とコードとしてのインフラストラクチャ
Terraform は、最も広く使用されている Infrastructure as Code (IaC) ツールです。これを使用すると、バージョン管理、レビュー、テスト、自動化が可能な宣言型構成ファイルでクラウド インフラストラクチャ (サーバー、データベース、ネットワーク、権限) を定義できます。クラウド コンソールをクリックする代わりに、インフラストラクチャの望ましい状態を記述するコードを記述すると、Terraform がどのような変更を加えるべきかを判断します。
---

## コアコンセプト
|コンセプト |説明 |
|----------|---------------|
| **プロバイダー** |特定のクラウド プラットフォーム (AWS、Azure、GCP など) を管理するプラグイン |
| **リソース** |インフラストラクチャ オブジェクト (サーバー、データベース、ネットワーク) |
| **州** |どのようなインフラストラクチャが存在するかについての Terraform の記録。状態ファイルに保存される |
| **計画** | Terraform が行う変更のプレビュー |
| **適用** |計画を実行します。インフラストラクチャの作成/更新/破棄 |
| **モジュール** |再利用可能なリソースのコレクション |
| **変数** |構成の入力パラメータ |
| **出力** |モジュールまたは構成からエクスポートされた値 |
| **データソース** |既存のインフラストラクチャから情報を読み取る |
---

## 基本的なワークフロー
|ステップ |コマンド |説明 |
|------|--------|---------------|
| **1.構成の書き込み** |`.tf`ファイルを作成する |プロバイダー、リソース、変数を定義する |
| **2.初期化** | `terraform init`|ダウンロードプロバイダー。バックエンドをセットアップする |
| **3.形式** | `terraform fmt`|書式設定を標準化する |
| **4.検証** | `terraform validate`|構文と構成を確認する |
| **5.計画** | `terraform plan`|変更のプレビュー (ドライラン) |
| **6.適用** | `terraform apply`|インフラストラクチャの作成または更新 |
| **7.破壊** | `terraform destroy`|すべての管理されたインフラストラクチャを破壊する |
---

## 一般的なコマンド
|コマンド |説明 |
|----------|---------------|
| `terraform init`|作業ディレクトリを初期化します。プロバイダーとモジュールをダウンロードする |
| `terraform plan`|どのような変更が行われるかを表示する |
| `terraform apply`|変更を適用します。確認をスキップするには`-auto-approve`を追加します。
| `terraform destroy`|すべての管理リソースを破棄する |
| `terraform fmt`|構成ファイルを標準スタイルにフォーマットする |
| `terraform validate`|構成構文を検証する |
| `terraform output`|出力値を表示 |
| `terraform state list`|状態 | 内のすべてのリソースをリストします。
| `terraform state show <resource>`|特定のリソースの詳細を表示する |
| `terraform import <resource> <id>`|既存のインフラストラクチャを状態にインポートする |
| `terraform taint <resource>`|次回の適用時にリソースを再作成するようにマークする |
| `terraform refresh`|実際のインフラストラクチャと一致するように状態を更新する |
| `terraform graph`|視覚的な依存関係グラフの生成 (DOT 形式) |
| `terraform console`|式をテストするための対話型コンソール |
---

## 状態管理
|ベストプラクティス |説明 |
|--------------|---------------|
| **リモート状態** |状態を S3、GCS、Azure Blob、または Terraform Cloud に保存します。決してローカルには保存しません。
| **状態のロック** | DynamoDB (S3 バックエンド) またはネイティブ ロックを使用して同時変更を防止する |
| **状態の暗号化** |状態ファイルの保存時の暗号化を有効にする (機密データが含まれる) |
| **国家の分離** |異なる環境またはチームに対して個別の状態ファイルを使用する |
| **状態のバックアップ** |リモート バックエンドは自動的にバージョン状態を示します。これを有効にしておきます |
| **状態を手動で編集しないでください** |代わりに`terraform state mv`、`rm`、`import`を使用してください。
---

## モジュール構造
```
module/
├── main.tf          # Primary resources
├── variables.tf     # Input variables
├── outputs.tf       # Output values
├── versions.tf      # Provider and Terraform version constraints
├── README.md        # Documentation
└── examples/        # Example usage
    └── basic/
        └── main.tf
```

---

## 変数の型
|タイプ |例 |使用例 |
|------|--------|----------|
| **文字列** | `variable "region" { type = string }`|単一のテキスト値 |
| **番号** | `variable "count" { type = number }`|数値 |
| **ブール** | `variable "enable" { type = bool }`|真/偽フラグ |
| **リスト** | `variable "zones" { type = list(string) }`|注文されたコレクション |
| **地図** | `variable "tags" { type = map(string) }`|キーと値のペア |
| **オブジェクト** | `variable "config" { type = object({...}) }`|構造化された構成 |
---

## 一般的なパターン
|パターン |説明 |
|----------|---------------|
| **数** | `count = 3`はリソースの複数のインスタンスを作成します。
| **それぞれについて** | `for_each = var.items`はマップまたはセットを反復処理します。
| **ダイナミック ブロック** |繰り返しネストされたブロック (イングレス ルールなど) を生成します。
| **ローカル値** | `locals { ... }`計算値と繰り返しの削減 |
| **データソース** |既存のインフラストラクチャを読み取る (例: 既存の VPC を見つける) |
| **プロビジョナー** |作成後にリソースに対してスクリプトを実行します (慎重に使用してください) |
| **ワークスペース** |同じ構成内の異なる環境の個別の状態 |
---

## トラブルシューティング
|問題 |ソリューション |
|----------|----------|
| **状態ドリフト** |`terraform plan`を実行して違いを確認します。 `terraform apply`を調整する |
| **ロック状態** |誰がロックを持っているかを確認してください。安全であれば`terraform force-unlock`を使用してください。
| **プロバイダーエラー** |資格情報を確認してください。プロバイダーのバージョンを更新します。 API 制限を確認する |
| **インポートの競合** |リソースはすでに状態にあります。最初に`terraform state rm`を使用してください。
| **循環依存関係** |リソースを再構築します。`depends_on`は慎重に使用してください。
| **大規模な州** |モジュールに分割します。部分的な操作には`-target`を使用します。
---

＃＃ まとめ
Terraform は、宣言型構成ファイルを通じてインフラストラクチャを管理します。ワークフローは、構成の書き込み → 初期化 → 計画 → 適用です。状態は存在するものを追跡するため、ロックしてリモートに保存する必要があります。モジュールにより再利用が可能になります。変数は構成をパラメータ化します。重要な原則は次のとおりです。インフラストラクチャをコードとして扱う (バージョン管理、レビュー、テスト)。状態を手動で編集しないでください。申請前に計画を立てる。ロック付きのリモート状態を使用します。保守性を高めるためにモジュールを使用して構成を構成します。