import sqlite3
import os

os.remove("escola.bd") if os.path.exists("escola.bd") else None

con = sqlite3.connect("escola.bd")

cur = con.cursor()

sql_create = "create table cursos "\
    "(id  integer primary key, "\
    "titulo varchar(100), "\
    "categoria varchar(140)) "

cur.execute(sql_create)

sql_insert = "insert into cursos values(?, ?, ?)"

# dados

recset = [(1000, "ciencia de dados", "data science"),
          (1001, "big data fundamentos", "big data"),
          (1002, "python fundamentos", "Analise de dados")]
