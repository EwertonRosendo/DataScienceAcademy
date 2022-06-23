import os
import sqlite3
import datetime
import random
import matplotlib.pyplot as plt

# Verificando se o arquivo já existe
import time

os.remove("dsa.db") if os.path.exists("dsa.db") else None

# criando uma conexão com o arquivo
conn = sqlite3.connect("dsa.db")

# criando um cursor para usar no bd
c = conn.cursor()

# criando a tabela de produtos, mas só se ela não existir
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, "\
              "prod_name TEXT, valor REAL)")

# inserindo dados na tabela
def data_insert():
    c.execute("INSERT INTO produtos VALUES(10, '2018-05-02 14:32:11', 'Teclado', 90 )")
    conn.commit()


# Chamando as funções
create_table()

data_insert()


# Criando uma função para inserir dados no bd
def data_insert_var():
    new_date = datetime.datetime.now()
    new_prod_name = "Monitor"
    new_valor = random.randrange(200, 800)
    c.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (?, ?, ?)", (new_date, new_prod_name, new_valor))
    conn.commit()

#chamando a função de inserir dados num laço de repetção for
for i in range(10):
    data_insert_var()

def leitura_todos_dados():
    c.execute("select * from produtos")
    for linha in c.fetchall():
        print(f"{linha}")
        time.sleep(0.2)

def leitura_registros():
    c.execute("select * from produtos where valor > 500.0")
    for linha in c.fetchall():
        print(linha)
        time.sleep(0.2)

def leitura_colunas():
    c.execute("select * from produtos")
    for linha in c.fetchall():
        print(linha[3])


def atualiza_dados():
    c.execute("update produtos set valor = 70.0 where valor = 199")
    conn.commit()

def remove_dados():
    c.execute("delete from produtos where valor < 200.0")
    conn.commit()



print("-----------------TODOS OS DADOS-----------------")
leitura_todos_dados()


def dados_grafico():
    c.execute("select id, valor from produtos")
    ids = []
    valores = []
    dados = c.fetchall()
    for linha in dados:
        ids.append(linha[0])
        valores.append(linha[1])

    plt.bar(ids, valores)
    plt.show()


dados_grafico()

c.close()
conn.close()
