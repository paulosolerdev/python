import vendas.calc_preco

preco = 19.90
preco_novo = vendas.calc_preco.aum_preco(preco, 4)

print(f'O valor corrigido é : {preco_novo}')
