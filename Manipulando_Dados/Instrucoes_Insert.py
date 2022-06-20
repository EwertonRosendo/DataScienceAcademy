import os
import sqlite3

# Verificando se o arquivo já existe
os.remove("dsa.db") if os.path.exists("dsa.db") else None

# criando uma conexão com o arquivo
conn = sqlite3.connect("dsa.db")

# criando um cursor para usar no bd
c = conn.cursor()

