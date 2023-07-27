# Casting

Em C++, o casting é uma operação que permite converter explicitamente um valor de um tipo para outro. Isso é útil quando queremos garantir que um determinado valor seja tratado como outro tipo. Existem vários tipos de cast em C++, sendo um deles o C-style cast, também conhecido como cast tradicional do C.

## (Cast Tradicional do C)

Essa é uma forma de conversão que herda a sintaxe do cast utilizado em C.

A sintaxe do C-style cast é a seguinte:

```c++
(NovoTipo) expressao;
```

Onde NovoTipo é o tipo de dados para o qual desejamos converter a expressão.

## Exemplos

- **Conversão de Inteiro para Ponto Flutuante:**

```c++
int idade = 25;
double idadeEmAnos = (double)idade;
```

Neste exemplo, temos uma variável idade do tipo `int` que armazena o valor 25. Usando o casting, convertemos explicitamente o valor de idade para o tipo `double`, atribuindo-o à variável idadeEmAnos. Dessa forma, garantimos que a conversão seja realizada corretamente e que o valor seja tratado como um número de ponto flutuante.

- **Conversão de Ponto Flutuante para Inteiro:**

```c++
double preco = 25.99;
int precoInteiro = (int)preco;
```

Neste exemplo, temos uma variável preco do tipo `double` que armazena o valor 25.99. Ao usar o casting, convertemos explicitamente o valor de preco para o tipo `int`, atribuindo-o à variável precoInteiro. Nesse caso, o valor decimal é truncado, e a variável precoInteiro armazena o valor 25.

- **Conversão de Char para Int:**

```c++
char caractere = 'A';
int valorAscii = (int)caractere;
```

Neste exemplo, temos uma variável caractere do tipo `char` que armazena o caractere 'A'. Ao utilizar o casting, convertemos explicitamente o valor de caractere para o tipo `int`, atribuindo-o à variável valorAscii. O casting converterá o valor ASCII do caractere 'A' (que é 65) para o tipo `int`, e a variável valorAscii armazenará o valor 65.

## Atenção

É importante ter cuidado ao usar um casting, pois ele pode permitir conversões que são perigosas ou que possam resultar em perda de dados, como na conversão de `double` para `int`, em que a parte decimal (.99) se perdeu.

O C++ possui outros tipos de castings mais seguros e específicos para algumas situações, como o **Static Cast**, **Dynamic Cast**, **Const Cast** e **Reinterpret Cast**.
