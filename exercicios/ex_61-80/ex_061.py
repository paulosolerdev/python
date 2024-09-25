def soma(*args):
    
    num = 0

    for valor_digitado in args:
        num += valor_digitado

    print(f'O resultado da soma é: {num}')

soma = soma(18, 43, 99, 1)
