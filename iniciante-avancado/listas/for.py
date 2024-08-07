# Laço de repetição for

repetir = 's'
fatura = []
total = 0

while repetir == 's':
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço: '))

    fatura.append([produto, preco])
    total += preco

    repetir = input('Cadastrar mais algum item? (S ou N): ').lower()

for i in fatura:
    print(i[0], ':', i[1])

print(f'O total da fatura é : {total:.2f}')
