# # Sintaxe básica de uma string

# frase = 'Atributo em formato alfanumérico...'
# frase2 = 'Incluindo números e símbolos!!!'

# print(frase)
# print(frase2)

#===============================================#

# # Contando quantos caracteres compõe uma string

# frase1 = 'Porto Alegre é uma cidade brasileira.'

# print(len(frase1))
# print(len(frase1) - frase1.count(' '))

#===============================================#

# Substituindo elementos de uma string

# frase = 'Porto Alegre é uma cidade brasileira'

# frase = frase.replace('Porto Alegre', 'Curitiba')

# print(frase)

#===============================================#

# frase = 'Porto Alegre é uma cidade brasileira.'

# print(frase.count('a'))
# print(frase.count('A'))

# print(frase.find('é'))  # Qual a posição do caractere 'é'

# print(frase[16])

# print(frase.split())

#===============================================#

# Concatenando strings por meio de variáveis

# mensagem = 'Seja bem-vindo(a) '
# usuario = 'Ana Clara'

# base = mensagem + usuario
# print(base)

#===============================================#

# # Concatenando diferentes tipos de dados em uma string

# nome = 'Ana Clara'
# idade = 12

# print(f'{nome} tem {idade} anos.')

# aviso = f'Atenção, geradores entrarão em manutenção às: {str(12)} horas.'
# print(aviso)

#===============================================#

# Operadores lógicos em uma string

# aviso = 'Não é permitida a entrada de menores de 18 anos.'

# print(aviso)

# print('anos' in aviso)

# print('gestante' not in aviso)

#===============================================#

# Letras maiúsculas ou minúsculas em uma string

# alerta = 'Risco de morte'

# print(alerta.upper())

# print(alerta.lower())

# print(alerta.title())

# print(alerta.capitalize())

#===============================================#

# Convertendo outro tipo de dado para string

num1 = 5623
num2 = str(num1)

print(type(num1))
print(type(num2))
