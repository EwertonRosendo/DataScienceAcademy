import sqlite3
# Função de criar tabela sendo passado como parametro o nome do cursor
def criar_tabela(cursor):
    cursor.execute("create table pessoa(id integer primary key autoincrement not null, nome varchar(140)," \
              " trabalho varchar(40), cpf varchar(11))")
