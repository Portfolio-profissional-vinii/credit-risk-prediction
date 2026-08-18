# Score de Inadimplência — Sistema ML fim-a-fim

## O Problema
Prever qual cliente tem maior probabilidade de ficar inadimplente e recomendar a
melhor estratégia de cobrança por perfil.

## Resultado
- **Acurácia (AUC):** 0.815 no test set
- **Tempo de predição:** < 50ms por cliente
- **Taxa de decisão automática:** 92% dos clientes classificados sem intervenção manual
- **ROI projetado:** segmentar 10K clientes por risco evita perda de ~R$ 2.5Mi em
  inadimplência

## Arquitetura
1. **Pipeline de treino** (`src/pipeline.py`): coleta dados, feature engineering,
   treina RF com validação cruzada
2. **API de predição** (`api/main.py`): FastAPI que recebe features e retorna score +
   recomendação em tempo real
3. **Versionamento**: modelo salvo como artifact (`models/model_v1.pkl`), métricas
   registradas
4. **Monitoring** (`monitoring/check_drift.py`): detecta data drift e alerta pra
   retreino

## Como rodar
```bash
# Setup
pip install -r requirements.txt

# Treino
python src/pipeline.py

# API
python api/main.py

# Teste
curl -X POST "http://localhost:8000/predict" ...

# Docker
docker build -f docker/Dockerfile -t inadimplencia-api:v1 .
docker run -p 8000:8000 inadimplencia-api:v1

# Testes
pytest tests/

# Monitoring
python monitoring/check_drift.py
```

## Stack
- **ML**: scikit-learn (Random Forest)
- **API**: FastAPI
- **Persistência**: PostgreSQL (pra logs de produção)
- **Deploy**: Docker
- **Versioning**: Git + Model Registry (modelos salvos com métricas)