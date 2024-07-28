paulo = {'nome': 'Paulo Soler',
         'idade': '39',
         'formação': ['Desenvolvedor de Software',
         'Profissional Linux']}

print(paulo)
print(f"Há {len(paulo)} pares chave:valor neste dicionário.")
print(f'A idade {paulo.get('nome')} é de {paulo.get('idade')} anos.')

print(f'Há {len(paulo)} chaves neste dicionário, e elas são: \n\t{paulo.keys()}')
print(f'E os valores são: \n\t{paulo.values()}')

print(f'{paulo.items()}')

for chave, valor in paulo.items():
    print(f'Chave: {chave}, Valor: {valor}')
