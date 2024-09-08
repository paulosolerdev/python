# Fazendo operações compostas dentro de uma função

def aumento_percentual(valor, percentual):
    return (valor + (valor * percentual / 100))

num1 = int(input('Digite o valor: '))
num2 = int(input('Você deseja somar quantos % ?: '))

calculo = aumento_percentual(num1, num2)

print(f'O valor final será: {calculo}')

print(f'O valor final será: {round(calculo, 2)} reais.')

print(f'O valor final será: R${calculo:.2f} reais.')
