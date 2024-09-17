# Try, Except


# try:
#     print(variavel)
# except:
#     pass



# try:
#     print(var)
# except:
#     print('A variável não existe!')


# Exibindo que erro aconteceu

try:
    print(a)

# except NameError as erro:
#     print(f'Ocorreu um erro: {erro}')
    
# except genérico:
except Exception as erro:
    print(f'Ocorreu um erro inesperado: {erro}')
