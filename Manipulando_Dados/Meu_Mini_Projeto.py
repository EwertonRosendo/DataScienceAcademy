import sqlite3
import modulos.funções
conn = sqlite3.connect("projeto.db")
c = conn.cursor()
while True:
    print(f"[1] - Criar tabela")
    print(f"[2] - Pesquisar na tabela")
    print(f"[3] - Deletar na tabela")
    print(f"[4] - Alterar na tabela")
    print(f"[5] - Sair")
    duvida = int(input("Informe qual ação deseja realizar: \n"))
    # A opção [1] serve para criar a tabela Pessoa que possui id, nome, trabalho e cpf
    if duvida == 1:
        modulos.funções.criar_tabela(c)

    # A opção [2] serve para buscar algum dado na tabela
    elif duvida == 2:
        print()

    # A opção [3] serve para deletar algum dado da tabela
    elif duvida == 3:
        print()

    # A opção [4] serve para alterar algum dado na tabela
    elif duvida == 4:
        print()

    # A opção [5] serve para finalizar o teste
    elif duvida == 5:
        break


c.close()
conn.close()