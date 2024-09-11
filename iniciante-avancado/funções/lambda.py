# Expressões Lambda / Funções Vazias

def multiplica(num1, num2):
    return num1 * num2

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

#variavel = multiplica(num1, num2)

variavel = lambda num1, num2: num1*num2

print(variavel(num1, num2))
