listaDeValores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def verificarPar(x):
    return True if x%2 == 0 else False

print(list(filter(verificarPar, listaDeValores)))
