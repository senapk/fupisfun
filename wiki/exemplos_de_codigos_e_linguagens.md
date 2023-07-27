# Exemplos de códigos de linguagens

<!-- toc -->
- [O que são linguagens de programação](#o-que-são-linguagens-de-programação)
- [Exemplos de linguagens de programação](#exemplos-de-linguagens-de-programação)
<!-- toc -->

## O que são linguagens de programação

Uma **linguagem de programação** é um conjunto estruturado de regras, símbolos e palavras-chave que nos permite instruir um computador a executar tarefas específicas.

Cotidianamente, usamos o português como linguagem de comunicação, mas os computadores não possuem a nossa capacidade linguística de interpretação e por isso precisamos de uma gramática muito simplificada e que não permita ambiguidades como visto no tópico sobre [algoritmos](o_que_sao_algoritmos.md).

O ato de escrever um algoritmo em uma linguagem de programação específica é chamado de **implementar** o algoritmo.

Por conta da diversidade de problemas na computação, existem diversas linguagens de programação, cada uma com suas características específicas. Geralmente as classificamos como linguagens de baixo-nível e linguagens de alto-nível:

1. Linguagens de baixo-nível: São linguagens que se aproximam mais da máquina, sendo mais difíceis de serem compreendidas por nós.

2. Linguagens de alto-nível: São linguagens que se aproximam mais das línguas humanas, sendo assim mais fáceis de serem compreendidas por nós.

Embora pareça óbvia a escolha de linguagens de alto-nível, as linguagens de baixo-nível possuem vantagens quando se trata de velocidade e flexibilidade.

## Exemplos de linguagens de programação

Para exemplificar o mundo das linguagens de programação iremos implementar o algoritmo de somar dois números em uma linguagem de baixo-nível: o *C++*, e em uma linguagem de alto-nível: o *Python*.

```c++
#include <iostream>

int main() {
    int num1 = 0; //cria um lugar
    std::cout << "Digite o primeiro número\n";
    std::cin >> num1; //lê o número

    int num2 = 0;
    std::cout << "Digite o segundo número\n";
    std::cin >> num2; //lê o número

    int soma = num1 + num2;

    std::cout << "A soma é " << soma << "\n";
    return 0;
}
```

O código acima é um código em C++. Ele utiliza o `std::cout` para enviar uma mensagem para o terminal e o `std::cin` para receber uma valor do terminal. Ele guarda os valores recebidos em variáveis e depois as soma e exibe o resultado.

Executar o código acima no terminal resulta em:

```txt
Digite o primeiro número
5
Digite o segundo número
7
A soma é 12
```

O mesmo código em Python:

```py
print("Digite o primeiro número)
num1 = int(input()) //lê o número

print("Digite o segundo número)
num2 = int(input()) //lê o número

soma = a + b
print("A soma é", soma)
```

O código acima é uma implementação do mesmo algoritmo em Python. Observe que o código é muito mais simples que a implementação em C++ e se aproxima muito das linguagens humanas. No entanto, o código em C++ é executado de forma mais eficiente pelo computador, ou seja, mais rápido e usando menos memória.
