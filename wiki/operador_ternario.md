# Operador Ternário

<!-- toc -->
- [Introdução](#introdução)
- [Sintaxe do Operador Ternário](#sintaxe-do-operador-ternário)
- [Utilizando o Operador Ternário](#utilizando-o-operador-ternário)
<!-- toc -->

## Introdução

O operador ternário é uma construção poderosa e compacta que permite realizar uma avaliação condicional em uma única linha de código. Ele é bastante utilizado para atribuir valores a uma variável com base em uma condição.

## Sintaxe do Operador Ternário

A sintaxe do operador ternário é a seguinte:

```cpp
condição ? valor_caso_verdadeiro : valor_caso_falso
```

- A `condição` é uma expressão lógica que será avaliada como verdadeira ou falsa.
- `valor_caso_verdadeiro` é o valor que será atribuído à variável se a condição for verdadeira.
- `valor_caso_falso` é o valor que será atribuído à variável se a condição for falsa.

## Utilizando o Operador Ternário

O operador ternário é especialmente útil quando desejamos atribuir diferentes valores a uma variável com base em uma condição. Veja um exemplo simples:

```cpp
int idade = 18;
string status = (idade >= 18) ? "adulto" : "menor de idade"; // adulto
```

No exemplo acima, a variável `status` receberá o valor "adulto" se a idade for maior ou igual a 18, caso contrário, receberá o valor "menor de idade".

É importante notar que o operador ternário pode ser aninhado para realizar avaliações condicionais mais complexas. Porém, é necessário utilizar parênteses para garantir a correta avaliação das expressões. Veja um exemplo com aninhamento:

```cpp
int nota = 75;
std::string resultado = (nota >= 60) ? (nota >= 90 ? "excelente" : "aprovado") : "reprovado";
```

Nesse caso, a variável `resultado` receberá o valor "excelente" se a nota for maior ou igual a 90, "aprovado" se a nota for maior ou igual a 60, e "reprovado" caso contrário.

Note que o aninhamento do operador adiciona uma certa ilegibilidade ao código, por isso, quando precisar de condições mais complexas considere usar um [bloco condicional](../wiki/selecao_if_else.md).

## Regras

O retorno do ternário tem que ser do mesmo tipo nas duas saídas.

```cpp
std::cout << (4 > 5 ? "maior" : 0) << std::endl; // erro pois "maior" eh string e 0 eh int
```
