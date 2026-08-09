---
# Metadata
title: "Cybersecurity Fundamentals"
description: "Encryption, TLS, OWASP, secure coding, SDL"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cybersecurity, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Fundamentos de segurança cibernética
A segurança não é um recurso que você incorpora no final — é uma disciplina que precisa ser integrada em cada camada de um sistema desde o primeiro dia. Esteja você criando um aplicativo Web, gerenciando infraestrutura ou enviando uma API, é essencial compreender o cenário de ameaças e os fundamentos da defesa.
---

## Criptografia e criptografia
### Criptografia Simétrica vs Assimétrica
| Tipo | Como funciona | Velocidade | Distribuição de Chaves | Exemplos |
|------|------------|-------|------|----------|
| **Simétrico** | Mesma chave para criptografia e descriptografia | Rápido | Desafio: como compartilhar a chave? | AES-256, ChaCha20 |
| **Assimétrico** | Criptografa com chave pública, descriptografa com chave privada | Mais lento | A chave pública pode ser compartilhada abertamente | RSA, ECC (curva elíptica) |
Na prática, a maioria dos sistemas usa **ambos**: criptografia assimétrica para trocar com segurança uma chave simétrica e, em seguida, criptografia simétrica para a maior parte dos dados. É assim que funciona o TLS/HTTPS.
### Hashing
Hashing é uma função unidirecional: converte a entrada em uma string de tamanho fixo. Você não pode reverter isso, mas a mesma entrada sempre produz a mesma saída.
| Caso de uso | Algoritmo Recomendado | Evite |
|----------|----------------------|-------|
| **Armazenamento de senha** | Argon2id, bcrypt, scrypt | MD5, SHA-1, SHA-256 simples (muito rápido) |
| **Integridade dos dados** | SHA-256, SHA-3 | MD5 (quebrado), SHA-1 (quebrado) |
| **Assinaturas digitais** | Ed25519, RSA-2048+ | DSA |
###TLS/HTTPS
HTTPS é HTTP sobre TLS (Transport Layer Security). Ele fornece:
- **Criptografia**: dados em trânsito não podem ser lidos por bisbilhoteiros.
- **Autenticação**: O servidor comprova sua identidade por meio de um certificado.
- **Integridade**: os dados não podem ser modificados em trânsito sem detecção.
Use TLS 1.2 ou 1.3. Desative o TLS 1.0 e 1.1. Habilite HSTS (HTTP Strict Transport Security) para forçar os navegadores a sempre usarem HTTPS.
---

## Autenticação e Autorização
### Autenticação: Quem é você?
| Método | Nível de segurança | Caso de uso |
|--------|---------------|----------|
| **Senha** | Baixo-Médio | Contas básicas (aplicar mais de 12 caracteres, verificar violações) |
| **MFA (TOTP)** | Alto | Padrão para contas confidenciais (Google Authenticator, Authy) |
| **Chave de hardware (FIDO2/WebAuthn)** | Muito alto | Contas de alta segurança (YubiKey) |
| **Biométrico** | Médio–Alto | Desbloqueio do dispositivo (impressão digital, rosto) – não é bom como único fator |
| **OAuth2/OIDC** | Alto | Login de terceiros (“Faça login com o Google”) |
**Regras de senha**: imponha comprimento mínimo (12 a 16 caracteres), verifique listas de senhas violadas, use Argon2id ou bcrypt para hash com sais por usuário.
### Autorização: O que você pode fazer?
| Modelo | Descrição | Exemplo |
|-------|-------------|---------|
| **RBAC** (controle de acesso baseado em função) | Permissões atribuídas às funções; usuários obtêm funções | Administrador, Editor, Visualizador |
| **ABAC** (baseado em atributos) | Regras baseadas em atributos do usuário, recurso, ambiente | “Os gestores podem aprovar as solicitações de sua equipe” |
| **ACL** (Lista de Controle de Acesso) | Permissões explícitas por usuário/recurso | Permissões de arquivo (leitura/gravação/execução) |
**Princípio do menor privilégio**: conceda a cada usuário, serviço e processo apenas o acesso mínimo necessário.
### JWT (Tokens da Web JSON)
| Aspecto | Recomendação |
|--------|---------------|
| **Assinatura** | RS256 ou ES256 (assimétrico) preferido; HS256 aceitável com segredos gerenciados |
| **Expiração** | 15–60 minutos para tokens de acesso; use tokens de atualização para sessões mais longas |
| **Armazenamento** | Cookies somente HTTP (não localStorage — vulneráveis ​​a XSS) |
| **Validação** | Sempre verifique assinatura, emissor, público e vencimento |
---

## Top 10 do OWASP (2021)
O OWASP Top 10 é o documento de conscientização padrão para segurança de aplicações web. Representa os riscos mais críticos:
| # | Risco | O que isso significa |
|---|------|---------|
| 1 | **Controle de acesso quebrado** | Os usuários podem acessar recursos que não deveriam |
| 2 | **Falhas criptográficas** | Criptografia fraca ou ausente para dados confidenciais |
| 3 | **Injeção** | SQL, NoSQL, comando OS ou injeção LDAP |
| 4 | **Design Inseguro** | Falhas arquitetônicas que não podem ser corrigidas com implementação |
| 5 | **Configuração incorreta de segurança** | Senhas padrão, portas abertas, mensagens de erro detalhadas |
| 6 | **Componentes vulneráveis** | CVEs conhecidos em dependências |
| 7 | **Falhas de autenticação** | Senhas fracas, gerenciamento incorreto de sessões |
| 8 | **Falhas de integridade** | Ataques à cadeia de suprimentos, atualizações não assinadas |
| 9 | **Falhas de registro/monitoramento** | Nenhuma detecção de violações |
| 10 | **SSRF** | Servidor enganado para fazer solicitações a sistemas internos |
---

## Práticas de codificação seguras
### Validação de entrada
| Regra | Por que |
|------|-----|
| **Lista de permissões > Lista negra** | Defina o que é permitido e não o que está bloqueado |
| **Consultas parametrizadas** | Nunca concatene a entrada do usuário no SQL — use instruções preparadas ou ORM |
| **Codificação HTML** | Codifique`<`,`>`,`&`,`"`,`'`para evitar XSS |
| **Shell escapando** | Evite criar comandos shell a partir da entrada do usuário; usar`shlex.quote()`|
| **Limites de comprimento** | Aplique comprimentos máximos para evitar buffer overflows e DoS |
| **Verificação de tipo** | Certifique-se de que inteiros sejam inteiros, booleanos sejam booleanos |
### Vulnerabilidades Comuns
| Vulnerabilidade | Ataque | Defesa |
|-------------|--------|---------|
| **Injeção SQL** | `' OR 1=1 --`no formulário de login | Consultas parametrizadas |
| **XSS** | `<script>alert('hacked')</script>`no campo de comentários | Codificação de saída, Política de segurança de conteúdo |
| **CSRF** | Enganar o navegador do usuário para que ele faça uma solicitação não autorizada | Tokens CSRF, cookies SameSite |
| **Travessia de caminho** | `../../etc/passwd`no parâmetro de arquivo | Validar e limpar caminhos de arquivos |
| **IDOR** | Altere`/user/123`para`/user/124`para ver os dados de outra pessoa | Verificações de autorização em cada solicitação |
---

## Segurança de rede
###Firewalls
| Tipo | Descrição |
|------|-------------|
| **Filtragem de pacotes** | Regras baseadas em IP, porta, protocolo |
| **Com estado** | Rastreia estados de conexão; filtragem mais inteligente |
| **Nível de aplicativo (WAF)** | Inspeciona o tráfego HTTP; bloqueia injeção de SQL, XSS, etc. |
| **Grupos de segurança na nuvem** | Firewalls virtuais para instâncias de nuvem (AWS SGs, Azure NSGs) |
**Regra prática**: bloqueie todo o tráfego de entrada por padrão; abra apenas o que é explicitamente necessário (80, 443 para web).
### Segmentação de rede
Coloque bancos de dados e caches em sub-redes privadas sem acesso direto à Internet. Use uma DMZ para serviços públicos (servidores web, balanceadores de carga). Aplique o princípio do menor privilégio ao acesso à rede.
---

## Gerenciamento de segredos
### A Regra de Ouro
**Nunca codifique segredos.** Nenhuma chave de API, senha ou URL de banco de dados no código-fonte. Nenhum segredo nas variáveis ​​de ambiente comprometidas com o Git. Não há segredos nas imagens do Docker.
### Ferramentas
| Ferramenta | Tipo | Melhor para |
|------|------|----------|
| **Cofre HashiCorp** | Gerenciador de segredos empresariais | Segredos dinâmicos, criptografia como serviço |
| **Gerenciador de segredos da AWS** | Nativo da nuvem | Ambientes AWS |
| **Cofre de Chaves do Azure** | Nativo da nuvem | Ambientes Azure |
| **SOPS** | Arquivos criptografados | Criptografar segredos no Git (com KMS ou GPG) |
| **Segredos do Docker** | Nativo de contêiner | Docker Swarm (para K8s, considere Secrets Store CSI) |
| **dotenv (.env)** | Desenvolvimento local | Somente desenvolvimento — nunca em produção ou comprometido |
### Rotação
Alterne os segredos regularmente e automaticamente. Se um segredo vazar (por exemplo, comprometido com um repositório público), alterne-o imediatamente – mesmo se você achar que ninguém o viu.
---

## Segurança de Dependências
Seu aplicativo é tão seguro quanto sua dependência mais fraca.
### Ferramentas de digitalização
| Idioma | Ferramentas |
|----------|-------|
| **Píton** | `safety`,`pip-audit`,`bandit`|
| **Node.js** | `npm audit`,`yarn audit`,`snyk`|
| **Ferrugem** | `cargo audit`|
| **Vá** | `govulncheck`|
| **Geral** | `Dependabot`(GitHub), `Renovate`,`Trivy`|
### Integridade da cadeia de suprimentos
- Use arquivos de bloqueio (`package-lock.json`,`Cargo.lock`,`go.sum`) para compilações reproduzíveis.
- Verifique somas de verificação de dependências baixadas.
- Prefira registros oficiais e editores verificados.
- Automatize atualizações secundárias/patch via Dependabot ou Renovate.
---

## Ciclo de vida de desenvolvimento de segurança (SDL)
| Fase | Atividade |
|-------|----------|
| **Treinamento** | Garanta que os desenvolvedores entendam as vulnerabilidades comuns |
| **Modelagem de ameaças** | Identificar ameaças potenciais durante o projeto |
| **Padrões de codificação seguros** | Aplicar por meio de linters e listas de verificação de revisão de código |
| **SAST** | Análise estática de código fonte (SonarQube, CodeQL) |
| **DAST** | Análise dinâmica de aplicação em execução (OWASP ZAP, Burp Suite) |
| **SCA** | Análise de composição de software — verificar dependências |
| **Teste de penetração** | Exercícios regulares de hacking ético |
| **Recompensa de Bugs** | Incentivar investigadores externos a encontrar vulnerabilidades |
| **Plano de resposta a incidentes** | Tenha um plano claro para quando uma violação for detectada |
---

## Lista de verificação de emergência
Quando você suspeita de uma violação:
1. **Não entre em pânico** – mas aja rapidamente.
2. **Isolar** os sistemas afetados (desconectar da rede, se necessário).
3. **Preservar evidências**: capturar logs, despejos de memória e imagens de disco.
4. **Identificar o escopo**: quais sistemas, quais dados?
5. **Alterne** todas as credenciais e segredos comprometidos.
6. **Corrija** a vulnerabilidade.
7. **Notificar** os usuários e reguladores afetados, se necessário (dentro dos prazos legais).
8. **Post-mortem**: documente a causa raiz e os itens de ação dentro de 24 a 48 horas.