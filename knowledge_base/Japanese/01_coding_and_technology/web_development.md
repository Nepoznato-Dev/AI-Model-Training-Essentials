<!--
---
# Metadata
title: "Web Development"
description: "Frontend, backend, DevOps, security"
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
tags: [web, development, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "13 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# ウェブ開発
## フロントエンド開発
### コアテクノロジー
#### HTML (ハイパーテキスト マークアップ言語)
- **セマンティック HTML**: 意味のあるタグの使用 (`<header>`、`<nav>`、`<main>`、`<article>`、`<section>`、`<aside>`、`<footer>`)
- **フォーム**: 入力タイプ、検証、アクセシビリティラベル
- **メディア**: 画像、ビデオ、オーディオの埋め込み
- **メタタグ**: SEO、ビューポート、文字エンコーディング
- **HTML5 の機能**: キャンバス、SVG、ローカル ストレージ、地理位置情報、Web ソケット
#### CSS (カスケード スタイル シート)
- **ボックス モデル**: コンテンツ、パディング、ボーダー、マージン
- **レイアウト システム**:
  - **フレックスボックス**: 1 次元レイアウト、コンテンツの位置揃え、項目の配置
  - **グリッド**: 2次元レイアウト、グリッドテンプレート、グリッドエリア
  - **位置決め**: 静的、相対、絶対、固定、スティッキー
- **レスポンシブ デザイン**: メディア クエリ、モバイル ファースト アプローチ
- **CSS 変数**: テーマのカスタム プロパティ
- **アニメーション**: トランジション、キーフレーム、トランスフォーム
- **プリプロセッサ**: Sass、Less (変数、ミックスイン、ネスト)
#### JavaScript
- **DOM 操作**: 要素の選択、作成、変更
- **イベント**: クリック、送信、キーボード、カスタム イベント、イベント委任
- **ES6+ 機能**: アロー関数、分割、スプレッド/レスト、モジュール、非同期/待機
- **API**: Fetch、XMLHttpRequest、localStorage、sessionStorage
- **TypeScript**: 静的型付け、インターフェイス、ジェネリックス、デコレーター
### 最新のフロントエンド フレームワーク
#### 反応する
- **コンポーネント**: 機能コンポーネント、クラスコンポーネント
- **フック**: useState、useEffect、useContext、useReducer、カスタム フック
- **状態管理**: コンテキスト API、Redux、Zustand、Recoil
- **ルーティング**: React Router (BrowserRouter、Routes、Route、Link)
- **エコシステム**: Next.js (SSR、SSG)、リミックス、ギャツビー
- **仮想 DOM**: 差分アルゴリズムによる効率的なレンダリング
#### Vue.js
- **オプション API**: データ、メソッド、計算、監視
- **Composition API**: setup()、ref、reactive、computed
- **ディレクティブ**: v-if、v-for、v-bind、v-on、v-model
- **Vuex/Pinia**: 状態管理
- **Vue Router**: クライアント側ルーティング
- **Nuxt.js**: サーバー側レンダリング フレームワーク
#### 角度
- **コンポーネント**: デコレーター、テンプレート、ライフサイクルフック
- **サービス**: 依存性注入、シングルトン パターン
- **RxJS**: リアクティブ プログラミング、オブザーバブル
- **ルーティング**: RouterModule、ガード、リゾルバー
- **フォーム**: テンプレート主導のリアクティブフォーム
- **NgRx**: Redux スタイルの状態管理
### ビルドツールとバンドラー
- **Webpack**: モジュールのバンドル、コード分割、ローダー、プラグイン
- **Vite**: ネイティブ ES モジュールを使用した高速ビルド ツール
- **Parcel**: ゼロ構成バンドラー
- **ロールアップ**: ライブラリ用に最適化
- **esbuild**: 非常に高速な JavaScript バンドラー
- **Babel**: 下位互換性のための JavaScript トランスパイラー
- **PostCSS**: プラグインによる CSS 処理
### CSS フレームワークとライブラリ
- **ブートストラップ**: コンポーネント ライブラリ、グリッド システム、ユーティリティ
- **Tailwind CSS**: ユーティリティファーストの CSS フレームワーク
- **マテリアル UI**: Google のマテリアル デザイン実装
- **Chakra UI**: アクセス可能なコンポーネント ライブラリ
- **Ant Design**: エンタープライズレベルの UI コンポーネント
- **スタイル付きコンポーネント**: CSS-in-JS ライブラリ
- **感情**: ソースマップを含む JS 内の CSS
## バックエンド開発
### サーバーサイド言語
#### Node.js
- **ランタイム**: サーバー上の JavaScript (V8 エンジン)
- **Express.js**: 最小限の Web フレームワーク、ミドルウェア アーキテクチャ
- **NestJS**: Angular にインスピレーションを得たアーキテクチャ、TypeScript
- **Fastify**: 高性能フレームワーク
- **Koa**: 同じクリエイターによるモダン エクスプレス
- **パッケージ管理**: npm、yarn、pnpm
#### パイソン
- **Django**: フル機能のフレームワーク、ORM、管理パネル、バッテリー付属
- **Flask**: マイクロフレームワーク、拡張機能エコシステム
- **FastAPI**: 最新の非同期自動 API ドキュメント
- **ピラミッド**: 柔軟でスケーラブルなフレームワーク
#### 他のバックエンド言語
- **Ruby on Rails**: 構成よりも規約、ActiveRecord ORM
- **Java Spring**: エンタープライズ フレームワーク、依存関係の注入
- **PHP Laravel**: エレガントな構文、雄弁な ORM、ブレード テンプレート
- **Go Gin**: 高パフォーマンス、最小限のフレームワーク
- **Rust Actix**: メモリの安全性、パフォーマンス
- **C# ASP.NET Core**: クロスプラットフォームのエンタープライズ機能
### データベースの統合
#### ORM (オブジェクト リレーショナル マッピング)
- **Sequelize**: SQL データベース用の Node.js ORM
- **Prisma**: タイプセーフなデータベース アクセス、自動生成されたクライアント
- **SQLAlchemy**: Python SQL ツールキットと ORM
- **ActiveRecord**: Ruby on Rails ORM
- **休止状態**: Java ORM
- **エンティティ フレームワーク**: .NET ORM
#### データベースドライバー
- **pg**: Node.js 用 PostgreSQL クライアント
- **mysql2**: Promise を備えた MySQL クライアント
- **pymongo**: Python 用 MongoDB ドライバー
- **redis**: 複数言語用の Redis クライアント
### API開発
#### REST API
- **HTTP メソッド**: GET、POST、PUT、PATCH、DELETE
- **ステータスコード**: 200、201、400、401、403、404、500
- **リソースの名前付け**: 名詞、複数形、階層構造
- **バージョン管理**: URL パス、ヘッダー、クエリ パラメータ
- **認証**: JWT、OAuth、API キー
- **ドキュメント**: OpenAPI/Swagger、Postman
#### グラフQL
- **スキーマ定義**: タイプ、クエリ、ミューテーション、サブスクリプション
- **リゾルバー**: フィールドレベルのデータ取得
- **Apollo Server**: GraphQL サーバーの実装
- **Relay**: Facebook の GraphQL クライアント
- **利点**: オーバーフェッチなし、単一エンドポイント、強力な型指定
#### gRPC
- **プロトコル バッファ**: インターフェイス定義言語
- **HTTP/2**: 双方向ストリーミング
- **ユースケース**: マイクロサービス通信、リアルタイム アプリケーション
### 認証と認可
- **セッションベース**: Cookie、サーバー側セッション
- **トークンベース**: JWT (JSON Web トークン)、ステートレス
- **OAuth 2.0**: 認証フレームワーク、サードパーティのログイン
- **OpenID Connect**: OAuth 2.0 の ID レイヤー
- **SAML**: エンタープライズ シングル サインオン
- **パスワードハッシュ**: bcrypt、argon2、scrypt
- **多要素認証**: TOTP、SMS、電子メール コード
## DevOps とデプロイメント
### バージョン管理
- **Git**: 分散バージョン管理
- **GitHub/GitLab/Bitbucket**: リポジトリ ホスティング
- **分岐戦略**: Git Flow、GitHub Flow、トランクベースの開発
- **CI/CD**: 自動化されたテストおよび展開パイプライン
### コンテナ化
- **Docker**: コンテナ ランタイム、Dockerfile、イメージ
- **Docker Compose**: マルチコンテナ オーケストレーション
- **コンテナ レジストリ**: Docker Hub、AWS ECR、Google GCR
- **ベスト プラクティス**: 複数段階のビルド、最小限の基本イメージ
### オーケストレーション
- **Kubernetes**: コンテナ オーケストレーション、ポッド、サービス、デプロイメント
- **Helm**: Kubernetes パッケージ マネージャー
- **サービス メッシュ**: マイクロサービス ネットワーキング用の Istio、Linkerd
### クラウドプラットフォーム
- **AWS**: EC2、S3、Lambda、RDS、CloudFront、ECS/EKS
- **Google Cloud**: Compute Engine、Cloud Storage、Cloud Functions、GKE
- **Azure**: 仮想マシン、BLOB ストレージ、関数、AKS
- **Vercel**: フロントエンド展開、サーバーレス機能
- **Netlify**: 静的サイトホスティング、サーバーレス機能
- **Heraku**: サービスとしてのプラットフォーム (PaaS)
- **DigitalOcean**: 簡素化されたクラウド インフラストラクチャ
### CI/CD パイプライン
- **GitHub アクション**: ワークフローの自動化
- **GitLab CI**: 組み込みの継続的インテグレーション
- **Jenkins**: 拡張可能なオートメーション サーバー
- **CircleCI**: クラウドベースの CI/CD
- **Travis CI**: 継続的インテグレーション サービス
- **ArgoCD**: Kubernetes 向けの GitOps 継続的デリバリー
### 監視とロギング
- **アプリケーションのパフォーマンス**: New Relic、Datadog、AppDynamics
- **エラー追跡**: セントリー、ロールバー、バグスナッグ
- **ロギング**: ELK スタック (Elasticsearch、Logstash、Kibana)、Splunk
- **稼働時間監視**: Pingdom、UptimeRobot
- **分析**: Google 分析、ミックスパネル、振幅
## ウェブパフォーマンス
### 最適化手法
- **コード分割**: 遅延読み込み、動的インポート
- **Tree Shaking**: 未使用のコードの削除
- **縮小**: ファイルサイズの縮小
- **圧縮**: Gzip、Brotli
- **キャッシュ**: ブラウザー キャッシュ、CDN、サービス ワーカー
- **画像の最適化**: WebP、AVIF、遅延読み込み、レスポンシブ画像
- **重要な CSS**: スクロールせずに見える範囲のスタイルをインライン化する
- **データベースの最適化**: インデックス作成、クエリの最適化、接続プーリング
### コア ウェブ バイタル
- **LCP (最大コンテンツフル ペイント)**: 読み込みパフォーマンス (<2.5 秒)
- **FID (最初の入力遅延)**: インタラクティブ性 (<100ms)
- **CLS (累積レイアウト シフト)**: 視覚的な安定性 (<0.1)
- **INP (次のペイントへのインタラクション)**: 応答性の指標
### コンテンツ配信ネットワーク (CDN)
- **Cloudflare**: セキュリティ、パフォーマンス、DNS
- **Akamai**: エンタープライズ CDN
- **Amazon CloudFront**: AWS CDN
- **高速**: エッジ クラウド プラットフォーム
- **StackPath**: エッジ サービス
## Webセキュリティ
### 一般的な脆弱性 (OWASP トップ 10)
- **インジェクション**: SQL インジェクション、コマンド インジェクション
- **認証の失敗**: セッションハイジャック、認証情報のスタッフィング
- **機密データの漏洩**: 暗号化されていないデータ、弱い暗号化
- **XML 外部エンティティ (XXE)**: XML パーサーの脆弱性
- **アクセス制御の違反**: 権限昇格、不正アクセス
- **セキュリティの構成ミス**: デフォルトの認証情報、詳細なエラー
- **クロスサイト スクリプティング (XSS)**: 反映、保存、DOM ベース
- **安全でない逆シリアル化**: オブジェクト インジェクション攻撃
- **既知の脆弱性のあるコンポーネントの使用**: 古い依存関係
- **不十分なロギングとモニタリング**: 検出されない侵害
### セキュリティのベストプラクティス
- **HTTPS**: TLS/SSL 暗号化、HSTS
- **コンテンツ セキュリティ ポリシー (CSP)**: XSS 攻撃を防止します。
- **入力検証**: ユーザー入力をサニタイズします。
- **出力エンコーディング**: インジェクション攻撃を防止します
- **CSRF 保護**: アンチ CSRF トークン、SameSite Cookie
- **レート制限**: ブルートフォース攻撃を防止します
- **セキュリティ ヘッダー**: X-Frame-Options、X-Content-Type-Options
- **依存関係スキャン**: npm Audit、Snyk、Dependabot
## テスト
### テストの種類
- **単体テスト**: 個々のコンポーネント/機能
- **統合テスト**: コンポーネントの相互作用
- **エンドツーエンド (E2E)**: 完全なユーザー ワークフロー
- **ビジュアル回帰**: UI 変更検出
- **パフォーマンス テスト**: 負荷、ストレス、スパイク テスト
- **アクセシビリティ テスト**: WCAG 準拠
### テストフレームワーク
- **Jest**: JavaScript テスト フレームワーク
- **Mocha**: 柔軟なテスト ランナー
- **pytest**: Python テスト フレームワーク
- **RSpec**: Ruby テスト フレームワーク
- **JUnit**: Java テスト フレームワーク
### E2E テストツール
- **Selenium**: ブラウザ自動化
- **Cypress**: 最新の E2E テスト
- **Playwright**: クロスブラウザーの自動化
- **Puppeteer**: ヘッドレス Chrome コントロール
## アクセシビリティ (a11y)
### WCAG ガイドライン
- **認識可能**: 代替テキスト、キャプション、適応可能なコンテンツ
- **操作可能**: キーボード ナビゲーション、十分な時間、発作なし
- **理解可能**: 読みやすく、予測可能な、入力支援
- **堅牢**: 支援技術と互換性があります
### 実装
- **セマンティック HTML**: 適切な見出し階層、ランドマーク
- **ARIA 属性**: 役割、状態、プロパティ
- **フォーカス管理**: 目に見えるフォーカスインジケーター、論理的なタブオーダー
- **カラーコントラスト**: テキストの比率は最小 4.5:1
- **スクリーン リーダーのテスト**: NVDA、JAWS、VoiceOver
- **キーボード ナビゲーション**: すべてのインタラクティブ要素にアクセス可能
## プログレッシブ ウェブ アプリ (PWA)
### PWA の機能
- **Service Worker**: オフライン機能、バックグラウンド同期
- **Web アプリ マニフェスト**: プロンプト、アイコン、テーマの色をインストールします。
- **App Shell**: キャッシュされた UI スケルトン
- **プッシュ通知**: ユーザーエンゲージメント
- **レスポンシブデザイン**: すべてのデバイスで動作します
- **HTTPS が必要**: 安全なコンテキスト
### ツール
- **ワークボックス**: Service Worker ライブラリ
- **Lighthouse**: PWA 監査
- **PWA Builder**: マニフェストとアイコンを生成します
## 新興テクノロジー
### WebAssembly (Wasm)
- **目的**: コンパイルされたコードをブラウザーでネイティブに近い速度で実行します。
- **言語**: C++、Rust、Go コンパイル ターゲット
- **ユースケース**: ゲーム、ビデオ編集、暗号化、ML 推論
### サーバーレスアーキテクチャ
- **Functions as a Service**: AWS Lambda、Azure Functions、Google Cloud Functions
- **利点**: サーバー管理不要、自動スケーリング、従量課金制
- **考慮事項**: コールド スタート、ベンダー ロックイン、デバッグの複雑さ
### ジャムスタックのアーキテクチャ
- **JavaScript**: クライアント側の対話性
- **API**: サーバーレス機能、サードパーティのサービス
- **マークアップ**: 事前に構築された静的ファイル
- **ツール**: Next.js、Gatsby、Hugo、イレブンティ
- **メリット**: パフォーマンス、セキュリティ、スケーラビリティ、開発者エクスペリエンス
### リアルタイム通信
- **WebSocket**: 双方向通信
- **サーバー送信イベント**: サーバーからクライアントへのストリーミング
- **WebRTC**: ピアツーピアのビデオ、オーディオ、データ
- **使用例**: チャット、コラボレーション、ライブ ストリーミング、ゲーム
### マイクロフロントエンド
- **コンセプト**: マイクロサービスをフロントエンドに拡張する
- **アプローチ**: ビルド時、実行時、エッジサイドの統合
- **利点**: 独立した導入、チームの自律性
- **課題**: 一貫性、パフォーマンス、複雑さ