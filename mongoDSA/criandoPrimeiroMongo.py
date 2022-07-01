from pymongo import MongoClient

import datetime

# A função MongoClient realiza a conexão com o banco de dados, e salvamos essa conexão na variavel conn
conn = MongoClient("localhost", 27017)

db = conn.cadastrodb

colletion = conn.cadastrodb

post1 = {"codigo": "ID-9987725",
         "prod_name": "Geladeira",
         "geladeira": ["brastemp", "consul", "eletrolux"],
         "data_cadastro": datetime.datetime.utcnow()}


colletion = db.posts

post_id = colletion.insert_one(post1)

post_id.inserted_id