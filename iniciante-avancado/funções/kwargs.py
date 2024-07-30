def informacoes(**kwargs):
    for dado, valor in kwargs.items():
        print(f'{dado}:{str(valor)}')

pessoa = informacoes(nome='Paulo',
                     idade=39,
                     nacionalidade='Brasileiro')

print(pessoa)
