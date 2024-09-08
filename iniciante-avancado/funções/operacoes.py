# Fazendo operações dentro de uma função

# n1 = int(input('Digite o primeiro número: '))
# n2 = int(input('Digite o segundo número: '))

# print(f'O resultado da soma é: {n1 + n2}')

def soma(n1, n2):
    return f'O resultado da soma é: {n1 + n2}'

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print(soma(n1, n2))
