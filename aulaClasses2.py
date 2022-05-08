class Cachorro():
    def __init__(self, raca):

        self.raca = raca
        print(f"Construtor chamado para criar um objeto dessa clase")
        print(f" Raça: {raca} ")

Niko = Cachorro("Maltes")

print(f"Raça: {Niko.raca} ")
