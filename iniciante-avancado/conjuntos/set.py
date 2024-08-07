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
