# O que são matrizes e para que usar?

<!-- toc -->
- [Definição](#definição)
- [Utilizações de Matrizes em C++](#utilizações-de-matrizes-em-c)
- [Semelhanças com Arrays](#semelhanças-com-arrays)
- [Exemplos](#exemplos)
  - [Armazenando dados multidimensionais](#armazenando-dados-multidimensionais)
  - [Lendo os valores do usuário](#lendo-os-valores-do-usuário)
<!-- toc -->

## Definição

Em programação, uma matriz em é uma estrutura de dados que organiza elementos do mesmo tipo em uma grade bidimensional. Ela pode ser imaginada como uma tabela com linhas e colunas, onde cada célula armazena um valor. A definição de uma matriz inclui, assim como os arrays, sua dimensão, que agora é o número de linhas e colunas.

## Utilizações de Matrizes em C++

As matrizes desempenham um papel crucial na programação, especialmente em C++. Elas oferecem uma maneira eficiente de armazenar e manipular dados tabulares. Algumas utilizações comuns incluem:

1. **Matrizes como Estruturas de Dados**: Matrizes podem representar estruturas de dados como tabuleiros de jogos, imagens, mapas e grades para problemas numéricos ou científicos.

2. **Manipulação de Dados Multidimensionais**: Matrizes permitem armazenar e acessar dados em duas ou mais dimensões, como em aplicações de processamento de imagens ou simulações físicas.

## Semelhanças com Arrays

Em C++, matrizes têm semelhanças com arrays unidimensionais. Uma matriz pode ser vista como um conjunto de arrays, onde cada array representa uma linha da matriz. Ambos compartilham a propriedade de armazenar elementos do mesmo tipo em posições contíguas de memória. A diferença fundamental é que as matrizes possuem duas dimensões (linhas e colunas), enquanto os arrays unidimensionais têm apenas uma.

## Exemplos

### Armazenando dados multidimensionais

Aqui está um exemplo simples de como uma matriz pode ser declarada e usada em C++ para armazenar notas de alunos em uma sala de aula:

```cpp
#include <iostream>

using namespace std;

int main() {
    int NUM_ALUNOS = 3;
    int NUM_PROVAS = 4;

    double notas[NUM_ALUNOS][NUM_PROVAS] = {
        {7.5, 8.0, 9.2, 6.8},
        {9.0, 7.5, 8.8, 9.5},
        {6.5, 8.7, 7.2, 7.0}
    };

    // Acessando uma nota específica
    double nota = notas[1][2]; // Nota do segundo aluno na terceira prova
    cout << "Nota: " << nota << endl;
}
```

Neste exemplo, uma matriz é usada para armazenar notas de alunos em várias provas. A matriz é acessada usando índices para identificar a linha (aluno) e a coluna (prova) desejada.

### Lendo os valores do usuário

Aqui está um exemplo simples de como realizar a leitura e preenchimento de uma matriz:

```cpp
#include <iostream>

using namespace std;

int main() {
    int LINHAS = 3;
    int COLUNAS = 3;

    int matriz[LINHAS][COLUNAS];

    // Preenchendo a matriz com dados inseridos pelo usuário
    cout << "Digite os valores da matriz " << LINHAS << "x" << COLUNAS << ":" << endl;
    for (int i = 0; i < LINHAS; i++) {
        for (int j = 0; j < COLUNAS; j++) {
            cout << "Digite o valor para a posição [" << i << "][" << j << "]: ";
            cin >> matriz[i][j];
        }
    }

    // Exibindo os valores da matriz
    cout << "Valores da matriz:" << endl;
    for (int i = 0; i < LINHAS; i++) {
        for (int j = 0; j < COLUNAS; j++) {
            cout << matriz[i][j] << " ";
        }
        cout << endl;
    }
}
```

Neste exemplo, a matriz é preenchida com valores inseridos pelo usuário. O programa utiliza um loop para percorrer cada elemento da matriz e pede ao usuário para fornecer um valor para cada posição. Em seguida, os valores inseridos são exibidos na saída.

Lembrando que a matriz possui 3 linhas e 3 colunas neste exemplo, mas você pode ajustar `LINHAS` e `COLUNAS` para o tamanho de matriz que deseja usar.