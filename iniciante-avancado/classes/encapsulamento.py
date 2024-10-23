class BaseDeDados:
    def __init__(self):
        self.__base = {}
    
    def inserir(self, nome, fone):
        if 'clientes' not in self.__base:
            self.__base['clientes'] = {nome:fone}
        else:
            self.__base['clientes'].update({nome:fone})

    def listar(self):
        for nome, fone in self.__base['clientes'].items():
            print(nome, fone)

    def apagar(self, nome):
        del self.__base['clientes'][nome]

relClientes = BaseDeDados()

relClientes.inserir('Ana', 991358899)
relClientes.inserir('Fernando', 981252001)
relClientes.inserir('Maria', 999111415)

relClientes.listar()
relClientes.__base = 'Novo Banco de Dados'
print(relClientes.__base)
print(relClientes._BaseDeDados__base)
