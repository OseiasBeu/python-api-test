from flask import Flask
from flask import jsonify
from flask import request
from pymongo import MongoClient
app = Flask(__name__)

client = MongoClient()
db = client.teste_db
collection = db.catalogo

@app.route('/get_records', methods=['GET'])
def get_records():
    saida = []
    for data in collection.find():
        saida.append({'nome': data['nome'], 'email': data['email'], 'telefone': data['telefone']})
    return jsonify({'catalogo': saida})


