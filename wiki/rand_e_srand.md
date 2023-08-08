# `rand()` e `srand()`

<!-- toc -->
<!-- toc -->

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

## Combinando `srand` com `ctime`

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
