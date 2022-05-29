# O Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes em do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança" e "polimorfismo".
# Opcionalmente, você pode também utilizar "propriedades", "encapsulamento" e "classe abstrata".


# # classe para controlar listas, veriﬁcação quanto à duplicidade de valores
# class ListaÚnica:
#     def __init__(self, elem_class):
#         self.lista = []
#         self.elem_class = elem_class
#     def __len__(self):
#         return len(self.lista)
#     def __iter__(self):
#         return iter(self.lista)
#     def __getitem__(self, p):
#         return self.lista[p]
#     def indiceVálido(self, i):
#         return i >= 0 and i < len(self.lista)
#     def adiciona(self, elem):
#         if self.pesquisa(elem) == -1:
#             self.lista.append(elem)
#     def remove(self, elem):
#         self.lista.remove(elem)

#     def pesquisa(self, elem):
#         self.verifica_tipo(elem)
#         try:
#             return self.lista.index(elem)
#         except ValueError:
#             return -1
#     def verifica_tipo(self, elem):
#             if type(elem) != self.elem_class:
#                 raise TypeError("Tipo inválido")
#     def ordena(self, chave=None):
#         self.lista.sort(key=chave)

# class Nome:
#     def  __init__(self, nome):
#         if nome == None or not nome.strip():
#             raise ValueError("Nome não pode ser nulo nem em branco")
#         self.nome = nome
#         self.chave = nome.strip().lower()
#     def  __str__(self):
#         return self.nome
#     def  __repr__(self):
#         return "<Classe {3} em 0x{0:x} Nome: {1} Chave: {2}>".format(id(self), self.nome, self.chave, type(self).__name__)
#     def  __eq__(self, outro):
#         print("__eq__  Chamado")
#         return self.nome == outro.nome
#     def  __lt__(self, outro):
#         print("__lt__  Chamado")
#         return self.nome < outro.nome


# joão = Cliente("João da Silva", "M", "3777-1234", "100000")
# maria = Cliente("Maria da Silva", "F", "2555-4321", "200000")

# Conta.extrato(joão)
# Conta.saque(1000)
