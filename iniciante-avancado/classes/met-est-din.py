# Método Dinâmico

# class Pessoa:
#     ano_atual = 2024

#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     @classmethod
#     def ano_nascimento(cls, nome, ano_nascimento):
#         idade = cls.ano_atual - ano_nascimento
#         return cls(nome, idade)

# pessoa2 = Pessoa.ano_nascimento('Paulo', 1985)
# print(pessoa2.idade)


#=====================================================#


# Método Estático

from random import randint

class Pessoa:
    @staticmethod
    def gerador_id():
        gerador = randint(100, 999)
        return gerador
    
print(Pessoa.gerador_id())
