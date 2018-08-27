from flask import Flask
from flask import jsonify
from flask import request
from pymongo import MongoClient
app = Flask(__name__)

client = MongoClient()
db = client.teste_db
collection = db.catalogo




