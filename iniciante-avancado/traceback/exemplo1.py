# num1 = 13
# num2 = ad

# soma = num1 + num2

# print(soma)

while True:
    try:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        soma = num1 + num2
        print(f'O resultado da soma é: {soma}')
        break
    
    except ValueError:
        print('Número inválido, tente novamente. ')
