from vendas.calc_preco import aum_preco as ap

preco = 19.90
preco_novo = ap(preco, 4)

print(f'O valor corrigido é : {preco_novo:.2f}')
