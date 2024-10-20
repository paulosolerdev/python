class Calculadora:

    def soma(self, n1, n2):
        return n1 + n2
    
    def subtracao(self, n1, n2):
        return n1 - n2
    
    def multiplicacao(self, n1, n2):
        return n1 * n2
    
    def divisao(self, n1, n2):
        return n1 / n2
    
n1 = Calculadora()

print(n1.multiplicacao(5, 4))
print(n1.divisao(20,  5))
