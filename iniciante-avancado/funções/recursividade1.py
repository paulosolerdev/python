# # Recursividade

# def fatorial(num):
#     if num == 1:
#         return 1
    
#     return num * fatorial(num - 1)

# fator = fatorial(int(input('Digite o número a descobrir o fatorial: ')))

# print(f'O resultado é: {fator}')


def fatorial(num):
    print(f'Chamando fatorial {num}')
    if num == 1:
        print(f'Base: fatorial(1) = 1')
        return 1
    resultado = num * fatorial(num-1)
    print(f'Retorno de fatorial({num}): {resultado}')
    return resultado

fator = fatorial(int(input('Digite o número a descobrir o fatorial: ')))

print(f'O resultado é: {fator}')
