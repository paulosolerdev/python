# Definindo parâmetros padrão como False

class Pessoa:
    def __init__(self, nome, idade, sexo=False, altura=False):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura

pessoa1 = Pessoa('Susana', 40, 'F', 1.72)
print(pessoa1.nome)
print(pessoa1.altura)

pessoa2 = Pessoa('Paulo', 39, 'M', 1.83)
print(pessoa2.nome)
print(pessoa2.idade)
