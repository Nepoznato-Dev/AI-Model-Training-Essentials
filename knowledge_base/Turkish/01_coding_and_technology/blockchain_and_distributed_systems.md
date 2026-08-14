<!--
---
# Metadata
title: "Blockchain and Distributed Systems"
description: "Consensus, smart contracts, DeFi, Byzantine fault tolerance"
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
tags: [blockchain, distributed, systems, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Blockchain ve Dağıtık Sistemler
Blockchain, kayıtların (blokların) kriptografik hash'lerle bağlandığı, merkezi olmayan, yalnızca eklenen bir defter olan özel bir dağıtılmış sistem türüdür. Dağıtılmış sistemler, birden fazla bilgisayarın tek bir bilgisayar gibi birlikte çalışmasını sağlayan daha geniş bir alandır. Her iki kavram da, kripto para biriminden dağıtılmış veritabanlarına ve küresel hizmetleri destekleyen fikir birliği algoritmalarına kadar modern altyapıyı anlamak için önemlidir.
---

## Dağıtık Sistemlerin Temelleri
### Neden Dağıtık Sistemler?
| Motivasyon | Açıklama |
|-----------|----------------|
| **Ölçeklenebilirlik** | Daha fazla yükün üstesinden gelmek için daha fazla makine ekleyin |
| **Hata toleransı** | Bazı makineler arızalansa bile sistem çalışmaya devam ediyor |
| **Coğrafi dağılım** | Kullanıcılara yakındaki veri merkezlerinden hizmet verin |
| **Uzmanlık** | Farklı makineler farklı görevleri yerine getirir |
### Temel Kavramlar
| Konsept | Açıklama | Mücadelesi |
|-----------|---------------|-----------|
| **Uzlaşı** | Tüm düğümlerin bir değer üzerinde anlaşmasını sağlama | Ağ bölümleri; Bizans fayları |
| **Çoğaltma** | Verileri birden çok düğüme kopyalama | Tutarlılık ve kullanılabilirlik |
| **Bölümleme (parçalama)** | Verileri düğümler arasında bölme | Sıcak noktalar; parçalar arası sorgular |
| **Tutarlılık modelleri** | Farklı okuyucuların ne göreceğine dair garantiler | Güçlü tutarlılık yavaştır; nihai tutarlılık kullanıcıları şaşırtabilir |
| **CAP teoremi** | Şunlardan yalnızca 2 tanesine sahip olabilirsiniz: Tutarlılık, Kullanılabilirlik, Bölüm toleransı | Uygulamada bölme toleransı gereklidir; C veya A'yı seçin |
### CAP Teoremi
| Seçim | Ne Alırsınız | Nelerden Vazgeçiyorsun | Örnek |
|----------|----------------|------|-----------|
| **CP** | Tutarlı + bölümlemeye dayanıklı | Bölümleme sırasında bazı düğümler kullanılamayabilir | HBase, MongoDB, Redis |
| **AP** | Mevcut + bölüm toleranslı | Okumalar eski verileri döndürebilir | Cassandra, DynamoDB, CouchDB |
| **CA** | Tutarlı + mevcut | Ağ bölümlerine tolerans gösterilemiyor | Tek düğümlü veritabanları (gerçekten dağıtılmamış) |
---

## Konsensus Algoritmaları
Dağıtılmış düğümler sistemin durumu konusunda nasıl anlaşırlar?
| Algoritma | Tür | Hata Toleransı | Kullanılan |
|-----------|------|-----|--------|
| **Paxos** | Çarpışma hatasına dayanıklı | 2f+1 düğümlü f'ye kadar arıza | Google Tombul; temel teori |
| **Sal** | Çarpışma hatasına dayanıklı | 2f+1 düğümlü f'ye kadar arıza | vbd, Konsolos, TiKV |
| **PBFT** | Bizans hatasına dayanıklı | 3f+1 düğümlü f'ye kadar arıza | Hyperledger Kumaş |
| **İş Kanıtı** | Bizans hatasına dayanıklı | Hash gücüne bağlıdır | Bitcoin |
| **Shis Kanıtı** | Bizans hatasına dayanıklı | Bahis miktarına bağlıdır | Ethereum 2.0, Cardano |
### Sal (Basitleştirilmiş)
| Rol | Sorumluluk |
|------|---------------|
| **Lider** | Tüm müşteri isteklerini yönetir; takipçilere günlük girdileri gönderir |
| **Takipçi** | Liderin isteklerine yanıt verir; seçimlerdeki oylar |
| **Aday** | Lider olmak için oy istiyor |
1. Tüm düğümler takipçi olarak başlar
2. Bir takipçi, seçim zaman aşımı süresince liderden haber alamazsa aday olur
3. Adaylar oy ister; en çok oyu alan lider olur
4. Lider, günlük girişlerini takipçilere kopyalar
5. Çoğunluk onayladığında katılım kesinleşir
---

## Blockchain
### Bir Blockchain Nasıl Çalışır?
| Bileşen | Açıklama |
|-----------|----------------|
| **Engelle** | Bir grup işlem + meta veriler + önceki bloğun karması |
| **Hash** | Bloğun içeriğinin kriptografik parmak izi |
| **Zincir** | Her blok, önceki bloğun karmasına referans vererek değişmez bir zincir oluşturur |
| **Uzlaşı** | Ağ katılımcıları hangi blokların ekleneceği konusunda anlaşırlar |
| **Merkle ağacı** | Tüm işlemleri bir blokta özetleyen karma ağacı |
### Blockchain'i Kurcalamak Neden Zor?
1. Her blok bir önceki bloğun hash değerini içerir
2. Herhangi bir işlemin değiştirilmesi bloğun karmasını değiştirir
3. Değiştirilen karma, zinciri bozar — sonraki tüm bloklar geçersiz hale gelir
4. Saldırganın sonraki tüm blokları yeniden kazması VE ağın %50'sinden fazlasını kontrol etmesi gerekir
### Blockchain Türleri
| Tür | Erişim | Doğrulayıcı | Örnek |
|------|-----|-----------|-----|
| **Herkese açık (izinsiz)** | Herkes okuyabilir ve yazabilir | Açık fikir birliği (PoW, PoS) | Bitcoin, Ethereum |
| **Özel (izinli)** | Kısıtlı erişim | Bilinen doğrulayıcılar | Hyperledger, Corda |
| **Konsorsiyum** | Bir grup kuruluş tarafından yönetilmektedir | Seçilen doğrulayıcılar | Bankacılık için R3 Corda |
### Akıllı Sözleşmeler
Önceden belirlenmiş koşullar karşılandığında çalışan, blok zincirinde saklanan, kendi kendini çalıştıran kod.
| Platformu | Dil | Önemli Özellik |
|----------|----------|------|
| **Ethereum** | Sağlamlık, Vyper | En büyük akıllı sözleşme ekosistemi |
| **Solana** | Pas, C | Yüksek verim; düşük ücretler |
| **Cardano** | Haskell (Plutus) | Hakemli; resmi doğrulama |
| **Hiper Defter** | Git, Java, JavaScript | Girişim; izin verildi |
---

## Kripto para birimi
| Para Birimi | Konsensüs | Tedarik | Birincil Kullanım |
|----------|-----------|----------|------------|
| **Bitcoin** | Çalışma Kanıtı | 21 milyon (sınırlı) | Değer deposu; dijital altın |
| **Ethereum** | Hisse Kanıtı | Sert kapak yok | Akıllı sözleşmeler; DeFi; NFT'ler |
| **Solana** | Hisse Kanıtı + Geçmiş Kanıtı | Sert kapak yok | Yüksek hızlı işlemler |
| **Cardano** | Hisse Kanıtı (Ouroboros) | 45 milyar (sınırlı) | Akademik yaklaşım; sürdürülebilirlik |
---

## Dağıtılmış Veritabanları
| Veritabanı | Mimarlık | Tutarlılık | En İyisi |
|----------|----------------|---------------|----------|
| **Cassandra** | Geniş sütunlu; eşler arası | Ayarlanabilir (nihai çoğunluk) | Yüksek yazma verimi; zaman serisi |
| **MongoDB** | Belge; kopya setleri | Nihai (nedensel tutarlılık seçeneğiyle) | Esnek şema; hızlı gelişme |
| **HamamböceğiDB** | Dağıtılmış SQL; Raft fikir birliği | Güçlü | Dağıtılmış SQL; küresel dağıtım |
| **TiDB** | Dağıtılmış SQL; Sal (TiKV aracılığıyla) | Güçlü | MySQL uyumlu; yatay ölçeklendirme |
| **DinamoDB** | Anahtar/değer çifti; yönetilen | Nihai (veya tutarlı okumalarla güçlü) | Sunucusuz; AWS ile entegre |
| **Anahtar** | Dağıtılmış SQL; Paxos | Güçlü | Google Bulut; küresel tutarlılık |
---

## Dağıtılmış Sistem Modelleri
| Desen | Açıklama | Kullanım Örneği |
|-----------|---------------|----------|
| **Lider seçimi** | Koordine edilecek bir düğüm seçin | Sal lideri; Hayvanat Bahçesi Bekçisi |
| **Çoğaltma** | Artıklık için verileri kopyalayın ve ölçeklendirmeyi okuyun | Veritabanı kopyaları; CDN |
| **Parçalama** | Verileri anahtar aralığına veya karmaya göre bölümleme | Büyük ölçekli veritabanları |
| **Harita Azaltma** | Hesaplamayı düğümlere bölme; toplu sonuçlar | Büyük veri işleme |
| **Dedikodu protokolü** | Düğümler durumu düzenli olarak rastgele eşlerle paylaşır | Küme üyeliği; arıza tespiti |
| **İki aşamalı taahhüt** | Birden çok düğümdeki işlemleri koordine edin | Dağıtılmış veritabanları |
| **Destan deseni** | Telafi edici eylemler içeren bir dizi yerel işlem | Mikro hizmet işlemleri |
| **Devre kesici** | Başarısız bir hizmeti aramayı bırakın; hızlı başarısız ol | Dayanıklılık; ardışık arızaları önleyin |
---

## Dağıtık Sistemlerdeki Zorluklar
| Mücadelesi | Açıklama | Azaltma |
|-----------|----------------|------------|
| **Ağ bölümleri** | Düğümler iletişim kuramıyor | CAP takası; geri çekilme ile yeniden dene |
| **Saat çarpıklığı** | Farklı düğümlerin farklı saatleri vardır | Mantıksal saatler kullanın; NTP; duvar saatine güvenmekten kaçının |
| **Bizans fayları** | Yalan söyleyen veya keyfi davranan düğümler | BFT fikir birliği; blok zinciri |
| **Bölünmüş beyin** | İki düğümün ikisi de kendilerinin lider olduğunu düşünüyor | Eskrim; yeter sayıya dayalı kararlar |
| **Basamaklı arızalar** | Bir başarısızlık diğerlerini tetikler | Devre kesiciler; bölmeler; zarif bozulma |
| **Veri tutarlılığı** | Kopyaları senkronize tutmak | Tutarlılık modelleri; anlaşmazlık çözümü |
---

## Özet
Dağıtılmış sistemler, modern yazılımın ölçeklenmesi, arızalardan kurtulması ve kullanıcılara dünya çapında hizmet vermesidir. Konsensüs algoritmaları (Raft, Paxos) düğümlerin aynı fikirde olmasını sağlar. Blok zincirleri, güvenilmez defterler oluşturmak için kriptografik doğrulama ve merkezi olmayan yönetim sağlar. Dağıtılmış veritabanları (Cassandra, CockroachDB, DynamoDB) verileri uygun ölçekte işler. CAP teoreminin yakaladığı temel ödünleşim, ağ güvenilmez olduğunda tutarlılık ve kullanılabilirlik arasındadır. Bu kavramları anlamak, internet ölçeğinde çalışan sistemler oluşturmak için çok önemlidir.