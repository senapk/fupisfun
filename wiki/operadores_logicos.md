# Operadores lógicos

<!-- toc -->
- [Operador lógico AND (&&)](#operador-lógico-and-)
- [Operador lógico OR (||)](#operador-lógico-or-)
- [Operador lógico NOT (!)](#operador-lógico-not-)
- [Uso dos parênteses](#uso-dos-parênteses)
- [Comparação dois a dois](#comparação-dois-a-dois)
<!-- toc -->

Em C++, os operadores lógicos são utilizados para realizar operações de lógica booleana em expressões condicionais. Existem três operadores lógicos principais: AND (&&), OR (||) e NOT (!). Esses operadores permitem combinar condições para criar expressões mais complexas.

## Operador lógico AND (&&)

O operador lógico AND retorna verdadeiro (true) apenas quando ambas as condições que ele conecta forem verdadeiras.

Exemplo:

```cpp
#include <iostream>
using namespace std;

int main() {
    int idade = 25;
    bool possuiCarteiraMotorista = true;

    if (idade >= 18 && possuiCarteiraMotorista) {
        cout << "Pode dirigir." << endl;
    } else {
        cout << "Não pode dirigir." << endl;
    }

    return 0;
}
```

Neste exemplo, o programa verifica se a idade é maior ou igual a 18 e se possuiCarteiraMotorista é verdadeiro. Somente se ambas as condições forem verdadeiras, a mensagem "Pode dirigir." será exibida.

## Operador lógico OR (||)

O operador lógico OR retorna verdadeiro (true) quando pelo menos uma das condições que ele conecta é verdadeira.

Exemplo:

```cpp
#include <iostream>
using namespace std;

int main() {
    bool temDiploma = true;
    bool experienciaProfissional = false;

    if (temDiploma || experienciaProfissional) {
        cout << "Atende aos requisitos mínimos." << endl;
    } else {
        cout << "Não atende aos requisitos mínimos." << endl;
    }

    return 0;
}
```

Neste exemplo, o programa verifica se o candidato temDiploma ou experiência profissional. Se ao menos uma das condições for verdadeira, a mensagem "Atende aos requisitos mínimos." será exibida.

## Operador lógico NOT (!)

O operador lógico NOT inverte o valor de uma expressão. Ou seja, se a expressão é verdadeira, o operador NOT a torna falsa, e vice-versa.

Exemplo:

```cpp
#include <iostream>
using namespace std;

int main() {
    bool temCarteiraEstudante = false;

    if (!temCarteiraEstudante) {
        cout << "Você precisa de uma carteira de estudante para obter desconto." << endl;
    } else {
        cout << "Parabéns! Você tem desconto." << endl;
    }

    return 0;
}
```

Neste exemplo, o programa verifica se temCarteiraEstudante é falso (ou seja, o operador NOT inverte o valor). Se for o caso, a mensagem "Você precisa de uma carteira de estudante para obter desconto." será exibida.

Esses operadores lógicos podem ser combinados para criar expressões condicionais mais complexas e flexíveis em programas C++.

## Uso dos parênteses

O uso de parênteses em comparações dois a dois usando operadores lógicos é uma prática importante para garantir a correta avaliação das expressões e evitar ambiguidades. Cada linguagem de programação tem uma sequência que define a ordem de avaliação dos operadores. No C++, a sequência de precedência dos operadores é a seguinte, sendo as linhas de cima avaliadas primeiro:

```cpp
MAIOR PRECEDÊNCIA
() [] -> . ++ -- ! ~ * &
* / %
+ -
<< >>
< <= > >=
== !=
&
^
|
&&
||
?:
= += -= *= /= %= >>= <<= &= ^= |=
MENOR PRECEDÊNCIA
```

Ou seja, entre soma e multiplicação, a multiplicação é avaliada primeiro. Entre comparação e AND, a comparação é avaliada primeiro.

Minha sugestão é, sempre que você tiver dúvida, use parênteses para garantir a ordem de avaliação que você deseja. Por exemplo, suponha que você queira saber se uma pessoa pode viajar sozinha de ônibus intermunicipal.

Você pode se tiver 18 anos ou mais e tiver pago a passagem ou se tiver 60 anos ou mais, independentemente de ter pago a passagem ou não. pPara agrupar comparações AND, você pode usar parênteses para garantir que a comparação idade >= 18 && pagouAPassagem seja avaliada primeiro e depois o resultado seja combinado com a segunda comparação idade >= 60 usando o operador OR. Vamos ver os dois jeitos:

```cpp
    //PERIGOSO: juntando tudo
    if (idade >= 18 && pagouAPassagem || idade >= 60) {

    //SEGURO: separando e agrupando com parênteses
    if ((idade >= 18 && pagouAPassagem) || (idade >= 60)) {

```

## Comparação dois a dois

Não existe no C++ um operador lógico que permita comparar mais de dois operandos ao mesmo tempo. Para comparar mais de dois operandos, você precisa combinar operadores lógicos dois a dois. Por exemplo, para saber se a idade é maior ou igual a 18 e menor que 65, você precisa escrever assim:

- Errado: `18 >= idade > 65`
- Certo : `18 <= idade && idade < 65`

```cpp
    if (idade >= 18 && idade < 65) {
        cout << "Pode viajar sozinho." << endl;
    } else {
        cout << "Não pode viajar sozinho." << endl;
    }
```
