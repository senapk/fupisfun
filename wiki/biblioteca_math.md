# A biblioteca `cmath`

- [Introdução](#introdução)
- [Principais funções](#principais-funções)
  - [Função `pow`](#função-pow)
  - [Função `sqrt`](#função-sqrt)
  - [Função `abs`](#função-abs)
  - [Funções `floor`, `ceil` e `round`](#funções-floor-ceil-e-round)
- [Outras funções](#outras-funções)

## Introdução

Neste texto, vamos explorar a biblioteca `cmath` em C++, que é uma biblioteca padrão do C++ que fornece funções matemáticas comuns. A biblioteca `cmath` contém um conjunto de funções que permitem realizar cálculos matemáticos avançados, como potenciação, raiz quadrada, trigonometria, logaritmos e muito mais.

> Todas as bibliotecas padrão da linguagem C são disponíveis em C++ no formato `c<nome>`, por exemplo `math.h` se torna `cmath`, `stdio.h` se torna `cstdio` e etc...

## Principais funções

### Função `pow`

A função `pow` é usada para calcular a potência de um número. Ela aceita dois argumentos: a base e o expoente, e retorna a base elevada ao expoente.

```cpp
#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double base = 2.0, expoente = 3.0;
    double resultado = pow(base, expoente); // Resultado: 8.0
    cout << "Resultado da potência: " << resultado << endl;

    return 0;
}
```

### Função `sqrt`

A função `sqrt` é utilizada para calcular a raiz quadrada de um número. Ela aceita um único argumento, que é o número do qual queremos calcular a raiz quadrada, e retorna o resultado.

```cpp
#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double numero = 25.0;
    double resultado = sqrt(numero); // Resultado: 5.0
    cout << "Resultado da raiz quadrada: " << resultado << endl;

    return 0;
}
```

### Função `abs`

A função `abs` é utilizada para calcular o valor absoluto de um número, ou seja, ignorando o sinal dele. Ela aceita um único argumento, que é o número do qual queremos o valor absoluto, e retorna o resultado.

```cpp
#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int numero = -2;
    int resultado = abs(numero); // Resultado: 2
    cout << "Valor absoluto: " << resultado << endl;

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
#include <cmath>

int main() {
    double numero1 = 2.9;
    double numero2 = 2.1;
    double numero3 = 2.2;
    double numero4 = 2.7;

    double arredondamentoFloor1 = floor(numero1); // Resultado: 2.0
    double arredondamentoCeil1 = ceil(numero1);   // Resultado: 3.0
    double arredondamentoRound1 = round(numero1); // Resultado: 3.0

    double arredondamentoFloor2 = floor(numero2); // Resultado: 2.0
    double arredondamentoCeil2 = ceil(numero2);   // Resultado: 3.0
    double arredondamentoRound2 = round(numero2); // Resultado: 2.0

    double arredondamentoFloor3 = floor(numero3); // Resultado: 2.0
    double arredondamentoCeil3 = ceil(numero3);   // Resultado: 3.0
    double arredondamentoRound3 = round(numero3); // Resultado: 2.0

    double arredondamentoFloor4 = floor(numero4); // Resultado: 2.0
    double arredondamentoCeil4 = ceil(numero4);   // Resultado: 3.0
    double arredondamentoRound4 = round(numero4); // Resultado: 3.0

    cout << "Arredondamento usando floor: " << arredondamentoFloor1 << ", " << arredondamentoFloor2 << ", "
              << arredondamentoFloor3 << ", " << arredondamentoFloor4 << endl;
    cout << "Arredondamento usando ceil: " << arredondamentoCeil1 << ", " << arredondamentoCeil2 << ", "
              << arredondamentoCeil3 << ", " << arredondamentoCeil4 << endl;
    cout << "Arredondamento usando round: " << arredondamentoRound1 << ", " << arredondamentoRound2 << ", "
              << arredondamentoRound3 << ", " << arredondamentoRound4 << endl;

    return 0;
}
```

É importante observar que, para utilizar as funções da biblioteca `cmath`, é necessário incluir a biblioteca `<cmath>` no início do programa.

## Outras funções

A biblioteca `cmath` possui várias outras funções que podem ser interessantes dependendo do seu problema, como cálculo de logaritmos, funções trigonométricas e funções hiperbólicas.

Você pode visualizar a lista completa [aqui](https://cplusplus.com/reference/cmath/).
