# Entrada de dados básica com `cin`

<!-- toc -->
- [Introdução](#introdução)
- [Como funciona o `cin`](#como-funciona-o-cin)
- [Tipos de dados](#tipos-de-dados)
- [Espaços e quebras de linha](#espaços-e-quebras-de-linha)
- [Função `getline`](#função-getline)
- [Curiosidades](#curiosidades)
  - [Limpando o buffer](#limpando-o-buffer)
  - [Verificando se a leitura deu certo](#verificando-se-a-leitura-deu-certo)
<!-- toc -->

## Introdução

Em C++, a entrada padrão (normalmente o teclado) pode ser lida utilizando-se o objeto `cin`, que faz parte da biblioteca padrão `iostream`. O `cin` é responsável pela leitura de dados inseridos pelo usuário durante a execução do programa.

## Como funciona o `cin`

Para lermos dados através do `cin` usamos o operador `>>`, chamado de operador de extração. Observe abaixo:

```cpp
#include <iostream>

using namespace std;

int main() {
    int a {}, b {}, c {};
    
    cout << "Digite o valor do número a: ";
    cin >> a; // Lê um inteiro e armazena em a
    cout << "Digite o valor do número b: ";
    cin >> b; // Lê um inteiro e armazena em b
    cout << "Digite o valor do número c: ";
    cin >> c; // Lê um inteiro e armazena em c

    cout << "Digite novos valores para a, b e c: ";
    cin >> a >> b >> c; // O operador pode ser encadeado
}
```

A cada instrução de leitura a execução do código é pausada até que aquele dado seja informado. No caso do terminal, até que o usuário digite a informação e aperte `Enter`.

Internamente o `cin` utiliza um buffer (um armazenamento temporário na memória) para guardar os dados recebidos pela entrada padrão. Dessa forma se o usuário digitar os valores de `a`, `b` e `c` na instrução `cin >> a`, o código não será pausado na leitura de `b` e `c`, pois esses valores já estão disponíveis no buffer.

## Tipos de dados

O `cin` realiza uma leitura orientada a tipos de dados. Isso significa que a leitura é feita baseada no tipo de dado da variável. Se você deseja ler o nome de uma pessoa, a variável precisa possuir o tipo `string` e se você deseja ler a idade de uma pessoa, a variável precisa possuir o tipo `int`. Sempre use os tipos correspondentes ao tipo de dado esperado.

## Espaços e quebras de linha

Por padrão o `cin` entende que uma informação acabou baseado pelos caracteres de espaço e depois caracteres de quebra de linha. Por exemplo:

```cpp
#include <iostream>

using namespace std;

int main() {
    string nome;

    cout << "Digite o seu nome: ";
    cin >> nome;
}
```

Caso o usuário digitasse *"Maria da Silva"*, apenas *"Maria"* seria armazenado na variável `nome`, pois o `cin` entende que o espaço em branco delimita duas strings.

## Função getline

Para fazer a leitura até uma quebra de linha, ou seja, até onde o usuário apertou enter, usamos a função `getline`.

```cpp
#include <iostream>

using namespace std;

int main() {
    string nome;

    cout << "Digite o seu nome: ";
    getline(cin, nome);
}
```

A função `getline` recebe dois parâmetros: a origem dos dados, e o destino. Nesse caso informamos que queremos ler os dados do `cin` (poderíamos ler de um arquivo de texto também) e desejamos salvar essa informação na variável `nome`.

Agora o nome *"Maria da Silva"* seria armazenado completo dentro da variável.

## Curiosidades

### Limpando o buffer

Um problema conhecido na leitura de textos são os caracteres finais indesejados. Por exemplo, veja o seguinte o código:

```cpp
#include <iostream>

using namespace std;

int main() {
    int idade;
    string nome;

    cout << "Digite a sua idade: ";
    cin >> idade;
    cout << "Digite o seu nome: ";
    getline(cin, nome);

    cout << nome << endl;
}
```

Após digitar a idade o programa encerra sem esperar o usuário digitar o valor do nome. Isso acontece por conta do buffer utilizado pelo `cin`. Se o usuário digitasse que possui 20 anos de idade, o buffer seria preenchido assim: `20\n`, sendo esse `\n` o `Enter` que foi apertado.

Quando a instrução `cin >> idade` é executada, o 20 é retirado do buffer. Quando a instrução `getlin(cin, nome)` é executada, o `cin` observa que já possui uma `string` no buffer, o `\n` da leitura passada, e dessa forma apenas esse caractere é enviado para a variável.

Para resolver isso, precisamos fazer uma limpeza no buffer antes da leitura da `string`, usando o método `cin.ignore()`, que como o nome sugere, ignora o próximo caractere em branco (espaços, tabulaçoes e quebras de linha).

```cpp
#include <iostream>

using namespace std;

int main() {
    int idade;
    string nome;

    cout << "Digite a sua idade: ";
    cin >> idade;

    cout << "Digite o seu nome: ";
    cin.ignore(); // Ignora o '\n' restante
    getline(cin, nome);

    cout << nome << endl;
}
```

Essa é a versão corrigida so exemplo anterior.

### Verificando se a leitura deu certo

Como já explicado, o `cin` faz uma leitura orientada a tipos de dados, mas isso não impede o usuário de digitar algo inválido como entrada.

```cpp
#include <iostream>

using namespace std;

int main() {
    int numero;

    cout << "Digite um número: ";
    cin >> numero;
}
```

Nada impede o usuário de digitar *"zero"*, o que não funcionaria no código, pois esperamos ler um inteiro. Podemos verificar se a leitura deu certo usando uma estrutura de seleção com base no valor retornado do operador de extração (`>>`).

```cpp
#include <iostream>

using namespace std;

int main() {
    int numero;

    cout << "Digite um número: ";

    if (cin >> numero) {
        cout << "Você digitou o número " << numero << endl;
    } else {
        cout << "Houve um erro na leitura\n";
    }
}
```
