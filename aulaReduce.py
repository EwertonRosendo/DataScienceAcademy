from functools import reduce
listaDeValores = [2, 3, 4, 5, 6]

def somar(a, b):
    soma = a + b
    return soma

reduce(somar, listaDeValores)

print(reduce(somar, listaDeValores))