# Desafio 2 - Strings
# 1. Pergunte ao usuário em qual cidade e o estado em que ele(a) mora
nome = input('Qual é o seu nome?')
cidade = input('Qual é a sua cidade que você mora?')
estado = input('Qual é o Estado que você mora?')
# 2. Imprima uma mensagem diga a cidade em que o usuário mora. 
print(nome, "é da cidade de", cidade, estado)
#    O nome da cidade deve estar todo em letras maiúsculas.
print(nome, "é da cidade de", cidade.upper(), estado)
# 3. Imprima uma mensagem diga o estado em que o usuário mora. 
print(nome, "é do Estado de:", estado)
#    O nome do estado deve estar todo em letras maiúsculas.
print(nome, "é do Estado de:", estado.upper())
#    Utilize uma forma de formatação de string diferente da que foi usada no item 2.
print(f'{nome.title()} é da cidade de {cidade.capitalize()}/{estado.upper()}')