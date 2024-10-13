import PesquisaFilme
import FilmeDAO

class Main:

    def __init__(self):
        self.pegador_filme = PesquisaFilme.PesquisaFilme()

    def main(self):
        nomefilme = input("Digite o nome do filme a ser procurado \n")
        self.pegador_filme.filme_por_nome(nomefilme)


if __name__ == '__main__':
        iniciar = Main()
        iniciar.main()
    