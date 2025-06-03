from fastapi import FastAPI, HTTPException
from models import Base, engine
from scraper import (
    producao_rt,
    comercializacao_rt,
    processamento_rt,
    importacao_rt,
    exportacao_rt
)

# Criação do banco e tabelas (executado apenas se o banco estiver vazio)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Vitibrasil Scraper API")

@app.get("/")
def home():
    return {"mensagem": "API do Projeto Tech Challenger - Vitibrasil"}

@app.get("/producao/{ano}")
def get_producao(ano: int):
    try:
        dados = producao_rt(ano)
        return {"status": "ok", "ano": ano, "dados": dados}
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

@app.get("/processamento/{ano}/{opcao}")
def get_processamento(ano: int, opcao: int):
    try:
        dados = processamento_rt(ano, opcao)
        return {"status": "ok", "ano": ano, "tipo": opcao, "dados": dados}
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

@app.get("/comercializacao/{ano}")
def get_comercializacao(ano: int):
    try:
        dados = comercializacao_rt(ano)
        return {"status": "ok", "ano": ano, "dados": dados}
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

@app.get("/importacao/{ano}/{opcao}")
def get_importacao(ano: int, opcao: int):
    try:
        dados = importacao_rt(ano, opcao)
        return {"status": "ok", "ano": ano, "tipo": opcao, "dados": dados}
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

@app.get("/exportacao/{ano}/{opcao}")
def get_exportacao(ano: int, opcao: int):
    try:
        dados = exportacao_rt(ano, opcao)
        return {"status": "ok", "ano": ano, "tipo": opcao, "dados": dados}
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
