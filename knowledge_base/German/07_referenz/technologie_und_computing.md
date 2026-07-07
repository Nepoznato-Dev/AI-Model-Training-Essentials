<!-- 
Diese Datei wurde automatisch aus dem Englischen ins Deutsche übersetzt.
Quelle: technology_and_computing.md
Hinweis: Technische Begriffe, Codebeispiele und Eigennamen können auf Englisch bleiben.
Für Verbesserungen der Genauigkeit bitten wir um Beiträge via Pull Requests.
-->

# Technologie und Datenverarbeitung

## Was ist ein Computer?

Ein Computer ist ein elektronisches Gerät, das Daten gemäß einem Satz von Anweisungen verarbeitet, die als Programm bezeichnet werden. Moderne Computer basieren auf der Von-Neumann-Architektur, die aus einer Zentraleinheit (CPU), Speicher, Massenspeicher und Eingabe-/Ausgabegeräten besteht. Die CPU führt Anweisungen aus. RAM (Random Access Memory) speichert Daten temporär, während der Computer läuft. Speichergeräte wie SSDs und Festplatten speichern Daten dauerhaft.

## Programmiersprachen

Eine Programmiersprache ist eine formale Sprache, die verwendet wird, um Anweisungen für Computer zu schreiben. Python ist eine hochlevelige, interpretierte Allzweck-Programmiersprache, die für ihre einfache Syntax und Lesbarkeit bekannt ist. Sie wird häufig in der Datenwissenschaft, im maschinellen Lernen, in der Webentwicklung und zur Automatisierung eingesetzt. JavaScript ist die primäre Sprache für die Webentwicklung und läuft in Browsern. Java ist eine kompilierte, objektorientierte Sprache, die weit verbreitet in Unternehmenssoftware und der Android-Entwicklung eingesetzt wird. C und C++ sind niedrigere Sprachen, die eine feinkörnige Kontrolle über die Hardware bieten und in der Systemprogrammierung, Spieleentwicklung und leistungskritischen Anwendungen verwendet werden. Rust ist eine moderne Systemprogrammiersprache mit Fokus auf Sicherheit und Leistung.

## Wie das Internet funktioniert

Das Internet ist ein globales Netzwerk von miteinander verbundenen Computern, die unter Verwendung standardisierter Protokolle kommunizieren. Das World Wide Web ist ein System von Websites und Webseiten, auf das über das Internet mittels Browser zugegriffen wird. HTTP (HyperText Transfer Protocol) und HTTPS (sicheres HTTP) sind die Protokolle, die zum Übertragen von Webseiten verwendet werden. Eine IP-Adresse ist eine eindeutige numerische Adresse, die jedem Gerät in einem Netzwerk zugewiesen wird. DNS (Domain Name System) übersetzt für Menschen lesbare Domainnamen (wie google.com) in IP-Adressen. Ein Router leitet den Netzwerkverkehr zwischen Geräten und Netzwerken.

## Netzwerke und Protokolle

TCP/IP ist die grundlegende Protokollsuite des Internets. IP (Internet Protocol) übernimmt die Adressierung und das Routing von Paketen zwischen Netzwerken, während TCP (Transmission Control Protocol) eine zuverlässige, geordnete Zustellung mit Neuübertragung und Flusskontrolle bietet. UDP ist eine verbindungslose Alternative, die verwendet wird, wenn niedrige Latenz wichtiger ist als garantierte Zustellung (zum Beispiel beim Streaming, Gaming oder bei DNS-Anfragen). HTTP ist ein zustandsloses Anwendungsschichtprotokoll für die Anfrage-/Antwort-Kommunikation zwischen Clients und Servern. HTTPS ist HTTP über TLS und fügt Verschlüsselung und Integritätsschutz hinzu. REST (Representational State Transfer) ist ein API-Architekturstil, der Ressourcen, Standard-HTTP-Verben (GET, POST, PUT, PATCH, DELETE) und zustandslose Interaktionen verwendet. WebSockets bieten persistente Vollduplex-Verbindungen, sodass Client und Server Nachrichten in Echtzeit senden können, was nützlich für Chat, Live-Dashboards und kollaborative Apps ist.

## Künstliche Intelligenz

Künstliche Intelligenz (KI) ist die Simulation menschlicher Intelligenz durch Maschinen, insbesondere Computersysteme. Maschinelles Lernen ist ein Teilbereich der KI, bei dem Systeme aus Daten lernen, um Vorhersagen oder Entscheidungen zu treffen, ohne explizit programmiert zu werden. Deep Learning ist ein Teilbereich des maschinellen Lernens, der neuronale Netze mit vielen Schichten verwendet. Neuronale Netze sind Rechenmodelle, die lose von der Struktur biologischer Gehirne inspiriert sind. Große Sprachmodelle (LLMs) sind KI-Modelle, die auf riesigen Textmengen trainiert wurden, um natürliche Sprache zu generieren und zu verstehen.

## Algorithmen und Datenstrukturen

Ein Algorithmus ist eine schrittweise Vorgehensweise zur Lösung eines Problems. Datenstrukturen sind Möglichkeiten, Daten in einem Computer so zu organisieren, dass sie effizient abgerufen und geändert werden können. Zu den gängigen Datenstrukturen gehören Arrays, verkettete Listen, Stapel, Warteschlangen, Bäume, Graphen und Hashtabellen. Sortieralgorithmen ordnen Elemente in einer bestimmten Reihenfolge; gängige Beispiele sind Bubble Sort, Merge Sort und Quicksort. Die binäre Suche ist ein effizienter Algorithmus zum Finden eines Elements in einer sortierten Liste, indem der Suchbereich wiederholt halbiert wird.

## Datenbanken

Eine Datenbank ist eine organisierte Sammlung von strukturierten Daten, die elektronisch gespeichert werden. Eine relationale Datenbank speichert Daten in Tabellen mit Zeilen und Spalten. SQL (Structured Query Language) ist die Standardsprache zur Verwaltung und Abfrage relationaler Datenbanken. NoSQL-Datenbanken speichern Daten in anderen Formaten als Tabellenbeziehungen, wie zum Beispiel Dokumente, Schlüssel-Wert-Paare oder Graphen. Gängige Datenbanksysteme sind PostgreSQL, MySQL, SQLite, MongoDB und Redis. Ein Index in einer Datenbank beschleunigt den Datenabruf auf Kosten zusätzlichen Speichers.

## Grundlagen des Systemdesigns

Das Systemdesign konzentriert sich auf den Aufbau zuverlässiger, skalierbarer und wartbarer Softwaresysteme. Load Balancing verteilt den Verkehr auf mehrere Server, um die Verfügbarkeit zu verbessern und die Latenz zu verringern. Horizontale Skalierung fügt mehr Maschinen hinzu; vertikale Skalierung fügt einer Maschine mehr Ressourcen hinzu. Caching speichert häufig abgerufene Daten in schnellem Speicher (zum Beispiel Redis, Memcached oder CDN-Edge-Caches), um die Datenbanklast und die Antwortzeit zu reduzieren. Datenbanken im großen Maßstab erfordern Replikation, Partitionierung (Sharding), Backup-Strategien und sorgfältige Kompromisse bei der Konsistenz. Microservices teilen große Anwendungen in kleinere, unabhängig bereitstellbare Dienste auf, während Monolithen die meiste Logik in einer bereitstellbaren Einheit behalten; beide Ansätze beinhalten Kompromisse hinsichtlich Komplexität, Bereitstellungsgeschwindigkeit, Debugging und Teamautonomie.

## Betriebssysteme

Ein Betriebssystem (OS) ist Software, die Computerhardware verwaltet und Dienste für Programme bereitstellt. Gängige Betriebssysteme sind Windows, macOS und Linux. Linux ist ein Open-Source-OS-Kernel, der in Servern, eingebetteten Systemen und Android verwendet wird. Das Betriebssystem verwaltet Prozesse (laufende Programme), Speicher, Dateisysteme und Eingabe-/Ausgabegeräte. Ein Prozess ist eine laufende Instanz eines Programms. Ein Thread ist die kleinste Ausführungseinheit innerhalb eines Prozesses.

## Versionskontrolle

Versionskontrollsysteme verfolgen Änderungen am Code im Laufe der Zeit und ermöglichen Entwicklern die Zusammenarbeit und die Rückkehr zu früheren Zuständen. Git ist das am weitesten verbreitete Versionskontrollsystem. Ein Repository (Repo) ist eine Sammlung von Dateien und ihrem Verlauf. Ein Commit ist eine gespeicherte Momentaufnahme von Änderungen. Ein Branch ist eine unabhängige Entwicklungslinie. Ein Pull Request ist ein Vorschlag, Änderungen von einem Branch in einen anderen zusammenzuführen.

## Praktiken der Softwareentwicklung

Objektorientierte Programmierung (OOP) organisiert Code in Objekten, die Daten und Verhalten kombinieren. Zu den Grundprinzipien der OOP gehören Kapselung, Vererbung, Polymorphie und Abstraktion. Testgetriebene Entwicklung (TDD) ist eine Praxis, bei der Tests geschrieben werden, bevor der Code geschrieben wird. Agile ist eine Reihe von Softwareentwicklungsmethoden, die iterative Entwicklung, Zusammenarbeit und Anpassungsfähigkeit betonen. DevOps kombiniert Softwareentwicklung und IT-Betrieb, um den Entwicklungslebenszyklus zu verkürzen. APIs (Application Programming Interfaces) ermöglichen die Kommunikation zwischen verschiedenen Softwaresystemen.

## Grundlagen von Cloud und DevOps

Cloud-Computing bietet On-Demand-Infrastruktur und verwaltete Dienste über das Internet. Die drei großen öffentlichen Cloud-Anbieter sind AWS (Amazon Web Services), Microsoft Azure und Google Cloud Platform (GCP). Gängige Servicemodelle sind IaaS (Infrastruktur), PaaS (Plattform) und SaaS (Software). Zu den wichtigsten Cloud-Bausteinen gehören Compute-Instanzen/Container, Objektspeicher, verwaltete Datenbanken, Netzwerke und IAM (Identity and Access Management). CI/CD (Continuous Integration und Continuous Delivery/Bereitstellung) automatisiert Build-, Test- und Release-Pipelines, sodass Code sicher vom Commit bis zur Produktion gelangen kann. Docker packt Anwendungen und Abhängigkeiten in portable Container; in der Produktion werden diese Container typischerweise über Orchestratoren (wie Kubernetes), serverlose Plattformen oder verwaltete Containerdienste bereitgestellt.

## Datenformate und Werkzeuge

JSON (JavaScript Object Notation) ist ein leichtgewichtiges Textformat, das aus Objekten (Schlüssel/Wert-Paaren), Arrays, Strings, Zahlen, Booleschen Werten und Null aufgebaut ist; es wird häufig in APIs verwendet. YAML ist ein benutzerfreundliches Konfigurationsformat, das verschachtelte Strukturen und Kommentare unterstützt und häufig in CI/CD und Infrastrukturdefinitionen verwendet wird. CSV (Comma-Separated Values) speichert Tabellendaten als Zeilen von getrenntem Text und ist üblich für Datenimport-/exportpipelines. XML (eXtensible Markup Language) ist ein tagbasiertes strukturiertes Format, das in Legacy-Systemen, Konfigurationen und Dokumentenworkflows verwendet wird. Entwickler validieren und transformieren diese Formate häufig mit Lintern, Schemavalidatoren (wie JSON Schema), Abfragetools (`jq`, XPath) und Parsing-Bibliotheken in ihrer Programmiersprache.

## Reguläre Ausdrücke (Regex)

Ein regulärer Ausdruck ist eine Patternsprache, die zum Suchen, Matchen, Extrahieren und Transformieren von Text verwendet wird. Zu den Kernkonzepten von Regex gehören Literale (`cat`), Zeichenklassen (`[a-z]`, `\d`), Quantifizierer (`*`, `+`, `?`, `{n,m}`), Anker (`^`, `$`), Gruppen (`(...)`), Alternation (`a|b`) und das Escapen von Sonderzeichen. Regex wird häufig für die Eingabevalidierung, Log-Parsing, Textextraktion und Suchen-/Ersetzen-Automatisierung verwendet. Unterschiedliche Engines (PCRE, JavaScript, Python `re`, RE2) haben unterschiedliche Funktionsumfänge, sodass das Verhalten zwischen Tools variieren kann. Regex ist leistungsstark, kann aber schwer lesbar werden; komplexe Muster sollten getestet und dokumentiert werden, um Fehler zu vermeiden.

## Cybersicherheit

Cybersicherheit ist die Praxis, Computersysteme, Netzwerke und Daten vor digitalen Angriffen zu schützen. Häufige Bedrohungen sind Malware (schädliche Software), Phishing (betrügerische Kommunikation zum Stehlen von Informationen), Ransomware (Malware, die Daten verschlüsselt und Zahlung fordert) und Denial-of-Service-Angriffe. Verschlüsselung wandelt Daten in eine unlesbare Form um, die nur mit einem Schlüssel entschlüsselt werden kann. HTTPS verwendet TLS (Transport Layer Security), um Webverkehr zu verschlüsseln. Starke, eindeutige Passwörter und Zwei-Faktor-Authentifizierung sind grundlegende Sicherheitspraktiken.

## Sicherheitskonzepte für Entwickler

OAuth 2.0 ist ein Autorisierungsframework, mit dem Benutzern begrenzten Zugriff auf eine Anwendung gewähren können, ohne Anmeldeinformationen direkt weiterzugeben. OpenID Connect (OIDC) ist eine Identitätsschicht, die auf OAuth 2.0 für die Authentifizierung aufbaut. JWT (JSON Web Token) ist ein kompaktes Tokenformat, das Claims enthält und häufig für zustandslose Authentifizierung verwendet wird, muss jedoch korrekt signiert und streng validiert werden (Signatur, Ablauf, Aussteller, Zielgruppe). TLS sichert Daten während der Übertragung durch Verschlüsselung, Integrität und Serverauthentifizierung über Zertifikate. Die OWASP Top 10 ist eine weit verbreitete Liste gängiger Sicherheitsrisiken für Webanwendungen, darunter fehlerhafte Zugriffskontrolle, kryptografische Fehler, Injection, unsicheres Design, Sicherheitsfehlkonfiguration, anfällige Komponenten und unzureichendes Logging/Monitoring. Sichere Entwicklung erfordert Defense-in-Depth: Eingabevalidierung, Ausgabe-Encoding, geringste Privilegien, Geheimnisverwaltung, Patching von Abhängigkeiten und regelmäßige Sicherheitstests.
