CREATE TABLE Livro (
    isbn  VARCHAR(13) PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    ano_publicacao INT NOT NULL CHECK (ano_publicacao > 0),
    genero VARCHAR(100)
);

