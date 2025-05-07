import pandas as pd
from relacoes import Livro
from sqlalchemy.orm import Session
from sqlalchemy import update

class CRUD:
    def __init__(self, session: Session):
        self.__session = session

    def create(self, isbn, titulo, autor, ano_publicacao, genero=None):
        # TODO: recebe os parâmetros do livro e cria o registro no banco de dados
        novo_livro = Livro (
            isbn = isbn,
            titulo = titulo, 
            autor = autor,
            ano_publicacao = ano_publicacao, 
            genero = genero, 
        
        )
        
        self.__session.add(novo_livro)
        self.__session.commit()


    def read(self, isbn=None):
        # TODO: retorna um livro específico pelo ISBN
        if isbn:
            # Consulta não é executada até chamar .first() (ou .all(), .one(), etc.)
            # Lazy evaluation: A construção da query é separada da execução
            return self.__session.query(Livro).filter(Livro.isbn == isbn).first()
        # .filter(...) → adiciona condições (WHERE no SQL)
        # session.query(Livro) → seleciona a tabela Livro
        else: 
            return self.__session.query(Livro)
        ''' O método .all() no SQLAlchemy é usado para executar a consulta 
            e retornar todos os resultados como uma lista. ''' 
    def update(self, isbn, titulo=None, autor=None, ano_publicacao=None, genero=None):
        # TODO: atualiza os valores dos parâmetros de um livro específico pelo ISBN
        livro = self.__session.query(Livro).filter_by(isbn=isbn).first()
        if titulo:
            livro.titulo = titulo

        if autor:
            livro.autor = autor

        if ano_publicacao:
            livro.ano_publicacao = ano_publicacao

        if genero:
            livro.genero = genero


        self.__session.commit()
        return livro
        
    def delete(self, isbn):
        # TODO: delete um livro específico pelo ISBN
        livro = self.__session.query(Livro).filter(Livro.isbn == isbn).first()
        if not livro:
            return False 
            
        self.__session.delete(livro)
        self.__session.commit()
        return True
    # O método .all() no SQLAlchemy é usado para executar a consulta e retornar todos os resultados como uma lista.