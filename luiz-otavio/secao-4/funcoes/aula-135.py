# Empacotamento e desempacotamento de dicionários
# a, b = 1, 2
# a, b = b, a
#print(a, b)

pessoa = {
    'nome': 'Susana',
    'sobrenome': 'Mottes',
}

# (a1, a2), b = pessoa.items()
# print(a1, a2)
# print(b)

dados_pessoa = {
    'idade': 16, 
    'altura': 1.6,
}

#pessoas_completa = {**pessoa, 'chave':1}
pessoas_completa = {**pessoa, **dados_pessoa}

#print(pessoa, dados_pessoa)
#print(pessoas_completa)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


#mostro_argumentos_nomeados(nome='Joana', qlq=123)
#mostro_argumentos_nomeados(1, 2, nome='Joana')

mostro_argumentos_nomeados(**pessoas_completa)