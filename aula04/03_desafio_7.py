# Desafio 7 - Debug

# O programa abaixo deve calcular a média dos valores digitados pelo usuário.
# No entanto, ele não está funcionando bem. Você pode consertá-lo?

def calcular_media(valores):
    soma = 0.0  # 0.0 somar todos os valores
    for i, valor in enumerate(valores):
        soma += valor  # soma = soma + valor
        tamanho = i + 1
        media = soma / tamanho
        return media


continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
    if valor.isdigit():  # SE a var 'valor' receber somente número, a var 'continuar' será TRUE / Retorna TRUE se todos os caracteres forem dígitos, caso contrário, False.
        valores.append(int(valor)) # add valor digitado no final da sequencia valores[]
        continuar = True        
    elif valor.lower() == 'ok': # SENÃO SE a var 'valor' receber 'ok', a var 'continuar' será FALSE
        continuar = False
    else:
        print('Valor digitado é inválido, digite novamente')
        continuar = True

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {}'.format(valores, media))
  
  
  
