# # Condição

# nomes = ['Paulo', 'Susana', 'Rafaela']

# usuario = input('Digite o seu nome: ')


# if usuario in nomes:
#     print(f'Bem-vindo(a) {usuario}')
# else:
#     print(f'Usuário não cadastrado.')

#============================================#

# Estruturas Condicionais com Validação Simples (em string)

# nome = input(f'Digite o seu nome: ')


# if nome == 'Paulo':
#     print(f'Olá Paulo, você é o administrador do sistema!')
# elif nome in 'Ana Bárbara Carlos José Maria Fernando Tatiana':
#     print(f'Bem-vindo(a) {nome}, você é um(a) usuário(a) registrado(a) no sistema.')
# else:
#     print(f'Olá, você não está logado no sistema, suas permissões são restritas.')

#============================================#


# nome = input('Digite o seu nome: ')


# if nome == 'Paulo':
#     print(f'Olá Paulo, você é o administrador do sistema!')
# elif nome in 'Susana Ana Bárbara Maria Tatiana':
#     print(f'Bem-vinda {nome}, você é uma usuária registrada no sistema.')
# elif nome in 'Carlos José Fernando':
#     print(f'Bem vindo {nome}, você é um usuário registrado no sistema.')
# else:
#     print(f'Olá, você não está logado no sistema, suas permissões são restritas.')

#============================================#


# nome = input('Digite o seu nome: ')

# funcionarios_homens = ['Carlos', 'José', 'Fernando']
# funcionarias_mulheres = ['Susana', 'Ana', 'Bárbara', 'Maria', 'Tatiana']

# if nome == 'Paulo':
#     print(f'Olá Paulo, você é o administrador do sistema!')
# elif nome in funcionarias_mulheres:
#     print(f'Bem-vinda {nome}, você é uma usuária registrada no sistema.')
# elif nome in funcionarios_homens:
#     print(f'Bem vindo {nome}, você é um usuário registrado no sistema.')
# else:
#     print(f'Olá, você não está logado no sistema, suas permissões são restritas.')

#============================================#


veiculo1 = 'Gol'
veiculo2 = 'Corsa'
veiculo3 = 'Onibus'
cor1 = 'Branco'
cor2 = 'Vermelho'

if veiculo1 == 'Gol' or veiculo2 == 'Celta':
    print('Carro')
if veiculo1 == 'Gol' and cor1 == 'Branco':
    print('Gol Branco')
if veiculo1 == 'Onibus' and cor2 == 'Vermelho':
    print('Ônibus Vermelho')

