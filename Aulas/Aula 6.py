class Dog(object):

    especie = 'Mamiferos'

    def __init__(self, raca):
        self.raca = raca
        self.numcaract = len(self.especie)
        pass

    def latir(self):
        print("Au au")
        pass


Katie = Dog(raca = 'Vira-Lata')
Katie.latir()

class Circulo(object):
    
    pi = 3.1415

    def __init__(self, raio = 1):
        self.raio = raio
    
    def area(self):
        return self.raio ** 2 * self.pi

    def defRaio(self, raio):
        self.raio = raio

    def obtemRaio(self):
        return self.raio

c = Circulo()

c.defRaio(input())