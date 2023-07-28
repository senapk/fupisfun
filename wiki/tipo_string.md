
o padrão é um valor não modificável, uma constante.

```cpp
#include <iostream>

int main() {
    auto v = "banana madura"; //const char*

    std::string s = "banana"; //converte para string

    auto g = std::string("banana estragada"); //std::string

}

```

a string é uma classe, possui métodos, pode ser alterada, será estudada mais a fundo no futuro.

Por enquanto, se você quiser guardar um texto numa variável, use string.