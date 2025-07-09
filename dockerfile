# Usa uma imagem oficial do Python como base
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código do projeto
COPY . .

# Expõe a porta que o Flask irá rodar (ajuste se necessário)
EXPOSE 5000

# Define a variável de ambiente para produção
ENV FLASK_ENV=production

# Comando para rodar a aplicação (ajuste se necessário)
CMD ["python", "app.py"]