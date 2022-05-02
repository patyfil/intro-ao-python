# Desafio 3 - datetime, booleans, variáveis
from datetime import datetime, timedelta

# Peça para o usuário digitar a data de seu próximo aniversário no formato brasileiro
niver = input('Digite a data do seu próximo aniversário no formato brasileiro (dd/mm/aaaa): ')

# Imprima uma mensagem dizendo quantos dias faltam para o aniversário dele
dias = datetime.strptime(niver, '%d/%m/%Y') - datetime.now()
print(f'Faltam {dias.days} dias para o seu aniversário!')

# Pergunte ao usuário se ele(a) gosta de aniversário e salve a resposta
gosta = input('Você gosta de aniversário?')

# Pergunte ao usuário se ele(a) vai fazer festa e salve a resposta
festa = input('Você vai fazer festa?')

# Imprima uma mensagem dizendo se o usuário vai ganhar presente ou não
# A regra é: o usuário só pode ganhar presente se gostar de aniversário e for fazer festa.
if gosta == "sim" and festa == "sim":
    print('\n Você vai ganhar presente!')
else:
    print('\nVocê não vai ganhar presente')
