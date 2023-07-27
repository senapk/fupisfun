# Modificadores de Tipo

O C++ permite o uso de modificadores para ajustar os intervalos de valores armazenados por certos tipos de dados. Os principais modificadores são `short`, `long`, `signed` e `unsigned`. Também existe o modificador `const`, que permite a criação de constantes.

## Modificador `short`

Reduz o intervalo de valores do tipo, ocupando menos espaço em memória.

- Só pode ser usado no tipo `int`.

Exemplo:

```c++
int contador1;
short int contador2;
// O contador2 armazena um intervalo de valores menor que o contador1.
```

## Modificador `long`

Aumenta o intervalo de valores dos tipos, permitindo representar números maiores.

- Pode ser usado nos tipos `int` e `double`.

Exemplo:

```c++
int contador1;
long int contador2;
// O contador2 pode representar um intervalo de valores inteiros maior que o contador1.
```

```c++
double contador1;
long double contador2;
// O contador2 pode representar um intervalo de valores reais maior que o contador1.
```

## Modificador `signed`

Indica que um tipo pode representar tanto valores positivos como negativos.

- Pode ser usado nos tipos `int` e `char`.
- No C++, o tipo `int` é signed por padrão. Ou seja, `int` é equivalente a `signed int`, o que significa que esse tipo pode representar valores negativos e positivos dentro de um determinado intervalo.

Exemplo:

```c++
int contador1;
signed int contador2;
// São equivalentes, ambos podem representar valores negativos e positivos.
```

```c++
signed char letra;
// O letra pode representar valores negativos e positivos.
```

## Modificador `unsigned`

Indica que um tipo pode representar apenas valores não negativos (ou seja, valores positivos e zero).

- Pode ser usado nos tipos `int` e `char`;
- Isso permite que o intervalo de valores armazenados seja totalmente deslocado para o lado positivo, dobrando o intervalo de valores possíveis para o tipo de dado.

Exemplo:

```c++
int contador1;
unsigned int contador2;
// O contador2 só pode representar valores de 0 a algum valor positivo máximo. O intervalo é dobrado em relação ao contador1.
```

```c++
unsigned char letra;
// O letra pode representar valores de 0 a algum valor positivo máximo.
```

## Modificador `const`

Tornar uma variável imutável, ou seja, seu valor não pode ser alterado após a atribuição inicial. Isso é útil para garantir a integridade de variáveis que não devem ser modificadas durante a execução do programa.

- Pode ser usado em todos os tipos.

Exemplo:

```c++
const int quantidade = 10;
const float altura = 10.5;
const long double pi = 3.14159265359;
const unsigned char letra = 'a';
// O valor de nenhuma dessas variáveis (ou melhor, constantes) pode ser modificado após a atribuição inicial.
```
