# Criando um conjunto numérico (set) em Python

# SET

# conjunto = {5, 10, 15, 20}

# print(type(conjunto))

#=======================================#

# Operações entre conjuntos

# cj1 = {1, 2, 3, 4, 5}

# cj2 = {1, 3, 5, 7, 9}

# print(cj2 - cj1)

#=======================================#

# União de conjuntos númericos

# conjunto1 = {5, 10, 15, 20, 25}

# conjunto2 = {1, 2, 3, 4, 5}

# uniao = conjunto1.union(conjunto2)

# print(uniao)

#=======================================#

# Intersecção de dois conjuntos

# conjunto1 = {5, 10, 15, 20, 25}

# conjunto2 = {1, 2, 3, 4, 5}

# interseccao = conjunto1.intersection(conjunto2)

# print(interseccao)

#=======================================#

# Operações lógicas entre conjuntos

# conjunto1 = {5, 10, 15, 20, 25}

# conjunto2 = {1, 2, 3, 4, 5}

# uniao = conjunto1.union(conjunto2)

# print(uniao == conjunto1)

# print(uniao >= conjunto2)

# #=======================================#

# # Diferença entre conjuntos

# c1 = {1, 2, 3, 4, 5} - {1, 2}

# print(c1)

#=======================================#

# Diferença entre conjuntos associados a variáveis

c1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
c2 = {1, 3, 5, 7, 9}

print(c1 - c2)


#=======================================#


# Adicionando elementos a um conjunto


# cj = {1, 2, 3, 4, 5}

# cj.add(6)

# print(cj)

#


#=======================================#


# Removendo elementos de um conjunto


# cj = {1, 2, 3, 4, 5}

# cj.remove(2)

# print(cj)

#

#=======================================


# Checando se um elemento está presente em um conjunto

# cj = {1, 2, 3, 4, 5}

# print(2 in cj)

#


#=======================================


# Iterando sobre um conjunto


# cj = {1, 2, 3, 4, 5}


# for elemento in cj:
#     print(elemento)

#


#=======================================


# Convertendo um conjunto em uma lista


# cj = {1, 2, 3, 4, 5}


# lista = list(cj)


# print(lista)


#=======================================


# Contando o número de elementos de um conjunto


# cj = {1, 2, 3, 4, 5}


# print(len(cj))


#


#=======================================


# Ordenando os elementos de um conjunto


# cj = {5, 10, 15, 20, 25}


# print(sorted(cj))


#


#=======================================


# Fazendo uma cópia de um conjunto


# cj = {1, 2, 3, 4, 5}


# cj_copia = cj.copy()


# print(cj_copia)


#


#=======================================


# Atualizando um conjunto com dados de outro


# cj1 = {1, 2, 3, 4, 5}

# cj2 = {1, 3, 5, 7, 9}


# cj1.update(cj2)


# print(cj1)


#


#=======================================


# Verificando se um conjunto pertence ao outro


# cj1 = {1, 2, 3, 4, 5}

# cj2 = {1, 3, 5, 7, 9}


# print(cj2.issubset(cj1))


#


#


#=======================================


# Verificando se um conjunto é um superconjunto de outro


# cj1 = {1, 2, 3, 4, 5}

# cj2 = {1, 3, 5, 7, 9}


# print(cj1.issuperset(cj2))


#


#


#=======================================


# Verificando se um conjunto é um subconjunto de outro


# cj1 = {1, 2, 3, 4, 5}

# cj2 = {1, 3, 5, 7, 9}


# print(cj2.issubset(cj1))


#


#


#=======================================

