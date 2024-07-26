# Adicionando ítens à lista
lista = [1, 5, 'Maria', 'João']
print(lista)

lista.append(4)
print(f'{lista}')


#==========$$==========#===$$$===#==========$$==========#
#==========$$==========#===$$$===#==========$$==========#


# Removendo ítens da lista
lista.remove('Maria')
print(lista)


#==========$$==========#===$$$===#==========$$==========#
#==========$$==========#===$$$===#==========$$==========#


# Removendo dados via índice
lista = ['Ana', 'Carlos', 'João', 'Sônia']
print(f'{lista}')

del lista[2]
print(f'{lista}')


#==========$$==========#===$$$===#==========$$==========#
#==========$$==========#===$$$===#==========$$==========#


# Verificando a posição de um elemento
lista = [1, 5, 'Maria', 'João']
print(f'{lista}')

lista.append(4)
print(lista.index('Maria'))
print(f'{lista.index("Maria")}')


#==========$$==========#===$$$===#==========$$==========#
#==========$$==========#===$$$===#==========$$==========#


# Verificando se um elemento consta na lista
lista = [1, 5, 'Maria', 'João']
lista.append(4)
print(f'{"João" in lista}')
