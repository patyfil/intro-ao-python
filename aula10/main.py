from banco import Banco
from conta import ContaEspecial, ContaNormal
from cliente import Cliente, Nome

banco = Banco()

# Inserindo dados dos clientes
# cliente = Cliente(nome, sexo, telefone)
cliente1 = Cliente('Patrícia de Souza', 'F', '3244-0044')
cliente2 = Cliente('Priscila Sá', 'F', '3200-0331')
cliente3 = Cliente('Alex', 'M', '3248-4488')

# Definindo se o cliente tem conta especial ou normal
# conta = Conta(agencia, conta, saldo, renda)
conta1 = ContaEspecial('Delas', 101, 0, 1000)
conta2 = ContaEspecial('Delas', 102, 0, 1000)
conta3 = ContaNormal('Delas', 103, 0, 1000)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

# Inserindo Cliente e Conta na Class 'Banco'
banco.inserir_cliente(cliente1)  
banco.inserir_conta(conta1) 
banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)  
banco.inserir_cliente(cliente3)
banco.inserir_conta(conta3)

# Efetuando operações nas contas
if banco.autenticar(cliente1):
    cliente1.conta.deposito(40)
    print('-'*50, '\n')
    cliente1.conta.saque(1000)
    print('-'*50, '\n')
    cliente1.conta.saque(1000)
    print('-'*50,'\n')
    
else:
    print('Cliente não autenticado/Conta Inexistente')
    print('-'*50, '\n')

if banco.autenticar(cliente2):
    cliente2.conta.deposito(10)
    print('-'*50, '\n')
    cliente2.conta.saque(10)
    print('-'*50, '\n')
else:
    print('Cliente não autenticado/Conta Inexistente')
    print('-'*50, '\n')

if banco.autenticar(cliente3):
    cliente3.conta.deposito(100)
    print('-'*50, '\n')
    cliente3.conta.saque(200)
    print('-'*50, '\n')
else:
    print('Cliente não autenticado/Conta Inexistente')
    print('-'*50, '\n')