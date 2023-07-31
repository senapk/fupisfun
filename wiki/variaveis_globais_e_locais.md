# Variáveis Locais e Globais

<!-- toc -->
- [Variáveis Locais e Globais](#variáveis-locais-e-globais)
  - [Introdução](#introdução)
  - [Variáveis Locais](#variáveis-locais)
    - [Escopo de Bloco](#escopo-de-bloco)
    - [Variáveis Locais em Blocos Aninhados](#variáveis-locais-em-blocos-aninhados)
    - [Variáveis Locais Com o Mesmo Nome](#variáveis-locais-com-o-mesmo-nome)
    - [Duração de Armazenamento Automático](#duração-de-armazenamento-automático)
  - [Variáveis Globais](#variáveis-globais)
    - [Escopo de Arquivo](#escopo-de-arquivo)
    - [Variáveis Globais e Locais com o Mesmo Nome](#variáveis-globais-e-locais-com-o-mesmo-nome)
    - [Duração de Armazenamento Estático](#duração-de-armazenamento-estático)
  - [Melhores Práticas](#melhores-práticas)
<!-- toc -->

## Introdução

Imagine que você está escrevendo um código em C++ para resolver um problema. Em muitos casos, você precisa armazenar informações temporárias que serão usadas apenas em uma parte específica do seu código, como dentro de uma função. Essas são chamadas de variáveis locais. Porém, em outros casos, você precisa armazenar informações que serão usadas em várias partes do seu código. Essas são chamadas de variáveis globais.

## Variáveis Locais

A principal característica das variáveis locais é o seu "escopo", que é como uma "área de alcance" onde a variável pode ser usada. Quando uma variável está dentro do seu escopo, podemos acessá-la e utilizá-la, mas quando está fora do seu escopo, não podemos mais usar essa variável.

### Escopo de Bloco

O escopo de uma variável determina onde ela pode ser acessada dentro do código-fonte. Quando uma variável pode ser acessada, dizemos que ela está em escopo, e quando não pode ser acessada, dizemos que ela está fora de escopo. O escopo é uma propriedade em tempo de compilação, e tentar usar uma variável fora de escopo resultará em um erro de compilação.

As variáveis locais têm um escopo de bloco, o que significa que elas só existem dentro do bloco em que foram criadas. Um bloco é como um pedaço de código cercado por chaves "{ }".

Por exemplo:

```cpp
int main() { // Início do bloco do main
    int i = 5; // Variável local 'i' dentro do bloco do main é criada
    double d = 4.0; // Variável local 'd' dentro do bloco do main é criada
} // Fim do bloco do main, as variáveis 'i' e 'd' são destruídas
```

### Variáveis Locais em Blocos Aninhados

É possível colocar blocos dentro de blocos. Quando isso acontece, dizemos que um bloco está "aninhado" dentro de outro bloco. Quando um bloco está aninhado dentro de outro bloco, as variáveis definidas dentro do bloco aninhado só podem ser usadas dentro desse bloco aninhado.

Por exemplo:

```cpp
#include <iostream>

int main() { // Início do bloco do main
    int idade = 30; // Variável local 'idade' dentro do bloco do main é criada
    std::cout << "Minha idade é: " << idade << '\n';
    
    { // Início de um bloco aninhado
        int valor = 10; // Variável local 'valor' dentro do bloco aninhado é criada
        std::cout << "Valor é: " << valor << '\n';
    } // Fim do bloco aninhado, a variável 'valor' é destruída

    // std::cout << valor; // Isso geraria um erro, pois 'valor' não está mais em escopo aqui e já foi destruída

} // Fim do bloco do main, a variável 'idade' é destruída
```

### Variáveis Locais Com o Mesmo Nome

É possível ter variáveis locais com o mesmo nome em blocos diferentes. Apesar de terem o mesmo nome, essas variáveis são objetos diferentes e podem ter valores diferentes.

Para resolver essa ambiguidade dos nomes, o compilador faz uma busca hierárquica nos escopos. Quando o compilador encontra uma variável, ele procura por uma variável com o mesmo nome dentro do escopo atual. Se ele não encontrar, ele procura no escopo anterior, e assim por diante. Se ele não encontrar em nenhum escopo, ele gera um erro de compilação.

Exemplo:

```cpp
int main() { // Início do bloco do main
    int x = 2; // variável local x dentro do bloco do main é criada

    { // Início de um bloco aninhado
        int x = 3; // variável local x dentro do bloco aninhado é criada (essa é uma variável diferente da anterior)
        std::cout << x << '\n'; // 3
    } // Fim do bloco aninhado, a variável x (a de valor 3) é destruída

    std::cout << x << '\n'; // 2
} // Fim do bloco do main, a variável x (a de valor 2) é destruída
```

### Duração de Armazenamento Automático

As variáveis locais têm uma "duração de armazenamento automático", o que significa que elas são criadas quando o programa entra no bloco onde foram definidas e são destruídas quando o programa sai desse bloco. Isso acontece automaticamente, sem precisarmos nos preocupar em criar ou destruir essas variáveis manualmente.

Por exemplo:

```cpp
#include <iostream>

int main() {
    { // Início de um bloco aninhado
        int numero = 5; // Variável local 'numero' dentro do bloco aninhado é criada
        std::cout << "Número é: " << numero << '\n';
    } // A variável local 'numero' é destruída ao final do bloco aninhado

    // std::cout << numero; // Erro, pois a variável 'numero' não é acessível aqui, pertence ao bloco aninhado
}
```

## Variáveis Globais

Em C++, além das variáveis locais (definidas dentro do corpo de uma função ou bloco), também podemos declarar variáveis globais. Essas variáveis são declaradas fora de qualquer função ou bloco e podem ser acessadas de qualquer lugar do programa.

### Escopo de Arquivo

A principal característica das variáveis globais é que elas têm um escopo de arquivo, o que significa que elas podem ser acessadas de qualquer lugar do arquivo em que foram declaradas. Podemos imaginar que o arquivo é um bloco gigante que envolve todo o código-fonte do programa, em que a primeira linha do arquivo é o início do bloco e a última linha do arquivo é o final do bloco.

Por convenção, as variáveis globais são declaradas no topo de um arquivo, abaixo dos includes. Veja um exemplo de declaração de uma variável global:

```cpp
#include <iostream>

int numeroGlobal = 20; // Variável global declarada fora de qualquer função ou bloco

int main() {
    std::cout << "Posso acessar a variável global numeroGlobal aqui: " << numeroGlobal << '\n'; // 20
}
```

### Variáveis Globais e Locais com o Mesmo Nome

Quando você tem variáveis globais e locais com o mesmo nome no seu programa, elas são tratadas como duas variáveis distintas, mesmo que tenham o mesmo nome. Isso acontece porque as variáveis globais e locais têm escopos diferentes.

Se houver uma variável local com o mesmo nome, o compilador usará a variável local, pois o escopo mais interno possui prioridade.

Exemplo:

```cpp
#include <iostream>

int numero = 20; // Variável global

int main() {
    int numero = 10; // Variável local com o mesmo nome da variável global
    std::cout << "Valor de numero: " << numero << '\n'; // 10
}
```

### Duração de Armazenamento Estático

As variáveis globais têm uma "duração de armazenamento estático", o que significa que elas são criadas quando o programa inicia e são destruídas quando o programa termina. Isso significa que as variáveis globais existem durante toda a execução do programa.

## Melhores Práticas

- Defina as variáveis no escopo mais limitado possível. Isso significa que devemos declarar as variáveis dentro do bloco onde realmente as usaremos e não em blocos externos sem necessidade.

- Evite variáveis globais. Elas podem ser acessadas de qualquer lugar do programa, o que pode tornar o código mais difícil de entender e depurar. Além disso, as variáveis globais podem ser modificadas por qualquer função, o que pode causar efeitos colaterais indesejados.

- Evite variáveis globais com o mesmo nome de variáveis locais. Isso pode causar confusão e erros difíceis de encontrar.
