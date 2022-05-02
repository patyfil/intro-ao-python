# Desafio 5 - Listas e loops
# Crie uma lista com 60 números começando com o valor 1 e indo até o número 60 (ou seja, o número 60 deve estar na lista).
lista = list(range(1, 61))
print(lista)

# Imprima todos os itens da sua lista de índice par. Imprima o índice e o item.
# print(lista[1::2])
par = lista[1::2]
print('índice | item')
print('------ | ----')
for i, item in enumerate(par):
    print(f'   {i}   |  {item}')
print()