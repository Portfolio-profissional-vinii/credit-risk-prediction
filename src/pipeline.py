import pandas as pd
from src.features import processar_atributos
from src.model import treinar_e_avaliar

def executar_pipeline():
    print("Iniciando Pipeline de Treinamento de Machine Learning...")
    
    # 1. Carregar dataset
    caminho_dados = 'data/processed/data_cleaned.csv'  # ajuste para o seu arquivo em data/ se necessário
    print(f"Lendo dados de: {caminho_dados}")
    df = pd.read_csv(caminho_dados, low_memory=False)

    # 2. Processar Atributos
    print("Processando atributos (remoção de leakage + encoding)...")
    X, y = processar_atributos(df)

    # 3. Treinar e Salvar
    print("Treinando o modelo...")
    treinar_e_avaliar(X, y, caminho_modelo='models/model_v1.pkl')

    print("Pipeline automatizado concluído com sucesso!")

if __name__ == "__main__":
    executar_pipeline()