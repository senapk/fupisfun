# Cópia e Referência

<!-- toc -->
- [Introdução](#introdução)
- [Cópias](#cópias)
- [Referências](#referências)
- [Considerações Finais](#considerações-finais)
<!-- toc -->

## Introdução

Em `C++`, `cópias e referências` são maneiras diferentes de lidar com a manipulação de dados e a passagem de objetos entre funções ou partes do código.

## Cópias

Uma `cópia` em `C++` envolve a criação de uma duplicata independente de um objeto existente. Quando você cria uma `cópia` de um objeto, está criando uma nova instância desse objeto com os mesmos valores dos membros (atributos) do objeto original. Qualquer alteração feita em uma `cópia` não afeta o objeto original e vice-versa.

As `cópias` são usadas para trabalhar com versões separadas dos dados, evitando interferências entre diferentes partes do código que manipulam o mesmo tipo de objeto.

Exemplo:
```c++
int valorOriginal = 10;
int copiaValor = valorOriginal; // Cópia

copiaValor = 20; // Altera apenas a cópia

std::cout << "Original value: " << valorOriginal << std::endl; // Saída: Valor Original: 10
std::cout << "Copied value: " << copiaValor << std::endl;       // Saída: Valor da Cópia: 20
```

## Referências

Uma `referência` em `C++` é uma maneira de se referir diretamente a um objeto existente, em vez de criar uma `cópia` dele. Uma `referência` é, em essência, um "apelido" para o objeto original. Qualquer alteração feita na referência afeta diretamente o objeto original, pois eles estão compartilhando o mesmo espaço de memória.

As `referências` são frequentemente usadas quando se deseja passar objetos para funções sem a sobrecarga de copiar grandes quantidades de dados. Isso é útil para melhorar a eficiência e evitar a criação desnecessária de `cópias`.

Exemplo:
```c++
int valorOriginal = 10;
int& valorReferencia = valorOriginal; // Referência

valorReferencia = 20; // Altera diretamente o objeto original

std::cout << "Original value: " << valorOriginal << std::endl;   // Saída: Valor Original: 20
std::cout << "Referenced value: " << valorReferencia << std::endl; // Saída: Valor Referencia: 20
```

## Considerações Finais

Em resumo, `cópias em C++` são duplicatas independentes de objetos, enquanto `referências` permitem trabalhar diretamente com o objeto original. A escolha entre `cópias` e `referências` depende das necessidades do programa, do desempenho desejado e da manipulação dos dados em diferentes partes do código.
