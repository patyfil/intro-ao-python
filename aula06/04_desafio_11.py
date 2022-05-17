# Desafio 11 - Ler e escrever em arquivos


# Dado um arquivo de entrada, escreva um programa que leia o conteudo do arquivo para uma string,
# e escreva um outro arquivo de saída que imprima o texto ao contrário.
# Exemplo de entrada: Oi mulheres maravilhosas do curso de Python do ConstruDelas!
# Exemplo de saída: !saleDurtsnoC od nohtyP ed\nosruc od sasohlivaram serehlum iO

# arquivo = 'entrada_desafio_11.txt'


########## OPÇÃO 1 ##############

# entrada = './entrada_desafio_11.txt'
# with open(entrada, 'r') as file1:
#     text = file1.read()

# saida = './saida_desafio_11.txt'
# with open(saida, 'w') as file2:
#     file2.write(text[::-1])



#   ANOTAÇÕES

# Para fazer uma cópia identica:
# from shutil import copyfile
# copyfile('./entrada_desafio_11.txt', './saida_desafio_11.txt')

# A função read() lê todo o conteúdo do arquivo e retorna uma string
# arquivo = open("./entrada_desafio_11.txt")
# print(arquivo.read())
# arquivo.close()


########## OPÇÃO 2 ##############
# https://datamarte.com/manipulando-arquivos-txt-e-binarios-com-python/

def novo_arq():
    with open('./entrada_desafio_11.txt', 'r') as arq1:
        texto = arq1.read()
    with open('./saida_desafio_11.txt', 'w') as arq3:
        arq3.write(texto[::-1])
    return arq3
def main():
    novo_arq()
main()