from drugpub.io.logger import setup_logging
from drugpub.launcher.execute import analyze_data, load_data, process_data
from config import conf as cf


def main():
    """Point d'entrée principal pour le traitement des données.

    Cette fonction configure le système de journalisation, charge les données,
    traite les données et exécute l'analyse sur les médicaments spécifiés. 
    Elle suit les étapes suivantes :

    1. Configuration de la journalisation avec les paramètres définis dans le fichier de configuration.
    2. Chargement des données nécessaires à partir des fichiers CSV et JSON.
    3. Traitement des données pour créer un dictionnaire graphique représentant les relations entre les médicaments et les publications.
    4. Analyse des données pour le médicament spécifié ('EPINEPHRINE') et affichage des résultats.

    Les exceptions survenant à chaque étape sont gérées via le logger configuré, garantissant que les erreurs sont correctement enregistrées pour un diagnostic ultérieur.

    Raises:
        Exception: Si une erreur se produit lors de la configuration, du chargement ou du traitement des données,
                   cette exception sera levée et enregistrée.

    Notes:
        - Assurez-vous que les fichiers de données sont accessibles et bien formatés avant d'exécuter cette fonction.
        - Le médicament à analyser peut être modifié directement dans le code si nécessaire.
    """
    logger = setup_logging(cf)  # Configuration de la journalisation
    drugs, data = load_data(cf, logger)  # Chargement des données
    dict_graph = process_data(drugs, data, cf, logger)  # Traitement des données
    analyze_data(dict_graph, 'EPINEPHRINE', logger)  # Analyse des données pour le médicament spécifié


if __name__ == "__main__":
    main()
