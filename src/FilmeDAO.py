import sqlite3
import os

class FilmeDao:
    
    def __init__(self):
        db_path = '../db_filme'

        if not os.path.isfile(db_path): 
            self.connection = sqlite3.connect(db_path)
            self.cursor = self.connection.cursor()           
            self.cursor.execute("CREATE TABLE tbFilme(imdb_id_Filme TEXT,nome_Filme TEXT,ano_Filme INT,diretor_Filme TEXT,resumo_Filme TEXT,poster_Filme TEXT,nota_imdb_Filme DOUBLE,nota_rt_Filme DOUBLE,CONSTRAINT pk_tbFilme PRIMARY KEY (imdb_id_Filme))")
            self.connection.commit()
        else:
            self.connection = sqlite3.connect(db_path)
            self.cursor = self.connection.cursor()

    def create(self,filme):
        data = (filme.imdb_id, filme.nome, filme.ano, filme.diretor,filme.resumo, filme.poster, filme.nota_imdb, filme.nota_rt)
        
        if filme.imdb_id not in self.get_imdb_id():
            self.cursor.execute("INSERT INTO tbFilme (imdb_id_Filme,nome_Filme,ano_Filme,diretor_Filme,resumo_Filme,poster_Filme,nota_imdb_Filme,nota_rt_Filme) VALUES (?,?,?,?,?,?,?,?)",data)
        self.connection.commit()

    def list_all(self): 
        self.cursor.execute("SELECT * FROM tbFilme")
        return self.cursor.fetchall()

    def get_imdb_id(self):
        self.cursor.execute("SELECT imdb_id_Filme FROM tbFilme")
        lista = []
        for var in self.cursor.fetchall():
            lista.append(str(var))
        return lista

    def close(self):
        self.cursor.close()
        self.connection.close()