# Compilando manualmente

Para compilar, você precisa ter o g++ instalado. Crie e salve o arquivo como arquivo.cpp. Navegue até a pasta onde você salvou o arquivo. Ao dar o comando `ls` dentro da pasta, você deve encontrar o arquivo que salvou. Após isso compile e execute com os comandos.

**No windows:**

```bash
g++ -Wall -Wextra -Werror arquivo.cpp -o arquivo.exe
.\arquivo.exe
```

**No linux:**

```bash
g++ -Wall -Wextra -Werror arquivo.cpp -o arquivo.out
./arquivo.out
```

A primeira linha compila o código-fonte arquivo.cpp para gerar o arquivo executável arquivo.exe. Se houver qualquer erro ou **possível erro**, as flags -Wall -Wextra -Werror, vão impedir a finalização e avisar onde você deve consertar.

O comando `.\arquivo.exe` ou `./arquivo.out` é uma instrução para executar o código gerado pela primeira linha.

## Explicando as flags

No contexto do compilador GCC (GNU Compiler Collection) e do g++ (o compilador para C++ da GCC), as opções -Wall, -Wextra e -Werror são usadas para controlar a exibição de mensagens de aviso (warnings) e como esses avisos são tratados durante o processo de compilação. Aqui está uma explicação de cada uma delas:

-Wall (Ativar todos os avisos padrão):

A opção -Wall é usada para ativar a maioria dos avisos padrão do compilador. Quando você a utiliza, o g++ mostrará uma série de mensagens de aviso relacionadas a possíveis problemas no código-fonte que podem resultar em comportamentos indesejados ou erros em tempo de execução. No entanto, vale ressaltar que nem todos os avisos são ativados com essa opção; alguns avisos mais específicos ainda podem ser habilitados separadamente.

Por exemplo, se você tem um código com variáveis não inicializadas ou conversões implícitas, o -Wall pode emitir avisos relacionados a essas questões, incentivando boas práticas de programação.

-Wextra (Ativar mais avisos além dos habilitados por -Wall):

A opção -Wextra é usada para habilitar ainda mais avisos do compilador do que aqueles ativados por -Wall. Isso inclui avisos adicionais que podem não ser considerados obrigatórios ou padrão, mas que podem ser úteis para identificar problemas potenciais no código.

Ao usar -Wextra, o compilador será mais proativo na identificação de situações suspeitas no código-fonte, como variáveis não utilizadas ou conversões que podem levar a perda de dados.

-Werror (Tratar avisos como erros):

A opção -Werror é usada para tratar os avisos como erros durante o processo de compilação. Quando ativada, qualquer aviso gerado pelo compilador fará com que o processo de compilação seja interrompido e o código-fonte não será transformado em um executável até que todos os avisos sejam corrigidos.

Essa opção é frequentemente utilizada em projetos em que a equipe deseja garantir que o código esteja livre de avisos, incentivando práticas de programação mais seguras e consistentes. No entanto, é essencial ter cuidado ao habilitar -Werror, pois às vezes os avisos podem ser mais estritos do que o necessário e podem gerar falso-positivos. Nesses casos, é importante revisar os avisos cuidadosamente antes de tratá-los como erros.

Em resumo, -Wall e -Wextra são usados para habilitar avisos do compilador e -Werror é usado para tratá-los como erros. A combinação dessas opções pode ajudar a melhorar a qualidade do código, tornando-o mais seguro e livre de problemas potenciais. No entanto, ao usar -Werror, é fundamental garantir que os avisos são relevantes e não prejudicam o processo de compilação de forma imprópria.