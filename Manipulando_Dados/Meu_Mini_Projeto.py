import sqlite3
import modulos.funções
import time
conn = sqlite3.connect("projeto.db")
c = conn.cursor()
while True:
    print(f"[1] - Criar tabela")
    print(f"[2] - Inserir dados na tabela")
    print(f"[3] - Pesquisar na tabela")
    print(f"[4] - Deletar na tabela")
    print(f"[5] - Alterar na tabela")
    print(f"[6] - Sair")
    duvida = int(input("Informe qual ação deseja realizar: \n"))
    # A opção [1] serve para criar a tabela Pessoa que possui id, nome, trabalho e cpf
    if duvida == 1:
        modulos.funções.criar_tabela(c)


    # A opção [2] serve para adicionar dados na tabela
    if duvida == 2:
        modulos.funções.inserir_dados(conn, c)


    # A opção [3] serve para buscar algum dado na tabela
    elif duvida == 3:
        print()

    # A opção [4] serve para deletar algum dado da tabela
    elif duvida == 4:
        while True:
            try:
                cpf = str(input("Informe o cpf da pessoa que deseja deletar: "))
                modulos.funções.deletar_linha(conn, c, cpf)
            except Exception as causa:
                print(f"Problema detectado, tente novamente - {causa.__class__}")
            else:
                for c in range(0, 3):
                    print("Pesquisando..{}".format(c*"."))
                    time.sleep(1)
            break

    # A opção [5] serve para alterar algum dado na tabela
    elif duvida == 5:
        print()

    # A opção [6] serve para finalizar o teste
    elif duvida == 6:
        break

    else:
        print("Opção não detectada, informe um valor valido!")


c.close()
conn.close()