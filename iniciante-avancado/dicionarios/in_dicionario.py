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

    print()

print()

# Atualizando um valor


usuarios['João']['Salário'] = '2200'

print(f'Novo salário de João: {usuarios["João"]["Salário"]}')

print()

# Adicionando um novo funcionário

usuarios['Pedro'] = {'Identificador':'0004',
                     'Cargo':'Gerente',
                     'Salário':'3000'}

print(f'Funcionário adicionado: {usuarios["Pedro"]}')

print()

# Removendo um funcionário

del usuarios['Maria']

print(f'Funcionário removido: {usuarios.get("Maria")}')

print()

# Buscando um funcionário pelo identificador

for chave, valor in usuarios.items():
    if valor['Identificador'] == '0003':
        print(f'Funcionário encontrado: {chave}')

        for i, j in valor.items():
            print(f'\t {i} = {j}')

        print()
        break
else:
    print('Funcionário não encontrado')

print()

# Ordenando os funcionários pelo salário

funcionarios_ordenados = sorted(usuarios.items(), key=lambda x: x[1]['Salário'], reverse=True)

for chave, valor in funcionarios_ordenados:
    print(f'Funcionário: {chave}')

    for i, j in valor.items():
        print(f'\t {i} = {j}')

    print()

print()
