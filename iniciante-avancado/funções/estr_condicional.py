# Estruturas condicionais dentro de funções

def repetidor(msg):
    contador = 0
    while contador < 5:
        print(msg)
        contador += 1

print(repetidor(msg=input('Digite algo para ser repetido 5 vezes: ')))
