# workshopvetement


URL de l'API :
http://ns327097.ip-37-187-109.eu:5000/

routes : 

	GET

		/
		Retourne "hello world !"


		/list/clothes
		Retourne toute la table vetement

		/list/clothes/'user'
		Retourne la liste des vetements pour l'utilisateur 'user'

		/list/clothes/0/'user'
		Retourne la liste des Vetement de torse pour l'utilisateur 'user'

		/list/clothes/1/'user'
		Retourne la liste des vetement de jambes pour l'utilisateur 'user'


		/list/clothes/2/'user'
		Retourne la liste des chaussures pour l'utilisateur 'user'


	POST

		/upload
		Arguments: 
		- file
		- user
		- type_clothes

		/inscription
		Arguments: 