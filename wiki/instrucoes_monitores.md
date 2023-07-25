# Instruções

## Configuração Vscode

- No vscode tem duas opções secretas, elas atualizam os links se você renomear os arquivos ou os títulos. Dá um `control ,` e ediciona essas duas linhas no seu arquivo de configuração.

```json
"markdown.validate.enabled": true,
"markdown.updateLinksOnFileMove.enabled": "always",
```

Quando você tiver um link pra algum arquivo usando markdown, ou pra algum título de algum arquivo usando markdown, se você alterar o arquivo ou o título usando F2, o vscode vai procurar e alterar todas as referencias também.

## Rodando códigos diretamente do markdown

Você vai precisar do `bash`, `xsel` e `g++` e `gnome-terminal` instalados.

Para rodar um código diretamente do markdown no vscode, eu:

- seleciono o código inteiro: `alt + shift + right` vai expandir a seleção até abarcar o código.
- teclo `Control + C` para copiar o código para a área de transferência
- teclo `Windows + V` para rodar o script que eu criei para rodar o código no `gnome-terminal`.

___

Crie esse script com o nome `run_from_clipboard.sh`.

```bash
#!/bin/bash
cd  /tmp
xsel -b > solver.cpp
g++ -Wall solver.cpp -o solver.out && ./solver.out
echo "Press ESC key to quit"
# read a single character
while read -r -n1 key
do
# if input == ESC key
if [[ $key == $'\e' ]];
    then
        break;
    fi
done
```

___

Para executar, vá no seu Window Manager (xfce, gnome, kde, openbox, mate, etc) e configure um atalho de teclado para executar o seguinte comando: Coloque o caminho correto para seu script. No meu caso, eu uso as teclas `Windows + V` para rodar esse comando. Eu coloquei meu script em `~/bin/run_from_clipboard.sh`. Esse comando vai abrir um novo terminal e executar o script nesse terminal.

```bash
gnome-terminal --tab -- bash -c "~/bin/run_from_clipboard.sh"
```

## Git steps

```bash
git clone `no link do ssh`

acessar a página do projeto
    reservar os ítens que tem interesse
    marcar como todo
quando começar a escrever, marcar como `em progress`
quando terminar de escrever, marcar como `review`
fazer o commit
git pull (com rebase)
se tiver conflito, você consertar
fazer o push
```
