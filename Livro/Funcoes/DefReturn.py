# Como a função só imprime um texto na tela, não é necessário utilizar return
def imprimir():
    print('Estou imprimindo...')


# Função que recebe o nome e sobremone e imprime na tela.
def meuNome(nome, sobrenome): 
    texto = 'Olá, me chamo ' + nome + ' ' +  sobrenome
    return texto

# Chamndo a função imprimir
imprimir()
print()

# Chamando a função meuNome.
# É importante passar os argumetos na ordem certa: primeiro o nome e depois o sobrenome.
print('Aqui os parametros forma passados errados')
funcao_meuNome = meuNome('Santos', 'Priscyla') # Issa forma está errada
print(funcao_meuNome)
print()

print('Aqui os parametros forma passados certos')
funcao_meuNome = meuNome('Priscyla', 'Santos') # Issa forma está certa
print(funcao_meuNome)
print()

# Chamando a função meuNome. Aqui não importa a ordem  argumetos, 
# pois estao sendo passados junto com as palavras-chaves
funcao_meuNome_com_palavraChave = meuNome(sobrenome='Santos', nome='Priscyla')
print(funcao_meuNome_com_palavraChave)
print()

# Caso não queria dar valor a um argumento
funcao_meuNome = meuNome('Priscyla', '')
print(funcao_meuNome)