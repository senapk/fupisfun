# Exemplos de códigos de linguagens

- [O que são linguagens de programação](#o-que-são-linguagens-de-programação)
- [Exemplos de linguagens de programação](#exemplos-de-linguagens-de-programação)

## O que são linguagens de programação

Uma **linguagem de programação** é um conjunto estruturado de regras, símbolos e palavras-chave que nos permite instruir um computador a executar tarefas específicas.

Cotidianamente usamos o português como linguagem de comunicação, mas os computadores não possuem a nossa capacidade linguística de interpretação, e por isso precisamos de uma gramática muito simplificada e que não permita ambiguidades, como visto no tópico sobre [algoritmos](o_que_sao_algoritmos.md).

O ato de escrever um algoritmo em uma linguagem de programação específica é chamado de **implementar** o algoritmo.

Por conta da diversidade de problemas na computação, existem diversas linguagens de programação, cada uma com suas características específicas. Geralmente as classificamos como linguagens de baixo-nível e linguagens de alto-nível:

1. Linguagens de baixo-nível: São linguagens que se aproximam mais da máquina, sendo mais difíceis de serem compreendidas por nós.

2. Linguagens de alto-nível: São linguagens que se aproximam mais das línguas humanas, sendo assim mais fáceis de serem compreendidas por nós.

Embora pareça óbvia a escolha de linguagens de alto-nível, as linguagens de baixo-nível possuem vantagens quando se trata de velocidade e flexibilidade.

## Exemplos de linguagens de programação

Para exemplificar o mundo das linguagens de programação iremos implementar o algoritmo de somar dois números em uma linguagem de baixo-nível: o *C++*, e em uma linguagem de alto-nível: o *Python*.

```c++
#include <iostream>

using namespace std;

int main() {
    int a = 5;
    int b = 2;
    int soma = a + b;

    cout << soma << "\n";
    return 0;
}
```

O código acima é uma implementação da soma de dois números em C++. Diferentemente do pseudocódigo agora precisamos lidar com aspectos específicos da linguagem como tipos de dados.

```py
a = 5
b = 2
soma = a + b
print(soma)
```

O código acima é uma implementação do mesmo algoritmo em Python. Observe que o código é muito mais simples que a implementação em C++ e se aproxima muito das linguagens humanas. No entanto, o código em C++ é executado muito mais rápido pelo computador.
