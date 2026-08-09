---
# Metadata
title: "Security Best Practices"
description: "OWASP Top 10, input validation, auth, secrets management"
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
tags: [security, best, practices, coding-and-technology]
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

# Melhores práticas de segurança
Um guia prático para proteger aplicativos, infraestrutura e dados — do desenvolvimento à produção.
---

## OWASP Top 10 (2021) - Visão geral
1. **Controle de acesso quebrado**: os usuários podem acessar recursos que não deveriam.
2. **Falhas criptográficas**: Criptografia fraca ou ausente.
3. **Injeção**: SQL, NoSQL, comando do sistema operacional ou injeção LDAP.
4. **Design Inseguro**: Falhas arquitetônicas.
5. **Configuração incorreta de segurança**: senhas padrão, portas abertas, erros detalhados.
6. **Componentes vulneráveis ​​e desatualizados**: CVEs conhecidos em dependências.
7. **Falhas de identificação e autenticação**: Senhas fracas, gerenciamento incorreto de sessões.
8. **Falhas de integridade de software e dados**: ataques à cadeia de suprimentos, atualizações não assinadas.
9. **Falhas de registro e monitoramento de segurança**: Nenhuma detecção de violações.
10. **Falsificação de solicitação no lado do servidor (SSRF)**: Abuso do servidor para fazer solicitações a sistemas internos.
---

## Validação de entrada e codificação de saída
### Regras de validação
- **Lista de permissões > Lista negra**: defina padrões permitidos (por exemplo, regex para e-mail) em vez de bloquear padrões inválidos conhecidos.
- **Limites de comprimento**: aplique comprimentos máximos para evitar buffer overflows e DoS.
- **Verificação de tipo**: certifique-se de que números inteiros sejam inteiros e booleanos sejam booleanos.
- **Use bibliotecas bem testadas**: para validação de email, URL e data, use bibliotecas padrão (por exemplo,`email-validator`em Python,`validator.js`em Node).
### Codificação de saída
- **Codificação HTML**: Codifique`<`,`>`,`&`,`"`,`'`para evitar XSS.
- **Parametrização SQL**: Nunca concatene a entrada do usuário em consultas SQL. Use consultas parametrizadas (instruções preparadas) ou um ORM.
- **Escape de shell**: evite criar comandos de shell a partir da entrada do usuário; se inevitável, use`shlex.quote()`ou similar.
---

## Autenticação e Autorização
### Gerenciamento de senhas
- **Hashing**: armazene senhas com um algoritmo de hash forte e lento: **Argon2id** (preferencial), **bcrypt**, **scrypt** ou **PBKDF2**.
- **Salga**: Adicione um sal exclusivo por usuário.
- **Comprimento mínimo**: aplique pelo menos 12 a 16 caracteres.
- **MFA (autenticação multifator)**: requer um segundo fator (TOTP, SMS, chave de hardware) para operações confidenciais.
- **Limitação de taxa**: evita tentativas de força bruta em endpoints de login (por exemplo, 5 tentativas a cada 5 minutos por IP/usuário).
### Gerenciamento de sessão
- Use cookies SameSite seguros, somente HTTP, para tokens de sessão.
- Defina tempos de expiração apropriados.
- Invalidar sessões ao sair e alterar senha.
- Evite expor IDs de sessão em URLs.
###OAuth2/OIDC
- Use bibliotecas bem estabelecidas (por exemplo, Authlib, PyJWT, Passport.js, Spring Security).
- Valide completamente os tokens de identificação (assinatura, emissor, público, expiração).
- Use parâmetros de estado para evitar CSRF.
- Mantenha os segredos do cliente confidenciais.
### JWT (Tokens da Web JSON)
- **Sinal**: Utilize RS256 ou ES256 (assimétrico) para melhor segurança; HS256 (simétrico) é aceitável se os segredos compartilhados forem bem gerenciados.
- **Validar**: sempre verifique assinatura, emissor (`iss`), público (`aud`) e expiração (`exp`).
- **Mantenha uma expiração curta**: 15–60 minutos para tokens de acesso; use tokens de atualização para sessões mais longas.
- **Armazene com segurança**: Nunca armazene JWTs em localStorage (vulnerável a XSS); use cookies somente HTTP.
---

## Segurança de API
### Autenticação
- Sempre autentique chamadas de API (exceto endpoints públicos).
- Prefira chaves de API ou tokens OAuth2 em vez de autenticação básica (que envia credenciais em cada solicitação).
### Limitação e limitação de taxa
- Aplique limites de taxa por usuário e por IP para evitar abusos e DoS.
- Retorna`429 Too Many Requests`com um cabeçalho `Retry-After`.
### CORS (compartilhamento de recursos entre origens)
- Permitir apenas origens específicas (nunca`*`em produção).
- Valide o cabeçalho`Origin`no lado do servidor.
### Validação de entrada
- Valide todos os parâmetros da solicitação, incluindo cabeçalhos e corpo.
- Rejeitar campos inesperados (`"strict": true`ou`additionalProperties: false`no esquema JSON).
###HTTPS/TLS
- Aplicar HTTPS na produção.
- Use HSTS (HTTP Strict Transport Security) para forçar os navegadores a usar HTTPS.
- Use TLS 1.2 ou 1.3 (desative TLS 1.0/1.1).
---

## Gerenciamento de segredos
### Nunca codifique segredos
- Não comprometa segredos (chaves de API, senhas, URLs de banco de dados) para controle de origem.
- Use variáveis ​​de ambiente ou ferramentas de gerenciamento de segredos.
### Ferramentas
| Ferramenta | Descrição |
|------|-------------|
| **Cofre HashiCorp** | Segredos dinâmicos de nível empresarial |
| **AWS Secrets Manager/Azure Key Vault/GCP Secret Manager** | Nativo da nuvem |
| **SOPS** | Criptografe segredos em arquivos e confirme-os (com KMS ou GPG) |
| **Segredos do Docker** | Para o modo Enxame; Segredos do Kubernetes (considere o driver CSI externo do Secrets Store) |
### Rotação
- Alterne regularmente segredos e contas de serviço.
- Automatize a rotação sempre que possível.
---

## Gerenciamento de Dependências
### Verificação de vulnerabilidades
| Idioma/Plataforma | Ferramentas |
|-------------------|-------|
| **Píton** | `safety`,`pip-audit`,`bandit`|
| **Nó** | `npm audit`,`yarn audit`,`snyk`|
| **Ferrugem** | `cargo audit`|
| **Vá** | `govulncheck`|
| **Geral** | `Dependabot`(GitHub), `Renovate`,`Trivy`|
### Patches
- Mantenha as dependências atualizadas para versões corrigidas.
- Configure solicitações pull automatizadas para atualizações secundárias/de patch.
- Revise os changelogs para alterações significativas.
### Integridade da cadeia de suprimentos
- Use arquivos de bloqueio de pacote (`package-lock.json`,`Cargo.lock`,`go.sum`) para garantir compilações reproduzíveis.
- Verifique somas de verificação de dependências baixadas.
- Prefira registros oficiais e confie apenas em editores verificados.
---

## Segurança de infraestrutura
###Firewalls
- Bloqueie todas as portas de entrada, exceto aquelas explicitamente necessárias (por exemplo, 80, 443).
- Limite o acesso SSH a intervalos de IP específicos (ou use um VPN/bastion host).
- Use grupos de segurança (AWS) ou NSGs (Azure) para controle refinado.
### Endurecimento do SO
- Aplique atualizações de segurança regularmente (`sudo apt upgrade`,`yum update`).
- Desative serviços desnecessários e contas padrão.
- Use fail2ban para bloquear tentativas de força bruta no SSH.
- Harden SSH: desative o login root, use autenticação baseada em chave, altere a porta padrão (opcional).
### Segmentação de rede
- Coloque bancos de dados e caches em sub-redes privadas sem acesso à Internet.
- Use uma DMZ para serviços públicos.
- Aplicar o princípio do menor privilégio ao acesso à rede.
### Segredos em infraestrutura
- Nunca armazene segredos em variáveis de ambiente CI/CD, a menos que sejam criptografados.
- Use as funções IAM do provedor de nuvem para instâncias EC2/VM em vez de chaves de longa duração.
---

## Registro e monitoramento
### O que registrar
- Eventos de autenticação (sucesso/falha).
- Decisões de controlo de acessos (falhas de autorização).
- Ações administrativas (criação de usuários, exclusão, alterações de permissão).
- Alterações no esquema do banco de dados.
- Erros e exceções do sistema.
- Solicitações e respostas de API (redigir dados confidenciais).
### O que não registrar
- Senhas, segredos, tokens, PII (informações de identificação pessoal), a menos que tenham hash/redigido.
- Números completos de cartão de crédito.
### Alerta
- Configurar alertas para:
  - Vários logins com falha (potencial força bruta).
  - Padrões de acesso incomuns (por exemplo, de novos locais, em horários estranhos).
  - Novas contas de administrador criadas.
  - Altas taxas de erro ou picos de latência.
- Use um SIEM (Gerenciamento de Informações e Eventos de Segurança) para correlação avançada.
### Retenção de registros
- Retenha os registros por pelo menos 30 a 90 dias, dependendo dos requisitos regulamentares.
- Armazene logs em um sistema centralizado e inviolável (por exemplo, ELK Stack, Splunk, Datadog).
---

## Ciclo de vida de desenvolvimento seguro (SDL)
1. **Treinamento**: garanta que os desenvolvedores entendam as vulnerabilidades comuns.
2. **Modelagem de ameaças**: identifique ameaças potenciais no início do projeto.
3. **Padrões de codificação seguros**: aplique por meio de linters e listas de verificação de revisão de código.
4. **SAST** (teste estático de segurança de aplicativos): verifica o código-fonte em busca de vulnerabilidades (SonarQube, CodeQL).
5. **DAST** (Teste Dinâmico de Segurança de Aplicativos): Verifica aplicativos em execução (OWASP ZAP, Burp Suite).
6. **SCA** (Análise de Composição de Software): verifica dependências.
7. **Testes de penetração**: exercícios regulares de hacking ético.
8. **Recompensa de bugs**: incentive pesquisadores externos a encontrar vulnerabilidades de maneira responsável.
9. **Plano de resposta a incidentes**: tenha um plano claro para quando uma violação for detectada.
---

## Lista de verificação de emergência (quando há suspeita de violação)
1. **Não entre em pânico** – mas aja rapidamente.
2. **Isole** os sistemas afetados (desconecte da rede, se necessário).
3. **Preservar evidências**: capture logs, despejos de memória e imagens de disco.
4. **Identifique** o escopo: quais sistemas, quais dados.
5. **Alterne** todas as credenciais e segredos comprometidos.
6. **Corrija** a vulnerabilidade.
7. **Notificar** os usuários e órgãos reguladores afetados, se necessário (dentro dos prazos legais).
8. **Realize uma análise post-mortem** para entender a causa raiz e melhorar os processos.