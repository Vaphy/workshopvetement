#!/usr/bin/python3
## nécéssaire d'installer python3, pip , flask, requests, flask-cors, flask-talisman

import cgitb; cgitb.enable()
import os
import requests
import color
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_talisman import Talisman
from werkzeug.utils import secure_filename
from logging.handlers import RotatingFileHandler

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

#inscription d'un utilisateur
@app.route('/inscription', methods=['POST'])
# Sécurisation du code en https avec flask-talisman
@talisman(force_https=True)
def inscription():
    if request.form['user'] and request.form['password']:
        user=request.form['user']
        password=request.form['password']
        app.logger.info(user)
        app.logger.info(password)
        return jsonify(
            retour="bien inscrit"
        ), 200
    else:
        return jsonify(
            retour="erreur durant l'inscription"
        ), 400




# Réception d'un fichier
@app.route('/upload', methods=['POST'])
# Sécurisation du code en https avec flask-talisman
@talisman(force_https=True)
def upload():
    """
    Prend en entrée un fichier

    Retourne un json de type :
        - {"code": "ok", "color": "#<color>"}
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
            f_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            f.save(f_path)
            f_color = color.get_color(f_path)
            d = {
                "code": "ok",
                "color": f_color
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
