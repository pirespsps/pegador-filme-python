
class Filme:
    
    def __init__(self, dic_filme):
        self._imdb_id = dic_filme["imdbID"]
        self._nome = dic_filme["Title"].capitalize()
        self._ano = dic_filme["Year"].capitalize()
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
    
