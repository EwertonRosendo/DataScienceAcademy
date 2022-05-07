class Livro():

    def __init__(self):
        self.titulo = "O monge e o executivo"
        self.isbn = 9988888
        print("Contrustor chamado para criar um objeto desta classe!")


    def imprime(self):
        print(f"foi criado um livro {self.titulo} e um ISBN de {self.isbn}")


Livro1 = Livro()

print(Livro1.isbn)
