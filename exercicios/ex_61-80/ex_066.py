numeros = (39, 1985, 2024)
dados = {'Nome':'Paulo', 'Profissão': 'Cientista de Datos'}

def identificação(*args, **kwargs):
    print(args)
    print(kwargs)

identificação(*numeros, **dados)
