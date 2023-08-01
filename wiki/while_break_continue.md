# Introdução às Estruturas de Repetição em C++

<!--toc-->
- [Introdução às Estruturas de Repetição em C++](#introdução-às-estruturas-de-repetição-em-c)
  - [A Estrutura de Repetição While](#a-estrutura-de-repetição-while)
  - [Exemplo de Uso do While](#exemplo-de-uso-do-while)
  - [Utilização do `while(true)`](#utilização-do-whiletrue)
    - [Controlando loop com `break`](#controlando-loop-com-break)
      - [Exemplo de utilização do `break`](#exemplo-de-utilização-do-break)
    - [Controlando loop com `continue`](#controlando-loop-com-continue)
      - [Exemplo de utilização do `continue`](#exemplo-de-utilização-do-continue)
    - [Exemplo de Uso do `while(true)` com `break` e `continue`](#exemplo-de-uso-do-whiletrue-com-break-e-continue)
<!--toc-->

As estruturas de repetição são recursos essenciais em qualquer linguagem de
programação, permitindo que um conjunto de instruções seja executado
**repetidamente** enquanto uma determinada condição for verdadeira. Isso é
especialmente útil quando se deseja executar um bloco de código **várias vezes**
sem ter que repetir manualmente as mesmas instruções. Neste texto,
abordaremos a estrutura de repetição `while` em C++ e discutiremos o conceito
de `while(true)`, juntamente com as palavras-chave `break` e `continue`.

## A Estrutura de Repetição While

Em C++, o `while` é uma das estruturas de repetição mais simples e
amplamente utilizadas. A sintaxe básica do `while` é a seguinte:

```cpp
while (condicao) {
    // Bloco de código a ser repetido enquanto a condição for verdadeira
}
```

O bloco de código dentro das chaves será repetido enquanto a condição
especificada dentro dos parênteses for verdadeira. É importante garantir que
a condição eventualmente se torne falsa em algum momento, caso contrário, o
**loop se tornará infinito.**

## Exemplo de Uso do While

Suponha que desejamos exibir os números de 1 a 5 na saída padrão:

```cpp
#include <iostream>

int main() {
    int i = 1;
    while (i <= 5) {
        std::cout << i << " "; // 1 2 3 4 5
        i++;
    }

    return 0;
}
```

loop while é iniciado `while (i <= 5)` . Isso significa que enquanto a condição
i <= 5 for **verdadeira**, o bloco de código dentro do loop será executado repetidamente.
Na sétima linha `i++` incrementa o valor de i em 1 a cada iteração, garantindo
que o loop eventualmente termine. Quando i se torna 6, a condição i <= 5 se torna
falsa e o loop **termina**.

## Utilização do `while(true)`

O `while(true)` é uma forma de criar um loop infinito, pois a condição
sempre será verdadeira (`true`). É útil quando queremos executar um bloco de
código repetidamente até que uma condição de saída seja encontrada no
próprio bloco ou quando queremos controlar o loop de forma mais flexível com
a utilização de `break` e `continue`.

### Controlando loop com `break`

Quando o `break` é encontrado dentro de um loop, o loop é
interrompido imediatamente, e a execução continua a partir da próxima
instrução após o loop.

#### Exemplo de utilização do `break`

Neste exemplo, criaremos um programa para encontrar o primeiro número que seja
divisível por ambos 4 e 5.

```cpp
#include <iostream>

int main() {
    int numero = 1;

    while (true) {
        if (numero % 4 == 0 && numero % 5 == 0) {
            std::cout << "O primeiro número divisível por 4 e 5 é: "; 
            std::cout << numero << '\n'; // 20

            break; // Sai do loop quando o número é divisível por 4 e 5
        }

        numero++;
    }

    return 0;
}
```

Neste código, o loop `while(true)` executa indefinidamente, mas dentro do loop,
usamos a estrutura condicional `if` para verificar se o número é divisível por
4 e 5. Quando essa condição é verdadeira, o loop é interrompido usando a instrução
`break`. O programa imprimirá o primeiro número que atende à condição especificada.
No caso, o número que é divisível tanto por 4 quanto por 5 é 20. Portanto, a saída
esperada será 20

### Controlando loop com `continue`

Quando o `continue` é encontrado dentro de um loop, a
execução do loop é interrompida para a iteração atual, e a próxima
iteração é iniciada.

#### Exemplo de utilização do `continue`

Neste exemplo, criaremos um programa para imprimir apenas os números ímpares
entre 1 e 10, pulando os números pares.

```cpp
#include <iostream>

int main() {
    int numero = 1;

    while (numero <= 10) {
        if (numero % 2 == 0) {
            numero++;
            continue; // Pula para a próxima iteração se o número for par
        }

        std::cout << numero << " "; // 1 3 5 7 9
        numero++;
    }
    
    std::cout << '\n';

    return 0;
}
```

Neste exemplo, os números pares (2, 4, 6, 8 e 10) são ignorados pelo `continue`,
enquanto os números ímpares (1, 3, 5, 7 e 9) são impressos no console.

### Utilizando um loop infinito para ler entradas do usuário

Na seção sobre [entrada de dados](entrada_dados.md) vimos algumas técnicas de uso do `cin`.

- Podemos fazer um teste para saber se o `cin` conseguiu fazer a leitura corretamente.
- Podemos usar o `cin.ignore()` para limpar o buffer de entrada.
- Podemos usar o `cin.clear()` para destravar o `cin` caso ele tenha entrado em estado de erro.

O código abaixo vai ficar em loop até o usuário digitar um número inteiro válido.

```cpp
#include <iostream>
#include <limits> // std::numeric_limits

int main() {
    int value {};
    while (true) {
        std::cout << "Digite um número inteiro: ";
        if (std::cin >> value) {
            break;
        }
        std::cout << "Entrada inválida. Tente novamente." << '\n';
        std::cin.clear(); //destrava o cin
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); //limpa o buffer de entrada
    }
    std::cout << "Você digitou o número: " << value << '\n';
}
```

O `std::numeric_limits<std::streamsize>::max()` indica que queremos limpar o buffer até o final da linha, não importa o tamanho da linha.

### Exemplo de Uso do `while(true)` com `break` e `continue`

Vamos criar um exemplo onde pedimos ao usuário para **adivinhar** um número entre
1 e 100. O loop continuará até que o usuário **adivinhe corretamente** o número
secreto (que será 42, por exemplo). O usuário pode optar por sair do jogo
digitando "0".

```cpp
#include <iostream>
#include <limits>

int main() {
    int numeroSecreto = 42;
    int palpite;

    while (true) {
        std::cout << "Digite um palpite entre 1 e 50 (ou 0 para sair): ";

        if (not (std::cin >> palpite)) { //digitou algo que não é um número
            std::cout << "Entrada inválida. Tente novamente." << '\n';
            std::cin.clear(); //destrava o cin
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); //limpando tudo que foi escrito
            continue; //voltando pro começo do loop
        }

        if (palpite == 0) {
            std::cout << "Você desistiu. O número secreto era: ";
            std::cout << numeroSecreto << '\n';
            break;
        }

        if (palpite == numeroSecreto) {
            std::cout << "Parabéns! Você acertou!" << '\n';
            break;
        }
        std::cout << "Tente novamente." << '\n';
    }

    return 0;
}
```

Neste exemplo, o loop `while(true)` continua até que o usuário acerte o
número ou insira "0" para sair. O `break` é usado para sair do loop quando o
número correto é adivinhado ou quando o usuário desiste, e o `continue` é
utilizado para ignorar o restante do loop e pedir um novo palpite caso o
palpite atual esteja incorreto.

Assim, as estruturas `break` e `continue` proporcionam maior controle sobre o
fluxo do loop e permitem criar lógicas mais complexas para lidar com a
repetição de código.

Exemplo de interação com o programa:

- Exemplo 1

```cpp
Digite um palpite (ou 0 para sair): 20
Tente novamente.
Digite um palpite (ou 0 para sair): 54 
Tente novamente.
Digite um palpite (ou 0 para sair): 33
Tente novamente.
Digite um palpite (ou 0 para sair): 1
Tente novamente.
Digite um palpite (ou 0 para sair): 42
Parabéns! Você acertou!
```

- Exemplo 2

```cpp
Digite um palpite (ou 0 para sair): 2
Tente novamente.
Digite um palpite (ou 0 para sair): 30
Tente novamente.
Digite um palpite (ou 0 para sair): 45
Tente novamente.
Digite um palpite (ou 0 para sair): 23
Tente novamente.
Digite um palpite (ou 0 para sair): 0
Você desistiu. O número secreto era: 42
```
