# Bash

<!-- toc -->
- [Windows: Instalando o Git Bash](#windows-instalando-o-git-bash)
  - [Como instalar](#como-instalar)
  - [Como utilizar](#como-utilizar)
- [Utilizando o Bash](#utilizando-o-bash)
  - [Comandos básicos](#comandos-básicos)
  - [Atalhos](#atalhos)
<!-- toc -->

O **Bash** é um interpretador de comandos que permite executar comandos diretamente no terminal. Ele é o interpretador padrão do Linux e do MacOS.

## Windows: Instalando o Git Bash

Como o **Bash** não é o interpretador padrão do Windows, é necessário instalar um programa que o permita ser executado. Para isso, vamos utilizar o **Git Bash**.

### Como instalar

- Baixe por este [link](https://git-scm.com/downloads) e escolha a versão para windows.

- **Execute** o arquivo baixado e siga com os padrões de instalação. Não é necessário alterar nada.

### Como utilizar

- Para abrir o **Git Bash**, basta clicar com o botão direito em uma pasta e selecionar a opção `Git Bash Here`:

    ![GIF](https://github.com/senapk/fupisfun/assets/103089400/71e1b93e-6db3-4555-a477-a5c0618b24bf)

- Alternativamente, você pode abrir o **Git Bash** pelo **menu iniciar**:

    ![Imagem](https://github.com/senapk/fupisfun/assets/103089400/0f31cf83-8874-4b52-9c0f-95e07bc5f2bb)

  - Porém, ao fazer isso, o Git Bash será aberto na pasta do seu usuário. Para navegar até a pasta desejada, utilize o comando `cd`.

## Utilizando o Bash

O **Bash** tem uma sintaxe muito simples. Para executar um comando, basta escrevê-lo e apertar `Enter`. Por exemplo, para listar os arquivos de uma pasta, basta escrever `ls` e apertar `Enter`.

![GIF](https://github.com/senapk/fupisfun/assets/103089400/f6e3850b-6783-4796-8eeb-a69ece072f3b)

### Comandos básicos

- `ls`: lista os arquivos da pasta atual
  - `ls -a`: lista todos os arquivos, incluindo os ocultos
  - `ls -l`: lista os arquivos com mais detalhes

  ![GIF](https://github.com/senapk/fupisfun/assets/103089400/37a594cc-fdb4-45e2-898b-7d56facc53dd)

- `cd`: navega entre pastas
  - `cd ..`: volta uma pasta

  ![GIF](https://github.com/senapk/fupisfun/assets/103089400/a4bec9ae-438f-4ff4-89ad-2ba626326f74)

- `mkdir`: cria uma pasta
  - `mkdir -p`: cria uma pasta e todas as pastas necessárias para chegar até ela

  ![GIF](https://github.com/senapk/fupisfun/assets/103089400/dd6a7daf-f922-4082-a90d-c2b843dfd497)

- `rm`: remove um arquivo
  - `rm -rf` remove uma pasta

  ![GIF](https://github.com/senapk/fupisfun/assets/103089400/78a4b043-7308-4831-83f5-7771189f9b76)

- `cat`: mostra o conteúdo de um arquivo
  ![GIF](https://github.com/senapk/fupisfun/assets/103089400/d7494f0b-8fa5-4297-8e4d-6d89dbe92587)

- `clear`: limpa o terminal
  ![GIF](https://github.com/senapk/fupisfun/assets/103089400/8cc50e26-30ab-44b8-9b9c-ddd1f7c2a4a0)

- `exit`: fecha o terminal

### Atalhos

- `Ctrl + L`: "limpa" o terminal
- `Ctrl + D`: fecha o terminal
- `Ctrl + A`: vai para o início da linha
- `Ctrl + E`: vai para o final da linha
- `Ctrl + U`: apaga a linha
- `Ctrl + W`: apaga a palavra anterior
- `Ctrl + C`: cancela o comando atual **(IMPORTANTE!!)**
  - Muito útil quando um comando está demorando muito para executar, geralmente é a única forma de cancelá-lo, já que o terminal fica travado enquanto o comando está sendo executado.
