import os
import sqlite3

# Essa linha irá remover o arquivo escola.db caso ele exista, se não existir,  não fará nada

os.remove("escola.db") if os.path.exists("escola.db") else None

# A função connect é usada para conectar-se a um banco de dados, entretanto
# Caso não seja localizado, ele também cria um banco de dados com o nome do parametro passado
con = sqlite3.connect("escola.db")  # salvamos a conexão em um objeto chamado con


# Agora vamos criar um Cursor, que serve para acessar todos os dados dentro do banco de dados
cur = con.cursor()

# Essa é a sintaxe SQL para criar tabelas e definir tipos

sql_create = "create table cursos "\
    "(id integer primary key, "\
    "titulo varchar(100), "\
    "categoria varchar(140))"

cur.execute(sql_create)

# esse é o comando para inserir os valores na tabela cursos
sql_insert = "insert into cursos values (?, ?, ?)"

recset = [(1000, "Ciência de Dados", "Data Science"),
          (1001, "Big Data Fundamentos", "Big Data"),
          (1002, "Python Fundamentos", "Analise de Dados")]

try:
    for rec in recset:
        cur.execute(sql_insert, rec)

except Exception.__class__ as causa:
    print(f"Não foi possivel gravar os dados na tabela por: {causa}")

else:
    print(f"Dados gravados com sucesso!")

finally:
    con.commit()

sql_select = "select * from cursos"

cur.execute(sql_select)
dados = cur.fetchall()

for linha in dados:
    print(f'Curso Id: {linha[0]} Titulo: {linha[1]}, Categoria: {linha[2]}\n')