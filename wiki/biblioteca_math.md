# A biblioteca `cmath`

<!-- toc -->
- [Introdução](#introdução)
- [Principais funções](#principais-funções)
  - [Função `pow`](#função-pow)
  - [Função `sqrt`](#função-sqrt)
  - [Função `abs`](#função-abs)
  - [Funções `floor`, `ceil` e `round`](#funções-floor-ceil-e-round)
- [Outras funções](#outras-funções)
<!-- toc -->

## Introdução

Neste texto, vamos explorar a biblioteca `cmath` em C++, que é uma biblioteca padrão do C++ que fornece funções matemáticas comuns. A biblioteca `cmath` contém um conjunto de funções que permitem realizar cálculos matemáticos avançados, como potenciação, raiz quadrada, trigonometria, logaritmos e muito mais.

> Todas as bibliotecas padrão da linguagem C são disponíveis em C++ no formato `c<nome>`, por exemplo `math.h` se torna `cmath`, `stdio.h` se torna `cstdio` e etc...

## Principais funções

### Função `pow`

A função `pow` é usada para calcular a potência de um número. Ela aceita dois argumentos: a base e o expoente, e retorna a base elevada ao expoente. A maioria das pessoas conhece apenas a potenciação utilizando números inteiros, mas o `pow` foi feito para suportar número em ponto flutuante.

```cpp
#include <iostream>
#include <cmath>    //pow

int main() {
    std::cout << "Dois ao cubo: " << pow(2, 3) << '\n';          // 8
    std::cout << "2.5 elevado a 3.1: " << pow(2.5, 3.1) << '\n'; // 17.1243
}
```

### Função `sqrt`

A função `sqrt` é utilizada para calcular a raiz quadrada de um número. Ela aceita um único argumento, que é o número do qual queremos calcular a raiz quadrada, e retorna o resultado. Ela também trabalha com números em ponto flutuante.

```cpp
#include <iostream>
#include <cmath> //sqrt

int main() {
    std::cout << "Raiz de 25: " << sqrt(25) << '\n';   // 5
    std::cout << "Rais de 1.5: " << sqrt(1.5) << '\n'; // 1.22474
}
```

### Função `abs`

A função `abs` é utilizada para calcular o valor absoluto de um número, ou seja, ignorando o sinal dele. Ela aceita um único argumento, que é o número do qual queremos o valor absoluto, e retorna o resultado.

Para valores em ponto flutuante utilize o `fabs`.

```cpp
#include <iostream>
#include <cmath> //abs e fabs

int main() {
    std::cout << "Valor absoluto de -2: " << abs(-2) << '\n';     // 2
    std::cout << "Valor absoluto de 2: " << abs(2) << '\n';       // 2
    std::cout << "Valor absoluto de -1.5: " << abs(-1.5) << '\n'; // 1.5
    std::cout << "Valor absoluto de 1.5: " << abs(1.5) << '\n';   // 1.5
    return 0;
}
```

### Funções `floor`, `ceil` e `round`

Essas funções servem para calcular o arredondamento de números reais, cada uma utilizando um critério específico:

- `floor`: Arredonda um número para baixo, por exemplo 2.9 seria arrendado para 2.0 mesmo estando mais próximo do 3.0.
- `ceil`: Arredonda um número para cima, por exemplo 2.1 seria arrendado para 3.0 mesmo estando mais próximo do 2.0.
- `round`: Arrendonda um número baseado no valor da casa decimal, por exemplo, 2.2 seria arredondado para 2.0 e 2.7 seria arredondado para 3.0.

```cpp
#include <iostream>
#include <cmath> //floor, ceil, round

int main() {
    std::cout << "floor de 2.1: " << floor(2.1) << '\n'; // 2
    std::cout << "ceil de 2.1: " << ceil(2.1) << '\n';   // 3
    std::cout << "round de 2.1: " << round(2.1) << '\n'; // 2

    std::cout << "floor de 2.7: " << floor(2.7) << '\n'; // 2
    std::cout << "ceil de 2.7: " << ceil(2.7) << '\n';   // 3
    std::cout << "round de 2.7: " << round(2.7) << '\n'; // 3
}
```

É importante observar que, para utilizar as funções da biblioteca `cmath`, é necessário incluir a biblioteca `<cmath>` no início do programa.

## Outras funções

A biblioteca `cmath` possui várias outras funções que podem ser interessantes dependendo do seu problema, como cálculo de logaritmos, funções trigonométricas e funções hiperbólicas.

Você pode visualizar a lista completa [aqui](https://cplusplus.com/reference/cmath/).
