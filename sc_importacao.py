import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from models import Importacao, SessionLocal

# Mapeamento dos tipos de importação
TIPOS = {
    "subopt_01": "Vinhos de mesa",
    "subopt_02": "Espumantes",
    "subopt_03": "Uvas frescas",
    "subopt_04": "Uvas passas",
    "subopt_05": "Suco de uva",
}

# URL base com placeholders
URL = "http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao={tipo}&ano={ano}&opcao=opt_05"

# Detecta o intervalo de anos disponível
url_base = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05"
res = requests.get(url_base)
soup = BeautifulSoup(res.text, "html.parser")

range_text = soup.find("label", class_="lbl_pesq").get_text(strip=True)
match = re.search(r"\[(\d{4})-(\d{4})\]", range_text)
min_year, max_year = int(match.group(1)), int(match.group(2)) if match else (1970, 2023)

# Lista final
data = []

for tipo_cod, tipo_nome in TIPOS.items():
    for ano in range(min_year, max_year + 1):
        link = URL.format(tipo=tipo_cod, ano=ano)
        res = requests.get(link)
        soup = BeautifulSoup(res.text, "html.parser")

        table = soup.find("table", class_="tb_base tb_dados")
        if not table:
            print(f"Tabela não encontrada: {tipo_nome} - {ano}")
            continue

        rows = table.find_all("tr")[1:]

        for row in rows:
            cols = [col.get_text(strip=True) for col in row.find_all("td")]
            if len(cols) >= 3:
                try:
                    qtd = int(cols[1].replace(".", "").replace(",", ""))
                except:
                    qtd = 0
                try:
                    val = int(cols[2].replace(".", "").replace(",", ""))
                except:
                    val = 0
                data.append({
                    "ano": ano,
                    "tipo": tipo_nome,
                    "pais": cols[0],
                    "quantidade": qtd,
                    "valor": val
                })

# Salva no banco
df = pd.DataFrame(data)
db = SessionLocal()
for _, row in df.iterrows():
    novo = Importacao(
        ano=row["ano"],
        tipo=row["tipo"],
        pais=row["pais"],
        quantidade=row["quantidade"],
        valor=row["valor"]
    )
    db.add(novo)
db.commit()
db.close()
