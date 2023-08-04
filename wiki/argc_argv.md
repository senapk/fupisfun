# Argc e Argv

<!-- toc -->
- [Introdução](#introdução)
- [Explicação](#explicação)
- [Exemplos de utilização de argc e argv](#exemplos-de-utilização-de-argc-e-argv)
  - [Exemplo 1: Contagem dos argumentos](#exemplo-1-contagem-dos-argumentos)
  - [Exemplo 2: Impressão dos argumentos](#exemplo-2-impressão-dos-argumentos)
  - [Exemplo 3: Soma de números](#exemplo-3-soma-de-números)
<!-- toc -->

## Introdução

Em linguagem C++, o `argc` e `argv` são **parâmetros especiais** usados para
lidar com argumentos da linha de comando. Quando você executa um programa a
partir da linha de comando, pode passar **argumentos adicionais** para esse
programa. O `argc` representa o **número de argumentos** passados, e o `argv` é
um vetor (array) de **strings**, onde cada elemento desse vetor contém um dos
argumentos passados para o programa.

## Explicação

1. `argc` (argument count): Essa é uma variável inteira que indica o **número
de argumentos** passados para o programa a partir da linha de comando. O valor de
`argc` é sempre no mínimo 1, pois o primeiro elemento do vetor `argv` sempre
contém o **nome do próprio programa**.

2. `argv` (argument vector): Esse é um **vetor de strings**, onde cada elemento contém
um dos argumentos passados para o programa. O primeiro elemento (`argv[0]`) é sempre
uma string que contém o **nome do programa** em execução, e os elementos seguintes
(`argv[1]`,`argv[2]`, etc.) contêm os argumentos adicionais fornecidos.

## Exemplos de utilização de argc e argv

### Exemplo 1: Contagem dos argumentos

Neste exemplo, criaremos um programa simples que recebe argumentos da linha de
comando e conta quantos argumentos foram passados.

```cpp
#include <iostream>

int main(int argc, char* argv[]) {
    std::cout << "Número de argumentos passados: " << argc << '\n';
    return 0;
}
```

Funcionamento:
Se você compilar e executar o programa da seguinte forma:

```cpp
./contagem_argumentos arg1 arg2 arg3
```

A saída será:

```cpp
Número de argumentos passados: 4
```

O valor de `argc` será 4, pois foram passados quatro argumentos:
"./contagem_argumentos", "arg1", "arg2" e "arg3".

### Exemplo 2: Impressão dos argumentos

Neste exemplo, criaremos um programa que imprime todos os argumentos passados
na linha de comando.

```cpp
#include <iostream>

int main(int argc, char* argv[]) {
    std::cout << "Argumentos passados:\n";
    for (int i = 0; i < argc; ++i) {
        std::cout << "Argumento " << i << ": " << argv[i] << '\n';
    }
    return 0;
}
```

Funcionamento:
Se você compilar e executar o programa da seguinte forma:

```cpp
./imprimir_argumentos abacaxi morango banana
```

A saída será:

```cpp
Argumentos passados:
Argumento 0: ./imprimir_argumentos
Argumento 1: abacaxi
Argumento 2: morango
Argumento 3: banana
```

### Exemplo 3: Soma de números

Neste exemplo, criaremos um programa que recebe argumentos numéricos da linha
de comando e realiza a soma desses números.

```cpp
#include <iostream>
#include <cstdlib>

int main(int argc, char* argv[]) {
    //Error: poucos argumentos passados
    if (argc < 3) {
        std::cerr << "Uso: " << argv[0] << " <número1> <número2> ..." << '\n';
        return 1;
    }

    int soma = 0;
    for (int i = 1; i < argc; ++i) {
        int numero = std::atoi(argv[i]);
        soma += numero;
    }

    std::cout << "Soma dos números: " << soma << '\n';
    return 0;
}
```

Funcionamento:
Se você compilar e executar o programa da seguinte forma:

```cpp
./soma_numeros 10 20 30
```

A saída será:

```cpp
Soma dos números: 60
```

O programa soma os números 10, 20 e 30 que foram passados como argumentos e
exibe o resultado na tela.

---

Em resumo o `argc` e `argv` possibilitam que os programas sejam mais **interativos
e personalizáveis**, permitindo que os usuários forneçam informações específicas
durante a execução do programa. Os argumentos podem ser utilizados para **configurar
o comportamento do programa**, realizar operações específicas ou processar dados
diferentes a cada execução. No entanto, é importante fazer a devida **validação
dos argumentos** para evitar erros e garantir uma execução segura do programa.
