# Tratando Conflitos de Nomes com Namespaces

<!-- toc -->
- [Introdução](#introdução)
- [Namespaces](#namespaces)
- [Namespaces Aninhados](#namespaces-aninhados)
- [O Namespace Global](#o-namespace-global)
- [O Namespace `std`](#o-namespace-std)
- [Usando `using namespace`](#usando-using-namespace)
<!-- toc -->

## Introdução

Em C++, conflitos de nomes ocorrem quando dois ou mais identificadores com o mesmo nome são introduzidos no mesmo escopo, levando à ambiguidade e impossibilitando o compilador de diferenciá-los. Isso gera um erro de compilação.

Por exemplo:

```cpp
#include <iostream>

int x {2};
int y {4};

int x {8}; // Erro, pois 'x' já foi declarado anteriormente
int y {16}; // Erro, pois 'y' já foi declarado anteriormente

int main() {
    // ...
}
```

Isso é um grande problema, pois pode ser difícil evitar conflitos de nomes em programas grandes. Os nomes de variáveis `x` e `y` são muito genéricos, e podem ser usados em muitos lugares diferentes. Se um programador usar um nome de variável que já foi usado em outro lugar, o programa não irá compilar.

Para evitar esse problema, podemos usar nomes mais descritivos e evitar os nomes genéricos. No entanto, isso não é uma solução perfeita, pois ainda é possível que dois programadores diferentes usem o mesmo nome para variáveis diferentes. Para resolver esse problema, C++ oferece uma ferramenta chamada **namespace**.

## Namespaces

Um namespace é um escopo que contém um conjunto de identificadores (nomes) que podem ser usados para evitar conflitos de nomes. Um namespace pode conter variáveis, funções, etc. Um namespace é declarado usando a palavra-chave `namespace` seguida pelo nome do namespace e um bloco de código entre chaves `{ }` que contém os identificadores que pertencem ao namespace.

```cpp
namespace nome_do_namespace {
    // Identificadores que pertencem ao namespace
}
```

Por exemplo:

```cpp
#include <iostream>

namespace math {
    int x {2};
    int y {4};
}

namespace physics {
    int x {8};
    int y {16};
}

int main() {
    // ..
}
```

Dessa forma, conseguimos declarar variáveis com o mesmo nome e sem que ocorra um conflito de nomes, pois cada variável pertence a um escopo diferente.

Agora, para acessar as variáveis `x` e `y`, precisamos especificar o namespace ao qual elas pertencem. Para isso, usamos o operador de resolução de escopo `::`:

A sintaxe é:

```cpp
namespace::identificador
```

Por exemplo:

```cpp
// ...

int main() {
    std::cout << math::x << '\n'; // 2
    std::cout << math::y << '\n'; // 4

    std::cout << physics::x << '\n'; // 8
    std::cout << physics::y << '\n'; // 16
}
```

## Namespaces Aninhados

Namespaces podem ser aninhados. Por exemplo:

```cpp
#include <iostream>

namespace math {
    namespace algebra {
        int x {2};
        int y {4};
    }

    namespace geometry {
        int x {5};
        int y {10};
    }
}

int main() {
    // Para acessar as variáveis `x` e `y`, precisamos especificar todos os namespaces ao qual elas pertencem:

    std::cout << math::algebra::x << '\n'; // 2
    std::cout << math::algebra::y << '\n'; // 4

    std::cout << math::geometry::x << '\n'; // 5
    std::cout << math::geometry::y << '\n'; // 10
}
```

## O Namespace Global

Em C++, qualquer identificador que não seja definido dentro de função, classe ou namespace é considerado parte de um namespace implicitamente definido chamado de espaço de nomes global.

No primeiro exemplo desta aula, as variáveis `x` e `y` foram declaradas no namespace global. Esse namespace é o namespace padrão, e não possui um nome específico.

Nesse exemplo, podemos acessar as variáveis `x` e `y` de duas formas: usando o operador de resolução de escopo `::` sem nenhum nome antes, explicitamente indicando que queremos acessar o namespace global, ou simplesmente omitindo o operador de resolução de escopo, pois o compilador irá assumir que estamos nos referindo ao namespace global.

```cpp
#include <iostream>

int x {2};
int y {4};

int main() {
    std::cout << ::x << '\n'; // 2
    std::cout << ::y << '\n'; // 4

    std::cout << x << '\n'; // 2
    std::cout << y << '\n'; // 4
}
```

## O Namespace `std`

Quando o C++ foi originalmente projetado, todos os identificadores na biblioteca padrão do C++ (incluindo std::cin e std::cout) estavam disponíveis para serem usados sem o prefixo std:: (eles faziam parte do espaço de nomes global). No entanto, isso significava que qualquer identificador na biblioteca padrão poderia entrar em conflito potencialmente com qualquer nome que você escolhesse para seus próprios identificadores (também definidos no espaço de nomes global). Código que estava funcionando poderia de repente ter um conflito de nomes quando você incluísse um novo arquivo da biblioteca padrão. Ou pior, programas que compilavam em uma versão do C++ podem não compilar em uma versão futura do C++, pois novos identificadores introduzidos na biblioteca padrão poderiam entrar em conflito com código já escrito. Por isso, o C++ moveu todas as funcionalidades da biblioteca padrão para um espaço de nomes chamado "std" (abreviação de standard, que significa padrão).

Acontece que o nome std::cout na verdade não é std::cout. Na verdade, ele é apenas cout, e std é o nome do espaço de nomes ao qual o identificador cout pertence. Porque cout é definido no espaço de nomes std, o nome cout não entrará em conflito com quaisquer objetos ou funções com o nome cout que criarmos no espaço de nomes global.

Da mesma forma, ao acessar um identificador definido em um namespace (por exemplo, std::cout), você precisa informar ao compilador que estamos procurando um identificador definido dentro do namespace (std).

## Usando `using namespace`

Em C++, podemos usar a palavra-chave `using` para indicar que queremos usar um identificador definido em um namespace sem ter que especificar o namespace ao qual ele pertence toda vez que quisermos usá-lo. Isso é chamado de declaração de namespace.

A sintaxe é:

```cpp
using namespace nome_do_namespace;
```

Ao fazer isso, todos os identificadores definidos no namespace especificado estarão disponíveis para uso sem o operador de resolução de escopo.

Por exemplo:

```cpp
#include <iostream>

namespace math {
    int x {2};
    int y {4};
}

namespace physics {
    int x {8};
    int y {16};
}

int main() {
    using namespace std; // Declaração do namespace std
    using namespace math; // Declaração do namespace math

    // Não precisamos usar o operador de resolução de escopo para acessar o cout e as variáveis x e y,
    // pois fizemos a declaração dos namespaces std e math
    cout << x << '\n'; // 2
    cout << y << '\n'; // 4

    // O namespace physics não foi declarado, então precisamos usar o operador de resolução de escopo
    cout << physics::x << '\n'; // 8
    cout << physics::y << '\n'; // 16
}
```
