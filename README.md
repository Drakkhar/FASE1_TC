# Projeto Tech Challenger – Vitibrasil Scraper API

Este projeto consiste em uma API desenvolvida com **FastAPI** que realiza a raspagem de dados do site [Vitibrasil Embrapa](http://vitibrasil.cnpuv.embrapa.br/index.php?subopcao=subopt_01&opcao=opt_06). O objetivo é fornecer acesso em tempo real aos dados de produção, processamento, comercialização, importação e exportação de vinhos e derivados no Brasil, com uma estrutura de fallback para base local (`vitibrasil.db`).

## ![image](https://github.com/user-attachments/assets/08dc21e4-2d2d-46aa-b683-42b3f252bfa7) Tecnologias Utilizadas

- Python
- FastAPI
- SQLAlchemy
- SQLite
- BeautifulSoup4
- Requests
- Pandas
- Uvicorn

## 📁 Estrutura do Projeto

```
.API/
  ├── index.py                # Inicialização da API e rotas
├── models.py              # Modelos do banco de dados
├── scraper.py             # Funções de raspagem em tempo real
├── atualizar_banco.py     # Script para atualizar o banco local
├── sc_producao.py         # Raspagem: Produção
├── sc_processamento.py    # Raspagem: Processamento
├── sc_comercializacao.py  # Raspagem: Comercialização
├── sc_importacao.py       # Raspagem: Importação
├── sc_exportacao.py       # Raspagem: Exportação
├── vitibrasil.db          # Banco de dados local (versão salva do site)
├── requirements.txt       # Dependências do projeto
└── .gitignore             # Exclusões de versionamento
```

## 🚀 Lógica de Funcionamento

- **Raspagem em tempo real**: tentativas de obter dados diretamente do site.
- **Fallback**: se o site estiver fora ou demorar, os dados são retornados do `vitibrasil.db`.
- **Atualização manual**: `atualizar_banco.py` atualiza o banco com base nas raspagens locais.


## ⚙️ Instalação e Execução Local

### Pré-requisitos

- Python 3.10+
- Git

### Passos

 ## 1. Clone o repositório:
   
   ```bash
   git clone https://github.com/Drakkhar/FASE1_TC.git
   cd FASE1_TC
   ```

 ## 2. Crie e ative um ambiente virtual:

  ```bash
  python -m venv venv
  source venv/bin/activate  # No Windows: venv\Scripts\activate
  ```

 ## 3. Instale as dependências:
   
  ```bash
  pip install -r requirements.txt
  ```

 ## 4. Raspagem e atualização dos dados:

  ```bash
  python scraper.py
  python atualizar_banco.py
  ```

 ## 5. Inicie a API:
   
  ```bash
  uvicorn main:app --reload
  ```

Acesse a documentação interativa da API:

http://127.0.0.1:8000/docs

## 🚀 Implantação

O projeto está configurado para ser implantado na plataforma Vercel, utilizando o arquivo vercel.json. Basta conectar o repositório à sua conta Vercel e realizar a primeira implantação.

🤝 Colaboradores

- Pedro Paolielo
- Erick Navevaiko

## Observações

- O banco `vitibrasil.db` está incluso no repositório para uso como backup.
- Evite alterações diretas no banco, utilize os scripts disponíveis.
