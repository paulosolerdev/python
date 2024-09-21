class Pessoa:
    administrador = 'Admin'

    def __init__(self, nome):
        self.nome = nome

        self.msg = 'Classe Pessoa em execução.'
        print(self.msg)

    def metodo1(self):
        print(self.msg)
        pass

var1 = Pessoa('Paulo')
var1.metodo1()
