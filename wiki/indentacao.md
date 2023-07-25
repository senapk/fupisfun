# Indentação

[](toc)

- [Como indentar](#como-indentar)
- [PIADINHA](#piadinha)
[](toc)

## Como indentar

A indentação é uma forma de alinhar o código para facilitar a leitura e compreensão. Ele serve para indicar em que escopo aquela linha está, ou seja, de qual bloco lógico ela faz parte.

Cada vez que um novo escopo é iniciado, seja uma função, um if, um for, um while, um switch, etc, o código deve aumentar um nível de indentação. Cada vez que um escopo é fechado, o código deve diminuir um nível de indentação.

A indentação é feita através da tecla TAB. Cada TAB aumenta um nível de indentação. Cada SHIFT+TAB diminui um nível de indentação.

Alguns editores utilizam 4 espaços para indentar, como o vscode, outros como o Replit optam por utilizar 2 espaços. Desde que você seja consistente, não há problema em utilizar um ou outro.

A indentação correta cria uma aparência de escada no código, como no exemplo abaixo:

![escada](https://wiki.hippoedit.com/_media/view/indent-guides.png)

```cpp
#include <iostream>

bool eh_primo(int value) {
    if (value <= 1) {
        return false;
    }
    for (int i = 2; i < value; i++) {
        if (value % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    std::cout << "Digite o valor maximo: ";
    
    int maximo {};
    std::cin >> maximo;

    std::cout << "Os numeros primos ate " << maximo << std::endl;
    for (int i = 0; i <= maximo; i++) {
        std::cout << i;
        if (eh_primo(i)) {
            std::cout << " sim";
        } else {
            std::cout << " nao";
        }
        std::cout << std::endl;
    }
}
```

## PIADINHA

Se você já jogou D&D, provavelmente já ouviu falar de alinhamentos. Alguém pegou os vários estilos de indentação e fez uma brincadeira com os alinhamentos. 

![alinhamentos](https://pbs.twimg.com/media/Fm8AIOzXEBY8NQZ?format=jpg&name=small)

Sugerimos apenas os alinhamentos `Lawful Good` (Ordeiro e Bom) e `Chaotic Good` (Caótico e Bom).
