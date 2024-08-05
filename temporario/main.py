class Calculadora:

    def __init__(self, n1=10, n2=10):
        self.n1 = n1
        self.n2 = n2

    def somar(self, n1, n2):
        return n1+n2
    def subtrair(self, n1, n2):
        return n1-n2
    def multiplicar(self, n1, n2):
        return n1*n2
    def dividir(self, n1, n2):
        return n1/n2

pessoa1 = Calculadora()
print(f"Valores default: {pessoa1.somar(pessoa1.n1,pessoa1.n2)}")

pessoa2 = Calculadora(50,2)
print(f"Valores passados: {pessoa2.somar(pessoa2.n1, pessoa2.n2)}")