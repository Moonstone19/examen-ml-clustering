# Examen de Machine Learning – Clustering

## Description

Ce projet a été réalisé dans le cadre de mon examen de Machine Learning.
Il consiste à appliquer un algorithme de clustering (KMeans) sur un jeu
de données réel, puis à développer une application interactive pour
visualiser les résultats.

## Dataset

Le dataset utilisé est :
**Facebook Live Sellers in Thailand**

Source officielle :
https://archive.ics.uci.edu/dataset/488/facebook+live+sellers+in+thailand

## Méthodologie

- Nettoyage de la base de données
- Création d’une variable `status` pour identifier les individus
- Sélection de variables numériques pertinentes
- Normalisation des données
- Application de l’algorithme KMeans
- Visualisation des clusters à l’aide de scatterplots

## Application

j'ai developpee application Streamlit afin de :

- Visualiser tous les clusters
- Visualiser chaque cluster séparément
- Afficher la liste des individus par cluster

## Fichiers du projet

- `app.py` : application Streamlit
- `live.csv` : dataset nettoyé
- `requirements.txt` : dépendances du projet
- `clustering_facebook_live.ipynb` : notebook d’analyse

## Auteur

Rita Marie Chambaz  
Licence 3 – Big Data  
Dakar Institute of Technology (DIT)

