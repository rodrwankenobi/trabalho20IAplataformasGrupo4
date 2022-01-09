FROM python:3.7
# copia o diretório da aplicaçao para o container
COPY ./app /app
WORKDIR /app
# Instalação de pacotes do python
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
# Faz o treinamento do modelo
RUN python /app/localdev/training/treina.py
# comando de entrada quando o container for criado
ENTRYPOINT ["python", "/app/localdev/serving/serving.py"]