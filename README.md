# ⚙️ Data Automation Engine (Portail IPE)

> ⚠️ **Note :** Ce dépôt présente **les algorithmes centraux et la logique métier** (Snippets) que j'ai conçus. L'application complète n'est pas publique afin de protéger le code source de la solution developpé par Alan.

## 🎯 Contexte du Projet

Le traitement manuel de données massives (croisement de fichiers Excel, vérification d'historiques, application de règles métier complexes) est chronophage et source d'erreurs humaines. L'objectif de ce projet était de créer un **moteur d'automatisation intelligent** pour remplacer des heures de travail sur tableur par un script de quelques secondes.

## 💡 Mon Rôle & Mes Réalisations

J'ai développé un outil complet allant de la logique algorithmique à la restitution visuelle des données :

* **Moteur d'Analyse (Pandas) :** Développement d'algorithmes Python capables de lire, nettoyer et fusionner des bases de données massives (fichiers CSV/XLSX) de manière résiliente.
* **Scanner Intelligent :** Création d'une fonction de détection automatisée capable de scanner plusieurs onglets Excel pour trouver les bonnes colonnes malgré des formats d'entrée changeants (fuzzy matching des en-têtes).
* **Application des Règles Métier :** Traduction de règles métier complexes (statuts d'accréditation, gestion de dates de grâce, recherche de doublons) en code Python optimisé.
* **Dashboard Full-Stack :** Conception d'une interface web permettant aux utilisateurs finaux de glisser-déposer leurs fichiers, de lancer l'analyse côté serveur, et de visualiser instantanément les KPIs générés via Chart.js.

## 🛠️ Compétences Techniques Démontrées

* **Data Science :** Python, Pandas, Openpyxl, Data Cleaning & Merging.
* **Développement Web :** Flask, JavaScript, HTML/CSS.
* **Visualisation :** Chart.js pour la génération de graphiques dynamiques.

## 📂 Contenu de ce dépôt

Ce dépôt met en avant la qualité de mon code à travers plusieurs extraits clés :
* `smart_reader.py` : L'algorithme de détection et de nettoyage intelligent des données brutes.
* `data_merging.py` : La logique de jointure complexe et d'application des statuts.
* `api_handler.py` : Le lien Flask qui fait le pont entre le frontend et le script d'analyse.
