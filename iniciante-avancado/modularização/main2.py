from medicos import medicos

menu = str(input('Deseja agendar uma consulta? (S ou N)')).upper()

if menu == 'S':
    paciente = input('Por favor, digite seu nome completo: ')
    print(f'{paciente}, escolha com qual médico deseja consultar: ')

    print('1 - Grazielle Veiga')
    print('2 - Matheus Correa')

    print('3 - José Alvarenga')
    print('4 - Natália Caprini')
    print('5 - Alberto Lins')

    medico = int(input('Com qual médico deseja agendar consulta? '))

    if medico == 1:
        print(f'{paciente}, Sua consulta com a Dr.a {medicos[0]} será agendada.')
    if medico == 2:
        print(f'{paciente}, Sua consulta com o Dr. {medicos[1]} será agendada.')
    if medico == 3:
        print(f'{paciente}, Sua consulta com o Dr. {medicos[2]} será agendada.')
    if medico == 4:
        print(f'{paciente}, Sua consulta com o Dr. {medicos[3]} será agendada.')
    if medico == 5:
        print(f'{paciente}, Sua consulta com o Dr. {medicos[4]} será agendada.')
    else:
        print(f'Agradecemos o seu contato!')
