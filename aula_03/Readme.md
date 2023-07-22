# Primeiro código

## Hello World

Um primeiro código em C++ é geralmente um programa simples que visa familiarizar os iniciantes com a sintaxe e os conceitos básicos da linguagem. Vamos criar um exemplo de um programa que exibe uma mensagem na tela.

```cpp
#include <iostream> // Inclui a biblioteca iostream, que permite a entrada/saída de dados.

//tudo que é escrito após // é um comentário e é ignorado pelo compilador.

int main() // A função main() é o ponto de partida de qualquer programa C++.
{
    std::cout << "Olá, mundo! Este é o meu primeiro programa em C++.\n";
    // A função std::cout é usada para exibir mensagens na tela.
    // O operador << é usado para inserir a mensagem que será exibida.
    // \n representa uma quebra de linha.

    return 0; // Indica que o programa foi concluído com sucesso. (opcional)
}
```

**Explicação:**

1. `#include <iostream>`: Esta linha inclui a biblioteca `iostream`, que fornece funcionalidades para entrada/saída de dados. É uma biblioteca padrão do C++ que nos permite usar as funções `cin` e `cout`.

2. `int main()`: Todo programa C++ precisa ter a função `main()`, que é o ponto de entrada do programa. O tipo de retorno `int` indica que a função `main()` deve retornar um valor inteiro (0 neste caso) para indicar o status de saída do programa.

3. `{}`: As chaves indicam o início e o fim do escopo da função `main()`. Todas as instruções dentro dessas chaves fazem parte do corpo da função.

4. `std::cout << "Olá, mundo! Este é o meu primeiro programa em C++." << std::endl;`: Esta linha utiliza a função `cout` da biblioteca `iostream` para exibir uma mensagem na tela. A mensagem é delimitada pelas aspas duplas (`"..."`). O operador `<<` é usado para inserir a mensagem na saída padrão. `\n` é usado para adicionar uma quebra de linha após a mensagem.

5. `return 0;`: O comando `return` é usado para finalizar a função `main()` e retornar um valor inteiro (0) que indica que o programa foi concluído com sucesso. Valores diferentes de zero podem indicar diferentes estados de saída do programa, mas, nesse caso, 0 é usado para sucesso. No caso da main em c++, esse retorno pode ser omitido.

Para executar o programa, basta compilar e depois executar o arquivo resultante. Ao ser executado, o programa exibirá a mensagem "Olá, mundo! Este é o meu primeiro programa em C++." no console ou na tela do terminal. Esse é um ponto de partida comum para aprender os fundamentos da linguagem C++ e começar a explorar conceitos mais avançados à medida que se avança no desenvolvimento de software com essa linguagem.

## Compilando manualmente

Para compilar, você precisa ter o g++ instalado. Crie e salve o arquivo como arquivo.cpp. Navegue até a pasta onde você salvou o arquivo. Ao dar o comando `ls` dentro da pasta, você deve encontrar o arquivo que salvou. Após isso compile e execute com os comandos.

**No windows:**

```bash
g++ -Wall -Wextra -Werror arquivo.cpp -o arquivo.exe
.\arquivo.exe
```

**No linux:**

```bash
g++ -Wall -Wextra -Werror arquivo.cpp -o arquivo.out
./arquivo.out
```

A primeira linha compila o código-fonte arquivo.cpp para gerar o arquivo executável arquivo.exe. Se houver qualquer erro ou **possível erro**, as flags -Wall -Wextra -Werror, vão impedir a finalização e avisar onde você deve consertar.

O comando `.\arquivo.exe` ou `./arquivo.out` é uma instrução para executar o código gerado pela primeira linha.

## Explicando as flags

No contexto do compilador GCC (GNU Compiler Collection) e do g++ (o compilador para C++ da GCC), as opções -Wall, -Wextra e -Werror são usadas para controlar a exibição de mensagens de aviso (warnings) e como esses avisos são tratados durante o processo de compilação. Aqui está uma explicação de cada uma delas:

-Wall (Ativar todos os avisos padrão):

A opção -Wall é usada para ativar a maioria dos avisos padrão do compilador. Quando você a utiliza, o g++ mostrará uma série de mensagens de aviso relacionadas a possíveis problemas no código-fonte que podem resultar em comportamentos indesejados ou erros em tempo de execução. No entanto, vale ressaltar que nem todos os avisos são ativados com essa opção; alguns avisos mais específicos ainda podem ser habilitados separadamente.

Por exemplo, se você tem um código com variáveis não inicializadas ou conversões implícitas, o -Wall pode emitir avisos relacionados a essas questões, incentivando boas práticas de programação.

-Wextra (Ativar mais avisos além dos habilitados por -Wall):

A opção -Wextra é usada para habilitar ainda mais avisos do compilador do que aqueles ativados por -Wall. Isso inclui avisos adicionais que podem não ser considerados obrigatórios ou padrão, mas que podem ser úteis para identificar problemas potenciais no código.

Ao usar -Wextra, o compilador será mais proativo na identificação de situações suspeitas no código-fonte, como variáveis não utilizadas ou conversões que podem levar a perda de dados.

-Werror (Tratar avisos como erros):

A opção -Werror é usada para tratar os avisos como erros durante o processo de compilação. Quando ativada, qualquer aviso gerado pelo compilador fará com que o processo de compilação seja interrompido e o código-fonte não será transformado em um executável até que todos os avisos sejam corrigidos.

Essa opção é frequentemente utilizada em projetos em que a equipe deseja garantir que o código esteja livre de avisos, incentivando práticas de programação mais seguras e consistentes. No entanto, é essencial ter cuidado ao habilitar -Werror, pois às vezes os avisos podem ser mais estritos do que o necessário e podem gerar falso-positivos. Nesses casos, é importante revisar os avisos cuidadosamente antes de tratá-los como erros.

Em resumo, -Wall e -Wextra são usados para habilitar avisos do compilador e -Werror é usado para tratá-los como erros. A combinação dessas opções pode ajudar a melhorar a qualidade do código, tornando-o mais seguro e livre de problemas potenciais. No entanto, ao usar -Werror, é fundamental garantir que os avisos são relevantes e não prejudicam o processo de compilação de forma imprópria.

## Segundo código

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
    
    char primeira_letra {'a'}; // Declara uma variável caractere (char) chamada primeira_letra e inicializa seu valor com 'a'.
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
