from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
import PesquisaFilmeGUI
import FilmeGUI

class ScreenManagerApp(App):

    def build(self):
        sm = ScreenManager()

        tela_busca = PesquisaFilmeGUI.PesquisaFilmeGUI(name = "pesquisa_filme_screen")
        tela_filme = FilmeGUI.FilmeGUI(filme = None, name = "filme_screen")

        sm.add_widget(tela_busca)
        sm.add_widget(tela_filme)

        return sm