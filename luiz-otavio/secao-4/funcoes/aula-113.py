# # Exercício 1

# def multiplica(*numeros):
#     resultado = 1
#     for numero in numeros:
#         resultado *= numero

#     return resultado


# # Exemplo de uso:
# print(multiplica(2, 3, 4))
# print(multiplica(5, 10))
# print(multiplica(7))
# print(multiplica())


#=============================================#


# Exercício 2

def par_ou_impar(numero):
    if numero % 2 == 0:
        return f"O {numero} é par."
    
    return f"O {numero} é ímpar."
    

# Exemplos de uso:
print(par_ou_impar(4))
print(par_ou_impar(7))
print(par_ou_impar(8))
