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

relClientes = BaseDeDados()

relClientes.inserir('Ana', 991358899)
relClientes.inserir('Fernando', 981252001)
relClientes.inserir('Maria', 999111415)

relClientes.listar()
