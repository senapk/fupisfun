# Atribuição e incremento

<!-- toc -->
- [Introdução](#introdução)
- [Operadores de Atribuição](#operadores-de-atribuição)
- [Operadores de Incremento e Decremento](#operadores-de-incremento-e-decremento)
<!-- toc -->

## Introdução

Além do operador básico de atribuição, o `=`, no C++ temos como realizar uma atribuição e operação matemática ao mesmo tempo de maneira mais concisa com operadores especiais.

## Operadores de Atribuição

O operador de atribuição básico em C++ é o `=`. Ele é usado para atribuir um valor a uma variável. A sintaxe é simples:

```cpp
int x = 10;
```

Neste exemplo, a variável `x` é declarada como um inteiro e recebe o valor 10 através do operador de atribuição.

Além do operador de atribuição simples, existem operadores de atribuição combinados que realizam uma operação aritmética e atribuem o resultado à variável. Os operadores de atribuição combinados são:

- `+=`: Adição e atribuição
- `-=`: Subtração e atribuição
- `*=`: Multiplicação e atribuição
- `/=`: Divisão e atribuição
- `%=`: Módulo (resto da divisão) e atribuição

Aqui está um exemplo de uso do operador `+=`:

```cpp
int y = 5;
y += 3; // Agora, y é igual a 8 (5 + 3)
```

Esse operador é útil para atualizar o valor de uma variável de forma concisa, evitando a repetição de código.

## Operadores de Incremento e Decremento

Os operadores de incremento (`++`) e decremento (`--`) são utilizados para aumentar ou diminuir o valor de uma variável em uma unidade, respectivamente.

O operador de incremento `++` adiciona 1 ao valor da variável:

```cpp
int a = 3;
a++; // Agora, a é igual a 4
```

Da mesma forma, o operador de decremento `--` subtrai 1:

```cpp
int b = 8;
b--; // Agora, b é igual a 7
```

É importante mencionar que os operadores de incremento e decremento podem ser usados de duas formas: **antes** ou **depois** do nome da variável. Se usados **antes**, a variável é incrementada/decrementada antes de ser usada na expressão. Se usados **depois**, a variável é usada primeiro e depois incrementada/decrementada.

Por exemplo:

```cpp
int c = 5;
int d = ++c; // Primeiro c é incrementado e depois d recebe o valor
// Agora, c e d são iguais a 6

int e = 5;
int f = e++; // f recebe o valor de e (5) e depois o incremento acontece
// e é igual a 6, mas f é igual a 5
```

O código acima é interpretado pelo compilador como:

```cpp
int c = 5;

//int d = ++c; //incrementa antes e usa depois
c += 1; int d = c;


int e = 5;
//int f = e++;  //usa antes e incrementa depois
int f = e; e += 1;
```
