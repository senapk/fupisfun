# Impressão formatada

<!-- toc -->
- [Casas decimais](#casas-decimais)
- [Para que serve fixed](#para-que-serve-fixed)
- [Alinhamentos (Padding)](#alinhamentos-padding)
- [Preencher com zeros à esquerda](#preencher-com-zeros-à-esquerda)
- [Atalhos](#atalhos)
<!-- toc -->

Para formatar a saída no C++ usando `cout`, você pode utilizar a biblioteca `<iomanip>`, que fornece manipuladores de fluxo para controlar a formatação de saída. Aqui estão algumas das principais regras para formatar a saída com certo número de casas decimais ou inserir zeros antes do número:

## Casas decimais

Para imprimir um número com um número específico de casas decimais, você pode usar o manipulador `std::fixed` junto com `std::setprecision(n)`, onde 'n' é o número de casas decimais que você deseja imprimir.

```cpp
#include <iostream>
#include <iomanip>

int main() {
    double num = 3.14159265359;
    std::cout << std::fixed; //persistente, só precisa ser dado uma vez
    std::cout << std::setprecision(2) << "2 casas: " << num << '\n'; //precisa ser dado antes de cada número
    std::cout << std::setprecision(4) << "4 casas: " << num << '\n';
}
```

## Para que serve fixed

Por default, o `cout` faz alguns arredondamentos para imprimir um número. O `std::fixed` desabilita esse arredondamento, fazendo com que o número seja impresso exatamente como está armazenado na memória.

O std::fixed é persistente, ou seja, uma vez que você o ativa, ele permanece ativo até que você o desative. Outras opções, por curiosidade, são:

- `std::scientific` (para imprimir usando notação científica).
- `std::hexfloat` (para imprimir em hexadecimal).
- `std::defaultfloat` (para voltar ao padrão).

```cpp
#include <iostream>
#include <iomanip> //fixed

int main() {
    double num = 0.000001;
    
    //imprimindo sem std::fixed
    std::cout << num << '\n'; //1e-06

    std::cout << std::fixed;
    std::cout << num << '\n'; //0.000001
}
```

## Alinhamentos (Padding)

Para alinhar a saída, fazer um padding, em você pode usar o manipulador `std::setw(n)`, onde 'n' é o número total de caracteres que você deseja que a saída ocupe. Por exemplo, se você quiser que a saída ocupe 10 caracteres, você pode usar `std::setw(10)`. Ele precisa ser dado antes de cada entrada que você quer alinhar.

```cpp
#include <iostream>
#include <iomanip> //setw

int main() {
    std::cout << "[" << std::setw(10) << "bingo" << "]\n"; // [     bingo]
    //o setw(10) só vale para a próxima entrada
    //"bingo" tem 5 caracteres, então ele preenche com 5 espaços para completar 10
}
```

É possível definir o caractere de preenchimento com `std::setfill('c')`, onde 'c' é o caractere que você deseja usar para preencher o espaço. Por exemplo, se você quiser preencher o espaço com `*`, você pode usar `std::setfill('*')`. O setfill é persistente, ou seja, uma vez que você o ativa, ele permanece ativo até que você o desative.

O alinhamento padrão é à direita. Para alinhar à esquerda, você pode usar `std::left`. O comando `std::right` volta ao padrão. O left e right são persistentes, ou seja, uma vez que você o ativa, ele permanece ativo até que você o desative.

```cpp
#include <iostream>
#include <iomanip> //setw, left, right, setfill

int main() {

    std::cout << std::setfill('*') << std::left; //persistentes

    std::cout << std::setw(10) << "tango" << "\n"; // tango*****
    std::cout << std::setw(10) << "cash" << "\n";  // cash******

    std::cout << std::right; //volta ao padrão
    std::cout << std::setfill('_'); //muda o caractere de preenchimento para _

    std::cout << std::setw(10) << "tango" << "\n"; // _____tango
    std::cout << std::setw(10) << "cash" << "\n";  // cash******
}
```

## Preencher com zeros à esquerda

Para preencher um número com zeros à esquerda, você pode usar o manipulador `std::setw(n)` junto com `std::setfill('0')`, onde 'n' é o número total de dígitos no número após o preenchimento com zeros. Por exemplo, para imprimir hora e minuto com dois dígitos, com zeros à esquerda, você pode usar:

```cpp
#include <iostream>
#include <iomanip> //setw, setfill

int main() {
    std::cout << std::setfill('0');
    int hora {4};
    int minuto {5};

    std::cout << std::setw(2) << hora << ":" << std::setw(2) << minuto << "\n"; //04:05
}
```

## Atalhos

É possível simplificar seu código com alguns atalhos.

- Você pode aproveitar o mesmo `std::cout` para imprimir vários elementos em várias linhas, basta separar os elementos com `<<`:

```cpp
#include <iostream>

int main() {
    std::cout << "Vou aprender"
              << " programação"
              << "\n";
}
```

- Você pode salvar o comando de formatação em um atalho, por exemplo:
  - `p2` vai ser uma atalho para `std::setprecision(2)`,
  - `w2` vai ser uma atalho para `std::setw(2)`.

```cpp
#include <iostream>
#include <iomanip> //fixed, setprecision

int main() {
    double peso {78};
    double altura {1.7};
    
    auto p2 = std::setprecision(2); //guarda o comando de formatação em p2

    std::cout << std::fixed
              << "Eu tenho " << p2 << peso << "kg e " << p2 << altura << "m de altura\n";
              //Eu tenho 78.00kg e 1.70m de altura

    int hora {4};
    int minuto {5};
    auto w2 = std::setw(2);         //guarda o comando de formatação em w2

    std::cout << std::setfill('0')
              << "A hora é " << w2 << hora << ":" << w2 << minuto << "\n";
                //A hora é 04:05
}
```
