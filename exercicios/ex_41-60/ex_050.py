base = {
    'Pergunta 01':{
        'pergunta':'Quanto é 4x4?',
        'alternativas':{'a':'12', 'b':'24', 'c':'16', 'd':'20'},
        'resposta_certa':'c',
    },
    'Pergunta 02':{
        'pergunta':'Quanto é 6/3?',
        'alternativas':{'a':'2', 'b':'1', 'c':'3', 'd':'4'},
        'resposta_certa':'a',
    },
}

respostas_certas = 0

for pkeys, pvalues in base.items():
    print(f'{pkeys}:{pvalues["pergunta"]}')

    for rkeys, rvalues in pvalues['alternativas'].items():
        print(f'[{rkeys}]:{rvalues}')

    resposta = input('Escolha uma alternativa: [a], [b], [c], ou [d]: ')

    if resposta == pvalues['resposta_certa']:
        print('Resposta Correta!')
        respostas_certas += 1
    else:
        print('Resposta Incorreta!')
if respostas_certas == 0:
    print('Você não acertou nenhuma questão.')
elif respostas_certas == 1:
    print('Você acertou apeans uma questão.')
else:
    print('Você acertou todas as questões.')
