class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def boas_vindas(self):
        print(f'Usuário: {self.nome}, Idade: {self.idade}')

usuario1 = Usuario(nome='Paulo', idade=39)
usuario1.boas_vindas()

print(usuario1.nome)
