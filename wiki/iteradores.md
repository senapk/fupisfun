# Iteradores

<!-- toc -->
- [Introdução](#introdução)
- [Sintaxe](#sintaxe)
- [O método begin()](#o-método-begin)
- [O método end()](#o-método-end)
- [O operador de desreferência](#o-operador-de-desreferência)
- [O operador de incremento/decremento](#o-operador-de-incrementodecremento)
- [O operador de soma/subtração](#o-operador-de-somasubtração)
- [O operador de igualdade/desigualdade](#o-operador-de-igualdadedesigualdade)
- [O operador de atribuição](#o-operador-de-atribuição)
<!-- toc -->

## Introdução

Iteradores são objetos que fornecem uma maneira de acessar os elementos de uma coleção de dados sequencialmente, permitindo a iteração (percorrimento) de todos os elementos de uma coleção. Eles são uma abstração que facilita a tarefa de percorrer e manipular os elementos de uma coleção, independentemente do tipo de coleção ou de como ela é armazenada na memória. Sendo assim, funcionam com uma grande variedade de coleções, como listas, vetores, mapas, etc.

Os iteradores atuam como "ponteiros" para elementos em uma coleção, permitindo que você percorra a coleção, acesse seus elementos e realize operações sobre eles. Eles fornecem uma interface consistente para avançar, retroceder e acessar os elementos da coleção, sem a necessidade de conhecer os detalhes internos da implementação da coleção.

## Sintaxe

A sintaxe para a criação de um iterador em C++ é a seguinte:

```text
tipo_da_colecao::iterator nome_do_iterador;
```

Onde:

- **tipo_da_colecao**: é o tipo da coleção que você deseja percorrer. Por exemplo, `vector`, `list`, `map`, etc.
- **nome_do_iterador**: é o nome que você deseja dar ao iterador.

Por exemplo, para criar um iterador para percorrer um vector de inteiros, você pode fazer:

```cpp
vector<int>::iterator it;
```

Esse iterador não está apontando para nenhum elemento do vector, ele está apenas declarado. Para que ele aponte para um elemento, você precisa inicializá-lo com o endereço de um elemento dentro do vector. Por exemplo, podemos inicializá-lo com o endereço do primeiro elemento do vector usando o método `begin()` de alguma coleção existente.

## O método begin()

O método `begin()` pertence às instâncias de coleções, como variáveis do tipo `vector`, `list`, `map`, etc. Ele retorna um iterador apontando para o primeiro elemento da coleção.

Por exemplo, imagine que você tem um vector de inteiros chamado `vetor`. Ao chamar o método `begin()` desse vetor, você obtém um iterador apontando para o primeiro elemento da coleção. Você pode então atribuir esse iterador a uma variável do tipo `vector<int>::iterator` para guardar o iterador.

```cpp
vector<int> vetor {1, 2, 3, 4, 5};
vector<int>::iterator it {vetor.begin()};
```

Dessa forma, a variável `it` está apontando para o primeiro elemento do vector `vetor`.

## O método end()

O método `end()`, assim como o `begin()`, também pertence às instâncias de coleções. Ele retorna um iterador apontando para o elemento seguinte ao último elemento da coleção. Esse elemento seguinte ao último elemento não existe, mas o iterador aponta para ele mesmo assim. Isso é útil para saber quando você chegou ao final da coleção.

Por exemplo, imagine que você tem um vector de inteiros chamado `vetor`. Ao chamar o método `end()` desse vetor, você obtém um iterador apontando para o elemento seguinte ao último elemento da coleção. Se a coleção tem 5 elementos, o iterador aponta para o elemento 6, que não existe. Você pode então atribuir esse iterador a uma variável do tipo `vector<int>::iterator`.

```cpp
vector<int> vetor {1, 2, 3, 4, 5};
vector<int>::iterator it {vetor.end()};
```

Dessa forma, a variável `it` está apontando para o elemento seguinte ao último elemento do vector `vetor`.

## O operador de desreferência

O operador de desreferência `*` é usado para acessar o elemento apontado pelo iterador. Por exemplo, se você tem um iterador `it` apontando para um elemento de um vector, você pode acessar o elemento usando o operador de desreferência `*it`.

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> vetor {1, 2, 3, 4, 5};
    std::vector<int>::iterator it {vetor.begin()};
    std::cout << *it << std::endl; // 1
}
```

## O operador de incremento/decremento

O operador de incremento `++` é usado para avançar o iterador para o próximo elemento da coleção. O operador de decremento `--` é usado para retroceder o iterador para o elemento anterior da coleção.

Por exemplo, se você tem um iterador `it` apontando para um elemento de um vector, você pode avançar o iterador para o próximo elemento usando o operador de incremento `++it`. Você pode retroceder o iterador para o elemento anterior usando o operador de decremento `--it`.

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> vetor {1, 2, 3, 4, 5};
    std::vector<int>::iterator it {vetor.begin()};

    std::cout << *it << std::endl; // 1

    ++it; // avança o iterador para o próximo elemento
    std::cout << *it << std::endl; // 2

    --it; // retrocede o iterador para o elemento anterior
    std::cout << *it << std::endl; // 1
}
```

## O operador de soma/subtração

O operador de soma `+` é usado para avançar o iterador para uma posição específica da coleção. O operador de subtração `-` é usado para retroceder o iterador para uma posição específica da coleção.

Por exemplo, se você tem um iterador `it` apontando para um elemento de um vector, você pode avançar o iterador para uma posição específica usando o operador de soma `it + n`. Você pode retroceder o iterador para uma posição específica usando o operador de subtração `it - n`.

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> vetor {1, 2, 3, 4, 5};
    std::vector<int>::iterator it {vetor.begin()};

    std::cout << *it << std::endl; // 1

    it = it + 2; // avança o iterador em 2 posições
    std::cout << *it << std::endl; // 3

    it = it - 1; // retrocede o iterador em 1 posição
    std::cout << *it << std::endl; // 2
}
```

## O operador de igualdade/desigualdade

O operador de igualdade `==` é usado para verificar se dois iteradores apontam para a mesma posição na coleção. O operador de desigualdade `!=` é usado para verificar se dois iteradores apontam para posições diferentes na coleção.

Por exemplo, se você tem dois iteradores `it1` e `it2` apontando para elementos de um vector, você pode verificar se eles apontam para a mesma posição usando o operador de igualdade `it1 == it2`. Você pode verificar se eles apontam para posições diferentes usando o operador de desigualdade `it1 != it2`.

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> vetor {1, 2, 3, 4, 5};
    std::vector<int>::iterator it1 {vetor.begin()};
    std::vector<int>::iterator it2 {vetor.begin()};

    std::cout << (it1 == it2) << std::endl; // true (1)

    ++it1; // avança o iterador para o próximo elemento
    std::cout << (it1 == it2) << std::endl; // false (0)

    std::cout << (it1 != it2) << std::endl; // true (1)
}
```

Agora observe o seguinte código:

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> vetor {1, 1};
    std::vector<int>::iterator it1 {vetor.begin()};
    std::vector<int>::iterator it2 {vetor.begin() + 1};

    std::cout << (it1 == it2) << std::endl; // false (0)
}
```

Nesse caso, o iterador `it1` aponta para o primeiro elemento do vector, e o iterador `it2` aponta para o segundo elemento. Apesar de apontarem para valores iguais, eles apontam para posições diferentes na coleção, então o resultado da comparação `it1 == it2` é `false` (0). Para comparar os valores apontados pelos iteradores, você precisa usar o operador de desreferência `*`:

```cpp
*(it1) == *(it2)
```

## O operador de atribuição

O operador de atribuição `=` é usado para atribuir um iterador a outro. Por exemplo, se você tem dois iteradores `it1` e `it2` apontando para elementos de um vector, você pode atribuir o iterador `it2` ao iterador `it1` usando o operador de atribuição `it1 = it2`.

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> vetor {1, 2, 3, 4, 5};
    std::vector<int>::iterator it1 {vetor.begin()};
    std::vector<int>::iterator it2 {vetor.begin()};

    std::cout << *it1 << std::endl; // 1
    std::cout << *it2 << std::endl; // 1

    ++it2; // avança o iterador para o próximo elemento
    std::cout << *it1 << std::endl; // 1
    std::cout << *it2 << std::endl; // 2

    it1 = it2; // atribui o iterador it2 ao iterador it1
    std::cout << *it1 << std::endl; // 2
    std::cout << *it2 << std::endl; // 2
}
```

Ao atribuir o iterador `it2` ao iterador `it1`, o iterador `it1` passa a apontar para o mesmo elemento que o `it2`. É importante mencionar que nenhum elemento da coleção é modificado, apenas o iterador `it1` que passa a apontar para o mesmo elemento que o `it2`. Sendo assim, os valores da coleção continuam sendo [1, 2, 3, 4, 5], e não [2, 2, 3, 4, 5].

Para modificar o valor de um elemento da coleção, você precisa usar o operador de desreferência `*` e atribuir um novo valor ao elemento apontado pelo iterador. Por exemplo, se você tem um iterador `it` apontando para um elemento de um vector, você pode modificar o valor do elemento usando o operador de desreferência `*it = novo_valor`.

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> vetor {1, 2, 3, 4, 5};
    std::vector<int>::iterator it {vetor.begin()};

    std::cout << *it << std::endl; // 1

    *it = 10; // modifica o valor do elemento apontado pelo iterador
    std::cout << *it << std::endl; // 10
}
```
