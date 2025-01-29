# dias = int(input('Digite o número de dias: '))
# horas = int(input('Digite o número de horas: '))
# minutos = int(input('Digite o número de minutos: '))
# segundos = int(input('Digite o número de segundos: '))

# total_em_segundos = segundos + (minutos*60) + (horas*60*60) + (dias*24*60*60)
# print(total_em_segundos)


# c = float(input('Digite a temperatura em Celsius: '))

# f = ((9 * c) / 5 + 32)

# print(f'A temperatura em F é: {f}')


minutos = int(input('Quantos minutos você utilizou este mês?: '))

if minutos < 200:
    preco = 0.20
elif minutos < 400:
        preco = 0.18
else:
        preco = 0.15
    
print(f'Você vai pagar R${minutos*preco:6.2f} este mês.')
