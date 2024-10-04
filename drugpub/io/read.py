import json
import re
import pandas as pd

def read_csv_file(file_path, logger):
    """Lire un fichier CSV et retourner un DataFrame.

    Args:
        file_path (str): Le chemin vers le fichier CSV à lire.

    Returns:
        pd.DataFrame: Un DataFrame contenant les données du fichier CSV.

    Raises:
        FileNotFoundError: Si le fichier spécifié n'est pas trouvé.
        pd.errors.EmptyDataError: Si le fichier est vide.
        pd.errors.ParserError: Si le fichier contient des erreurs de syntaxe.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        logger.error(f"Erreur : Le fichier '{file_path}' n'a pas été trouvé.")
    except pd.errors.EmptyDataError:
        logger.error(f"Erreur : Le fichier '{file_path}' est vide.")
    except pd.errors.ParserError as e:
        logger.error(f"Erreur lors de l'analyse du fichier CSV : {e}")

def read_json_to_csv(file_path, logger):
    """Lire un fichier JSON et retourner un DataFrame.

    Args:
        file_path (str): Le chemin vers le fichier JSON à lire.

    Returns:
        pd.DataFrame: Un DataFrame contenant les données du fichier JSON.

    Raises:
        FileNotFoundError: Si le fichier spécifié n'est pas trouvé.
        json.JSONDecodeError: Si le fichier JSON contient des erreurs de syntaxe.
    """
    try:
        with open(file_path, 'r') as file:
            data = file.read()

        # Correction des virgules traînantes pour un JSON valide
        valid_data = re.sub(r',\s*([}\]])', r'\1', data)

        valid_data = json.loads(valid_data)
        df = pd.DataFrame.from_dict(valid_data)
        return df
    except FileNotFoundError:
        logger.error(f"Erreur : Le fichier '{file_path}' n'a pas été trouvé.")
    except json.JSONDecodeError as e:
        logger.error(f"Erreur lors du chargement du JSON : {e}")
