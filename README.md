# Workshop vêtements

Application permettant de trouver la bonne tenue pour n'importe quelle occasion !

Travail / École / Entretient / Mariage / Enterrement / Bar Mitzvah / Robanukah


##### URL de l'API : http://ns327097.ip-37-187-109.eu:5000/

## routes : 

### GET

#### /

Retourne « Hello World ! »

#### /list/clothes

Retourne toute la table vetement

#### /list/clothes/'user'

Retourne la liste des vetements pour l'utilisateur 'user'

#### /list/clothes/0/'user'

Retourne la liste des Vetement de torse pour l'utilisateur 'user'

#### /list/clothes/1/'user'

Retourne la liste des vetement de jambes pour l'utilisateur 'user'

#### /list/clothes/2/'user'

Retourne la liste des chaussures pour l'utilisateur 'user'

#### /download?id=<id>

Permet de récupérer l'image d'un vêtement par rapport à son id


### POST

#### /upload

Arguments :
	- file
	- user
	- type_clothes

#### /inscription

Arguments :
	- user
	- password

## Dépendance

Pour faire tourner le Back il y a besoin de :

	- MariaDB
	- Python 3
	- Flask (https://github.com/pallets/flask)
	- Flask-cors (https://github.com/corydolphin/flask-cors)
	- Flask-talisman (https://github.com/GoogleCloudPlatform/flask-talisman)
	- PyMySQL (https://github.com/PyMySQL/PyMySQL)
	- Color Thief (https://github.com/fengsp/color-thief-py)
