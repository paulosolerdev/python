# Atributos de Classe

class Classe1:
    var1 = 101001

variavel1 = Classe1()


print(Classe1.var1)

print(variavel1.var1)


# Mudando um atributo de classe

Classe1.var1 = 'Maria'
# ou variavel1.var1 = 'Maria'
# Faz o mesmo através da variável (instância)

print(Classe1.var1)
