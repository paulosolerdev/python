# Encapsulamento

class BaseDeDados:
    def __init__(self):
        #self.dados = {}
        self._dados = {}
        # declarado como protegido (ainda acessível de fora da classe)

        #self.__dados = {}
        # declarado como privado (inacessível e imutável de fora da classe)


base = BaseDeDados()

print(base._dados)

#base.dados = {'chave':'valor'}

#print(base.dados)
