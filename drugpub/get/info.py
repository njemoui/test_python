def journal_with_most_drugs(data):
    """Trouver le journal avec le plus de médicaments différents.

    Cette fonction parcourt les données des médicaments et des journaux, 
    en comptant le nombre de médicaments différents mentionnés dans chaque journal. 
    Elle retourne le ou les journaux ayant le plus grand nombre de médicaments distincts 
    ainsi que ce nombre.

    Args:
        data (dict): Un dictionnaire où les clés sont des noms de médicaments 
                     et les valeurs sont des dictionnaires de journaux associés.

    Returns:
        tuple: Un tuple contenant une liste des journaux avec le plus de médicaments 
               différents et le nombre de médicaments.
    """
    journal_drug_count = {}  # Dictionnaire pour stocker les journaux et les médicaments associés

    # Parcourir chaque médicament et ses journaux associés
    for drug, journals in data.items():
        for journal in journals.keys():
            # Si le journal n'est pas encore dans le dictionnaire, l'initialiser avec un ensemble vide
            if journal not in journal_drug_count:
                journal_drug_count[journal] = set()
            # Ajouter le médicament à l'ensemble des médicaments pour ce journal
            journal_drug_count[journal].add(drug)

    # Trouver le nombre maximum de médicaments associés à un journal
    max_count = max(len(drugs) for drugs in journal_drug_count.values())
    
    # Créer une liste des journaux qui ont le même nombre maximum de médicaments
    max_journals = [journal for journal, drugs in journal_drug_count.items() if len(drugs) == max_count]

    return max_journals, max_count  # Retourner la liste des journaux et le nombre maximum de médicaments



def drugs_in_same_journals(data, target_drug):
    """Trouver tous les médicaments mentionnés par les mêmes journaux que le médicament cible.

    Args:
        data (dict): Un dictionnaire où les clés sont des médicaments et les valeurs sont des dictionnaires 
                     contenant les journaux associés à chaque médicament.
        target_drug (str): Le nom du médicament cible pour lequel on recherche des médicaments associés.

    Returns:
        set: Un ensemble de médicaments mentionnés par les mêmes journaux que le médicament cible.
    """
    # Récupérer les journaux associés au médicament cible
    target_journals = set(data.get(target_drug, {}).keys())
    related_drugs = set()  # Ensemble pour stocker les médicaments associés

    # Parcourir tous les médicaments et leurs journaux
    for drug, journals in data.items():
        for journal in journals.keys():
            # Si le journal est dans les journaux du médicament cible et que le médicament n'est pas le même
            if journal in target_journals and drug != target_drug:
                related_drugs.add(drug)  # Ajouter le médicament associé à l'ensemble

    return related_drugs