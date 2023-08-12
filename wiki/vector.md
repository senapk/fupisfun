# Vector

<!-- toc -->
- [Introdução](#introdução)
- [Implementação](#implementação)
- [Inserindo Elementos em um Vector](#inserindo-elementos-em-um-vector)
- [Removendo Elementos em um Vector](#removendo-elementos-em-um-vector)
- [Acessando Elementos de um Vector](#acessando-elementos-de-um-vector)
- [Alterando Elementos de um Vector](#alterando-elementos-de-um-vector)
- [Percorrendo um Vector](#percorrendo-um-vector)
<!-- toc -->

## Introdução

Em `C++`, o termo `vector` se refere a um tipo de contêiner dinâmico da Biblioteca Padrão do C++ `(STL - Standard Template Library)`. Um vector é uma coleção ordenada de elementos, semelhante a um array, mas com a capacidade de crescer ou diminuir automaticamente em tamanho conforme necessário.

## Implementação

Em `C++`, o `vector` é implementado como arrays dinâmicos, o que significa que o tamanho do `vector` pode ser ajustado durante a execução do programa. Isso contrasta com arrays estáticos, cujo tamanho precisa ser definido em tempo de compilação e não pode ser alterado posteriormente.

Para implementar um vector, precisamos de duas informações:

- O tipo dos elementos que serão guardados no vector: `int`, `double`, `char`, etc.
- Vale ressaltar que o vector só pode armazenar elementos do mesmo tipo, não é possível armazenar elementos de tipos diferentes em um mesmo vector.

Para implementar o vector é nescessário importar a biblioteca vector:

```c++
#include <vector>
```

A sintaxe para declarar um vector é:

```c++
std::vector<tipo> nome;
```

Por exemplo:

```c++
std::vector<int> numeros;
```

## Inserindo Elementos em um Vector

Inserir elementos em um `vector` em `C++` é uma operação importante quando se trabalha com contêineres dinâmicos. A biblioteca padrão do `C++` fornece várias maneiras de inserir elementos em um `vector`, permitindo adicionar novos valores ao `final do vetor`, em uma `posição específica` ou até mesmo `a partir de outro intervalo de elementos`. Aqui estão algumas maneiras comuns de inserir elementos em um vetor:

**push_back()**: O método `push_back()` é usado para adicionar um elemento ao final do vetor:

```c++
std::vector<int> numeros;

numeros.push_back(10);
numeros.push_back(20);
numeros.push_back(30);
```

**insert()**: O método `insert()` permite inserir elementos em uma posição específica do vetor. Ele aceita dois argumentos: um iterador apontando para a posição de inserção e o valor a ser inserido:
```c++
std::vector<int> numeros;

numeros.push_back(10);
numeros.push_back(20);
numeros.push_back(30);

auto iter = numeros.begin() + 1; // Inserir na segunda posição (índice 1)
numeros.insert(iter, 25);
```

## Removendo Elementos em um Vector

Remover elementos de um `vector` em C++ é outra operação comum ao trabalhar com contêineres dinâmicos. A Biblioteca Padrão do C++ fornece métodos para remover elementos do vetor de várias maneiras, incluindo a `remoção de elementos específicos`, a `remoção de elementos de uma determinada posição` e a `remoção de um intervalo de elementos`. Aqui estão algumas das principais maneiras de remover elementos de um vetor:

**pop_back()**: O método `pop_back()` remove o último elemento do vetor:

```c++
std::vector<int> numeros;

numeros.push_back(10);
numeros.push_back(20);
numeros.push_back(30);

numeros.pop_back(); // Remove o último elemento (30)
```

**erase()**: O método `erase()` é usado para remover elementos em uma posição específica do vetor. Ele aceita um iterador que aponta para o elemento a ser removido ou um intervalo de elementos a serem removidos.
```c++
std::vector<int> numeros;

numeros.push_back(10);
numeros.push_back(20);
numeros.push_back(30);

auto iter = numeros.begin() + 1; // Remover o segundo elemento (índice 1)
numeros.erase(iter);
```

**Remoção a partir de um intervalo de elementos**: Você pode usar o `método erase()` com um intervalo de elementos para remover mais de um elemento de uma vez:
```c++
std::vector<int> numeros;

numeros.push_back(10);
numeros.push_back(20);
numeros.push_back(30);

auto primeiro = numeros.begin() + 1; // Remover do segundo ao quarto elemento
auto ultimo = numeros.begin() + 4;
numeros.erase(primeiro, ultimo);
```

**remove() com erase()**: Para remover elementos específicos com base em seu valor, você pode combinar a função `std::remove()` com o método `erase()`. Isso é útil quando você deseja remover todos os elementos com um valor específico:
```c++
std::vector<int> numeros;

numeros.push_back(10);
numeros.push_back(20);
numeros.push_back(30);

int valorParaRemover = 20;
numeros.erase(std::remove(numeros.begin(), numeros.end(), valorParaRemover), numeros.end());
```

## Acessando Elementos de um Vector

Acessar elementos de um vector em C++ é uma tarefa fundamental quando se trabalha com contêineres dinâmicos. Os elementos em um vetor são armazenados em posições sequenciais e podem ser acessados por meio de índices. Aqui estão algumas maneiras de acessar elementos em um vetor:

**Operador de índice ([])**: Você pode usar o `operador de índice` para acessar um elemento específico do vetor. Os índices de vetores em C++ começam em 0.
```c++
std::vector<int> numeros;

numeros.push_back(10);
numeros.push_back(20);
numeros.push_back(30);

int primeiroElemento = numeros[0]; // Acessa o primeiro elemento (índice 0)
int segundoElemento = numeros[1];  // Acessa o segundo elemento (índice 1)
```

**Método front() e back()**: Os métodos `front()` e `back()` permitem acessar o primeiro e o último elemento do vetor, respectivamente:

```c++
std::vector<int> numeros;

numeros.push_back(10);
numeros.push_back(20);
numeros.push_back(30);

int primeiroElemento = numeros.front(); // Acessa o primeiro elemento
int ultimoElemento = numeros.back();    // Acessa o último elemento
```

## Alterando Elementos de um Vector

Alterar elementos de um `vector` em C++ envolve a modificação do valor de um elemento existente dentro do vetor. Existem várias maneiras de realizar essa operação, sendo as mais comuns usando o operador de índice ([]) ou iteradores. Aqui está essa abordagem:

**Operador de índice ([])**: Você pode usar o operador de índice para `acessar e modificar` elementos individuais do vetor.

```c++
std::vector<int> numeros;

numeros.push_back(10);
numeros.push_back(20);
numeros.push_back(30);

numeros[1] = 25; // Modifica o segundo elemento (índice 1) para 25
```

## Percorrendo um Vector

Percorrer (ou iterar) um `vector` em C++ significa percorrer todos os elementos armazenados no vetor para realizar alguma operação, como leitura, modificação ou exibição. Existem várias maneiras de percorrer um `vector`, e cada uma delas tem suas próprias vantagens e casos de uso. Aqui estão algumas maneiras comuns de percorrer um vetor em C++:

**Usando um loop for tradicional:**
```c++
std::vector<int> numeros;

numeros.push_back(10);
numeros.push_back(20);
numeros.push_back(30);

for (int i = 0; i < numeros.size(); ++i) {
    std::cout << numeros[i] << " ";
}
```

**Usando um loop for-each (C++11 em diante):**
```c++
std::vector<int> numeros;

numeros.push_back(10);
numeros.push_back(20);
numeros.push_back(30);

for (int num : numeros) {
    std::cout << num << " ";
}
```

**Usando iteradores:**
```c++
std::vector<int> numeros;

numeros.push_back(10);
numeros.push_back(20);
numeros.push_back(30);

for (auto iter = numeros.begin(); iter != numeros.end(); ++iter) {
    std::cout << *iter << " ";
}
```
