class Contato:
    def __init__(self, residencial, celular):
        self.residencial = residencial
        self.celular = celular

class Cliente:
    def __init__(self, nome, idade, fone=None):
        self.nome = nome
        self.idade = idade
        self.fone = []

    def addFone(self, residencial, celular):
        self.fone.append(Contato(residencial, celular))
    def listaFone(self):
        for fone in self.fone:
            print(fone.residencial, fone.celular)

cliente1 = Cliente('Paulo', 39)
cliente1.addFone(33325644, 999999999)
print(cliente1.nome)
print(cliente1.listaFone())
