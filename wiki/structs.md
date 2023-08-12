# Structs

<!-- toc -->
- [**Introdução**](#introdução)
- [**Definindo Uma Struct**](#definindo-uma-struct)
- [**Acessando Valores de uma Struct++**](#acessando-valores-de-uma-struct)
- [**Inicializando Structs Utilizando Chaves**](#inicializando-structs-utilizando-chaves)
- [Exemplos práticos](#exemplos-práticos)
  - [**Exemplo 1: Representando Pontos em 2D**](#exemplo-1-representando-pontos-em-2d)
    - [Definindo a `struct` **Ponto2D**](#definindo-a-struct-ponto2d)
    - [Usando a `struct` Ponto2D Para Somar Dois Pontos](#usando-a-struct-ponto2d-para-somar-dois-pontos)
  - [**Exemplo 2: Modelando um Veículo**](#exemplo-2-modelando-um-veículo)
    - [Definindo a `struct` **Veiculo**](#definindo-a-struct-veiculo)
    - [Imprimindo **informações** de Vários Veículos](#imprimindo-informações-de-vários-veículos)
<!-- toc -->

## **Introdução**

As `structs` (estruturas) em C++ oferecem uma maneira versátil de criar
tipos de dados personalizados, permitindo **agrupar variáveis de diferentes**
tipos em uma única entidade. Neste texto, vamos aprofundar a discussão sobre
structs, explorar alguns conceitos adicionais e fornecer **exemplos** práticos
de uso em cenários diversos.

## **Definindo Uma Struct**

A definição de uma `struct` em C++, como já apresentado, permite criar um tipo
de dado customizado para armazenar informações relacionadas:

```cpp
struct NomeDaStruct {
    TipoDeDado1 Variavel1;
    TipoDeDado2 Variavel2;
    // ... outras variáveis
};
```

## **Acessando Valores de uma Struct++**

Para acessar os valores armazenados em uma `struct` em C++, utilize o operador
ponto (`.`) seguido do nome do campo desejado. Esse operador permite que você
acesse diretamente os atributos da `struct` e os utilize em suas operações. Por
exemplo:

```cpp
#include <iostream>

struct Pessoa {
    std::string nome;
    int idade;
};

int main() {
    Pessoa pessoa1;
    pessoa1.nome = "Alice";
    pessoa1.idade = 30;

    std::cout << "Nome: " << pessoa1.nome << '\n'; // Nome: Alice
    std::cout << "Idade: " << pessoa1.idade << " anos\n"; // Idade: 30 anos

    return 0;
}
```

Neste código, a `struct` `Pessoa` é criada com os campos "nome" e "idade". Para
acessar os valores desses campos, utilizamos o operador ponto após o nome da
instância (`pessoa1`), seguido pelo nome do campo (`nome` ou `idade`). Isso
nos permite exibir os valores dos campos na saída.

## **Inicializando Structs Utilizando Chaves**

A inicialização de chaves é uma abordagem poderosa para criar e configurar
structs de maneira concisa. Ela é realizada durante a criação do objeto e
segue a seguinte sintaxe:

```cpp
NomeDaStruct nomeDoObjeto = {valor1, valor2, /* ... outros valores */};
```

Isso permite atribuir valores aos campos da `struct` diretamente no momento da
criação, sem a necessidade de usar construtores explícitos. Vamos utilizar
essa abordagem no exemplo anterior:

```c++
#include <iostream>

struct Pessoa {
    std::string nome;
    int idade;
};

int main() {
    Pessoa pessoa1 = {"Alice", 30};
    Pessoa pessoa2 = {"Bob", 25};

    std::cout << "Pessoa 1:\n";
    std::cout << "Nome: " << pessoa1.nome << '\n'; // Nome: Alice
    std::cout << "Idade: " << pessoa1.idade << " anos\n"; // Idade: 30 anos

    std::cout << "\nPessoa 2:\n";
    std::cout << "Nome: " << pessoa2.nome << '\n'; // Nome: Bob
    std::cout << "Idade: " << pessoa2.idade << " anos\n"; // Idade: 25 anos

    return 0;
}
```

## Exemplos práticos

### **Exemplo 1: Representando Pontos em 2D**

#### Definindo a `struct` **Ponto2D**

Consideremos a seguinte `struct` para representar pontos em um plano 2D:

```cpp
#include <iostream>

struct Ponto2D {
    double x;
    double y;
};

int main() {
    Ponto2D pontoA = {3.0, 2.5};

    std::cout << "Coordenadas do ponto A:";
    std::cout << (" << pontoA.x << ", " << pontoA.y << ")" << '\n';

    return 0;
}
```

- Saida do programa:

```c++
Coordenadas do ponto A:(3, 2.5)
```

#### Usando a `struct` Ponto2D Para Somar Dois Pontos

Agora vamos utilizar a `struct` Ponto2D para criar uma função que recebe, dois
pontos e retorna a distância entre os dois. Para isso podemos seguir o seguinte
raciocínio:

```cpp
#include <iostream>
#include <cmath>  // Para usar a função de raiz quadrada (sqrt)

struct Ponto2D {
    double x;
    double y;
};

// Função para calcular a distância entre dois pontos
double calcularDistancia(Ponto2D ponto1, Ponto2D ponto2) {
    double deltaX = ponto2.x - ponto1.x;
    double deltaY = ponto2.y - ponto1.y;
    return sqrt(deltaX * deltaX + deltaY * deltaY);
}

int main() {
    Ponto2D pontoA = {3.0, 2.5};
    Ponto2D pontoB = {6.0, 7.8};

    std::cout << "Coordenadas do ponto A:";
    std::cout << "(" << pontoA.x << ", " << pontoA.y << ")" << '\n';
    std::cout << "Coordenadas do ponto B:";
    std::cout << "(" << pontoB.x << ", " << pontoB.y << ")" << '\n';

    double distancia = calcularDistancia(pontoA, pontoB);
    std::cout << "Distância entre os pontos A e B: " << distancia << '\n';

    return 0;
}
```

Neste programa, a função `calcularDistancia` calcula a distância entre dois
pontos utilizando a fórmula da distância euclidiana no plano 2D. A função
`sqrt` da biblioteca `cmath` é usada para calcular a raiz quadrada,
necessária para a fórmula. O programa cria dois pontos `pontoA` e `pontoB`,
calcula a distância entre eles usando a função `calcularDistancia` e exibe o
resultado.

- A saída do programa será:

```c++
Coordenadas do ponto A:(3, 2.5)
Coordenadas do ponto B:(6, 7.8)
Distância entre os pontos A e B: 6.09016
```

### **Exemplo 2: Modelando um Veículo**

Agora, consideremos um cenário em que precisamos modelar veículos com
informações como marca, modelo e ano de fabricação:

#### Definindo a `struct` **Veiculo**

Uma declaração válida para uma `struct` que representase um veículos da
maneira esperada seria a segiunte:

```cpp
struct Veiculo {
    string marca;
    string modelo;
    int anoFabricacao;
};
```

#### Imprimindo **informações** de Vários Veículos

Com a `struct` definida, agora é possível criar uma função que recebe um
veículo
e mostra na tela suas informações. Uma boa implementação desta
funcionalidade
seria a seguinte:

```c++
#include <iostream>

struct Veiculo {
    std::string marca;
    std::string modelo;
    int anoFabricacao;
};

// Função para imprimir os dados do carro
void imprimirCarro(Veiculo carro) {
    std::cout << "Marca: " << carro.marca << '\n';
    std::cout << "Modelo: " << carro.modelo << '\n';
    std::cout << "Ano de Fabricação: " << carro.anoFabricacao << '\n';
    std::cout << '\n';
}

int main() {
    Veiculo carro1 = {"Toyota", "Corolla", 2022};
    Veiculo carro2 = {"Honda", "Civic", 2023};
    Veiculo carro3 = {"Ford", "Mustang", 2022};

    std::cout << "Carro 1:" << '\n';
    imprimirCarro(carro1);

    std::cout << "Carro 2:" << '\n';
    imprimirCarro(carro2);

    std::cout << "Carro 3:" << '\n';
    imprimirCarro(carro3);

    return 0;
}
```

- Saida do programa

```c++
Carro 1:
Marca: Toyota
Modelo: Corolla
Ano de Fabricação: 2022

Carro 2:
Marca: Honda
Modelo: Civic
Ano de Fabricação: 2023

Carro 3:
Marca: Ford
Modelo: Mustang
Ano de Fabricação: 2022
```

---

Structs em C++ com são uma ferramenta essencial para a criação de tipos de
dados personalizados. Eles oferecem um meio eficaz de agrupar variáveis relacionadas
e inicializá-las de maneira conveniente. Neste texto, discutimos a sintaxe para
definir e utilizar structs, além de apresentar exemplos práticos para representar
pontos em 2D e veículos. À medida que você aprofunda seus conhecimentos em C++,
esses conceitos se tornarão valiosos em seus projetos de programação, proporcionando
uma abordagem organizada e eficiente para lidar com informações complexas.
