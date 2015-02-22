#TODOPLAN

##Définir une api rest

GET /projects/ #Liste des projets
POST /projects/ #Insert project(s)
GET /projects/<id_project:int> #Représentation du projet
PUT /projects/<id_project:int> #Mise à jour du projet
DELETE /projects/<id_project:int> #Suppression du projet
GET /projects/<id_project:int>/impacts #Liste des Impacts concernés par un projet

GET /impacts/ #Liste des impacts
GET /impacts/ #Insert impact
GET /impacts/<id_impact:int> #Représentation de l'impact
PUT
DELETE

GET /groups
POST /groups
GET /groups/<id_group:int>
PUT
DELETE
GET /groups/<id_group:int>/projects #Liste des projects

##Définir le modèle
* projects
- id_project
- name
- id_groupe
- date_impact

* impacts
- id_impact
- id_location
- type
- nb_real
- nb_feel

* groups
- id_group
- name
- date_start
- date_end

#Définir la test suite
#Utiliser bottle en python
#A voir pour la restitution graphique

