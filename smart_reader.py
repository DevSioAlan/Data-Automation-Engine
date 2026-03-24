"""
Vitrine Technique - Portail Automatisation Data
Extrait : Scanner intelligent d'Excel.
Objectif : Trouver automatiquement le bon onglet et les bons en-têtes via Fuzzy Matching, 
           même si le fichier source est mal formaté.
"""
import pandas as pd

def lire_fichier_intelligent(file_obj, mots_cles):
    """ Scanne tous les onglets d'un Excel et choisit le bon automatiquement basé sur des mots-clés """
    xl = pd.ExcelFile(file_obj)
    meilleur_onglet = xl.sheet_names[0]
    max_score = -1
    
    # Analyse de chaque onglet
    for sheet in xl.sheet_names:
        df_test = xl.parse(sheet, nrows=10) # Test limité aux 10 premières lignes (Performance)
        # Concaténation de l'échantillon pour recherche
        text = " ".join([str(c).upper() for c in df_test.columns]) + " " + " ".join([str(v).upper() for v in df_test.values.flatten()])
        score = sum(1 for mot in mots_cles if mot.upper() in text)
        
        if score > max_score:
            max_score = score
            meilleur_onglet = sheet
            
    return pd.read_excel(file_obj, sheet_name=meilleur_onglet)

def nettoyer_colonnes(df):
    """ Supprime les lignes vides au-dessus du vrai tableau et nettoie les en-têtes """
    df.dropna(how='all', inplace=True)
    cols_str = " ".join([str(c).upper() for c in df.columns])
    mots_cles = ['INDUSTRY', 'SITE ID', 'USER NAME', 'CERTIFICATION NAME']
    
    # Si le header est décalé (ex: rapport généré d'un ERP), on cherche la vraie ligne des titres
    if not any(k in cols_str for k in mots_cles):
        for i, row in df.iterrows():
            row_strs = [str(x).upper() for x in row.values]
            if any(k in x for x in row_strs for k in mots_cles):
                df.columns = row.values
                df = df.iloc[1:].reset_index(drop=True)
                break
                
    df.columns = df.columns.astype(str).str.replace('\n', ' ').str.strip()
    return df
