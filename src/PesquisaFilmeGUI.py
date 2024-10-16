from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.config import Config
import PesquisaFilme
Config.set('input', 'wm_pen', 'null')
Config.set('input', 'wm_touch', 'null')

class PesquisaFilmeGUI(Screen):

    def __init__(self,**kwargs):
        super(PesquisaFilmeGUI,self).__init__(**kwargs)
        self.layout = None
        self.nome_filme_textfield = None

    def build(self):
        
        self.layout = FloatLayout()

        label = Label(text = "Digite o nome de um filme",
                       size_hint = (.5,.5),
                        pos_hint = {'center_x':.5,'center_y':0.8},
                        font_size = '30sp')
        self.layout.add_widget(label)

        self.nome_filme_textfield = TextInput(size_hint = (None,None),
                                         pos_hint = {'center_x':.5,'center_y':0.65},
                                         size = (300,40), 
                                         multiline = False,
                                         on_text_validate = self.search_filme)


        self.layout.add_widget(self.nome_filme_textfield)
        
        self.clear_widgets()
        self.add_widget(self.layout)


    def on_pre_enter(self):
        self.build()
    
    def search_filme(self,instance):
         filme_nome = self.nome_filme_textfield.text
         filme = PesquisaFilme.PesquisaFilme().filme_por_nome(filme_nome)
         self.manager.get_screen('filme_screen').filme = filme
         self.manager.current = 'filme_screen'

    