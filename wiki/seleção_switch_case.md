# Estrutura de Seleção Switch

<!-- toc -->
- [Introdução](#introdução)
- [Funcionamento do switch case](#funcionamento-do-switch-case)
- [Utilização do switch case](#utilização-do-switch-case)
- [Exemplo em C++](#exemplo-em-c)
<!-- toc -->

## **Introdução**

Em linguagens de programação, o controle de fluxo é essencial para tomar
decisões com base em certas condições. Uma das estruturas de controle de
fluxo disponíveis em C++ é o `switch`. O `switch` é usado para selecionar um
bloco de código a ser executado com base no valor de uma expressão. Essa
estrutura é especialmente útil quando você precisa comparar um valor com
várias opções diferentes.

## **Funcionamento do `switch case`**

O `switch` é uma estrutura condicional que avalia uma expressão e, em
seguida, verifica se o valor da expressão corresponde a algum dos casos
especificados. Cada caso representa uma opção possível. Quando um caso
coincide com o valor da expressão, o bloco de código associado a esse caso é
executado. Se nenhum caso coincidir, é possível definir um bloco de código
padrão (com o uso do `default`) para ser executado.

A sintaxe geral do `switch` é a seguinte:

```cpp
switch (expressao) {
    case valor1:
        // Código a ser executado se a expressão for igual a valor1
        break;
    case valor2:
        // Código a ser executado se a expressão for igual a valor2
        break;
    // ...
    case valorN:
        // Código a ser executado se a expressão for igual a valorN
        break;
    default:
        // Código a ser executado se nenhum caso corresponder à expressão
        break;
}
```

## **Utilização do `switch case`**

O `switch` é uma ótima escolha quando você tem muitos valores possíveis
para a expressão que deseja **comparar**. Ele melhora a legibilidade do código e
facilita a manutenção, pois evita **aninhamentos excessivos** de `if-else`.

É importante mencionar que a expressão usada com `switch` deve ser um valor
**discreto**, como um número inteiro, caractere, enumeração ou constantes
definidas. O `switch` não pode ser usado com expressões mais complexas, como
strings ou tipos flutuantes.

## **Exemplo em C++:**

Vamos supor que temos um programa que recebe o número de um mês (de 1 a 12) e
exibe o nome do mês correspondente.

```cpp
#include <iostream>

int main() {
    int mes;
    std::cout << "Digite o número de um mês (1 a 12): ";
    std::cin >> mes;

    switch (mes) {
        case 1:
            std::cout << "Janeiro" << '\n';
            break;
        case 2:
            std::cout << "Fevereiro" << '\n';
            break;
        case 3:
            std::cout << "Março" << '\n';
            break;
        case 4:
            std::cout << "Abril" << '\n';
            break;
        case 5:
            std::cout << "Maio" << '\n';
            break;
        case 6:
            std::cout << "Junho" << '\n';
            break;
        case 7:
            std::cout << "Julho" << '\n';
            break;
        case 8:
            std::cout << "Agosto" << '\n';
            break;
        case 9:
            std::cout << "Setembro" << '\n';
            break;
        case 10:
            std::cout << "Outubro" << '\n';
            break;
        case 11:
            std::cout << "Novembro" << '\n';
            break;
        case 12:
            std::cout << "Dezembro" << '\n';
            break;
        default:
            std::cout << "Mês inválido!" << '\n';
            break;
    }

    return 0;
}
```

Neste exemplo, o programa solicita ao usuário um número de mês, utiliza a
estrutura `switch` para comparar esse número e, em seguida, imprime o nome do
mês correspondente na saída. Se o número fornecido não estiver entre 1 e
12, o bloco de código `default` será executado, informando que o mês é
inválido.

Exemplos de execução do código:

- Exemplo 1

```c++
Digite o número de um mês (1 a 12): 5
Maio
```

- Exemplo 2

```c++
Digite o número de um mês (1 a 12): 12
Dezembro 
```

- Exemplo 3

```c++
Digite o número de um mês (1 a 12): 7
Julho
```

- Exemplo 4

```c++
Digite o número de um mês (1 a 12): 15
Mês inválido!
```

Essa é apenas uma das muitas aplicações do `switch`. Ele pode ser utilizado
em diversos cenários onde é necessário fazer seleções baseadas em valores
discretos.
