# Classe Abstrata

from abc  import ABC, abstractclassmethod

class Pessoa(ABC):
    @abstractclassmethod
    def logar(self):
        pass


class Usuario(Pessoa):
    def logar(self):
        print(f'Usuário logado no sistema.')


user1 = Usuario()
user1.logar()
