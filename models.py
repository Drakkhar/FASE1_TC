from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração do banco de dados SQLite
DATABASE_URL = "sqlite:///./vitibrasil.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

#Producao
class Producao(Base):
    __tablename__ = "producao"

    id = Column(Integer, primary_key=True, index=True)
    ano = Column(Integer, nullable=False)
    produto = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)

#Processamento
class Processamento(Base):
    __tablename__ = "processamento"

    id = Column(Integer, primary_key=True, index=True)
    ano = Column(Integer, nullable=False)
    tipo = Column(String, nullable=False)
    produto = Column(String, nullable=False)    
    quantidade = Column(Integer, nullable=False)

# Comercialização
class Comercializacao(Base):
    __tablename__ = "comercializacao"

    id = Column(Integer, primary_key=True, index=True)
    ano = Column(Integer, nullable=False)
    produto = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)


## Importação
class Importacao(Base):
    __tablename__ = "importacao"

    id = Column(Integer, primary_key=True, index=True)
    ano = Column(Integer, nullable=False)
    tipo = Column(String, nullable=False)
    pais = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)
    valor = Column(Integer, nullable=False)

## Exportação
class Exportacao(Base):
    __tablename__ = "exportacao"

    id = Column(Integer, primary_key=True, index=True)
    ano = Column(Integer, nullable=False)
    tipo = Column(String, nullable=False)
    pais = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)
    valor = Column(Integer, nullable=False)