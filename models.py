# models.py

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração do banco de dados SQLite
DATABASE_URL = "sqlite:///./vitibrasil.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

# Exemplo de tabela para Produção
class Producao(Base):
    __tablename__ = "producao"

    id = Column(Integer, primary_key=True, index=True)
    ano = Column(Integer, nullable=False)
    estado = Column(String, nullable=False)
    variedade = Column(String, nullable=False)
    quantidade = Column(Float, nullable=False)
    unidade = Column(String, nullable=True)

# Exemplo de tabela para Processamento
class Processamento(Base):
    __tablename__ = "processamento"

    id = Column(Integer, primary_key=True, index=True)
    ano = Column(Integer, nullable=False)
    tipo = Column(String, nullable=False)
    quantidade = Column(Float, nullable=False)
    unidade = Column(String, nullable=True)

# Comercialização
class Comercializacao(Base):
    __tablename__ = "comercializacao"

    id = Column(Integer, primary_key=True, index=True)
    ano = Column(Integer, nullable=False)
    produto = Column(String, nullable=False)
    local = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    unidade = Column(String, nullable=True)

# Importação
class Importacao(Base):
    __tablename__ = "importacao"

    id = Column(Integer, primary_key=True, index=True)
    ano = Column(Integer, nullable=False)
    pais = Column(String, nullable=False)
    produto = Column(String, nullable=False)
    quantidade = Column(Float, nullable=False)
    unidade = Column(String, nullable=True)

# Exportação
class Exportacao(Base):
    __tablename__ = "exportacao"

    id = Column(Integer, primary_key=True, index=True)
    ano = Column(Integer, nullable=False)
    pais = Column(String, nullable=False)
    produto = Column(String, nullable=False)
    quantidade = Column(Float, nullable=False)
    unidade = Column(String, nullable=True)
