# FUP is FUN

## Plano de 30 aulas

- Bloco 01: Introdução
  - Aula 01: O que são linguagens de programação?
    - [ ] O que são algoritmos?
    - [ ] Exemplos de códigos e linguagens
    - [ ] Linguagens de marcação vs linguagens de programação
  - Aula 02: Configuração do ambiente:
    - [ ] [Ferramentas úteis](wiki/ferramentas_uteis.md) File Manager, Terminal, Text Editor
    - [ ] [Instalação do C++ (Mingw)](wiki/configure_cpp.md)
    - [ ] [IDE: Visual Studio Code (vscode)](wiki/configure_vscode.md)
    - [ ] [IDE: Replit](wiki/configure_replit.md)
  - Aula 03: Primeiro código
    - [x] [Primeiro código](wiki/primeiro_codigo.md)
    - [x] [Compilando e Executando](wiki/compilando.md)
    - [x] [Segundo código](wiki/segundo_codigo.md)
- Bloco 02: Regras do C++
  - Aula 04: Entendendo melhor os tipos
    - [ ] [Tipos de dados e casts](wiki/tipos.md)
    - [x] [Variáveis](wiki/variaveis.md): Criando, Boas práticas, Erros comuns, Não utilizando
    - [ ] [Operações aritméticas +, -, *, /](wiki/operacoes.md)
    - [ ] [Não tenha medo de erros](wiki/erros_variaveis.md)
- Aula 05: Operações Básicas
  - math.h (pow, sqrt)
  - Problema da divisão de dois inteiros
  - Entrada de dados básica com cin
- Semana 03: Seleção Básica
  - Atribuição com substituição +=, -=
  - Operadores unários ++, --
  - [ ] [Estruturas de seleção](wiki/estruturas_de_selecao.md)
  - [ ] [técnica da seleção intervalada](wiki/tecnica_selecao_intervalada.md)
  - [ ] [Debugando o primeiro código](wiki/debugando.md)
  - [ ] [Guia de escrita](wiki/guia_de_estilo.md)
  - [x] [Impressão formatada](wiki/impressao_formatada.md) Casas decimais, alinhamento e zeros à esquerda.
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
  - tipos de passagem de parâmetros
    - cópias, referências e referências constantes
  - ponteiros
  - sobrecarga de funções
- Semana 12
  - enum
  - arquivos
  
- dá pra navegar pelos links do markdown pelo editor integrado, primeiro dá o preview, no preview você consegue navegar. Tem um botão open preview
- no vscode tem duas opções secretas, elas atualizam os links se você renomear os arquivos ou os títulos. Dá um `control ,` e ediciona essas duas coisas.

```txt
"markdown.validate.enabled": true,
"markdown.updateLinksOnFileMove.enabled": "always",
```

Quando você tiver um link pra algum arquivo usando markdown, ou pra algum título de algum arquivo usando markdown, se você alterar o arquivo ou o título usando f2, o vscode vai procurar e alterar todas as referencias também.
