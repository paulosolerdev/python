class Carro:
    ano = 2024
    cor = 'prata'
    modelo = 'hatch'
    opcionais = 'nenhum'

carro1 = Carro()

carro2 = Carro()
carro2.ano = 2020
carro2.cor = 'preto'
carro2.modelo = 'sedan'


print(f'Carro nº1: Ano = {carro1.ano}, Cor = {carro1.cor}, Modelo = {carro1.modelo}, Opcionais = {carro1.opcionais}')

print(f'Carro nº2: Ano = {carro2.ano}, Cor = {carro2.cor}, Modelo = {carro2.modelo}, Opcionais = {carro2.opcionais}')
