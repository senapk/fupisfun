# Variáveis estáticas em funções

<!-- toc -->
- [Introdução](#introdução)
- [Declaração de variáveis estáticas](#declaração-de-variáveis-estáticas)
- [Escopo de variáveis estáticas](#escopo-de-variáveis-estáticas)
- [Vantagens do uso de variáveis estáticas em funções](#vantagens-do-uso-de-variáveis-estáticas-em-funções)
<!-- toc -->

## Introdução

As variáveis estáticas em funções são um conceito importante em programação que afeta o escopo e a vida útil das variáveis declaradas dentro de uma função. Diferente das variáveis locais comuns, as variáveis estáticas são preservadas entre as chamadas da função, mantendo seu valor entre as invocações.

## Declaração de variáveis estáticas

Em C++, uma variável é tornada estática dentro de uma função através da utilização da palavra-chave `static` antes do tipo e do nome da variável. Vamos ver um exemplo de como isso é feito:

```cpp
#include <iostream>

using namespace std;

void contador() {
    static int cont = 0;
    cont++;
    cout << "Chamada da funcao: " << cont << endl;
}

int main() {
    contador(); // Chamada da funcao: 1
    contador(); // Chamada da funcao: 2
    contador(); // Chamada da funcao: 3
}
```

Neste exemplo, a função `contador` contém uma variável estática chamada `cont`. Essa variável é inicializada apenas uma vez, quando a função é chamada pela primeira vez, e preserva seu valor entre as chamadas subsequentes. Cada vez que a função é chamada, a variável `cont` é incrementada, mantendo o registro do número de vezes que a função foi executada.

## Escopo de variáveis estáticas

As variáveis estáticas têm escopo local dentro da função em que são declaradas, ou seja, elas só podem ser acessadas dentro dessa função. Isso significa que não é possível utilizar a variável estática fora da função em que ela foi definida.

## Vantagens do uso de variáveis estáticas em funções

As variáveis estáticas em funções têm algumas vantagens importantes:

1. **Preservação do Valor**: O valor de uma variável estática é mantido entre as chamadas da função, permitindo que informações sejam mantidas e atualizadas através das execuções.

2. **Persistência**: As variáveis estáticas têm tempo de vida durante toda a execução do programa. Elas são criadas quando a função é chamada pela primeira vez e só são destruídas quando o programa termina.

3. **Compartilhamento de Dados**: Como as variáveis estáticas têm escopo local na função, elas podem ser utilizadas para manter informações persistentes sem que sejam acessíveis de fora da função, evitando poluição do espaço global.

Entretanto, é importante ter cuidado ao utilizar variáveis estáticas em funções, pois elas podem tornar o código mais difícil de entender e depurar, especialmente quando há muitas variáveis estáticas espalhadas em diferentes partes do código. O uso adequado das variáveis estáticas pode ajudar a melhorar o design e a eficiência do programa, tornando-o mais modular e organizado.
