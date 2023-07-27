# Introdução aos Tipos de Dados em C++

Em C++, os tipos de dados são fundamentais para a definição dos valores que uma variável pode armazenar e como esses valores serão tratados pelo programa. C++ possui diversos tipos de dados, cada um com características específicas. Nesta aula, vamos explorar os principais tipos de dados disponíveis na linguagem e a inferência de tipos usando o `auto`.

<!-- toc -->
- [Tipos de Dados Fundamentais](#tipos-de-dados-fundamentais)
- [Tipos Integrais](#tipos-integrais)
  - [`int`](#int)
  - [`char`](#char)
- [Tipos de Ponto Flutuante](#tipos-de-ponto-flutuante)
  - [`float`](#float)
  - [`double`](#double)
- [Tipo Booleano](#tipo-booleano)
  - [`bool`](#bool)
- [Uso do `auto` para Inferir Tipo](#uso-do-auto-para-inferir-tipo)
<!-- toc -->

## Tipos de Dados Fundamentais

Os tipos de dados fundamentais em C++ podem ser agrupados em três categorias principais:

1. **Tipos Integrais**: Armazenam valores inteiros. Exemplos: `int`, `char`, etc.

2. **Tipos de Ponto Flutuante**: Armazenam valores com casas decimais. Exemplos: `float`, `double`.

3. **Tipo Booleano**: Armazena valores `true` ou `false`. Exemplo: `bool`.

## Tipos Integrais

### `int`

- É usado para armazenar valores inteiros, como 1, 100, -50, etc;
- É um dos tipos de dados mais comuns em C++;
- A maioria das plataformas representa o tipo int usando 32 bits (4 bytes) de memória;
- Permite representar valores entre aproximadamente -2 bilhões a +2 bilhões.

Exemplo de declaração e atribuição de uma variável do tipo int:

```c++
int idade = 25;
```

### `char`

- É usado para armazenar caracteres individuais, como letras, dígitos ou símbolos;
- Cada caractere `char` ocupa 1 byte de memória e é representado usando aspas simples (' ').

Exemplo de declaração e atribuição de uma variável do tipo char:

```c++
char letra = 'a';
```

## Tipos de Ponto Flutuante

### `float`

- É usado para armazenar valores de ponto flutuante de precisão simples;
- Geralmente, representa 32 bits (4 bytes) de memória.

Exemplo de declaração e atribuição de uma variável do tipo float:

```c++
float altura = 1.75;
```

### `double`

- É usado para armazenar valores de ponto flutuante de dupla precisão;
- É mais preciso que o `float`, geralmente representado usando 64 bits (8 bytes) de memória;
- É adequado para aplicações que requerem alta precisão em cálculos com números decimais.

Exemplo de declaração e atribuição de uma variável do tipo double:

```c++
float pi = 3.14159265359;
```

## Tipo Booleano

### `bool`

- É usado para armazenar valores lógicos, representando true (verdadeiro) ou false (falso);
- Ocupa 1 byte de memória
- É útil para expressar condições e estados em um programa.

Exemplo de declaração e atribuição de uma variável do tipo bool:

```c++
bool eh_par = true;
```

## Uso do `auto` para Inferir Tipo

O C++11 introduziu o uso da palavra-chave `auto` para permitir a inferência de tipo de variáveis em tempo de compilação. Quando usamos `auto` ao declarar uma variável, o compilador automaticamente infere o tipo com base no valor atribuído à variável. Isso torna a declaração de variáveis mais concisa e legível.

Exemplo:

```c++
auto idade = 25; // O tipo da variável idade será inferido como int.
auto altura = 1.75; // O tipo da variável altura será inferido como double.
```
