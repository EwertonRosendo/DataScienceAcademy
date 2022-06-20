import os
import sqlite3
import datetime
import random

# Verificando se o arquivo já existe
import time

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



create_table()
data_insert()


def data_insert_var():
    new_date = datetime.datetime.now()
    new_prod_name = "Monitor"
    new_valor = random.randrange(200, 800)
    c.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (?, ?, ?)", (new_date, new_prod_name, new_valor))
    conn.commit()


for i in range(10):
    data_insert_var()
    time.sleep(1)

c.close()
conn.close()
