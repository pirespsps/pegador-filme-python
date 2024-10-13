
class Filme:
    
    def __init__(self, dic_filme):
        self._imdb_id = dic_filme["imdbID"]
        self._nome = dic_filme["Title"].capitalize()
        self._ano = dic_filme["Year"]
        self._diretor = dic_filme["Director"].capitalize()
        self._resumo = dic_filme["Plot"].capitalize()
        self._poster = dic_filme["Poster"]
        self._nota_imdb = dic_filme["imdbRating"]
        self._nota_rt = self.get_rt(dic_filme["Ratings"])

    def get_rt(self,ratings):
        rt_rating = ratings[1]
        rt_rating = rt_rating["Value"]
        return rt_rating

    def __str__(self):
        return f" \n Nome do filme:{self._nome} \n Ano:{self._ano} \n Diretor:{self._diretor} \n \n Resumo \n {self._resumo} \n \n IMDB:{self._nota_imdb} \n Rotten Tomatoes:{self._nota_rt}"

    @property
    def imdb_id(self):
        return self._imdb_id

    @imdb_id.setter
    def imdb_id(self, value):
        self._imdb_id = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, value):
        self._ano = value

    @property
    def diretor(self):
        return self._diretor

    @diretor.setter
    def diretor(self, value):
        self._diretor = value

    @property
    def resumo(self):
        return self._resumo

    @resumo.setter
    def resumo(self, value):
        self._resumo = value

    @property
    def poster(self):
        return self._poster

    @poster.setter
    def poster(self, value):
        self._poster = value

    @property
    def nota_imdb(self):
        return self._nota_imdb

    @nota_imdb.setter
    def nota_imdb(self, value):
        self._nota_imdb = value

    @property
    def nota_rt(self):
        return self._nota_rt

    @nota_rt.setter
    def nota_rt(self, value):
        self._nota_rt = value