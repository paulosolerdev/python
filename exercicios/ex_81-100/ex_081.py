def num_por_extenso(n):
    if n == 0:
        return 'zero'
    
    unidades = ('', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
    dezenas = ('', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')
    especiais = ('dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')

    if n == 100:
        return 'cem'
    elif 10 <= n <= 19:
        return especiais[n - 10]
    elif n >= 20:
        dezena = dezenas[n // 10]
        unidade = unidades[n % 10]
        return f"{dezena} e {unidade}".strip(" e ")
    else:
        return unidades[n]

num = int(input('Digite um número entre 0 e 100: '))

if 0 <= num <= 100:
    print(f'{num} por extenso é: {num_por_extenso(num)}')
else:
    print('Número fora do intervalo.')
