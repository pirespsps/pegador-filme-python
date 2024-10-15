
class Filme:
    
    def __init__(self, dic_filme):
        self._imdb_id = dic_filme["imdbID"]
        self._nome = " ".join(dic_filme["Title"].split()).capitalize()
        self._ano = dic_filme["Year"].strip()  
        self._diretor = " ".join(dic_filme["Director"].split()).capitalize()  
        self._resumo = " ".join(dic_filme["Plot"].split()).capitalize()  
        self._poster = dic_filme["Poster"].strip()  
        self._nota_imdb = dic_filme["imdbRating"].strip()  
        self._nota_rt = self.get_rt(dic_filme["Ratings"])

    def get_rt(self,ratings):
        rt_rating = None
        try:
            rt_rating = ratings[1]
            rt_rating = rt_rating["Value"]
        except:
            pass

        return rt_rating

    def __str__(self):
        return f" \n Nome:{self._nome} \n Ano:{self._ano} \n Diretor:{self._diretor} \n \n Resumo \n {self._resumo} \n \n IMDB:{self._nota_imdb} \n Rotten Tomatoes:{self._nota_rt}"

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