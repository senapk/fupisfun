# Funções em C++: Parâmetros e Retorno

<!-- toc -->
- [Introdução](#introdução)
- [Definindo Funções](#definindo-funções)
- [Parâmetros de Função](#parâmetros-de-função)
- [Retorno de Função](#retorno-de-função)
<!-- toc -->

## Introdução

Em C++, funções são blocos de código que realizam tarefas específicas e podem ser chamadas em diferentes partes do programa. Elas ajudam a organizar o código, tornando-o mais modular e fácil de manter. As funções podem receber parâmetros (dados de entrada) e retornar valores (dados de saída).

## Definindo Funções

A definição de uma função em C++ segue a seguinte sintaxe:

```cpp
tipo_retorno nome_funcao(tipo_parametro1 nome_parametro1, tipo_parametro2 nome_parametro2, ...) {
    // Código para realizar a tarefa da função
    return valor_retorno; // Opcional, dependendo do tipo de retorno da função
}
```

- `tipo_retorno`: é o tipo de dado que a função retorna após sua execução. Pode ser qualquer tipo válido em C++ (int, float, char, bool, etc.), ou mesmo void, se a função não retornar nenhum valor (também chamadas de procedimentos nesse caso).
- `nome_funcao`: é o nome da função, que será usado para chamá-la em outras partes do programa.
- `tipo_parametroX`: são os tipos dos parâmetros que a função recebe (se houver).
- `nome_parametroX`: são os nomes dos parâmetros que a função recebe (se houver).
- `valor_retorno`: é o valor que a função retorna (se a função não for do tipo void).

Aqui está um exemplo de como definiríamos uma função que calcula o quadrado de um número e como executaríamos essa função:

```cpp
#include <iostream>

using namespace std;

// Definição da função para calcular o quadrado de um número inteiro
int quadrado(int x) {
    return x * x;
}

int main() {
    int numero = 5;
    int resultado = quadrado(numero); // Chamada da função quadrado e atribuição do resultado a uma variável
    
    cout << resultado << endl; // 25

    return 0;
}
```

Neste exemplo, temos uma função `quadrado`, que recebe um parâmetro `x` do tipo inteiro e retorna o valor de `x` elevado ao quadrado. Na função `main`, declaramos uma variável `numero` e atribuímos o valor 5 a ela. Em seguida, chamamos a função `quadrado` passando `numero` como argumento e armazenamos o resultado retornado na variável `resultado`.

## Parâmetros de Função

Os parâmetros de uma função são variáveis locais que recebem os valores passados como argumentos na chamada da função. Eles permitem que dados sejam passados para a função, permitindo maior flexibilidade no processamento dos dados.

Veja um exemplo de função com parâmetros:

```cpp
int soma(int a, int b) {
    return a + b;
}
```

Nesse exemplo, a função `soma` recebe dois parâmetros `a` e `b`, ambos do tipo inteiro. A função retorna a soma dos dois valores passados como argumentos.

## Retorno de Função

O retorno de uma função é feito através da palavra-chave `return`, seguida pelo valor que deve ser retornado. O tipo desse valor deve corresponder ao tipo de retorno declarado na definição da função.

Aqui está um exemplo de função que retorna um valor:

```cpp
int quadrado(int x) {
    return x * x;
}
```

A função `quadrado` recebe um parâmetro `x` e retorna o valor de `x` elevado ao quadrado.

Quando uma função tem o tipo de retorno definido como `void`, ela não retorna valor algum. Ela pode executar tarefas, mas não produz um resultado para ser utilizado em expressões.

```cpp
void exibirMensagem() {
    cout << "Olá, mundo!" << endl;
}
```

A função `exibirMensagem` não possui retorno, mas imprime a mensagem "Olá, mundo!" no terminal.
