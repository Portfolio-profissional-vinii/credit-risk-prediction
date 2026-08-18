from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Credit Scoring API")

# Carregar o modelo treinado
modelo = joblib.load('models/model_v1.pkl')

# 1. Definir o esquema dos dados recebidos
class ClienteInput(BaseModel):
    loan_amnt: float
    int_rate: float
    annual_inc: float
    dti: float

# 2. Rota de teste
@app.get("/")
def home():
    return {"status": "API Operacional","modelo":"v1"}

# 3. Rota dedicada para predição
@app.post("/predict")
def predict(dados: ClienteInput):
    #Converter o JSON recebio em DataFrame
    df_input = pd.DataFrame([dados.model_dump()])

    #Preencher automaticamente as colunas faltantes do One-Hot Enconding em 0
    df_input = df_input.reindex(columns=modelo.feature_names_in_, fill_value=0)

    # Calcular a probabilidade de inadimplência
    probabilidade = float(modelo.predict_proba(df_input)[0,1])
    decisao = "Reprovado" if probabilidade > 0.40 else "Aprovado"

    return {
        "probabilidade_inadimplencia": round(probabilidade, 4),
        "recomendacao": decisao
    }