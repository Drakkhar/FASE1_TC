# main.py

from fastapi import FastAPI, HTTPException
from models import Base, engine
from scraper import (
    producao_rt,
    comercializacao_rt,
    processamento_rt,
    importacao_rt,
    exportacao_rt
)

# Criação do banco e tabelas
Base.metadata.create_all(bind=engine)

# Inicialização da API FastAPI (opcional)
app = FastAPI(title="Vitibrasil Scraper API")

@app.get("/")
def home():
    return {"mensagem": "API do Projeto Tech Challenger - Vitibrasil"}

# Rota GET para consulta dos dados de Produção
@app.get("/producao/{ano}")
def get_producao(ano: int):
    try:
        dados = producao_rt(ano)
        return {"Status": "Consulta realizada com sucesso", "Ano": ano, "Dados Produção": dados}
    except ValueError as ve:
        raise HTTPException(status_code=404, Erro=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, Erro=f"Erro interno: {str(e)}")

# Rota GET para consulta dos dados de Processamento    
@app.get("/processamento/{ano}/{opcao}")
def get_processamento(ano: int, opcao: int):
    try:
        dados = processamento_rt(ano, opcao)
        return {"Status": "Consulta realizada com sucesso", "Ano": ano, "Tipo": opcao, "Dados Processamento": dados}
    except ValueError as ve:
        raise HTTPException(status_code=404, Erro=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, Erro=f"Erro interno: {str(e)}")        


# Rota GET para consulta dos dados de Comercialização    
@app.get("/comercializacao/{ano}")
def get_comercializacao(ano: int):
    try:
        dados = comercializacao_rt(ano)
        return {"Status": "Consulta realizada com sucesso", "Ano": ano, "Dados Comercialização": dados}
    except ValueError as ve:
        raise HTTPException(status_code=404, Erro=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, Erro=f"Erro interno: {str(e)}")
    
# Rota GET para consulta dos dados de Importação    
@app.get("/importacao/{ano}/{opcao}")
def get_importacao(ano: int, opcao: int):
    try:
        dados = importacao_rt(ano, opcao)
        return {"Status": "Consulta realizada com sucesso", "Ano": ano, "Tipo": opcao, "Dados Processamento": dados}
    except ValueError as ve:
        raise HTTPException(status_code=404, Erro=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, Erro=f"Erro interno: {str(e)}")       

# Rota GET para consulta dos dados de Processamento    
@app.get("/exportacao/{ano}/{opcao}")
def get_exportacao(ano: int, opcao: int):
    try:
        dados = exportacao_rt(ano, opcao)
        return {"Status": "Consulta realizada com sucesso", "Ano": ano, "Tipo": opcao, "Dados Exportação": dados}
    except ValueError as ve:
        raise HTTPException(status_code=404, Erro=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, Erro=f"Erro interno: {str(e)}")           

#@app.post("/scrap/processamento")
#def run_processamento():c
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
