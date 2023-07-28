# O problema da divisão de dois inteiros

<!-- toc -->
- [Introdução](#introdução)
- [Exemplo do problema](#exemplo-do-problema)
- [Resolvendo o problema](#resolvendo-o-problema)
<!-- toc -->

## Introdução

Neste texto, abordaremos um problema comum nas operações aritméticas em C++: a divisão inteira. Mostraremos porque ela acontece e como podemos resolver.

## Exemplo do problema

```cpp
#include <iostream>

int main() {
    std::cout << 5 / 2 << '\n'; // 2

    int a = 5;
    int b = 2;
    std::cout << a / b << '\n'; // 2
}
```

O resultado **esperado** pelo aluno dessa operação é o valor 2.5, pois esse é o valor de `5 / 2`. No entanto, se você executar esse código verá que o resultado mostrado é 2.

Isso acontece por conta da forma como o C++ trata os tipos de dados dentro de uma operação aritmética. Observe que os dois operandos, 5 e 2, são números inteiros, dessa forma, a linguagem realizará apenas uma divisão inteira, que não resulta em casas decimais. Da mesma forma que você aprendeu quando estava na terceira série do ensino fundamental, o resultado de uma divisão inteira é o quociente da divisão, ou seja, a parte inteira do resultado.

## Resolvendo o problema

A abordagem de resolução desse problema é transformar pelo menos um dos valores em um tipo de dado de ponto flutuante, dessa forma a divisão não será inteira.

Dessa forma, precisamos realizar um cast como visto em [Tipos de dados e casts](tipos_primitivos.md) ou utilizar um dos argumentos como ponto flutuante.

```cpp
#include <iostream>

int main() {
    std::cout << 5 / (double) 2 << '\n'; // 2.5  fazendo cast
    std::cout << 5.0 / 2 << '\n';        // 2.5  usando um literal como ponto flutuante
    
    int a = 5;
    std::cout << a / 2.0 << '\n';        // 2.5
    int b = 2;
    std::cout << a / (double) b << '\n'; // 2.5
}
```
