pessoa = {
    'nome': 'pessoa Soler',
    'idade': 39,
    'formação': ['Desenvolvedor de Software', 'Profissional Linux']
}

print(pessoa)
print(f"Há {len(pessoa)} pares chave:valor neste dicionário.")
print(f'O nome é {pessoa.get("nome")} e a idade é de {pessoa.get("idade")} anos.')

print(f'Há {len(pessoa)} chaves neste dicionário, e elas são: \n\t{list(pessoa.keys())}')
print(f'E os valores são: \n\t{list(pessoa.values())}')

print(f'{list(pessoa.items())}')

for chave, valor in pessoa.items():
    print(f'Chave: {chave}, Valor: {valor}')

pessoa['idade'] = 40
print(pessoa)

pessoa['formação'].append('Cientista de Dados')
print(pessoa)

pessoa['cidade'] = 'Balneário Camboriú'
pessoa['nacionalidade'] = 'brasileiro'
print(pessoa)
