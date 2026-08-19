import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

def treinar_e_avaliar(X, y, caminho_modelo: str = 'models/model_v1.pkl'):
    """
    Divide os dados, treina o algoritmo RandomForest, avalia no teste e salva o modelo.
    """
    # Divisão treino/teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Instanciando o modelo
    modelo = RandomForestClassifier(
        n_estimators=100, 
        max_depth=10, 
        random_state=42, 
        n_jobs=-1
    )
    
    # Treino
    modelo.fit(X_train, y_train)
    
    # Avaliação
    y_pred_proba = modelo.predict_proba(X_test)[:, 1]
    auc_roc = roc_auc_score(y_test, y_pred_proba)

    print(f"AUC-ROC no conjunto de teste: {auc_roc:.4f}")

    # Salvar em disco
    joblib.dump(modelo, caminho_modelo)
    print(f"Modelo salvo com sucesso em: {caminho_modelo}")

    return modelo, auc_roc
    