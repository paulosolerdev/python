# Passando o parâmetro ao chamar a função

# def funcao(msg):
#     print(msg)

# mensagem = 'Boas vindas!'

# funcao(mensagem)

#===================================#

# def mensagem(nome):
#     print(f'Bem-vindo(a) {nome}')

# usuario = mensagem('Paulo Soler')

# print(usuario)

#===================================#

# Passando mais de um parâmetro para uma função

def mensagem(nome, idade):
    print(f'{nome} tem {idade} anos...')

usuario = mensagem('Paulo Soler', 33)

print(usuario)
