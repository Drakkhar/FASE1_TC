import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from models import Comercializacao, SessionLocal, Base, engine
base_url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={}&opcao=opt_04'

# 1. Obter os anos disponíveis a partir da página inicial
initial_url = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04'
response = requests.get(initial_url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')

# Extrai o range de anos da label
range_text = soup.find('label', class_='lbl_pesq').get_text(strip=True)  # Ex: "Ano: [1970-2023]"
match = re.search(r'\[(\d{4})-(\d{4})\]', range_text)
min_year, max_year = int(match.group(1)), int(match.group(2)) if match else (1970, 2023)

#print(f"Raspando dados de {min_year} até {max_year}")

# 2. Raspagem ano a ano
data = []

for ano in range(min_year, max_year + 1):
    #print(f"Ano: {ano}")
    url = base_url.format(ano)
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontra a tabela
    table = soup.find('table', {'class': 'tb_base tb_dados'})
    if not table:
        print(f"Tabela não encontrada para {ano}")
        continue

    rows = table.find_all('tr')

    for row in rows[1:]:  # Pula o cabeçalho
        cells = row.find_all(['th', 'td'])
        cells_text = [cell.get_text(strip=True) for cell in cells]

        if len(cells_text) >= 2:
            data.append({
                'ano': ano,
                'produto': cells_text[0],
                'quantidade': cells_text[1]
            })

df = pd.DataFrame(data)

db = SessionLocal()

for _, row in df.iterrows():
    try:
        quantidade = int(str(row['quantidade']).replace('.', '').replace(',', ''))
    except ValueError:
        continue  # pula se não for número válido

    nova_linha = Comercializacao(
        ano=int(row['ano']),
        produto=row['produto'],
        quantidade=quantidade
    )
    db.add(nova_linha)
db.commit()
db.close()