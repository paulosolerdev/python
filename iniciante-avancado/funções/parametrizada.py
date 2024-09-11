# Função que recebe outra função como parâmetro

def mestre(funcao):
    return funcao()

def msg_boas_vindas():
    return 'Seja muito bem-vindo!'

executa = mestre(msg_boas_vindas)

print(executa)
