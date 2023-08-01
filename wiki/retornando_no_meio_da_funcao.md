# Retornando no meio da função

<!-- toc -->
- [Introdução](#introdução)
- [Retornando na última linha](#retornando-na-última-linha)
- [Retornando antes](#retornando-antes)
<!-- toc -->

## Introdução

Nesse tópico abordaremos como podemos usar o retorno de uma função antes do seu fim. Essa é uma técnica comum que pode passar despercebida no primeiro contato com funções.

## Retornando na última linha

Suponha a seguinte função:

```cpp
int calculo_aleatorio(int a, int b) {
    int soma = a + b;
    int multiplicacao = a * b;

    return soma / multiplicacao;
}
```

Ela recebe dois números e faz alguns cálculos sem sentido. Observe que a última coisa que essa função executa é um comando `return`, que indica que o valor dessa expressão, `soma / multiplicaca` deve ser devolvido para quem fez a chamada.

Esse é um padrão muito comum de estruturação: primeiro executamos todos os processos e cálculos desejados, e retornamos um resultado ao final.

Além do papel de devolver um valor, o `return` também indica que aquela função finalizou, voltando a execução para quem realizou a chamada. Funções com retorno `void` podem omitir o `return` ao final, pois isso já é implícito.

## Retornando antes

Considere a seguinte função que com base no tamanho dos lados de um triângulo retorna qual o tipo dele:

```cpp
string tipo_triangulo(int lado1, int lado2, int lado3) {
    string resultado;

    // Casos onde os lados não formam um triângulo
    if (lado1 <= 0 || lado2 <= 0 || lado3 <= 0) {
        resultado = "Não é um triângulo";
    } else if (lado1 >= lado2 + lado3 || lado2 >= lado1 + lado3 || lado3 >= lado1 + lado2) {
        resultado = "Não é um triângulo";
    }
    
    // Casos onde temos um triângulo
    if (lado1 == lado2 && lado2 == lado3) {
        resultado = "Triângulo equilátero";
    } else if (lado1 == lado2 || lado1 == lado3 || lado2 == lado3) {
        resultado = "Triângulo isósceles";
    } else {
        resultado = "Triângulo escaleno";
    }

    return resultado;
}
```

Essa seria uma implementação simples para o problema, armazenamos o tipo do triângulo em uma variável, executamos algumas comparações e retornamos o valor correto ao final.

No entanto, observe que caso os lados não formem um triângulo ainda fazemos as verificações abaixo de maneira desnecessária, pois já descobrimos que ele não é um triângulo.

Podemos substituir a variável por retornos diretos dentro de cada condição, pois a partir do momento que uma delas é verdadeira o triângulo não pode ter outro tipo. A função ficaria assim:

```cpp
string tipo_triangulo(int lado1, int lado2, int lado3) {
    // Casos onde os lados não formam um triângulo
    if (lado1 <= 0 || lado2 <= 0 || lado3 <= 0) {
        return "Não é um triângulo";
    } else if (lado1 >= lado2 + lado3 || lado2 >= lado1 + lado3 || lado3 >= lado1 + lado2) {
        return "Não é um triângulo";
    }
    
    // Casos onde temos um triângulo
    if (lado1 == lado2 && lado2 == lado3) {
        return "Triângulo equilátero";
    } else if (lado1 == lado2 || lado1 == lado3 || lado2 == lado3) {
        return "Triângulo isósceles";
    } else {
        return "Triângulo escaleno";
    }
}
```

Agora, se um dos lados for menor ou igual a 0, já paramos a execução e retornamos "Não é um triângulo", pois não há mais necessidade de outras checagens.

Esse tipo de padrão onde primeiros verificamos possíveis inconsistências e só depois executamos o código de fato é normalmente chamado de *Guard Clauses* e facilita a diminiuir a complexidade de condicionais.
