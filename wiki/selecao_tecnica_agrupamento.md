# Técnica de Agrupamento

<!-- toc -->
- [Introdução](#introdução)
- [Exemplos em C++](#exemplos-em-c)
  - [1. **Par ou Ímpar**](#1-par-ou-ímpar)
  - [2. **Jokenpô**](#2-jokenpô)
- [Considerações Finais](#considerações-finais)
<!-- toc -->

## Introdução

O **agrupamento de estruturas condicionais aninhadas** é uma técnica avançada e poderosa na programação para resolver problemas mais complexos. À medida que os programas se tornam mais sofisticados, as necessidades de tomar decisões mais elaboradas também aumentam. Nesse contexto, o uso de múltiplas instruções `if` e `else` encadeadas na `linguagem C++` oferece uma maneira estruturada e organizada de abordar esses desafios.

Quando um problema requer avaliação de múltiplas condições e tomadas de decisões com base em diferentes cenários, a utilização de estruturas condicionais aninhadas se torna uma escolha eficaz. Isso permite que o código seja mais modular, claro e legível, facilitando a manutenção e o entendimento do programa, mesmo em situações complexas.

## Exemplos em C++

Abaixo, temos os exemplos dos conhecidos jogos "Par ou Ímpar" e "Jokenpô". Vamos explorar esses exemplos para ilustrar o uso das técnicas de estruturas condicionais e agrupamento na `linguagem c++`.

### 1. **Par ou Ímpar**

Seja um jogo entre dois jogadores. As entradas são:

- Opção do primeiro jogador: "par" ou "impar";
- Número do primeiro jogador.
- Número do segundo jogador.

Seu código deve informar quem ganhou o jogo.

Exemplo abaixo na `linguagem c++`:

```c++
#include <iostream>

int main() {
    std::string opcao_jog1 {};
    int num_jog1 {};
    int num_jog2 {};

    std::cin >> opcao_jog1 >> num_jog1 >> num_jog2;

    int numero = num_jog1 + num_jog2;

    // agora vamos agrupar TODOS os casos em que o jogador 1 venceu
    if ((numero % 2 == 0 and opcao_jog1 == "par") or (numero % 2 != 0 and opcao_jog1 == "impar")) {
        std::cout << "Jogador 1 venceu!" << std::endl;
    } else {
        std::cout << "Jogador 2 venceu!" << std::endl;
    }
}
```

Observe que o jogador 1 só ganha se a opção escolhida for igual ao resultado da soma dos números ser par ou ímpar. Caso contrário, o jogador 2 ganha. Não precisamos verificar nenhum dos casos para o jogador 2, pois se o jogador 1 não ganhou, o jogador 2 ganhou.

### 2. **Jokenpô**

O jogo `Jokenpô`, também conhecido como Pedra, Papel e Tesoura, é um jogo simples e popular entre duas pessoas. Cada jogador escolhe uma das três opções: "Pedra", "Papel" ou "Tesoura". As regras são: Pedra vence Tesoura, Tesoura vence Papel e Papel vence Pedra. Se ambos escolherem a mesma opção, é um empate.

Novamente vamos agrupar os casos em que o jogador 1 venceu:

```c++
if (jogador1 == jogador2) {
    std::cout << "Empate!" << std::endl;
} else if ((jogador1 == "pedra"   and jogador2 == "tesoura") or 
           (jogador1 == "papel"   and jogador2 == "pedra") or 
           (jogador1 == "tesoura" and jogador2 == "papel")) {
    std::cout << "Jogador 1 venceu!" << std::endl;
} else {
    std::cout << "Jogador 2 venceu!" << std::endl;
}
```

No código acima, a mensagem "Empate!" será exibida apenas se ambos os jogadores escolherem a mesma opção.

A mensagem "Jogador 1 venceu!" será exibida apenas em três ocasiões, são elas:

- Se o jogador 1 escolher pedra e o jogador 2 escolher tesoura.
- Se o jogador 1 escolher papel e o jogador 2 escolher pedra.
- Se o jogador 1 escolher tesoura e o jogador 2 escolher papel.

Caso contrário, será exibida a mensagem "Jogador 2 venceu!"

## Considerações Finais

Em conclusão, exploramos os exemplos dos jogos `Par ou Ímpar` e `Jokenpô` (Pedra, Papel e Tesoura) para ilustrar o uso das técnicas de estruturas condicionais em C++.

No par ou ímpar, utilizamos a técnica de agrupamento de estruturas condicionais aninhadas para resolver o problema de forma mais eficiente e elegante.

Por sua vez, o jogo `Jokenpô` revelou a importância do agrupamento de estruturas condicionais aninhadas. Neste exemplo, utilizamos múltiplas instruções `if` e `else` encadeadas para comparar as escolhas dos jogadores e decidir o vencedor de acordo com as regras do jogo.

Esses dois exemplos nos permitiram entender como as estruturas condicionais são poderosas e versáteis em resolver problemas com várias condições e situações complexas. Além disso, eles destacaram a importância da lógica de programação e da criatividade para abordar desafios de forma eficiente e elegante.
