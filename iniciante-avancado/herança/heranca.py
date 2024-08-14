class Carros():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def descricao(self):
        print(f'O carro: {self.nome} é {self.cor}')

class Gol(Carros):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class Corsa(Carros):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

gol = Gol('Gol 2019 Completo', 'branco')
corsa = Corsa('Corsa 2017 2 Portas', 'vermelho')

print(gol.descricao())
print(corsa.descricao())
