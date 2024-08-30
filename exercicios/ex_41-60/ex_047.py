itens = ['Caneta', 'Lápis', 'Borracha', 'Caderno']
precos = ['1,99', '0,99', '0,50', '9,90']

dicionario = dict(keys=itens, values=precos)

print(dicionario)
print(type(dicionario))

for c, v in dicionario.items():
    print(f'{c} {v}')