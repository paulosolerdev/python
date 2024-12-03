# # Dicionários

# pessoa = {
#     'nome': 'Paulo',
#     'sobrenome': 'Soler',
#     'idade' : 39,
#     'altura': 1.83,
#     'endereços': [
#         {'rua': 'Tali talks', 'número': 156},
#         {'rua': 'Balts Lue', 'número': 537},
#     ]
# }

# # print(pessoa['nome'])
# # print(pessoa['sobrenome'])

# # for chave in pessoa:
# #     print(chave, pessoa[chave])
pessoa = {}

chave = 'nome_completo'

pessoa[chave] = 'Paulo Soler'
pessoa['sobrenome'] = 'Soler'
lista = []

print(pessoa[chave])
print(pessoa)

pessoa[chave] = 'Susana Mottes'
print(pessoa)

del pessoa['sobrenome']
print(pessoa)
print(pessoa[chave])

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])
