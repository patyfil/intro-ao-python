# Desafio 14 - JSON e CSV

import sys
import requests
import json

# Crie uma aplicação que lê na linha de comando o nome de um feitiço
# Utilize a biblioteca requests para ler o JSON disponível em
# https://construdelas.blob.core.windows.net/intro-ao-python/feiticos.json
# Imprima para o usuário os dados sobre o feitiço que ele solicitou.
# Se o feitiço não foi encontrado, lance uma exceção.

# "Summoning Charm": {
#     "encantamento": "Accio",
#     "tipo": "Charm",
#     "descricao": "Summons an object",
#     "cor_da_luz": "None"
# }

# _____________________________ MODELO 1 - CASE SENSITIVE _________________________
# def pesquisa():
#     feitico = input('Digite o nome de um Feitiço para consultar: ')

#     arquivo_dict = buscar_json()  # dicionário gerado pela função 'buscar_json'

#     try:
#         if arquivo_dict[feitico]:
#             print('='*40)
#             print('\n')
#             print(f'Feitiço: ', feitico)
#             for chave, valor in arquivo_dict[feitico].items():
#                 resultado = (f'{chave}: {valor}')
#                 print(resultado)
#             print('\n')
#             print('='*40)

#     except KeyError:
#         print('\n')
#         print(" ******  FEITIÇO NÃO ENCONTRADO!  ******")
#         print('\n')
#         print('='*40)


# # FUNÇÃO PARA BAIXAR O ARQUIVO JSON DA URL E CONVERTER EM DICT:
# def buscar_json():
#     # request.get - baixa uma página html
#     resposta = requests.get(
#         "https://construdelas.blob.core.windows.net/intro-ao-python/feiticos.json")
#     # content - usado para acessar dados de carga útil no formato de bytes brutos.
#     arquivo_dict = json.loads(resposta.content)
#     # A função 'json.loads()' converte uma JSON string para o formato de Python 'dict'.
#     print('\n')
#     print('='*40)
#     print('Código da resposta:', resposta.status_code)
#     # 404: não encontrado, 200: ok
#     print('Tipo da resposta:', resposta.headers['Content-Type'])  # text/html
#     # print(resposta.text)
#     return arquivo_dict


# pesquisa()

# _____________________________ MODELO 2 - NO-CASE SENSITIVE _________________________
# FUNÇÃO PARA SOLICITAR QUE O USUÁRIO DIGITE O NOME DO FEITIÇO

def entrada():
    feitico = input('Digite o nome de um Feitiço para consultar: ')
    feitico = feitico.lower()
    return feitico

# FUNÇÃO PARA PESQUISAR SE O NOME DIGITADO PELO USUÁRIO TEM NO ARQUIVO 'arquivo_dict'
def pesquisa():
    feitico = entrada()  # feitiço digitado pelo usuário
    arquivo_dict = buscar_json()  # dicionário gerado pela função 'buscar_json'

    try:
        if arquivo_dict[feitico]:
            print('='*40)
            print('Feitiço encontrado!!!\n')
            print(f'Feitiço: ', feitico.upper())
            for chave, valor in arquivo_dict[feitico].items():
                resultado = (f'{chave}: {valor}')
                print(resultado.title())
            print('\n')
            print('='*40)

    except KeyError:
        print('\n')
        print(" ******  FEITIÇO NÃO ENCONTRADO!  ******")
        print('\n')
        print('='*40)

# FUNÇÃO PARA BAIXAR O ARQUIVO JSON DA URL E CONVERTER EM DICT:
def buscar_json():
    # request.get - baixa uma página html
    resposta = requests.get(
        "https://construdelas.blob.core.windows.net/intro-ao-python/feiticos.json")
    # content - usado para acessar dados de carga útil no formato de bytes brutos.
    arquivo_dict = json.loads(resposta.content.lower())
    # A função 'json.loads()' converte uma JSON string para o formato de Python 'dict'.
    print('\n')
    print('='*40)
    print('Consultando o site....\nCódigo da resposta:', resposta.status_code)
    # 404: não encontrado, 200: ok
    print('Tipo da resposta:', resposta.headers['Content-Type'])  # text/html
    # print(resposta.text)
    return arquivo_dict


pesquisa()
