import logging

def setup_logging(cf):
    """Configurer la journalisation pour l'application.

    Cette fonction initialise la configuration de journalisation en utilisant les paramètres fournis 
    dans l'objet de configuration `cf`. Elle configure la journalisation pour écrire à la fois 
    dans un fichier et sur la console, en utilisant le niveau de journalisation spécifié.

    Args:
        cf: Un objet de configuration qui doit contenir un attribut `log_output` 
            spécifiant le chemin du fichier de sortie pour les logs.

    Returns:
        Logger: Un objet Logger configuré pour l'application.
    
    Raises:
        ValueError: Si `cf.log_output` n'est pas spécifié ou si le chemin est invalide.
    """
    log_output = getattr(cf, 'log_output', None)
    
    if not log_output:
        raise ValueError("Le chemin de sortie pour les logs n'est pas spécifié dans la configuration.")

    logging.basicConfig(
        level=logging.INFO,  # Ajustez le niveau de journalisation selon les besoins
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_output),  # Journaliser dans un fichier
            logging.StreamHandler()            # Journaliser sur la console
        ]
    )
    return logging.getLogger(__name__)
