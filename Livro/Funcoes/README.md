### Funções

#### Instrução def e return

Pra definir uma função em python, se utiliza o instrução __def__ . A instrução __return__ especifica o valor de retorno dessa função quando necessário. 

Uma função pode receber nenhum ou vários argumetos, que são indentificada pela sua posição na chamada da função ou por uma palavra-chave inserinda antes na chamada da função.


_syntax_ para funções

``` python
    def nomedafuncao():
        # bloco de código
        # .
        # .
        # .
        return valorderetorno


    def nomedafuncao(argumento1, argumento2):
        # bloco de codigo
        # .
        # .
        # .
        return valorderetorno

```

_Exemplo_:
``` python
    def imprimir():
        print('Estou imprimindo...')

    def meuNome(primeiro_nome, primeiro_sobrenome) 
        texto = 'Olá, me chamo' + primeiro_nome + ' ' + primeiro_sobrenome
        return texto

```
Pra executar o [exemplo](DefReturn.py) digite no terminal:

    $ python3 DefReturn.py

