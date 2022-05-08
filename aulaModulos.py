class Circulo():

    pi = 3.14

    def __init__(self, raio=4):
        self.raio = raio

    def area(self):
        return (self.raio*self.raio) * Circulo.pi

    def setRaio(self, novo_raio):
        self.raio = novo_raio

    def getRaio(self):
        return self.raio

circ = Circulo()
#  Raio antigo
print(f"O raio é: {circ.getRaio()}")
#  Alterando o raio
circ.setRaio(5)
#  Area com o novo raio
print(f"A area é: {circ.area()}")
