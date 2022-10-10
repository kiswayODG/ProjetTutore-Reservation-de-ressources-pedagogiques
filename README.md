# ProjetTutore
Il s'agit d'un projet de classe réalisé avec des camarades de l'Ecole Supérieure d'Informatique (ESI) de l'université Nazi Boni. Ce projet a pour finalité d'être apprécié et noté par un enseignant de notre établissement.
Le projet est constitue d'un site web realisé avec le framework Django(framework base sur le langage python) pour permettre l'intégration de d'une base de donnée afin de sauvegarder des données et de rendre le site web dynamique.
L'éditeur Pycharm nous a servi d'Environnement de Developpement Intégré. Il utilise la version 1.8 de Django prenant en charge la version 3.10.7 de python.
Pour tester le projet en local, il faut d'abord démarrer le serveur avec la commande "python manage.py runserver". Mais avant d'exécuter cette commande,  vous devez vous assurer d'abord télécharger toutes les dépendances. Vous pouvez aussi le faire a travers la commande "pip install -r requirements.txt" 
Le projet est hébergé sur l'hébergeur heroku et est consultable à partir de l'adresse: projet-tutoreesi007.herokuapp.com

Le système de gestion mis en place est avant tout un moyen pour permettre une gestion éfficiente des ressources pédagogiques (salles, matériels…) en offrant aux acteurs une avance sur la gestion et la résolution des accès concurrents aux-dites ressources.Il est à noter que notre système a pour environnement le milieu scolaire. Il sera donc possible de le déployer dans les établissement d’enseignement de tout niveau (Primaire, Secondaire, Universitaire..) 

Afin de permettre d’avoir une vue globale de toutes les ressources disponibles, un tableau de toutes les ressources de l’établissement est mis à la disposition des utilisateurs.

Voici quelques exemples qui peuvent être résolus avec notre application:
 
 * Nous avons un projecteur qui doit être utilisé fréquemment par plusieurs classes.
 
 * Ou encore nous disposons d’une seule salle machine pour toutes les classes. 
 
 * Possibilité de faire une réservation selon une plage horaire bien précise du projecteur ou de la salle à partir d’un compte utilisateur ayant les droits de la faire.
 
 * Rendre indisponible (hors d’usage) un équipement en panne ou une salle en maintenance depuis un compte administrateur
 
 * Connaitre toutes les réservations faites sur une ressource grâce à un calendrier interactif de réservation concernant l’objet.
 * les ressources ainsi que les reservations peuvent etre modifiées ou supprimées par les administrateurs

