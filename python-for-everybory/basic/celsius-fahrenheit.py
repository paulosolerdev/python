# Fórmula

# F = (C * 9/5) + 32

# c = float(input('Digite a temperatura em Celsius: '))

# f = (c * 9/5) + 32

# print(f'{c} graus Celsius equivale a {f} graus fahrenheit.')


#=====================================#


inp = input('Enter Fahrenheit Temperature: ')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')
