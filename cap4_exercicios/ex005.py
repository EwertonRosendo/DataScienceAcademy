from functools import reduce

listaA = [2, 3, 4]
listaB = [10, 11, 12]

def juntar(lista1, lista2):
    listaJuntas = list(zip(lista1, lista2))
    resultado = [[x[0]**x[1]] for x in listaJuntas]
    return f"A lista é {resultado}"


print(juntar(listaA, listaB))