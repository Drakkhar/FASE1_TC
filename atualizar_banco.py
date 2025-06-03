# atualizar_banco.py

from models import SessionLocal, Producao, Processamento, Comercializacao, Importacao, Exportacao
from sc_producao import run as run_producao
from sc_processamento import run as run_processamento
from sc_comercializacao import run as run_comercializacao
from sc_importacao import run as run_importacao
from sc_exportacao import run as run_exportacao

def limpar_banco():
    db = SessionLocal()
    db.query(Producao).delete()
    db.query(Processamento).delete()
    db.query(Comercializacao).delete()
    db.query(Importacao).delete()
    db.query(Exportacao).delete()
    db.commit()
    db.close()

def atualizar_todas_tabelas():
    print("Iniciando atualização do banco...")

    try:
        limpar_banco()
        run_producao()
        run_processamento()
        run_comercializacao()
        run_importacao()
        run_exportacao()
        print("Atualização finalizada com sucesso!")
    except Exception as e:
        print(f"Erro durante a atualização: {e}")

if __name__ == "__main__":
    atualizar_todas_tabelas()
