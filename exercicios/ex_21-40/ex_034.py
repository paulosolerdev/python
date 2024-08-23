contador = 0
soma = 0

for i in range(1, 101):
    if i%3==0:
        soma += i
        contador += 1

print(f'Foram encontrados {contador} números ímpares.')
print(f'A soma destes números é: {soma}')
