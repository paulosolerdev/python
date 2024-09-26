# Arquivo medicos.py
medicos = ['Grazielle Veiga',
           'Matheus Correa',
           'José Alvarenga',
           'Natália Caprini',
           'Alberto Lins']

# Arquivo main.py
menu = str(input('Deseja agendar uma consulta? (S ou N)')).upper()

if menu == 'S':
    paciente = input('Por favor, digite seu nome completo: ')
    print(f'{paciente}, escolha com qual médico deseja consultar: ')

    print('1 - Grazielle Veiga')
    print('2 - Matheus Correa')

    medico = int(input('Com qual médico deseja agendar consulta?'))

    if medico == 1:
        print(f'Sua consulta com a Dr.a {medicos[0]} será agendada.')
    if medico == 2:
        print(f'Sua consulta com o Dr. {medicos[1]} será agendada.')
    else:
        print(f'Agradecemos o seu contato!')
