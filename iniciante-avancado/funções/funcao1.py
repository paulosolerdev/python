# Interagindo com o usuário

# def funcao(msg='Olá', nome='usuário', msg2='Seja bem vindo!'):
#     nome = input('Digite o seu nome: ')
#     print(msg, nome, msg2)

# variavel1 = funcao()

# variavel2 = funcao(msg='Fala', msg2='Tá bão?')


# Interagindo com o usuário #3

def funcao(msg='Olá', nome='usuário', msg2='Seja bem vindo!'):
    return f'{msg} {nome}, {msg2}'

variavel1 = funcao(nome=input('Digite o seu nome: '))

print(variavel1)
