# Métodos que até interagem com funções internas,
# mas retorna dados para o escopo global da classe.

class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def ano_nasc(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    

pessoa2 = Pessoa.ano_nasc('Paulo', 1985)

print(pessoa2.idade)
