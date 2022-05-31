import sqlite3
import os

os.remove("escola.bd") if os.path.exists("escola.bd") else None

con = sqlite3.connect("escola.bd")

cur = con.cursor()

sql_create = "create table cursos "\
    "(id  integer primary key, "\
    "titulo varchar(100),"\
    "categoria varchar(140)"
