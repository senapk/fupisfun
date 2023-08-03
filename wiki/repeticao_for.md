# Estrutura de repetição for

<!-- toc -->
- [Estrutura de repetição for](#estrutura-de-repetição-for)
  - [Introdução](#introdução)
  - [Funcionamento genérico do loop `for`](#funcionamento-genérico-do-loop-for)
  - [Exemplos de utilização do `for`](#exemplos-de-utilização-do-for)
    - [Exemplo 1: Iteração Crescente](#exemplo-1-iteração-crescente)
    - [Exemplo 2: Iteração Decrescente](#exemplo-2-iteração-decrescente)
  - [Equivalência entre o `while` e o `for`](#equivalência-entre-o-while-e-o-for)
    - [Exemplo de equivalência do `for` com `while`](#exemplo-de-equivalência-do-for-com-while)
  - [Outras formas de usar o `for`](#outras-formas-de-usar-o-for)
    - [Iterar uma string com `for`](#iterar-uma-string-com-for)
    - [Iterar um array com `for`](#iterar-um-array-com-for)
<!-- toc -->

## **Introdução:**

A linguagem de programação C++ oferece várias estruturas de controle para
**facilitar** o desenvolvimento de programas. Uma das estruturas mais poderosas e
versáteis é o loop `for`. O `for` permite que um bloco de código seja
repetido várias vezes com base em uma **condição específica**. Essa estrutura
é amplamente utilizada para iterar por listas, sequências e realizar tarefas
repetitivas de maneira eficiente.

## **Funcionamento genérico do loop `for`:**

O loop `for` em C++ tem a seguinte sintaxe geral:

```c++
for (inicialização; condição; atualização) {
    // Código a ser executado repetidamente
}
```

- **Inicialização:** Uma expressão que é executada **apenas uma vez**, antes do
início do loop. Geralmente, é usada para definir ou inicializar a variável
de controle do loop.

- **Condição:** Uma expressão que é avaliada **antes de cada iteração** do
loop. Se a condição for verdadeira, o bloco de código dentro do `for` será
executado. Se a condição for falsa, o loop será encerrado.

- **Atualização:** Uma expressão que é executada **após cada iteração** do
loop. É normalmente usada para modificar a variável de controle do loop, de
forma que a condição possa eventualmente se tornar falsa e o loop seja
interrompido.

## **Exemplos de utilização do `for`**

### **Exemplo 1**: Iteração Crescente

Vamos criar um programa simples que imprime de forma crescente os números de
1 a 5 usando o loop
`for`:

```cpp
#include <iostream>

int main() {
    for (int i = 1; i <= 5; i++) {
        std::cout << i << " "; // 1 2 3 4 5
    }
    std::cout << '\n';
    return 0;
}
```

- **Inicialização**: `int i = 1` define a variável i com o valor inicial 1.

- **Condição**:  `i <= 5` é verificada antes de cada iteração do loop. Enquanto i
for menor ou igual a 5, o loop continuará sendo executado.

- **Atualização**: A expressão `i++` é executada após cada iteração e incrementa
o valor de i em 1.

Neste exemplo, o loop `for` é utilizado para iterar a variável i de 1 até 5
(inclusive). A cada iteração, o valor de i é impresso na tela.

### **Exemplo 2**: Iteração Decrescente

Podemos facilmente inverter a direção do loop para contar de 5 até 1 usando
o loop `for`:

```cpp
#include <iostream>

int main() {
    for (int i = 5; i >= 1; i--) {
        std::cout << i << " "; // 5 4 3 2 1 
    }
    std::cout << '\n';
    return 0;
}
```

- **Inicialização**: `int i = 5` define a variável i com o valor inicial 5.

- **Condição**:  `i >= 1` é verificada antes de cada iteração do loop. Enquanto i
for maior ou igual a 1, o loop continuará sendo executado.

- **Atualização**: A expressão `i--` é executada após cada iteração e incrementa
o valor de i em 1.

Neste exemplo, o loop começa com o valor 5 e decrementa `i` a cada iteração
até que o valor seja igual a 1, imprimindo os números de 5 a 1.

## **Equivalência entre o `while` e o `for`:**

O `for` e o "while" são estruturas de controle **diferentes**, mas é possível
expressar o **mesmo código** usando ambos. O "while" é geralmente usado quando a
condição de repetição é **desconhecida** antes de entrar no loop, enquanto o
`for` é mais adequado quando o **número de iterações é conhecido** ou quando
é necessário definir uma variável de controle específica.

### **Exemplo de equivalência do `for` com `while`:**

Vamos reescrever **Exemplo 1** usando um loop "while":

```cpp
#include <iostream>

int main() {
    int i = 1; //Inicialização
    while (i <= 5) { //Condição
        std::cout << i << " ";
        i++; //Atualização
    }
    std::cout << '\n';
    return 0;
}
```

Observe que a variável `i` foi inicializada antes do loop e incrementada
dentro do loop, assim como a atualização no `for`.

## **Outras formas de usar o `for`:**

### **Iterar uma string com `for`:**

O loop `for` pode ser usado para percorrer
os caracteres de uma string.

```cpp
#include <iostream>

int main() {
    std::string message = "Hello";
    for (size_t i = 0; i < message.length(); i++) {
        std::cout << "[" << i << "] -> "<< message[i] << '\n';
    }
    return 0;
}
```

Neste exemplo, menssage.length() retorna o **tamanho da string**, assim cada caractere
da string "Hello" é acessado usando o índice `i` e é impresso na tela junto com o
valor do seu índice.
  
Saida do programa:

```cpp
[0] -> H
[1] -> e
[2] -> l
[3] -> l
[4] -> o
```

### **Iterar um array com `for`:**

Mais a frente serão mostradas estruturas chamadas `arrays` que armazenam cadeias
de valores na memória. Muitas vezes será necessário analizar sequencialmente
todos os valores de um array. Assim, o `for` se torna uma maneira mais **simples
e direta de realizar essas iterações.**

---

Em resumo, o loop `for` é uma poderosa estrutura de repetição em C++ que
oferece **flexibilidade para controlar** o fluxo de um programa e executar tarefas
repetitivas de maneira eficiente. Através de sua **sintaxe simples**, é possível
implementar uma ampla variedade de algoritmos e iterações em diferentes
contextos de programação. Sua versatilidade e aplicabilidade tornam o loop
`for` uma escolha comum para programadores C++.
