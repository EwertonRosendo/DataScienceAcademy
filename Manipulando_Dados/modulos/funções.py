import sqlite3
# Função de criar tabela sendo passado como parametro o nome do cursor
def criar_tabela(cursor):
    try:
        cursor.execute("create table pessoa(id integer primary key autoincrement not null, nome varchar(140)," \
                  " trabalho varchar(40), cpf varchar(11))")
    except Exception as causa:
        print(f"Detectamos uma falha e não conseguimos realizar a operação! causa: {causa.__class__}")

    else:
        print("Tabela criada com sucesso")

    #finally:
        #print()


def deletar_linha(conexao, cursor, cpf):
    cursor.execute("delete from pessoa where cpf = {}".format(cpf))
    conexao.commit()


def inserir_dados(conexao, cursor):
    while True:
        nome = str(input("Informe o nome: ")).strip().upper()
        trabalho = str(input("Informe o seu trabalho")).strip().upper()
        cpf = str(input("Informe o cpf")).strip()

        if nome.isnumeric() or trabalho.isnumeric() or cpf.isalpha():
            print("Algum ou alguns dados foram inseridos incorretamente, tente novamente!")
        else:
            print("Dados inseridos corretamente")
            break

    cursor.execute("insert into pessoa (nome, trabalho, cpf) values(?, ?, ?)", (nome, trabalho, cpf))
    conexao.commit()
