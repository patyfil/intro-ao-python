# Desafio 12 - CSV e JSON

# Escreva um programa que leia o arquivo "exemplo2.csv", e converta
# os registros desse CSV para o formato JSON.
# Escreva um arquivo de saída que contenha o conteúdo em JSON.
import csv
import json

with open('exemplo2.csv', 'r') as arquivo:
    leitor_csv = csv.DictReader(arquivo)
    dict = []
    for registro in leitor_csv:
        dict.append(registro)
        # print(dict)
    # for i, cont in enumerate(leitor_csv):
    #     dict[i + 1] = cont

    with open('./saida_desafio_12.json', 'w') as arquivo_json:
        json.dump(dict, arquivo_json, ensure_ascii=False, indent=4)
    # arquivo_json = json.dumps(Dict)
    # print(arquivo_json)

        # json.dump(dict, arquivo_json, indent=4)
