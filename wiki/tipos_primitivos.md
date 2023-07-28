# Introdução aos Tipos de Dados em C++

<!-- toc -->
- [Tipos de Dados Fundamentais (ou Primitivos)](#tipos-de-dados-fundamentais-ou-primitivos)
- [Tipos Integrais](#tipos-integrais)
  - [`int`](#int)
  - [`char`](#char)
- [Tipos de Ponto Flutuante](#tipos-de-ponto-flutuante)
  - [`float`](#float)
  - [`double`](#double)
- [Tipo Booleano](#tipo-booleano)
  - [`bool`](#bool)
- [Uso do `auto` para inferir tipo](#uso-do-auto-para-inferir-tipo)
- [Curiosidade 1 - imprecisão](#curiosidade-1---imprecisão)
- [Curiosidade 2 - `sizeof`](#curiosidade-2---sizeof)
<!-- toc -->

Em C++, os tipos de dados são fundamentais para a definição dos valores que uma variável pode armazenar e como esses valores serão tratados pelo programa. C++ possui diversos tipos de dados, cada um com características específicas. Nesta aula, vamos explorar os principais tipos de dados disponíveis na linguagem e a inferência de tipos usando o `auto`.

## Tipos de Dados Fundamentais (ou Primitivos)

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

```cpp
float altura = 1.75f; //o f depois do número indica que é um float
```

### `double`

- É usado para armazenar valores de ponto flutuante de dupla precisão;
- É mais preciso que o `float`, geralmente representado usando 64 bits (8 bytes) de memória;
- É adequado para aplicações que requerem alta precisão em cálculos com números decimais.

Exemplo de declaração e atribuição de uma variável do tipo double:

```cpp
double pi = 3.14159265359;
```

Double é o valor padrão de ponto flutuante e, na dúvida, use sempre double.

## Tipo Booleano

### `bool`

- É usado para armazenar valores lógicos, representando true (verdadeiro) ou false (falso);
- Ocupa 1 byte de memória
- É útil para expressar condições e estados em um programa.

Exemplo de declaração e atribuição de uma variável do tipo bool:

```c++
bool eh_par = true;
```

## Uso do `auto` para inferir tipo

O C++11 introduziu o uso da palavra-chave `auto` para permitir a inferência de tipo de variáveis em tempo de compilação. Quando usamos `auto` ao declarar uma variável, o compilador automaticamente infere o tipo com base no valor atribuído à variável. Isso torna a declaração de variáveis mais concisa e legível.

Exemplo:

```c++
auto idade = 25; // O tipo da variável idade será inferido como int.
auto altura = 1.75; // O tipo da variável altura será inferido como double.
auto largura = 1.8f; // O tipo da variável largura será inferido como float.
auto eh_par = false; // O tipo da variável eh_par será inferido como bool.
auto letra = 'a'; // O tipo da variável letra será inferido como char.
```

## Curiosidade 1 - imprecisão

Só por curiosidade, o código abaixo mostra como o número 0.1 é representado em memória usando `float` e `double`.

```cpp
#include <iostream>
#include <iomanip>

int main (){
    std::cout << std::fixed;
    std::cout << "float : " << std::setprecision(20) << (float) 0.1 << '\n';
    std::cout << "double: " << std::setprecision(20) << (double) 0.1 << '\n';
}
```

O resultado é:

```txt
float : 0.10000000149011611938
double: 0.10000000000000000555
```

Dá pra ver como é a aproximação do número 0.1 em cada tipo de dado e como o tipo `double` é mais preciso.

## Curiosidade 2 - `sizeof`

A função `sizeof` pode ser utilizada para descobrir o tamanho em bytes de um tipo de dado. O código abaixo vai imprimir o tamanho em bytes de cada tipo de dado:

```cpp
#include <iostream>

int main() {
  std::cout << "int : " << sizeof(int) << '\n';
  std::cout << "char: " << sizeof(char) << '\n';
  std::cout << "float: " << sizeof(float) << '\n';
  std::cout << "double: " << sizeof(double) << '\n';
  std::cout << "bool: " << sizeof(bool) << '\n';
}
```
