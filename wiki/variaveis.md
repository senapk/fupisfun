# Variáveis

## Criação

Em C++, variáveis são espaços de memória que podem armazenar valores de diferentes tipos, como inteiros, números de ponto flutuante, caracteres, entre outros. As variáveis são essenciais para armazenar informações e manipulá-las durante a execução de um programa.

Para criar uma variável em C++, você precisa especificar o tipo da variável seguido pelo seu nome. Duas opções de sintaxe são possíveis:

```cpp
tipo_da_variável nome_da_variável = valor_inicial;
tipo_da_variável nome_da_variável {valor_inicial};
```

Por exemplo, para criar uma variável inteira chamada "idade" e uma variável ponto flutuante chamada "altura", você faria:

```cpp
int idade = 15;
double altura = 1.89;
```

## Boas práticas

A seguir, alguns pontos importantes para criar boas variáveis em C++:

- **Evite abreviações**

Procure usar nomes completos que reflitam claramente o que a variável representa. Evite abreviações confusas, a menos que sejam amplamente reconhecidas e aceitas.

Ao invés de `alt`, `lar`, `pro`, que alguém tem que adivinhar o que significa, melhor usar `altura`, `largura` e `profundidade` como nomes de variáveis.

Seu código não é uma equação de matemática, mesmo que a descrição da questão ou problema que você está resolvendo utilize um modelo matemático para representar a regras de lógica, no seu código você deve utilizar nomes de variáveis que façam sentido independente do contexto.

- **Inicialize suas variáveis**

Sempre inicialize suas variáveis com um valor adequado antes de usá-las. Variáveis não inicializadas podem conter lixo de memória e levar a comportamentos inesperados. Existem algumas formas de inicializar:

```cpp

int idade; //errado, não está inicializada

//-----------

int idade = 0; //certo, e faz conversões de tipos se necessário

//-----------

int idade {0}; //melhor ainda, mas não faz conversões de tipos

//-----------

int idade {}; // indica que você está criando agora usando o
              // valor padrão do tipo e vai ler a variável em 
              // seguida, normalmente do cin.
std::cin >> idade;
```

- **Utilize snake_case**

Em Fundamentos de Programação usando C++, utilize o modo de nomenclatura snake_case. Ele consiste em utilizar letras minúsculas e depois o `_` para separar as palavras.

```cpp
int melhor_idade {0};
double peso_medio = 0.0;
char primeira_letra = 'a';
```
