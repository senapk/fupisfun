# Valores default em funções

<!-- toc -->
- [Introdução](#introdução)
- [Definindo valores default](#definindo-valores-default)
- [Chamando funções com valores default](#chamando-funções-com-valores-default)
- [Benefícios e considerações](#benefícios-e-considerações)
<!-- toc -->

## Introdução

Em C++, é possível definir valores default (padrão) para os parâmetros de uma função. Isso permite que a função seja chamada com menos argumentos do que os declarados, utilizando os valores default para os parâmetros ausentes. Essa flexibilidade torna o código mais conciso e facilita a reutilização da função em diferentes contextos.

## Definindo valores default

A definição de valores default para parâmetros de função é feita na declaração da função, na parte entre os parênteses dos parâmetros. Para isso, atribuímos os valores desejados diretamente aos parâmetros na lista de parâmetros. Veja um exemplo:

```cpp
void saudacao(string nome = "usuário", string saudacao = "Olá") {
    cout << saudacao << ", " << nome << "!" << endl;
}
```

Neste exemplo, a função `saudacao` possui dois parâmetros, `nome` e `saudacao`. Ambos têm valores default (definidos pelo `=`), ou seja, caso a função seja chamada sem passar argumentos para esses parâmetros, os valores "usuário" e "Olá" serão usados respectivamente.

Também é importante dizer que parâmetros que possuam valores default sempre devem ser os últimos na lista de parâmentros, por exemplo, a função abaixo está incorreta e resulta em um erro de compilação:

```cpp
void saudacao(string saudacao = "Olá", string nome) {
    cout << saudacao << ", " << nome << "!" << endl;
}
```

## Chamando funções com valores default

Ao chamar uma função com valores default definidos para alguns parâmetros, temos a opção de omitir os argumentos correspondentes. Caso não seja fornecido um valor específico para um parâmetro com valor default, a função utilizará automaticamente o valor padrão. Veja o exemplo usando a função `saudacao` definida acima:

```cpp
int main() {
    saudacao();             // Olá, usuário!
    saudacao("Maria");      // Olá, Maria!
    saudacao("João", "Oi"); // Oi, João!
}
```

No exemplo acima, chamamos a função `saudacao` em diferentes contextos. Na primeira chamada, não passamos nenhum argumento, portanto, a função utiliza os valores default para `nome` e `saudacao`. Nas chamadas seguintes, fornecemos apenas um dos argumentos, fazendo com que a função utilize o valor default para o argumento ausente.

## Benefícios e considerações

A utilização de valores default em funções oferece diversos benefícios, tais como:

- **Flexibilidade**: Facilita o uso da função em diferentes situações, evitando a necessidade de criar várias sobrecargas da mesma função.

- **Legibilidade**: Torna o código mais claro e conciso ao eliminar a necessidade de escrever argumentos repetitivos em chamadas de função.

- **Compatibilidade**: Permite que funções com valores default sejam chamadas por código já existente, mesmo se o novo parâmetro for adicionado posteriormente.

Contudo, é importante utilizar valores default com parcimônia e consideração. Ao definir valores padrão, é preciso garantir que eles façam sentido em diferentes contextos de chamada da função. Valores default complexos ou inconsistentes podem levar a comportamentos inesperados e dificultar a manutenção do código.
