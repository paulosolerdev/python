# Dicionários dentro de dicionários

usuarios = {'João':{'Identificador':'0001',
                    'Cargo':'Porteiro',
                    'Salário':'2000'},
            'Maria':{'Identificador':'0002',
                     'Cargo':'Aux. Limpeza',
                     'Salário':'1900'},
            'José':{'Identificador':"0003",
                    'Cargo':'Técnico',
                    'Salário':'2500'}}

for chave, valor in usuarios.items():
    print(f'Funcionário: {chave}')

    for i, j in valor.items():
        print(f'\t {i} = {j}')
