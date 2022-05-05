def quadrado(valor):
    return valor**2

def cubo(valor):
    return valor**3

lista = [0, 1, 2, 3, 4]
resultado = [[f"{x}^2={quadrado(x)} e {x}^3={cubo(x)}"] for x in lista]
print(resultado)


print(f"A lista ao quadrado é igual a {list(map(quadrado, lista))} e ao cubo é igual a {list(map(cubo, lista))}")
