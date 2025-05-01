from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Livro(Base):
    __tablename__ = "Livro"

    isbn = Column(String(13), primary_key=True)
    titulo = Column(String(255), nullable=False)
    autor = Column(String(255), nullable=False)
    ano_publicacao = Column(Integer, nullable=False)
    genero = Column(String(100), nullable=True)