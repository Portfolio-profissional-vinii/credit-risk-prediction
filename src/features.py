import pandas as pd

LEAKAGE_COLUMNS = [
    'id', 'member_id', 'issue_d', 'loan_status', 'pymnt_plan', 
    'url', 'desc', 'title', 'zip_code', 'addr_state',
    'out_prncp', 'out_prncp_inv', 'total_pymnt', 'total_pymnt_inv',
    'total_rec_prncp', 'total_rec_int', 'total_rec_late_fee',
    'recoveries', 'collection_recovery_fee', 'last_pymnt_d',
    'last_pymnt_amnt', 'next_pymnt_d', 'last_credit_pull_d',
    'target', 'inadimplente', 'last_fico_range_low', 'last_fico_range_high'
]

def processar_atributos(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """
    Limpa o dataset, remove colunas de vazamento de dados,
    define a variável alvo (target) e aplica One-Hot Encoding.
    """
    df_clean = df.copy()

    # 1. Definir o Target (1 para Inadimplente, 0 para Quitado)
    if 'target' in df_clean.columns:
        target = df_clean['target']
    elif 'loan_status' in df_clean.columns:
        target = df_clean['loan_status'].apply(
            lambda x: 1 if str(x) in ['Charged Off', 'Default', 'Late (31-120 days)'] else 0
        )
    elif 'inadimplente' in df_clean.columns:
        target = df_clean['inadimplente']
    else:
        raise ValueError("Nenhuma coluna de alvo (target/loan_status/inadimplente) foi encontrada.")

    # 2. Remover colunas de vazamento de dados e o próprio alvo do X
    colunas_para_remover = [col for col in LEAKAGE_COLUMNS if col in df_clean.columns]
    df_clean = df_clean.drop(columns=colunas_para_remover)

    # 3. Preencher valores nulos em colunas numéricas com 0
    num_cols = df_clean.select_dtypes(include=['float64', 'int64']).columns
    df_clean[num_cols] = df_clean[num_cols].fillna(0)

    # 4. One-Hot Encoding em variáveis categóricas
    cat_cols = df_clean.select_dtypes(include=['object', 'category']).columns
    df_clean = pd.get_dummies(df_clean, columns=cat_cols, drop_first=True)

    return df_clean, target