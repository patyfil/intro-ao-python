from abc import ABC, abstractmethod

from cliente import Cliente
# ABC (abstract base classes, ou classes base abstratas).
# As classes ABC tem dois propósitos: agir como um contrato (interface) e
# bloquear a criação de instâncias/objetos dessa classe.


class Conta(ABC):
    def __init__(self, agencia, conta, saldo, renda):
        self.agencia = agencia
        self.conta = conta
        self.saldo = float(saldo)
        self.renda = float(renda)

    def deposito(self, valor):
        self.saldo += valor
        # adiciona ao extrato
        self.extrato()
        print('DEPÓSITO EFETUADO COM SUCESSO: R$ %.2F' % valor)

    def extrato(self):
        print('\n')
        print('           ------  Extrato  ------       ')
        print(f'Agência: {self.agencia} '
              f'\nConta número: {self.conta} '
              f'\n--------------')
        print('Saldo: R$ %.2F' % self.saldo)
        print('Renda R$ %.2F' % self.renda)
        print('\n')
        print('Disponivel: R$ %.2F' % (self.saldo + self.renda))
    #     self.menu()
    #     while True:
    #         Conta.menu()

    # def menu(self):
    #     print('-' * 30)
    #     print(f'     MENU DE OPERAÇÕES')
    #     print('-' * 30)
    #     print('Opções:')
    #     print('1 - Extrato')
    #     print('2 - Depósito')
    #     print('3 - Saque')
    #     print('4 - Sair')
    #     opcao = input('Digite a opção desejada: ')
    #     if opcao == '1':
    #         self.extrato()
    #     elif opcao == '2':
    #         valor = float(input('Digite o valor a ser DEPOSITADO: '))
    #         self.deposito(valor)
    #     elif opcao == '3':
    #         valor = float(input('Digite o valor a ser SACADO: '))
    #         self.saque(valor)
    #     elif opcao == '4':
    #         exit()

    @abstractmethod
    def saque(self, valor):
        if valor < (self.saldo + self.renda):
            self.saldo -= valor
            # adiciona ao extrato
            self.extrato.append("- Saque: " + valor)
            return valor
        else:
            print('Saldo insuficiente para esta operação')


class ContaNormal(Conta):
    def saque(self, valor):
        if self.saldo < valor:
            print(f'Agência: {self.agencia} '
                  f'\nConta número: {self.conta} '
                  f'\n--------------')
            print('TENTATIVA DE SAQUE DE: R$ %.2F' % valor)
            print('Saldo insuficiente')
            print('Saldo: R$ %.2F' % self.saldo)
            print('Renda R$ %.2F' % self.renda)
            print('Disponivel: R$ %.2F' % self.saldo)
            return
        self.saldo -= valor
        self.extrato()


class ContaEspecial(Conta):
    def saque(self, valor):
        if (self.saldo + self.renda) < valor:
            print(f'Agência: {self.agencia} '
                  f'\nConta número: {self.conta} '
                  f'\n--------------')
            print('TENTATIVA DE SAQUE DE: R$ %.2F' % valor)
            print('Saldo insuficiente')
            print('Saldo: R$ %.2F' % self.saldo)
            return

        self.saldo -= valor
        self.extrato()
        print('SAQUE EFETUADO COM SUCESSO: R$ %.2f' % valor)





