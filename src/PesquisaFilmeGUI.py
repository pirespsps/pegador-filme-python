from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.image import AsyncImage
import PesquisaFilme
import FilmeDAO
Config.set('input', 'wm_pen', 'null')
Config.set('input', 'wm_touch', 'null')

class PesquisaFilmeGUI(Screen):

    def __init__(self,**kwargs):
        super(PesquisaFilmeGUI,self).__init__(**kwargs)
        self.layout = None
        self.nome_filme_textfield = None

    def build(self):
        
        self.layout = FloatLayout()

        if len(self.show_last_3()) == 3:
            img1,img2,img3 = self.show_last_3()

            self.layout.add_widget(img1)
            self.layout.add_widget(img2)
            self.layout.add_widget(img3)


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

    def show_last_3(self):
        filme_mngr = FilmeDAO.FilmeDao()
        last3 = filme_mngr.fetch_3()
        lista_display = list()
        if len(last3) == 3:
            x_dist = 0.20
            for filme in last3:
                img = AsyncImage(source = filme[5],
                                size_hint=(None, None),
                                size=(150,300),
                                pos_hint = {'center_x':x_dist,'center_y':0.25})
                lista_display.append(img)
                x_dist += 0.30
        filme_mngr.close()
        return lista_display