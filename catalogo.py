from flask import Flask
from flask import jsonify
from flask import request
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = MongoClient()
db = client.teste_db
collection = db.catalogo

@app.route('/get_records', methods=['GET'])
def get_records():
    saida = []
    for data in collection.find():
        saida.append({'nome': data['nome'], 'email': data['email'], 'telefone': data['telefone']})
    return jsonify(saida)

@app.route('/insert_record', methods=['POST'])
def insert_record():
  nome = request.json['nome']
  email = request.json['email']
  telefone = request.json['telefone']
  cat_id = collection.insert({'nome': nome, 'email': email, 'telefone': telefone})
  new_cat = collection.find_one({'_id': cat_id})
  saida = {'nome': new_cat['nome'], 'email': new_cat['email'], 'telefone': new_cat['telefone']}
  return jsonify(saida)


