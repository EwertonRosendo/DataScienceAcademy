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