# Teknoloji ve Bilişim

## Bilgisayar Nedir?

Bilgisayar, program adı verilen bir talimatlar kümesine göre verileri işleyen elektronik bir cihazdır. Modern bilgisayarlar; merkezi işlem birimi (CPU), bellek, depolama ve giriş/çıkış aygıtlarından oluşan von Neumann mimarisine dayanır. CPU talimatları yürütür. RAM (random access memory), bilgisayar çalışırken verileri geçici olarak depolar. SSD ve hard drive gibi depolama aygıtları ise verileri kalıcı olarak saklar.

## Programlama Dilleri

Programlama dili, bilgisayarlar için talimat yazmakta kullanılan biçimsel bir dildir. Python, basit sözdizimi ve okunabilirliğiyle bilinen, yüksek seviyeli, yorumlanan, genel amaçlı bir programlama dilidir. Veri bilimi, makine öğrenimi, web geliştirme ve otomasyonda yaygın olarak kullanılır. JavaScript, web geliştirme için temel dildir ve tarayıcılarda çalışır. Java, kurumsal yazılımlarda ve Android geliştirmede yaygın kullanılan, derlenen nesne yönelimli bir dildir. C ve C++, donanım üzerinde ayrıntılı denetim sağlayan daha düşük seviyeli dillerdir ve sistem programlama, oyun geliştirme ve performans açısından kritik uygulamalarda kullanılır. Rust, güvenlik ve performansa odaklanan modern bir sistem programlama dilidir.

## İnternet Nasıl Çalışır?

İnternet, standartlaştırılmış protokoller kullanarak iletişim kuran birbirine bağlı bilgisayarlardan oluşan küresel bir ağdır. World Wide Web, internet üzerinden tarayıcılarla erişilen web siteleri ve web sayfaları sistemidir. HTTP (HyperText Transfer Protocol) ve HTTPS (secure HTTP), web sayfalarını aktarmak için kullanılan protokollerdir. IP adresi, ağ üzerindeki her cihaza atanan benzersiz sayısal adrestir. DNS (Domain Name System), insanların okuyabildiği alan adlarını (örneğin google.com) IP adreslerine çevirir. Router, cihazlar ve ağlar arasındaki ağ trafiğini yönlendirir.

## Ağlar ve Protokoller

TCP/IP, internetin temel protokol takımıdır. IP (Internet Protocol), ağlar arasında paketlerin adreslenmesini ve yönlendirilmesini sağlar; TCP (Transmission Control Protocol) ise yeniden iletim ve akış denetimiyle güvenilir, sıralı teslimat sunar. UDP, garanti edilmiş teslimattan çok düşük gecikmenin önemli olduğu durumlarda kullanılan bağlantısız bir alternatiftir (örneğin streaming, gaming veya DNS sorgularında). HTTP, istemciler ve sunucular arasında istek/yanıt iletişimi için kullanılan durumsuz bir uygulama katmanı protokolüdür. HTTPS, TLS üzerinden çalışan HTTP'dir; şifreleme ve bütünlük koruması ekler. REST (Representational State Transfer), kaynakları, standart HTTP fiillerini (GET, POST, PUT, PATCH, DELETE) ve durumsuz etkileşimleri kullanan bir API mimari stilidir. WebSockets, istemci ile sunucunun gerçek zamanlı olarak mesaj gönderebilmesi için kalıcı, çift yönlü bağlantılar sağlar; bu da sohbet, canlı panolar ve ortak çalışmalı uygulamalar için yararlıdır.

## Yapay Zekâ

Yapay zekâ (AI), özellikle bilgisayar sistemleri tarafından insan zekâsının taklit edilmesidir. Makine öğrenimi, sistemlerin açıkça programlanmadan verilerden öğrenerek tahminlerde veya kararlarda bulunduğu AI alt alanıdır. Derin öğrenme, çok katmanlı sinir ağlarını kullanan makine öğrenimi alt alanıdır. Sinir ağları, biyolojik beyinlerin yapısından gevşek biçimde esinlenen hesaplama modelleridir. Büyük dil modelleri (LLMs), doğal dili üretmek ve anlamak için çok büyük miktarda metin üzerinde eğitilen AI modelleridir.

## Algoritmalar ve Veri Yapıları

Algoritma, bir problemi çözmek için adım adım izlenen bir prosedürdür. Veri yapıları, verilerin bir bilgisayarda verimli şekilde erişilip değiştirilebilmesi için düzenlenme biçimleridir. Yaygın veri yapıları arasında array'ler, linked list'ler, stack'ler, queue'lar, tree'ler, graph'lar ve hash table'lar bulunur. Sıralama algoritmaları öğeleri belirli bir düzene koyar; yaygın örnekler bubble sort, merge sort ve quicksort'tur. Binary search, arama aralığını tekrar tekrar yarıya bölerek sıralı bir listede öğe bulmak için kullanılan verimli bir algoritmadır.

## Veritabanları

Veritabanı, elektronik olarak depolanan yapılandırılmış verilerin düzenli bir koleksiyonudur. İlişkisel veritabanı, verileri satır ve sütunlardan oluşan tablolarda saklar. SQL (Structured Query Language), ilişkisel veritabanlarını yönetmek ve sorgulamak için kullanılan standart dildir. NoSQL veritabanları, verileri tablo ilişkileri dışındaki biçimlerde saklar; örneğin belge, anahtar-değer çifti veya graph yapıları gibi. Yaygın veritabanı sistemleri arasında PostgreSQL, MySQL, SQLite, MongoDB ve Redis bulunur. Veritabanındaki index, ek depolama maliyeti karşılığında veri erişimini hızlandırır.

## Sistem Tasarımının Temelleri

Sistem tasarımı, güvenilir, ölçeklenebilir ve bakımı yapılabilir yazılım sistemleri kurmaya odaklanır. Load balancing, erişilebilirliği artırmak ve gecikmeyi azaltmak için trafiği birden çok sunucuya dağıtır. Horizontal scaling daha fazla makine ekler; vertical scaling tek bir makineye daha fazla kaynak ekler. Caching, veritabanı yükünü ve yanıt süresini azaltmak için sık erişilen verileri hızlı depolamada (örneğin Redis, Memcached veya CDN edge cache'leri) tutar. Büyük ölçekte veritabanları çoğaltma, bölümleme (sharding), yedekleme stratejileri ve tutarlılık konusunda dikkatli ödünleşmeler gerektirir. Microservices, büyük uygulamaları bağımsız olarak dağıtılabilen daha küçük hizmetlere böler; monolith'ler ise mantığın çoğunu tek bir dağıtım biriminde tutar. Her iki yaklaşım da karmaşıklık, dağıtım hızı, hata ayıklama ve ekip özerkliği açısından ödünleşmeler içerir.

## İşletim Sistemleri

İşletim sistemi (OS), bilgisayar donanımını yöneten ve programlara hizmet sunan yazılımdır. Yaygın işletim sistemleri arasında Windows, macOS ve Linux bulunur. Linux, sunucularda, gömülü sistemlerde ve Android'de kullanılan açık kaynaklı bir OS çekirdeğidir. OS; süreçleri (çalışan programları), belleği, dosya sistemlerini ve giriş/çıkış aygıtlarını yönetir. Süreç, bir programın çalışan örneğidir. Thread, bir süreç içindeki en küçük yürütme birimidir.

## Sürüm Kontrolü

Sürüm kontrol sistemleri, kodda zaman içinde yapılan değişiklikleri izleyerek geliştiricilerin birlikte çalışmasına ve önceki durumlara dönmesine olanak tanır. Git en yaygın kullanılan sürüm kontrol sistemidir. Repository (repo), dosyaların ve geçmişlerinin koleksiyonudur. Commit, değişikliklerin kaydedilmiş bir anlık görüntüsüdür. Branch, bağımsız bir geliştirme hattıdır. Pull request, bir branch'teki değişiklikleri başka bir branch'e birleştirme önerisidir.

## Yazılım Geliştirme Uygulamaları

Nesne yönelimli programlama (OOP), kodu veri ile davranışı birleştiren nesneler hâlinde düzenler. OOP'nin temel ilkeleri arasında kapsülleme, kalıtım, çok biçimlilik ve soyutlama yer alır. Test güdümlü geliştirme (TDD), koddan önce test yazma pratiğidir. Agile, yinelemeli geliştirmeyi, iş birliğini ve uyarlanabilirliği vurgulayan bir yazılım geliştirme yöntemleri kümesidir. DevOps, geliştirme yaşam döngüsünü kısaltmak için yazılım geliştirme ile IT operasyonlarını birleştirir. API'ler (Application Programming Interfaces), farklı yazılım sistemlerinin birbiriyle iletişim kurmasını sağlar.

## Cloud ve DevOps Temelleri

Cloud computing, internet üzerinden isteğe bağlı altyapı ve yönetilen hizmetler sunar. Üç büyük public cloud sağlayıcısı AWS (Amazon Web Services), Microsoft Azure ve Google Cloud Platform'dur (GCP). Yaygın hizmet modelleri IaaS (infrastructure), PaaS (platform) ve SaaS'tır (software). Cloud'un temel yapı taşları arasında compute instance/container'lar, object storage, yönetilen veritabanları, networking ve IAM (Identity and Access Management) bulunur. CI/CD (Continuous Integration ve Continuous Delivery/Deployment), build, test ve release pipeline'larını otomatikleştirerek kodun commit'ten production'a güvenli biçimde taşınmasını sağlar. Docker, uygulamaları ve bağımlılıkları taşınabilir container'lara paketler; production ortamında bu container'lar genellikle Kubernetes gibi orchestrator'lar, serverless platformlar veya yönetilen container hizmetleri aracılığıyla dağıtılır.

## Veri Biçimleri ve Araçlar

JSON (JavaScript Object Notation), nesnelerden (anahtar/değer çiftleri), array'lerden, string'lerden, sayılardan, boolean değerlerden ve null'dan oluşan hafif bir metin biçimidir; API'lerde yaygın olarak kullanılır. YAML, iç içe yapıları ve yorumları destekleyen, insan dostu bir yapılandırma biçimidir; genellikle CI/CD ve altyapı tanımlarında kullanılır. CSV (Comma-Separated Values), tablo verilerini ayrılmış metin satırları olarak saklar ve veri içe/dışa aktarma pipeline'larında yaygındır. XML (eXtensible Markup Language), eski sistemlerde, yapılandırmada ve belge iş akışlarında kullanılan etiket tabanlı yapılandırılmış bir biçimdir. Geliştiriciler bu biçimleri sıklıkla linter'lar, şema doğrulayıcıları (örneğin JSON Schema), sorgu araçları (`jq`, XPath) ve kullandıkları programlama dilindeki ayrıştırma kütüphaneleriyle doğrular ve dönüştürür.

## Regular Expressions (Regex)

Regular expression, metni aramak, eşleştirmek, çıkarmak ve dönüştürmek için kullanılan bir desen dilidir. Regex'in temel kavramları arasında düz metin kalıpları (`cat`), karakter sınıfları (`[a-z]`, `\d`), niceleyiciler (`*`, `+`, `?`, `{n,m}`), ankrajlar (`^`, `$`), gruplar (`(...)`), alternation (`a|b`) ve özel karakterlerin escape edilmesi bulunur. Regex, girdi doğrulama, log ayrıştırma, metin çıkarma ve bul/değiştir otomasyonu için yoğun biçimde kullanılır. Farklı motorlar (PCRE, JavaScript, Python `re`, RE2) farklı özellik kümelerine sahiptir; bu nedenle davranış araçlar arasında değişebilir. Regex güçlüdür ancak okunması zor hâle gelebilir; karmaşık kalıplar hata oluşmaması için test edilmeli ve belgelenmelidir.

## Siber Güvenlik

Siber güvenlik, bilgisayar sistemlerini, ağları ve verileri dijital saldırılardan koruma uygulamasıdır. Yaygın tehditler arasında malware (kötü amaçlı yazılım), phishing (bilgi çalmak için tasarlanmış sahte iletişim), ransomware (verileri şifreleyip ödeme talep eden kötü amaçlı yazılım) ve denial-of-service saldırıları bulunur. Encryption, verileri yalnızca bir anahtarla çözülebilecek okunamaz bir biçime dönüştürür. HTTPS, web trafiğini şifrelemek için TLS (Transport Layer Security) kullanır. Güçlü ve benzersiz parolalar ile iki faktörlü kimlik doğrulama, temel güvenlik uygulamalarıdır.

## Geliştiriciler İçin Güvenlik Kavramları

OAuth 2.0, kullanıcıların kimlik bilgilerini doğrudan paylaşmadan bir uygulamaya sınırlı erişim vermesini sağlayan bir yetkilendirme çerçevesidir. OpenID Connect (OIDC), kimlik doğrulama için OAuth 2.0 üzerine kurulu bir kimlik katmanıdır. JWT (JSON Web Token), claim'ler içeren kompakt bir token biçimidir; çoğunlukla durumsuz auth için kullanılır, ancak doğru biçimde imzalanmalı ve sıkı şekilde doğrulanmalıdır (imza, son kullanma, issuer, audience). TLS, sertifikalar aracılığıyla şifreleme, bütünlük ve sunucu kimlik doğrulaması sağlayarak aktarım hâlindeki veriyi korur. OWASP Top 10, erişim kontrolü açıkları, kriptografik hatalar, injection, güvensiz tasarım, yanlış güvenlik yapılandırması, zafiyetli bileşenler ve yetersiz günlükleme/izleme dâhil olmak üzere yaygın web uygulaması güvenlik risklerinin geniş kabul gören bir listesidir. Güvenli geliştirme, katmanlı savunma gerektirir: girdi doğrulama, çıktı kodlama, en az ayrıcalık, secret yönetimi, bağımlılık yamalama ve düzenli güvenlik testi.
