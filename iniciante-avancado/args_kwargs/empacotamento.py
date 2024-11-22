numeros = (33, 1987, 2020, 19.90, 100000000)
dados = {'Nome': 'Paulo', 'Profissão':'Engenheiro de Software'}
nomes = ['Paulo', 'Susana']
numbers = {'Nine':9, 'Ten':10}


def identificacao(*args, **kwargs):
    print(args)
    print(kwargs)


identificacao(*numeros, **dados)
identificacao(*nomes, **numbers)
