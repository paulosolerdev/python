# class Pessoa:
#     nome = 'Padrão'

#     def __init__(self):
#         self.nome =  'Administrador'

# usuario1 = Pessoa()

# print(usuario1.nome)
# print(Pessoa.nome)


#==========================================#

#APROFUNDAMENTO NO TÓPICO

# Exemplo 1

# class Pessoa:
#     nome = 'Padrão' # Atributo de classe

#     def __init__(self, nome):
#         self.nome = nome # Atributo de instância

# usuario1 = Pessoa('Administrador')
# usuario2 = Pessoa('Usuário Comum')

# print(Pessoa.nome)  # Saída: Padrão (atributo de classe)
# print(usuario1.nome)    # Saída: Administrador (atributo de instância)
# print(usuario2.nome)    # Saída: Usuário Comum (atributo de instância)

#==========================================#

# Exemplo 2

# class Pessoa:
#     nome = 'Padrão' # Atributo de classe

#     def __init__(self, nome=None):
#         if nome:
#             self.nome = nome    # Atributo de instância

# usuario1 = Pessoa('Administrador')
# usuario2 = Pessoa()

# # Acessando o atributo de classe
# print(Pessoa.nome)

# # Modificando o atributo de classe
# Pessoa.nome = 'Novo Padrão'
# print(f'Atributo de classe modificado -> "{Pessoa.nome}"')

# # Instâncias
# print(usuario1.nome) # Saída: Administrador (atributo de instância, inalterado)
# print(usuario2.nome) # Saída: Novo Padrão (agora reflete o novo valor de classe)

#==========================================#
#==========================================#

# Exemplo 3

# class Pessoa:
#     nome = 'Padrão'

# class Funcionario(Pessoa):
#     def __init__(self, nome):
#         self.nome = nome # Sobrescreve o atributo de instância

# usuario1 = Funcionario('Administrador')
# usuario2 = Pessoa()

# print(usuario1.nome) # Saída: Administrador (atributo de instância)
# print(usuario2.nome) # Saída: Padrão (atributo de classe herdado)

#==========================================#
#==========================================#

# Exemplo 4

class Pessoa:
    total_pessoas = 0 # Atributo de classe

    def __init__(self, nome):
        self.nome = nome
        Pessoa.total_pessoas += 1 # Incrementa o contador a cada nova pessoa criada

usuario1 = Pessoa('Administrador')
usuario2 = Pessoa('Usuário Comum')

print(Pessoa.total_pessoas) # Saída: 2
