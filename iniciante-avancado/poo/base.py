class BaseDeDados:
    def __init__(self):
        self.base = {}
    
    def inserir(self, nome, fone):
        if 'clientes' not in self.base:
            self.base['clientes'] = {nome:fone}
        else:
            self.base['clientes'].update({nome:fone})

    def listar(self):
        for nome, fone in self.base['clientes'].items():
            print(nome, fone)

    def apagar(self, nome):
        del self.base['clientes'][nome]
