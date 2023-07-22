# Erros com variáveis

## Erros

- Qual erro acontece quando:
  - Você declara duas vezes a mesma variável no mesmo escopo?
  - Cria uma variável fora da main?
  - Esquece de colocar o `;` no final da declaração?
  - Você tenta utilizar uma variável que não foi criada ou com um nome diferente?
  - Você esquece o tipo da variável?
  - Você cria uma variável, mas não a utiliza pra nada?

## Solução

Vamos declarar duas variáveis com o mesmo nome no mesmo escopo:

```cpp
#include <iostream>

int main() {
    int x = 10;
    int x = 20;
    std::cout << x << std::endl;
}
```

Temos um erro de compilação do tipo "redeclaration of 'int x'".

```bash
solver.cpp: In function ‘int main()’:
solver.cpp:5:9: error: redeclaration of ‘int x’
    5 |     int x = 20;
      |         ^
solver.cpp:4:9: note: ‘int x’ previously declared here
    4 |     int x = 10;
      |    
```
