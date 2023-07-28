# Limites e Modificadores de Tipo

<!-- toc -->
- [Modificador `long`](#modificador-long)
- [Modificador `unsigned`](#modificador-unsigned)
- [Modificador `const`](#modificador-const)
<!-- toc -->

O C++ permite o uso de modificadores para ajustar os intervalos e limites de valores armazenados por certos tipos de dados. Os principais modificadores são:

- `long`: aumenta o intervalo de valores armazenados;
- `unsigned`: representa apenas valores não negativos;
- `const`: cria variáveis que não podem ser alteradas (constantes).

## Modificador `long`

Aumenta o intervalo de valores dos tipos, permitindo representar números maiores. O código abaixo vai uma variável do tipo `int` e uma do tipo `long int`, que podem representar valores maiores. Vai também utilizar as função `sizeof` para mostrar o tamanho em bytes de cada dado e a função `numeric_limits` para imprimir os limites máximos e mínimos de cada tipo.

```c++
#include <iostream>
#include <limits>

int main() {
    int i {};
    long int li {};

    std::cout << "Tamanho em bytes:\n";
    std::cout << "int " << sizeof(i) << '\n';       // 4
    std::cout << "long int " << sizeof(li) << '\n'; // 8

    std::cout << "Valor máximo:\n";
    std::cout << "int "           << std::numeric_limits<int>::max() << '\n';      //  2147483647
    std::cout << "long int "      << std::numeric_limits<long int>::max() << '\n'; //  9223372036854775807

    std::cout << "Valor mínimo:\n";
    std::cout << "int "           << std::numeric_limits<int>::min() << '\n';      // -2147483648
    std::cout << "long int "      << std::numeric_limits<long int>::min() << '\n'; // -9223372036854775808
}

```

Então fique atento, se o problema que você está resolvendo envolve números muito grandes, acima de 2 bilhões, você deve usar o tipo `long int` ou `long double`.

## Modificador `unsigned`

Indica que um tipo pode representar apenas valores não negativos (ou seja, valores positivos e zero).

- Pode ser usado nos tipos `int` e `char`;
- Isso permite que o intervalo de valores armazenados seja totalmente deslocado para o lado positivo, dobrando o intervalo de valores possíveis para o tipo de dado.

Exemplo:

```c++
int contador1;
unsigned int contador2;
```

Mas fica a dica, **evite** utilizar o tipo `unsigned int` para representar valores, pois isso pode causar problemas de lógica no seu programa. Por exemplo, se você declarar uma variável do tipo `unsigned int` e tentar atribuir um valor negativo a ela, o compilador não vai reclamar, mas o valor armazenado vai ser convertido e se tornará um valor muito grande, que pode causar problemas de lógica no seu programa.

```cpp
#include <iostream>

int main() {
    unsigned int x = 0;
    x -= 1;
    std::cout << x << '\n'; //4294967295
}

```

## Modificador `const`

Tornar uma variável imutável, ou seja, seu valor não pode ser alterado após a atribuição inicial. Isso é útil para garantir a integridade de variáveis que não devem ser modificadas durante a execução do programa.

- Pode ser usado em todos os tipos.

Exemplo:

```c++
const int quantidade = 10;
const float altura = 10.5;
const long double pi = 3.14159265359;
const unsigned char letra = 'a';
// O valor de nenhuma dessas variáveis (ou melhor, constantes) pode ser modificado após a atribuição inicial.
```
