# string = '123456789012345678905918273645'

# # print(string[0:10])
# # print(string[10:20])
# # print(string[20:30])

# n = 10
# comp = [i for i in range(0, len(string), n)]

# print(comp)


# comp2 = [(i, i+n) for i in range(0, len(string), n)]
# print(comp2)


# comp3 = [string[i:i + n] for i in range(0, len(string), n)]
# print(comp3)


# lista = [string[i:i + n] for i in range(0, len(string), n)]
# retorno = '.'.join(lista)

# print(retorno)


carrinho = []
carrinho.append(('Item 1', 30))
carrinho.append(('Item 2', 45))
carrinho.append(('Item 3', 22))
total = 0

for produto in carrinho:
    total = total + produto[1]

print('Método tradicional', total)

total2 = []
for produto in carrinho:
    total2.append(produto[1])
print('Usando funções internas', sum(total2))


total = sum(produto[1] for produto in carrinho)
print('Usando expressão geradora', total)
