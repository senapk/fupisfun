# Configurando o Compilador GCC (G++)

<!-- toc -->
- [Windows](#windows)
- [Arch-Based Linux](#arch-based-linux)
- [Debian-Based Linux](#debian-based-linux)
<!-- toc -->

## Windows
- **Instalação do MinGW**
    - Realize o ***[DOWNLOAD](https://github.com/brechtsanders/winlibs_mingw/releases/download/13.1.0-16.0.5-11.0.0-msvcrt-r5/winlibs-x86_64-posix-seh-gcc-13.1.0-mingw-w64msvcrt-11.0.0-r5.7z)***
        - Note que o arquivo é um ***.7z***, portanto, você precisará de um descompactador de arquivos como o ***[RAR](https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-622br.exe)***
        - *A versão escolhida é compatível com a última versão do SFML, que será instalada no futuro.*

    - Extraia o Arquivo ***"mingw64"*** para o diretório C:

    - Após, digite na pesquisa do Windows **"ambiente"** e, em seguida, clique em **"Editar as variáveis de ambiente do sistema"**
        - ![Imagem](https://github.com/senapk/fupisfun/assets/103089400/aea4b4ab-17d9-412e-8bbf-3b99988c9e79)

    - Ao abrir, clique no botão **"Variáveis de Ambiente..."**
        - ![Imagem](https://github.com/senapk/fupisfun/assets/103089400/60e89d4f-c556-4f7c-a8fe-b1b7e73de9b6)

    - Na nova janela, você terá que colocar o caminho do mingw na variável ***"Path"*** 
        - Observe que você terá duas abas, uma para o usuário atual e outra para o sistema. Escolha de acordo com suas necessidades.
        - ![Imagem](https://github.com/senapk/fupisfun/assets/103089400/6d591d98-7013-44e9-a0a4-0472fb451004) 

    - Selecione o ***"Path"*** desejado e clique em **"Editar..."**. Uma janela será aberta, clique em **"Novo"** e digite o caminho do mingw. No nosso caso é `C:\mingw64\bin`
        - ![Imagem](https://github.com/senapk/fupisfun/assets/103089400/c62e2535-692f-4937-aa15-4efc6512b889)

    - Clique em **"OK"** para todas as janelas.
 
- **Testando a instalação**
    - Abra o terminal do Windows (CMD) e digite 
    ```shell
    g++ --version
    ```
    - Deverá aparecer isto:
        - ![Imagem](https://github.com/senapk/fupisfun/assets/103089400/39097e38-5be4-4a16-a087-0b32c7137995)
    - E pronto, seu compilador para Windows está instalado e configurado.

## Arch-Based Linux 
- Instalando o GDB (GCC, G++ e GDB)
```bash
sudo pacman -S base-devel gdb
```
- Testando a Instalação:
```bash
g++ --version
```

## Debian-Based Linux 
- Instalando o GDB (GCC, G++ e GDB)
```bash
sudo apt-get update
sudo apt-get install build-essential gdb
```
- Testando a Instalação:
```bash
g++ --version
```



