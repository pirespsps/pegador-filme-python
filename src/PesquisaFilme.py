import requests
import Filme

class PesquisaFilme:
    pass

    def __init__(self):
        pass


    def filme_por_nome(self,nome):

        try:
            nome = nome.lower()
            request = requests.get(f"https://www.omdbapi.com/?apikey=59ff0a7e&t={nome}")
        except:
            print("Não foi possível realizar a pesquisa")
        else:
            filme = Filme.Filme(request.json())
            print(filme.__str__())
