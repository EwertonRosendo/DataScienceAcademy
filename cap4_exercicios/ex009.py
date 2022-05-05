dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 4, 'd': 5}

def trocar(d1, d2):
    dicTemp = {}
    for key, val in zip(d1, d2.values()):
        dicTemp[key] = val

    return dicTemp

dict3 = trocar(dict1, dict2)
print(dict3)
