# O problema da divisão de dois inteiros

- [Introdução](#introdução)
- [Exemplo do problema](#exemplo-do-problema)
- [Resolvendo o problema](#resolvendo-o-problema)
  - [Literais como ponto flutuante](#literais-como-ponto-flutuante)
  - [Realizando um cast](#realizando-um-cast)

## Introdução

Neste texto, abordaremos um problema comum nas operações aritméticas em C++: a divisão inteira. Mostraremos porque ela acontece e como podemos resolver.

## Exemplo do problema

```cpp
#include <iostream>

using namespace std;

int main() {
    cout << 5 / 2 << endl;
}
```

O resultado esperado dessa operação é o valor 2.5, pois esse é o valor de `5 / 2`. No entando, se você executar esse código verá que o resultado mostrado é 2.

Isso acontece por conta da forma como o C++ trata os tipos de dados dentro de uma operação aritmética. Observe que os dois operandos, 5 e 2, são números inteiros, dessa forma, a linguagem realizará apenas uma divisão inteira, que não resulta em casas decimais.

## Resolvendo o problema

A abordagem de resolução desse problema é transformar pelo menos um dos valores em um tipo de dado de ponto flutuante, dessa forma a divisão não será inteira.

### Literais como ponto flutuante

Uma das formas mais simples de resolver esse problema quando se utiliza apenas números literais, ou seja, os valores estão escritos no código e não em variáveis, é acrescentar um ponto decimal em pelo menos um desses números.

Dessa forma, o exemplo anterior ficaria assim:

```cpp
#include <iostream>

using namespace std;

int main() {
    cout << 5 / 2.0 << endl;
}
```

Apenas a substituição do 2 por 2.0 já resolve o nosso problema.

### Realizando um cast

A solução anterior funciona quando usamos números literais, mas não quando lidamos com variáveis, pois não temos como adicionar um ponto decimal após o nome delas.

Dessa forma, precisamos realizar um cast como visto em [Tipos de dados e casts](./tipos_primitivos.md.md). O nosso primeiro exemplo ficaria assim:

```cpp
#include <iostream>

using namespace std;

int main() {
    cout << 5 / (double) 2 << endl;
}
```

Caso utilizássemos variáveis:

```cpp
#include <iostream>

using namespace std;

int main() {
    int a = 5;
    int b = 2;
    cout << a / (double) b << endl;
}
```
