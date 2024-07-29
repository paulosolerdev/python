#Função composta(com parâmetros)

def eleva_numero_ao_cubo(num):
    valor_a_retornar = num * num * num
    return(valor_a_retornar)

num = int(input('Informe um número que queira elevar ao cubo: '))
num = eleva_numero_ao_cubo(num)
print(num)
