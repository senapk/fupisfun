# Técnica de Agrupamento

<!-- toc -->
- [Introdução](#introdução)
- [Exemplo em C++](#exemplos-em-c)
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

O jogo `Par ou Ímpar` é uma atividade lúdica que envolve duas pessoas. Cada jogador escolhe um número para mostrar e, em seguida, os números são somados. Um dos jogadores anuncia se a soma é `Par` ou `Ímpar` sem revelar o resultado exato. O outro jogador deve adivinhar se a soma é `Par` (se for divisível por 2) ou `Ímpar` (se não for divisível por 2).


Exemplo abaixo na `linguagem c++`:


```c++
if (numero % 2 == 0) {
  std::cout << numero << " é um número par, jogador 1 venceu!" << std::endl;
} else {
  std::cout << numero << " é um número ímpar, jogador 2 venceu!" << std::endl;
}
```

No código acima, a mensagem "é um número par, jogador 1 venceu!" apenas vai ser mostrada se
a variável `numero` dividido por 2 obter resto 0. Caso contrário a mensagem mostrada será "é um número ímpar, jogador 2 venceu!"

### 2. **Jokenpô**

O jogo `Jokenpô`, também conhecido como Pedra, Papel e Tesoura, é um jogo simples e popular entre duas pessoas. Cada jogador escolhe uma das três opções: "Pedra", "Papel" ou "Tesoura". As regras são: Pedra vence Tesoura, Tesoura vence Papel e Papel vence Pedra. Se ambos escolherem a mesma opção, é um empate.

Exemplo abaixo na `linguagem c++`:

```c++
if (jogador1 == jogador2) {
  std::cout << "Empate!" << std::endl;
} else if ((jogador1 == "pedra" && jogador2 == "tesoura") || (jogador1 == "papel" && jogador2 == "pedra") || (jogador1 == "tesoura" && jogador2 == "papel")) {
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

O jogo `Par ou Ímpar` nos mostrou como utilizar a estrutura condicional `if` e `else` para tomar decisões com base em uma condição simples: a paridade de um número. A partir disso, pudemos verificar se um número é par ou ímpar e, assim, determinar o vencedor do jogo com base nas escolhas feitas pelos jogadores.

Por sua vez, o jogo `Jokenpô` revelou a importância do agrupamento de estruturas condicionais aninhadas. Neste exemplo, utilizamos múltiplas instruções `if` e `else` encadeadas para comparar as escolhas dos jogadores e decidir o vencedor de acordo com as regras do jogo.

Esses dois exemplos nos permitiram entender como as estruturas condicionais são poderosas e versáteis em resolver problemas com várias condições e situações complexas. Além disso, eles destacaram a importância da lógica de programação e da criatividade para abordar desafios de forma eficiente e elegante.
