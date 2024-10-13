CREATE DATABASE db_filmes;

USE db_filmes;

CREATE TABLE tbFilme(
imdb_id_Filme VARCHAR(20),
nome_Filme VARCHAR(150),
ano_Filme INT,
diretor_Filme VARCHAR(150),
resumo_Filme VARCHAR(255),
poster_Filme VARCHAR(255),
nota_imdb_Filme DOUBLE,
nota_rt_Filme DOUBLE,

CONSTRAINT pk_tbFilme PRIMARY KEY (imdb_id_Filme)
)