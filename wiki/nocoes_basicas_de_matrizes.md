# Noções Básicas sobre Matrizes: Diagonais e Outras Propriedades

<!-- toc -->
- [Introdução](#introdução)
- [Diagonais em Matrizes](#diagonais-em-matrizes)
  - [Diagonal Principal]()
  - [Diagonal Secundária]()
- [Propriedades Adicionais](#propriedades-adicionais)
- [Exemplo de Diagonais e Propriedades](#exemplo-de-diagonais-e-propriedades)
<!-- toc -->

## Introdução

Uma matriz é uma estrutura de dados bidimensional que organiza elementos em linhas e colunas. Além das noções básicas de criação e manipulação de matrizes, existem propriedades específicas que podem ser exploradas para entender melhor os padrões e as relações entre os elementos. Neste texto, vamos explorar as diagonais em matrizes e algumas outras propriedades importantes.

## Diagonais em Matrizes

As diagonais de uma matriz são linhas formadas pelos elementos que estão na mesma posição ao longo de suas linhas e colunas. Existem duas diagonais principais:

### Diagonal Principal

É a diagonal que vai da posição superior esquerda à posição inferior direita da matriz. Ela é formada pelos elementos onde o índice da linha é igual ao índice da coluna.

O código abaixo imprime apenas os elementos da diagonal principal de uma matriz:

```cpp
#include <iostream>

using namespace std;

int main() {
    int TAMANHO = 4;
    int matriz[TAMANHO][TAMANHO] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12},
        {13, 14, 15, 16}
    };

    cout << "Elementos da diagonal principal:" << endl;
    for (int i = 0; i < TAMANHO; i++) {
        cout << matriz[i][i] << " ";
    } // Saída: 1 6 11 16
}

```

Como usamos a mesma variável para acessar a matriz, sempre teremos um índice de linha igual ao índice de coluna.

### Diagonal Secundária

É a diagonal que vai da posição superior direita à posição inferior esquerda da matriz. Nela, os elementos têm a soma dos índices da linha e da coluna igual ao tamanho da matriz menos 1.

O código abaixo imprime os elementos da diagonal secundária de uma matriz:

```cpp
#include <iostream>

using namespace std;

int main() {
    int TAMANHO = 4;
    int matriz[TAMANHO][TAMANHO] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12},
        {13, 14, 15, 16}
    };

    cout << "Elementos da diagonal secundária:" << endl;
    for (int i = 0; i < TAMANHO; i++) {
        cout << matriz[i][TAMANHO - 1 - i] << " ";
    } // Saída: 4 7 10 13
}

```

Nesse código usamos os valores `i` e `TAMANHO - 1 - i` para acessarmos os elementos da diagonal secundária. Como explicado acima, esses elementos estão em índices cuja soma é igual ao tamanho da matriz menos 1. Se somarmos `i + TAMANHO - 1 - i` observe que obtemos `TAMANHO - 1` que é justamente a definição da diagonal.

## Propriedades Adicionais

Além das diagonais, outras propriedades importantes em matrizes incluem:

1. **Matriz Identidade**: É uma matriz quadrada em que todos os elementos da diagonal principal são iguais a 1 e os demais elementos são iguais a 0.

2. **Matriz Simétrica**: Uma matriz é simétrica se ela é igual à sua própria transposta. Isso significa que os elementos refletem em relação à diagonal principal.

3. **Matriz Transposta**: A matriz transposta de uma matriz A é obtida trocando suas linhas por colunas, ou seja, os elementos na posição (i, j) de A passam para a posição (j, i) na matriz transposta.

4. **Matriz Triangular Superior/Inferior**: Uma matriz triangular superior tem todos os elementos abaixo da diagonal principal iguais a zero. Da mesma forma, uma matriz triangular inferior tem todos os elementos acima da diagonal principal iguais a zero.

## Exemplo de Diagonais e Propriedades

Considere a seguinte matriz 3x3 como exemplo:

```
| 5  8  2 |
| 4  6  9 |
| 1  3  7 |
```

- A diagonal principal é formada pelos elementos 5, 6 e 7.
- A diagonal secundária é formada pelos elementos 2, 6 e 1.
- Esta matriz não é simétrica, pois não é igual à sua transposta.
- Ela é uma matriz triangular superior, pois todos os elementos abaixo da diagonal principal são zeros.

Explorar essas propriedades permite compreender melhor as relações entre os elementos de uma matriz e é fundamental para diversas aplicações em matemática, ciência da computação e outras disciplinas.