# main.py

from fastapi import FastAPI
from models import Base, engine
from scraper import (
    salvar_producao,
    salvar_processamento,
    salvar_comercializacao,
    salvar_importacao,
    salvar_exportacao
)

# Criação do banco e tabelas
Base.metadata.create_all(bind=engine)

# Inicialização da API FastAPI (opcional)
app = FastAPI(title="Vitibrasil Scraper API")

@app.get("/")
def home():
    return {"mensagem": "API do Projeto Tech Challenger - Vitibrasil"}

@app.post("/scrap/producao")
def run_producao():
    salvar_producao()
    return {"status": "Producao salva com sucesso"}

#@app.post("/scrap/processamento")
#def run_processamento():
#    salvar_processamento()
#    return {"status": "Processamento salvo com sucesso"}

#@app.post("/scrap/comercializacao")
#def run_comercializacao():
#    salvar_comercializacao()
#    return {"status": "Comercializacao salva com sucesso"}

#@app.post("/scrap/importacao")
#def run_importacao():
#    salvar_importacao()
#    return {"status": "Importacao salva com sucesso"}

#@app.post("/scrap/exportacao")
#def run_exportacao():
#    salvar_exportacao()
#    return {"status": "Exportacao salva com sucesso"}
