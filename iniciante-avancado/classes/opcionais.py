class Pessoa:
    def __init__(self, nome, idade, sexo=False, altura=False):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura
    
pessoa1 = Pessoa('Paulo', 39, 'M', 1.83)
pessoa2 = Pessoa('Susana', 40)

print(pessoa1.nome, pessoa1.altura)
print(pessoa2.nome, pessoa2.idade)
