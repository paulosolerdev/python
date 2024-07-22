class Cor:
    vermelho = 1
    verde = 2
    azul = 3
    branco = 4
    preto = 5

# Mude a cor para testar
cor_atual = 2

if cor_atual == Cor.vermelho:
    print('Vermelho')
elif cor_atual == Cor.verde:
    print('Verde')
elif cor_atual == Cor.azul:
    print('Azul')
elif cor_atual == Cor.branco:
    print('Branco')
elif cor_atual == Cor.preto:
    print('Preto')
else:
    print('Desconhecido')
