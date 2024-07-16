# py-traducteur 🔈

py-traducter est une application web qui permet à un utilisateur authentifié de traduire des textes d’une langue à une autre. Les réponses sont disposées sous forme de chat.

## L’application repose sur 3 “briques”:

* Une base de données MySQL qui tourne dans un container Docker.
* Un backend python qui utilise FastAPI pour faire le lien entre le client, la base de données et le modèle de traduction
* Un client, un front-end développé avec streamlit

## Technologies utilisées

* Streamlit : framework Python pour la création d'applications web interactives.
* streamlit_chat : bibliothèque permettant d'implémenter un système de chat dans 	une application Streamlit.
* Requêtes HTTP : l'application utilise des requêtes HTTP pour communiquer avec un serveur distant et récupérer les informations nécessaires aux traductions.
* transformers: 	la bibliothèque de Hugging Face qui propose un pipeline d’inférence de différent modèles d’IA, notamment  https://huggingface.co/Helsinki-NLP
* Docker: pour faire tourner la base de données
* MySQL:  la base de donnée relationnelles
* Grafana: pour créer et afficher des dashboards de monitoring.

## Installation
L'application de départ contenant les bugs à regler se trouve ici: https://github.com/Stephane-ISEN/py-traducteur

1. cloner le repo 

```bash
git clone https://github.com/Hatchi-Kin/py-traducteur.git
```

2. Lancer d'abord la base de données grâce à Docker Compose.

```bash
cd bdd_traducteur
docker compose up -d
```

3. Créer un environnement virtuel pour l'API, puis installez dans l'environnement virtuel les dépendances à partir du fichier `requirements.txt`. Lancez l'API en exécutant le code Python.

```bash
cd api_traducteur
python3 -m venv .apivenv
source .apivenv/bin/activate
pip install -r requirements.tx
python src/api.py
```

4. Créer un environnement virtuel pour l'application web, puis installez dans l'environnement virtuel les dépendances à partir du fichier `requirements.txt`. Lancez l'application web grâce aux commandes de Streamlit.

```bash
cd web_traducteur
python3 -m venv .webvenv
source .webvenv/bin/activate
pip install -r requirements.tx
streamlit run src/app.py
```