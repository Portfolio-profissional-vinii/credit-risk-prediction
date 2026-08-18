# 1. Imagem base oficial do Python
from python:3.11-slim

# 2. Definir pasta de trabalho dentro do contêiner
WORKDIR /app

# 3. Copiar arquivo de dependências e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar o restante dos arquivos do projeto para contêiner
COPY . .

# 5. Expor a porta 8000
EXPOSE 8000

# 6. Comando para iniciar a API no contêiner
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]