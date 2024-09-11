# Escopo Global vs Escopo Local

variavel = 'Paulo'

def funcao():
    print(f'Print da variável do escopo global: {variavel}')

funcao()


def funcao2():
    variavel2 = 'Maria'
    print(f'Print da variável do escopo local: {variavel2}')

funcao2()
