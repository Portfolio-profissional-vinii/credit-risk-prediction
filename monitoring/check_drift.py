import pandas as pd
from scipy.stats import ks_2samp

# 1. Simular os dados de treino (referência)
dados_referencia = [15000, 12000, 18000, 10000, 20000, 15000, 13000]

# 2. Simular os dados de "produção" (clientes novos) pedindo empréstimos muito mais altos
dados_producao = [35000, 42000, 38000, 40000, 45000, 39000, 41000]

# 3. Teste de Kolmogorov-Smirnov (KS) para comparar as distribuições
estatistica, p_valor = ks_2samp(dados_referencia, dados_producao)

print("--- Monitoramento de Data Drift na variável 'loan_amnt' ---")
print(f'P-Valor: {p_valor:.5f}')

if p_valor < 0.05:
    print("❌ Alerta: Data Drift detectado! O perfil dos clientes mudou drasticamente. É hora de reiniciar o modelo.")
else:
    print("✅ Tudo normal. Os dados de produção estão similares aos dados de treinoi.")