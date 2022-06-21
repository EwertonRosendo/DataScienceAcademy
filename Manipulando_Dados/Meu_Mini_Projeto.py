import sqlite3
import modulos.funções
conn = sqlite3.connect("projeto.db")
c = conn.cursor()
while True:
    print(f"[1] - Criar tabela")
    print(f"[2] - Pesquisar na tabela")
    print(f"[3] - Deletar na tabela")
    print(f"[4] - Alterar na tabela")
    duvida = int(input("Informe qual ação deseja realizar: \n"))

    if duvida == 1:
        modulos.funções.criar_tabela(c)
    break


c.close()
conn.close()