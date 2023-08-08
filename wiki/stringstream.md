# A Classe `std::stringstream`

<!-- toc -->
- [Os básicos](#os-básicos)
  - [Incluindo a biblioteca](#incluindo-a-biblioteca)
  - [Operadores de fluxo](#operadores-de-fluxo)
  - [Casts e conversões](#casts-e-conversões)
- [Construção e Manipulação de Strings](#construção-e-manipulação-de-strings)
  - [Extração de Dados de Strings](#extração-de-dados-de-strings)
  - [Manipulação de Formatação](#manipulação-de-formatação)
- [Métodos Úteis do objeto](#métodos-úteis-do-objeto)
<!-- toc -->

`std::stringstream` é uma classe da biblioteca padrão do C++ que permite manipular strings como se fossem fluxos de entrada e saída, semelhantes aos fluxos associados a arquivos ou à entrada/saída padrão (cin e cout). Isso é útil quando você precisa construir ou analisar strings de maneira eficiente.

## Os básicos

### Incluindo a biblioteca

  Para usar `std::stringstream`, você precisa incluir a biblioteca `<sstream>`.

  ```cpp
  #include <sstream>
  ```

### Operadores de fluxo

  `std::stringstream` é uma classe de fluxo, portanto, você pode usar os operadores de fluxo `<<` e `>>` para inserir e extrair dados. Por exemplo, para inserir dados em um fluxo, você pode fazer:

  ```cpp
  std::stringstream ss;
  ss << "Hello, world!";
  ```

  Para extrair dados de um fluxo, você pode fazer:

  ```cpp
  std::stringstream ss("Hello, world!");
  std::string s;
  ss >> s;
  ```

### Casts e conversões

  O fluxo stringstream permite que você converta dados de um tipo para outro. Por exemplo, para converter um `int` para uma `string`, você pode fazer:

  ```cpp
  std::stringstream ss;
  ss << 42;
  std::string s = ss.str();
  ```

  Para converter uma `string` para um `int`, você pode fazer:

  ```cpp
  std::stringstream ss("42");
  int i;
  ss >> i;
  ```

  Os **casts** também são possíveis. Por exemplo, para converter um `int` para um `double`, você pode fazer:

  ```cpp
  std::stringstream ss;
  ss << 42;
  double d;
  ss >> d;
  ```

  Porém o contrário não é possível. Por exemplo, para converter um `double` para um `int`, você não pode fazer:

  ```cpp
  std::stringstream ss;
  ss << 42.0;
  int i;
  ss >> i; // Isso não funciona!
  ```

  Erro:

  ```cpp
  error: invalid operands to binary expression ('std::stringstream' (aka 'basic_stringstream<char>') and 'int')
  ```

  Isso se deve ao fato de que o operador `>>` não é capaz de converter um `double` para um `int`. Para fazer isso, você precisa usar um **cast**. Isso mostra que o stream `stringstream` não é capaz de converter todos os tipos de dados, mas ainda se mostra muito útil para manipular strings.

## Construção e Manipulação de Strings

  Você pode usar um `std::stringstream` para construir strings concatenando diferentes tipos de dados, como inteiros, floats, strings, etc. Use o operador de inserção `<<` para adicionar dados ao fluxo e o método `str()` para obter a string resultante.

  ```cpp
  std::stringstream ss;
  ss << "Hello, " << 42 << " World!";
  std::string result = ss.str();
  ```

### Extração de Dados de Strings

  `std::stringstream` também pode ser usado para extrair dados de uma string formatada. Use o operador de extração `>>` para ler dados do fluxo.

  ```cpp
  std::string input = "42 3.14 Hello";
  std::stringstream input_ss(input);
  int intValue;
  double doubleValue;
  std::string stringValue;
  input_ss >> intValue >> doubleValue >> stringValue;
  ```

### Manipulação de Formatação

  Você pode controlar a formatação dos dados inseridos no fluxo usando manipuladores de fluxo como `std::setw`, `std::setprecision`, etc.

  ```cpp
  #include <iomanip>

  std::stringstream ss;
  ss << std::setw(10) << std::setfill('-') << 42;
  ```

## Métodos Úteis do objeto

- **Reset do Fluxo:**
   Se desejar reutilizar o `std::stringstream` para criar uma nova string, é importante redefinir seu estado.

   ```cpp
   std::stringstream ss;
   ss << "Hello";
   ss.str("");  // Limpa o conteúdo
   ss.clear();  // Limpa os erros e flags
   ```

- **Obtendo um Char a Cada Vez:**
   Você pode usar `get()` para extrair caracteres individuais do fluxo.

   ```cpp
   char c;
   while (ss.get(c)) {
       // Fazer algo com 'c'
   }
   ```

- **Testando o Fim do Fluxo:**
   Use a função `eof()` para verificar se você atingiu o fim do fluxo.

   ```cpp
   if (ss.eof()) {
       // O fluxo atingiu o fim
   }
   ```

- **Controle de Erros:**
   Você pode verificar se ocorreram erros durante a operação do `stringstream` usando as funções `fail()` ou `bad()`.

   ```cpp
   if (ss.fail()) {
       // Algum erro ocorreu
   }
   ```

- **Obtendo o Tamanho da String:**
  Você pode usar o método `tellp()` para obter o tamanho da string.

  ```cpp
  std::stringstream ss;
  ss << "Hello";
  std::cout << ss.tellp() << std::endl;  // 5
  ```

- **Obtendo o Tamanho do Fluxo:**
  Você pode usar o método `tellg()` para obter o tamanho do fluxo, ou seja, o número de elementos que podem ser lidos do fluxo.

  ```cpp
  std::stringstream ss;
  ss << "Hello";
  std::cout << ss.tellg() << std::endl;  // 5
  ```
  