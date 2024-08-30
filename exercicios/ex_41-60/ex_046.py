d = {'Alto nível':'Python',
     'Médio Nível':'C',
     'Baixo Nível':'Assembly'}

for i in d.values():
    if not i == 'Python':
        print(f'Python não consta na lista.')
    else:
        print(f'Python consta na lista.')
        break
