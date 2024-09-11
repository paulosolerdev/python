# Modificando uma variável global de dentro de uma função

num1 = 100

print(f'Variável com seu valor inicial: {num1}')


def modificador():
    global num1
    num1 = 200
    print(f'Variável alterada dentro da função: {num1}')

modificador()


print(f'Variável atualizada pela função modificador: {num1}')
