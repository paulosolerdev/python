p1 = {
    'nome': 'Paulo',
    'sobrenome': 'Soler',
}

# print(p1.get('nome'))
# print(p1.get('nome', ''))

# nome = p1.pop('nome')
# print(nome)
# print(p1)


# ultima_chave = p1.popitem()

# print(ultima_chave)
# print(p1)


# print(p1)

# p1.update({
#     'nome': 'Novo Valor'
# })

# print(p1)


# p1.update(nome = 'novo valor', idade = 39)

# tupla = ('nome', 'novo valor'),
# print(p1)

lista = [['nome', 'novo valor'], ['idade', 30]]

p1.update(lista)
print(p1)
