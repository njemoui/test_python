import json

def write_json(dict_graph, output_path,logger):
    """Écrire un dictionnaire dans un fichier JSON.

    Args:
        dict_graph (dict): Le dictionnaire à écrire dans le fichier JSON.
        output_path (str): Le chemin du fichier de sortie où les données seront enregistrées.

    Raises:
        IOError: Si le fichier ne peut pas être ouvert ou écrit.
    """
    try:
        with open(output_path, 'w') as json_file:
            json.dump(dict_graph, json_file, indent=4)
    except IOError as e:
        logger.error(f"Erreur lors de l'écriture dans le fichier '{output_path}': {e}")
