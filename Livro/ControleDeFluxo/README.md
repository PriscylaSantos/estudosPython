### Controle de Fluxo

#### Valores Booleanos
Uma variável do tipo boolenado pode receber apenas dois valores: True ou False

> Os valores booleanos começam com letra maiúscula. 

``` python
taxa_adicional = False
fatura_paga = True
```

#### Operadores de Comparação
Esses operadors comparam dois valores e retornam um booleano como resposta.

|Operador | Significado
|:------: | :---------:
|==       | Igual a
|!=       | Diferente de
|<        | Menor que
|>        |Maior que
|<=       | Menor igual
|>=       | Maior igual

> __Atenção__: O operador __'=='__ pergunta se dois valores são iguais, já o operador __'='__ atribui valor a uma variável.

Os operadores __==__ e __!=__ podem comparar numeros e strings, já os operadores <, >, <=, >= comparam somente números.

Pra executar o [exemplo](OperComparacao.py) digite no terminal:

    $ python3 OperComparacao.py

#### Operadores booleanos

Os operadores __and__ e __or__ são utilizados para comparar dois valores booleanos ou expressões e o operador __not__ atua sobre um único valor booleano ou expressão.

O __and__ avalia uma expressão como _True_ se ambos os valores booleanos forem True, caso contrario a expressão recebe _False_.

O __or__ avalia uma expressão como _True_ se um dos valores for True, caso contrário a expressão recebe _False_

o __not__ avilia uma expressao com seu valor booleano oposto. Se a expressão for _True_ ele avalia como _False_, e se for _False_ avalia como _True_

Tabela verdade do Operador and|    |Tabela verdade do Operador or|    |Tabela verdade do operador not|
:----------------------------:|:--:|:---------------------------:|:--:|:----------------------------:|
_Expressão       ->  Retorno_ |    |_Expressão      ->  Retorno_ |    |_Expressão ->  Retorno_       |
True and True   ->  True      |    |True or True   ->  True      |    |not True  ->  False           |
True and False  ->  False     |    |True or False  ->  True      |    |not False ->  True            |
False and True  ->  False     |    |False or True  ->  True      |    |                              |
False and False ->  False     |    |False or False ->  False     |    |                              |

Pra executar o [exemplo](OperBooleano.py) digite no terminal:

    $ python3 OperBooleano.py

#### Instrução de controle de fluxo

##### if, else e elif

Uma instrução _if_ será executada se a expressão for True, caso seja False será ignorada. o _if_ pode ser seguido de um _else_ que será executado se a expressão for False. A instrução _elif_ pode vir após um _if_ ou de outro _elif_, que só será executado se as expressões anteriores forem False.

_syntax_ do if
``` python 
    if expressao:
        # executa se a expressao for verdadeira/True
``` 

_syntax_ do else
``` python 
    if expressao:
        # executa se a expressao for verdadeira/True
    else:
        # executa se a expressao for falsa/False
``` 

_syntax_ do elif
``` python 
    if expressao1:
        # executa se a expressao1 for verdadeira/True
    elif expressao2:
        # executa se a expressao2 for verdadeira/True
    elif expressao3:
        # executa se a expressao3 for verdadeira/True
    else:
        # executa se nenhuma das expressoes acima forem verdadeiras/True
``` 

_Exemplo_:
``` python
    valor = 5
    if 5 > valor:
        print('5 é maior que variável valor')
    elif 5 < valor:
        print('5 é menor que variável valor')
    else:
        print('5 é igual a variável valor')
```

Pra executar o [exemplo](IfElseElif.py) digite no terminal:

    $ python3 IfElseElif.py


##### loop while

Uma instrução _while_ será executada enquando a expressão for True, caso seja False será interrompida.

_syntax_ do while
``` python 
    while expressao:
        # executa enquanto expressao for verdadeira/True
``` 

_Exemplo_:
``` python
    valor = 0
    while valor < 5:
        print('A variavel valor é menor que 5')
        valor = valor + 1
```

Pra executar o [exemplo](LoopWhile.py) digite no terminal:

    $ python3 LoopWhile.py

##### for e a função range()
Uma instrução _for_  executada um bloco de código um determinado número de vezes

_syntax_ do for
``` python 
    for variavel in range(inicio, fim, incremento):
        # executa até variavel atingir o valor final(fim)
``` 

_Exemplo_:
``` python
    for i in range(0, 10, 2)
        print(i)
```
Pra executar o [exemplo](ForERange.py) digite no terminal:

    $ python3 ForERange.py



