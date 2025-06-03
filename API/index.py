from fastapi import FastAPI, HTTPException
from models import Base, engine, SessionLocal, Producao, Processamento, Comercializacao, Importacao, Exportacao
from scraper import (
    producao_rt,
    comercializacao_rt,
    processamento_rt,
    importacao_rt,
    exportacao_rt
)

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Vitibrasil Scraper API")

@app.get("/")
def home():
    return {"mensagem": "API do Projeto Tech Challenger - Vitibrasil"}

@app.get( "/producao/{ano}",
        summary="Consultar produção por ano",
        description="Retorna os dados de produção de vinhos, sucos e derivados para o ano informado.",
        response_description="Dados extraídos com sucesso"
        )
def get_producao(ano: int):
    try:
        dados = producao_rt(ano)
        return {"Status": "Consulta realizada com sucesso", "Ano": ano, "Dados Produção": dados}
    except:
        db = SessionLocal()
        dados = db.query(Producao).filter(Producao.ano == ano).all()
        db.close()
        if not dados:
            raise HTTPException(status_code=503, detail="Falha ao acessar o site e dados não encontrados no banco.")
        return {
            "Status": "Site indisponível. Dados do banco.",
            "Ano": ano,
            "Dados Produção": [{"produto": d.produto, "quantidade": d.quantidade} for d in dados]
        }

@app.get("/processamento/{ano}/{opcao}",
            summary="Consultar processamento por ano e item",
            description="Retorna os dados de processamento de uvas para o ano e opção informada.",
            response_description="Dados extraídos com sucesso")
def get_processamento(ano: int, opcao: int):
    try:
        dados = processamento_rt(ano, opcao)
        return {"Status": "Consulta realizada com sucesso", "Ano": ano, "Tipo": opcao, "Dados Processamento": dados}
    except:
        db = SessionLocal()
        dados = db.query(Processamento).filter(Processamento.ano == ano, Processamento.tipo == str(opcao)).all()
        db.close()
        if not dados:
            raise HTTPException(status_code=503, detail="Falha ao acessar o site e dados não encontrados no banco.")
        return {
            "Status": "Site indisponível. Dados do banco.",
            "Ano": ano,
            "Tipo": opcao,
            "Dados Processamento": [{"produto": d.produto, "quantidade": d.quantidade} for d in dados]
        }

@app.get(        "/comercializacao/{ano}",
        summary="Consultar comercialização por ano",
        description="Retorna os dados de comercialização de vinho e derivados para o ano informado.",
        response_description="Dados extraídos com sucesso")
def get_comercializacao(ano: int):
    try:
        dados = comercializacao_rt(ano)
        return {"Status": "Consulta realizada com sucesso", "Ano": ano, "Dados Comercialização": dados}
    except:
        db = SessionLocal()
        dados = db.query(Comercializacao).filter(Comercializacao.ano == ano).all()
        db.close()
        if not dados:
            raise HTTPException(status_code=503, detail="Falha ao acessar o site e dados não encontrados no banco.")
        return {
            "Status": "Site indisponível. Dados do banco.",
            "Ano": ano,
            "Dados Comercialização": [{"produto": d.produto, "quantidade": d.quantidade} for d in dados]
        }

@app.get(        "/importacao/{ano}/{opcao}",
        summary="Consultar importação por ano e item",
        description="Retorna os dados de importação de derivados de uva para o ano e opção informada.",
        response_description="Dados extraídos com sucesso")
def get_importacao(ano: int, opcao: int):
    try:
        dados = importacao_rt(ano, opcao)
        return {"Status": "Consulta realizada com sucesso", "Ano": ano, "Tipo": opcao, "Dados Importação": dados}
    except:
        db = SessionLocal()
        dados = db.query(Importacao).filter(Importacao.ano == ano, Importacao.tipo == str(opcao)).all()
        db.close()
        if not dados:
            raise HTTPException(status_code=503, detail="Falha ao acessar o site e dados não encontrados no banco.")
        return {
            "Status": "Site indisponível. Dados do banco.",
            "Ano": ano,
            "Tipo": opcao,
            "Dados Importação": [{"pais": d.pais, "quantidade": d.quantidade, "valor": d.valor} for d in dados]
        }

@app.get(        "/exportacao/{ano}/{opcao}",
        summary="Consultar exportação por ano e item",
        description="Retorna os dados de exportação de derivados de uva para o ano e opção informada.",
        response_description="Dados extraídos com sucesso")
def get_exportacao(ano: int, opcao: int):
    try:
        dados = exportacao_rt(ano, opcao)
        return {"Status": "Consulta realizada com sucesso", "Ano": ano, "Tipo": opcao, "Dados Exportação": dados}
    except:
        db = SessionLocal()
        dados = db.query(Exportacao).filter(Exportacao.ano == ano, Exportacao.tipo == str(opcao)).all()
        db.close()
        if not dados:
            raise HTTPException(status_code=503, detail="Falha ao acessar o site e dados não encontrados no banco.")
        return {
            "Status": "Site indisponível. Dados do banco.",
            "Ano": ano,
            "Tipo": opcao,
            "Dados Exportação": [{"pais": d.pais, "quantidade": d.quantidade, "valor": d.valor} for d in dados]
        }
