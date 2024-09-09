def divisao(n1, n2):
    if n2 == 0:
        return 'Operação Inválida'
    
    return n1 / n2

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

print(f'O resultado da divisão é: {divisao(num1, num2)}')
