class Biblioteca:
    def __init__(self, livro1, **kwargs):
        self.livro1 = livro1

prateleira1 = Biblioteca('LIVRO TESTE')
prateleira1.livro2 = '1984 - George Orwell'
prateleira1.livro3 = 'Duna - Frank Herbert'
prateleira1.livro4 = 'O Iluminado - Stephen King'
prateleira1.livro5 = 'O Exorcista - William Peter Blatty'
prateleira1.livro6 = 'O Hobbit - J. R. R. Tolkien'

print(prateleira1.livro4)
print(prateleira1.livro1)
print(prateleira1.livro2)
print(prateleira1.livro3)
