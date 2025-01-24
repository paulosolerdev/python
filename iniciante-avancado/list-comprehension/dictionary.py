# lista = [('chave1', 'chave2'), ('chave2', 'valor2'), ('chave3', 'valor3')]

# dicionario = {x:y for x, y in lista}
# dicionario2 = dict(lista)

# print(f"{dicionario}")
# print(f"{dicionario2}")

produtos = [('Caneta', 1.99), ('Lápis', 1.49), ('Caderno', 8.99)]

# Criando o dicionário com os preços ajustados
produtos_com_imposto = {x: y * 1.6 for x, y in produtos}

# Exibindo os resultados formatados
print(f'Preços SEM impostos: {produtos}')
print('Preços COM impostos: {', end='')
print(', '.join(f"'{x}': {y:.2f}" for x, y in produtos_com_imposto.items()), end='}\n')
