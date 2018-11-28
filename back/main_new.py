#!/usr/bin/python3
## nécéssaire d'installer python3, pip , flask, requests, flask-cors, flask-talisman, PyMySQL

import cgitb; cgitb.enable()
import os
import requests
import color
import database
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
        sql = "insert into users (login, password) values ('%s','%s');"%(user,password)
        r = database.insert(sql)
        return jsonify(r), 200
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
            #sauvegarde du fichier photo sur le serveur
            print("etape 1")
            filename = secure_filename(f.filename)
            print("etape 2")
            f_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            print("etape 3")
            f.save(f_path)
            print("etape 4")

            #génération de l'url_photo


            #obtention de la couleur
            f_color = color.get_color(f_path)
            print("etape 5")

            #récuperation user

            user = request.form['user']
            print("etape 6")

            #récuperation type
            type_clothes = request.form['type_clothes']
            print("etape 7")

            #calcul du dressing en fonction de l'user connecté
            sql = "SELECT id FROM users WHERE login = '%s';"%(user)
            requette_user_id = database.select(sql)
            user_id = requette_user_id[0].get("id")
            print("user_id : "%d)%(user_id)

            sql = "SELECT id FROM dressing WHERE user_id = '%s';"%(user_id)
            requette_dressing_id = database.select(sql)
            dressing_id = requette_dressing_id[0].get("id")
            print("dressing_id : "%d)%(dressing_id)

            #sauvegarde des paramètre du vetement en BDD
            #sql = "insert into vetement (dressing_id, path_photo, color, type, url_photo) values ('%d','%s','%s','%d','%s');"%(dressing_id, path_photo, color, type_clothes, url_photo)
            

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


# Réception d'un fichier
@app.route('/list/clothes', methods=['GET'])
# Sécurisation du code en https avec flask-talisman
@talisman(force_https=True)
def list_clothes():
    sql = "SELECT * FROM vetement"
    r = database.select(sql)
    return jsonify(r)


if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
