# Score de Inadimplência — Sistema ML Fim-a-fim

## O Problema
Prever qual cliente tem maior probabilidade de ficar inadimplente (com base em dados históricos de empréstimos) para otimizar a tomada de crédito e mitigar riscos de calote.

## Resultados Esperados
- **Acurácia / Métricas do Modelo:** Foco em otimização de AUC-ROC no conjunto de teste.
- **Tempo de predição:** < 50ms por cliente via API.
- **Impacto de Negócio:** Segmentar clientes por risco reduz perdas significativas em carteiras de crédito de varejo.

## Arquitetura
1. **Pipeline de treino** (`src/pipeline.py`): Coleta dados brutos (`data/raw/`), executa feature engineering, lida com nulos e treina o modelo de Machine Learning.
2. **API de predição** (`api/main.py`): FastAPI que recebe as características do cliente e retorna o score de risco em tempo real.
3. **Versionamento**: Modelo salvo como artefato (`models/model_v1.pkl`) utilizando `joblib`.
4. **Monitoring** (`monitoring/check_drift.py`): Estrutura para detecção de *data drift* e alertas de retreino.

## Como rodar

```bash
# Setup do Ambiente Virtual e Dependências
python -m venv .venv
# No Windows: .\.venv\Scripts\activate
# No Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt

# Treinamento do Modelo (exemplo)
python src/pipeline.py

# Subir a API de predição
python api/main.py

# Rodar os Testes Automatizados
pytest tests/

# Executar com Docker
docker build -f docker/Dockerfile -t inadimplencia-api:v1 .
docker run -p 8000:8000 inadimplencia-api:v1
```

## Stack
- **ML**: scikit-learn (Random Forest)
- **API**: FastAPI
- **Persistência**: PostgreSQL (pra logs de produção)
- **Deploy**: Docker
- **Versioning**: Git + Model Registry (modelos salvos com métricas)
