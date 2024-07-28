a = {1, 2, 3}
print(type(a))


# União de conjuntos
c1 = {1, 2}
c2 = {2, 3}

print(c1.union(c2))


# Intersecção de conjuntos
c1 = {1, 2}
c2 = {2, 3}

print(c1.intersection(c2))


# Salvando com .update()
c1 = {1, 2}
c2 = {2, 3}

c1.union(c2)
c1.update(c2)

print(c1)


# Verificando se um conjunto pertence ao outro
c1 = {1, 2}
c2 = {2, 3}

c1.union(c2)
print(c2 <= c1)

c1.update(c2)
print(c2 <= c1)


# Diferença entre conjuntos
c1 = {1, 2}
c2 = {2, 3}

c1.union(c2)
c1.update(c2)

c1 = c1 - {2}
print(c1)

#==========$ou$==========#
