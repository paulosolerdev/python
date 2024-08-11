# FUNÇÕES

# Sintaxe básica de uma função

# def nome_da_funcao2(parametros):
#     'corpo da função'

# def minha_funcao():
#     print('Minha primeira função personalizada!')

# variavel = minha_funcao()

#===============================================#

# Definindi uma função sem parâmetros

# def exibe_mensagem():
#     print('Seja bem-vindo!')
#     # poderia ser, dependendo do contexto, return 'Seja bem-vindo'!

# print(exibe_mensagem())

# msg = exibe_mensagem()

#===============================================#

# Chamando a função

# def mensagem():
#     print('Seja bem-vindo!')

# mensagem()

#===============================================#
 # Função associada a uma variável

# def mensagem():
#     print('Seja bem-vindo!')

# mensagem1 = mensagem()

# print(mensagem1)

#=======================#

# def mensagem():
#     return 'Seja bem-vindo!'

# mensagem1 = mensagem()

# print(mensagem1)

#=======================#

# Criando uma função que temporariamente não faz nada

# def funcao():
#     pass

# var = funcao()

# print(type(var))

#=======================#

# Função interagindo com variável que interage com o usuário

usuario = input('Digite o seu nome: ')

def mensagem(nome):
    print(f'Bem-vindo {nome}!')

#print(mensagem(usuario))
mensagem(usuario)
