# For Indexado

## Introdução

O for indexado é uma estrutura de repetião utilizada em programação para percorrer uma coleção de elementos, como um array ou um vector, de maneira controlada e eficiente. Esse for é chamado de indexado porque utiliza um índice para acessar os elementos da coleção. Isso significa que você tem controle não apenas sobre os elementos em si, mas também sobre suas posições na coleção.

## Sintaxe do For Indexado

A sintaxe básica do **for indexado** é a seguinte:

```cpp
for(int i = 0; i < tamanho; ++i) {
    // Corpo do loop
}
```

> `int i = 0`: Inicializa uma variável `i` como contador e define seu valor inicial como 0.
>
> `i < tamanho`: Define a condição para continuar o loop. Nesse caso, o loop continuará a ser executado enquanto `i` for menor que `tamanho`. O `tamanho` é a quantidade de elementos da coleção.
>
> `++i`: Incrementa o valor de `i` a cada iteração.

## Exemplo de For Indexado

Imagine que você tenha um vector com 5 elementos e queira imprimir todos os elementos na tela com suas respectivas posições. Os índices dos elementos vão de 0 a tamanho - 1, ou seja, de 0 a 4. Desse modo, vamos inicializar o contador `i` com 0 e incrementá-lo até que ele seja menor que o tamanho do vetor. O código abaixo mostra como fazer isso:

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> vetor = {1, 2, 3, 4, 5};
    int tamanho = vetor.size();

    for(int i = 0; i < tamanho; ++i) {
        std::cout << i << ':' << vetor[i] << std::endl;
    } // 0:1 1:2 2:3 3:4 4:5 (posição:elemento)
}
```

## Dicas para o Uso Eficiente

- **Índices Começam em 0**: Lembre-se de que os índices de vetores começam em 0. O primeiro elemento tem índice 0, o segundo tem índice 1 e assim por diante.
- **Limite Inferior e Superior**: O índice inicial é 0 e o índice final é tamanho - 1.
- **Evite Erros de Índice**: Certifique-se de não ultrapassar o limite superior do vetor, pois isso pode causar erros ou comportamentos inesperados.
