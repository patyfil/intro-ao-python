# Escreva um programa que leia o arquivo "exemplo2.csv", e converta
# os registros desse CSV para o formato JSON. 
# Escreva um arquivo de saída que contenha o conteúdo em JSON.
import csv
import json

with open('exemplo2.csv', mode='r') as arquivo:
    leitor_csv = csv.DictReader(arquivo)
    Dict = []
    for registro in leitor_csv:
        Dict.append(registro)

with open('./saida_desafio_12.json', 'w', encoding='utf8') as arquivo_json:
    json.dump(Dict, arquivo_json)
    # arquivo_json = json.dumps(Dict)
    # print(arquivo_json)

