# Debuggando

<!-- toc -->
- [Configurando o Debug](#configurando-o-debug)
- [Iniciando o Debug](#iniciando-o-debug)
- [Usando o Debug](#usando-o-debug)
<!-- toc -->

Depurar (debugar) código é o processo de encontrar e corrigir erros, falhas ou problemas em um código.
A ferramenta de debug do VSCode é muito útil para encontrar erros no seu código, pois utiliza breakpoints e outras ferramentas
que facilitam o processo de depuração.

## Configurando o Debug

Para configurar o debug no VSCode, clique no ícone de **debug** na barra lateral e 
em seguida clique em **create a launch.json file**. Após isso, selecione a opção **C++ (GDB/LLDB)**.

![GIF](https://github.com/senapk/fupisfun/assets/103089400/d630685a-f3cd-41ed-a23c-113e07c28da7)

## Iniciando o Debug

Para começar a debuggar, o primeiro passo, é colocar um **breakpoint** na linha que você quer debuggar. Para isso, clique à esquerda do número na linha desejada. Depois, clique no ícone de **debug** na barra lateral e em seguida clique em **Run And Debbug** ou aperte `F5`. Ao fazer isso, aparecerão os compiladores disponíveis para a depuração. Selecione a opção **g++.exe build and debug active file** e em seguida o debug irá iniciar.

![GIF](https://github.com/senapk/fupisfun/assets/103089400/510ff958-c905-4131-b608-c212a917a4af)

## Usando o Debug

Após iniciar o debug, irá aparecer uma barra na parte superior da tela:

![Image](https://github.com/senapk/fupisfun/assets/103089400/682009e2-87f2-43ea-a924-e50c4c5d1ee1)

Você pode utilizar os botões para **avançar** ou **voltar** o código, **continuar** a execução ou **parar** a depuração. Você também pode usar o **terminal** para executar comandos. Teste por você mesmo!
