#!/usr/bin/python3
## nécéssaire d'installer python3, pip , flask, requests, flask-cors, flask-talisman

import cgitb; cgitb.enable()
import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_talisman import Talisman
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
talisman = Talisman(app)

# Upload folder for files
UPLOAD_FOLDER = './files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

array = []

# Json rempli manuellement pour le moment, mais qui devrait se remplir automatiquement par la suite
retourErreur = {
}

# Fonction de test de vie de l'API
@app.route('/')
def index():
    d = {
        "Hello": "World !"
    }
    return jsonify(d)


# Réception d'un fichier
@app.route('/upload', methods=['POST'])
# Sécurisation du code en https avec flask-talisman
@talisman(force_https=True)
def upload():
    """
    Prend en entrée un fichier

    Retourne un json de type :
        - {"code": "ok"}
            - Quand le fichier est bien reçu
        - {"code": "error", "error": "<explication>"}
            - Quand il y a une erreur avec l'envoie du fichier
    """
    if 'file' not in request.files:
        d = {
            "error": "No file",
            "code": "error"
        }
        return jsonify(d)
    else:
        f = request.files['file']
        if f.filename == '':
            d = {
                "error": "Filename is empty",
                "code": "error"
            }
            return jsonify(d)

        elif f:
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            d = {
                "code": "ok"
            }
            return jsonify(d)
        else:
            d = {
                "error": "error with upload file",
                "code": "error"
            }
            return jsonify(d)


if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
