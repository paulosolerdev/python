def identificacao(*args, **kwargs):
    # Itera sobre os argumentos posicionais (*args)
    for nome in args:
        # Itera sobre os argumentos nomeados(**kwargs)
        idade = kwargs.get('idade')
        sexo = kwargs.get('sexo')

        # Verifica se idade e sexo foram passados corretamente
        if idade is not None and sexo is not None:
            print(f'Nome: {nome}, Idade: {idade}, Sexo: {sexo}')
        else:
            print('Dados insuficientes!')


# Chamando a função com nome, idade e sexo
pessoa = identificacao('Soler', idade = 39, sexo = 'M')
pessoa1 = identificacao('Susana', idade = 40, sexo = 'F')
