def negativar(valor):
    return True if valor < 0 else False


print(list(filter(negativar, range(-5, 5))))
