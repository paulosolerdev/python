fixo = 500.00
vendas = float(input('Digite o valor de vendas: '))
comissao = vendas * 6 / 100
faturamento = fixo + comissao

print(f'O faturamento do mês é: {faturamento}')
