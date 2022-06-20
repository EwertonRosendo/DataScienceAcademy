import os
import sqlite3

# Verificando se o arquivo já existe
os.remove("dsa.db") if os.path.exists("dsa.db") else None

# criando uma conexão com o arquivo
conn = sqlite3.connect("dsa.db")

# criando um cursor para usar no bd
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, "\
              "prod_name TEXT, valor REAL)")

def data_insert():
    c.execute("INSERT INTO produtos VALUES(10, '2018-05-02 14:32:11', 'Teclado', 90 )")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_insert()