"""
A forma com que eu fiz

elementos = [1, 2, 4]
def potencia(valor):
    return valor**3

print(list(map(potencia, elementos)))
"""

# Forma da DSA
elementos = [3, 4, 5]
resultado = [valor**3 for valor in elementos]
print(resultado)
