class Pessoa:
    def __init__(self, nome, login=False, logoff=False):
        self.nome = nome
        self.login = login
        self.logoff = logoff

    def logar(self):
        print(f'Bem-vindo {self.nome}, você está logado no sistema.')
        self.login = True

usuario = Pessoa('Paulo')
usuario.logar()
