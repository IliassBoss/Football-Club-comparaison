# Football-Club-comparaison

README PROJET NOSQL
Contexte et objectif
Ce projet a pour objectif de comparer deux équipes de football en utilisant des statistiques extraites du site Fbref via web scraping. Les données collectées couvrent plusieurs aspects de la performance des équipes, telles que les buts, les tirs, la possession, les passes, et d’autres indicateurs clés.
L’analyse s’appuie sur une base de données NoSQL (MongoDB) pour manipuler des documents JSON et réaliser des comparaisons statistiques pertinentes entre équipes.
Description du projet
Extraction des données
Les données des équipes ont été récupérées par scraping depuis Fbref, un site spécialisé dans les statistiques footballistiques.
Stockage des données
Les données ont été structurées au format JSON puis importées dans MongoDB. Chaque document représente une équipe avec ses différentes statistiques.
Comparaison des équipes
Un script Python (snosql3.py) permet d’interroger la base MongoDB, récupérer les données de deux équipes choisies par l’utilisateur, puis afficher une comparaison graphique des statistiques clés.
Technologies utilisées
MongoDB : base de données NoSQL pour le stockage et la requête des données.
Python : langage principal pour le traitement des données, la connexion à MongoDB via la bibliothèque PyMongo, et la génération des graphiques avec Matplotlib.
Bibliothèques Python :
PyMongo pour la communication avec MongoDB
Matplotlib pour la visualisation des données
Fonctionnement du projet
Importer les fichiers JSON dans MongoDB en utilisant la commande mongoimport ou via MongoDB Compass.
Exécuter le script Python snosql3.py.
Le script demande à l’utilisateur de saisir les noms des deux équipes à comparer.
Les données des équipes sont extraites depuis la base MongoDB.
Un graphique radar comparatif est affiché, mettant en lumière les différences statistiques entre les deux équipes.
Limites et améliorations possibles
Le scraping dépend de la structure du site Fbref, qui peut évoluer et rendre les scripts obsolètes.
Les statistiques utilisées pourraient être enrichies pour affiner la comparaison (par exemple, en tenant compte des performances par saison ou compétition).
Une interface graphique pourrait être développée pour faciliter l’utilisation du programme par des utilisateurs non techniques.
Conclusion
Ce projet a permis de mettre en pratique les concepts de bases de données NoSQL avec MongoDB, ainsi que les techniques de traitement et de visualisation de données en Python. La comparaison entre équipes est automatisée et facilement extensible, offrant un outil simple pour l’analyse statistique sportive.

![image](https://github.com/user-attachments/assets/55639874-4d5b-483a-821f-a788abcb0fb8)
![image](https://github.com/user-attachments/assets/d6305598-4a7c-41c7-a952-4a47398cf1e8)
![image](https://github.com/user-attachments/assets/9f415ac7-ea7f-4647-b9cf-0d8005f02cd4)

![image](https://github.com/user-attachments/assets/804642b3-813a-4c46-a8d8-107632a5714a)

