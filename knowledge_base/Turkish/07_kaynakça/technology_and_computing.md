# Teknoloji ve Bilişim

## Bilgisayar Nedir?

Bilgisayar, program adı verilen bir dizi talimata göre veriyi işleyen elektronik bir cihazdır. Modern bilgisayarlar; merkezi işlem birimi (CPU), bellek, depolama ve giriş/çıkış aygıtlarından oluşan von Neumann mimarisine dayanır. CPU talimatları yürütür. RAM (rastgele erişimli bellek), bilgisayar çalışırken verileri geçici olarak saklar. SSD'ler ve sabit diskler gibi depolama aygıtları verileri kalıcı olarak saklar.

## Programlama Dilleri

Programlama dili, bilgisayarlar için talimat yazmakta kullanılan biçimsel bir dildir. Python, basit sözdizimi ve okunabilirliğiyle bilinen üst düzey, yorumlanan, genel amaçlı bir programlama dilidir. Veri bilimi, makine öğrenmesi, web geliştirme ve otomasyonda yaygın olarak kullanılır. JavaScript, web geliştirmenin temel dilidir ve tarayıcılarda çalışır. Java, kurumsal yazılımlarda ve Android geliştirmede yaygın kullanılan derlenen, nesne yönelimli bir dildir. C ve C++, donanım üzerinde ayrıntılı denetim sağlayan daha düşük seviyeli dillerdir; sistem programlama, oyun geliştirme ve performans açısından kritik uygulamalarda kullanılır. Rust, güvenlik ve performansa odaklanan modern bir sistem programlama dilidir.

## İnternet Nasıl Çalışır?

İnternet, standartlaştırılmış protokoller kullanarak iletişim kuran birbirine bağlı bilgisayarların küresel ağıdır. World Wide Web, tarayıcılar aracılığıyla internet üzerinden erişilen web siteleri ve web sayfalarından oluşan bir sistemdir. HTTP (HyperText Transfer Protocol) ve HTTPS (güvenli HTTP), web sayfalarını aktarmak için kullanılan protokollerdir. IP adresi, bir ağdaki her cihaza atanan benzersiz sayısal adrestir. DNS (Domain Name System), google.com gibi insan tarafından okunabilir alan adlarını IP adreslerine çevirir. Router, ağ trafiğini cihazlar ve ağlar arasında yönlendirir.

## Ağlar ve Protokoller

TCP/IP, internetin temel protokol paketidir. IP (Internet Protocol), ağlar arasında paketlerin adreslenmesini ve yönlendirilmesini yönetirken TCP (Transmission Control Protocol), yeniden iletim ve akış kontrolüyle güvenilir, sıralı teslimat sağlar. UDP, garantili teslimattan çok düşük gecikmenin önemli olduğu durumlarda kullanılan bağlantısız bir alternatiftir (örneğin akış, oyun veya DNS sorgularında). HTTP, istemciler ile sunucular arasında istek/yanıt iletişimi için durum tutmayan bir uygulama katmanı protokolüdür. HTTPS, TLS üzerinden çalışan HTTP'dir ve şifreleme ile bütünlük koruması ekler. REST (Representational State Transfer), kaynakları, standart HTTP fiillerini (GET, POST, PUT, PATCH, DELETE) ve durum tutmayan etkileşimleri kullanan bir API mimari tarzıdır. WebSockets, istemci ve sunucunun gerçek zamanlı olarak mesaj gönderebilmesi için kalıcı, tam çift yönlü bağlantılar sağlar; bu, sohbet, canlı panolar ve ortak çalışma uygulamaları için yararlıdır.

## Yapay Zekâ

Yapay zekâ (AI), özellikle bilgisayar sistemleri olmak üzere makineler tarafından insan zekâsının benzetimidir. Makine öğrenmesi, sistemlerin açıkça programlanmadan veri üzerinden öğrenerek tahminler veya kararlar aldığı AI'ın bir alt alanıdır. Derin öğrenme, çok katmanlı sinir ağlarını kullanan makine öğrenmesinin bir alt alanıdır. Sinir ağları, biyolojik beyinlerin yapısından genel olarak esinlenen hesaplamalı modellerdir. Büyük dil modelleri (LLM'ler), doğal dili üretmek ve anlamak için çok büyük miktarda metin üzerinde eğitilen AI modelleridir.

## Algoritmalar ve Veri Yapıları

Algoritma, bir problemi çözmek için izlenen adım adım prosedürdür. Veri yapıları, verilerin bilgisayarda verimli biçimde erişilebilmesi ve değiştirilebilmesi için düzenlenme yollarıdır. Yaygın veri yapıları arasında diziler, bağlı listeler, yığınlar, kuyruklar, ağaçlar, graflar ve hash tabloları bulunur. Sıralama algoritmaları öğeleri belirli bir düzende sıralar; yaygın örnekler bubble sort, merge sort ve quicksort'tur. Binary search, sıralı bir listede arama aralığını tekrar tekrar ikiye bölerek öğe bulmaya yarayan verimli bir algoritmadır.

## Veritabanları

Veritabanı, elektronik olarak depolanan düzenli bir yapılandırılmış veri koleksiyonudur. İlişkisel veritabanı, verileri satır ve sütunlardan oluşan tablolarda saklar. SQL (Structured Query Language), ilişkisel veritabanlarını yönetmek ve sorgulamak için standart dildir. NoSQL veritabanları, verileri tablo ilişkileri dışında; belgeler, anahtar-değer çiftleri veya graflar gibi biçimlerde saklar. Yaygın veritabanı sistemleri arasında PostgreSQL, MySQL, SQLite, MongoDB ve Redis bulunur. Veritabanındaki bir indeks, ek depolama maliyeti karşılığında veri getirmeyi hızlandırır.

## Sistem Tasarımının Temelleri

Sistem tasarımı; güvenilir, ölçeklenebilir ve sürdürülebilir yazılım sistemleri oluşturmaya odaklanır. Yük dengeleme, kullanılabilirliği artırmak ve gecikmeyi azaltmak için trafiği birden fazla sunucuya dağıtır. Yatay ölçeklendirme daha fazla makine ekler; dikey ölçeklendirme ise tek bir makineye daha fazla kaynak ekler. Önbellekleme, veritabanı yükünü ve yanıt süresini azaltmak için sık erişilen verileri hızlı depolamada (örneğin Redis, Memcached veya CDN uç önbellekleri) tutar. Büyük ölçekte veritabanları çoğaltma, bölümlendirme (sharding), yedekleme stratejileri ve dikkatli tutarlılık ödünleşimleri gerektirir. Mikroservisler büyük uygulamaları bağımsız olarak dağıtılabilen daha küçük hizmetlere ayırırken monolitler çoğu mantığı tek bir dağıtılabilir birimde tutar; her iki yaklaşım da karmaşıklık, dağıtım hızı, hata ayıklama ve ekip özerkliği açısından ödünleşimler içerir.

## İşletim Sistemleri

İşletim sistemi (OS), bilgisayar donanımını yöneten ve programlar için hizmetler sağlayan yazılımdır. Yaygın işletim sistemleri arasında Windows, macOS ve Linux bulunur. Linux, sunucularda, gömülü sistemlerde ve Android'de kullanılan açık kaynaklı bir OS çekirdeğidir. OS; süreçleri (çalışan programları), belleği, dosya sistemlerini ve giriş/çıkış aygıtlarını yönetir. Süreç, bir programın çalışan örneğidir. İş parçacığı, bir süreç içindeki en küçük yürütme birimidir.

## Sürüm Kontrolü

Sürüm kontrol sistemleri, kodda zaman içinde yapılan değişiklikleri izleyerek geliştiricilerin iş birliği yapmasını ve önceki durumlara geri dönmesini sağlar. Git en yaygın kullanılan sürüm kontrol sistemidir. Depo (repo), dosyaların ve geçmişlerinin koleksiyonudur. Commit, değişikliklerin kaydedilmiş bir anlık görüntüsüdür. Branch, bağımsız bir geliştirme hattıdır. Pull request, değişiklikleri bir branch'ten başka bir branch'e birleştirme önerisidir.

## Yazılım Geliştirme Uygulamaları

Nesne yönelimli programlama (OOP), kodu veri ve davranışı birleştiren nesneler hâlinde düzenler. OOP'nin temel ilkeleri kapsülleme, kalıtım, çok biçimlilik ve soyutlamadır. Test güdümlü geliştirme (TDD), kod yazmadan önce test yazma uygulamasıdır. Agile; yinelemeli geliştirmeyi, iş birliğini ve uyarlanabilirliği vurgulayan bir yazılım geliştirme yöntemleri kümesidir. DevOps, geliştirme yaşam döngüsünü kısaltmak için yazılım geliştirme ile IT operasyonlarını birleştirir. API'ler (Application Programming Interfaces), farklı yazılım sistemlerinin birbirleriyle iletişim kurmasını sağlar.

## Cloud ve DevOps Temelleri

Bulut bilişim, internet üzerinden talep üzerine altyapı ve yönetilen hizmetler sağlar. Üç büyük genel bulut sağlayıcısı AWS (Amazon Web Services), Microsoft Azure ve Google Cloud Platform'dur (GCP). Yaygın hizmet modelleri IaaS (altyapı), PaaS (platform) ve SaaS'tır (yazılım). Temel bulut yapı taşları arasında işlem örnekleri/konteynerler, nesne depolama, yönetilen veritabanları, ağ ve IAM (Identity and Access Management) bulunur. CI/CD (Continuous Integration and Continuous Delivery/Deployment), kodun commit'ten üretime güvenli biçimde ilerleyebilmesi için derleme, test ve yayın hatlarını otomatikleştirir. Docker, uygulamaları ve bağımlılıkları taşınabilir konteynerler hâlinde paketler; üretimde bu konteynerler genellikle orkestratörler (Kubernetes gibi), serverless platformlar veya yönetilen konteyner hizmetleri aracılığıyla dağıtılır.

## Veri Biçimleri ve Araçlar

JSON (JavaScript Object Notation), nesnelerden (anahtar/değer çiftleri), dizilerden, string'lerden, sayılardan, boolean değerlerden ve null'dan oluşan hafif bir metin biçimidir; API'lerde yaygın olarak kullanılır. YAML, iç içe yapıları ve yorumları destekleyen, CI/CD ve altyapı tanımlarında yaygın kullanılan insan dostu bir yapılandırma biçimidir. CSV (Comma-Separated Values), tablo verilerini sınırlayıcılarla ayrılmış metin satırları olarak saklar ve veri içe/dışa aktarma hatlarında yaygındır. XML (eXtensible Markup Language), eski sistemlerde, yapılandırmada ve belge iş akışlarında kullanılan etiket tabanlı yapılandırılmış bir biçimdir. Geliştiriciler bu biçimleri genellikle linter'lar, şema doğrulayıcılar (JSON Schema gibi), sorgu araçları (`jq`, XPath) ve kendi programlama dillerindeki ayrıştırma kütüphaneleriyle doğrular ve dönüştürür.

## Düzenli İfadeler (Regex)

Düzenli ifade, metni aramak, eşleştirmek, ayıklamak ve dönüştürmek için kullanılan bir örüntü dilidir. Temel regex kavramları arasında sabit dizgeler (`cat`), karakter sınıfları (`[a-z]`, `\d`), niceleyiciler (`*`, `+`, `?`, `{n,m}`), çapa işaretleri (`^`, `$`), gruplar (`(...)`), alternatifleme (`a|b`) ve özel karakterleri kaçışlama bulunur. Regex; giriş doğrulama, günlük ayrıştırma, metin çıkarma ve bul/değiştir otomasyonunda yoğun biçimde kullanılır. Farklı motorların (PCRE, JavaScript, Python `re`, RE2) farklı özellik kümeleri vardır; bu nedenle davranış araçlar arasında değişebilir. Regex güçlüdür ancak okunması zor hâle gelebilir; karmaşık örüntüler hatalardan kaçınmak için test edilmeli ve belgelenmelidir.

## Siber Güvenlik

Siber güvenlik, bilgisayar sistemlerini, ağları ve verileri dijital saldırılardan koruma uygulamasıdır. Yaygın tehditler arasında malware (kötü amaçlı yazılım), phishing (bilgi çalmak için tasarlanmış sahte iletişim), ransomware (verileri şifreleyip ödeme talep eden kötü amaçlı yazılım) ve denial-of-service saldırıları bulunur. Şifreleme, veriyi yalnızca bir anahtarla çözülebilecek okunamaz bir biçime dönüştürür. HTTPS, web trafiğini şifrelemek için TLS (Transport Layer Security) kullanır. Güçlü, benzersiz parolalar ve iki faktörlü kimlik doğrulama temel güvenlik uygulamalarıdır.

## Geliştiriciler İçin Güvenlik Kavramları

OAuth 2.0, kullanıcıların kimlik bilgilerini doğrudan paylaşmadan bir uygulamaya sınırlı erişim vermesini sağlayan bir yetkilendirme çerçevesidir. OpenID Connect (OIDC), kimlik doğrulama için OAuth 2.0 üzerine kurulmuş bir kimlik katmanıdır. JWT (JSON Web Token), iddialar içeren kompakt bir token biçimidir; çoğunlukla durum tutmayan kimlik doğrulama için kullanılır, ancak doğru şekilde imzalanmalı ve sıkı biçimde doğrulanmalıdır (imza, süre sonu, yayıncı, hedef kitle). TLS, sertifikalar aracılığıyla şifreleme, bütünlük ve sunucu kimlik doğrulaması sağlayarak aktarım hâlindeki verileri güvence altına alır. OWASP Top 10; bozuk erişim kontrolü, kriptografik hatalar, injection, güvensiz tasarım, güvenlik yanlış yapılandırması, savunmasız bileşenler ve yetersiz günlükleme/izleme dâhil yaygın web uygulaması güvenlik risklerinin çok kullanılan bir listesidir. Güvenli geliştirme derinlemesine savunma gerektirir: giriş doğrulama, çıktı kodlama, en az ayrıcalık, sır yönetimi, bağımlılık yamalama ve düzenli güvenlik testleri.
