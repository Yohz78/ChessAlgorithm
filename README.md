# Projet 4 formation developpeur python : 
## Designez une application Python adaptée aux besoins d'un client 

Le but du programme est de réponse aux besoin d'un client. L'application doit permettre de gérer des tournois d'échec. 
L'application doit être capable de gérer une base de joueurs disposant d'un classement. Elle doit permettre de créer et lancer des tournois.
L'application doit pouvoir afficher des rapports concernant les différents objets la composant. Elle doit permettre de les enregistrer dans une base de données.

## 1) Installation

### 1) Clonage et navigation dans le dossier

Pour faire fonctionner ce projet, il est nécessaire de le cloner via la commande 

`git clone https://github.com/yohz78/Projet_4`

`cd Projet_4`

### 2) Préparation de l'environnement virtuel

Il faut ensuite installer le paquet nécessaire à la création d'un environnement virtuel via la `commande pip install virtualenv`.

### 3) Création de l'environnement virtuel

Un environnement virtuel devra ensuite être créé via l'execution de la commande `py -m venv .venv`

### 4) Installation des paquets

 Une fois cela fait, il faudra procéder à l'installation des paquets présents dans requirements.txt via la commande `pip install -r requirements.txt`

 ---
##  2) Utilisation

### 1) Execution du programme

Lancez le fichier "main.py"

### Utilisation du programme

Un menu s'affiche de façon permanente entre deux actions de l'utilisateur :

1 -- Ajouter des joueurs à la base de données
2 -- Creer un tournois
3 -- Lancer un tournois
4 -- Afficher le classement des joueurs
5 -- Afficher la liste des joueurs
6 -- Afficher la liste des tournois
7 -- Modifier le classement d'un joueur
8 -- Sauvegarder les joueurs dans la database
9 -- Charger les joueurs enregistrés dans la database
10 -- Sauvegarder les tournois dans la database
11 -- Charger les tournois de la database
12 -- Afficher la liste des joueurs d'un tournois
13 -- Afficher le classement des joueurs d'un tournois
14 -- Afficher les tours d'un tournois
15 -- Afficher tous les matchs d'un tournois
16 -- Quitter l'application

L'utilisateur doit saisir un nombre entier entre 1 et 16 pour choisir une action à réaliser.

L'option 1 va lui permettre de choisir un nombre de joueur à créer. Il devra ensuite rentrer les données nécessaires à la création de chaque joueur.

L'option 2 permet de créer un tournois. L'utilisateur va devoir entrer les informations nécessaire à sa création.

L'option 3 permet de lancer un tournois en le choisissant dans la liste des tournois de l'application. L'utilisateur va ensuite devoir choisir les 8 joueurs prenant part au tournois.
Il devra ensuite indiquer la fin de chaque round du tournois puis saisir les résultats des matchs de celui-ci. A la fin du tournois, le classement des joueurs avant tournois sera affiché, puis 
le classement des joueurs par leur score lors du tournois sera affiché. L'utilisateur devra ensuite modifier le classement global de chaque joueur ayant pris part au tournois.

L'option 4 affiche le classement des joueurs.

L'option 5 permet d'afficher la liste des joueurs par ordre alphabétique.

L'option 6 affiche la liste des tournois

L'option 7 permet de modifier le classement d'un joueur après avoir affiché le classement.

L'option 8 sauvegarder les joueurs entrés dans l'application dans la database.

L'option 9 permet de charger les joueurs contenus dans la database.

L'option 10 permet de sauvegarder les tournois créés dans la database.

L'option 11 permet de charger les tournois contenus dans la database.

L'option 12 permet d'afficher la liste des joueurs d'un tournois.

L'option 13 permet d'afficher le classement des joueurs d'un tournois.

L'option 14 permet d'afficher tous les tours d'un tournois.

L'option 15 permet d'afficher tous les matchs d'un tournois.

L'option 16 permet de quitter l'application.

Versionnages :

V0.1 : Initialisation du projet

V0.2 : Définition des modèles

V0.3 : Définition des constructeurs de modèles

V0.4 : Construction de méthodes des modèles

V0.5 : Construction de la vue.

V0.6 : Construction du contrôleur

V0.7 : Construction du menu

V0.8 : Gestion de la base de données

V0.9 : Finalisation de l'app.

V1.0 : Version finale nettoyée, Requirement.txt fait.