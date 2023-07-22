# Segundo código

```cpp
#include <iostream>

int main()
{
    int idade {0}; // Declara uma variável inteira chamada idade e inicializa seu valor com 0.
    std::cout << "Qual a sua idade? "; // Exibe a mensagem "Qual a sua idade?" na tela.
    std::cin >> idade; // Lê um valor inteiro do usuário e o armazena na variável idade.

    double altura {0.0}; // Declara uma variável ponto flutuante (double) chamada altura e inicializa seu valor com 0.0.
    std::cout << "Qual a sua altura? ";
    std::cin >> altura;
    
    char primeira_letra {'a'}; // Declara uma variável caractere (char) chamada primeira_letra e inicializa seu valor com 'a'. Um char é um único caractere e deve ser escrito entre aspas simples.
    
    std::cout << "Qual a primeira letra do seu nome? ";
    std::cin >> primeira_letra;

    std::cout << "A sua idade é " << idade << " anos." << std::endl; // std::endl é usado para adicionar uma quebra de linha.
    std::cout << "A sua altura é " << altura << " metros." << '\n';  // \n também é usado para adicionar uma quebra de linha.
    std::cout << "A primeira letra do seu nome é " << primeira_letra << ".\n";

    return 0; // Termina a função main() e retorna 0 para indicar que o programa foi concluído com sucesso.
}
```

**Explicação:**

1. `int idade {0};`: Declara uma variável inteira chamada `idade` e inicializa seu valor com 0.

2. `double altura {0.0};`: Declara uma variável ponto flutuante (double) chamada `altura` e inicializa seu valor com 0.0.

3. `char primeira_letra {'a'};`: Declara uma variável caractere (char) chamada `primeira_letra` e inicializa seu valor com 'a'.

4. `std::cout << "Qual a sua idade? ";`: Exibe a mensagem "Qual a sua idade?" na tela.

5. `std::cin >> idade;`: Lê um valor inteiro do usuário e o armazena na variável `idade`.

6. `std::cout << "Qual a sua altura? ";`: Exibe a mensagem "Qual a sua altura?" na tela.

7. `std::cin >> altura;`: Lê um valor ponto flutuante (double) do usuário e o armazena na variável `altura`.

8. `std::cout << "Qual a primeira letra do seu nome? ";`: Exibe a mensagem "Qual a primeira letra do seu nome?" na tela.

9. `std::cin >> primeira_letra;`: Lê um caractere do usuário e o armazena na variável `primeira_letra`.

10. `std::cout << "A sua idade é " << idade << " anos." << std::endl;`: Exibe a mensagem "A sua idade é `idade` anos." na tela. `std::endl` é usado para adicionar uma quebra de linha.
