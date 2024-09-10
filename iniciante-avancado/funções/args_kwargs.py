# Função com parâmetros baseados em *args e **kwargs

# Supondo que está cadastrando senhas e usuários em um sistema
# def funcao(*args, **kwargs):
#     print(args)
#     print(kwargs)

# senhas_padrao = [12345, 11111, 54321]

# resultado = funcao(*senhas_padrao, usuario='user', administrador='admin')

# print(resultado)

#=======================================================#

# Buscando dados do modelo anterior

def funcao(*args, **kwargs):
    nome = kwargs['usuario']
    nome2 = kwargs['administrador']
    senha = args[0]
    senha1 = args[1]

    print(f'O usuário padrão é: {nome}')
    print(f'O administrador é: {nome2}')
    print(f'A senha padrão é: {senha}')
    print(f'A senha alternativa é: {senha1}')

senha_padrao = [12345, 11111]

funcao(*senha_padrao, usuario='user', administrador='admin')
