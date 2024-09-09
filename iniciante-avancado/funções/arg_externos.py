# Função com argumentos externos

def funcao(*args):
    for parametro in args:
        print(parametro)

argumentos = ('nome', 'idade')

print(funcao(*argumentos))
