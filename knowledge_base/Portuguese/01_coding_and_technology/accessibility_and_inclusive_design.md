---
# Metadata
title: "Accessibility and Inclusive Design"
description: "WCAG, inclusive UX, assistive technology, accessible coding"
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
tags: [accessibility, inclusive, design, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Acessibilidade e Design Inclusivo
Acessibilidade (muitas vezes abreviada como a11y) é a prática de tornar o software utilizável por todos – incluindo pessoas com deficiências visuais, auditivas, motoras, cognitivas e neurológicas. Não é bom ter; é um requisito legal em muitas jurisdições, uma obrigação moral e uma boa engenharia. Software acessível é melhor para todos, porque as decisões de design que ajudam os usuários com deficiência – estrutura clara, navegação por teclado, contraste suficiente, texto legível – melhoram a experiência para todos os usuários.
---

## Quem se beneficia com a acessibilidade?
| Tipo de deficiência | Exemplos | Tecnologia Assistiva |
|----------------|---------|---------------------|
| **Visuais** | Cegueira, baixa visão, daltonismo | Leitores de tela (JAWS, NVDA, VoiceOver); lupas; modos de alto contraste |
| **Auditivo** | Surdez, deficiência auditiva | Legendas; transcrições; alertas visuais |
| **Motor** | Destreza limitada, paralisia, tremor | Navegação apenas com teclado; controle de voz; trocar dispositivos; rastreamento ocular |
| **Cognitivo** | Dislexia, TDAH, autismo, problemas de memória | Linguagem clara; navegação consistente; distrações reduzidas |
| **Temporário** | Braço quebrado, luz solar intensa, ambiente barulhento | Mesmas acomodações que as deficiências permanentes |
| **Situacional** | Segurando um bebê, dirigindo, com uma mão ocupada | Interfaces de voz; grandes alvos tácteis |
**Informações importantes**: os recursos de acessibilidade projetados para usuários com deficiência ajudam a todos. Os cortes de meio-fio (rampas nas calçadas) foram projetados para cadeiras de rodas, mas são usados ​​por pais com carrinhos de bebê, entregadores com carrinhos e viajantes com bagagem.
---

## Acessibilidade na Web (WCAG)
As Diretrizes de Acessibilidade para Conteúdo da Web (WCAG) são o padrão internacional para acessibilidade na web.
### Princípios WCAG (POUR)
| Princípio | Requisito |
|-----------|------------|
| **Perceptível** | As informações devem ser apresentáveis ​​de forma que os usuários possam percebê-las (alternativas de texto, legendas, layout adaptável) |
| **Operável** | A interface deve ser navegável e utilizável (teclado acessível, tempo suficiente, sem conteúdo indutor de convulsões) |
| **Compreensível** | A informação e a operação devem ser compreensíveis (legíveis, previsíveis, com assistência de entrada) |
| **Robusto** | O conteúdo deve funcionar com tecnologias assistivas atuais e futuras |
### Níveis de conformidade WCAG
| Nível | Requisitos | Alvo típico |
|-------|------------|---------------|
| **A** | Nível mínimo; 30 critérios de sucesso | Mínimo legal em algumas jurisdições |
| **AA** | Aborda as barreiras mais comuns | Meta padrão para a maioria das organizações |
| **AAA** | Nível mais alto; nem todo conteúdo consegue alcançá-lo | Conteúdo especializado; sites educativos |
### Principais critérios de sucesso (nível AA)
| Critério | Requisito | Como conseguir |
|-----------|-------------|---------------|
| **1.1.1 Conteúdo não textual** | Todas as imagens possuem alternativas de texto |  Atributos `alt`; `aria-label`para ícones |
| **1.3.1 Informações e relacionamentos** | Estrutura transmitida programaticamente | HTML semântico; títulos; listas; marcos |
| **1.4.3 Contraste (mínimo)** | O texto tem taxa de contraste de pelo menos 4,5:1 | Teste com verificadores de contraste; escolha paletas de cores acessíveis |
| **1.4.4 Redimensionar texto** | O texto pode ser redimensionado para 200% sem perda | Use unidades relativas (rem, em); design responsivo |
| **2.1.1 Teclado** | Todas as funcionalidades disponíveis via teclado | Sem armadilhas de teclado; indicadores de foco visíveis |
| **2.4.3 Ordem de foco** | A ordem do foco preserva o significado e a operabilidade | Ordem lógica de tabulação; A ordem do DOM corresponde à ordem visual |
| **2.4.7 Foco visível** | O foco do teclado é indicado visualmente | Estilos CSS `:focus-visible`; nunca`outline: none`sem reposição |
| **3.3.2 Etiquetas ou instruções** | As entradas possuem rótulos |  Elementos `<label>`; `aria-label`|
| **4.1.2 Nome, função, valor** | Os componentes da UI têm nomes e funções acessíveis | Atributos ARIA; HTML semântico |
---

## ARIA (Aplicativos Ricos para Internet Acessíveis)
ARIA adiciona informações de acessibilidade a elementos HTML que não possuem semântica integrada.
### Funções ARIA
| Função | Finalidade | Exemplo |
|------|---------|---------|
| `button`| Identifica um elemento como um botão | Um`<div>`estilizado como um botão |
| `dialog`| Diálogo modal ou não modal | Componentes modais personalizados |
| `tablist`/`tab`/`tabpanel`| Interface da guia | Componentes de guias personalizadas |
| `alert`| Mensagem importante que aparece dinamicamente | Notificações de erro |
| `progressbar`| Indicador de progresso | Carregando estados |
| `menu`/`menuitem`| Navegação nos menus | Menus suspensos |
###ARIA Atributos
| Atributo | Finalidade | Exemplo |
|-----------|---------|---------|
| `aria-label`| Nome acessível quando não há texto visível | Botão apenas de ícone:`aria-label="Search"`|
| `aria-describedby`| Vincula o elemento à sua descrição | Campo de formulário com texto de ajuda |
| `aria-expanded`| Indica se uma seção está expandida | Acordeão; menu suspenso |
| `aria-hidden`| Oculta elemento da tecnologia assistiva | Ícones decorativos |
| `aria-live`| Anuncia mudanças dinâmicas de conteúdo | Atualizações ao vivo; notificações |
| `aria-disabled`| Indica que o elemento está desabilitado | Botões acinzentados |
### A Primeira Regra do ARIA
> **Não use ARIA se você puder usar HTML nativo.** Um`<button>`já está acessível. Um`<div role="button">`requer que você adicione manualmente o manuseio do teclado, gerenciamento de foco e suporte para leitor de tela. Use HTML semântico primeiro; ARIA somente quando os elementos nativos não conseguem fazer o trabalho.
---

## Navegação pelo teclado
| Chave | Comportamento Esperado |
|-----|-------------------|
| **Guia** | Mover o foco para o próximo elemento interativo |
| **Shift + Tabulação** | Mover o foco para o elemento interativo anterior |
| **Entrar / Espaço** | Ative o elemento em foco (botão, link) |
| **Teclas de seta** | Navegue dentro dos componentes (menus, abas, grupos de rádio) |
| **Fuga** | Fechar uma caixa de diálogo, menu ou popover |
| **Início / Fim** | Ir para o primeiro/último item de uma lista |
### Armadilhas comuns de teclado
| Problema | Correção |
|--------|-----|
| O foco entra em um componente, mas não consegue sair | Certifique-se de que Tab mova o foco; lidar com Fuga |
| Modal não prende o foco | O foco deve circular dentro do modal; retornar ao acionamento no fechamento |
| Componentes personalizados não respondem ao teclado | Adicione manipuladores de teclas para Enter, Espaço, setas |
---

## Cores e Design Visual
| Diretriz | Requisito |
|-----------|------------|
| **Relação de contraste** | 4,5:1 para texto normal; 3:1 para texto grande (18pt+ ou 14pt+ negrito) |
| **Não confie apenas na cor** | Use ícones, texto ou padrões além de cores |
| **Indicadores de foco** | Sempre visível; alto contraste; nunca removido sem substituição |
| **Redimensionamento de texto** | Layout deve funcionar com zoom de 200% |
| **Responsivo** | O conteúdo deve refluir com largura de 320px (móvel) |
### Considerações sobre daltonismo
| Tipo | Cores afetadas | Dica de design |
|------|-----------------|------------|
| **Deuteranopia** | Vermelho-verde (mais comum) | Não use vermelho/verde para transmitir status; usar ícones + cor |
| **Protanopia** | Vermelho-verde | Igual ao acima |
| **Tritanopia** | Azul-amarelo | Não usar azul/amarelo como único diferencial |
---

## Testando acessibilidade
| Método | Ferramenta | O que pega |
|--------|------|----------------|
| **Verificação automatizada** | machado, farol, WAVE | Texto alternativo ausente; questões de contraste; Erros ARIA |
| **Teste de teclado** | Manual: desconecte o mouse, use apenas o teclado | Ordem de foco; armadilhas de teclado; manipuladores desaparecidos |
| **Teste do leitor de tela** | NVDA (grátis), VoiceOver (macOS), JAWS | Etiquetas ausentes; estrutura deficiente; mudanças não anunciadas |
| **Teste de zoom** | Zoom do navegador para 200%, 400% | Quebra de layout; texto recortado; problemas de estouro |
| **Contraste de cores** | Verificador de contraste WebAIM, plugin Stark | Rácios de contraste insuficientes |
| **Teste de usuário** | Teste com usuários deficientes | Barreiras do mundo real que as ferramentas automatizadas ignoram |
---

## Requisitos Legais
| Direito | Região | Requisitos |
|-----|--------|------------|
| **ADA** (Lei dos Americanos Portadores de Deficiência) | EUA | Sites de alojamentos públicos devem ser acessíveis |
| **Seção 508** | EUA (federal) | As TIC das agências federais devem ser acessíveis |
| **EAA** (Lei Europeia da Acessibilidade) | UE (2025+) | Os produtos e serviços devem cumprir requisitos de acessibilidade |
| **EN 301 549** | UE | Norma técnica para acessibilidade das TIC |
| **ACA** (Lei de Acessibilidade do Canadá) | Canadá | Indústrias governamentais e regulamentadas |
| **Lei da Igualdade de 2010** | Reino Unido | Os prestadores de serviços devem fazer ajustes razoáveis ​​|
---

## Acessibilidade móvel
| Plataforma | Diretrizes | Ferramentas principais |
|----------|-----------|-----------|
| **iOS** | Diretrizes de Interface Humana da Apple (seção Acessibilidade) | VozOver; Tipo Dinâmico; Controle de interruptor |
| **Android** | Diretrizes de acessibilidade do Android | TalkBack; Acesso com interruptor; Selecione para falar |
| Preocupação móvel | Solução |
|---------------|----------|
| **Alvos de toque** | Mínimo 44×44 pontos (iOS) / 48×48 dp (Android) |
| **Suporte para leitor de tela** | Descrições de conteúdo; etiquetas de acessibilidade |
| **Sensibilidade ao movimento** | Respeite `prefers-reduced-motion`; evite animações de reprodução automática |
| **Dimensionamento de texto dinâmico** | Suporta tamanhos de fonte do sistema; usar unidades de texto escaláveis ​​|
---

## Resumo
Acessibilidade não é um recurso que você adiciona no final — é um princípio de design que deve informar todas as decisões desde o início. Use HTML semântico. Certifique-se de que a navegação pelo teclado funcione. Mantenha contraste de cores suficiente. Fornece alternativas de texto para conteúdo não textual. Teste com leitores de tela e usuários reais com deficiência. O resultado é um software que funciona melhor para todos — não apenas para aqueles com deficiência, mas também para aqueles com deficiências temporárias, limitações situacionais, dispositivos mais antigos, conexões lentas e milhares de outras maneiras pelas quais o uso no mundo real difere do ambiente idealizado pelo desenvolvedor.