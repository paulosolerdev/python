medicos = ['Grazielle Veiga',
           'Matheus Correa']

usuarios = {'001':'Paulo Soler',
            '002':'Susana Mottes'}

usuario = str(input('Digite seu número de usuário: '))
if usuario in usuarios.keys():
    usuario_nome = usuarios[usuario] # Acessa o nome direto do dicionário
    print(f'Bem-vindo(a) {usuario_nome}')

    # Pergunta se deseja agendar uma consulta
    menu = input('Deseja agendar uma consulta? (S ou N): ').upper()
    if menu == 'S':
        print(f'{usuario_nome}, escolha com qual médico deseja consultar: ')
        print('1 - Grazielle Veiga')
        print('2 - Matheus Correa')

        # Solicita a escolha do médico
        medico = int(input('Com qual médico deseja agendar consulta?: '))
        if medico == 1:
            print(f'{usuario_nome}, sua consulta com a Drª. {medicos[0]} está agendada.')
        elif medico == 2:
            print(f'{usuario_nome}, sua consulta com a Dr. {medicos[1]} está agendada.')
        else:
            print('Opção de médico inválida.')
    else:
        print('Agradecemos o seu contato!')
else:
    print('Usuário desconhecido ou não cadastrado.')
