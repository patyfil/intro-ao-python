# Desafio 2 - Strings
# 1. Pergunte ao usuário em qual cidade e o estado em que ele(a) mora
nome = input('Qual é o seu nome? ')
cidade = str(input('Qual é a sua cidade que você mora? '))
estado = str(input('Qual é o Estado que você mora? '))
print('='*40)
print('\n')
# 2. Imprima uma mensagem diga a cidade em que o usuário mora. 
#    O nome da cidade deve estar todo em letras maiúsculas.
print(nome.upper(), "é da Cidade de", cidade.upper(),'/', estado.upper())
# 3. Imprima uma mensagem diga o estado em que o usuário mora. 
#    O nome do estado deve estar todo em letras maiúsculas.
#    Utilize uma forma de formatação de string diferente da que foi usada no item 2.
print('\n')
print(nome.upper() + ' ' + 'é do Estado de ' + estado.upper())
print('\n')
