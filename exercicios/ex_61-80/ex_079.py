def mostra_msg_maior(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        print(f'{s1} é a string de maior tamanho.')
    elif len2 > len1:
        print(f'{s2} é a string de maior tamanho.')
    else:
        print(f'{s1} e {s2} são strings de mesmo tamanho.')
        print(s1)
        print(s2)

mostra_msg_maior('Paulo', 'Python')
