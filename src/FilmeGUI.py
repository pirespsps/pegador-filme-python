from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class FilmeGUI(Screen):

    def __init__(self, filme,**kwargs):
        super(FilmeGUI, self).__init__(**kwargs)
        self.filme = filme
        self.layout = None

    def build(self):
        self.layout = FloatLayout()

        
        img = self.get_poster()
        self.layout.add_widget(img)

        label = Label(text=self.filme.__str__(),
                      size_hint=(None, None), #tam em % definido como none - deixa "livre"
                      size = (300,40),  #define tamanho
                      pos_hint={'center_x': 0.5, 'center_y': 0.5}, #posicao  
                      halign='left',  #alinhamento H label
                      valign='middle', #alinhamento V label
                      text_size=(350, None)) #tamanho do texto (corta se passar e manda pra outra linha)
        self.layout.add_widget(label)

        button = Button(text="Voltar",
                        size_hint=(None,None),
                        size=(200,40),
                        pos_hint={'center_x':0.5,'center_y':0.1},
                        on_release=self.button_function)
        
        self.layout.add_widget(button)

        self.clear_widgets()
        self.add_widget(self.layout)

    def on_pre_enter(self):
        self.build()

    def button_function(self,botao):
        self.manager.current = "pesquisa_filme_screen"

    def get_poster(self):
        img = AsyncImage(source=self.filme.poster,size_hint=(0.25, 1), width=200)  
        return img
    
    @property
    def getFilme(self):
        return self.filme