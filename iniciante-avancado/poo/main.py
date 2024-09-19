from base import BaseDeDados

clientes = BaseDeDados()

clientes.inserir('Ana', 991415888)
clientes.inserir('Paulo', 991028222)
clientes.inserir('Luara', 999888523)

clientes.listar()

print('$========================$')

clientes.apagar('Ana')

print('Apagando Ana.')

print('$========================$')

clientes.listar()
