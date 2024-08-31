aluno = [{'Nome':'Paulo','Notas':[62, 73, 90]}]

def calcula_media(aluno):
    notas = []

    for media in aluno:
        if len(media['Notas']) > 0:
            temp = round(sum(media['Notas']) / len(media['Notas']))
        else:
            temp = 0
        notas.append({'Nome':media['Nome'], 'Média das notas':temp})
    return notas

media_estudante = calcula_media(aluno)
print(media_estudante)
