# Variáveis

## Criação

Em C++, variáveis são espaços de memória que podem armazenar valores de diferentes tipos, como inteiros, números de ponto flutuante, caracteres, entre outros. As variáveis são essenciais para armazenar informações e manipulá-las durante a execução de um programa.

Para criar uma variável em C++, você precisa especificar o tipo da variável seguido pelo seu nome. A sintaxe geral é a seguinte:

```cpp
tipo_da_variavel nome_da_variavel = valor_inicial;
```

Por exemplo, para criar uma variável inteira chamada "idade" e uma variável ponto flutuante chamada "altura", você faria:

```cpp
int idade = 15;
double altura = 1.89;
```

## Boas práticas

A seguir, alguns pontos importantes para criar boas variáveis em C++:

1. **Escolha nomes descritivos**: Nomeie suas variáveis de forma clara e significativa, para que o propósito da variável seja evidente para qualquer pessoa que leia seu código. Evite nomes genéricos como "a", "b" ou "x".

2. **Inicialize suas variáveis**: Sempre inicialize suas variáveis com um valor adequado antes de usá-las. Variáveis não inicializadas podem conter lixo de memória e levar a comportamentos inesperados. Existem algumas formas de inicializar:

```cpp
int idade; //errado
int idade = 0; //certo
int idade {0}; //melhor ainda
int idade {}; //indica que você está criando agora usando o valor padrão do tipo e vai ler a variável em seguida, normalmente do cin.
```

3. **Utilize snake_case**: Em Fundamentos de Programação usando c++, utilize o modo de nomenclatura snake_case. Ele consiste em utilizar letras minúsculas e depois o _ para separar as palavras.

```cpp
int melhor_idade {0};
double peso_medio = 0.0;
char primeira_letra = 'a';
```

3. **Evite abreviações obscuras**: Procure usar nomes completos que reflitam claramente o que a variável representa. Evite abreviações confusas, a menos que sejam amplamente reconhecidas e aceitas. Ao invés de alt, lar, pro, melhor usar largura, altura e profundidade como nomes de variáveis.

Criar boas variáveis é uma prática importante para tornar o seu código mais legível, compreensível e mais fácil de manter ao longo do tempo.

## Erros

- Qual erro acontece quando:
  - Você declara duas vezes a mesma variável no mesmo escopo?
  - Você tenta utilizar uma variável que não foi criada ou com um nome diferente?
  - Você esquece o tipo da variável?
  - Você cria uma variável, mas não a utiliza pra nada?

## Avisando que você não vai utilizar uma variável

Você pode usar o (void) antes da variável para avisar que não vai utilizar a variável.

```cpp

int main() {
  int idade = 0;
  (void) idade; //não vou utilizar idade pra nada.
}

```
