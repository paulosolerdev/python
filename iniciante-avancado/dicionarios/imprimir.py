# Imprimindo só chaves e só valores

d1 = {'1':'A',
      '2':'B',
      '3':'C',
      '4':'D',
      '5':'E',
      '6':'F'}

# print(d1.keys())

# print(d1.values())

# #==================================#

# # Pesquisando o tamanho de um dicionário

# print(len(d1))

# #==================================#

# # Lendo as chaves ou valores por meio do laço for

# for chave in d1.keys():
#     print('Chave: ', chave)
# print('$==========$')
# for j in d1.values():
#     print('Valor: ', j)

# for itens in d1.items():
#     print('Chaves : Valores = ', itens)

#=====================================#

for c, v in d1.items():
    print(f'Chave: {c} -> Valor: {v}')
