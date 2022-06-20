import os
import sqlite3
from time import sleep
# Essa linha irá remover o arquivo escola.db caso ele exista, se não existir,  não fará nada

os.remove("escola.db") if os.path.exists("escola.db") else None

# A função connect é usada para conectar-se a um banco de dados, entretanto
# Caso não seja localizado, ele também cria um banco de dados com o nome do parametro passado
con = sqlite3.connect("escola.db")  # salvamos a conexão num objeto chamado con


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

# Base de dados para ser incluida no Banco de Dados
recset = [(1000, "Ciência de Dados", "Data Science"),
          (1001, "Big Data Fundamentos", "Big Data"),
          (1002, "Python Fundamentos", "Analise de Dados")]

# -----------------------------------------------------------------------
# Aqui utilizamos um loop for para passar pelos dados que vão ser adicionados
# ao bd. Com o comando cur.execute fazemos com que o cursor insira os dados com
# o comando sql salvo na variavel sql_insert
try:
    for rec in recset:
        cur.execute(sql_insert, rec)

except Exception.__class__ as causa:
    print(f"Não foi possivel gravar os dados na tabela por: {causa}")

else:
    print(f"Dados gravados com sucesso!")

finally:
    con.commit()
    # Aqui passamos as atualizações do repositorio local para o arquivo escola.db
# -----------------------------------------------------------------------

# Comando para selecionar todos os elementos da tabela cursos
sql_select = "select * from cursos"

# Executamos o comando de seleção
cur.execute(sql_select)

# Seleciona todos os valores em formatos de 'listas'
dados = cur.fetchall()

# Utilizamos o laço for para printar os dados
for linha in dados:
    print(f'Curso Id: {linha[0]} Titulo: {linha[1]}, Categoria: {linha[2]}\n')

# ---------------------------------------------------------------------------
# Refazemos o mesmo processo de antes
recset = [(1003, "Gestão de dados com MongoDB", "Big Data"),
          (1004, "R Fundamentos", "Analise de Dados")]

try:
    for rec in recset:
        cur.execute(sql_insert, rec)
except Exception as causa:
    print(f"A causa do erro foi: {causa.__class__}")

else:
    print(f"Dados adicionados com sucesso")

finally:
    con.commit()

cur.execute(sql_select)
dados = cur.fetchall()

for linha in dados:
    sleep(1)
    print(f"Id: {dados[0]}, Titulo: {dados[1]}, Categoria: {dados[2]}")

# ---------------------------------------------------------------------------

# Por fim fechamos o banco de dados para evitar problemas
con.close()