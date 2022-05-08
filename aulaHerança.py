#  Criando a super classe animal

class Animal():


    def __init__(self):
        print(f"Animal criado!")

    def identify(self):
        print(f"Animal!")

    def comer(self):
        print(f"Comendo!")

#  Criando a subclasse

class Cachorro(Animal):

    def __init__(self):
        Animal.__init__(self)
        print(f"Cachorro criado")

    def identify(self):
        print("Cachorro")

    def latir(self):
        print("Latindo!")

niko = Cachorro()

print(niko.comer())