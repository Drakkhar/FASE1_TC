import requests
from bs4 import BeautifulSoup
from models import (
    SessionLocal, Producao, Processamento,
    Comercializacao, Importacao, Exportacao
)


def get_soup(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'html.parser')


def salvar_producao():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02"
    soup = get_soup(url)
    table = soup.find_all("table")[1]
    linhas = table.find_all("tr")[2:]

    db = SessionLocal()
    for linha in linhas:
        colunas = linha.find_all("td")
        if len(colunas) == 5:
            ano = int(colunas[0].text.strip())
            produto_macro = colunas[1].text.strip()
            produto_micro = colunas[2].text.strip()
            quantidade = int(float(colunas[3].text.strip().replace(".", "").replace(",", ".")))
            db.add(Producao(
                ano=ano,
                produto_macro=produto_macro,
                produto_micro=produto_micro,
                quantidade=quantidade
            ))
    db.commit()
    db.close()


def salvar_processamento():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03"
    soup = get_soup(url)
    table = soup.find_all("table")[1]
    linhas = table.find_all("tr")[2:]

    db = SessionLocal()
    for linha in linhas:
        colunas = linha.find_all("td")
        if len(colunas) == 5:
            ano = int(colunas[0].text.strip())
            tipo = colunas[1].text.strip()
            produto_macro = colunas[2].text.strip()
            produto_micro = colunas[3].text.strip()
            quantidade = int(float(colunas[4].text.strip().replace(".", "").replace(",", ".")))
            db.add(Processamento(
                ano=ano,
                tipo=tipo,
                produto_macro=produto_macro,
                produto_micro=produto_micro,
                quantidade=quantidade
            ))
    db.commit()
    db.close()


def salvar_comercializacao():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04"
    soup = get_soup(url)
    table = soup.find_all("table")[1]
    linhas = table.find_all("tr")[2:]

    db = SessionLocal()
    for linha in linhas:
        colunas = linha.find_all("td")
        if len(colunas) == 4:
            ano = int(colunas[0].text.strip())
            produto_macro = colunas[1].text.strip()
            produto_micro = colunas[2].text.strip()
            quantidade = int(float(colunas[3].text.strip().replace(".", "").replace(",", ".")))
            db.add(Comercializacao(
                ano=ano,
                produto_macro=produto_macro,
                produto_micro=produto_micro,
                quantidade=quantidade
            ))
    db.commit()
    db.close()


def salvar_exportacao():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06"
    soup = get_soup(url)
    table = soup.find_all("table")[1]
    linhas = table.find_all("tr")[2:]

    db = SessionLocal()
    for linha in linhas:
        colunas = linha.find_all("td")
        if len(colunas) == 5:
            ano = int(colunas[0].text.strip())
            tipo = colunas[1].text.strip()
            pais = colunas[2].text.strip()
            quantidade = int(float(colunas[3].text.strip().replace(".", "").replace(",", ".")))
            valor = int(float(colunas[4].text.strip().replace(".", "").replace(",", ".")))
            db.add(Exportacao(
                ano=ano,
                tipo=tipo,
                pais=pais,
                quantidade=quantidade,
                valor=valor
            ))
    db.commit()
    db.close()


def salvar_importacao():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05"
    soup = get_soup(url)
    table = soup.find_all("table")[1]
    linhas = table.find_all("tr")[2:]

    db = SessionLocal()
    for linha in linhas:
        colunas = linha.find_all("td")
        if len(colunas) == 5:
            ano = int(colunas[0].text.strip())
            tipo = colunas[1].text.strip()
            pais = colunas[2].text.strip()
            quantidade = int(float(colunas[3].text.strip().replace(".", "").replace(",", ".")))
            valor = int(float(colunas[4].text.strip().replace(".", "").replace(",", ".")))
            db.add(Importacao(
                ano=ano,
                tipo=tipo,
                pais=pais,
                quantidade=quantidade,
                valor=valor
            ))
    db.commit()
    db.close()
