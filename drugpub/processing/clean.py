import re
import pandas as pd

def clean_text(text):
    """Nettoyer le texte en supprimant les séquences d'échappement hexadécimales.

    Args:
        text (str or bytes): Le texte à nettoyer.

    Returns:
        str: Le texte nettoyé.
    """
    try:
        # Décodage si le texte est en bytes
        if isinstance(text, bytes):
            text = text.decode('latin1', errors='ignore')
        
        # Suppression des séquences d'échappement hexadécimales
        cleaned_text = re.sub(r'\\x[0-9a-fA-F]{2}', '', text) 
        return cleaned_text

    except Exception as e:
        print(f"Erreur lors du nettoyage du texte: {str(e)}")
        print(f"Texte original: {str(text)}")
        return text

def apply_text_cleaner(df, cols, f=clean_text):
    """Appliquer une fonction de nettoyage de texte sur des colonnes spécifiques d'un DataFrame.

    Args:
        df (pd.DataFrame): Le DataFrame contenant les données.
        cols (list of str): Les noms des colonnes à nettoyer.
        f (function): La fonction de nettoyage à appliquer (par défaut: clean_text).

    Returns:
        pd.DataFrame: Le DataFrame avec les colonnes nettoyées.
    """
    for col in cols:
        df[col] = df[col].apply(f)
    return df

def drop_if_na_or_whitespace(df, cols):
    """Créer un masque pour filtrer les lignes avec des valeurs NaN ou des espaces blancs.

    Args:
        df (pd.DataFrame): Le DataFrame à filtrer.
        cols (list of str): Les noms des colonnes à vérifier.

    Returns:
        pd.Series: Un masque de booléens indiquant les lignes valides.
    """
    mask = pd.Series(True, index=df.index)  # Initialiser le masque à True
    for col in cols:
        mask &= df[col].notna() & df[col].str.strip().astype(bool)  # Mettre à jour le masque
    return mask
