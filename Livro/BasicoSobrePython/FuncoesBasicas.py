valor_inteiro = 19
valor_string_inteiro = '276'
valor_flutuante = 34.65
valor_string_flutuante = '71.65'

# imprimendo as variáveis. Todos as variáveis do tipo float e int são convertidas
# para str() para serem concatenadas com o texto
print('valor_inteiro: ' + str(valor_inteiro))
print('valor_string_inteiro: ' + valor_string_inteiro)
print('valor_flutuante: ' + str(valor_flutuante))
print('valor_string_flutuante: ' + valor_string_flutuante)
print()

print('Convertendo valores...')
print('Inteiro para String')
print(str(valor_inteiro))
print()

print('Inteiro para Flutuante') 
print(float(valor_inteiro))
print()

print('String para Inteiro')
print(int(valor_string_inteiro))
print()

print('String para Flutuante')
print(float(valor_string_flutuante))
print()

print('Flutuante para Inteiro')
print(int(valor_flutuante))
print()

print('Flutuante para String')
print(str(valor_string_flutuante))
print()

# Escrevendo na tela
print('Olá')
print('Qual o seu nome?')

# Recebendo o valor digitado pelo usuário
nome = input()

# Escrevendo com o nome do usuário
print('Prazer em conhecer você,' + nome)

# Verificando quantos caracteres existem no nome do usuário. 
# Como a resposta é um inteiro, utiliza o str() para imprimir 
# o valor como string
print('Seu nome tem ' + str(len(nome)) + ' letras')
print('Qual a sua idade?')
idade = input()

# Soma (idade + 1) de depois converte o valor para uma string 
# para ser impressa
print('Eu tenho ' + str(int(idade) + 1))
