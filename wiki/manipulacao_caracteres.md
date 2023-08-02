# Manipulação de caracteres

<!-- toc -->
<!-- toc -->

## Introdução

Na programação, lidar com caracteres é uma parte fundamental, seja para processar texto, verificar padrões ou converter entre letras maiúsculas e minúsculas. Nesta aula, exploraremos várias técnicas e funções para manipulação de caracteres em C++.

## Convertendo caractere para inteiro e vice-versa

Em C++, os caracteres são representados por valores numéricos de acordo com a tabela ASCII, como já visto no tópico anterior anterior. Isso permite que você converta facilmente um caractere em um valor inteiro (código ASCII) e vice-versa. A conversão é feita usando a conversão de tipo (casting).

Por exemplo, para converter o caractere 'A' em um inteiro, você pode fazer o seguinte:

```c++
#include <iostream>

int main() {
    char letra = 'A';
    int codigo_ascii = (int) letra;
    std::cout << codigo_ascii << '\n'; // 65
}
```

O contrário também é possível, ou seja, converter um inteiro em um caractere. Para isso, basta fazer o casting para o tipo char:

```c++
#include <iostream>

int main() {
    int codigo_ascii = 65;
    char letra = (char) codigo_ascii;
    std::cout << letra << '\n'; // A
}
```

> **Obs:** Realizamos um casting explícito, tanto de `char` para `int` quanto de `int` para `char`. Uma conversão implícita aconteceria se não tivéssemos especificado o tipo do casting.
> 
> Por exemplo:
>
> ```c++
> char letra = 'A';
> int codigo_ascii = letra; // conversão implícita de char para int
> char letra2 = codigo_ascii; // conversão implícita de int para char
> ```
>
> No entanto, é uma boa prática sempre realizar um casting explícito, pois isso deixa o código mais legível e evita erros.

## Funções da biblioteca `<cctype>`

A biblioteca `<cctype>` fornece um conjunto de funções que ajudam a verificar e manipular caracteres. Para usá-la, basta incluir a biblioteca no início do seu programa:

### isalpha() - Verifica se é uma letra

A função isalpha() verifica se um caractere é uma letra (maiúscula ou minúscula). Ou seja, se o caractere estiver entre 'A' e 'Z' ou entre 'a' e 'z'.

- **Parâmetros**: um caractere
- **Retorno**: um inteiro, 0 para falso e qualquer outro valor para verdadeiro

```c++
#include <iostream>

int main() {
    char letra = 'A';
    if (isalpha(letra)) {
        std::cout << "É uma letra\n";
    } else {
        std::cout << "Não é uma letra\n";
    }
}
```

### isdigit() - Verifica se é um dígito

A função isdigit() verifica se um caractere é um dígito. Ou seja, se o caractere estiver entre '0' e '9'.

- **Parâmetros**: um caractere
- **Retorno**: um inteiro, 0 para falso e qualquer outro valor para verdadeiro

```c++
#include <iostream>

int main() {
    char digito = '5';
    if (isdigit(digito)) {
        std::cout << "É um dígito\n";
    } else {
        std::cout << "Não é um dígito\n";
    }
}
```

### isalnum() - Verifica se é uma letra ou um dígito

A função isalnum() verifica se um caractere é uma letra ou um dígito. Ou seja, se o caractere estiver entre 'A' e 'Z', entre 'a' e 'z' ou entre '0' e '9'.

- **Parâmetros**: um caractere
- **Retorno**: um inteiro, 0 para falso e qualquer outro valor para verdadeiro

```c++

#include <iostream>

int main() {
    char caractere1 = '5';
    char caractere2 = 'A';
    if (isalnum(caractere1) and isalnum(caractere2)) {
        std::cout << "Ambos são dígitos ou letras\n";
    } else {
        std::cout << "Um ou ambos não são dígitos ou letras\n";
    }
}
```

> **Dica:** A função isalnum() é equivalente a usar as funções isalpha() e isdigit() em conjunto.

### islower() - Verifica se é uma letra minúscula

A função islower() verifica se um caractere é uma letra minúscula. Ou seja, se o caractere estiver entre 'a' e 'z'.

- **Parâmetros**: um caractere
- **Retorno**: um inteiro, 0 para falso e qualquer outro valor para verdadeiro

```c++
#include <iostream>

int main() {
    char letra = 'a';
    if (islower(letra)) {
        std::cout << "É uma letra minúscula\n";
    } else {
        std::cout << "Não é uma letra minúscula\n";
    }
}
```

### isupper() - Verifica se é uma letra maiúscula

A função isupper() verifica se um caractere é uma letra maiúscula. Ou seja, se o caractere estiver entre 'A' e 'Z'.

- **Parâmetros**: um caractere
- **Retorno**: um inteiro, 0 para falso e qualquer outro valor para verdadeiro

```c++
#include <iostream>

int main() {
    char letra = 'A';
    if (isupper(letra)) {
        std::cout << "É uma letra maiúscula\n";
    } else {
        std::cout << "Não é uma letra maiúscula\n";
    }
}
```

### tolower() - Converte para minúscula

A função tolower() converte um caractere para minúscula. Ou seja, se o caractere estiver entre 'A' e 'Z', ele será convertido para seu equivalente entre 'a' e 'z'. Se o caractere já for uma letra minúscula, ele não será alterado.

- **Parâmetros**: um caractere
- **Retorno**: um inteiro, o código ASCII do caractere convertido

```c++
#include <iostream>

int main() {
    char letra = 'A';
    char letra_minuscula = (char) tolower(letra);
    std::cout << letra_minuscula << '\n'; // a
}
```

### toupper() - Converte para maiúscula

A função toupper() converte um caractere para maiúscula. Ou seja, se o caractere estiver entre 'a' e 'z', ele será convertido para seu equivalente entre 'A' e 'Z'. Se o caractere já for uma letra maiúscula, ele não será alterado.

- **Parâmetros**: um caractere
- **Retorno**: um inteiro, o código ASCII do caractere convertido

```c++
#include <iostream>

int main() {
    char letra = 'a';
    char letra_maiuscula = (char) toupper(letra);
    std::cout << letra_maiuscula << '\n'; // A
}
```
