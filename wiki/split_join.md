# Métodos `split()` e `join()`

<!-- toc -->
<!-- toc -->

Os métodos `split()` e `join()` são métodos de string que permitem quebrar uma string em várias strings menores e juntar várias strings em uma única string, respectivamente.

## Método `split()`

O método `split()` recebe como parâmetro um caractere e retorna um vetor de strings. O vetor de strings é composto por todas as strings que estavam separadas pelo caractere passado como parâmetro.

- **Exemplo**

```cpp
#include <iostream>
#include <fn.hpp> //biblioteca de funções úteis
                  //para manipulação de strings
                  //feita pelo professor David Sena
                  //https://github.com/senapk/cppaux

int main(){

    // Declaração de uma string
    std::string s = "O rato roeu a roupa do rei de Roma"; 

    // Quebra a string s em várias strings menores e armazena em um vetor
    std::vector<std::string> v = fn::split(s, ' ');

    // Imprime o vetor de strings
    for (auto e : v)
        std::cout << e << std::endl;
}
```

- **Saída**

```out
O
rato
roeu
a
roupa
do
rei
de
Roma
```

- O caractere `' '` (espaço) foi passado como parâmetro para o método `split()`, então a string foi quebrada em várias strings menores. A condição para quebrar a string é que o caractere passado como parâmetro seja encontrado.
- Na saída, cada string do vetor está em uma linha **diferente**, mostrando que o vetor de strings foi criado **corretamente**.

## Método `join()`

O método `join()` recebe como parâmetro um vetor de strings e retorna uma única string. A string retornada é composta pela junção de todas as strings do vetor de strings passado como parâmetro, separadas por um caractere.

- **Exemplo**

```cpp
#include <iostream>
#include <fn.hpp> //biblioteca de funções úteis
                  //para manipulação de strings
                  //feita pelo professor David Sena
                  //https://github.com/senapk/cppaux

int main(){
 
    // Declaração de um vetor de strings
    std::vector<std::string> v = {"O", "rato", "roeu", "a", "roupa", "do", "rei", "de", "Roma"};

    // Junta todas as strings do vetor v em uma única string
    std::string s = fn::join(v, ' ');

    // Imprime a string s
    std::cout << s << std::endl;
}
```

- **Saída**

```out
O rato roeu a roupa do rei de Roma
```

- O caractere `' '` (espaço) foi passado como parâmetro para o método `join()`, então todas as strings do vetor foram juntadas em uma única string, separadas por um espaço. Dessa forma, a string retornada foi `"O rato roeu a roupa do rei de Roma"`, que é a junção de todas as strings do vetor `v`.
