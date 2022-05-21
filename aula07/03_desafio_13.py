#  Desafio 13 - Decorators

import time

# Crie um decorator que calcule o tempo de execução de uma determinada função
def calcula_duracao(funcao):
    def wrapper():
        # Calcula o tempo de execução
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()
        tempo_total = tempo_final - tempo_inicial

        # Formata a mensagem que será mostrada na tela
        print(
            f'O Tempo total de execução do programa: {tempo_total:.2f} segundos')
    return wrapper

# Aplique seu decorator na função abaixo e veja quanto tempo
# a busca de um mesmo valor em um set e uma lista demoram para serem executadas
def encontrar_item(container, item):
    return item in container

# Fluxo de execução principal
@calcula_duracao
def main():
    tamanho = 1000000
    set_grande = set(range(tamanho))
    lista_grande = list(range(tamanho))
    item = 500399
    encontrar_item(set_grande, item)
    encontrar_item(lista_grande, item)

if __name__ == '__main__':
    main()