---
# Metadata
title: "Cloud Services Comparison"
description: "AWS vs Azure vs GCP side-by-side comparison"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cloud, services, comparison, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# クラウドサービスの比較
3 つの主要なクラウド プロバイダー (AWS、Azure、Google Cloud) を、コンピューティング、ストレージ、データベース、AI/ML、ネットワーキング、モニタリング、コードとしてのインフラストラクチャの面で並べて比較します。アーキテクトがどのプラットフォームを使用するかを決定する場合、またはあるクラウドから別のクラウドにサービスをマッピングする場合に役立ちます。
---

## プロバイダーの概要
| | AWS |アズール |グーグルクラウド（GCP） |
|---|-----|------|----------|
| **市場シェア** | ~31% (最大) | ~25% (2 番目) | ~11% (3 番目、最も急速に成長) |
| **強み** |幅広いサービス。成熟;エコシステム |エンタープライズ統合。ハイブリッドクラウド。 Microsoft スタック |データ/AI; Kubernetes;グローバルネットワーク |
| **こんな用途に最適** |スタートアップから企業まで。最も広範なサービスカタログ | Microsoft/Active Directory を使用している企業。ハイブリッド |データ集約型のワークロード。 Kubernetes ネイティブ。 AI/ML |
| **地域** | 33 リージョン、105 AZ | 60以上の地域 | 40 以上のリージョン、100 以上のゾーン |
| **無料利用枠** | 12 か月の無料枠 + 常時無料 | 12 か月無料 + $200 クレジット | 90 日間 $300 クレジット + 常時無料 |
---

## 計算する
|サービスカテゴリー | AWS |アズール | GCP |
|------|-----|----------|-----|
| **仮想マシン** | EC2 (エラスティック コンピューティング クラウド) |仮想マシン |コンピューティング エンジン |
| **自動スケーリング** | Auto Scaling グループ |仮想マシン スケール セット |インスタンス グループ |
| **サーバーレス機能** |ラムダ | Azure 関数 |クラウド機能 |
| **コンテナ レジストリ** | ECR (エラスティック コンテナ レジストリ) | Azure コンテナー レジストリ |アーティファクトレジストリ |
| **コンテナ オーケストレーション** | ECS / EKS | ACS / AKS | GKE / クラウドラン |
| **サーバーレス コンテナ** |ファーゲート |コンテナアプリ |クラウドラン |
| **アプリ プラットフォーム (PaaS)** | Elastic Beanstalk、アプリランナー |アプリサービス |アプリエンジン |
| **バッチ処理** | AWS バッチ |アズールバッチ |クラウドバッチ |
| **GPU / AI コンピューティング** | EC2 (P4d、P5 インスタンス) | NC/ND シリーズ VM | A2/A3 VM。 TPU |
### VM 価格モデル
|モデル | AWS |アズール | GCP |
|----------|-----|----------|-----|
| **オンデマンド** |オンデマンドインスタンス |従量課金制 |オンデマンド |
| **予約済み/コミット済み** |リザーブドインスタンス (1 ～ 3 年) |予約済み VM (1 ～ 3 年) |確約利用割引 (1 ～ 3 年間) |
| **スポット / 中断可能** |スポットインスタンス |スポット VM |プリエンプティブル / スポット VM |
| **貯蓄プラン** |貯蓄プラン |貯蓄プラン |確約利用割引 |
---

＃＃ ストレージ
|サービスカテゴリー | AWS |アズール | GCP |
|------|-----|----------|-----|
| **オブジェクト ストレージ** | S3 | BLOB ストレージ |クラウドストレージ |
| **ブロック ストレージ** | EBS |管理対象ディスク |永続ディスク |
| **ファイル ストレージ** | EFS、FSx | Azure ファイル |ファイルストア |
| **アーカイブ / コールド** | S3 氷河、ディープ アーカイブ | BLOB のクール/アーカイブ層 |クラウド ストレージ コールドライン/アーカイブ |
| **データ転送** |スノーボール、データ同期 |データボックス |転送アプライアンス |
### ストレージ クラスの比較
|使用例 | AWS S3 |アズールブロブ | GCP クラウド ストレージ |
|----------|----------|---------------|----------|
| **頻繁なアクセス** | S3 スタンダード |ホット |標準 |
| **アクセス頻度が低い** | S3 標準-IA |クール |ニアライン |
| **稀なアクセス** | S3 ワン ゾーン - IA | — |コールドライン |
| **アーカイブ** | S3 氷河 / ディープ アーカイブ |アーカイブ |アーカイブ |
---

## データベース
|サービスカテゴリー | AWS |アズール | GCP |
|------|-----|----------|-----|
| **リレーショナル (マネージド)** | RDS (MySQL、PostgreSQL、Oracle、SQL Server) | Azure データベース (MySQL、PostgreSQL); Azure SQL | Cloud SQL (MySQL、PostgreSQL) |
| **リレーショナル (クラウドネイティブ)** | Aurora (MySQL/PostgreSQL 互換) | Azure SQL データベース (エラスティック プール) | Cloud Spanner (グローバルに分散) |
| **NoSQL (ドキュメント)** |ダイナモDB | Cosmos DB (MongoDB API、SQL API) |ファイアストア;データストア |
| **NoSQL (ワイドカラム)** | DynamoDB (も) | Cosmos DB (Cassandra API) |ビッグテーブル |
| **NoSQL (キーと値)** | DynamoDB、ElastiCache | Redis 用 Azure キャッシュ |メモリストア (Redis) |
| **グラフ** |ネプチューン | Cosmos DB (グレムリン API) | — |
| **時系列** |タイムストリーム | Azure データ エクスプローラー | — |
| **元帳** |クイーンズランド州 | Azure 機密台帳 | — |
| **インメモリ キャッシュ** | ElastiCache (Redis、Memcached) | Redis 用 Azure キャッシュ |メモリーストア |
| **検索** |オープンサーチサービス | Azure AI 検索 |クラウド検索; Vertex AI 検索 |
| **データ ウェアハウス** |赤方偏移 |シナプス分析 |ビッグクエリ |
---

## AI と機械学習
|サービスカテゴリー | AWS |アズール | GCP |
|------|-----|----------|-----|
| **ML プラットフォーム** |セージメーカー | Azure 機械学習 |頂点 AI |
| **事前トレーニングされた API** | Rekognition (ビジョン)、Polly (TTS)、Comprehend (NLP)、Transcribe |認知サービス (視覚、音声、言語、意思決定) | Vision AI、Speech-to-Text、自然言語 API |
| **LLM / 生成 AI** |岩盤 (クロード、ラマ、タイタン) | Azure OpenAI サービス (GPT-4、DALL-E) | Vertex AI (ジェミニ);モデルガーデン |
| **ベクター / 埋め込み** | OpenSearch (k-NN)、Bedrock 知識ベース | Azure AI 検索 (ベクター) | Vertex AI ベクトル検索、AlloyDB |
| **MLOps** | SageMaker パイプライン、モデル レジストリ | Azure ML パイプライン、モデル レジストリ | Vertex AI パイプライン、モデル レジストリ |
| **データのラベル付け** | SageMaker グラウンド トゥルース | Azure ML データのラベル付け | Vertex AI データのラベル付け |
| **会話型 AI** |レックス | Azure ボット サービス |ダイアログフロー CX / ES |
| **翻訳** |翻訳 |翻訳者 |翻訳API |
---

## ネットワーキング
|サービスカテゴリー | AWS |アズール | GCP |
|------|-----|----------|-----|
| **仮想ネットワーク** | VPC |仮想ネットワーク (VNet) | VPC |
| **負荷分散** | ELB/ALB/NLB/CLB |ロードバランサー (アプリケーション、ネットワーク、ゲートウェイ) |クラウド負荷分散 |
| **DNS** |ルート53 | Azure DNS |クラウドDNS |
| **CDN** |クラウドフロント |アズールフロントドア |クラウドCDN |
| **API ゲートウェイ** | APIゲートウェイ | API管理 | APIゲートウェイ |
| **VPN** |サイト間 VPN、クライアント VPN | VPN ゲートウェイ |クラウドVPN |
| **直接接続 / ExpressRoute** |ダイレクトコネクト |エクスプレスルート |クラウドインターコネクト |
| **プライベートリンク** | PrivateLink、VPC エンドポイント |プライベート リンク、プライベート エンドポイント |プライベート サービス コネクト |
| **ファイアウォール** | WAF、ネットワーク ファイアウォール | Azure ファイアウォール、WAF |クラウドアーマー、ファイアウォール |
| **DDoS 保護** |シールド スタンダード / アドバンス | DDoS 保護 |クラウドアーマー |
---

## 監視とロギング
|サービスカテゴリー | AWS |アズール | GCP |
|------|-----|----------|-----|
| **メトリクス / モニタリング** |クラウドウォッチ | Azure モニター |クラウド モニタリング (Stackdriver) |
| **ロギング** | CloudWatch ログ |ログ分析 (Azure Monitor ログ) |クラウドロギング |
| **トレース** | X線 |アプリケーションインサイト |クラウドトレース |
| **警告** | CloudWatch アラーム | Azure モニターのアラート |クラウド監視アラート |
| **ダッシュボード** | CloudWatch ダッシュボード | Azure ワークブック/ダッシュボード |クラウド監視ダッシュボード |
| **エラー追跡** | CloudWatch 合成 |アプリケーションインサイト |クラウドエラーレポート |
| **サードパーティ** | Datadog、New Relic、PagerDuty | Datadog、New Relic、PagerDuty | Datadog、New Relic、PagerDuty |
---

## コードとしてのインフラストラクチャと DevOps
|サービスカテゴリー | AWS |アズール | GCP |
|------|-----|----------|-----|
| **IaC (ネイティブ)** |クラウドフォーメーション | ARM テンプレート / 上腕二頭筋 |導入マネージャー / Pulumi |
| **IaC (クロスクラウド)** | Terraform、プルミ、CDK | Terraform、プルミ、上腕二頭筋 | Terraform、プルミ |
| **CI/CD** |コードパイプライン、コードビルド | Azure DevOps、GitHub アクション |クラウドビルド。クラウド展開 |
| **コンテナ レジストリ** | ECR | Azure コンテナー レジストリ |アーティファクトレジストリ |
| **GitOps** |アプリメッシュ + Flux/ArgoCD | AKS 上の Flux/ArgoCD |構成同期（Anthos） |
| **秘密管理** | Secrets Manager、SSM パラメータ ストア |キー コンテナー |シークレットマネージャー |
---

## 価格に関する考慮事項
|係数 | AWS |アズール | GCP |
|----------|-----|----------|-----|
| **請求の粒度** | 1 秒あたり (一部の場合は最初の 1 時間後) |毎秒 |毎秒 |
| **継続利用割引** |リザーブドインスタンス / Savings Plan |予約済み VM |確約利用割引 |
| **スポット インスタンス** |最大 90% オフ |最大 90% オフ |最大 91% オフ |
| **データ送信** |有料（高価）｜充電済み |目的地に関係なく同じ料金（安い場合が多い） |
| **無料利用枠** | 12 か月 + 常時無料 | 12 か月 + 200 ドルのクレジット | 90 日間 $300 + 常時無料 |
| **エンタープライズ割引** |エンタープライズ割引プログラム (EDP) | MACC (金銭コミットメント契約) |確約使用 + CUD |
---

## いつどれを使用するか
|シナリオ |おすすめ |なぜ |
|----------|---------------|-----|
| **最も幅広いサービスの選択;成熟したエコシステム** | AWS |最大のカタログ。ほとんどのサードパーティ統合 |
| **マイクロソフトエンタープライズ;アクティブディレクトリ。ハイブリッド** |アズール |ネイティブ AD 統合。強力なハイブリッドツーリング |
| **データウェアハウジング。 BigQuery;分析が多い** | GCP | BigQuery はクラス最高です。シームレスなデータ統合 |
| **Kubernetes ネイティブ開発** | GCP | GKE は最も洗練されたマネージド Kubernetes |
| **生成 AI / LLM アプリケーション** | Azure または GCP | GPT モデル用の Azure OpenAI。 Gemini 用 Vertex AI |
| **世界規模の低遅延アプリケーション** | GCP | Google のグローバル ネットワークは真の利点です |
| **政府/コンプライアンス重視のワークロード** | AWS または Azure |ほとんどのコンプライアンス認証。 GovCloud 地域 |
| **コスト重視のスタートアップ** | GCP または AWS | GCP の無料枠は寛大です。 AWS にはスタートアップ クレジットがあります |
| **既存の Microsoft / .NET スタック** |アズール | Visual Studio、.NET、Office 365 との緊密な統合 |
| **マルチクラウド戦略** | Terraform + 3 つすべて | Terraform を使用してクラウド全体のリソースを管理する |
---

＃＃ まとめ
3 つのクラウドはすべて、機能と信頼性が高く、継続的に拡張されています。通常、選択は、チームがすでに知っていること、既存の契約がどのようなものであるか、ワークロードにとってどの特定のサービスが重要であるかによって決まります。マルチクラウドはますます一般的になってきています。Terraform または Pulumi を使用してインフラストラクチャ層でのベンダー ロックインを回避し、それぞれのクラウドが最適な機能を発揮できるように選択してください。