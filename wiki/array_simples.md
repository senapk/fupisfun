# Array Simples

<!-- toc -->
- [Introdução](#introdução)
- [Declarando e Inicializando Arrays](#declarando-e-inicializando-arrays)
- [Acessando Elementos de um Array](#acessando-elementos-de-um-array)
- [Alterando Elementos de um Array](#alterando-elementos-de-um-array)
- [Percorrendo um Array](#percorrendo-um-array)
- [Extra](#extra)
  - [Arrays de Tamanho "Variável"](#arrays-de-tamanho-variável)
<!-- toc -->

## Introdução

Os arrays simples são estruturas de dados essenciais em C++. Eles permitem armazenar múltiplos elementos do mesmo tipo em uma única variável. Por exemplo, se precisarmos armazenar 5 números inteiros, podemos criar 5 variáveis inteiras.

```c++
int numero1;
int numero2;
int numero3;
int numero4;
int numero5;
```

Mas isso não é prático. Em vez disso, podemos criar um array capaz de armazenar 5 inteiros em uma única variável. Para diferenciar os 5 inteiros, cada um deles possui um índice, que é um número inteiro que identifica a posição do elemento no array. O primeiro elemento do array tem índice 0, o segundo elemento tem índice 1 e assim por diante. O último elemento de um array de tamanho `N` tem índice `N-1`. No nosso exemplo com 5 elementos, o primeiro elemento tem índice 0 e o último elemento tem índice 4.

## Declarando e Inicializando Arrays

Para declarar um array, precisamos de duas informações:

- O tipo dos elementos do array: `int`, `double`, `char`, etc. Um array só pode armazenar elementos do mesmo tipo, não é possível armazenar elementos de tipos diferentes em um mesmo array.
- O tamanho do array: quantos elementos o array pode armazenar.

A sintaxe para declarar um array é:

```c++
tipo nome[tamanho];
```

Por exemplo, para declarar um array de 5 inteiros, usamos:

```c++
int numeros[5];
```

O array `numeros` possui 5 espaços para armazenar inteiros. Esse tamanho é fixo e não pode ser alterado depois que o array é criado.

Perceba que os espaços do array ainda não possuem valores definidos, pois eles não foram inicializados. Dessa forma, podem conter qualquer valor (**lixo de memória**).

Para inicializar um array e resolver isso, podemos usar uma **lista de inicialização**. A lista de inicialização é uma sequência de valores separados por vírgula entre chaves. O primeiro valor da lista de inicialização é atribuído ao primeiro elemento do array, o segundo valor da lista de inicialização é atribuído ao segundo elemento do array e assim por diante.

```c++
int numeros[5] {1, 2, 3, 4, 5};
```

> **Dica:** Se a lista de inicialização tiver menos elementos do que o tamanho do array, os elementos restantes são inicializados com o valor 0.
>
> ```cpp
> int numeros[5] {1, 2, 3}; // numeros = {1, 2, 3, 0, 0}
> ```
>
> **Atençao:** Se a lista de inicialização tiver mais elementos do que o tamanho do array, o compilador gera um erro.

## Acessando Elementos de um Array

Para acessar um elemento de um array, usamos o nome do array seguido do índice do elemento entre colchetes. Por exemplo, para acessar o primeiro elemento do array `numeros` e guardar o valor em uma variável `primeiro`, usamos:

```c++
int primeiro = numeros[0]; // numeros tem 5 elementos, o primeiro tem índice 0
```

Para acessar o último elemento do array `numeros` e guardar o valor em uma variável `ultimo`, usamos:

```c++
int ultimo = numeros[4]; // numeros tem 5 elementos, o último tem índice 4
```

## Alterando Elementos de um Array

Os elementos de um array podem ser alterados atribuindo um novo valor a eles. Por exemplo, para alterar o primeiro elemento do array `numeros` para o valor 10, usamos:

```c++
numeros[0] = 10;
```

## Percorrendo um Array

É possível percorrer um array usando um loop for, acessando cada elemento pelo índice. Para isso, precisa-se de um contador que sirva de indexador e varie de 0 até o tamanho do array menos 1. Por exemplo, para percorrer o array `numeros` e imprimir todos os seus 5 elementos, precisamos de um contador que varie de 0 até 4.

```c++
#include <iostream>

int main() {
    int numeros[5] {1, 2, 3, 4, 5};

    for(int i = 0; i < 5; i++) {
        std::cout << numeros[i] << '\n';
    }
}
```

## Extra

### Arrays de Tamanho "Variável"

O GCC permite criar arrays de tamanho "variável", em que o tamanho só é definido durante a execução do programa. Por exemplo, podemos criar um array de tamanho qualquer, lendo um valor pela entrada padrão:

```c++
int tamanho;
std::cin >> tamanho;
int numeros[tamanho];
```

Porém, isso não é permitido pelo padrão da linguagem C++. O GCC está usando uma extensão da linguagem C++ que permite criar arrays de tamanho variável. Porém, essa extensão não é padrão e é desencorajada. Para que o GCC adote um comportamento mais rígido e não permita essa extensão, podemos usar a flag `-pedantic-errors` na compilação.

```c++
g++ -pedantic-errors code.cpp
```

De qualquer forma, o tamanho de um array não pode ser alterado depois que ele é criado. Então, mesmo que o GCC permita criar arrays de tamanho variável, não é possível alterar o tamanho de um array depois que ele é criado. Se precisarmos de mais flexibilidade, podemos usar o tipo `std::vector`, ele é mais apropiado para isso.
