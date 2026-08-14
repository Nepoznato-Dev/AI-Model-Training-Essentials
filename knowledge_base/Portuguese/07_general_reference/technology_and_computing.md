---
# Metadata
title: "Technology and Computing"
description: "Computing basics, internet, databases, cloud, security"
category: "General Reference"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "General Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [technology, computing, general-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Tecnologia e Computação
A computação está em toda parte – no seu telefone, no seu carro, na sua geladeira, nos seus dispositivos médicos e na infraestrutura que administra a sociedade moderna. Você não precisa ser um programador para entender como tudo funciona. Este arquivo aborda os fundamentos: o que é um computador, como funciona a Internet, como o software é construído e os conceitos que moldam o mundo digital.
> **Quer se aprofundar?** Este arquivo é uma visão geral ampla. Para cobertura detalhada de qualquer tópico, consulte os arquivos dedicados em[`01_coding_and_technology/`](../01_coding_and_technology/)— incluindo[database systems](../01_coding_and_technology/database_systems.md),[cloud architecture](../01_coding_and_technology/cloud_architecture.md),[networking](../01_coding_and_technology/networking_basics.md)e.
---

## O que é um computador?
Basicamente, todo computador – de um smartphone a um supercomputador – faz a mesma coisa: recebe informações, processa-as de acordo com instruções (um programa) e produz resultados. A magia está na velocidade e na escala.
### A Arquitetura Von Neumann
Quase todos os computadores modernos seguem este design básico:
| Componente | O que faz | Analogia |
|-----------|-------------|---------|
| **CPU** (Unidade Central de Processamento) | Executa instruções; o "cérebro" | O chef seguindo uma receita |
| **RAM** (Memória) | Armazena dados que a CPU está usando ativamente; perdido quando a energia está desligada | A bancada — acesso rápido, espaço limitado |
| **Armazenamento** (SSD/HDD) | Armazena dados permanentemente | A despensa — acesso mais lento, muito mais espaço |
| **Entrada/Saída** | Teclado, mouse, tela, rede | Como o chef recebe os pedidos e entrega a comida |
| **GPU** (Unidade de Processamento Gráfico) | Processador especializado para tarefas paralelas (gráficos, IA) | Uma equipe de assistentes realizando a mesma tarefa simultaneamente |
**Informação importante**: A RAM é rápida, mas temporária. O armazenamento é lento, mas permanente. Quando o seu computador “parece lento”, geralmente é porque ele está ficando sem memória RAM e precisa usar o armazenamento como memória temporária (troca), o que é muito mais lento.
---

## Linguagens de Programação — Conversando com Computadores
Uma linguagem de programação é um conjunto de instruções que um computador pode executar. Diferentes idiomas são projetados para finalidades diferentes. Para cobertura detalhada de 34 idiomas individuais, consulte a pasta [`programming_languages/`](../01_coding_and_technology/programming_languages/).
| Idioma | Melhor para | Por que escolher |
|----------|------------|---------------|
| **Píton** | Ciência de dados, IA, automação, backends web | Sintaxe simples; enorme ecossistema; ótimo para iniciantes |
| **JavaScript** | Front-ends da Web, pilha completa (Node.js) | Funciona em todos os navegadores; essencial para desenvolvimento web |
| **Java** | Software empresarial, aplicativos Android | Independente de plataforma (JVM); grande ecossistema |
| **C/C++** | Programação de sistemas, jogos, embarcados | Desempenho máximo; controle direto de hardware |
| **Ferrugem** | Programação de sistemas com garantias de segurança | Segurança de memória sem coleta de lixo |
| **Vá** | Serviços em nuvem, microsserviços, ferramentas CLI | Simples; excelente simultaneidade; compilação rápida |
| **SQL** | Consultas de banco de dados | A linguagem universal para trabalhar com dados |
| **TypeScript** | Aplicações web em grande escala | JavaScript com verificação de tipo; detecta bugs cedo |
---

## Como funciona a Internet
A internet não é a mesma coisa que a web. A Internet é a rede física – cabos, roteadores, servidores e protocolos que conectam bilhões de dispositivos. A World Wide Web é um serviço executado na Internet (junto com e-mail, transferência de arquivos, streaming, jogos, etc.).
### A jornada de uma solicitação da Web
Ao digitar`https://www.example.com`em seu navegador:
1. **Pesquisa de DNS**: seu navegador solicita a um servidor DNS que traduza "www.example.com" em um endereço IP (como 93.184.216.34).
2. **Conexão TCP**: seu dispositivo estabelece uma conexão com esse endereço IP usando TCP (um protocolo que garante entrega confiável).
3. **Handshake TLS**: Se estiver usando HTTPS, seu navegador e o servidor negociam uma conexão criptografada.
4. **Solicitação HTTP**: Seu navegador envia uma solicitação: "Dê-me a página em /index.html."
5. **Processamento do servidor**: O servidor web encontra a página, possivelmente consulta um banco de dados e prepara uma resposta.
6. **Resposta HTTP**: O servidor envia de volta HTML, CSS e JavaScript.
7. **Renderização**: seu navegador analisa o HTML, aplica estilos CSS e executa JavaScript para exibir a página.
Todo esse processo normalmente leva menos de um segundo.
### Principais Protocolos
| Protocolo | O que faz | Camada |
|----------|-------------|-------|
| **IP** (Protocolo de Internet) | Roteia pacotes entre redes | Rede |
| **TCP** | Entrega confiável e ordenada (retransmite pacotes perdidos) | Transporte |
| **UDP** | Entrega rápida e pouco confiável (sem retransmissão) | Transporte |
| **HTTP/HTTPS** | Transferência de páginas da Web (HTTPS adiciona criptografia) | Aplicação |
| **DNS** | Traduz nomes de domínio em endereços IP | Aplicação |
| **SSH** | Acesso remoto seguro a computadores | Aplicação |
| **SMTP/IMAP** | Envio e recebimento de e-mail | Aplicação |
---

## Desenvolvimento de software — Como os programas são construídos
### O Processo de Desenvolvimento
1. **Escrever código**: Os desenvolvedores escrevem instruções em uma linguagem de programação.
2. **Código de teste**: execute o código para verificar se funciona corretamente.
3. **Controle de versão**: rastreie alterações usando Git — o padrão universal.
4. **Revisão**: Outros desenvolvedores verificam erros e qualidade no código.
5. **Build**: Converte o código-fonte em um programa executável (compilação).
6. **Implantar**: Liberar o programa para os usuários (servidores, lojas de aplicativos, etc.).
7. **Monitore**: observe erros e problemas de desempenho na produção.
### Conceitos-chave
| Conceito | O que isso significa | Por que é importante |
|--------|---------------|----------------|
| **Controle de versão (Git)** | Acompanhe todas as alterações no código ao longo do tempo | Colaboração; capacidade de desfazer erros |
| **API** (Interface de Programação de Aplicativo) | Uma forma definida de comunicação entre componentes de software | Permite que diferentes sistemas funcionem juntos |
| **Banco de dados** | Armazenamento organizado de dados | Todo aplicativo precisa armazenar e recuperar dados |
| **Testes** | Verificações automatizadas se o código funciona corretamente | Evita que bugs cheguem aos usuários |
| **CI/CD** (Integração/Entrega Contínua) | Pipeline automatizado desde a confirmação do código até a produção | Lançamentos mais rápidos e seguros |
| **Conteinerização (Docker)** | Empacotar um aplicativo com todas as suas dependências | “Funciona na minha máquina” torna-se “funciona em qualquer lugar” |
---

## Bancos de dados – onde os dados residem
Todo aplicativo precisa armazenar dados. Os bancos de dados são os sistemas que fazem isso de forma eficiente e confiável.
| Tipo | Como os dados são armazenados | Melhor para | Exemplos |
|------|-------------------|----------|---------|
| **Relacional (SQL)** | Tabelas com linhas e colunas; esquema estrito | Dados estruturados; consultas complexas; transações | PostgreSQL, MySQL, SQLite |
| **Documento (NoSQL)** | Documentos semelhantes a JSON; esquema flexível | Dados semiestruturados; iteração rápida | MongoDB, CouchDB |
| **Valor-chave** | Chave simples → pares de valores | Cache; armazenamento de sessão; pesquisas rápidas | Redis, DynamoDB |
| **Gráfico** | Nós e arestas (relacionamentos) | Redes sociais; motores de recomendação | Neo4j, JanusGraph |
| **Série temporal** | Otimizado para dados com carimbo de data/hora | Monitoramento; análise; IoT | InfluxDB, TimescaleDB |
**SQL** (Structured Query Language) é a linguagem padrão para bancos de dados relacionais. É uma das habilidades técnicas mais valiosas que você pode aprender – quase todas as organizações usam bancos de dados, e SQL é a forma como você se comunica com eles.
---

## Sistemas operacionais
O sistema operacional (SO) é a camada de software entre você (e seus programas) e o hardware. Ele gerencia memória, processos, arquivos e dispositivos.
| SO | Onde domina | Recurso principal |
|----|----|---------|
| **Janelas** | Desktops/laptops (~72% de participação de mercado) | Maior compatibilidade de software/hardware |
| **macOS** | Profissionais criativos, desenvolvedores | Baseado em Unix; UI polida; Ecossistema Apple |
| **Linux** | Servidores (~96%), supercomputadores (100%), incorporados, desenvolvedores | Código aberto; livre; extremamente personalizável |
| **Android** | Móvel (~72% de participação no mercado global) | Baseado no kernel Linux; código aberto |
| **iOS** | Móvel (~27% global, mas receita maior) | Ecossistema fechado; polido; focado na privacidade |
O Linux merece menção especial: ele alimenta a maior parte da Internet, todos os 500 principais supercomputadores, a maior parte da infraestrutura em nuvem e todos os telefones Android. É gratuito, de código aberto e mantido por uma comunidade global.
---

## Computação em nuvem
Computação em nuvem significa alugar recursos computacionais (servidores, armazenamento, bancos de dados, etc.) pela internet em vez de comprar e manter seu próprio hardware. Para obter um guia abrangente sobre arquitetura de nuvem, modelos de serviço e comparações de provedores, consulte[cloud architecture](../01_coding_and_technology/cloud_architecture.md).
| Modelo de serviço | O que você ganha | Analogia | Exemplos |
|---------------|-------------|---------|---------|
| **IaaS** (Infraestrutura) | Servidores virtuais, armazenamento, rede | Alugar um terreno e construir o que quiser | AWS EC2, Google Compute Engine |
| **PaaS** (Plataforma) | Ambiente de execução; você traz código | Alugar apartamento mobiliado | Heroku, Google App Engine |
| **SaaS** (Software) | Aplicação completa; você acabou de usá-lo | Ficar em um hotel | Gmail, Slack, Salesforce |
Os três principais provedores de nuvem são **AWS** (Amazon, aproximadamente 32% de participação de mercado), **Azure** (Microsoft, aproximadamente 23%) e **GCP** (Google, aproximadamente 10%). Eles oferecem centenas de serviços que abrangem computação, armazenamento, bancos de dados, IA, redes e muito mais.
---

## Cibersegurança — Protegendo Sistemas Digitais
A segurança cibernética é a prática de defender computadores, redes e dados contra ataques. É importante porque tudo está conectado e o custo das violações é enorme. Para obter um guia completo que cobre os 10 principais OWASP, ciclo de vida de desenvolvimento seguro e gerenciamento de segredos, consulte.
### Ameaças Comuns
| Ameaça | O que é isso | Prevenção |
|--------|-----------|-----------|
| **Malware** | Software malicioso (vírus, worms, trojans) | Antivírus; manter o software atualizado |
| **Phishing** | E-mails/mensagens falsas enganando você para que revele informações | Treinamento; filtragem de e-mail; ceticismo |
| **Ransomware** | Criptografa seus dados; exige pagamento pela chave | Backups; sistemas de patches; não pague |
| **DDoS** | Sobrecarrega um serviço com tráfego | Filtragem de tráfego; Proteção CDN |
| **Injeção SQL** | Inserindo SQL malicioso em campos de entrada | Consultas parametrizadas; validação de entrada |
| **Man-in-the-middle** | Interceptando comunicação entre duas partes | Criptografia HTTPS/TLS |
### Fundamentos de segurança
- **Criptografia**: Codifique os dados para que somente pessoas autorizadas possam lê-los. HTTPS usa TLS para criptografar o tráfego da web.
- **Autenticação**: Verifique a identidade. Use autenticação multifator (MFA) — senha + outra coisa (código, biométrico).
- **Autorização**: verifique as permissões. Só porque você está logado não significa que você deva acessar tudo.
- **Princípio do menor privilégio**: forneça aos usuários e sistemas apenas o acesso necessário, nada mais.
- **Gerenciamento de patches**: mantenha o software atualizado. A maioria das violações explora vulnerabilidades conhecidas que já possuem patches.
---

## Formatos de dados
Os programas trocam dados em formatos específicos. O mais comum:
| Formato | Estrutura | Usado para |
|--------|-----------|----------|
| **JSON** | Pares de valores-chave; legível por humanos | APIs; configuração; intercâmbio de dados |
| **XML** | Baseado em tags; detalhado, mas flexível | Sistemas legados; documentos; APIs SOAP |
| **YAML** | Baseado em recuo; muito legível | Configuração (Docker, Kubernetes, CI/CD) |
| **CSV** | Linhas e colunas de texto simples | Importação/exportação de dados; planilhas |
---

## Resumo
A computação não é mágica – é engenharia. Os computadores seguem instruções com uma velocidade incrível. A Internet conecta bilhões deles usando protocolos padronizados. O software é construído por equipes de pessoas que escrevem, testam e implantam código em ciclos iterativos. Os bancos de dados armazenam e recuperam dados. A computação em nuvem permite que qualquer pessoa acesse enormes recursos de computação sob demanda. E a segurança cibernética é a batalha contínua para manter tudo isso protegido de pessoas que queiram explorá-lo. Compreender esses fundamentos ajuda você a navegar no mundo digital — seja você um usuário, um desenvolvedor ou apenas alguém tentando entender a tecnologia que molda a vida moderna.