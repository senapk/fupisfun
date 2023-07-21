# FUP is FUN

## Plano de 12 semanas
- Aula 01: O que são linguagens de programação?
  - Exemplos de códigos e linguagens
- Aula 02: Configuração do ambiente:
    - [Instalação do C++ (Mingw)](01/install.md)
    - [IDE: Visual Studio Code (vscode)](01/vscode.md)
    - [IDE: Replit](01/replit.md)
- Semana 01: Introdução à programação em C++:
    - [Primeiro código](01/primeiro.md)
    - [Compilando e Executando](01/compilando.md)
    - [Tipos de dados](01/tipos.md)
      - bool, int, float, double, char, string
      - casts compatíveis e perda de dados
    - [Dedução de tipos usando auto](01/auto.md)
    - [Modificadores: const, long e unsigned](01/variants.md)
- Semana 02: Operações Básicas
  - [Variáveis](02/variaveis.md): Criando, Boas práticas, Erros comuns, Não utilizando
  - [Operações aritméticas +, -, *, /](02/operacoes.md)
  - math.h (pow, sqrt)
  - Problema da divisão de dois inteiros
  - Entrada de dados básica com cin
  - [Debugando o primeiro código](02/debugando.md)
- Semana 03: Seleção Básica
  - Atribuição com substituição +=, -=
  - Operadores unários ++, --
  - estrutura do if e elses
    - técnica da seleção intervalada
  - Guia de escrita
  - Impressão formatada de zeros extras e casas decimais
- Semana 04: Técnicas de seleção
  - técnicas de if e else
    - Operadores lógicos &&, ||, ==, ()
    - agrupamento de saídas
  - switchs
  - resto da divisão e operação de módulo
    - execícios em lista circulas
- Semana 05
  - Variáveis globais e locais.
  - Escopo e tempo de vida
  - Sombreamento de variáveis
  - Funções: parâmetros e retornos
  - retornando no meio da função
  - Debugando em funções
  - Variáveis estáticas em funções
  - valores default em funções
- Semana 06
  - while(true), continue e break
  - for básico
- Semana 07
  - geração de números aleatórios com Mersenne Twister
  - argc e argv
  - stringstream e retornando textos
- Semana 08
  - raw array
  - vector
  - for indexado
- Semana 09
  - cópia e referência
  - for range, for auto&
  - introdução aos iteradores e sintaxe de iteradores 
- Semana 10
  - structs construtores com {}
  - vetores de structs
- Semana 11
  - tipos de passagem de parâmetros: 
    - cópias, referências e referências constantes
  - ponteiros
  - sobrecarga de funções
- Semana 12
  - enum
  - arquivos
  
- dá pra navegar pelos links do markdown pelo editor integrado, primeiro dá o preview, no preview você consegue navegar. Tem um botão open preview
- no vscode tem duas opções secretas, elas atualizam os links se você renomear os arquivos ou os títulos. Dá um `control ,` e ediciona essas duas coisas.
    "markdown.validate.enabled": true,
    "markdown.updateLinksOnFileMove.enabled": "always",

Quando você tiver um link pra algum arquivo usando markdown, ou pra algum título de algum arquivo usando markdown, se você alterar o arquivo ou o título usando f2, o vscode vai procurar e alterar todas as referencias também.