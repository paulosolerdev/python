def boas_vindas(nome, nacionalidade = 'Brasileiro(a)'):
    print(f'{nome} é {nacionalidade}')

nome = input('Digite o seu nome: ')
ex1 = boas_vindas(nome)

nacionalidade = input('Digite a sua nacionalidade: ')
ex2 = boas_vindas(nome, nacionalidade)
