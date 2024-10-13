
class Filme:
    
    def __init__(self, dic_filme):
        self._imdb_id
        self._nome
        self._ano
        self._diretor
        self._resumo
        self._poster
        self._nota_imdb
        self._nota_rt

    def __str__(self):
        return f"Nome do filme:{self._nome} \n Ano: {self._ano} \n Diretor:{self._diretor} \n \n Resumo \n {self._resumo} \n \n IMDB:{self._nota_imdb} \n Rotten Tomatoes: {self._nota_rt}"
    
