### Básico sobre o Python

#### Variáveis
Os nomes permitidos para variáveis devem obeceder a três regras:
1. O nome pode ser constituído somente de uma palavra
2. Somente letras, números e underscore(_) podem ser utilizados no nome da variável
3. O nome não pode começar com um número

O nome de uma variável deve iniciar com letra minúscula. Para atribuir um valor se utiliza o igual(=).

_Exemplo_: 
``` python
nome = 'Priscyla' 
nome_completo = 'Priscyla Santos' 
nomeCompleto = 'Priscyla Santos' 
endereco1 = 'Avenida Brasil'
numero_endereco_2 = 34
```

> __Observação__
> As variáveis no python são _case sensitive_, portanto __nome__  e __NOME__ não são a mesma variável.

#### Comentários
Para se fazer um comentário no código Python utiliza-se o símbolo #. Tudo que estiver escrito depois desse símbolo será ignorado.
_Exemplo_:
``` python
# Nome completo para registro
nome_completo = 'Priscyla Santos' 
```

#### Funções básicas
- __print()__ : é utilizada para imprimir o valor de uma variável. Essa variável precisa ser do tipo string.
- __input()__ : recebe um texto digitado pelo usuário.
- __len()__: verifica o tamanho de uma variável.
- __str()__: converte uma variável do tipo inteiro(int) ou flutuante(float) para o tipo string(str)
- __int()__: converte uma variavel do tipo string com valor numérico ou um flutuante para um valor inteiro  
- __float()__: coverte uma variável em ponto flutuante

Pra executar o [exemplo](FuncoesBasicas.py) digite no terminal:

    $ python3 FuncoesBasicas.py


#### Operadores matemáticos
- Adição: _a + b_
- Subtração: _a - b_
- Multiplicação: _a * b_  
- Divisão: _a / b_
- Módulo/Resto: _a % b_
- Divisão inteira: _a // b_
- Exponencial: _a ** b_

Pra executar o [exemplo](OperadoresMatematicos.py) digite no terminal:

    $ python3 OperadoresMatematicos.py

#### Tipo de dado inteiro, de ponto flutuante e string

- **Inteiros(int)**: Valores que contém números interos positivos ou negativos. 
    - _Ex: 3, -89_

- **Ponto Flutuante(float)**: Valores que contem um ponto decimal.
    - _Ex: 3.0, -89.65_

- **String(str)**: Valores textuais que se iniciam e terminam com aspas simples (').
    - _Ex: 'olá', 'Meu nome é Priscyla'_

- O operador _+_ pode ser utilizado para concatenar duas ou mais strings em uma única strings

- O operador _*_ pode ser utilizado para multiplicar uma string por um número inteiro positivo

Pra executar o [exemplo](IntFloatString.py) digite no terminal:

    $ python3 IntFloatString.py



