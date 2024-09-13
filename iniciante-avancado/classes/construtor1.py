# Criando uma classe com método construtor e objetos internos

class Pessoa:
    def __init__(self, nome, idade, sexo, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura

pessoa1 = Pessoa('Paulo', 39, 'M', 1.83)

print(pessoa1.nome, pessoa1.idade)
print(f'Bem-vindo {pessoa1.nome}, parabéns pelos seus {pessoa1.idade} anos.')
