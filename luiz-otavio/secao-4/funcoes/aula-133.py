# # Lambda

# lista = [4, 23, 1, 23, 56, 5, 6, 21, ]
# lista.sort()
# # sorted(lista) cria uma nova lista com cópia rasa

# print(lista)

lista = [
    {'nome': 'Paulo', 'sobrenome': 'Soler'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Susana', 'sobrenome': 'Mottes'},
    {'nome': 'Kátia', 'sobrenome': 'Mosciaro'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
]

# def ordena(item):
#     return item['sobrenome']

# lista.sort(key=ordena)

#lista.sort(key=lambda item: item['nome'])

def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)

# for item in lista:
#     print(item)
