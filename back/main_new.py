#! /usr/bin/python3
## nécéssaire d'installer python3, pip , flask, requests, flask-cors, flask-talisman

import cgitb; cgitb.enable()
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_talisman import Talisman

app = Flask(__name__)
CORS(app)
talisman = Talisman(app)

array = []

#Json rempli manuellement pour le moment, mais qui devrait se remplir automatiquement par la suite
retourErreur = {
}

@app.route('/')
#fonction de test de vie de l'API
def index():
    return "Hello world!"


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
