# Visual Studio Code (vscode)

<!-- toc -->
- [Como Instalar](#como-instalar)
- [Configurando](#configurando-o-vscode)
<!-- toc -->

O Visual Studio Code é uma **IDE (Integrated Development Environment)** desenvolvida pela Microsoft. É uma ferramenta gratuita e de código aberto, que pode ser utilizada para desenvolver em **diversas linguagens de programação**, incluindo **C++**.

## Como Instalar

<!-- toc -->
- [Windows](#windows)
- [Debian-Based Linux](#debian-based-linux)
- [Arch-Based Linux](#arch-based-linux)
<!-- toc -->

### Windows

- Baixe por este [link](https://az764295.vo.msecnd.net/stable/74f6148eb9ea00507ec113ec51c489d6ffb4b771/VSCodeUserSetup-x64-1.80.1.exe)
- Execute o arquivo baixado e siga as instruções de instalação

### Debian-Based Linux

- Execute os seguintes comandos no terminal:

  ```bash
  sudo apt update

  #instalando o wget
  sudo apt install software-properties-common apt-transport-https wget

  #baixando a chave de segurança
  wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -

  #adicionando o repositório
  sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"

  #instalando o vscode
  sudo apt update
  sudo apt install code
  ```

### Arch-Based Linux

- Execute os seguintes comandos no terminal:

  ```bash
  sudo pacman -Syu
  sudo pacman -S code
  ```

## Configurando o VSCode

<!-- toc -->
- [Abrindo o Terminal Integrado](#abrindo-o-terminal-integrado)
- [Usando o Explorer](#explorer)
- [Usando o Editor de Texto](#usando-o-editor-de-texto)
- [Instalando Extensões](#instalando-extensões)
- [Debuggando](#debuggando)
<!-- toc -->

### Abrindo o Terminal Integrado

O **Terminal Integrado** é uma ferramenta que permite executar comandos diretamente no VSCode. Para abrir, use a combinação de teclas `Ctrl + '` ou arraste de baixo para cima na aba do terminal.

![GIF](https://github.com/senapk/fupisfun/assets/103089400/419ed8f7-0684-4ee9-a7b4-11f65a88f367)

### Explorer

Para abrir o **Explorer**, use a combinação de teclas `Ctrl + Shift + E` ou clique no **ícone** do Explorer na barra lateral. Você pode usar o Explorer para **navegar** entre os arquivos do seu projeto.

![GIF](https://github.com/senapk/fupisfun/assets/103089400/439fecde-6932-4187-811b-6c1795e093d7)

### Usando o Editor de Texto

O editor de texto é a parte principal do VSCode. É onde você vai escrever o seu código, se aproveitando da **sintaxe colorida** e de **atalhos** para facilitar o seu trabalho.

- **Alguns atalhos úteis:**

  - `Ctrl + S`: Salva o arquivo
  - `Ctrl + Z`: Desfaz a última ação
  - `Ctrl + Shift + Z`: Refaz a última ação
  - `Ctrl + K + C`: Comenta a linha selecionada
  - `Ctrl + K + U`: Descomenta a linha selecionada
  - `Ctrl + C`: Copia o texto selecionado
  - `Ctrl + X`: Recorta o texto selecionado
  - `Ctrl + V`: Cola o texto selecionado
  - `Ctrl + F`: Abre a barra de busca
  - `Ctrl + A`: Seleciona todo o texto
  - `Shift + Alt + F`: Formata o código **(MUITO IMPORTANTE!!)**

## Extensões no VSCode

As extensões são ferramentas que podem ser instaladas no VSCode para adicionar funcionalidades.

### Instalando Extensões

Para instalar uma extensão, clique no ícone de **extensões** na barra lateral e digite o nome da extensão que você quer instalar. Clique em **instalar** para instalar a extensão.

![GIF](https://github.com/senapk/fupisfun/assets/103089400/7a52d544-5f68-47a4-b583-2d2982b64e92)

- **Algumas extensões que iremos usar:**
  - **C/C++**: Adiciona suporte para a linguagem C++
  - **Code Runner**: Permite executar o código diretamente no VSCode.
  - **Error Lens**: Mostra os erros no código sem precisar passar o mouse por cima.

### Debuggando

<!-- toc -->
- [Configurando o Debug](#configurando-o-debug)
- [Iniciando o Debug](#iniciando-o-debug)
- [Usando o Debug](#usando-o-debug)
<!-- toc -->

A ferramenta de debug do VSCode é muito útil para encontrar erros no seu código, utilizando breakpoints e outras ferramentas.

#### Configurando o Debug

Para configurar o debug, clique no ícone de **debug** na barra lateral e clique em **create a launch.json file**. Selecione **C++ (GDB/LLDB)**.

![GIF](https://github.com/senapk/fupisfun/assets/103089400/d630685a-f3cd-41ed-a23c-113e07c28da7)

#### Iniciando o Debug

Para começar a debuggar, primeiro coloque um **breakpoint** na linha que você quer debuggar. Para isso, clique na linha e aperte `F9` ou clique à esquerda do número da linha. Depois, clique no ícone de **debug** na barra lateral e clique em **start debugging** ou aperte `F5`. Aparecerão os compiladores disponíveis, selecione **g++ build and debug active file**. O debug irá começar.

![GIF](https://github.com/senapk/fupisfun/assets/103089400/510ff958-c905-4131-b608-c212a917a4af)

#### Usando o Debug

Após iniciar o debug, irá aparecer uma barra na parte superior da tela. Você pode usar os botões para **avançar** ou **voltar** o código, **continuar** a execução ou **parar** o debug. Você também pode usar o **terminal** para executar comandos. Teste por você mesmo!

![Image](https://github.com/senapk/fupisfun/assets/103089400/682009e2-87f2-43ea-a924-e50c4c5d1ee1)
