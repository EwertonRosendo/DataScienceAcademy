matrix = [[1, 2],[3,4],[5,6],[7,8]]
"""for i in matrix:
    print(i)

matris_Trasp = [[l1[0] for l1 in matrix], [l2[1] for l2 in matrix] ]
print(matris_Trasp)
"""

# Uma matriz transposta é quando tornamos as linhas de uma matriz em coluna, mas para min, pelo menos, tive dificuldade
# em conceber dessa forma. Por isso penso que uma matriz transposta é quando tornamos as colunas em linhas
resultado = [[linha[0] for linha in matrix], [linha[1] for linha in matrix]]
print(resultado)
