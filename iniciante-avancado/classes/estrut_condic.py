class Pessoa:
    def __init__(self, nome, login=False, logoff=False):
        self.nome = nome
        self.login = login
        self.logoff = logoff

    def logar(self):
        if self.login:
            print(f'{self.nome}, já está logado no sistema.')
            return
        
        print(f'Bem-vindo {self.nome}, você está logado no sistema.')
        self.login = True

    def deslogar(self):
        if not self.login:
            print(f'{self.nome} não está logado no sistema')
            return
        
        print(f'{self.nome} foi deslogado do sistema.')
        self.login = False

usuario = Pessoa('Soler')
usuario.logar()
usuario.logar()
usuario.deslogar()
usuario.deslogar()
