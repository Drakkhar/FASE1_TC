import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from models import Processamento, SessionLocal

base_url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={}&subopcao={}&opcao=opt_03'

# Tipos encontrados via botão
tipos = {
    'subopt_01': 'Viníferas',
    'subopt_02': 'Americanas e híbridas',
    'subopt_03': 'Uvas de mesa',
    'subopt_04': 'Sem classificação'
}

# Obtem anos disponíveis (usando subopt_01 como base)
initial_url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_03'
response = requests.get(initial_url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

# Pega intervalo de anos
range_text = soup.find('label', class_='lbl_pesq').get_text(strip=True)  # Ano: [1970-2023]
match = re.search(r'\[(\d{4})-(\d{4})\]', range_text)
min_year, max_year = int(match.group(1)), int(match.group(2)) if match else (1970, 2023)

#print(f"Raspando PROCESSAMENTO de {min_year} até {max_year}")

# Cria sessão com o banco
db = SessionLocal()

# Raspagem principal
for tipo_id, tipo_nome in tipos.items():
    for ano in range(min_year, max_year + 1):
        url = base_url.format(ano, tipo_id)
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table', {'class': 'tb_base tb_dados'})
        if not table:
            print(f"Tabela não encontrada para {ano} - {tipo_nome}")
            continue

        rows = table.find_all('tr')

        for row in rows[1:]:  # ignora cabeçalho
            cells = row.find_all(['th', 'td'])
            cells_text = [cell.get_text(strip=True) for cell in cells]

            if len(cells_text) >= 2:
                try:
                    quantidade = int(cells_text[1].replace('.', '').replace(',', ''))
                except ValueError:
                    continue

                item = Processamento(
                    ano=ano,
                    tipo=tipo_nome,
                    produto=cells_text[0],
                    quantidade=quantidade
                )
                db.add(item)

db.commit()
db.close()
#print("Raspagem e inserção de PROCESSAMENTO concluídas.")
