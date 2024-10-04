# Projet DrugPub

## Description

Le projet DrugPub est conçu pour traiter et analyser des données sur les médicaments et leur mention dans les journaux scientifiques. Il permet de charger des données à partir de fichiers CSV et JSON, de les nettoyer et de créer un graphique de relations entre les médicaments et les journaux.

## Fonctionnalités

- Chargement des données à partir de fichiers CSV et JSON.
- Nettoyage et prétraitement des données.
- Création d'un dictionnaire de graphes reliant les médicaments et les journaux.
- Analyse des journaux pour identifier celui qui mentionne le plus de médicaments.
- Identification des médicaments liés par des journaux communs.

## Prérequis

Assurez-vous d'avoir installé les dépendances nécessaires. Utilisez le fichier `env.dev.yaml` pour installer les bibliothèques requises :

```bash
conda env install -f env.dev.yaml

.
├── data
│   ├── in
│   │   ├── drugs.csv
│   │   ├── clinical_trials.csv
│   │   ├── pubmed.csv
│   │   └── pubmed.json
│   └── out
│       ├── graph.json
│       └── app.log
├── drugpub
│   ├── io
│   │   ├── logger.py
│   │   ├── read.py
│   │   └── write.py
│   ├── launcher
│   │   └── execute.py
│   ├── processing
│   │   ├── clean.py
│   │   ├── impute_reformat.py
│   │   └── transform.py
│   └── get
│       └── info.py
├── config
│   └── conf.py
│   
└── main.py
