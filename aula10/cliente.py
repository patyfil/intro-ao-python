class Nome:
    def __init__(self, nome, sexo, telefone):
        self.nome = nome
        self.__sexo = sexo  # ENCAPSULAMENTO
        self.telefone = telefone

    @property
    def sexo(self):
        print('getter de sexo')
        return self.__sexo

class Cliente(Nome):
    def __init__(self, nome, sexo, telefone):
        super().__init__(nome, sexo, telefone)
        self.conta = None

    def inserir_conta(self, conta):
        self.conta = conta

    def __str__(self):
        return f'Nome: {self.nome}\nSexo: {self.__sexo}\nTelefone: {self.telefone}\n'


# cliente1 = Cliente('Patrícia de Souza', 'F', '3244-0044', '3500.00')
# cliente2 = Cliente('Priscila Sá', 'F', '3200-0331', '2500.00')
# print('===================================')
# print('Dados do cliente 1: ')
# print(cliente1)
# print('===================================')
# print('Dados do cliente 2: ')
# print(cliente2)
# print('===================================')
# print()

# # Banco não consegue alterar o 'sexo' porque é privado (__underscore)
# cliente1.__sexo = 'M'
# print('*'*5, 'NÃO É POSSÍVEL ALTERAR SEXO', '*'*5)
# print(cliente1)
# print('===================================')
# print()

# cliente1.__sexo = 'M'
# print(cliente1.__sexo)
