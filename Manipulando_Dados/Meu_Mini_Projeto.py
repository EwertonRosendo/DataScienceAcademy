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
    # A opção [1] serve para CRIAR a tabela Pessoa que possui id, nome, trabalho e cpf
    if duvida == 1:
        # Cria a tabela pessoa
        modulos.funções.criar_tabela(c)

    # A opção [2] serve para ADICIONAR dados na tabela
    if duvida == 2:
        # Insere valores novos na tabela
        modulos.funções.inserir_dados(conn, c)


    # A opção [3] serve para PESQUISAR algum dado na tabela
    elif duvida == 3:
        # Chama a função de pesquisar dados
        modulos.funções.pesquisar_dados(c)


    # A opção [4] serve para DELETAR algum dado da tabela
    elif duvida == 4:
        # confesso que eu me perdi na organização disso aqui, MAS TA RODANDO
        c.execute("select * from pessoa")
        qtd_antigo = len(c.fetchall())

        while True:
            try:
                cpf = str(input("Informe o cpf da pessoa que deseja deletar: "))
                modulos.funções.deletar_linha(conn, c, cpf)
            except Exception as causa:
                print(f"Problema detectado, tente novamente - {causa.__class__}")
            else:
                for cont in range(0, 3):
                    print("Pesquisando..{}".format(cont*"."))
                    time.sleep(1)
            finally:
                c.execute("select * from pessoa")
                qtd_novo = len(c.fetchall())

                if qtd_novo == (qtd_antigo - 1):
                    print(f"O cadastro foi removido com sucesso!")
                    break
                else:
                    print("Não foi possivel localizar o usuario")

    # A opção [5] serve para ALTERAR algum dado na tabela
    elif duvida == 5:
        #chamando função de alterar dados
        modulos.funções.alterar_dados(conn, c)

    # A opção [6] serve para FINALIZAR o teste
    elif duvida == 6:
        # Fim da execução do programa
        break

    else:
        print("Opção não detectada, informe um valor valido!")


c.close()
conn.close()