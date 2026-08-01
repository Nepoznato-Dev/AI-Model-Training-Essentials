# Vieses Cognitivos e Falácias Lógicas

Este documento consolida vieses cognitivos, falácias lógicas e erros de raciocínio que afetam tanto a tomada de decisão humana quanto as saídas de sistemas de IA.

---

## Vieses cognitivos

Vieses cognitivos são padrões sistemáticos de desvio da racionalidade no julgamento e na tomada de decisão. Em desenvolvimento de software e sistemas de IA, eles podem levar a decisões ruins de design, requisitos falhos e comportamento enviesado do modelo.

### Viés de confirmação

**O que é:** tendência de buscar, interpretar e lembrar informações que confirmam crenças pré-existentes.

**Exemplo ruim em desenvolvimento:**
```python
# O desenvolvedor acredita que seu algoritmo é O(n log n)
def analyze_complexity(code):
    # Só busca evidências que apoiam O(n log n)
    sees_divide_and_conquer = True
    sees_recursion = True

    # Ignora evidências contraditórias
    nested_loop_present = True  # Na verdade torna O(n²)
    redundant_computation = True  # Adiciona fator extra

    return "O(n log n)"  # Conclusão errada
```

**Em revisões de código:**
```markdown
Desenvolvedor A (sênior): "Parece bom, ótimo trabalho!"
Desenvolvedor B (júnior): "Há vários problemas potenciais..."

A equipe aceita a revisão do Desenvolvedor A sem questionamento, mas questiona excessivamente o feedback do Desenvolvedor B.
```

**Mitigação:**
- buscar ativamente evidências contrárias
- usar revisões cegas
- incentivar opiniões divergentes
- documentar suposições explicitamente

### Viés de ancoragem

**O que é:** depender demais da primeira informação recebida.

**Exemplo ruim:**
```markdown
Gerente de projeto: "Essa funcionalidade deve levar cerca de 2 dias."
Desenvolvedor: (ancorado em 2 dias, embora a estimativa realista seja 5 dias)
"Certo, vou tentar terminar em 2 dias."

Resultado: trabalho apressado, dívida técnica e prazos perdidos mesmo assim.
```

**Mitigação:**
- obter várias estimativas independentes
- usar planning poker
- considerar intervalos em vez de números exatos
- consultar dados históricos

### Falácia do custo afundado

**O que é:** continuar um empreendimento por causa de recursos já investidos, mesmo quando abandonar seria melhor.

**Exemplo ruim:**
```markdown
"Já gastamos 6 meses construindo este framework próprio.
Não podemos trocar pelo padrão da indústria agora, mesmo que isso
nos economizasse tempo no longo prazo."
```

**Mitigação:**
- avaliar decisões pelo valor futuro, não pelo investimento passado
- reavaliar regularmente a viabilidade
- criar segurança psicológica para mudanças de rumo
- usar critérios objetivos para continuar/parar

### Heurística da disponibilidade

**O que é:** superestimar a importância de informações fáceis de acessar ou recentes.

**Exemplo ruim:**
```markdown
"Acabei de ler sobre um ataque de SQL injection, então devemos
priorizar a prevenção de SQL injection em vez de XSS, mesmo que
a nossa auditoria mostre que XSS é o maior risco."
```

**Mitigação:**
- decidir com base em dados
- consultar modelos de ameaça completos
- olhar taxas-base e estatísticas
- evitar viés de recência na priorização

### Efeito Dunning-Kruger

**O que é:** pessoas com pouca habilidade superestimam sua capacidade; especialistas podem subestimá-la.

**Exemplo ruim:**
```markdown
Desenvolvedor júnior: "Fiz um tutorial de Python.
Estou pronto para arquitetar toda a nossa plataforma de microsserviços."

Desenvolvedor sênior: "Conduzo sistemas distribuídos há 10 anos.
Provavelmente estou deixando passar algo importante neste design."
```

**Mitigação:**
- incentivar aprendizado contínuo
- implementar revisão por pares
- criar programas de mentoria
- promover humildade e curiosidade

---

## Falácias lógicas

Falácias lógicas são erros de raciocínio que enfraquecem a validade de um argumento. Modelos de IA podem produzir respostas que contenham essas falácias.

### Ad hominem (ataque à pessoa)

**O que é:** atacar a pessoa que faz o argumento em vez do argumento em si.

**Exemplo ruim:**
```markdown
"Essa revisão de código está errada porque o revisor é um desenvolvedor júnior."
```

**Por que está ruim:** a validade do feedback depende do conteúdo, não da senioridade do revisor.

### Apelo à autoridade

**O que é:** afirmar que algo é verdade só porque uma autoridade disse, sem evidências.

**Exemplo ruim:**
```markdown
"Essa arquitetura deve estar correta porque o Google a usa."
```

**Por que está ruim:** o que funciona para o Google em sua escala pode não funcionar para o seu caso.

### Falso dilema (pensamento preto-no-branco)

**O que é:** apresentar apenas duas opções quando existem mais.

**Exemplo ruim:**
```markdown
"Ou reescrevemos tudo em Rust ou aceitamos que nosso
código sempre será lento e cheio de bugs."
```

**Realidade:** existem muitas opções entre esses extremos.

### Escorregador íngreme

**O que é:** argumentar que um evento inevitavelmente levará a uma cadeia de consequências negativas.

**Exemplo ruim:**
```markdown
"Se permitirmos essa pequena dívida técnica, em breve
todo o nosso código ficará impossível de manter e a empresa vai falir."
```

**Por que está ruim:** assume uma progressão inevitável sem evidência.

### Raciocínio circular

**O que é:** usar a conclusão como premissa.

**Exemplo ruim:**
```markdown
"Nosso código é de alta qualidade porque escrevemos código bom."
```

### Falsa causa (post hoc ergo propter hoc)

**O que é:** presumir que, porque B veio depois de A, A causou B.

**Exemplo ruim:**
```markdown
"Implantamos a nova funcionalidade e depois vimos latência maior.
A nova funcionalidade deve estar causando a latência."
```

**Realidade:** correlação não implica causalidade.

### Espantalho

**O que é:** distorcer o argumento de alguém para facilitar o ataque.

**Exemplo ruim:**
```markdown
Desenvolvedor A: "Deveríamos adicionar mais testes para casos extremos."
Desenvolvedor B: "Então você quer que gastemos todo o nosso tempo
escrevendo testes e nunca lancemos funcionalidades?"
```

### Falácia do bandwagon

**O que é:** argumentar que algo é correto porque muitas pessoas acreditam nisso.

**Exemplo ruim:**
```markdown
"Todo mundo está usando Kubernetes, então nós também deveríamos."
```

**Por que está ruim:** popularidade não garante adequação.

---

## Falhas de raciocínio em IA

### Erros de lógica em múltiplas etapas

**Exemplo ruim:**
```
Usuário: Se todos os programadores escrevem código, e Alice escreve código, Alice é programadora?
Assistente: Sim, Alice deve ser programadora.
```

### Falhas de raciocínio matemático

**Exemplo ruim:**
```
Usuário: Um taco e uma bola custam $1,10 no total. O taco custa $1 a mais que a bola.
Quanto custa a bola?
Assistente: A bola custa $0,10.
```

### Erros de raciocínio causal

**Exemplo ruim:**
```
Usuário: Vendas de sorvete e afogamentos aumentam no verão. O sorvete causa afogamento?
Assistente: Sim, parece haver uma relação causal.
```

## Estratégias de melhoria

### Para a tomada de decisão humana
- buscar evidências contrárias
- usar dados e taxas-base
- registrar decisões e suposições
- fazer pré-mortems

### Para sistemas de IA
- decompor problemas complexos
- usar ferramentas externas para matemática e lógica
- verificar respostas antes de confiar nelas
- mostrar incerteza quando apropriado

## Tópicos relacionados
- vieses adicionais no desenvolvimento de software
- mais falácias lógicas
- ferramentas e estruturas para decisão e revisão

---

## Vieses cognitivos adicionais em desenvolvimento de software

### Viés do status quo
Preferir o estado atual mesmo quando mudanças seriam melhores.

### Viés de otimismo
Subestimar riscos e superestimar resultados positivos.

### Viés de sobrevivência
Focar apenas no que deu certo e ignorar falhas invisíveis.

### Erro fundamental de atribuição
Atribuir problemas a pessoas e não ao contexto ou ao sistema.

### Viés retrospectivo
Achar, depois do fato, que o resultado era óbvio.

## Mais falácias lógicas

### Apelo à novidade
Achar que algo é melhor só porque é novo.

### Apelo à tradição
Achar que algo é melhor só porque sempre foi feito assim.

### Tu quoque (apelo à hipocrisia)
Desviar a crítica apontando incoerência do crítico.

### Pergunta carregada
Fazer uma pergunta que pressupõe algo não comprovado.

### "No true Scotsman"
Redefinir o grupo para descartar contraexemplos.

### Falácia genética
Julgar algo pela origem, não pelo mérito.

### Falácia do meio-termo
Assumir que a posição intermediária é automaticamente correta.

## Vieses cognitivos em sistemas de IA

### Viés dos dados de treinamento
Os dados de treinamento refletem desigualdades e assimetrias do mundo real.

### Viés de automação
Confiar demais em sugestões automatizadas.

### Ilusão de compreensão
Achar que o modelo realmente entende quando apenas produz texto plausível.

## Estudos de caso

### Caso 1: viés de confirmação na escolha de arquitetura
### Caso 2: custo afundado em sistema legado
### Caso 3: heurística da disponibilidade em segurança

## Exercícios práticos

### Exercício de detecção de viés
### Identificação de falácias lógicas
### Técnica de pré-mortem

## Ferramentas e estruturas

### Modelo de diário de decisão
### Checklist de vieses
### Exercício de red team
