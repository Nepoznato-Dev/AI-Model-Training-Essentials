<!-- 
Este arquivo foi traduzido automaticamente do inglês para o português.
Fonte: coding_languages.md
Nota: Termos técnicos, exemplos de código e nomes próprios podem permanecer em inglês.
Para melhorias de precisão, contribua com edições via pull requests.
-->

# Linguagens de Programação

## Python

Python é uma linguagem de programação de alto nível, interpretada, dinamicamente tipada e de propósito geral. Ela enfatiza a legibilidade e usa indentação significativa como delimitadores de bloco.

### Sintaxe Básica

```python
# Variáveis e tipos
nome: str = "Alice"
idade: int = 30
pontuacao: float = 9.5
ativo: bool = True

# Condicionais
if idade >= 18:
    print("adulto")
elif idade >= 13:
    print("adolescente")
else:
    print("criança")

# Loops
for i in range(5):
    print(i)

while ativo:
    ativo = False
```

### Funções e Anotações de Tipo

```python
def saudar(nome: str, vezes: int = 1) -> str:
    return (f"Olá, {nome}! " * vezes).strip()
```

### List Comprehensions

```python
quadrados = [x**2 for x in range(10)]
pares = [x for x in range(20) if x % 2 == 0]
```

### Classes e POO

```python
class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self) -> str:
        return f"Meu nome é {self.nome} e tenho {self.idade} anos."
```

## JavaScript

JavaScript é uma linguagem de programação interpretada, orientada a objetos e orientada a eventos, usada principalmente para desenvolvimento web no cliente e servidor.

### Sintaxe Básica

```javascript
// Variáveis e tipos
let nome = "Alice";
const idade = 30;
let pontuacao = 9.5;
let ativo = true;

// Condicionais
if (idade >= 18) {
    console.log("adulto");
} else if (idade >= 13) {
    console.log("adolescente");
} else {
    console.log("criança");
}

// Loops
for (let i = 0; i < 5; i++) {
    console.log(i);
}

while (ativo) {
    ativo = false;
}
```

### Funções

```javascript
function saudar(nome, vezes = 1) {
    return `Olá, ${nome}! `.repeat(vezes).trim();
}

// Função de seta
const saudarArrow = (nome, vezes = 1) => {
    return `Olá, ${nome}! `.repeat(vezes).trim();
};
```

### Manipulação de Arrays

```javascript
const numeros = [1, 2, 3, 4, 5];
const quadrados = numeros.map(x => x ** 2);
const pares = numeros.filter(x => x % 2 === 0);
const soma = numeros.reduce((acc, x) => acc + x, 0);
```

## Java

Java é uma linguagem de programação compilada, orientada a objetos e multiplataforma, amplamente utilizada em aplicações empresariais e desenvolvimento Android.

### Sintaxe Básica

```java
// Variáveis e tipos
String nome = "Alice";
int idade = 30;
double pontuacao = 9.5;
boolean ativo = true;

// Condicionais
if (idade >= 18) {
    System.out.println("adulto");
} else if (idade >= 13) {
    System.out.println("adolescente");
} else {
    System.out.println("criança");
}

// Loops
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}

while (ativo) {
    ativo = false;
}
```

### Classes e POO

```java
public class Pessoa {
    private String nome;
    private int idade;
    
    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }
    
    public String apresentar() {
        return "Meu nome é " + nome + " e tenho " + idade + " anos.";
    }
}
```

## C++

C++ é uma linguagem de programação compilada, de alto desempenho e versátil, usada para sistemas, jogos e aplicações críticas.

### Sintaxe Básica

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    // Variáveis e tipos
    string nome = "Alice";
    int idade = 30;
    double pontuacao = 9.5;
    bool ativo = true;
    
    // Condicionais
    if (idade >= 18) {
        cout << "adulto" << endl;
    } else if (idade >= 13) {
        cout << "adolescente" << endl;
    } else {
        cout << "criança" << endl;
    }
    
    // Loops
    for (int i = 0; i < 5; i++) {
        cout << i << endl;
    }
    
    while (ativo) {
        ativo = false;
    }
    
    return 0;
}
```

## Fundamentos de Codificação (Agnóstico à Linguagem)

Os conceitos fundamentais de programação são comuns a todas as linguagens:

- **Variáveis**: Armazenamento de dados nomeados
- **Tipos de dados**: Definição da natureza dos dados (números, texto, booleanos, etc.)
- **Estruturas de controle**: Condicionais (if/else) e loops (for, while)
- **Funções**: Blocos de código reutilizáveis
- **Estruturas de dados**: Arrays, listas, dicionários, conjuntos
- **Programação orientada a objetos**: Classes, objetos, herança, polimorfismo
- **Tratamento de erros**: Try/catch, exceções
- **Entrada/Saída**: Leitura e escrita de dados

Esses conceitos fundamentais se aplicam independentemente da linguagem de programação escolhida. O domínio desses fundamentos permite aprender novas linguagens mais facilmente.
