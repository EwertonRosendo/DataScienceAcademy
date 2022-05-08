class Pessoa():

    def __init__(self, nome=str, cpf=str, dataNascimento=str):
        self.nome = nome
        self.cpf = cpf
        self.dataNascimento = dataNascimento
        print("Pessoa criada")

    def getNascimento(self):
        return self.dataNascimento

    def getNome(self):
        return self.nome

    def getCpf(self):
        return self.cpf


class Individuo(Pessoa):

    def __init__(self):
        Pessoa.__init__(self)
        self.nome = input("Informe o nome do individuo: ").upper().strip()
        self.cpf = input("Informe o cpf: ")
        self.dataNascimento = input("Informe sua data de nascimento: ")
        print("Individuo criado")

rosendo = Individuo()


#print(f"Nome: {rosendo.getNome()}\nNascimento: {rosendo.getNascimento()}\nCpf: {rosendo.getCpf()}")
print(rosendo)