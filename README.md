Projeto CRUD com SQLAlchemy e MSSQL

Este projeto foi desenvolvido para demonstrar operações CRUD (Create, Read, Update, Delete) em um banco de dados MSSQL usando a biblioteca SQLAlchemy em Python.

Estrutura do Projeto:
- `main.py`: Este arquivo contém o código principal do projeto. Ele estabelece a conexão com o banco de dados, cria uma sessão e demonstra as operações CRUD em um modelo de dados de Livro.

- `crud.py`: Este arquivo contém a classe `CRUD` que encapsula as operações CRUD em um objeto de sessão SQLAlchemy.

- `script.sql`: Este arquivo contém o script SQL para criar a tabela Livro no banco de dados.

- `alchemy.txt`: Este arquivo contém a descrição do projeto.

Operações CRUD:
- `create`: Cria um novo registro de Livro no banco de dados.
- `read`: Lê um registro de Livro do banco de dados com base no ISBN.
- `update`: Atualiza um registro de Livro no banco de dados com base no ISBN.
- `delete`: Exclui um registro de Livro do banco de dados com base no ISBN.

Para executar o projeto, é necessário ter um banco de dados MSSQL configurado e as credenciais de acesso configuradas no arquivo `.env`.

Para instalar as dependências do projeto, execute `pip install -r requirements.txt`.

Para executar o projeto, execute `python main.py`.
