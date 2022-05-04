"""texto = "Cientista de Dados é a profissão que mais tem crescido em
texto += "Esses profissionais precisam se especializar em Programação, Estatística e Machine Learning."
texto += "E claro, em Big Data."

import os

arquivo = open(os.path.join("arquivos/cientistas.txt"),"w")

for palavra in texto.split():
    arquivo.write(palavra+" ")
arquivo.close()

naosei = open("arquivos/cientistas.txt")
conteudo = naosei.read()
naosei.close()
print(conteudo)
"""
import os
arq = open(os.path.join("arquivos/testanto2.txt"), "w")

texto = "aprendendo a manipuilar arquivos de texto no Python3"
for palavra in texto.split():
    arq.write(palavra+" ")
arq.close()

arq = open("arquivos/testanto2.txt")
conteudo = arq.read()
arq.close()
print(conteudo)
