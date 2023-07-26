# Operações aritméticas

- [Introdução](#introdução)
- [Operadores Básicos](#operadores-básicos)
- [Ordem de Precedência](#ordem-de-precedência)
- [Exemplos](#exemplos)

## Introdução

Neste texto, vamos discutir os operadores aritméticos em C++, que são utilizados para realizar operações matemáticas em variáveis numéricas. Em C++, os operadores aritméticos são símbolos especiais que permitem a realização de adições, subtrações, multiplicações, divisões e outras operações matemáticas com valores numéricos.

## Operadores Básicos

Aqui estão os operadores aritméticos básicos em C++:

1. **Adição `+`**: O operador de adição é utilizado para somar dois valores.

2. **Subtração `-`**: O operador de subtração é utilizado para subtrair o valor do operando à direita do operando à esquerda.

3. **Multiplicação `*`**: O operador de multiplicação é utilizado para multiplicar dois valores.

4. **Divisão `/`**: O operador de divisão é utilizado para dividir o operando à esquerda pelo operando à direita.

5. **Módulo `%`**: O operador de módulo é utilizado para calcular o resto de uma divisão inteira entre o operando à esquerda e o operando à direita.

## Ordem de Precedência

É importante compreender a ordem de precedência dos operadores, pois ela determina a sequência em que as operações são realizadas. A ordem de precedência dos operadores aritméticos em C++ é a seguinte (do mais alto para o mais baixo):

1. Parênteses `()`
2. Multiplicação `*`, Divisão `/` e Módulo `%`
3. Adição `+` e Subtração `-`

Veja que em um cálculo como `4 / 2 + 1` a leitura padrão do compilador é `(4 / 2) + 1` pois a divisão possui uma precedência maior que a soma, caso você queria alterar esse ordem, sempre é possível adicionar parênteses: `4 / (2 + 1)`, assim a soma será efetuada antes da divisão.

## Exemplos

Vamos ver alguns exemplos de como utilizar os operadores aritméticos em C++:

```cpp
#include <iostream>

using namespace std;

int main() {
    int a = 10, b = 20, c = 5;

    // Exemplos de operações aritméticas
    int soma = a + b;       // Resultado: 30
    int subtracao = b - c;  // Resultado: 15
    int multiplicacao = a * c;  // Resultado: 50
    int divisao = b / a;    // Resultado: 2
    int resto = b % a;      // Resultado: 0

    // Utilizando parênteses para controlar a ordem de precedência
    int resultado1 = a + b * c;      // Resultado: 60 (pois a multiplicação é realizada antes)
    int resultado2 = (a + b) * c;    // Resultado: 150 (pois a adição é realizada antes)

    cout << "Soma: " << soma << endl;
    cout << "Subtração: " << subtracao << endl;
    cout << "Multiplicação: " << multiplicacao << endl;
    cout << "Divisão: " << divisao << endl;
    cout << "Resto: " << resto << endl;
    cout << "Resultado1: " << resultado1 << endl;
    cout << "Resultado2: " << resultado2 << endl;

    return 0;
}
```

Neste exemplo, demonstramos algumas operações aritméticas simples utilizando os operadores em C++. Também mostramos como os parênteses podem ser usados para controlar a ordem de precedência das operações.

Lembre-se de que os operadores aritméticos também podem ser aplicados em outros tipos numéricos, como ponto flutuante (float, double) e outros tipos personalizados, desde que o operador seja definido para esses tipos.
