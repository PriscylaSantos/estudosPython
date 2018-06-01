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

Operador | Significado
:------: | :---------:
==       | Igual a
!=       | Diferente de
<        | Menor que
>        |Maior que
<=       | Menor igual
>=       | Maior igual

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



