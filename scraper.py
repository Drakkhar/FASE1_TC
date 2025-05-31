import requests
from bs4 import BeautifulSoup
import json
from models import (
    SessionLocal, Producao, Processamento,
    Comercializacao, Importacao, Exportacao
)
import re


def get_soup(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')


def producao_rt(ano: int):
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_02"
    soup = get_soup(url)
    table = soup.find('table', {'class': 'tb_base tb_dados'})

    if not table:
        raise ValueError("Tabela de dados não encontrada para o ano informado.")

    rows = table.find_all('tr')

    if len(rows) <= 1:
        raise ValueError("Nenhum dado disponível para o ano informado.")
    
    if ano < 1970 or ano > 2025:
        raise ValueError("Tabela de dados não encontrada para o ano informado.")

    headers = [cell.get_text(strip=True) for cell in rows[0].find_all(['th', 'td'])]
    data = []

    for row in rows[1:]:
        cells = row.find_all(['td', 'th'])
        if len(cells) == len(headers):
            row_data = {headers[i]: cells[i].get_text(strip=True) for i in range(len(headers))}
            data.append(row_data)

    if not data:
        raise ValueError("Ano encontrado, mas sem dados na tabela.")

    return data


def processamento_rt(ano: int, opcao: int):
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_03&subopcao=subopt_0{opcao}"
    soup = get_soup(url)
    table = soup.find('table', {'class': 'tb_base tb_dados'})

    if not table:
        raise ValueError("Tabela de dados não encontrada para o ano informado.")

    rows = table.find_all('tr')

    if len(rows) <= 1:
        raise ValueError("Nenhum dado disponível para o ano informado.")
    
    if ano < 1970 or ano > 2025:
        raise ValueError("Tabela de dados não encontrada para o ano informado.")
    
    if opcao < 1 or opcao > 4:
        raise ValueError("Insira uma opção válida (entre 1 e 4).")

    headers = [cell.get_text(strip=True) for cell in rows[0].find_all(['th', 'td'])]
    data = []

    for row in rows[1:]:
        cells = row.find_all(['td', 'th'])
        if len(cells) == len(headers):
            row_data = {headers[i]: cells[i].get_text(strip=True) for i in range(len(headers))}
            data.append(row_data)

    if not data:
        raise ValueError("Ano encontrado, mas sem dados na tabela.")

    return data


def comercializacao_rt(ano: int):
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_04"
    soup = get_soup(url)
    table = soup.find('table', {'class': 'tb_base tb_dados'})

    if not table:
        raise ValueError("Tabela de dados não encontrada para o ano informado.")

    rows = table.find_all('tr')

    if len(rows) <= 1:
        raise ValueError("Nenhum dado disponível para o ano informado.")
    
    if ano < 1970 or ano > 2025:
        raise ValueError("Tabela de dados não encontrada para o ano informado.")
    
    headers = [cell.get_text(strip=True) for cell in rows[0].find_all(['th', 'td'])]
    data = []

    for row in rows[1:]:
        cells = row.find_all(['td', 'th'])
        if len(cells) == len(headers):
            row_data = {headers[i]: cells[i].get_text(strip=True) for i in range(len(headers))}
            data.append(row_data)

    if not data:
        raise ValueError("Ano encontrado, mas sem dados na tabela.")

    return data

def importacao_rt(ano: int, opcao: int):
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_05&subopcao=subopt_0{opcao}"
    soup = get_soup(url)
    table = soup.find('table', {'class': 'tb_base tb_dados'})

    if not table:
        raise ValueError("Tabela de dados não encontrada para o ano informado.")

    rows = table.find_all('tr')

    if len(rows) <= 1:
        raise ValueError("Nenhum dado disponível para o ano informado.")
    
    if ano < 1970 or ano > 2025:
        raise ValueError("Tabela de dados não encontrada para o ano informado.")
    
    if opcao < 1 or opcao > 5:
        raise ValueError("Insira uma opção válida (entre 1 e 5).")

    headers = [cell.get_text(strip=True) for cell in rows[0].find_all(['th', 'td'])]
    data = []

    for row in rows[1:]:
        cells = row.find_all(['td', 'th'])
        if len(cells) == len(headers):
            row_data = {headers[i]: cells[i].get_text(strip=True) for i in range(len(headers))}
            data.append(row_data)

    if not data:
        raise ValueError("Ano encontrado, mas sem dados na tabela.")

    return data

def exportacao_rt(ano: int, opcao: int):
    url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={ano}&opcao=opt_06&subopcao=subopt_0{opcao}"
    soup = get_soup(url)
    table = soup.find('table', {'class': 'tb_base tb_dados'})

    if not table:
        raise ValueError("Tabela de dados não encontrada para o ano informado.")

    rows = table.find_all('tr')

    if len(rows) <= 1:
        raise ValueError("Nenhum dado disponível para o ano informado.")
    
    if ano < 1970 or ano > 2025:
        raise ValueError("Tabela de dados não encontrada para o ano informado.")
    
    if opcao < 1 or opcao > 4:
        raise ValueError("Insira uma opção válida (entre 1 e 4).")

    headers = [cell.get_text(strip=True) for cell in rows[0].find_all(['th', 'td'])]
    data = []

    for row in rows[1:]:
        cells = row.find_all(['td', 'th'])
        if len(cells) == len(headers):
            row_data = {headers[i]: cells[i].get_text(strip=True) for i in range(len(headers))}
            data.append(row_data)

    if not data:
        raise ValueError("Ano encontrado, mas sem dados na tabela.")

    return data