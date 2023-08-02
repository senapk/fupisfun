# Métodos da classe string

<!-- toc -->
- [Introdução](#introdução)
- [size() - Tamanho da string](#size---tamanho-da-string)
- [empty() - Verificar se a string está vazia](#empty---verificar-se-a-string-está-vazia)
- [clear() - Apagar todos os caracteres](#clear---apagar-todos-os-caracteres)
- [push_back() - Adicionar um caractere no final](#push_back---adicionar-um-caractere-no-final)
- [pop_back() - Remover o último caractere](#pop_back---remover-o-último-caractere)
- [insert() - Inserir uma string dentro de outra](#insert---inserir-uma-string-dentro-de-outra)
- [erase() - Apagar uma parte da string](#erase---apagar-uma-parte-da-string)
- [replace() - Substituir uma parte da string](#replace---substituir-uma-parte-da-string)
- [find() - Encontrar uma string dentro de outra](#find---encontrar-uma-string-dentro-de-outra)
- [substr() - Obter uma parte da string](#substr---obter-uma-parte-da-string)
- [compare() - Comparar duas strings](#compare---comparar-duas-strings)
- [at() - Acessar um caractere](#at---acessar-um-caractere)
<!-- toc -->

## Introdução

Strings são objetos da classe `std::string` em C++. Essa classe oferece uma variedade de métodos que permitem a manipulação eficaz de strings e simplificam o trabalho do programador. Enquanto classes, objetos e métodos são tópicos abordados na Programação Orientada a Objetos, para esta lição, é suficiente compreender que um método é uma função associada a uma string. Exploraremos algumas funções comuns que podem ser aplicadas para manipular qualquer string.

Para utilizar um método em uma string, é necessário criar uma string previamente. Com uma string à disposição, basta adicionar um ponto após o nome da variável e seguir com o nome do método que se deseja utilizar.

Por se tratar de uma função, é fundamental chamar o método com parênteses. Mesmo que nenhum parâmetro seja necessário, os parênteses devem ser inseridos. Caso haja parâmetros requeridos, estes devem ser colocados entre os parênteses.

Alguns métodos têm a capacidade de retornar um valor. Para utilizar esse valor, podemos armazená-lo em uma variável ou usá-lo diretamente em uma expressão.

A sintaxe é a seguinte:

```cpp
minha_string.metodo(); // sem parâmetros
minha_string.metodo(parametro1, parametro2); // com parâmetros

// Armazenando o valor de retorno em uma variável
tipo_da_variavel variavel = minha_string.metodo();
```

## size() - Tamanho da string

O método `size()` retorna o tamanho da string. O tamanho da string é o número de caracteres que ela possui. Por exemplo, a string `"Hello World"` possui 11 caracteres, portanto, o método `size()` retorna o valor 11.

- **Parâmetros**: nenhum
- **Retorno**: um inteiro não negativo com o tamanho da string

```cpp
#include <iostream>

int main() {
    std::string texto {"Hello World"};
    unsigned int tamanho = texto.size();
    std::cout << tamanho << std::endl; // 11
}
```

## empty() - Verificar se a string está vazia

O método `empty()` retorna `true` se a string estiver vazia e `false` caso contrário. Uma string vazia é uma string que não possui nenhum caractere. Por exemplo, a string `""` é uma string vazia.

- **Parâmetros**: nenhum
- **Retorno**: um booleano com o valor `true` se a string estiver vazia e `false` caso contrário

```cpp
#include <iostream>

int main() {
    std::string texto {"Hello World"};
    bool vazia = texto.empty(); // false
    
    if (vazia) {
        std::cout << "A string está vazia" << std::endl;
    } else {
        std::cout << "A string não está vazia" << std::endl;
    }
}
```

## clear() - Apagar todos os caracteres

O método `clear()` apaga todos os caracteres da string. Após o uso do método, a string fica vazia.

- **Parâmetros**: nenhum
- **Retorno**: nenhum

```cpp
#include <iostream>

int main() {
    std::string texto {"Hello World"};
    texto.clear(); // Apagando todos os caracteres
    std::cout << texto << std::endl; // ""
}
```

## push_back() - Adicionar um caractere no final

O método `push_back()` adiciona um caractere no final da string. O caractere a ser adicionado deve ser passado como parâmetro.

- **Parâmetros**: um caractere
- **Retorno**: nenhum

```cpp
#include <iostream>

int main() {
    std::string texto {"Hello World"};
    texto.push_back('!'); // Adicionando o caractere '!'
    std::cout << texto << std::endl; // "Hello World!"
}
```

## pop_back() - Remover o último caractere

O método `pop_back()` remove o último caractere da string.

- **Parâmetros**: nenhum
- **Retorno**: nenhum

```cpp
#include <iostream>

int main() {
    std::string texto {"Hello World"};
    texto.pop_back(); // Removendo o último caractere
    std::cout << texto << std::endl; // "Hello Worl"
}
```

> **Observação**: o método `pop_back()` não verifica se a string está vazia. Se a string estiver vazia, o programa irá apresentar um erro.

## insert() - Inserir uma string dentro de outra

O método `insert()` insere uma string dentro de outra string.

- **Parâmetros**: um inteiro com a posição onde a string será inserida, uma string com o texto a ser inserido
- **Retorno**: uma referência para a própria string (podemos ignorar isso por enquanto)

```cpp
#include <iostream>

int main() {
    // Posições:        0123456789*
    std::string texto {"Hello World"};
    texto.insert(6, "My Dear "); // Inserindo logo após o espaço
    std::cout << texto << std::endl; // "Hello Goodbye World"
}
```

> **Observação**: a posição onde a string será inserida é a posição onde o primeiro caractere da string será colocado. No exemplo acima, a string `"My Dear "` será inserida logo após o espaço, portanto, o primeiro caractere da string `"My Dear "` será colocado na posição 6.

## erase() - Apagar uma parte da string

O método `erase()` apaga uma parte da string. Para isso, é necessário passar a posição inicial e a quantidade de caracteres a serem apagados.

- **Parâmetros**: um inteiro com a posição inicial, um inteiro com a quantidade de caracteres a serem apagados
- **Retorno**: uma referência para a própria string (podemos ignorar isso por enquanto)

```cpp
#include <iostream>

int main() {
    // Posições:        0123456789*
    std::string texto {"Hello World"};
    texto.erase(5, 6); // Apagando " World" (6 caracteres a partir da posição 5, contando com o espaço)
    std::cout << texto << std::endl; // "Hello"
}
```

## replace() - Substituir uma parte da string

O método `replace()` substitui uma parte da string por outra string. Para isso, é necessário passar a posição inicial, a quantidade de caracteres a serem substituídos e a string que será colocada no lugar.

- **Parâmetros**: um inteiro com a posição inicial, um inteiro com a quantidade de caracteres a serem substituídos, uma string com o texto que será colocado no lugar
- **Retorno**: uma referência para a própria string (podemos ignorar isso por enquanto)

```cpp
#include <iostream>

int main() {
    // Posições:        0123456789*
    std::string texto {"Hello World"};
    texto.replace(0, 5, "Goodbye");

    std::cout << texto << std::endl;
}
```

## find() - Encontrar uma string dentro de outra

O método `find()` encontra uma string dentro de outra string. Para isso, é necessário passar a string que será procurada. O método retorna a posição onde a string foi encontrada. Caso a string não seja encontrada, o método retorna o valor `std::string::npos`.

- **Parâmetros**: uma string com o texto que será procurado
- **Retorno**: um inteiro com a posição onde a string foi encontrada ou `std::string::npos` caso a string não seja encontrada

```cpp
#include <iostream>

int main() {
    // Posições:        0123456789*
    std::string texto {"Hello World"};
    unsigned int posicao = texto.find("World"); // 6
    
    if (posicao != std::string::npos) {
        std::cout << "A string foi encontrada na posição " << posicao << std::endl;
    } else {
        std::cout << "A string não foi encontrada" << std::endl;
    }
}
```

## substr() - Obter uma parte da string

O método `substr()` retorna uma parte da string. Para isso, é necessário passar a posição inicial e a quantidade de caracteres que serão retornados.

- **Parâmetros**: um inteiro com a posição inicial, um inteiro com a quantidade de caracteres que serão retornados
- **Retorno**: uma string com a parte da string

```cpp
#include <iostream>

int main() {
    // Posições:        0123456789*
    std::string texto {"Hello World"};
    std::string parte = texto.substr(6, 5); // "World"
    std::cout << parte << std::endl;
}
```

> **Dica**: para obter uma parte da string a partir de uma posição, basta passar a posição inicial e o tamanho da string menos a posição inicial. Por exemplo, para obter a parte da string a partir da posição 6, basta passar a posição 6 e o tamanho da string menos 6.

## compare() - Comparar duas strings

O método `compare()` compara duas strings. Para isso, é necessário passar a string que será comparada. O método retorna um inteiro com o resultado da comparação. Se as strings forem iguais, o método retorna `0`. Se a string for menor que a string passada como parâmetro, o método retorna um número negativo. Se a string for maior que a string passada como parâmetro, o método retorna um número positivo.

- **Parâmetros**: uma string com o texto que será comparado
- **Retorno**: um inteiro com o resultado da comparação

```cpp
#include <iostream>

int main() {
    std::string texto {"Hello World"};
    int resultado = texto.compare("Hello World"); // 0
    
    if (resultado == 0) {
        std::cout << "As strings são iguais" << std::endl;
    } else if (resultado < 0) {
        std::cout << "A string é menor" << std::endl;
    } else {
        std::cout << "A string é maior" << std::endl;
    }
}
```

## at() - Acessar um caractere

O método `at()` retorna o caractere que está na posição passada como parâmetro.

- **Parâmetros**: um inteiro com a posição do caractere
- **Retorno**: um caractere

```cpp
#include <iostream>

int main() {
    // Posições:        0123456789*
    std::string texto {"Hello World"};
    char caractere = texto.at(6); // 'W'
    //   caractere = texto[6]; // É possível usar o operador [] para acessar um caractere
    std::cout << caractere << std::endl;
}
```

> **Obs:** o método `at()` verifica se a posição passada como parâmetro é válida. Caso não seja, o método lança uma exceção do tipo `std::out_of_range`. Já o operador `[]` não verifica se a posição é válida. Então, caso não seja, o programa pode apresentar um comportamento inesperado.
