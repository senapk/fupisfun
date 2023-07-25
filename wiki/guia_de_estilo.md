# Estilo

Estilo Kernel para escrita de código em C/C++/Python utilizando o guia de estilos do Google.

## Nomes

```txt
[ ] funções e variáveis devem inicializar em minúscula e usar _
int funcao_que_faz_algo(int x, int z) {
def funcao_que_faz_algo(x: int, z: int) -> int
[ ] enum, structs e classes iniciam em maiúscula
```

## Variáveis

```txt
[ ] utilize nomes legíveis e evite abreviações
[ ] inicialize todas no momento da criação
[ ] crie apenas no contexto e quando forem necessárias.
```

## Indentação

```txt
[ ] sempre indente funções, controle(if, else), laço(for, while)
[ ] mantenha seu código alinhado (4 espaços ou um tab)
```

## Funções

```txt
[ ] o nome da função deve explicitar exatamente o que ela faz
[ ] utilize returns ao invés de if elses preferencialmente
[ ] sempre deixe um return default
[ ] em python, utilize a notação de tipos
```

## Escrita

```txt
[ ] existe espaço entre operadores binários(=, +, <, etc), ex: 
for (int i = a + b; i < vet[x]; i++) {
[ ] existe espaço entre controles, () e chaves, com chaves abrindo no final
for (...) {
if (...) {
} else if (...) {
[ ] não existe espaço entre funções e seus parâmetros e a chave abre embaixo
int soma(int a, int b) 
{
    return a + b;
}
[ ] o nome de variável em função tanto em python como em c deve ser no formato underline_case
```
