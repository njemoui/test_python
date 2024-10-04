import pandas as pd

def impute_id(df, col_name, id_type):
    """Imputer les ID manquants dans une colonne spécifiée d'un DataFrame.

    Args:
        df (pd.DataFrame): Le DataFrame à modifier.
        col_name (str): Le nom de la colonne contenant les ID.
        id_type (type): Le type attendu des ID ('int' ou 'str').

    Returns:
        pd.DataFrame: Le DataFrame avec les ID imputés.
    
    Raises:
        ValueError: Si le type d'ID n'est ni 'int' ni 'str'.
    """
    if id_type is int:
        # Convertir la colonne en numérique, en remplaçant les erreurs par NaN
        df[col_name] = pd.to_numeric(df[col_name], errors='coerce')
        
        # Déterminer le maximum des ID dans la colonne, en commençant à 0 si aucun ID n'existe
        max_id = df[col_name].max() if df[col_name].notnull().any() else 0
        counter = max_id + 1
        
        # Imputer les ID manquants avec des entiers consécutifs
        for index in df[df[col_name].isnull()].index:
            df.at[index, col_name] = counter
            counter += 1
        
        df[col_name] = df[col_name].astype(int)
        return df

    elif id_type is str:
        # Imputer les ID manquants avec une chaîne formatée
        for index in df.index:
            if pd.isna(df.at[index, col_name]):
                df.at[index, col_name] = f'NAN{"0" * (8 - len(str(index)))}{index}'
        return df

    else:
        raise ValueError("Type d'ID non pris en charge, utilisez 'int' ou 'str'.")

def column_date_format(df, column_name, date_format):
    """Convertir une colonne spécifiée d'un DataFrame en chaîne de date formatée.

    Args:
        df (pd.DataFrame): Le DataFrame contenant la colonne de dates.
        column_name (str): Le nom de la colonne à convertir.
        date_format (str): Le format de date souhaité (par exemple, '%d/%m/%Y').

    Returns:
        pd.DataFrame: Le DataFrame avec la colonne de dates formatée.
    """
    # Convertir la colonne en datetime, en gérant les formats mixtes
    df[column_name] = pd.to_datetime(df[column_name], format='mixed', errors='coerce')
    
    # Formatter la colonne datetime selon le format spécifié
    df[column_name] = df[column_name].dt.strftime(date_format)
    return df
