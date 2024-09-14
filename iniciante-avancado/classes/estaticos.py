# Métodos estáticos

# Aqueles que não possuel instâncias como atributos,
# funciona como uma função normal dentro da classe.

from random import randint


class Pessoa:
    @staticmethod
    def gerador_id():
        gerador = randint(100, 999)
        return gerador
    

print(Pessoa.gerador_id())
