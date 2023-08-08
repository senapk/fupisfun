# Mersenne Twister

<!-- toc -->
- [A Classe `std::random_device`](#a-classe-stdrandom_device)
  - [Quando usar `std::random_device`](#quando-usar-stdrandom_device)
<!-- toc -->

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

Lembre-se de que o Mersenne Twister é um gerador de números pseudoaleatórios, o que significa que ele gera sequências aparentemente aleatórias, mas com base em uma fórmula matemática determinística.

## A Classe `std::random_device`

A classe `std::random_device` é um gerador de números aleatórios não-determinístico, ou seja, ele gera números aleatórios verdadeiros. No entanto, a implementação de `std::random_device` pode variar entre plataformas, e alguns compiladores podem não implementá-lo corretamente. Portanto, você deve sempre verificar a documentação do seu compilador para garantir que `std::random_device` seja implementado corretamente.

### Quando usar `std::random_device`

Você deve usar `std::random_device` quando precisar de números aleatórios verdadeiros, como para fins criptográficos. No entanto, você deve ter em mente que `std::random_device` pode ser muito lento, dependendo da implementação. Portanto, você deve usá-lo apenas quando precisar de números aleatórios verdadeiros.
