import sqlite3
import os

class FilmeDao:
    
    def __init__(self):
        path_pasta = os.path.dirname(os.path.abspath(__file__))
        path_arquivo = os.path.join(path_pasta,'sql3','db_filme.db3')

        if sqlite3.connect(path_arquivo) is None: 
            self.connection = sqlite3.connect(path_arquivo)
            self.cursor = self.connection.cursor()           
            self.cursor.execute("CREATE TABLE tbFilme(imdb_id_Filme TEXT,nome_Filme TEXT,ano_Filme INT,diretor_Filme TEXT,resumo_Filme TEXT,poster_Filme TEXT,nota_imdb_Filme REAL,nota_rt_Filme REAL,CONSTRAINT pk_tbFilme PRIMARY KEY (imdb_id_Filme));")
            self.connection.commit()
        else:
            self.connection = sqlite3.connect(path_arquivo)
            self.cursor = self.connection.cursor()

    def create(self,filme):
        if not self.filme_existe(filme.imdb_id):
            data = (filme.imdb_id, filme.nome, filme.ano, filme.diretor,filme.resumo, filme.poster, filme.nota_imdb, filme.nota_rt)
            self.cursor.execute("INSERT INTO tbFilme (imdb_id_Filme,nome_Filme,ano_Filme,diretor_Filme,resumo_Filme,poster_Filme,nota_imdb_Filme,nota_rt_Filme) VALUES (?,?,?,?,?,?,?,?)",data)
        self.connection.commit()

    def list_all(self): 
        self.cursor.execute("SELECT * FROM tbFilme")
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def fetch_3(self):
        lista = self.list_all()

        if len(lista) >= 3:
            lista.reverse()
            last3 = lista[0],lista[1],lista[2]
            return last3
        

    def filme_existe(self, imdb_id):
        self.cursor.execute("SELECT imdb_id_Filme FROM tbFilme WHERE imdb_id_Filme = ?", (imdb_id,))
        return self.cursor.fetchone() is not None