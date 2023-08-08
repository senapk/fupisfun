# Os números aleatórios

<!-- toc -->
- [O que é um número aleatório?](#o-que-é-um-número-aleatório)
- [Por que usar números aleatórios?](#por-que-usar-números-aleatórios)
- [Números aleatórios vs pseudoaleatórios](#números-aleatórios-vs-pseudoaleatórios)
- [Como gerar números aleatórios?](#como-gerar-números-aleatórios)
  - [Gerador Mersenne Twister](#gerador-mersenne-twister)
  - [`rand()` e `srand()`](#rand-e-srand)
    - [Combinando `srand` com `ctime`](#combinando-srand-com-ctime)
<!-- toc -->

## O que é um número aleatório?

Um número aleatório é um número que não pode ser previsto ou reproduzido. Por exemplo, se você jogar um dado, você não pode prever qual número vai sair. Se você jogar o dado novamente, você não pode garantir que o mesmo número vai sair. Portanto, o número que sai é aleatório.

## Por que usar números aleatórios?

Os números aleatórios são úteis para simular situações que envolvem incerteza. Por exemplo, se você está fazendo um jogo de tabuleiro, você pode usar números aleatórios para simular o lançamento de um dado. Se você está fazendo um jogo de cartas, você pode usar números aleatórios para simular a distribuição de cartas.

## Números aleatórios vs pseudoaleatórios

Os números aleatórios são difíceis de gerar. Na verdade, é **impossível** gerar números verdadeiramente aleatórios usando um computador. Os computadores são máquinas **determinísticas**, o que significa que eles executam instruções em uma ordem previsível. Portanto, os computadores não podem gerar números verdadeiramente aleatórios. Em vez disso, os computadores geram números **pseudoaleatórios**. Os números pseudoaleatórios são números que parecem aleatórios, mas são gerados usando um algoritmo **matemático**. Os números pseudoaleatórios são úteis porque são fáceis de gerar e podem ser reproduzidos.

## Como gerar números aleatórios?

Para gerar números aleatórios, você precisa de um **gerador de números aleatórios** e de uma **semente**. A semente é um número que inicializa o gerador de números aleatórios. Se você usar a mesma semente, o gerador de números aleatórios vai produzir a mesma sequência de números aleatórios. Se você usar uma semente diferente, o gerador de números aleatórios vai produzir uma sequência diferente de números aleatórios.

### Gerador Mersenne Twister

A geração de números aleatórios usando o Mersenne Twister é uma técnica eficiente e amplamente utilizada para produzir sequências de números com propriedades estatísticas de alta qualidade. O Mersenne Twister é um algoritmo de geração de números pseudoaleatórios que tem um período muito longo e uma distribuição uniforme bem definida.

Para usar o Mersenne Twister em C++, você precisará incluir a biblioteca `<random>` e criar uma instância de um objeto do tipo `std::mt19937` (que é a implementação do Mersenne Twister). Aqui está um exemplo de como fazer isso:

```cpp
#include <iostream>
#include <random>  // Incluir a biblioteca random

int main() {
    // Criar um objeto Mersenne Twister
    std::mt19937 mt(std::random_device{}());  // Seed a partir do random_device

    // Criar uma distribuição uniforme entre 0 e 1
    std::uniform_real_distribution<double> dist(0.0, 1.0);

    // Gerar números aleatórios usando o Mersenne Twister
    for (int i = 0; i < 10; ++i) {
        double randomValue = dist(mt);
        std::cout << randomValue << std::endl;
    }

    return 0;
}
```

Neste exemplo:

1. `std::mt19937 mt(std::random_device{}())` cria um objeto Mersenne Twister inicializado com uma semente obtida a partir do `random_device`, que fornece uma semente mais verdadeiramente aleatória.

2. `std::uniform_real_distribution<double> dist(0.0, 1.0)` cria uma distribuição uniforme de números reais no intervalo [0.0, 1.0).

3. O loop gera e imprime 10 números aleatórios no intervalo [0.0, 1.0).

Lembre-se de que o Mersenne Twister é um gerador de números pseudoaleatórios, o que significa que ele gera sequências aparentemente aleatórias, mas com base em uma fórmula matemática determinística. Se você precisar de verdadeira aleatoriedade, como para fins criptográficos, considere usar `std::random_device` para gerar uma semente mais robusta.

### `rand()` e `srand()`

Em C++, você também pode usar as funções `rand()` e `srand()` para gerar números pseudoaleatórios simples, ideal para pequenos projetos pessoais ou para fins educacionais. `rand()` gera um número inteiro aleatório no intervalo [0, `RAND_MAX`], onde `RAND_MAX` é uma constante definida na biblioteca `<cstdlib>`. `srand()` define a semente para `rand()`. Aqui está um exemplo de como usar `rand()` e `srand()`:

```cpp
#include <iostream>
#include <cstdlib>  // Incluir a biblioteca cstdlib

int main() {
    // Definir a semente para rand()
    srand(0);

    // Gerar números aleatórios usando rand()
    for (int i = 0; i < 10; ++i) {
        int randomValue = rand();
        std::cout << randomValue << std::endl;
    }

    return 0;
}
```

Neste exemplo:

1. `srand(0)` define a semente para `rand()` como 0.

2. O loop gera e imprime 10 números aleatórios no intervalo [0, `RAND_MAX`].

Lembre-se de que `rand()` e `srand()` são geradores de números pseudoaleatórios, o que significa que eles geram sequências aparentemente aleatórias, mas com base em uma fórmula matemática determinística.

#### Combinando `srand` com `ctime`

Você pode usar `ctime` para obter o tempo desde o início do programa em segundos e usá-lo como semente para `srand`. Aqui está um exemplo de como fazer isso:

```cpp
#include <iostream>
#include <cstdlib>  // Incluir a biblioteca cstdlib
#include <ctime>    // Incluir a biblioteca ctime

int main() {
    // Definir a semente para rand()
    srand(time(0));

    // Gerar números aleatórios usando rand()
    for (int i = 0; i < 10; ++i) {
        int randomValue = rand();
        std::cout << randomValue << std::endl;
    }

    return 0;
}
```

Usando o tempo como semente, você pode gerar números aleatórios diferentes toda vez que executar o programa, já que o tempo se utilia de segundos, contando desde o início do programa, no ano de 1970.

Ou seja, se você executar o programa duas vezes no mesmo segundo, ele irá gerar os mesmos números aleatórios, porém ainda é uma boa forma de gerar números aleatórios para projetos pessoais ou educacionais.
