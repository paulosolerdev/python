class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
        ano_nasc = self.ano_atual - self.idade
        print(f'Seu ano de nascimento é {ano_nasc}')

pessoa1 = Pessoa('Paulo Soler', 39)
print(pessoa1.ano_nascimento())
