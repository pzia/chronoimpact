#TODOPLAN

##Définir une api rest

###Quelques sources
* l'api twitter : https://dev.twitter.com/rest/public
* une belle synthèse opérationnelle : http://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api
* l'api stripe : https://stripe.com/docs/api#intro
* une autre synthèse de "best practice" : https://blog.apigee.com/detail/restful_api_design_can_your_api_give_developers_just_the_information
* la RFC pour les template d'url : https://tools.ietf.org/html/rfc6570

###Project
* GET /projects/ #Liste des projets
* POST /projects/ #Insert project(s)
* GET /projects/<id_project:int> #Représentation du projet
* PUT /projects/<id_project:int> #Mise à jour du projet
* DELETE /projects/<id_project:int> #Suppression du projet
* GET /projects/<id_project:int>/impacts #Liste des Impacts concernés par un projet

###Impact
* GET /impacts/ #Liste des impacts
* GET /impacts/ #Insert impact
* GET /impacts/<id_impact:int> #Représentation de l'impact
* PUT
* DELETE

#Group
* GET /groups
* POST /groups
* GET /groups/<id_group:int>
* PUT
* DELETE
* GET /groups/<id_group:int>/projects #Liste des projects

#Location
* GET /locations
* GET /locations/<id_location:int>/impacts #Liste des impacts pour une location donnée

##Définir le modèle relationnel

###Normes
* tables et champs en minuscules
* nom de la table au pluriel
* une clef primaire unique autoincrémentée par table
* la clef est id_<nom de la table au singulier>
* Le modèle est défini par [src/sql/create.sql]

###projects
- id_project
- name
- id_group
- date_impact

###impacts
- id_impact
- id_location
- type
- nb_real
- nb_feel

###groups
- id_group
- name
- date_start
- date_end

###locations
- id_location
- name

##Technologies
- Python + Bottle pour l'api rest
- sqlite pour la db
- jtables pour l'ihm


##Définir une test suite
* ce serait bien...
* 

##Développer l'api en python
* Utilisation de bottle : http://bottlepy.org/docs/dev/index.html
* Faire un test rapide : OK dans src/misc/testbottle.py
* Développer une API complète pour une des tables
* ? Rendre générique le code :
  * Découvrir le modèle de donnée dynamiquement
  * Construire l'api dynamiquement
  * Worth reading : http://fr.slideshare.net/jeffknupp/building-automated-rest-apis-with-python

##Implémenter l'utilisation de l'API
* Basiquement, on est face à une IHM d'administration de tables : utilisons datables : https://datatables.net/
*

##Restitution graphique
* Essayer Google Chart : https://google-developers.appspot.com/chart/interactive/docs/gallery/bubblechart
  * Ce qui se traduirait par une page html avec un peu de javascript qui charge les données (Api ?) et les restitue

##Gérer l'authentification pour l'api
* REST & Authentification : http://broadcast.oreilly.com/2009/12/principles-for-standardized-rest-authentication.html

