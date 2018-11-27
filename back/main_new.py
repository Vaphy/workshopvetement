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

#réception d'un fichier
@app.route('/reception_fichier', methods=['POST'])
#sécurisation du code en https avec flask-talisman
@talisman(force_https=True)
def reception_fichier(self, request):
	try:
        if 'recipe_image' in request.files:
            filename = images.save(request.files['recipe_image'])
            self.image_filename = filename
            self.image_url = images.url(filename)
        else:
            json_data = request.get_json()
            self.recipe_title = json_data['title']
            self.recipe_description = json_data['description']
            if 'recipe_type' in json_data:
                self.recipe_type = json_data['recipe_type']
    except KeyError as e:
        raise ValidationError('Invalid recipe: missing ' + e.args[0])
    return self


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
