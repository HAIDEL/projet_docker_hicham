## Description

Ce projet met en place une application web simple qui permet d’ajouter des messages via un formulaire et d’afficher les 10 derniers messages. L’application utilise Flask et stocke les messages dans une base de données SQLite. Un conteneur Nginx agit comme reverse proxy pour rediriger les requêtes vers l’application Flask.

## Architecture du Projet

```
projet_docker_hicham/
├── docker-compose.yaml
├── README.md
├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
└── web/
    ├── Dockerfile
    └── default.conf
```

- **app/** : Contient l’application Flask, le Dockerfile pour construire l’image et le fichier `requirements.txt` (avec Flask, Gunicorn et SQLAlchemy).
- **web/** : Contient le Dockerfile et la configuration Nginx (`default.conf`) servant de reverse proxy vers l’application Flask.
- **docker-compose.yaml** : Définit les deux services (app et web) et leur réseau commun.

## Prérequis

- Docker
- Docker Compose

## Lancement du Projet

1. **Cloner le dépôt ou extraire l’archive**  
   Récupère le projet depuis le dépôt Git ou l’archive ZIP.

2. **Se placer dans le répertoire racine**

   ```bash
   cd projet_docker_hicham
   ```

3. **Construire et lancer les conteneurs**

   ```bash
   docker-compose up --build
   ```

4. **Accéder à l’application**  
   Ouvre ton navigateur et va à l’adresse [http://localhost](http://localhost).

## Fonctionnement de l'Application

- **Ajout de messages :**  
  Saisis un message dans le formulaire et clique sur "Envoyer". Le message sera enregistré dans la base SQLite.

- **Affichage des messages :**  
  La zone scrollable affiche les 10 derniers messages avec les plus récents en haut.

- **Stockage persistant :**  
  Les messages sont sauvegardés dans une base de données SQLite (mise en place pour simplifier le projet).  
  *Note : Pour une utilisation en production, il est conseillé d’envisager un stockage persistant (par exemple, en mappant un volume ou en utilisant une base de données dédiée).*

## Configuration et Communication

- **Chemins relatifs :**  
  Tous les chemins dans le projet sont relatifs au répertoire racine `projet_docker_hicham`.

- **Conteneurs utilisés :**  
  - **app** : Exécute l’application Flask avec Gunicorn.  
  - **web** : Exécute Nginx et redirige les requêtes vers l’application Flask.

- **Réseau :**  
  Les deux conteneurs communiquent via le réseau défini dans le fichier `docker-compose.yaml`.

- **Dockerfiles :**  
  - Le Dockerfile de **app/** installe les dépendances, copie le code et démarre l’application via Gunicorn.
  - Le Dockerfile de **web/** part de l’image Nginx officielle et copie la configuration personnalisée (`default.conf`).

## Tests

Pour tester l’application :

1. Lance le projet avec `docker-compose up --build`.
2. Accède à [http://localhost](http://localhost) dans ton navigateur.
3. Envoie plusieurs messages via le formulaire.
4. Vérifie que la zone des messages affiche bien les 10 derniers messages, les plus récents en haut.

## Remarques

- **Développement vs Production :**  
  Ce projet est initialement conçu pour un environnement de développement. Pour une mise en production, il est recommandé :
  - D’utiliser un nombre de workers adapté avec Gunicorn (ou un autre serveur WSGI) en ajustant l’option `-w` dans le Dockerfile.
  - D’envisager un système de stockage persistant pour la base de données, afin de ne pas perdre les messages en cas de redémarrage du conteneur.

- **Améliorations futures :**  
  Vous pouvez enrichir l’interface ou intégrer un système d’authentification pour limiter l’accès à l’ajout de messages, ainsi que migrer vers une base de données plus robuste en production.

