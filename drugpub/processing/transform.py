import numpy as np

def create_dict_graph(df, drug_list):
    """Créer un dictionnaire représentant les médicaments et leurs journaux correspondants.

    Args:
        df (pd.DataFrame): DataFrame contenant les données de publication avec les colonnes 'title', 'journal' et 'id'.
        drug_list (list): Liste des médicaments à rechercher dans les titres.

    Returns:
        dict: Un dictionnaire imbriqué où les clés sont des médicaments et les valeurs sont des journaux contenant
              les titres de 'pubmed' et 'clinical'.
    """
    dict_graph = {}

    for drug in drug_list:
        # Initialiser le dictionnaire pour le médicament
        dict_graph[drug] = {}

        # Créer un masque pour les titres contenant le médicament
        mask = df['title'].str.contains(drug, case=False, na=False)
        matching_indices = df.index[mask]

        for idx in matching_indices:
            journal = df.at[idx, 'journal']
            
            # Initialiser l'entrée du journal si elle n'existe pas
            if journal not in dict_graph[drug]:
                dict_graph[drug][journal] = {'pubmed': [], 'clinical': []}

            # Ajouter le titre à la catégorie appropriée en fonction de 'id'
            if isinstance(df.at[idx, 'id'], int):
                dict_graph[drug][journal]['pubmed'].append(df.at[idx, 'title'])
            else:
                dict_graph[drug][journal]['clinical'].append(df.at[idx, 'title'])

    return dict_graph
