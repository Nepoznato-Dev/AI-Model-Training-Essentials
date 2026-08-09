---
# Metadata
title: "API Design and Architecture"
description: "REST, GraphQL, gRPC, versioning, auth, API gateways"
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
tags: [api, design, architecture, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Design e arquitetura de API
Uma API (Interface de Programação de Aplicativo) é como os componentes de software se comunicam entre si. Uma API bem projetada é intuitiva, consistente e é um prazer trabalhar com ela. Um projeto mal projetado causa confusão, bugs e frustração. Este arquivo aborda os princípios, padrões e práticas para a construção de APIs que os desenvolvedores realmente desejam usar.
---

## Princípios da API REST
REST (Representational State Transfer) é o estilo arquitetônico dominante para APIs da web. Ele trata os dados como **recursos** identificados por URLs e usa métodos HTTP para operar neles.
### Princípios Fundamentais
| Princípio | Descrição |
|-----------|------------|
| **Recursos** | Tudo é um recurso com um URI (`/users/123`,`/orders/456`) |
| **Métodos HTTP** | GET (ler), POST (criar), PUT (substituir), PATCH (atualização parcial), DELETE (remover) |
| **Apatridia** | Cada solicitação contém todas as informações necessárias; nenhum estado de sessão do lado do servidor |
| **Interface Uniforme** | Nomenclatura consistente de recursos, métodos padrão, códigos de status padrão |
| **Representação** | Os recursos podem ser representados em vários formatos (JSON, XML) |
### Convenções de nomenclatura de recursos
| Faça | Não |
|----|-------|
| `/users`(substantivo plural) | `/user`(singular) |
| `/users/123/orders`(aninhado) | `/getOrdersForUser?id=123`|
| `/products?category=electronics`(parâmetros de consulta para filtragem) | `/productsByCategory/electronics`|
| Use hífens:`/user-profiles`| Use sublinhados:`/user_profiles`|
### Métodos HTTP e Idempotência
| Método | Finalidade | Idempotente? | Seguro? |
|----|---------|---------|-------|
| **OBTER** | Leia um recurso | ✅ Sim | ✅ Sim |
| **PUBLICAÇÃO** | Crie um recurso | ❌ Não | ❌ Não |
| **COLOCAR** | Substituir totalmente um recurso | ✅ Sim | ❌ Não |
| **PATCH** | Atualizar parcialmente um recurso | ❌Não* | ❌ Não |
| **EXCLUIR** | Remover um recurso | ✅ Sim | ❌ Não |
*PATCH pode ser tornado idempotente com um design cuidadoso.
### Códigos de status HTTP
| Código | Significado | Quando usar |
|------|---------|-------------|
| **200** | OK | GET, PUT, PATCH, DELETE com sucesso |
| **201** | Criado | POST bem sucedido (recurso criado) |
| **204** | Nenhum conteúdo | DELETE bem-sucedido (nada para retornar) |
| **400** | Solicitação incorreta | Entrada inválida ou solicitação malformada |
| **401** | Não autorizado | Autenticação ausente ou inválida |
| **403** | Proibido | Autenticado, mas não autorizado |
| **404** | Não encontrado | O recurso não existe |
| **409** | Conflito | Recurso duplicado ou conflito de estado |
| **422** | Entidade não processável | JSON válido, mas erros semânticos |
| **429** | Muitas solicitações | Limite de taxa excedido |
| **500** | Erro interno do servidor | Erro inesperado do servidor |
| **502** | Gateway ruim | Falha no serviço upstream |
| **503** | Serviço indisponível | Sobrecarga temporária ou manutenção |
---

## Versionamento de API
As APIs evoluem. Quando você precisa fazer alterações significativas, o controle de versão permite que os clientes existentes continuem trabalhando.
| Estratégia | Exemplo | Prós | Contras |
|----------|--------|------|------|
| **Caminho do URL** | `/v1/users`,`/v2/users`| Simples, explícito | Alterações de URL por versão |
| **Parâmetro de consulta** | `/users?version=2`| Flexível | Fácil de esquecer |
| **Cabeçalho** | `Accept: application/vnd.myapi.v2+json`| Limpar URLs | Menos detectável |
| **Sem controle de versão** | Apenas evolução do esquema | Mais simples | Mudanças radicais afetam a todos |
**Prática recomendada**: use o controle de versão do caminho de URL (`/v1/`) para maior clareza. Suporta pelo menos uma versão anterior. Descontinuar versões antigas com prazos claros.
---

## Métodos de autenticação
| Método | Como funciona | Melhor para |
|--------|-------------|----------|
| **Chaves de API** | Chave secreta no cabeçalho (`X-API-Key: abc123`) | Integrações simples de servidor para servidor |
| **OAuth2** | Delegação baseada em token com escopos | Acesso de terceiros, aplicativos autorizados pelo usuário |
| **JWT** | Token independente com reivindicações | Autenticação sem estado entre serviços |
| **Autenticação Básica** | Nome de usuário codificado em Base64:senha | Somente desenvolvimento — nunca produção sem TLS |
| **Cookies de sessão** | ID de sessão do lado do servidor em cookie somente HTTP | Aplicações web tradicionais |
### Fluxo OAuth2 (simplificado)
1. O cliente redireciona o usuário para o servidor de autorização.
2. O usuário faz login e concede permissão.
3. O servidor de autorização retorna um código de autorização.
4. O cliente troca o código pelo token de acesso (e, opcionalmente, pelo token de atualização).
5. O cliente usa token de acesso para chamar a API.
6. Quando o token de acesso expirar, use o token de atualização para obter um novo.
---

## Estilos de API: REST vs GraphQL vs gRPC
| Recurso | REST | GráficoQL | gRPC |
|--------|------|---------|------|
| **Formato de dados** | JSON (normalmente) | JSON | Protobuf (binário) |
| **Pontos finais** | Múltiplo (um por recurso) | Ponto final único | Definido pelo arquivo .proto |
| **Busca excessiva** | Comum (consiga mais do que o necessário) | Nenhum (cliente especifica campos) | Nenhum (definido pelo esquema) |
| **Busca insuficiente** | Requer múltiplas chamadas | Nenhum (obtenha exatamente o que é necessário) | Nenhum |
| **Em tempo real** | WebSockets necessários | Assinaturas integradas | Streaming integrado |
| **Cache** | O cache HTTP funciona naturalmente | Mais difícil de armazenar em cache | Limitado |
| **Curva de aprendizagem** | Baixo | Médio | Médio–Alto |
| **Melhor para** | APIs públicas, aplicativos CRUD | UIs complexas, aplicativos móveis | Microsserviços internos de alto desempenho |
---

## Paginação, filtragem e classificação
Para endpoints que retornam listas:
| Técnica | Exemplo | Quando usar |
|-----------|---------|------------|
| **Compensação/Limite** | `?offset=20&limit=10`| Simples; funciona para pequenos conjuntos de dados |
| **Baseado em cursor** | `?cursor=abc123&limit=10`| Grandes conjuntos de dados; resultados consistentes |
| **Conjunto de chaves** | `?created_after=2024-01-01&limit=10`| Muito eficiente; requer chave exclusiva |
```json
// Cursor-based response
{
  "data": [...],
  "pagination": {
    "next_cursor": "abc123",
    "has_more": true
  }
}
```

---

## Limitação de taxa
Proteja sua API contra abusos e garanta um uso justo.
| Estratégia | Como funciona |
|----------|------------|
| **Janela fixa** | N solicitações por janela de tempo (por exemplo, 100/hora) |
| **Janela deslizante** | Mais granulado; conta solicitações em janela contínua |
| **Balde de tokens** | Tokens adicionados a taxa fixa; cada solicitação consome um token |
Retorne`429 Too Many Requests`com cabeçalhos:```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1625097600
Retry-After: 60
```

---

## Tratamento de erros
Respostas de erro consistentes tornam as APIs muito mais fáceis de trabalhar:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "issue": "Invalid email format"
      }
    ]
  }
}
```

**Princípios**: use uma estrutura de erros consistente, inclua mensagens acionáveis, use códigos de status HTTP padrão, registre erros no servidor com IDs de correlação e nunca exponha rastreamentos de pilha ou detalhes internos.
---

## Documentação da API
| Ferramenta | Descrição |
|------|-------------|
| **OpenAPI (Swagger)** | Padrão da indústria para documentação da API REST |
| **IU do Swagger** | Documentação interativa da API da especificação OpenAPI |
| **Carteiro** | Teste de API, documentação e compartilhamento de coleções |
| **Redoc** | Lindos documentos de referência de API da especificação OpenAPI |
| **GraphQL Playground / GraphiQL** | Exploração interativa do GraphQL |
**Prática recomendada**: escreva primeiro a especificação OpenAPI (desenvolvimento baseado em especificações) e depois gere documentação e SDKs de cliente a partir dela.
---

## Padrões de gateway de API
Um gateway de API fica entre clientes e serviços de back-end, fornecendo um único ponto de entrada.
| Responsabilidade | Descrição |
|---------------|------------|
| **Roteamento** | Solicitações diretas para serviços de back-end apropriados |
| **Autenticação** | Validar tokens no nível do gateway |
| **Limitação de taxa** | Aplicar limites globais ou por cliente |
| **Transformação** | Converter entre protocolos (REST ↔ gRPC) |
| **Cache** | Cache de respostas comuns |
| **Monitoramento** | Registro e métricas centralizadas |
| **Balanceamento de carga** | Distribuir o tráfego entre instâncias de serviço |
| Ferramenta | Tipo |
|------|------|
| **Kong** | Gateway de API de código aberto (baseado em Nginx) |
| **Gateway de API da AWS** | Totalmente gerenciado, integrado com AWS |
| **Gerenciamento de API do Azure** | Gateway gerenciado com portal do desenvolvedor |
| **Enviado/Istio** | Malha de serviço com recursos de gateway de API |
| **Traefik** | Descoberta automática, integração Let's Encrypt |
---

## Webhooks
Os webhooks permitem que sua API envie eventos aos clientes em tempo real, em vez de fazer com que os clientes pesquisem alterações.
| Aspecto | Melhores Práticas |
|--------|-------------|
| **Entrega** | Solicitação POST com carga JSON para URL do cliente |
| **Segurança** | Assine cargas úteis com HMAC; cliente verifica assinatura |
| **Confiabilidade** | Tentar novamente entregas com falha com espera exponencial |
| **Idempotência** | Incluir ID de evento exclusivo; cliente lida com duplicatas |
| **Versionamento** | Incluir versão da API na carga útil do webhook |
---

## Lista de verificação de projeto
- [ ] Recursos são substantivos plurais (`/users`, não`/getUser`)
- [ ] Métodos HTTP usados corretamente (GET para leituras, POST para criações, etc.)
- [] Formato de resposta de erro consistente
- [] Paginação para todos os endpoints da lista
- [] Limitação de taxa com cabeçalhos claros
- [] Estratégia de versionamento de API definida
- [] Autenticação e autorização em vigor
- [] Validação de entrada em todos os endpoints
- [] Documentação OpenAPI/Swagger mantida
- [] CORS configurado corretamente
- [] HTTPS aplicado na produção
- [] Chaves de idempotência para operações POST quando necessário