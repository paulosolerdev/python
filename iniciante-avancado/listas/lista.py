# # Criando uma lista simples

# lista = ['Ana Clara', 'Carlos', 19.99, 'Michele', 'Gustavo', 1987]

# print(lista)

#==================================================#

# Descobrindo o elemento de uma lista através de seu índice

# lista = ['Ana Clara', 'Carlos', 'Susana', 'Michele', 'Gustavo', 1987]

# print(lista[2])

#==================================================#

# Descobrindo o número de índice de um determinado elemento

# lista = ['Ana Clara', 'Carlos', 'Susana', 'Michele', 'Gustavo', 1987]

# print(lista.index('Susana'))

#==================================================#

# Descobrindo o número de elementos de uma lista

# lista = ['Ana Clara', 'Carlos', 'Susana', 'Michele', 'Fernanda', 1987]

# print(len(lista))

#==================================================#
# Adicionando um novo elemento à lista

# lista = ['Ana Clara', 'Carlos', 'Susana', 'Michele', 'Fernanda', 1987]

# lista.append('Paulo')
# lista.append(1985)

# print(lista)

#==================================================#
# Adicionando (sobrescrevendo) um novo elemento à lista em uma posição específica

# lista = ['Ana Clara', 'Carlos', 'Susana', 'Michele', 'Fernanda', 1987]

# lista[2] = 'José'
# lista[4] = 99999

# print(lista)

#==================================================#

# Adicionando um novo elemento à lista em uma posição específica

# lista = ['Ana Clara', 'Carlos', 'Susana', 'Michele', 'Fernanda', 1987]

# lista.insert(2, 'José')
# lista.insert(3, ('Paulo'))

# print(lista)

#==================================================#

# Removendo um elemento de uma lista pelo seu número de índice

# lista = ['Ana Clara', 'Carlos', 'Susana', 'Michele', 'Fernanda', 1987]

# lista.remove(lista[5])

# print(lista)

#==================================================#
# Listas dentro de listas

cadastro = [1, 2, 3, 4, ['Ana', 'Maria', 'Paulo', 'Susana', 'Rafaela']]

print(cadastro)
print(cadastro[4])
