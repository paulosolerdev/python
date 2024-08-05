# Estrutura de Repetição

# WHILE

# variavel = 0

# while variavel <= 5:
#     print(variavel)
#     variavel +=1

#============================================#

# num = 0
# total = 10

# while num <= 10:
#     print(num)
#     num += 1

#     if num == 6:
#         print(f'50% computado')
#     if num == total+1:
#         print(f'100%, processo encerrado')
    
#============================================#

while True:
    validador = input('Digite "Brasil" para continuar: ')

    if validador == 'Brasil':
        print('Você digitou Brasil corretamente!')
        break
    else:
        print('Palavra-chave não confere, digite novamente: ')
