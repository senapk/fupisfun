# Exercícios de módulo

<!-- toc -->
- [Exercícios de módulo](#exercícios-de-módulo)
  - [Exercício 1: Verificando se um número é par ou ímpar](#exercício-1-verificando-se-um-número-é-par-ou-ímpar)
  - [Exercício 2: Repetições cíclicas](#exercício-2-repetições-cíclicas)
  - [Exercício 3: Manipulação de índices em arrays](#exercício-3-manipulação-de-índices-em-arrays)
  - [Exercício 4: Calendários e datas](#exercício-4-calendários-e-datas)
    - [Fórmula de Zeller](#fórmula-de-zeller)
    - [Utilizando a fórmula de Zeller](#utilizando-a-fórmula-de-zeller)
<!-- toc -->

## Exercício 1: Verificando se um número é par ou ímpar

Neste exemplo, o programa pede ao usuário para digitar um número inteiro. Em seguida, o operador de módulo é usado para verificar se o número é par ou ímpar. Se o resto da divisão do número por 2 for igual a 0, o número é par e a mensagem correspondente é exibida. Caso contrário, o número é ímpar, e outra mensagem é exibida. O operador de módulo é essencial para essa verificação, pois ele nos permite identificar se há um resto na divisão, o que é a característica fundamental dos números ímpares.

```cpp
#include <iostream>

int main() {
    int numero;

    std::cout << "Digite um número inteiro: ";
    std::cin >> numero;

    if (numero % 2 == 0) {
        std::cout << numero << " é um número par.\n";
    } else {
        std::cout << numero << " é um número ímpar.\n";
    }
}
```

## Exercício 2: Repetições cíclicas

Neste exemplo, temos um loop for que realiza 10 iterações, representadas por `i` variando de 1 a 10. A cada iteração, o valor de `i` é adicionado ao contador, e em seguida, o operador de módulo é aplicado ao resultado. O resultado do módulo 5 garante que o valor do contador permaneça dentro de um intervalo específico, criando um padrão cíclico. Essa técnica é útil para criar sequências periódicas ou repetições cíclicas em um programa.

```cpp
#include <iostream>

int main() {
    int contador = 0;

    for (int i = 1; i <= 10; i++) {
        contador = (contador + i) % 5;
        std::cout << "Iteração " << i << ": Contador = " << contador << '\n';
    }
}
```

## Exercício 3: Manipulação de índices em arrays

Neste exemplo, temos um array de tamanho 5, representado pela variável array. No código, tentamos acessar o valor do array no índice 7, o que é um índice inválido, pois está fora dos limites do array (0 a `4`). Para garantir que o índice seja válido, utilizamos o operador de módulo para calcular o resto da divisão do índice pelo tamanho do array. Dessa forma, o índice resultante será sempre um valor entre 0 e 4, garantindo que acessaremos um elemento válido do array. Essa técnica é muito útil para manipulação segura de índices em arrays e estruturas de dados, evitando acessos indevidos à memória.

```cpp
#include <iostream>

int main() {
    int tamanhoArray = 5;
    int array[] = {10, 20, 30, 40, 50};

    int indice = 7; // Um índice inválido, pois está fora dos limites do array.

    // Usando o operador de módulo para garantir um índice válido.
    indice = indice % tamanhoArray;

    std::cout << "Valor no índice " << indice << ": " << array[indice] << '\n';
}
```

## Exercício 4: Calendários e datas

### Fórmula de Zeller

A **fórmula de Zeller** é um algoritmo matemático desenvolvido pelo matemático alemão **Christian Zeller** no século XIX. Essa fórmula é usada para calcular o dia da semana correspondente a uma data específica, ou seja, determinar se uma data cai em uma segunda-feira, terça-feira, etc. O resultado é um número de 0 a 6, onde 0 representa o sábado, 1 o domingo e assim por diante.

Aqui está a fórmula de Zeller:

```mathematica
f = {k + [(m + 1) * 13 / 5] + C + [C / 4] + [D / 4] + [5 * D]} % 7
```

Onde:

- `f` é o dia da semana calculado (0: sábado, 1: domingo, 2: segunda-feira, ..., 6: sexta-feira).
- `k` é o dia do mês (1 a 31).
- `m` é o mês (3 para março, 4 para abril, ..., 14 para fevereiro; janeiro e fevereiro são tratados como meses 13 e 14 do ano anterior).
- `C` é o ano do século (`ano mod 100`)
  - Por exemplo, para 1995 o ano do século seria 95.
- `D` é o século do ano (`ano div 100`, ignorando os dígitos após a vírgula).
  - Por exemplo, para 1995 o século seria 19, ainda que na realidade o século seria XX.

### Utilizando a fórmula de Zeller

Neste exemplo, o programa solicita ao usuário que digite uma data (dia, mês e ano). Em seguida, utiliza a **fórmula de Zeller** para calcular o dia da semana correspondente a essa data.

```cpp
#include <iostream>
#include <iomanip>

int main() {
    int dia, mes, ano;

    std::cout << "Digite o dia (1-31): ";
    std::cin >> dia;

    std::cout << "Digite o mês (1-12): ";
    std::cin >> mes;

    std::cout << "Digite o ano: ";
    std::cin >> ano;

    // Ajustando o mês e o ano para a fórmula do cálculo.
    if (mes < 3) {
        mes += 12;
        ano--;
    }

    int anoDoSeculo = ano % 100;
    int seculo = ano / 100;

    // Fórmula de Zeller para calcular o dia da semana:
    int diaDaSemana = (dia + ((mes + 1) * 13 / 5) + anoDoSeculo + (anoDoSeculo / 4) + (seculo / 4) + (5 * seculo)) % 7;

    // Ajustando o resultado para valores positivos de 0 a 6 (sábado a sexta-feira).
    diaDaSemana = (diaDaSemana + 7) % 7;

    // Exibindo o resultado em texto.
    std::string diasDaSemana[] = {"Sábado", "Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"};

    auto sf = std::setfill('0');
    auto sw = std::setw(2);

    std::cout << "A data " << sf << sw << dia << "/" << sw << mes << "/" << ano << " cai em um(a) " << diasDaSemana[diaDaSemana] << ".\n";
}
```

Esse exemplo é útil para criar funcionalidades de calendário ou aplicações que precisam determinar o dia da semana de uma data específica, como agendas, sistemas de reservas ou organizadores. O operador de módulo é fundamental para ajustar o resultado da fórmula para um valor entre 0 e 6, tornando a saída mais intuitiva e fácil de interpretar.
