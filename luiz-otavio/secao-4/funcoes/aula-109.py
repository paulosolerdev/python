x = 1


def escopo():
    #global x Má prática de programação
    x = 10

    def outra_funcao():
        #global x Má prática de programação
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)
