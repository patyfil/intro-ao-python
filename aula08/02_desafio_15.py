# Desafio 15 - Classes

# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos/Métodos: liga, desliga, acelera, desacelera.

# class Carro:
# Atribuindo valor aos atributos da classe
#     def __init__(self, cor, modelo):
#         self.ligado = False
#         self.cor = cor
#         self.modelo = modelo
#         self.velocidade_atual = 0
#         self.vel_min = 1
#         self.vel_max = 100

#     def ligar(self):
#         self.ligado = True

#     def desligar(self):
#         self.ligado = False
#

# Definindo método acelerar
#     def acelerar(self):
#         if not self.ligado:
#             return

#         if self.velocidade_atual < self.vel_max:
#             self.velocidade_atual += 10

# Definindo método desacelerar
#     def desacelerar(self):
#         if not self.ligado:
#             return

#         if self.velocidade_atual > self.vel_min:
#             self.velocidade_atual -= 10

#     def __str__(self) -> str:
#         return f'Carro ligado: {self.ligado} - Cor: {self.cor} - Modelo: {self.modelo} - Velocidade: {self.velocidade_atual}'

# # Crie uma instância da classe carro.
# chevrolet = Carro('Branco', 'Onix')
# Toyota = Carro ('Preto', 'Yaris')

# # Faça o carro "andar" utilizando os métodos da sua classe.
# print("Vamos acelerar o Onix, Velocidade inicial: ",
#       (chevrolet.velocidade_atual), 'km/h')
# chevrolet.ligar()
# Toyota.desligar()

# for i in range(0, 100, 10):
#     chevrolet.acelerar()
#     print(chevrolet,'Km/h')

# print("Onix", f'Chevrolet acelerou e está na velocidade máxima de: ',
#       (chevrolet.velocidade_atual), 'km/h')

# # Faça o carro "desacelerar" utilizando os métodos da sua classe.
# print("Vamos desacelerar o Onix, Velocidade atual: ",
#       (chevrolet.velocidade_atual), 'km/h')
# for i in range(0, 100, 10):
#     chevrolet.desacelerar()
#     print(chevrolet,'Km/h')

# print("Onix", f'Chevrolet desacelerou até chegar a velocidade: ',
#       (chevrolet.velocidade_atual), 'Km/h')


# # Faça o carro "parar" utilizando os métodos da sua classe.
# print("Vamos PARAR o Onix!")
# chevrolet.desligar()
# print('Carro Ligado:', chevrolet.ligado, '- ' "Velocidade com o carro parado:",
#       (chevrolet.velocidade_atual), 'km/h')

# # Faça o carro "LIGAR" e coloque na velocidade máxima.
# print("Vamos LIGAR o Onix, e colocar na velocidade Máxima: ")
# chevrolet.ligar()
# print('Carro Ligado:', chevrolet.ligado, '- ' 'Velocidade Máxima: ', (chevrolet.vel_max), 'km/h')


# Criando classe
class Carro:
    # Definindo atributos da classe
    ligado = False
    cor = "Preto"
    modelo = "Gol"
    velocidade_atual = 0

# Crie uma instância da classe carro.
    # Definindo construtor da classe
    def __init__(self, cor='Preto', modelo='Gol'):
        # Atribuindo valor aos atributos da classe
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade_atual = 0

    # Definindo método ligar
    def ligar(self):
        self.ligado = True

    # Definindo método desligar
    def desligar(self):
        self.velocidade_atual = 0
        self.ligado = False
            

    # Definindo método acelerar
    def acelerar(self):
        # aumenta o valor da velocidade em 10
        self.velocidade_atual += 10
        self.ligado = True

    # Definindo método desacelerar
    def desacelerar(self):
        # Diminui o valor da velocidade em 10
        if self.velocidade_atual >= 10:
            self.velocidade_atual -= 10
        else:
            self.ligado = False

    def __str__(self) -> str:
        return f'Carro ligado: {self.ligado} - Cor: {self.cor} - Modelo: {self.modelo} - Velocidade: {self.velocidade_atual}'


carro = Carro('Vermelho', 'KA')  # Instânciando um objeto carro
print('O carro inicia desligado [ligado(True), desligado(False)]:', carro.ligado)  # chamando atributo ligado
print('A cor do carro é: ', carro.cor)  # chamando atributo cor do carro
print('O modelo do carro é: ', carro.modelo)  # chamando atributo modelo do carro
print('A velocidade atual do carro é: ', carro.velocidade_atual, 'Km')  # chamando atributo velocidade_atual do carro
print('\n')

# Faça o carro "andar" utilizando os métodos da sua classe.
print('*'*20, 'Status do Carro Acelerando', '*'*20)
print('\n')
for _ in range(0, 10, 2):
    carro.acelerar()
    # print(carro.velocidade_atual, 'Km/h')
    print(carro)
print('\n')


# Faça o carro "parar" utilizando os métodos da sua classe.
carro.desligar()
print('*'*20, 'Status do Carro Desligado', '*'*20)
print('\n')
print(carro)
print('\n')
