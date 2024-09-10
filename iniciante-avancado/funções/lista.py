# Desempacotando uma lista para que os elementos dela virem argumentos

lista = ['nome', 'idade', 'sexo', 'nacionalidade']

def funcao(*args):
    print('Informações Necessárias: ')
    print(args)

funcao(*lista)
