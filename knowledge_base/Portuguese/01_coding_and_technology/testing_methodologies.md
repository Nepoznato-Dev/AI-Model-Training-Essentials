<!--
---
# Metadata
title: "Testing Methodologies"
description: "Unit, integration, E2E, TDD, BDD, test pyramids"
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
tags: [testing, methodologies, coding-and-technology]
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

-->
# Metodologias de Teste
Testar é como você ganha confiança de que seu código funciona — e, mais importante, de que alterações nele não quebram o que já funciona. Bons testes detectam bugs antes dos usuários, documentam o comportamento esperado e permitem refatoração destemida. Este arquivo cobre todo o espectro de estratégias de teste, desde testes unitários até testes ponta a ponta, e os princípios que tornam os testes eficazes.
---

## A pirâmide de testes
A pirâmide de testes descreve a distribuição ideal de testes em um projeto.
```
        /  E2E  \          ← Few; slow; expensive; test the whole system
       /─────────\
      / Integration\       ← Some; test how components work together
     /───────────────\
    /   Unit Tests    \    ← Many; fast; cheap; test individual functions
   /─────────────────────\
```

| Nível | Contagem | Velocidade | Custo | O que testa |
|-------|-------|-------|------|---------------|
| **Unidade** | Muitos | Rápido (ms) | Baixo | Funções individuais, classes, métodos |
| **Integração** | Alguns | Médio (100ms-s) | Médio | Como os componentes interagem; consultas de banco de dados; Chamadas de API |
| **E2E** | Poucos | Lento (segundos-minutos) | Alto | O usuário completo flui através do sistema real |
---

## Teste de unidade
Testar unidades individuais de código isoladamente.
### Princípios
| Princípio | Descrição |
|-----------|------------|
| **Rápido** | Cada teste deve ser executado em milissegundos |
| **Isolado** | Os testes não dependem uns dos outros; nenhum estado compartilhado |
| **Determinístico** | Mesma entrada → mesma saída sempre (sem aleatoriedade, sem dependência de tempo) |
| **Autoverificação** | O teste passa ou falha automaticamente; sem inspeção manual |
| **Oportuno** | Escrito ao lado ou antes do código (TDD) |
### Anatomia de um Teste
| Fase | Descrição |
|-------|------------|
| **Organizar** | Configure os dados de teste e dependências |
| **Agir** | Chame a função ou método que está sendo testado |
| **Afirmar** | Verifique se o resultado corresponde às expectativas |
### O que testar
| Categoria | Exemplos |
|----------|---------|
| **Caminho feliz** | Os insumos normais produzem os resultados esperados |
| **Casos extremos** | Entrada vazia, nulo, zero, valores máximos, elemento único |
| **Casos de erro** | Entrada inválida, dados ausentes, permissão negada |
| **Condições-limite** | Um por um; exatamente nos limites |
### Zombando e Stubbing
| Prazo | Descrição | Quando usar |
|------|-------------|-------------|
| **Simulação** | Um objeto falso que registra como foi chamado | Verificando interações (esse método foi chamado?) |
| **Esboço** | Um objeto falso que retorna valores predeterminados | Fornecendo dados de teste (retorne este usuário do banco de dados) |
| **Espião** | Um wrapper que registra chamadas para um objeto real | Verificação parcial |
| **Falso** | Uma implementação simplificada, mas funcional | Banco de dados em memória para testes |
| Biblioteca Zombando | Idioma |
|----------------|--------|
| **unitest.mock** | Pitão |
| ** Brincadeira ** | JavaScript/TypeScript |
| **Mockito** | Java |
| **Quantidade mínima** | C# |
| **testemunhar / zombar** | Vá |
---

## Teste de Integração
Testando como vários componentes funcionam juntos.
| O que testar | Exemplo |
|------------|---------|
| **Consultas ao banco de dados** | O ORM produz SQL correto? São usados ​​índices? |
| **Endpoints de API** | O ciclo completo de solicitação-resposta funciona? |
| **Interações de serviço** | O serviço A chama corretamente o serviço B? |
| **Dependências externas** | A integração do gateway de pagamento funciona? |
### Estratégias
| Estratégia | Descrição | Troca |
|----------|-------------|-----------|
| **Dependências reais** | Use um banco de dados real, fila de mensagens real | Mais realista; Mais devagar; mais difícil de configurar |
| **Contêineres de teste** | Ative contêineres Docker para cada execução de teste | Bom equilíbrio; reproduzível |
| **Alternativas na memória** | H2 em vez de PostgreSQL; barramento de mensagens na memória | Rápido; pode perder questões do mundo real |
| **Testes de contrato** | Verifique se os serviços honram seus contratos de API | Captura alterações de interface |
---

## Teste ponta a ponta (E2E)
Testando o sistema completo da perspectiva do usuário.
| Ferramenta | Tipo | Melhor para |
|------|------|----------|
| **Dramaturgo** | Automação do navegador | Aplicativos Web; entre navegadores |
| **Cipreste** | Automação do navegador | Aplicativos Web; experiência do desenvolvedor |
| **Selênio** | Automação do navegador | Legado; amplo suporte a idiomas |
| **Desintoxicação** | E2E móvel | Aplicativos React Native |
| **Ápio** | E2E móvel | Aplicativos móveis nativos e híbridos |
| **Maestro** | E2E móvel | Aplicativos móveis; sintaxe YAML simples |
| **k6 / Gafanhoto** | Teste de carga | Desempenho sob carga |
### Melhores práticas E2E
| Prática | Por que |
|----------|-----|
| **Teste apenas caminhos críticos** | Os testes E2E são lentos; concentre-se no que é mais importante |
| **Use fábricas de dados de teste** | Crie dados de teste programaticamente; não confie em dados iniciais |
| **Limpeza após testes** | Cada teste deverá deixar o sistema em um estado conhecido |
| **Evite testar detalhes da IU** | Comportamento de teste, não classes CSS ou posições de elementos |
| **Executar em CI** | Os testes E2E devem ser executados automaticamente a cada alteração |
---

## Desenvolvimento Orientado a Testes (TDD)
Escreva o teste primeiro e depois escreva o código para fazê-lo passar.
| Etapa | Descrição |
|------|-------------|
| **1. Vermelho** | Escreva um teste com falha que descreva o comportamento desejado |
| **2. Verde** | Escreva o código mínimo para fazer o teste passar |
| **3. Refatorar** | Limpe o código enquanto mantém os testes verdes |
| Benefício | Descrição |
|--------|-------------|
| **Comentários sobre o projeto** | Os testes obrigam você a pensar nas interfaces antes da implementação |
| **Segurança de regressão** | Cada bug passa por um teste; o bug nunca pode retornar |
| **Documentação** | Os testes servem como documentação viva do comportamento esperado |
| **Confiança** | A alta cobertura de testes permite refatoração destemida |
---

## Desenvolvimento Orientado a Comportamento (BDD)
O BDD estende o TDD escrevendo testes em linguagem natural que descrevem o comportamento da perspectiva do usuário.
### Formato Dado-Quando-Então
```
Given a user with an empty shopping cart
When they add a "Python Book" priced at $29.99
Then the cart total should be $29.99
And the cart should contain 1 item
```

| Ferramenta | Idioma |
|------|----------|
| **Pepino** | Java, JavaScript, Ruby e outros |
| **Comporte-se** | Pitão |
| **SpecFlow** | C# |
| **Jest** (com descrição) | JavaScript |
---

## Outros tipos de teste
| Tipo | O que testa | Ferramentas |
|------|-------------|-------|
| **Desempenho/Carga** | Comportamento do sistema sob carga | k6, JMeter, Gafanhoto, Gatling |
| **Segurança** | Vulnerabilidades e vetores de ataque | OWASP ZAP, Suíte Burp, Snyk |
| **Acessibilidade** | Conformidade com WCAG | machado, farol, pa11y |
| **Contrato** | Compatibilidade de API entre serviços | Pacto, Contrato Spring Cloud |
| **Mutação** | Qualidade do próprio conjunto de testes | Stryker, idiota, PIT |
| **Regressão visual** | Mudanças na interface do usuário entre versões | Percy, Cromático, BackstopJS |
| **Caos** | Resiliência do sistema a falhas | Macaco do Caos, Tornassol, Gremlin |
| **Fumaça** | Funcionalidade básica após implantação | Scripts personalizados; exames de saúde |
| **Mergulhe** | Comportamento do sistema durante um período prolongado | Testes de carga de longa duração |
---

## Organização de teste
| Padrão | Descrição | Quando usar |
|---------|-------------|-------------|
| **Co-localizado** | Testes ao lado do código que eles testam (`src/utils.test.ts`) | A maioria dos projetos; fácil de encontrar |
| **Diretório separado** | Testes em uma pasta`tests/`ou`__tests__/`| Grandes projetos; separação clara |
| **Acessórios de teste** | Dados de teste compartilhados em um diretório`fixtures/`| Quando vários testes precisam dos mesmos dados |
| **Utilitários de teste** | Ajudantes compartilhados em um diretório`test-utils/`| Quando a lógica de configuração é complexa |
---

## Cobertura de código
| Métrica | O que mede | Limitação |
|--------|-------|-----------|
| **Cobertura de linha** | Porcentagem de linhas de código executadas por testes | Não mede qualidade das afirmações |
| **Cobertura de filiais** | Percentagem de sucursais (if/else) ocupadas | Melhor que a cobertura de linha; ainda não detecta todos os bugs |
| **Cobertura do caminho** | Percentagem de caminhos de execução percorridos | Mais completo; exponencial em código complexo |
| **Pontuação de mutação** | Percentagem de mutações detectadas em testes | Melhor medida de qualidade de teste |
**Meta**: 80% de cobertura de linha é um padrão razoável. Mas a cobertura é um guia, não uma meta – 100% de cobertura com afirmações fracas é pior do que 70% de cobertura com testes completos.
---

## Integração e testes contínuos
| Prática | Descrição |
|----------|------------|
| **Execute todos os testes unitários em cada commit** | Feedback rápido; captura regressões imediatamente |
| **Execute testes de integração em PR** | Detecta problemas que os testes unitários não percebem |
| **Execute testes E2E todas as noites ou ao mesclar com o principal** | Lento, mas completo |
| **Falha rápido** | Pare o pipeline na primeira falha para economizar tempo |
| **Política de teste instável** | Coloque em quarentena ou exclua testes instáveis ​​imediatamente; nunca ignore |
| **Paralelização de teste** | Execute testes em paralelo para reduzir o tempo de CI |
---

## Dicas Práticas
- **Nomeie os testes com clareza.**`test_calculates_tax_for_high_earner`informa o que quebrou. `test_1`não diz nada.
- **Uma afirmação por teste (quando prático).** Facilita o diagnóstico de falhas.
- **Não teste detalhes de implementação.** Teste o comportamento. Se você refatorar os internos, os testes não deverão falhar.
- **Evite testar código de terceiros.** Simule bibliotecas externas; teste a interação do seu código com eles.
- **Faça testes rapidamente.** Se seu conjunto de testes levar 10 minutos, os desenvolvedores irão parar de executá-lo. Otimize incansavelmente.
- **Excluir testes mortos.** Testes que sempre passam ou testam o código removido são ruídos.
- **Trate o código de teste como código de produção.** Ele deve ser legível, fácil de manter e bem estruturado.
---

## Resumo
O teste não é opcional – é como você cria um software que não quebra. A pirâmide de testes orienta você em direção a muitos testes unitários rápidos, alguns testes de integração e alguns testes E2E. TDD e BDD fornecem abordagens estruturadas. A zombaria isola unidades para teste. A cobertura do código mede a amplitude, mas não a profundidade. O princípio mais importante é este: se não for testado, está quebrado – você simplesmente não sabe disso ainda.