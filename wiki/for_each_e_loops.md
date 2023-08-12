# For-each e loops com referência

<!-- toc -->
- [Introdução](#introdução)
- [For-each](#for-each)
  - [Percorrendo um array](#percorrendo-um-array)
  - [Percorrendo um vector](#percorrendo-um-vector)
  - [Limitações](#limitações)
    - [Modificar os elementos](#modificar-os-elementos)
    - [Percorrer a coleção em ordem inversa](#percorrer-a-coleção-em-ordem-inversa)
    - [Percorrer apenas uma parte da coleção](#percorrer-apenas-uma-parte-da-coleção)
- [For-each com referência](#for-each-com-referência)
  - [Modificando os elementos de um array](#modificando-os-elementos-de-um-array)
- [O `auto`](#o-auto)
<!-- toc -->

## Introdução

Até o momento, vimos como percorrer listas usando loops tradicionais, como o `for` indexado. No entanto, existem outras formas de percorrer listas, como o `for-each`, que é mais simples e seguro. Nesta aula, veremos como usar o `for-each` e como ele se compara ao `for` indexado.

## For-each

Ao lidar com coleções de dados, como arrays e vectors, é comum precisarmos percorrer cada elemento para realizar alguma operação. Usando um loop for convencional, frequentemente precisamos gerenciar índices e contadores, o que pode tornar o código confuso e propenso a erros.

Os laços for-each foram introduzidos para simplificar esse processo, permitindo que iteremos diretamente sobre os elementos da coleção, sem se preocupar com detalhes de índices ou contadores.

A sintaxe básica do laço for-each é a seguinte:

```cpp
for (tipo_da_coleção elemento : coleção)
    instrução;
```

Quando a instrução do laço é encontrada, ele percorrerá cada elemento na coleção, atribuindo o valor do elemento atual à variável `elemento`. A instrução será executada uma vez para cada elemento da coleção.

### Percorrendo um array

Nesse exemplo, vamos percorrer um array de inteiros e imprimir cada elemento na tela.

```cpp
#include <iostream>

int main() {
    int array[] = {1, 2, 3, 4, 5};

    for(int elemento : array) {
        std::cout << elemento << ' ';
    } // 1 2 3 4 5

    std::cout << '\n';
}
```

### Percorrendo um vector

Nesse exemplo, vamos percorrer um vector de strings e imprimir cada elemento na tela.

```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
    std::vector<std::string> nomes = {"João", "Maria", "José"};

    for(std::string nome : nomes) {
        std::cout << nome << ' ';
    } // João Maria José

    std::cout << '\n';
}
```

### Limitações

O laço for-each é uma ferramenta muito útil, mas ele não é adequado para todas as situações e possui algumas limitações.

#### Modificar os elementos

Como o laço for-each atribui o valor do elemento atual à variável declarada na declaração_do_elemento, ou seja, ele faz uma cópia do elemento, se tentarmos modificar o elemento dentro do laço, a modificação não será refletida na coleção original, e sim na cópia.

Nesse exemplo, vamos tentar multiplicar cada elemento de um array por 2, usando um laço for-each. Ao final, vamos imprimir o array e perceber que os elementos não foram modificados.

```cpp
#include <iostream>

int main() {
    int array[] = {1, 2, 3, 4, 5};

    for(int elemento : array) {
        elemento *= 2;
    }

    for(int elemento : array) {
        std::cout << elemento << ' ';
    } // 1 2 3 4 5

    std::cout << '\n';
}
```

Essa limitação pode ser contornada usando referências, como veremos ainda nesta aula.

#### Percorrer a coleção em ordem inversa

O laço for-each sempre percorre a coleção do primeiro ao último elemento, ou seja, da esquerda para a direita. Não é possível percorrer a coleção da direita para a esquerda. Nessa situação, o laço for tradicional é mais adequado.

#### Percorrer apenas uma parte da coleção

O laço for-each sempre percorre a coleção inteira, então, a menos que uma instrução de controle de fluxo seja usada para interromper o laço, não é possível percorrer apenas uma parte da coleção. Nessa situação, o laço for tradicional também é o mais adequado.

## For-each com referência

Como vimos, o laço for-each faz uma cópia do elemento atual, o que pode ser um problema quando queremos modificar os elementos da coleção original. Outra situação em que isso pode ser um problema é quando a coleção contém elementos grandes, como objetos, pois fazer uma cópia de cada elemento pode ser custoso em termos de desempenho.

Felizmente, podemos contornar esse problema usando referências. Para isso, basta declarar a variável que armazenará o elemento como uma referência, usando o operador `&`.

```cpp
for(tipo_da_coleção& elemento : coleção)
    instrução;
```

Agora, a variável `elemento` é uma referência para o elemento atual, então, qualquer modificação feita na variável `elemento` será refletida na coleção original. Além disso, como não estamos mais fazendo uma cópia do elemento, o desempenho do laço é melhorado.

### Modificando os elementos de um array

Nesse exemplo, vamos multiplicar cada elemento de um array por 2, usando um laço for-each com referência. Ao final, vamos imprimir o array e perceber que os elementos foram modificados.

```cpp
#include <iostream>

int main() {
    int array[] = {1, 2, 3, 4, 5};

    for(int& elemento : array) {
        elemento *= 2;
    }

    for(int elemento : array) {
        std::cout << elemento << ' ';
    } // 2 4 6 8 10

    std::cout << '\n';
}
```

## O `auto`

Até o momento, sempre declaramos a variável que armazenará o elemento como o tipo da coleção. No entanto, isso não é obrigatório, pois o compilador é capaz de deduzir o tipo da variável automaticamente, usando o operador `auto`. O tipo da variável será o mesmo do tipo do valor que está sendo atribuído a ela, ou seja, o tipo do elemento da coleção.

```cpp
for(auto elemento : coleção)
    instrução;
```

Então, se quisermos, podemos usar o `auto` para simplificar a declaração da variável que armazenará o elemento. Por exemplo, se quisermos percorrer um array de inteiros com , podemos declarar a variável como `auto` em vez de `int`. O resultado será o mesmo. Também podemos usar o `auto` com referência.

```cpp
#include <iostream>

int main() {
    int array[] = {1, 2, 3, 4, 5};

    for(auto& elemento : array) {
        std::cout << elemento << ' ';
    } // 1 2 3 4 5

    std::cout << '\n';
}
```
