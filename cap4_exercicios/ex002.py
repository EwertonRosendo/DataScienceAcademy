"""frase = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'

def tratamento(txt):
    for palavra in txt.split():
        print(f"{palavra.upper()},{palavra.lower()},{len(palavra)} ")
#print(frase)

#print(list(map(tratamento, frase)))

resultado = [(map(tratamento, frase)) for palavra in frase.split()]


tratamento(frase)"""

frase = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
resultado = [["{}, {}, {}".format(palavra.upper(), palavra.lower(), len(palavra))] for palavra in frase]

for r in resultado:
    print(r)