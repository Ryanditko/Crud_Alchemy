# %%
# imports
import os

import dotenv
import pandas as pd
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

dotenv.load_dotenv()
# %%
# classes
Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True,autoincrement=False)
    name = Column(String(255), nullable=False)

class Book(Base):
    __tablename__ = 'books'

    isbn = Column(String(20), primary_key=True)
    title = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))

# %%
# Parâmetros de conexão com o banco de dados
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")
host = os.getenv("HOST")
banco_de_dados = os.getenv("BANCO_DE_DADOS")
url = f"mssql+pyodbc://{usuario}:{senha}@{host}/{banco_de_dados}?driver=ODBC+Driver+17+for+SQL+Server"

# %%
# Conexão com o banco de dados
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

# %%
# Criar instâncias de Author
author1 = Author(id=1, name="Ariano Suassuna")
author2 = Author(id=2, name="Jorge Amado")
# %%
# Adicionar os autores ao banco
session.add(author1)
session.add(author2)
session.commit()
# %%
# Verificar os IDs gerados automaticamente
print(f"Autor 1 ID: {author1.id}, Autor 2 ID: {author2.id}")

# %%
# Criar instâncias de Book associadas aos autores
book1 = Book(isbn="978-8520938393", title="Auto da Compadecida", author_id=author1.id)
book2 = Book(isbn="978-8535914061", title="Capitães da Areia", author_id=author2.id)

# %%
# Adicionar os livros ao banco
session.add_all([book1, book2])
session.commit()
# %%
# Buscar um autor (retorno como objeto)
author = session.query(Author).filter_by(name="Ariano Suassuna").first()
print(f"Autor: {author.name}")

# %%
# Buscar todos os livros (retorno como objeto)
books = session.query(Book).all()
for book in books:
    print(f"ISBN: {book.isbn}, Título: {book.title}, Autor ID: {book.author_id}")

# %%
# Buscar todos os autores e converter para DataFrame
authors = session.query(Author).all()
authors_data = [{"ID": author.id, "Nome": author.name} for author in authors]
authors_df = pd.DataFrame(authors_data)
print("Autores:")
print(authors_df)

# %%
# Buscar todos os livros e converter para DataFrame
books = session.query(Book).all()
books_data = [
    {"ISBN": book.isbn, "Título": book.title, "Autor ID": book.author_id}
    for book in books
]
books_df = pd.DataFrame(books_data)
print("\nLivros:")
print(books_df)