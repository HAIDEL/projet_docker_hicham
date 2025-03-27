# Projet Simple Flask avec Redis

## Description
Ce projet est une application web simple utilisant Flask et Redis. L'application affiche une page d'accueil avec un compteur de visites stocké dans Redis. Le projet utilise Docker Compose pour orchestrer deux conteneurs qui communiquent entre eux.

## Structure du projet

```
projet-flask-redis/
├── docker-compose.yaml
├── README.md
└── app/
    ├── Dockerfile
    ├── requirements.txt
    ├── main.py
    └── templates/
        └── index.html
```

## Lancement du projet

1. **Pré-requis** :  
   - Docker et Docker Compose installés sur votre machine.

2. **Commandes** :

   Pour construire et lancer les conteneurs, exécutez dans le dossier du projet :
   ```
   docker-compose up --build
   ```

3. **Accès à l'application** :  
   Ouvrez votre navigateur et allez à l'adresse : [http://localhost:5000](http://localhost:5000)

## Tests
- Rafraîchissez la page pour voir le compteur de visites augmenter.

## Configuration
- Le service web utilise les variables d'environnement `REDIS_HOST` et `REDIS_PORT` pour se connecter au conteneur Redis.
- Vous pouvez modifier ces paramètres dans le fichier `docker-compose.yaml` si nécessaire.
