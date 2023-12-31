# Configurando o Compilador GCC (G++)

<!-- toc -->
- [Windows](#windows)
- [Arch-Based Linux](#arch-based-linux)
- [Debian-Based Linux](#debian-based-linux)
<!-- toc -->

## Windows

- **Instalação do MinGW**
  - Realize o ***[DOWNLOAD](https://github.com/brechtsanders/winlibs_mingw/releases/download/13.1.0-16.0.5-11.0.0-msvcrt-r5/winlibs-x86_64-posix-seh-gcc-13.1.0-mingw-w64msvcrt-11.0.0-r5.7z)***
    - *A versão escolhida é compatível com a última versão do SFML, que poderá ser utilizada no futuro.*

  - Extraia o Arquivo ***"mingw64"*** para o diretório `C:`

  - Após, digite na pesquisa do Windows **"ambiente"** e, em seguida, clique em **"Editar as variáveis de ambiente do sistema"**
    - ![Imagem](https://github.com/senapk/fupisfun/assets/103089400/d859f639-8e4e-4305-913a-1265912ce650)

  - Ao abrir, clique no botão **"Variáveis de Ambiente..."**
    - ![Imagem](https://github.com/senapk/fupisfun/assets/103089400/60e89d4f-c556-4f7c-a8fe-b1b7e73de9b6)

  - Na nova janela, você terá que colocar o caminho do mingw na variável ***"Path"***
    - Observe que você terá duas abas, uma para o usuário atual e outra para o sistema. Escolha de acordo com suas necessidades.
    - ![Imagem](https://user-images.githubusercontent.com/103089400/256557320-e8a0e682-1cc3-4db3-bfa5-fe174d21346f.png)

  - Selecione o ***"Path"*** desejado e clique em **"Editar..."**. Uma janela será aberta, clique em **"Novo"** e digite o caminho do mingw. No nosso caso é `C:\mingw64\bin`
    - ![Imagem](https://github.com/senapk/fupisfun/assets/103089400/a9f4f4e4-6a0e-45e3-bb9f-afebd81aa2a6)

  - Clique em **"OK"** para todas as janelas.

- **Testando a instalação**
  - Abra o terminal do Windows (CMD) e digite

    ```shell
    g++ --version
    ```

  - Deverá aparecer isto:
    - ![Imagem](https://github.com/senapk/fupisfun/assets/103089400/e422193c-9911-4758-921a-75c15cf993b2)
  - E pronto, seu compilador para Windows está instalado e configurado.

## Arch-Based Linux

- **Instalando o GDB e o G++**

```bash
# atualize seu sistema
sudo pacman -Syyu

#instalação das ferramentas de compilação e do gdb
sudo pacman -S base-devel gdb
```

- **Testando a Instalação:**

```bash
gdb --version
g++ --version
```

## Debian-Based Linux

- **Instalando o GDB e o G++11**

```bash
#gdb
sudo apt-get update
sudo apt-get install build-essential gdb

#g++11
sudo add-apt-repository -y ppa:ubuntu-toolchain-r/test
sudo apt install -y g++-11

#configurando o g++11 como padrão
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-11 11
```

- **Testando a Instalação:**

```bash
gdb --version
g++ --version
```
