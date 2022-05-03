# Desafio 9 - Dicionários e Sets

# Escreva um código que imprima cada palavra da letra de música abaixo apenas uma vez.
# A saída deve estar ordenada (ordem lexicográfica).
# Saída esperada: And Breathe Come Down Everlong Hello Hold I I'll I'm I've If Out She Slow, 
# So The Tonight, When You've again along always and anything ask away be been breathe can 
# could down ever everything feel for forever good got head head, her here how in into 
# it know me my myself not now of only out over promise real red sang say she sing stop 
# the thing this throw to waited wanted waste when with wonder you you've your

# Dica: Python oferece recursos mais interessantes para trabalhar com strings, 
# como aspas triplas que permitem escrever longos textos mais facilmente. 
# Elas funcionam como as aspas, mas permitem digitar a mensagem em várias linhas.

everlong_foo_fighters = """
Hello
I've waited here for you
Everlong
Tonight, I throw myself into
And out of the red
Out of her head, she sang
Come down and waste away with me
Down with me
Slow, how you wanted it to be
I'm over my head
Out of her head, she sang
And I wonder
When I sing along with you
If everything could ever be this real forever
If anything could ever be this good again
The only thing I'll ever ask of you
You've got to promise not to stop when I say when
She sang
Breathe out
So I can breathe you in
Hold you in
And now
I know you've always been
Out of your head
Out of my head, I sang
And I wonder
When I sing along with you
If everything could ever feel this real forever
If anything could ever be this good again
The only thing I'll ever ask of you
You've got to promise not to stop when I say when
She sang
And I wonder
If everything could ever feel this real forever
If anything could ever be this good again
The only thing I'll ever ask of you
You've got to promise not to stop when I say when
"""

lista = everlong_foo_fighters.split()

#opção 1 - definindo uma função para remover palavras duplicadas
# def remove_dups(lista):
#     return sorted(set(lista))
# print(remove_dups(lista))

#opção 2 - Uma palavra em cada linha
palavras_ord = sorted(set(lista))
for x in palavras_ord:
    print(x, end = "\n")

#opção 3 - Removendo palavras duplicadas e ordenando
# palavras_ord = sorted(set(lista))
# print(palavras_ord)



# sorted() constrói uma nova lista ordenada.
# set() é uma coleção de itens únicos (distintos).
# split() dividi a string (usando como separador o caracter espaço) em uma lista.

