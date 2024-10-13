import sqlite3
import Filme

connection = sqlite3.connect('db_filmes')
cursor = connection.cursor()

cursor.execute("CREATE TABLE tbFilme(imdb_id_Filme TEXT,nome_Filme TEXT,ano_Filme INT,diretor_Filme TEXT,resumo_Filme TEXT,poster_Filme TEXT,nota_imdb_Filme DOUBLE,nota_rt_Filme DOUBLE,CONSTRAINT pk_tbFilme PRIMARY KEY (imdb_id_Filme))")

def create(filme):

    cursor.executemany("INSERT INTO db_filmes (imdb_id_Filme,nome_Filme,ano_Filme,diretor_Filme,resumo_Filme,poster_Filme,nota_imdb_Filme,nota_rt_Filme) VALUES (?,?,?,?,?,?,?,?)",data)
    connection.commit()