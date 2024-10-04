import pandas as pd
from drugpub.io.read import read_csv_file, read_json_to_csv
from drugpub.io.write import write_json
from drugpub.processing.impute_reformat import column_date_format, impute_id
from drugpub.processing.clean import apply_text_cleaner, drop_if_na_or_whitespace
from drugpub.processing.transform import create_dict_graph
from drugpub.get.info import drugs_in_same_journals, journal_with_most_drugs

def load_data(cf, logger):
    """Charger et prétraiter les données.

    Args:
        cf: Configuration contenant les chemins des fichiers et les formats.
        logger: Logger pour enregistrer les événements et les erreurs.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: DataFrames contenant les données de médicaments et de publications.
    """
    try:
        # Chargement des fichiers de données
        drugs = read_csv_file(cf.drugs_file_path, logger)
        clinical = read_csv_file(cf.clinical_file_path, logger)
        
        # Formatage des dates et nettoyage
        clinical = column_date_format(clinical, 'date', cf.date_format)
        clinical = clinical[drop_if_na_or_whitespace(clinical, ["scientific_title", "date", "journal"])]
        clinical.reset_index(drop=True, inplace=True)
        clinical = apply_text_cleaner(clinical, ['scientific_title', 'journal'])
        clinical = impute_id(clinical, 'id', str)

        # Chargement des données PubMed
        pubmed = read_csv_file(cf.pubmed_file_path.format(ext='csv'), logger)
        pubmed_json = read_json_to_csv(cf.pubmed_file_path.format(ext='json'), logger)
        
        # Fusion des données
        pubmed = pd.concat([pubmed, pubmed_json])
        pubmed.reset_index(drop=True, inplace=True)
        
        # Formatage et nettoyage des données PubMed
        pubmed = column_date_format(pubmed, 'date', cf.date_format)
        pubmed = apply_text_cleaner(pubmed, ['title', 'journal'])
        pubmed = impute_id(pubmed, 'id', int)

        # Renommage des colonnes pour une cohérence
        clinical.rename(columns={"scientific_title": "title"}, inplace=True)
        pubmed = pd.concat([pubmed, clinical])
        pubmed.reset_index(drop=True, inplace=True)

        return drugs, pubmed

    except Exception as e:
        logger.error(f"Erreur lors du chargement des données: {e}")
        raise

def process_data(drugs, pubmed, cf, logger):
    """Créer un graphe de dictionnaire et l'enregistrer au format JSON.

    Args:
        drugs: DataFrame contenant les données des médicaments.
        pubmed: DataFrame contenant les données des publications.
        cf: Configuration contenant le chemin de sortie pour le JSON.
        logger: Logger pour enregistrer les événements et les erreurs.

    Returns:
        dict: Dictionnaire représentant le graphe des données.
    """
    try:
        dict_graph = create_dict_graph(pubmed, drugs['drug'].tolist())
        write_json(dict_graph, cf.dict_graph_path, logger)
        return dict_graph
    except Exception as e:
        logger.error(f"Erreur lors du traitement des données: {e}")
        raise

def analyze_data(dict_graph, target_drug, logger):
    """Analyser les données des journaux et afficher les résultats.

    Args:
        dict_graph: Dictionnaire représentant le graphe des données.
        target_drug: Nom du médicament cible pour l'analyse.
        logger: Logger pour enregistrer les événements et les erreurs.
    """
    try:
        max_journals, count = journal_with_most_drugs(dict_graph)
        logger.info(f"Journaux avec le plus de médicaments différents ({count} médicaments): {', '.join(max_journals)}")

        related_drugs = drugs_in_same_journals(dict_graph, target_drug)
        logger.info(f"Médicaments mentionnés par les mêmes journaux que {target_drug}: {', '.join(related_drugs)}")

    except Exception as e:
        logger.error(f"Erreur lors de l'analyse des données: {e}")
        raise
