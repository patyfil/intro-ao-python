# Desafio 5 - Listas e loops
# Crie uma lista com 60 números começando com o valor 1 e indo até o número 60 
# (ou seja, o número 60 deve estar na lista).
print('\n')
print('='*20, '60 números de 1 a 60', '='*20)
lista = list(range(1, 61))
print('índice | item')
print('------ | ----')
for i, item in enumerate(lista):
        print(f'   {i}   |  {item}')
print('\n')
# Imprima todos os itens da sua lista de índice par. Imprima o índice e o item.

#******************** ÍNDICE PAR
print('='*20, 'ÍNDICE PAR', '='*20)
print('índice | item')
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'   {i}   |  {lista[i]}')
print('\n')
#******************** ITEM PAR 
print('='*20, 'ITEM PAR', '='*20)
print('índice | item')
print('------ | ----')
for i, item in enumerate(lista):
    if item % 2 == 0:
        print(f'   {i}   |  {item}')
print('='*20)

