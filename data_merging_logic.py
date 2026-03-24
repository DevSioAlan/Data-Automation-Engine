"""
Vitrine Technique - Portail Automatisation Data
Extrait : Logique métier Pandas.
Objectif : Fusionner plusieurs DataFrames et appliquer des conditions métier complexes.
"""
import pandas as pd

def process_business_logic(df_elm, df_master, df_eco):
    # 1. Création de clés de jointure composées
    df_elm['join_key'] = df_elm['Industry Name'].astype(str).str.strip() + df_elm['Industry Process Experience Name'].astype(str).str.strip()
    df_master['join_key'] = df_master['Industry Name'].astype(str).str.strip() + df_master['Industry Process Experience Name'].astype(str).str.strip()

    # 2. Jointure (Vlookup équivalent)
    df_master_unique = df_master.drop_duplicates(subset=['join_key'])
    colonnes_a_ramener = ['join_key', 'Industry ID', 'Industry Process Experience ID']
    
    df_merged = pd.merge(df_elm, df_master_unique[colonnes_a_ramener], on='join_key', how='left')

    # 3. Détection dynamique des colonnes de Site ID (selon les conventions de nommage ERP)
    elm_site_cols = [c for c in df_merged.columns if 'SITE ID' in str(c).upper()]
    site_col = elm_site_cols[0] if elm_site_cols else 'Site Id'
    
    elm_ipe_cols = [c for c in df_merged.columns if 'EXPERIENCE ID' in str(c).upper()]
    ipe_col = elm_ipe_cols[0] if elm_ipe_cols else 'join_key'

    # 4. Vérification d'historique avec conditions métier
    df_merged['check_key'] = df_merged[site_col].astype(str) + df_merged[ipe_col].astype(str)
    
    if df_eco is not None:
        eco_site_cols = [c for c in df_eco.columns if 'SITE ID' in str(c).upper()]
        eco_ipe_cols = [c for c in df_eco.columns if 'IPE ID' in str(c).upper()]
        eco_date_cols = [c for c in df_eco.columns if 'ENDDATE' in str(c).upper()]
        
        df_eco['check_key'] = df_eco[eco_site_cols[0]].astype(str) + df_eco[eco_ipe_cols[0]].astype(str)
        existing = df_eco[df_eco[eco_date_cols[0]].astype(str).str.contains('2100', na=False)]['check_key'].tolist()
        
        # Application du statut via Lambda
        df_merged['STATUS'] = df_merged['check_key'].apply(lambda x: 'Already accredited' if x in existing else 'To be processed')
    else:
        df_merged['STATUS'] = 'To be processed'

    # 5. Attribution des dates d'expiration selon le statut
    df_merged['IPE end date'] = df_merged['STATUS'].apply(lambda x: '2100-12-31' if 'Already' in x else '2027-01-31')

    return df_merged
