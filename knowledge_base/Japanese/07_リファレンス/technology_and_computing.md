<!-- 
This file was automatically translated from English to Japanese.
Source: technology_and_computing.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# テクノロジーとコンピューティング

## コンピュータとは何か

コンピュータは、プログラムと呼ばれる一連の命令に従ってデータを処理する電子機器です。現代のコンピュータは、中央処理装置（CPU）、メモリ、ストレージ、入出力装置から成る von Neumann アーキテクチャを基盤としています。CPU は命令を実行し、RAM（random access memory）は動作中のデータを一時的に保持します。SSD やハードドライブなどのストレージ装置は、データを永続的に保存します。

## プログラミング言語

プログラミング言語は、コンピュータに与える命令を書くための形式言語です。Python は高水準のインタプリタ型汎用言語で、簡潔な構文と高い可読性で知られています。データサイエンス、機械学習、ウェブ開発、自動化で広く使われています。JavaScript はウェブ開発の主要言語であり、ブラウザ上で動作します。Java はコンパイル型のオブジェクト指向言語で、エンタープライズソフトウェアや Android 開発で多用されます。C と C++ はより低レベルで、ハードウェアを細かく制御できるため、システムプログラミング、ゲーム開発、高性能アプリケーションに使われます。Rust は安全性と性能を重視した現代的なシステムプログラミング言語です。

## インターネットの仕組み

インターネットは、標準化されたプロトコルで通信する相互接続されたコンピュータの世界的ネットワークです。World Wide Web は、ブラウザを介してインターネット上でアクセスされるウェブサイトやウェブページの仕組みです。HTTP（HyperText Transfer Protocol）と HTTPS（secure HTTP）は、ウェブページの転送に使われるプロトコルです。IP address は各機器に割り当てられた固有の数値アドレスで、DNS（Domain Name System）は google.com のような人間に読みやすいドメイン名を IP address に変換します。router は機器やネットワーク間の通信を振り分けます。

## ネットワーキングとプロトコル

TCP/IP はインターネットの基盤となるプロトコル群です。IP（Internet Protocol）はアドレス指定と経路制御を担当し、TCP（Transmission Control Protocol）は信頼性のある順序付き配送、再送制御、フロー制御を提供します。UDP は接続レスの代替手段で、保証された配送より低遅延を優先したい場合に使われます（たとえば streaming、gaming、DNS query など）。HTTP は request/response 形式のための stateless な application-layer protocol です。HTTPS は TLS 上で動く HTTP であり、暗号化と完全性保護を追加します。REST（Representational State Transfer）は、resource、標準的な HTTP verbs（GET、POST、PUT、PATCH、DELETE）、stateless なやり取りを用いる API アーキテクチャスタイルです。WebSocket は永続的な双方向接続を提供し、chat、リアルタイムダッシュボード、共同編集アプリに向いています。

## 人工知能

人工知能（AI）は、機械、特にコンピュータシステムによって人間の知能を模倣する技術です。機械学習は AI の一分野で、システムが明示的にプログラムされなくてもデータから予測や意思決定を学びます。深層学習は機械学習の一分野で、多層のニューラルネットワークを利用します。ニューラルネットワークは生物の脳構造に着想を得た計算モデルです。Large Language Models（LLMs）は、膨大なテキストで学習し、自然言語を理解・生成する AI モデルです。

## アルゴリズムとデータ構造

アルゴリズムは問題を解くための手順です。データ構造は、データを効率よく参照・更新できるようコンピュータ内で整理する方法です。代表的なデータ構造には、array、linked list、stack、queue、tree、graph、hash table があります。sorting algorithm は要素を一定の順序に並べる手法で、bubble sort、merge sort、quicksort などがよく知られています。binary search は、整列済みリストに対して探索範囲を半分ずつ絞り込みながら要素を見つける効率的な探索法です。

## データベース

データベースは、電子的に保存された構造化データの組織的な集合です。relational database は行と列から成る table でデータを保持します。SQL（Structured Query Language）は、relational database を管理・照会する標準言語です。NoSQL database は、document、key-value、graph など、表形式以外の形式でデータを保存します。よく使われるデータベースシステムには PostgreSQL、MySQL、SQLite、MongoDB、Redis があります。データベースの index は、追加の記憶領域と引き換えに検索速度を高めます。

## システム設計の基礎

システム設計は、信頼性が高く、拡張しやすく、保守しやすいソフトウェアシステムを構築するための考え方です。load balancing は複数サーバーにトラフィックを分散し、可用性向上と遅延低減に役立ちます。horizontal scaling はマシン台数を増やすことで、vertical scaling は 1 台の資源を増やすことで拡張します。caching は、よく使うデータを高速な記憶領域（Redis、Memcached、CDN edge cache など）に保存し、データベース負荷と応答時間を減らします。大規模データベースでは、replication、partitioning（sharding）、backup 戦略、一貫性のトレードオフを慎重に扱う必要があります。microservices は大きなアプリケーションを独立デプロイ可能な小さなサービスに分割し、monolith は大部分のロジックを 1 つの単位にまとめます。どちらにも、複雑さ、デプロイ速度、デバッグ、チーム自律性の面でトレードオフがあります。

## オペレーティングシステム

オペレーティングシステム（OS）は、コンピュータのハードウェアを管理し、プログラムにサービスを提供するソフトウェアです。代表的な OS には Windows、macOS、Linux があります。Linux はオープンソースの OS kernel で、サーバー、組み込みシステム、Android などで広く使われています。OS は process（実行中のプログラム）、memory、file system、入出力装置を管理します。process はプログラムの実行中インスタンスであり、thread はその中での最小実行単位です。

## バージョン管理

バージョン管理システムは、コードの変更履歴を追跡し、共同作業や過去状態への巻き戻しを可能にします。Git はもっとも広く使われているバージョン管理システムです。repository（repo）はファイルとその履歴の集合です。commit は変更の保存されたスナップショット、branch は独立した開発ライン、pull request はある branch の変更を別の branch に統合する提案です。

## ソフトウェア開発プラクティス

Object-oriented programming（OOP）は、データと振る舞いをまとめた object を中心にコードを構成する考え方です。OOP の主要原則には encapsulation、inheritance、polymorphism、abstraction があります。test-driven development（TDD）は、実装前にテストを書く実践です。Agile は、反復的な開発、協調、適応性を重視するソフトウェア開発手法の総称です。DevOps はソフトウェア開発と IT 運用を結びつけ、開発ライフサイクルを短縮します。API（Application Programming Interface）は、異なるソフトウェアシステム同士が通信するための仕組みです。

## クラウドと DevOps の基礎

cloud computing は、インターネット経由でオンデマンドにインフラやマネージドサービスを提供します。主要な public cloud provider は AWS（Amazon Web Services）、Microsoft Azure、Google Cloud Platform（GCP）です。代表的なサービスモデルは IaaS、PaaS、SaaS です。クラウドの基本要素には、compute instance / container、object storage、managed database、networking、IAM（Identity and Access Management）があります。CI/CD（Continuous Integration と Continuous Delivery / Deployment）は、build、test、release のパイプラインを自動化し、commit から production まで安全にコードを届けられるようにします。Docker はアプリケーションと依存関係を可搬な container にまとめる技術で、本番環境では Kubernetes のような orchestrator、serverless platform、managed container service 上で動かすことが一般的です。

## データ形式とツール

JSON（JavaScript Object Notation）は、object、array、string、number、boolean、null から成る軽量なテキスト形式で、API で広く使われます。YAML は人が読みやすい設定形式で、入れ子構造やコメントを扱え、CI/CD やインフラ定義でよく使われます。CSV（Comma-Separated Values）は表形式データを区切り文字付きテキストとして表現する形式で、データの入出力で一般的です。XML（eXtensible Markup Language）はタグベースの構造化形式で、レガシーシステム、設定、文書ワークフローで使われます。開発者は、linters、schema validator（JSON Schema など）、query tool（`jq`、XPath など）、各言語の parsing library を使って、これらの形式を検証・変換します。

## 正規表現（Regex）

正規表現は、テキストを検索、照合、抽出、変換するためのパターン言語です。基本概念には、literal（`cat`）、character class（`[a-z]`、`\d`）、quantifier（`*`、`+`、`?`、`{n,m}`）、anchor（`^`、`$`）、group（`(...)`）、alternation（`a|b`）、特殊文字のエスケープがあります。Regex は、入力検証、ログ解析、テキスト抽出、検索置換の自動化で多用されます。engine ごとに機能差があり、PCRE、JavaScript、Python `re`、RE2 などで挙動が異なる場合があります。強力な一方で読みづらくなりやすいため、複雑なパターンは十分にテストし、必要なら説明を残すべきです。

## サイバーセキュリティ

cybersecurity は、コンピュータシステム、ネットワーク、データをデジタル攻撃から守る実践です。代表的な脅威には、malware、phishing、ransomware、denial-of-service attack があります。encryption はデータを読み取れない形に変換し、鍵を持つ者だけが復号できるようにします。HTTPS は TLS（Transport Layer Security）によってウェブ通信を暗号化します。強力で固有のパスワードと二要素認証は、基本かつ重要なセキュリティ対策です。

## 開発者向けセキュリティ概念

OAuth 2.0 は、認証情報を直接共有せずに、利用者がアプリケーションへ限定的な権限を委譲できる認可フレームワークです。OpenID Connect（OIDC）は OAuth 2.0 上に構築された認証のための identity layer です。JWT（JSON Web Token）は claim を含むコンパクトな token 形式で、stateless auth によく使われますが、署名、期限、issuer、audience を厳密に検証する必要があります。TLS は暗号化、完全性、証明書によるサーバー認証によって、転送中データを保護します。OWASP Top 10 は、broken access control、cryptographic failure、injection、insecure design、security misconfiguration、脆弱な component、不十分な logging / monitoring など、一般的なウェブアプリケーションのリスクをまとめた広く使われる一覧です。安全な開発には defense-in-depth が必要であり、input validation、output encoding、least privilege、secret management、dependency patching、定期的な security testing が重要です。
