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

print(fatura) # Exibindo a lista com as informações obtidas

for i in fatura: # Transformando a lista de listas em uma tabela para exibir e o valor total.
    print(i[0], ':', i[1]) # Exibe com aparâncie de um dicionário

print(f'O total da fatura é : {total:.2f}')
